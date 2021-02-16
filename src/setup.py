from setuptools import setup, Extension
from torch.utils import cpp_extension

setup(name='dcls_cpp',
      ext_modules=[cpp_extension.CppExtension('dcls_cpp', ['src/dcls.cpp','src/cuda/dcls_cuda_kernel.cu'])],
      cmdclass={'build_ext': cpp_extension.BuildExtension})
