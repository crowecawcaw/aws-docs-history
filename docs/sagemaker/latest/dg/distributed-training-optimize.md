# Distributed training optimization

Customize hyperparameters for your use case and your data to get the best scaling
efficiency. In the following discussion, we highlight some of the most impactful training
variables and provide references to state-of-the-art implementations so you can learn more
about your options. Also, we recommend that you refer to your preferred framework’s
distributed training documentation.

- [Apache
  MXNet distributed training](https://mxnet.apache.org/versions/1.7/api/faq/distributed_training "https://mxnet.apache.org/versions/1.7/api/faq/distributed_training")
- [PyTorch distributed
  training](https://pytorch.org/tutorials/beginner/dist_overview.html "https://pytorch.org/tutorials/beginner/dist_overview.html")
- [TensorFlow distributed
  training](https://www.tensorflow.org/guide/distributed_training "https://www.tensorflow.org/guide/distributed_training")

## Batch Size

SageMaker AI distributed toolkits generally allow you to train on bigger batches. For example,
if a model fits within a single device but can only be trained with a small batch size,
using either model-parallel training or data parallel training enables you to experiment
with larger batch sizes.

Be aware that batch size directly influences model accuracy by controlling the amount of
noise in the model update at each iteration. Increasing batch size reduces the amount of
noise in the gradient estimation, which can be beneficial when increasing from very small
batches sizes, but can result in degraded model accuracy as the batch size increases to
large values. 

###### Tip

Adjust your hyperparameters to ensure that your model trains to a satisfying
convergence as you increase its batch size.

A number of techniques have been developed to maintain good model convergence when batch
is increased.

## Mini-batch size

In SGD, the mini-batch size quantifies the amount of noise present in the gradient
estimation. A small mini-batch results in a very noisy mini-batch gradient, which is not
representative of the true gradient over the dataset. A large mini-batch results in a
mini-batch gradient close to the true gradient over the dataset and potentially not noisy
enough—likely to stay locked in irrelevant minima.

To learn more about these techniques, see the following papers:

- [Accurate, Large Minibatch
  SGD:Training ImageNet in 1 Hour](https://arxiv.org/pdf/1706.02677.pdf "https://arxiv.org/pdf/1706.02677.pdf"), Goya et al.
- [PowerAI DDL](https://arxiv.org/pdf/1708.02188.pdf "https://arxiv.org/pdf/1708.02188.pdf"), Cho et al.
- [Scale Out for Large Minibatch SGD:
  Residual Network Training on ImageNet-1K with Improved Accuracy and Reduced Time to
  Train](https://arxiv.org/pdf/1711.04291.pdf "https://arxiv.org/pdf/1711.04291.pdf"), Codreanu et al.
- [ImageNet Training in
  Minutes](https://arxiv.org/pdf/1709.05011.pdf "https://arxiv.org/pdf/1709.05011.pdf"), You et al.
- [Large Batch Training of
  Convolutional Networks](https://arxiv.org/pdf/1708.03888.pdf "https://arxiv.org/pdf/1708.03888.pdf"), You et al.
- [Large Batch Optimization for Deep
  Learning: Training BERT in 76 Minutes](https://arxiv.org/pdf/1904.00962.pdf "https://arxiv.org/pdf/1904.00962.pdf"), You et al.
- [Accelerated Large Batch Optimization
  of BERT Pretraining in 54 minutes](https://arxiv.org/pdf/2006.13484.pdf "https://arxiv.org/pdf/2006.13484.pdf"), Zheng et al.
- [Deep Gradient Compression](https://arxiv.org/abs/1712.01887 "https://arxiv.org/abs/1712.01887"), Lin
  et al.
