# Using the Deep Learning Base AMI

## Using the Deep Learning Base AMI

The Base AMI comes with a foundational platform of GPU drivers and acceleration
libraries to deploy your own customized deep learning environment. By default the AMI is
configured with any one NVIDIA CUDA version environment. You can also switch between different
versions of CUDA. Refer to the following instructions for how to do this.

## Configuring CUDA Versions

You can verify the CUDA version by running NVIDIA's `nvcc` program.

```
nvcc --version
```

You can select and verify a particular CUDA version with the following bash
command:

```
sudo rm /usr/local/cuda
sudo ln -s /usr/local/`cuda-12.0` /usr/local/cuda
```

For more information, see the [Base DLAMI release notes](appendix-ami-release-notes.md#appendix-ami-release-notes-base "appendix-ami-release-notes.md#appendix-ami-release-notes-base").
