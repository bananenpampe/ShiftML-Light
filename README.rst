==============
ShiftML-Light
==============

  A rapid model for predicting chemical shifts from molecular dynamics trajectories of organic solids.
    

Example
=======

* To analyze a .extxyz trajectory with a constant number of atoms and no change in indexing, import the (:code:`md_analysis_light`) routine::

  md_analysis_light("PATH_READ.xyz","PATH_WRITE.xyz")
  

Install notes
=============

* Clone this repository, change into the git repository and then install via pip::

  git clone <link>
  cd <./cloned_repository>
  pip install . 

Citations
=========

* This model and dataset curation is based on earlier works from Paruzzo et al. and Engel et al, 
  to cite them properly please include::
  
  
@article{paruzzo_chemical_2018,
	title = {Chemical shifts in molecular solids by machine learning},
	volume = {9},
	doi = {10.1038/s41467-018-06972-x},
	language = {en},
	number = {1},
	journal = {Nature Communications},
	author = {Paruzzo, Federico M. and Hofstetter, Albert and Musil, Félix and De, Sandip and Ceriotti, Michele and Emsley, Lyndon},
	year = {2018}
}

@article{engel_bayesian_2019,
	title = {A {Bayesian} approach to {NMR} crystal structure determination},
	volume = {21},
	doi = {10.1039/C9CP04489B},
	journal = {Physical Chemistry Chemical Physics},
	author = {Engel, Edgar A. and Anelli, Andrea and Hofstetter, Albert and Paruzzo, Federico and Emsley, Lyndon and Ceriotti, Michele},
	year = {2019},
}

* Feature optimization was performed using the helper functions from Willatt et al. and Goscinski et al.::


@article{goscinski_optimal_2021,
	title = {Optimal radial basis for density-based atomic representations},
	volume = {155},
	doi = {10.1063/5.0057229},
	number = {10},
	urldate = {2022-02-19},
	journal = {The Journal of Chemical Physics},
	author = {Goscinski, Alexander and Musil, Félix and Pozdnyakov, Sergey and Nigam, Jigyasa and Ceriotti, Michele},
	year = {2021},
	note = {Publisher: American Institute of Physics},
	pages = {104106},
}


@article{willatt_feature_2018,
	title = {Feature optimization for atomistic machine learning yields a data-driven construction of the periodic table of the elements},
	volume = {20},
  doi = {10.1039/C8CP05921G},
	number = {47},
	journal = {Physical Chemistry Chemical Physics},
	author = {Willatt, Michael J. and Musil, Félix and Ceriotti, Michele},
	year = {2018},
	note = {Publisher: The Royal Society of Chemistry},
	pages = {29661--29668},
}







  
  
