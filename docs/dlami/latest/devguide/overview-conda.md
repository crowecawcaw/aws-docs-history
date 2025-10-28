# Deep Learning AMI with Conda

The Conda DLAMI uses `conda` virtual environments, they are present either multi-framework
or single framework DLAMIs. These environments are
configured to keep the different framework installations separate and streamline switching
between frameworks. This is great for learning and experimenting with all of the frameworks
the DLAMI has to offer. Most users find that the new Deep Learning AMI with Conda is perfect for them.

They are updated often with the latest versions from
the frameworks, and have the latest GPU drivers and software. They are generally referred
to as the AWS Deep Learning AMIs in most documents. These DLAMIs support Ubuntu 20.04, Ubuntu 22.04, Amazon Linux 2, Amazon Linux 2023 Operating systems.
Operating systems support depends on support from upstream OS.

## Stable Versus Release Candidates

The Conda AMIs use optimized binaries of the most recent formal releases from each
framework. Release candidates and experimental features are not to be expected. The
optimizations depend on the framework's support for acceleration technologies like
Intel's MKL DNN, which speeds up training and inference on C5 and C4 CPU instance
types. The binaries are also compiled to support advanced Intel instruction sets
including but not limited to AVX, AVX-2, SSE4.1, and SSE4.2. These accelerate vector
and floating point operations on Intel CPU architectures. Additionally, for GPU instance
types, the CUDA and cuDNN are updated with whichever version the latest official
release supports.

The Deep Learning AMI with Conda automatically installs the most optimized version of the framework for
your Amazon EC2 instance upon the framework's first activation. For more information, refer to
[Using the Deep Learning AMI with Conda](tutorial-conda.md "tutorial-conda.md").

If you want to install from source, using custom or optimized build options, the
[Deep Learning Base AMI](overview-base.md "overview-base.md")s might be a better option for you.

## Python 2 Deprecation

The Python open source community has officially ended support for Python 2 on January
1, 2020. The TensorFlow and PyTorch community have announced that the TensorFlow 2.1 and
PyTorch 1.4 releases are the last ones supporting Python 2. Previous releases of the
DLAMI (v26, v25, etc) that contain Python 2 Conda environments continue to be
available. However, we provide updates to the Python 2 Conda environments on
previously published DLAMI versions only if there are security fixes published by the
open-source community for those versions. DLAMI releases with the latest versions of the
TensorFlow and PyTorch frameworks do not contain the Python 2 Conda
environments.

## CUDA Support

Specific CUDA version numbers can be found in the [GPU DLAMI release notes](appendix-ami-release-notes.md#appendix-ami-release-notes-gpu "appendix-ami-release-notes.md#appendix-ami-release-notes-gpu").

###### Next Up

[DLAMI Architecture Options](overview-architecture.md "overview-architecture.md")

## Related Topics

- For a tutorial on using a Deep Learning AMI with Conda, see the [Using the Deep Learning AMI with Conda](tutorial-conda.md "tutorial-conda.md") tutorial.
