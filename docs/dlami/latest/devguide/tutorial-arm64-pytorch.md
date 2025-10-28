# Using the ARM64 GPU PyTorch DLAMI

The AWS Deep Learning AMIs is ready to use with Arm64 processor-based GPUs, and comes optimized
for PyTorch. The ARM64 GPU PyTorch DLAMI includes a Python environment pre-configured
with [PyTorch](https://aws.amazon.com/pytorch "https://aws.amazon.com/pytorch"), [TorchVision](https://pytorch.org/vision/stable/index.html "https://pytorch.org/vision/stable/index.html"), and [TorchServe](https://pytorch.org/serve/ "https://pytorch.org/serve/") for deep learning training and
inference use cases.

###### Contents

- [Verify PyTorch Python
  Environment](#tutorial-arm64-pytorch-environment "#tutorial-arm64-pytorch-environment")
- [Run Training Sample with
  PyTorch](#tutorial-arm64-pytorch-training "#tutorial-arm64-pytorch-training")
- [Run Inference Sample with
  PyTorch](#tutorial-arm64-pytorch-inference "#tutorial-arm64-pytorch-inference")

## Verify PyTorch Python

Environment

Connect to your G5g instance and activate the base Conda environment with the following command:

```
source activate base
```

Your command prompt should indicate that you are working in the base Conda
environment, which contains PyTorch, TorchVision, and other libraries.

```
(base) $
```

Verify the default tool paths of the PyTorch environment:

```
(base) $ which python
(base) $ which pip
(base) $ which conda
(base) $ which mamba
>>> import torch, torchvision
>>> torch.__version__
>>> torchvision.__version__
>>> v = torch.autograd.Variable(torch.randn(10, 3, 224, 224))
>>> v = torch.autograd.Variable(torch.randn(10, 3, 224, 224)).cuda()
>>> assert isinstance(v, torch.Tensor)
```

## Run Training Sample with

PyTorch

Run a sample MNIST training job:

```
git clone https://github.com/pytorch/examples.git
cd examples/mnist
python main.py
```

Your output should look similar to the following:

```
...
Train Epoch: 14 [56320/60000 (94%)]    Loss: 0.021424
Train Epoch: 14 [56960/60000 (95%)]    Loss: 0.023695
Train Epoch: 14 [57600/60000 (96%)]    Loss: 0.001973
Train Epoch: 14 [58240/60000 (97%)]    Loss: 0.007121
Train Epoch: 14 [58880/60000 (98%)]    Loss: 0.003717
Train Epoch: 14 [59520/60000 (99%)]    Loss: 0.001729
Test set: Average loss: 0.0275, Accuracy: 9916/10000 (99%)
```

## Run Inference Sample with

PyTorch

Use the following commands to download a pre-trained densenet161 model and run
inference using TorchServe:

```
# Set up TorchServe
cd $HOME
git clone https://github.com/pytorch/serve.git
mkdir -p serve/model_store
cd serve

# Download a pre-trained densenet161 model
wget https://download.pytorch.org/models/densenet161-8d451a50.pth >/dev/null

# Save the model using torch-model-archiver
torch-model-archiver --model-name densenet161 \
    --version 1.0 \
    --model-file examples/image_classifier/densenet_161/model.py \
    --serialized-file densenet161-8d451a50.pth \
    --handler image_classifier \
    --extra-files examples/image_classifier/index_to_name.json  \
    --export-path model_store

# Start the model server
torchserve --start --no-config-snapshots \
    --model-store model_store \
    --models densenet161=densenet161.mar &> torchserve.log

# Wait for the model server to start
sleep 30

# Run a prediction request
curl http://127.0.0.1:8080/predictions/densenet161 -T examples/image_classifier/kitten.jpg
```

Your output should look similar to the following:

```
{
  "tiger_cat": 0.4693363308906555,
  "tabby": 0.4633873701095581,
  "Egyptian_cat": 0.06456123292446136,
  "lynx": 0.0012828150065615773,
  "plastic_bag": 0.00023322898778133094
}
```

Use the following commands to unregister the densenet161 model and stop the
server:

```
curl -X DELETE http://localhost:8081/models/densenet161/1.0
torchserve --stop
```

Your output should look similar to the following:

```
{
  "status": "Model \"densenet161\" unregistered"
}
TorchServe has stopped.
```
