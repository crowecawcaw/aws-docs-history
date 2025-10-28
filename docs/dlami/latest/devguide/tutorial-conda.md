# Using the Deep Learning AMI with Conda

###### Topics

- [Introduction to the Deep Learning AMI with Conda](#tutorial-conda-overview "#tutorial-conda-overview")
- [Log in to Your DLAMI](#tutorial-conda-login "#tutorial-conda-login")
- [Start the TensorFlow Environment](#tutorial-conda-switch-tf "#tutorial-conda-switch-tf")
- [Switch to the PyTorch Python 3 Environment](#tutorial-conda-switch-pytorch "#tutorial-conda-switch-pytorch")
- [Removing Environments](#tutorial-conda-remove-env "#tutorial-conda-remove-env")

## Introduction to the Deep Learning AMI with Conda

Conda is an open source package management system and environment management system that runs on Windows, macOS, and Linux. Conda quickly installs,
runs, and updates packages and their dependencies. Conda easily creates, saves, loads and switches between environments on your local computer.

The Deep Learning AMI with Conda has been configured for you to easily switch between deep learning
environments. The following instructions guide you on some basic commands with
`conda`. They also help you verify that the basic import of the framework
is functioning, and that you can run a couple simple operations with the framework. You
can then move on to more thorough tutorials provided with the DLAMI or the frameworks'
examples found on each frameworks' project site.

## Log in to Your DLAMI

After you log in to your server, you will see a server "message of the day" (MOTD)
describing various Conda commands that you can use to switch between the different deep
learning frameworks. Below is an example MOTD. Your specific MOTD may vary as new versions of the DLAMI are released.

```
=============================================================================
        AMI Name: Deep Learning OSS Nvidia Driver AMI (Amazon Linux 2) Version 77
        Supported EC2 instances: G4dn, G5, G6, Gr6, P4d, P4de, P5
            * To activate pre-built tensorflow environment, run: 'source activate tensorflow2_p310'
            * To activate pre-built pytorch environment, run: 'source activate pytorch_p310'
            * To activate pre-built python3 environment, run: 'source activate python3'

        NVIDIA driver version: 535.161.08

    CUDA versions available: cuda-11.7 cuda-11.8 cuda-12.0 cuda-12.1 cuda-12.2

    Default CUDA version is 12.1

    Release notes: https://docs.aws.amazon.com/dlami/latest/devguide/appendix-ami-release-notes.html
    AWS Deep Learning AMI Homepage: https://aws.amazon.com/machine-learning/amis/
    Developer Guide and Release Notes: https://docs.aws.amazon.com/dlami/latest/devguide/what-is-dlami.html
    Support: https://forums.aws.amazon.com/forum.jspa?forumID=263
    For a fully managed experience, check out Amazon SageMaker at https://aws.amazon.com/sagemaker
    =============================================================================
```

## Start the TensorFlow Environment

###### Note

When you launch your first Conda environment, please be patient while it loads.
The Deep Learning AMI with Conda automatically installs the most optimized version of the framework for your EC2 instance upon the framework's first activation.
You should not expect subsequent delays.

1. Activate the TensorFlow virtual environment for Python 3.

```
`$` source activate tensorflow2_p310
```

2. Start the iPython terminal.

```
`(tensorflow2_p310)$` ipython
```

3. Run a quick TensorFlow program.

```

import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))

```

You should see "Hello, Tensorflow!"

###### Next Up

[Running Jupyter Notebook Tutorials](tutorial-jupyter.md "tutorial-jupyter.md")

## Switch to the PyTorch Python 3 Environment

If you're still in the iPython console, use
`quit()`, then get ready to switch environments.

- Activate the PyTorch virtual environment for Python 3.

```
`$` source activate pytorch_p310
```

### Test Some PyTorch Code

To test your installation, use Python to write PyTorch code that creates and
prints an array.

1. Start the iPython terminal.

```
`(pytorch_p310)$` ipython
```

2. Import PyTorch.

```
import torch
```

You might see a warning message about a third-party package. You can ignore
it. 3. Create a 5x3 matrix with the elements initialized randomly. Print the
array.

```
x = torch.rand(5, 3)
print(x)
```

Verify the result.

```
tensor([[0.3105, 0.5983, 0.5410],
        [0.0234, 0.0934, 0.0371],
        [0.9740, 0.1439, 0.3107],
        [0.6461, 0.9035, 0.5715],
        [0.4401, 0.7990, 0.8913]])
```

## Removing Environments

If you run out of space on the DLAMI, you can choose to uninstall Conda packages that you are not using:

```
conda env list
conda env remove –-name `<env_name>`
```
