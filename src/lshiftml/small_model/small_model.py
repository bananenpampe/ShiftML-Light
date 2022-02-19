from ase.io import read, write
from rascal.neighbourlist.structure_manager import mask_center_atoms_by_species
from rascal.representations import SphericalInvariants as SOAP
from feature_utils.parallel import get_features_in_parallel
import json 
from joblib import load
import numpy as np
from copy import deepcopy
from pathlib import Path

model_fitted_for_species = set([1,6,7,8,16])


def load_frames(READPATH):
    frames = read(READPATH,format="extxyz",index=":")
    for frame in frames: frame.wrap(eps=1e-12)
    for frame in frames: frame.arrays.pop("center_atoms_mask",None)
    return frames


def small_model(READPATH,WRITEPATH,fit_species=None,nthreads=-1,prop_string="cs_iso"):
    
    trajframes =  load_frames(READPATH)  
   
    if len(trajframes) == 0:
        print("empty frames")
        return
    
    if prop_string in trajframes[0].arrays.keys():
        print("{} property already written".format(prop_string))
        return
    
    species_indices = [frame.numbers for frame in trajframes]
    
    if not np.all(species_indices == trajframes[0].numbers):
        print("ordering or length has changed of frames")
        return
    
    species_indices = np.concatenate([frame.numbers for frame in trajframes])
    shifts = np.full(species_indices.shape, np.NaN)
    species = set(np.unique(species_indices))
    
    
    
    if not species.issubset(model_fitted_for_species):
        print("sorry, model has only been fitted for H,C,N,O and S containing structures")
        return
    
    if fit_species is None:
        fit_species = list(species)
        
    if not set(fit_species).issubset(species):
        print("species not contained in structures")
        return
    
    
    for specie in fit_species:
        fit_frames = deepcopy(trajframes)

        for frame in fit_frames: mask_center_atoms_by_species(frame,[int(specie)]) 

        
        path_hyp = Path(__file__).parent.parent.parent.parent / "./data/RR_this_work_models/hypers/{}_hypers.json".format(specie)
        path_model =  Path(__file__).parent.parent.parent.parent / "./data/RR_this_work_models/{}_RR.joblib".format(specie)
        
        with open(path_hyp) as f:
            hypers = json.load(f)
        
        
        model = load(path_model)
        Xpredict = get_features_in_parallel(fit_frames,SOAP,hypers,n_cores=nthreads)

        Ypred = model.predict(Xpredict)
        shifts[species_indices==specie] = Ypred
    
    for frame_shift, frame in zip(np.split(shifts,len(trajframes)),trajframes):
        frame.arrays["cs_iso"] = frame_shift
    
    write(WRITEPATH,trajframes,format="extxyz")

if __name__ == "__main__":
    pass