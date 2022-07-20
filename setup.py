from setuptools import setup, find_packages

with open("./requirements.txt", "r") as fp:
    requirements = list(filter(lambda x: "#" not in x, (line.strip() for line in fp)))

setup(name='lshiftml',
        version='0.0.1',
        package_dir={'': 'src/'},
        packages=find_packages(where="src"),
        include_package_data=True,
        install_requires=requirements,
        license='MIT',
        url='https://github.com/bananenpampe/ShiftML-Light',
        author='Matthias Kellner',
        zip_safe=False)
            
    
"""    
    name='funniest',
      version='0.1',
      description='The funniest joke in the world',
      url='http://github.com/storborg/funniest',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      
      packages=['funniest'],
      zip_safe=False)
"""
