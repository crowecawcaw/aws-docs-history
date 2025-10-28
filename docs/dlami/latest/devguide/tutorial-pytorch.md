# PyTorch

## Activating PyTorch

When a stable Conda package of a framework is released, it's tested and pre-installed on the
DLAMI. If you want to run the latest, untested nightly build, you can [Install PyTorch's Nightly Build (experimental)](#tutorial-pytorch-install "#tutorial-pytorch-install")
manually.

To activate the currently installed framework, follow these instructions on your Deep Learning AMI with Conda.

For PyTorch on Python 3 with CUDA and MKL-DNN, run this command:

```
`$` source activate pytorch_p310
```

Start the iPython terminal.

```
`(pytorch_p310)$` ipython
```

Run a quick PyTorch program.

```
import torch
x = torch.rand(5, 3)
print(x)
print(x.size())
y = torch.rand(5, 3)
print(torch.add(x, y))

```

You should see the initial random array printed,
then its size, and then the addition of another random array.

## Install PyTorch's Nightly Build (experimental)

###### How to install PyTorch from a nightly build

You can install the latest PyTorch build into either or both of the PyTorch Conda environments on your Deep Learning AMI with Conda.

1. - (Option for Python 3) - Activate the Python 3 PyTorch environment:

   ```
   `$` source activate pytorch_p310
   ```

2. The remaining steps assume you are using the `pytorch_p310` environment.
   Remove the currently installed PyTorch:

```
`(pytorch_p310)$` pip uninstall torch
```

3. - (Option for GPU instances) - Install the latest nightly build of PyTorch with CUDA.0:

   ```
   `(pytorch_p310)$` pip install torch_nightly -f https://download.pytorch.org/whl/nightly/cu100/torch_nightly.html
   ```

   - (Option for CPU instances) - Install the latest nightly build of PyTorch for
     instances with no GPUs:

   ```
   `(pytorch_p310)$` pip install torch_nightly -f https://download.pytorch.org/whl/nightly/cpu/torch_nightly.html
   ```

4. To verify you have successfully installed latest nightly build, start the IPython terminal and check the version of PyTorch.

```
`(pytorch_p310)$` ipython
```

```
import torch
print (torch.__version__)
```

The output should print something similar to `1.0.0.dev20180922` 5. To verify that the PyTorch nightly build works well with the MNIST example, you can run a test script from PyTorch's examples repository:

```
`(pytorch_p310)$` cd ~
`(pytorch_p310)$` git clone https://github.com/pytorch/examples.git pytorch_examples
`(pytorch_p310)$` cd pytorch_examples/mnist
`(pytorch_p310)$` python main.py || exit 1
```

## More Tutorials

For further tutorials and examples refer to the framework's official docs,
[PyTorch documentation](http://pytorch.org/docs/master/ "http://pytorch.org/docs/master/"),
and the [PyTorch](http://pytorch.org "http://pytorch.org") website.
