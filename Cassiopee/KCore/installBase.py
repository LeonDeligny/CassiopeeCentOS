import os

# Forced Conda Configuration
conda_config = [
    'x86_r8',                                 # 0. System Name
    'mpif90',                                 # 1. F77
    'mpif90',                                 # 2. F90
    'g++',                                    # 3. C++
    ['-fPIC', '-O3', '-DNDEBUG', '-std=c++11'], # 4. C++ Flags
    ['-fPIC', '-O3'],                         # 5. Fortran Flags
    True,                                     # 6. OpenMP
    False,                                    # 7. Static
    ['/home/cfse2/miniconda3/envs/grifo/include'],                # 8. Includes
    ['gfortran', 'gomp', 'pthread', 'mpi'],   # 9. Libs
    ['/home/cfse2/miniconda3/envs/grifo/lib'],                    # 10. Lib Paths
    False,                                    # 11. CUDA
    []                                        # 12. NVCC
]

installDict = {
    None: conda_config,
    'x86_r8': conda_config,
    'default': conda_config
}
