# Docker Registry Paths and Example Code for Asia Pacific (Hyderabad) (ap-south-2)

The following topics list parameters for each of the algorithms and deep learning containers that are provided by Amazon SageMaker AI in this AWS Region.

###### Topics

- [AutoGluon (algorithm)](#autogluon-ap-south-2 "#autogluon-ap-south-2")
- [BlazingText (algorithm)](#blazingtext-ap-south-2 "#blazingtext-ap-south-2")
- [DeepAR Forecasting (algorithm)](#forecasting-deepar-ap-south-2 "#forecasting-deepar-ap-south-2")
- [Factorization Machines (algorithm)](#factorization-machines-ap-south-2 "#factorization-machines-ap-south-2")
- [Hugging Face (algorithm)](#huggingface-ap-south-2 "#huggingface-ap-south-2")
- [IP Insights (algorithm)](#ipinsights-ap-south-2 "#ipinsights-ap-south-2")
- [Image classification (algorithm)](#image-classification-ap-south-2 "#image-classification-ap-south-2")
- [K-Means (algorithm)](#kmeans-ap-south-2 "#kmeans-ap-south-2")
- [KNN (algorithm)](#knn-ap-south-2 "#knn-ap-south-2")
- [Linear Learner (algorithm)](#linear-learner-ap-south-2 "#linear-learner-ap-south-2")
- [MXNet (DLC)](#mxnet-ap-south-2 "#mxnet-ap-south-2")
- [NTM (algorithm)](#ntm-ap-south-2 "#ntm-ap-south-2")
- [Object Detection (algorithm)](#object-detection-ap-south-2 "#object-detection-ap-south-2")
- [Object2Vec (algorithm)](#object2vec-ap-south-2 "#object2vec-ap-south-2")
- [PCA (algorithm)](#pca-ap-south-2 "#pca-ap-south-2")
- [PyTorch (DLC)](#pytorch-ap-south-2 "#pytorch-ap-south-2")
- [PyTorch Neuron (DLC)](#pytorch-neuron-ap-south-2 "#pytorch-neuron-ap-south-2")
- [PyTorch Training Compiler (DLC)](#pytorch-training-compiler-ap-south-2 "#pytorch-training-compiler-ap-south-2")
- [Random Cut Forest (algorithm)](#randomcutforest-ap-south-2 "#randomcutforest-ap-south-2")
- [Scikit-learn (algorithm)](#sklearn-ap-south-2 "#sklearn-ap-south-2")
- [Semantic Segmentation (algorithm)](#semantic-segmentation-ap-south-2 "#semantic-segmentation-ap-south-2")
- [Seq2Seq (algorithm)](#seq2seq-ap-south-2 "#seq2seq-ap-south-2")
- [Spark (algorithm)](#spark-ap-south-2 "#spark-ap-south-2")
- [Tensorflow (DLC)](#tensorflow-ap-south-2 "#tensorflow-ap-south-2")
- [XGBoost (algorithm)](#xgboost-ap-south-2 "#xgboost-ap-south-2")

## AutoGluon (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='autogluon',region='ap-south-2',image_scope='inference',version='0.4')
```

| Registry path                                                             | Version | Job types (image scope) |
| ------------------------------------------------------------------------- | ------- | ----------------------- |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/autogluon-training:`<tag>`  | 0.5.2   | training                |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/autogluon-inference:`<tag>` | 0.5.2   | inference               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/autogluon-training:`<tag>`  | 0.4.3   | training                |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/autogluon-inference:`<tag>` | 0.4.3   | inference               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/autogluon-training:`<tag>`  | 0.4.2   | training                |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/autogluon-inference:`<tag>` | 0.4.2   | inference               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/autogluon-training:`<tag>`  | 0.4.0   | training                |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/autogluon-inference:`<tag>` | 0.4.0   | inference               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/autogluon-training:`<tag>`  | 0.3.2   | training                |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/autogluon-inference:`<tag>` | 0.3.2   | inference               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/autogluon-training:`<tag>`  | 0.3.1   | training                |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/autogluon-inference:`<tag>` | 0.3.1   | inference               |

## BlazingText (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='blazingtext',region='ap-south-2')
```

| Registry path                                                     | Version | Job types (image scope) |
| ----------------------------------------------------------------- | ------- | ----------------------- |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/blazingtext:`<tag>` | 1       | inference, training     |

## DeepAR Forecasting (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='forecasting-deepar',region='ap-south-2')
```

| Registry path                                                            | Version | Job types (image scope) |
| ------------------------------------------------------------------------ | ------- | ----------------------- |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/forecasting-deepar:`<tag>` | 1       | inference, training     |

## Factorization Machines (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='factorization-machines',region='ap-south-2')
```

| Registry path                                                                | Version | Job types (image scope) |
| ---------------------------------------------------------------------------- | ------- | ----------------------- |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/factorization-machines:`<tag>` | 1       | inference, training     |

## Hugging Face (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='huggingface',region='ap-south-2',version='4.4.2',image_scope='training',base_framework_version='tensorflow2.4.1')
```

| Registry path                                                                          | Version | Job types (image scope) |
| -------------------------------------------------------------------------------------- | ------- | ----------------------- |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-pytorch-inference:`<tag>`    | 4.49.0  | inference               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-pytorch-inference:`<tag>`    | 4.48.0  | inference               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-pytorch-inference:`<tag>`    | 4.37.0  | inference               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-pytorch-inference:`<tag>`    | 4.28.1  | inference               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-pytorch-inference:`<tag>`    | 4.26.0  | inference               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-tensorflow-inference:`<tag>` | 4.26.0  | inference               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.17.0  | training                |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-tensorflow-training:`<tag>`  | 4.17.0  | training                |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-pytorch-inference:`<tag>`    | 4.17.0  | inference               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-tensorflow-inference:`<tag>` | 4.17.0  | inference               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.12.3  | training                |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-tensorflow-training:`<tag>`  | 4.12.3  | training                |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-pytorch-inference:`<tag>`    | 4.12.3  | inference               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-tensorflow-inference:`<tag>` | 4.12.3  | inference               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.11.0  | training                |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-tensorflow-training:`<tag>`  | 4.11.0  | training                |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-pytorch-inference:`<tag>`    | 4.11.0  | inference               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-tensorflow-inference:`<tag>` | 4.11.0  | inference               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.10.2  | training                |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.10.2  | training                |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-tensorflow-training:`<tag>`  | 4.10.2  | training                |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-tensorflow-training:`<tag>`  | 4.10.2  | training                |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-pytorch-inference:`<tag>`    | 4.10.2  | inference               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-pytorch-inference:`<tag>`    | 4.10.2  | inference               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-tensorflow-inference:`<tag>` | 4.10.2  | inference               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-tensorflow-inference:`<tag>` | 4.10.2  | inference               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.6.1   | training                |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.6.1   | training                |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.6.1   | training                |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-tensorflow-training:`<tag>`  | 4.6.1   | training                |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-pytorch-inference:`<tag>`    | 4.6.1   | inference               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-tensorflow-inference:`<tag>` | 4.6.1   | inference               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.5.0   | training                |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-tensorflow-training:`<tag>`  | 4.5.0   | training                |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.4.2   | training                |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/huggingface-tensorflow-training:`<tag>`  | 4.4.2   | training                |

## IP Insights (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='ipinsights',region='ap-south-2')
```

| Registry path                                                    | Version | Job types (image scope) |
| ---------------------------------------------------------------- | ------- | ----------------------- |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/ipinsights:`<tag>` | 1       | inference, training     |

## Image classification (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='image-classification',region='ap-south-2')
```

| Registry path                                                              | Version | Job types (image scope) |
| -------------------------------------------------------------------------- | ------- | ----------------------- |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/image-classification:`<tag>` | 1       | inference, training     |

## K-Means (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='kmeans',region='ap-south-2')
```

| Registry path                                                | Version | Job types (image scope) |
| ------------------------------------------------------------ | ------- | ----------------------- |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/kmeans:`<tag>` | 1       | inference, training     |

## KNN (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='knn',region='ap-south-2')
```

| Registry path                                             | Version | Job types (image scope) |
| --------------------------------------------------------- | ------- | ----------------------- |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/knn:`<tag>` | 1       | inference, training     |

## Linear Learner (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='linear-learner',region='ap-south-2')
```

| Registry path                                                        | Version | Job types (image scope) |
| -------------------------------------------------------------------- | ------- | ----------------------- |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/linear-learner:`<tag>` | 1       | inference, training     |

## MXNet (DLC)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='mxnet',region='ap-south-2',version='1.4.1',py_version='py3',image_scope='inference', instance_type='ml.c5.4xlarge')
```

| Registry path                                                             | Version | Job types (image scope) | Processor types | Python versions |
| ------------------------------------------------------------------------- | ------- | ----------------------- | --------------- | --------------- |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/mxnet-training:`<tag>`      | 1.9.0   | training                | CPU, GPU        | py38            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/mxnet-inference:`<tag>`     | 1.9.0   | inference               | CPU, GPU        | py38            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/mxnet-training:`<tag>`      | 1.8.0   | training                | CPU, GPU        | py37            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/mxnet-inference:`<tag>`     | 1.8.0   | inference               | CPU, GPU        | py37            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/mxnet-training:`<tag>`      | 1.7.0   | training                | CPU, GPU        | py3             |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/mxnet-inference:`<tag>`     | 1.7.0   | inference               | CPU, GPU        | py3             |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/mxnet-inference-eia:`<tag>` | 1.7.0   | eia                     | CPU             | py3             |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/mxnet-training:`<tag>`      | 1.6.0   | training                | CPU, GPU        | py2, py3        |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/mxnet-inference:`<tag>`     | 1.6.0   | inference               | CPU, GPU        | py2, py3        |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/mxnet-inference-eia:`<tag>` | 1.5.1   | eia                     | CPU             | py2, py3        |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/mxnet-training:`<tag>`      | 1.4.1   | training                | CPU, GPU        | py3             |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/mxnet-inference:`<tag>`     | 1.4.1   | inference               | CPU, GPU        | py3             |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/mxnet-inference-eia:`<tag>` | 1.4.1   | eia                     | CPU             | py2, py3        |

## NTM (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='ntm',region='ap-south-2')
```

| Registry path                                             | Version | Job types (image scope) |
| --------------------------------------------------------- | ------- | ----------------------- |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/ntm:`<tag>` | 1       | inference, training     |

## Object Detection (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='object-detection',region='ap-south-2')
```

| Registry path                                                          | Version | Job types (image scope) |
| ---------------------------------------------------------------------- | ------- | ----------------------- |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/object-detection:`<tag>` | 1       | inference, training     |

## Object2Vec (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='object2vec',region='ap-south-2')
```

| Registry path                                                    | Version | Job types (image scope) |
| ---------------------------------------------------------------- | ------- | ----------------------- |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/object2vec:`<tag>` | 1       | inference, training     |

## PCA (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='pca',region='ap-south-2')
```

| Registry path                                             | Version | Job types (image scope) |
| --------------------------------------------------------- | ------- | ----------------------- |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/pca:`<tag>` | 1       | inference, training     |

## PyTorch (DLC)

For information about the supported and unsupported PyTorch versions, see the [Framework Support Policy Table](../../../deep-learning-containers/latest/devguide/dlc-framework-support-policy.md "../../../deep-learning-containers/latest/devguide/dlc-framework-support-policy.md")
in the _AWS Deep Learning Containers Developer Guide_.

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='pytorch',region='ap-south-2',version='1.8.0',py_version='py3',image_scope='inference', instance_type='ml.c5.4xlarge')
```

| Registry path                                                                    | Version | Job types (image scope) | Processor types | Python versions |
| -------------------------------------------------------------------------------- | ------- | ----------------------- | --------------- | --------------- |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-training:`<tag>`           | 2.7.1   | training                | CPU, GPU        | py312           |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-inference:`<tag>`          | 2.6.0   | inference               | CPU, GPU        | py312           |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-training:`<tag>`           | 2.6.0   | training                | CPU, GPU        | py312           |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-inference:`<tag>`          | 2.5.1   | inference               | CPU, GPU        | py311           |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-training:`<tag>`           | 2.5.1   | training                | CPU, GPU        | py311           |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-inference:`<tag>`          | 2.4.0   | inference               | CPU, GPU        | py311           |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-inference-graviton:`<tag>` | 2.4.0   | inference_graviton      | CPU             | py311           |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-training:`<tag>`           | 2.4.0   | training                | CPU, GPU        | py311           |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-inference:`<tag>`          | 2.3.0   | inference               | CPU, GPU        | py311           |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-inference-graviton:`<tag>` | 2.3.0   | inference_graviton      | CPU             | py311           |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-training:`<tag>`           | 2.3.0   | training                | CPU, GPU        | py311           |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-inference-graviton:`<tag>` | 2.2.1   | inference_graviton      | CPU             | py310           |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-inference:`<tag>`          | 2.2.0   | inference               | CPU, GPU        | py310           |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-training:`<tag>`           | 2.2.0   | training                | CPU, GPU        | py310           |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-inference:`<tag>`          | 2.1.0   | inference               | CPU, GPU        | py310           |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-inference-graviton:`<tag>` | 2.1.0   | inference_graviton      | CPU             | py310           |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-training:`<tag>`           | 2.1.0   | training                | CPU, GPU        | py310           |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-inference:`<tag>`          | 2.0.1   | inference               | CPU, GPU        | py310           |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-inference-graviton:`<tag>` | 2.0.1   | inference_graviton      | CPU             | py310           |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-training:`<tag>`           | 2.0.1   | training                | CPU, GPU        | py310           |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-inference:`<tag>`          | 2.0.0   | inference               | CPU, GPU        | py310           |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-inference-graviton:`<tag>` | 2.0.0   | inference_graviton      | CPU             | py310           |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-training:`<tag>`           | 2.0.0   | training                | CPU, GPU        | py310           |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-inference:`<tag>`          | 1.13.1  | inference               | CPU, GPU        | py39            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-training:`<tag>`           | 1.13.1  | training                | CPU, GPU        | py39            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-inference:`<tag>`          | 1.12.1  | inference               | CPU, GPU        | py38            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-inference-graviton:`<tag>` | 1.12.1  | inference_graviton      | CPU             | py38            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-training:`<tag>`           | 1.12.1  | training                | CPU, GPU        | py38            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-inference:`<tag>`          | 1.12.0  | inference               | CPU, GPU        | py38            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-training:`<tag>`           | 1.12.0  | training                | CPU, GPU        | py38            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-inference:`<tag>`          | 1.11.0  | inference               | CPU, GPU        | py38            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-training:`<tag>`           | 1.11.0  | training                | CPU, GPU        | py38            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-inference:`<tag>`          | 1.10.2  | inference               | CPU, GPU        | py38            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-training:`<tag>`           | 1.10.2  | training                | CPU, GPU        | py38            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-inference:`<tag>`          | 1.10.0  | inference               | CPU, GPU        | py38            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-training:`<tag>`           | 1.10.0  | training                | CPU, GPU        | py38            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-inference:`<tag>`          | 1.9.1   | inference               | CPU, GPU        | py38            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-training:`<tag>`           | 1.9.1   | training                | CPU, GPU        | py38            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-inference:`<tag>`          | 1.9.0   | inference               | CPU, GPU        | py38            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-training:`<tag>`           | 1.9.0   | training                | CPU, GPU        | py38            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-inference:`<tag>`          | 1.8.1   | inference               | CPU, GPU        | py3, py36       |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-training:`<tag>`           | 1.8.1   | training                | CPU, GPU        | py3, py36       |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-inference:`<tag>`          | 1.8.0   | inference               | CPU, GPU        | py3, py36       |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-training:`<tag>`           | 1.8.0   | training                | CPU, GPU        | py3, py36       |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-inference:`<tag>`          | 1.7.1   | inference               | CPU, GPU        | py3, py36       |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-training:`<tag>`           | 1.7.1   | training                | CPU, GPU        | py3, py36       |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-inference:`<tag>`          | 1.6.0   | inference               | CPU, GPU        | py3, py36       |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-training:`<tag>`           | 1.6.0   | training                | CPU, GPU        | py3, py36       |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-inference-eia:`<tag>`      | 1.5.1   | eia                     | CPU             | py3             |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-inference:`<tag>`          | 1.5.0   | inference               | CPU, GPU        | py3, py36       |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-training:`<tag>`           | 1.5.0   | training                | CPU, GPU        | py3, py36       |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-inference:`<tag>`          | 1.4.0   | inference               | CPU, GPU        | py3, py36       |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-training:`<tag>`           | 1.4.0   | training                | CPU, GPU        | py2, py3, py36  |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-inference-eia:`<tag>`      | 1.3.1   | eia                     | CPU             | py3             |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-inference:`<tag>`          | 1.3.1   | inference               | CPU, GPU        | py2, py3        |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-training:`<tag>`           | 1.3.1   | training                | CPU, GPU        | py2, py3        |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-inference:`<tag>`          | 1.2.0   | inference               | CPU, GPU        | py2, py3        |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-training:`<tag>`           | 1.2.0   | training                | CPU, GPU        | py2, py3        |

## PyTorch Neuron (DLC)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='pytorch-neuron',region='us-west-2', image_scope='inference')
```

| Registry path                                                                 | Version | Job types (image scope) | Processor types | Python versions |
| ----------------------------------------------------------------------------- | ------- | ----------------------- | --------------- | --------------- |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-training-neuron:`<tag>` | 1.11.0  | training                | TRN             | py38            |

## PyTorch Training Compiler (DLC)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='pytorch-training-compiler',region='us-west-2', version='py38')
```

| Registry path                                                                 | Version | Job types (image scope) | Processor types | Python versions |
| ----------------------------------------------------------------------------- | ------- | ----------------------- | --------------- | --------------- |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/pytorch-trcomp-training:`<tag>` | 1.12.0  | training                | GPU             | py38            |

## Random Cut Forest (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='randomcutforest',region='ap-south-2')
```

| Registry path                                                         | Version | Job types (image scope) |
| --------------------------------------------------------------------- | ------- | ----------------------- |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/randomcutforest:`<tag>` | 1       | inference, training     |

## Scikit-learn (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='sklearn',region='ap-south-2',version='0.23-1',image_scope='inference')
```

| Registry path                                                                | Version | Package version | Job types (image scope) |
| ---------------------------------------------------------------------------- | ------- | --------------- | ----------------------- |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/sagemaker-scikit-learn:`<tag>` | 1.2-1   | 1.2.1           | inference               |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/sagemaker-scikit-learn:`<tag>` | 1.2-1   | 1.2.1           | training                |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/sagemaker-scikit-learn:`<tag>` | 1.0-1   | 1.0.2           | inference               |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/sagemaker-scikit-learn:`<tag>` | 1.0-1   | 1.0.2           | training                |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/sagemaker-scikit-learn:`<tag>` | 1.0-1   | 1.0.2           | inference_graviton      |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/sagemaker-scikit-learn:`<tag>` | 0.23-1  | 0.23.2          | inference               |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/sagemaker-scikit-learn:`<tag>` | 0.23-1  | 0.23.2          | training                |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/sagemaker-scikit-learn:`<tag>` | 0.20.0  | 0.20.0          | inference               |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/sagemaker-scikit-learn:`<tag>` | 0.20.0  | 0.20.0          | training                |

## Semantic Segmentation (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='semantic-segmentation',region='ap-south-2')
```

| Registry path                                                               | Version | Job types (image scope) |
| --------------------------------------------------------------------------- | ------- | ----------------------- |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/semantic-segmentation:`<tag>` | 1       | inference, training     |

## Seq2Seq (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='seq2seq',region='ap-south-2')
```

| Registry path                                                 | Version | Job types (image scope) |
| ------------------------------------------------------------- | ------- | ----------------------- |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/seq2seq:`<tag>` | 1       | inference, training     |

## Spark (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='spark',region='ap-south-2',version='3.0',image_scope='processing')
```

| Registry path                                                                    | Version | Job types (image scope) |
| -------------------------------------------------------------------------------- | ------- | ----------------------- |
| 873151114052.dkr.ecr.ap-south-2.amazonaws.com/sagemaker-spark-processing:`<tag>` | 3.3     | processing              |
| 873151114052.dkr.ecr.ap-south-2.amazonaws.com/sagemaker-spark-processing:`<tag>` | 3.2     | processing              |
| 873151114052.dkr.ecr.ap-south-2.amazonaws.com/sagemaker-spark-processing:`<tag>` | 3.1     | processing              |
| 873151114052.dkr.ecr.ap-south-2.amazonaws.com/sagemaker-spark-processing:`<tag>` | 3.0     | processing              |
| 873151114052.dkr.ecr.ap-south-2.amazonaws.com/sagemaker-spark-processing:`<tag>` | 2.4     | processing              |

## Tensorflow (DLC)

For information about the supported and unsupported TensorFlow versions, see the [Framework Support Policy Table](../../../deep-learning-containers/latest/devguide/dlc-framework-support-policy.md "../../../deep-learning-containers/latest/devguide/dlc-framework-support-policy.md")
in the _AWS Deep Learning Containers Developer Guide_.

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='tensorflow',region='ap-south-2',version='1.12.0',image_scope='inference',instance_type='ml.c5.4xlarge')
```

| Registry path                                                                       | Version | Job types (image scope) | Processor types | Python versions |
| ----------------------------------------------------------------------------------- | ------- | ----------------------- | --------------- | --------------- |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.19.0  | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.19.0  | training                | CPU, GPU        | py312           |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.18.0  | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.18.0  | training                | CPU, GPU        | py310           |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.16.2  | training                | CPU, GPU        | py310           |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.16.1  | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference-graviton:`<tag>` | 2.16.1  | inference_graviton      | CPU             | py310           |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.14.1  | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference-graviton:`<tag>` | 2.14.1  | inference_graviton      | CPU             | py310           |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.14.1  | training                | CPU, GPU        | py310           |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.13.0  | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference-graviton:`<tag>` | 2.13.0  | inference_graviton      | CPU             | py310           |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.13.0  | training                | CPU, GPU        | py310           |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.12.1  | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference-graviton:`<tag>` | 2.12.1  | inference_graviton      | CPU             | py310           |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.12.0  | training                | CPU, GPU        | py310           |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.11.1  | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.11.0  | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.11.0  | training                | CPU, GPU        | py39            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.10.1  | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.10.1  | training                | CPU, GPU        | py39            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.10.0  | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.9.3   | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.9.2   | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.9.2   | training                | CPU, GPU        | py39            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference-graviton:`<tag>` | 2.9.1   | inference_graviton      | CPU             | py38            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.8.4   | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.8.0   | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.8.0   | training                | CPU, GPU        | py39            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.7.1   | training                | CPU, GPU        | py38            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.7.0   | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.6.3   | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.6.3   | training                | CPU, GPU        | py38            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.6.2   | training                | CPU, GPU        | py38            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.6.0   | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.6.0   | training                | CPU, GPU        | py38            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.5.1   | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.5.1   | training                | CPU, GPU        | py37            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.5.0   | training                | CPU, GPU        | py37            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.4.3   | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.4.3   | training                | CPU, GPU        | py37            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.4.1   | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.4.1   | training                | CPU, GPU        | py37            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.3.2   | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.3.2   | training                | CPU, GPU        | py37            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.3.1   | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.3.1   | training                | CPU, GPU        | py37            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference-eia:`<tag>`      | 2.3.0   | eia                     | CPU             | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.3.0   | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.3.0   | training                | CPU, GPU        | py37            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.2.2   | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.2.2   | training                | CPU, GPU        | py37            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.2.1   | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.2.1   | training                | CPU, GPU        | py37            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.2.0   | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.2.0   | training                | CPU, GPU        | py37            |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.1.3   | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.1.3   | training                | CPU, GPU        | py3, py36       |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.1.2   | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.1.2   | training                | CPU, GPU        | py3, py36       |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.1.1   | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.1.1   | training                | CPU, GPU        | py2, py3        |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.1.0   | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.1.0   | training                | CPU, GPU        | py2, py3        |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.0.4   | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.0.4   | training                | CPU, GPU        | py3, py36       |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.0.3   | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.0.3   | training                | CPU, GPU        | py3, py36       |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.0.2   | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.0.2   | training                | CPU, GPU        | py2, py3        |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.0.1   | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.0.1   | training                | CPU, GPU        | py2, py3        |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference-eia:`<tag>`      | 2.0.0   | eia                     | CPU             | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.0.0   | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.0.0   | training                | CPU, GPU        | py2, py3        |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 1.15.5  | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 1.15.5  | training                | CPU, GPU        | py3, py36, py37 |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 1.15.4  | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 1.15.4  | training                | CPU, GPU        | py3, py36, py37 |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 1.15.3  | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 1.15.3  | training                | CPU, GPU        | py2, py3, py37  |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 1.15.2  | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 1.15.2  | training                | CPU, GPU        | py2, py3, py37  |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference-eia:`<tag>`      | 1.15.0  | eia                     | CPU             | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 1.15.0  | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 1.15.0  | training                | CPU, GPU        | py2, py3        |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference-eia:`<tag>`      | 1.14.0  | eia                     | CPU             | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 1.14.0  | inference               | CPU, GPU        | -               |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 1.14.0  | training                | CPU, GPU        | py2, py3        |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-training:`<tag>`           | 1.13.1  | training                | CPU, GPU        | py3             |
| 772153158452.dkr.ecr.ap-south-2.amazonaws.com/tensorflow-inference:`<tag>`          | 1.13.0  | inference               | CPU, GPU        | -               |

## XGBoost (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='xgboost',region='ap-south-2',version='1.5-1')
```

| Registry path                                                           | Version | Package version | Job types (image scope) |
| ----------------------------------------------------------------------- | ------- | --------------- | ----------------------- |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.7-1   | 1.7.4           | inference               |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.7-1   | 1.7.4           | training                |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.5-1   | 1.5.2           | inference               |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.5-1   | 1.5.2           | training                |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.5-1   | 1.5.2           | inference_graviton      |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.3-1   | 1.3.3           | inference               |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.3-1   | 1.3.3           | training                |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.3-1   | 1.3.3           | inference_graviton      |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.2-2   | 1.2.0           | inference               |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.2-2   | 1.2.0           | training                |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.2-1   | 1.2.0           | inference               |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.2-1   | 1.2.0           | training                |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.0-1   | 1.0.0           | inference               |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.0-1   | 1.0.0           | training                |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/xgboost:`<tag>`           | 1       | 0.72            | inference               |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/xgboost:`<tag>`           | 1       | 0.72            | training                |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 0.90-2  | 0.90            | inference               |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 0.90-2  | 0.90            | training                |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 0.90-1  | 0.90            | inference               |
| 628508329040.dkr.ecr.ap-south-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 0.90-1  | 0.90            | training                |
