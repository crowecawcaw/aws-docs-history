# Docker Registry Paths and Example Code for Europe (Zurich) (eu-central-2)

The following topics list parameters for each of the algorithms and deep learning containers that are provided by Amazon SageMaker AI in this AWS Region.

###### Topics

- [AutoGluon (algorithm)](#autogluon-eu-central-2 "#autogluon-eu-central-2")
- [BlazingText (algorithm)](#blazingtext-eu-central-2 "#blazingtext-eu-central-2")
- [Clarify (algorithm)](#clarify-eu-central-2 "#clarify-eu-central-2")
- [DeepAR Forecasting (algorithm)](#forecasting-deepar-eu-central-2 "#forecasting-deepar-eu-central-2")
- [Factorization Machines (algorithm)](#factorization-machines-eu-central-2 "#factorization-machines-eu-central-2")
- [Hugging Face (algorithm)](#huggingface-eu-central-2 "#huggingface-eu-central-2")
- [IP Insights (algorithm)](#ipinsights-eu-central-2 "#ipinsights-eu-central-2")
- [Image classification (algorithm)](#image-classification-eu-central-2 "#image-classification-eu-central-2")
- [Inferentia MXNet (DLC)](#inferentia-mxnet-eu-central-2 "#inferentia-mxnet-eu-central-2")
- [Inferentia PyTorch (DLC)](#inferentia-pytorch-eu-central-2 "#inferentia-pytorch-eu-central-2")
- [K-Means (algorithm)](#kmeans-eu-central-2 "#kmeans-eu-central-2")
- [KNN (algorithm)](#knn-eu-central-2 "#knn-eu-central-2")
- [Linear Learner (algorithm)](#linear-learner-eu-central-2 "#linear-learner-eu-central-2")
- [MXNet (DLC)](#mxnet-eu-central-2 "#mxnet-eu-central-2")
- [Model Monitor (algorithm)](#model-monitor-eu-central-2 "#model-monitor-eu-central-2")
- [NTM (algorithm)](#ntm-eu-central-2 "#ntm-eu-central-2")
- [Neo Image Classification (algorithm)](#image-classification-neo-eu-central-2 "#image-classification-neo-eu-central-2")
- [Neo MXNet (DLC)](#neo-mxnet-eu-central-2 "#neo-mxnet-eu-central-2")
- [Neo PyTorch (DLC)](#neo-pytorch-eu-central-2 "#neo-pytorch-eu-central-2")
- [Neo Tensorflow (DLC)](#neo-tensorflow-eu-central-2 "#neo-tensorflow-eu-central-2")
- [Neo XGBoost (algorithm)](#xgboost-neo-eu-central-2 "#xgboost-neo-eu-central-2")
- [Object Detection (algorithm)](#object-detection-eu-central-2 "#object-detection-eu-central-2")
- [Object2Vec (algorithm)](#object2vec-eu-central-2 "#object2vec-eu-central-2")
- [PCA (algorithm)](#pca-eu-central-2 "#pca-eu-central-2")
- [PyTorch (DLC)](#pytorch-eu-central-2 "#pytorch-eu-central-2")
- [PyTorch Neuron (DLC)](#pytorch-neuron-eu-central-2 "#pytorch-neuron-eu-central-2")
- [PyTorch Training Compiler (DLC)](#pytorch-training-compiler-eu-central-2 "#pytorch-training-compiler-eu-central-2")
- [Random Cut Forest (algorithm)](#randomcutforest-eu-central-2 "#randomcutforest-eu-central-2")
- [Scikit-learn (algorithm)](#sklearn-eu-central-2 "#sklearn-eu-central-2")
- [Semantic Segmentation (algorithm)](#semantic-segmentation-eu-central-2 "#semantic-segmentation-eu-central-2")
- [Seq2Seq (algorithm)](#seq2seq-eu-central-2 "#seq2seq-eu-central-2")
- [Spark (algorithm)](#spark-eu-central-2 "#spark-eu-central-2")
- [Tensorflow (DLC)](#tensorflow-eu-central-2 "#tensorflow-eu-central-2")
- [Tensorflow Inferentia (DLC)](#inferentia-tensorflow-eu-central-2 "#inferentia-tensorflow-eu-central-2")
- [XGBoost (algorithm)](#xgboost-eu-central-2 "#xgboost-eu-central-2")

## AutoGluon (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='autogluon',region='eu-central-2',image_scope='inference',version='0.4')
```

| Registry path                                                               | Version | Job types (image scope) |
| --------------------------------------------------------------------------- | ------- | ----------------------- |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/autogluon-training:`<tag>`  | 0.5.2   | training                |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/autogluon-inference:`<tag>` | 0.5.2   | inference               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/autogluon-training:`<tag>`  | 0.4.3   | training                |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/autogluon-inference:`<tag>` | 0.4.3   | inference               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/autogluon-training:`<tag>`  | 0.4.2   | training                |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/autogluon-inference:`<tag>` | 0.4.2   | inference               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/autogluon-training:`<tag>`  | 0.4.0   | training                |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/autogluon-inference:`<tag>` | 0.4.0   | inference               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/autogluon-training:`<tag>`  | 0.3.2   | training                |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/autogluon-inference:`<tag>` | 0.3.2   | inference               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/autogluon-training:`<tag>`  | 0.3.1   | training                |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/autogluon-inference:`<tag>` | 0.3.1   | inference               |

## BlazingText (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='blazingtext',region='eu-central-2')
```

| Registry path                                                       | Version | Job types (image scope) |
| ------------------------------------------------------------------- | ------- | ----------------------- |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/blazingtext:`<tag>` | 1       | inference, training     |

## Clarify (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='clarify',region='eu-central-2',version='1.0',image_scope='processing')
```

| Registry path                                                                        | Version | Job types (image scope) |
| ------------------------------------------------------------------------------------ | ------- | ----------------------- |
| 730335477804.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-clarify-processing:`<tag>` | 1.0     | processing              |

## DeepAR Forecasting (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='forecasting-deepar',region='eu-central-2')
```

| Registry path                                                              | Version | Job types (image scope) |
| -------------------------------------------------------------------------- | ------- | ----------------------- |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/forecasting-deepar:`<tag>` | 1       | inference, training     |

## Factorization Machines (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='factorization-machines',region='eu-central-2')
```

| Registry path                                                                  | Version | Job types (image scope) |
| ------------------------------------------------------------------------------ | ------- | ----------------------- |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/factorization-machines:`<tag>` | 1       | inference, training     |

## Hugging Face (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='huggingface',region='eu-central-2',version='4.4.2',image_scope='training',base_framework_version='tensorflow2.4.1')
```

| Registry path                                                                            | Version | Job types (image scope) |
| ---------------------------------------------------------------------------------------- | ------- | ----------------------- |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-pytorch-inference:`<tag>`    | 4.49.0  | inference               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-pytorch-inference:`<tag>`    | 4.48.0  | inference               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-pytorch-inference:`<tag>`    | 4.37.0  | inference               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-pytorch-inference:`<tag>`    | 4.28.1  | inference               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-pytorch-inference:`<tag>`    | 4.26.0  | inference               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-tensorflow-inference:`<tag>` | 4.26.0  | inference               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.17.0  | training                |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-tensorflow-training:`<tag>`  | 4.17.0  | training                |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-pytorch-inference:`<tag>`    | 4.17.0  | inference               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-tensorflow-inference:`<tag>` | 4.17.0  | inference               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.12.3  | training                |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-tensorflow-training:`<tag>`  | 4.12.3  | training                |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-pytorch-inference:`<tag>`    | 4.12.3  | inference               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-tensorflow-inference:`<tag>` | 4.12.3  | inference               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.11.0  | training                |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-tensorflow-training:`<tag>`  | 4.11.0  | training                |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-pytorch-inference:`<tag>`    | 4.11.0  | inference               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-tensorflow-inference:`<tag>` | 4.11.0  | inference               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.10.2  | training                |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.10.2  | training                |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-tensorflow-training:`<tag>`  | 4.10.2  | training                |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-tensorflow-training:`<tag>`  | 4.10.2  | training                |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-pytorch-inference:`<tag>`    | 4.10.2  | inference               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-pytorch-inference:`<tag>`    | 4.10.2  | inference               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-tensorflow-inference:`<tag>` | 4.10.2  | inference               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-tensorflow-inference:`<tag>` | 4.10.2  | inference               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.6.1   | training                |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.6.1   | training                |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.6.1   | training                |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-tensorflow-training:`<tag>`  | 4.6.1   | training                |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-pytorch-inference:`<tag>`    | 4.6.1   | inference               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-tensorflow-inference:`<tag>` | 4.6.1   | inference               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.5.0   | training                |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-tensorflow-training:`<tag>`  | 4.5.0   | training                |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.4.2   | training                |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/huggingface-tensorflow-training:`<tag>`  | 4.4.2   | training                |

## IP Insights (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='ipinsights',region='eu-central-2')
```

| Registry path                                                      | Version | Job types (image scope) |
| ------------------------------------------------------------------ | ------- | ----------------------- |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/ipinsights:`<tag>` | 1       | inference, training     |

## Image classification (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='image-classification',region='eu-central-2')
```

| Registry path                                                                | Version | Job types (image scope) |
| ---------------------------------------------------------------------------- | ------- | ----------------------- |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/image-classification:`<tag>` | 1       | inference, training     |

## Inferentia MXNet (DLC)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='inferentia-mxnet',region='eu-central-2',version='1.5.1',instance_type='ml.inf1.6xlarge')
```

| Registry path                                                               | Version | Job types (image scope) | Processor types | Python versions |
| --------------------------------------------------------------------------- | ------- | ----------------------- | --------------- | --------------- |
| 010526262399.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-neo-mxnet:`<tag>` | 1.8     | inference               | inf             | py3             |
| 010526262399.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-neo-mxnet:`<tag>` | 1.5.1   | inference               | inf             | py3             |

## Inferentia PyTorch (DLC)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='inferentia-pytorch',region='eu-central-2',version='1.9',py_version='py3')
```

| Registry path                                                                 | Version | Job types (image scope) | Processor types | Python versions |
| ----------------------------------------------------------------------------- | ------- | ----------------------- | --------------- | --------------- |
| 010526262399.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-neo-pytorch:`<tag>` | 1.9     | inference               | inf             | py3             |
| 010526262399.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-neo-pytorch:`<tag>` | 1.8     | inference               | inf             | py3             |
| 010526262399.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-neo-pytorch:`<tag>` | 1.7     | inference               | inf             | py3             |

## K-Means (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='kmeans',region='eu-central-2')
```

| Registry path                                                  | Version | Job types (image scope) |
| -------------------------------------------------------------- | ------- | ----------------------- |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/kmeans:`<tag>` | 1       | inference, training     |

## KNN (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='knn',region='eu-central-2')
```

| Registry path                                               | Version | Job types (image scope) |
| ----------------------------------------------------------- | ------- | ----------------------- |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/knn:`<tag>` | 1       | inference, training     |

## Linear Learner (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='linear-learner',region='eu-central-2')
```

| Registry path                                                          | Version | Job types (image scope) |
| ---------------------------------------------------------------------- | ------- | ----------------------- |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/linear-learner:`<tag>` | 1       | inference, training     |

## MXNet (DLC)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='mxnet',region='eu-central-2',version='1.4.1',py_version='py3',image_scope='inference', instance_type='ml.c5.4xlarge')
```

| Registry path                                                               | Version | Job types (image scope) | Processor types | Python versions |
| --------------------------------------------------------------------------- | ------- | ----------------------- | --------------- | --------------- |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/mxnet-training:`<tag>`      | 1.9.0   | training                | CPU, GPU        | py38            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/mxnet-inference:`<tag>`     | 1.9.0   | inference               | CPU, GPU        | py38            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/mxnet-training:`<tag>`      | 1.8.0   | training                | CPU, GPU        | py37            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/mxnet-inference:`<tag>`     | 1.8.0   | inference               | CPU, GPU        | py37            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/mxnet-training:`<tag>`      | 1.7.0   | training                | CPU, GPU        | py3             |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/mxnet-inference:`<tag>`     | 1.7.0   | inference               | CPU, GPU        | py3             |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/mxnet-inference-eia:`<tag>` | 1.7.0   | eia                     | CPU             | py3             |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/mxnet-training:`<tag>`      | 1.6.0   | training                | CPU, GPU        | py2, py3        |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/mxnet-inference:`<tag>`     | 1.6.0   | inference               | CPU, GPU        | py2, py3        |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/mxnet-inference-eia:`<tag>` | 1.5.1   | eia                     | CPU             | py2, py3        |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/mxnet-training:`<tag>`      | 1.4.1   | training                | CPU, GPU        | py3             |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/mxnet-inference:`<tag>`     | 1.4.1   | inference               | CPU, GPU        | py3             |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/mxnet-inference-eia:`<tag>` | 1.4.1   | eia                     | CPU             | py2, py3        |

## Model Monitor (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='model-monitor',region='eu-central-2')
```

| Registry path                                                                            | Version | Job types (image scope) |
| ---------------------------------------------------------------------------------------- | ------- | ----------------------- |
| 590183933784.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-model-monitor-analyzer:`<tag>` |         | monitoring              |

## NTM (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='ntm',region='eu-central-2')
```

| Registry path                                               | Version | Job types (image scope) |
| ----------------------------------------------------------- | ------- | ----------------------- |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/ntm:`<tag>` | 1       | inference, training     |

## Neo Image Classification (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='image-classification-neo',region='eu-central-2')
```

| Registry path                                                                    | Version | Job types (image scope) |
| -------------------------------------------------------------------------------- | ------- | ----------------------- |
| 010526262399.dkr.ecr.eu-central-2.amazonaws.com/image-classification-neo:`<tag>` | latest  | inference               |

## Neo MXNet (DLC)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='neo-mxnet',region='eu-central-2',version='1.8',py_version='py3',image_scope='inference', instance_type='ml.c5.4xlarge')
```

| Registry path                                                                     | Version | Job types (image scope) | Processor types | Python versions |
| --------------------------------------------------------------------------------- | ------- | ----------------------- | --------------- | --------------- |
| 010526262399.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-inference-mxnet:`<tag>` | 1.8     | inference               | CPU, GPU        | py3             |

## Neo PyTorch (DLC)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='neo-pytorch',region='eu-central-2',version='1.6',image_scope='inference',instance_type='ml.c5.4xlarge')
```

| Registry path                                                                       | Version | Job types (image scope) | Processor types | Python versions |
| ----------------------------------------------------------------------------------- | ------- | ----------------------- | --------------- | --------------- |
| 010526262399.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-inference-pytorch:`<tag>` | 2.0     | inference               | CPU, GPU        | py3             |
| 010526262399.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-inference-pytorch:`<tag>` | 1.13    | inference               | CPU, GPU        | py3             |
| 010526262399.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-inference-pytorch:`<tag>` | 1.12    | inference               | CPU, GPU        | py3             |
| 010526262399.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-inference-pytorch:`<tag>` | 1.8     | inference               | CPU, GPU        | py3             |
| 010526262399.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-inference-pytorch:`<tag>` | 1.7     | inference               | CPU, GPU        | py3             |
| 010526262399.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-inference-pytorch:`<tag>` | 1.6     | inference               | CPU, GPU        | py3             |
| 010526262399.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-inference-pytorch:`<tag>` | 1.5     | inference               | CPU, GPU        | py3             |
| 010526262399.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-inference-pytorch:`<tag>` | 1.4     | inference               | CPU, GPU        | py3             |

## Neo Tensorflow (DLC)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='neo-tensorflow',region='eu-central-2',version='1.15.3',py_version='py3',instance_type='ml.c5.4xlarge')
```

| Registry path                                                                          | Version | Job types (image scope) | Processor types | Python versions |
| -------------------------------------------------------------------------------------- | ------- | ----------------------- | --------------- | --------------- |
| 010526262399.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-inference-tensorflow:`<tag>` | 2.9.2   | inference               | CPU, GPU        | py3             |
| 010526262399.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-inference-tensorflow:`<tag>` | 1.15.3  | inference               | CPU, GPU        | py3             |

## Neo XGBoost (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='xgboost-neo',region='eu-central-2')
```

| Registry path                                                       | Version | Job types (image scope) |
| ------------------------------------------------------------------- | ------- | ----------------------- |
| 010526262399.dkr.ecr.eu-central-2.amazonaws.com/xgboost-neo:`<tag>` | latest  | inference               |

## Object Detection (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='object-detection',region='eu-central-2')
```

| Registry path                                                            | Version | Job types (image scope) |
| ------------------------------------------------------------------------ | ------- | ----------------------- |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/object-detection:`<tag>` | 1       | inference, training     |

## Object2Vec (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='object2vec',region='eu-central-2')
```

| Registry path                                                      | Version | Job types (image scope) |
| ------------------------------------------------------------------ | ------- | ----------------------- |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/object2vec:`<tag>` | 1       | inference, training     |

## PCA (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='pca',region='eu-central-2')
```

| Registry path                                               | Version | Job types (image scope) |
| ----------------------------------------------------------- | ------- | ----------------------- |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/pca:`<tag>` | 1       | inference, training     |

## PyTorch (DLC)

For information about the supported and unsupported PyTorch versions, see the [Framework Support Policy Table](../../../deep-learning-containers/latest/devguide/dlc-framework-support-policy.md "../../../deep-learning-containers/latest/devguide/dlc-framework-support-policy.md")
in the _AWS Deep Learning Containers Developer Guide_.

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='pytorch',region='eu-central-2',version='1.8.0',py_version='py3',image_scope='inference', instance_type='ml.c5.4xlarge')
```

| Registry path                                                                      | Version | Job types (image scope) | Processor types | Python versions |
| ---------------------------------------------------------------------------------- | ------- | ----------------------- | --------------- | --------------- |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-training:`<tag>`           | 2.7.1   | training                | CPU, GPU        | py312           |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-inference:`<tag>`          | 2.6.0   | inference               | CPU, GPU        | py312           |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-training:`<tag>`           | 2.6.0   | training                | CPU, GPU        | py312           |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-inference:`<tag>`          | 2.5.1   | inference               | CPU, GPU        | py311           |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-training:`<tag>`           | 2.5.1   | training                | CPU, GPU        | py311           |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-inference:`<tag>`          | 2.4.0   | inference               | CPU, GPU        | py311           |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-inference-graviton:`<tag>` | 2.4.0   | inference_graviton      | CPU             | py311           |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-training:`<tag>`           | 2.4.0   | training                | CPU, GPU        | py311           |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-inference:`<tag>`          | 2.3.0   | inference               | CPU, GPU        | py311           |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-inference-graviton:`<tag>` | 2.3.0   | inference_graviton      | CPU             | py311           |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-training:`<tag>`           | 2.3.0   | training                | CPU, GPU        | py311           |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-inference-graviton:`<tag>` | 2.2.1   | inference_graviton      | CPU             | py310           |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-inference:`<tag>`          | 2.2.0   | inference               | CPU, GPU        | py310           |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-training:`<tag>`           | 2.2.0   | training                | CPU, GPU        | py310           |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-inference:`<tag>`          | 2.1.0   | inference               | CPU, GPU        | py310           |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-inference-graviton:`<tag>` | 2.1.0   | inference_graviton      | CPU             | py310           |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-training:`<tag>`           | 2.1.0   | training                | CPU, GPU        | py310           |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-inference:`<tag>`          | 2.0.1   | inference               | CPU, GPU        | py310           |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-inference-graviton:`<tag>` | 2.0.1   | inference_graviton      | CPU             | py310           |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-training:`<tag>`           | 2.0.1   | training                | CPU, GPU        | py310           |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-inference:`<tag>`          | 2.0.0   | inference               | CPU, GPU        | py310           |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-inference-graviton:`<tag>` | 2.0.0   | inference_graviton      | CPU             | py310           |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-training:`<tag>`           | 2.0.0   | training                | CPU, GPU        | py310           |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-inference:`<tag>`          | 1.13.1  | inference               | CPU, GPU        | py39            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-training:`<tag>`           | 1.13.1  | training                | CPU, GPU        | py39            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-inference:`<tag>`          | 1.12.1  | inference               | CPU, GPU        | py38            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-inference-graviton:`<tag>` | 1.12.1  | inference_graviton      | CPU             | py38            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-training:`<tag>`           | 1.12.1  | training                | CPU, GPU        | py38            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-inference:`<tag>`          | 1.12.0  | inference               | CPU, GPU        | py38            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-training:`<tag>`           | 1.12.0  | training                | CPU, GPU        | py38            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-inference:`<tag>`          | 1.11.0  | inference               | CPU, GPU        | py38            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-training:`<tag>`           | 1.11.0  | training                | CPU, GPU        | py38            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-inference:`<tag>`          | 1.10.2  | inference               | CPU, GPU        | py38            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-training:`<tag>`           | 1.10.2  | training                | CPU, GPU        | py38            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-inference:`<tag>`          | 1.10.0  | inference               | CPU, GPU        | py38            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-training:`<tag>`           | 1.10.0  | training                | CPU, GPU        | py38            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-inference:`<tag>`          | 1.9.1   | inference               | CPU, GPU        | py38            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-training:`<tag>`           | 1.9.1   | training                | CPU, GPU        | py38            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-inference:`<tag>`          | 1.9.0   | inference               | CPU, GPU        | py38            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-training:`<tag>`           | 1.9.0   | training                | CPU, GPU        | py38            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-inference:`<tag>`          | 1.8.1   | inference               | CPU, GPU        | py3, py36       |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-training:`<tag>`           | 1.8.1   | training                | CPU, GPU        | py3, py36       |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-inference:`<tag>`          | 1.8.0   | inference               | CPU, GPU        | py3, py36       |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-training:`<tag>`           | 1.8.0   | training                | CPU, GPU        | py3, py36       |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-inference:`<tag>`          | 1.7.1   | inference               | CPU, GPU        | py3, py36       |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-training:`<tag>`           | 1.7.1   | training                | CPU, GPU        | py3, py36       |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-inference:`<tag>`          | 1.6.0   | inference               | CPU, GPU        | py3, py36       |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-training:`<tag>`           | 1.6.0   | training                | CPU, GPU        | py3, py36       |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-inference-eia:`<tag>`      | 1.5.1   | eia                     | CPU             | py3             |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-inference:`<tag>`          | 1.5.0   | inference               | CPU, GPU        | py3, py36       |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-training:`<tag>`           | 1.5.0   | training                | CPU, GPU        | py3, py36       |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-inference:`<tag>`          | 1.4.0   | inference               | CPU, GPU        | py3, py36       |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-training:`<tag>`           | 1.4.0   | training                | CPU, GPU        | py2, py3, py36  |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-inference-eia:`<tag>`      | 1.3.1   | eia                     | CPU             | py3             |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-inference:`<tag>`          | 1.3.1   | inference               | CPU, GPU        | py2, py3        |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-training:`<tag>`           | 1.3.1   | training                | CPU, GPU        | py2, py3        |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-inference:`<tag>`          | 1.2.0   | inference               | CPU, GPU        | py2, py3        |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-training:`<tag>`           | 1.2.0   | training                | CPU, GPU        | py2, py3        |

## PyTorch Neuron (DLC)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='pytorch-neuron',region='us-west-2', image_scope='inference')
```

| Registry path                                                                   | Version | Job types (image scope) | Processor types | Python versions |
| ------------------------------------------------------------------------------- | ------- | ----------------------- | --------------- | --------------- |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-training-neuron:`<tag>` | 1.11.0  | training                | TRN             | py38            |

## PyTorch Training Compiler (DLC)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='pytorch-training-compiler',region='us-west-2', version='py38')
```

| Registry path                                                                   | Version | Job types (image scope) | Processor types | Python versions |
| ------------------------------------------------------------------------------- | ------- | ----------------------- | --------------- | --------------- |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/pytorch-trcomp-training:`<tag>` | 1.12.0  | training                | GPU             | py38            |

## Random Cut Forest (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='randomcutforest',region='eu-central-2')
```

| Registry path                                                           | Version | Job types (image scope) |
| ----------------------------------------------------------------------- | ------- | ----------------------- |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/randomcutforest:`<tag>` | 1       | inference, training     |

## Scikit-learn (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='sklearn',region='eu-central-2',version='0.23-1',image_scope='inference')
```

| Registry path                                                                  | Version | Package version | Job types (image scope) |
| ------------------------------------------------------------------------------ | ------- | --------------- | ----------------------- |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-scikit-learn:`<tag>` | 1.2-1   | 1.2.1           | inference               |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-scikit-learn:`<tag>` | 1.2-1   | 1.2.1           | training                |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-scikit-learn:`<tag>` | 1.0-1   | 1.0.2           | inference               |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-scikit-learn:`<tag>` | 1.0-1   | 1.0.2           | training                |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-scikit-learn:`<tag>` | 1.0-1   | 1.0.2           | inference_graviton      |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-scikit-learn:`<tag>` | 0.23-1  | 0.23.2          | inference               |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-scikit-learn:`<tag>` | 0.23-1  | 0.23.2          | training                |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-scikit-learn:`<tag>` | 0.20.0  | 0.20.0          | inference               |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-scikit-learn:`<tag>` | 0.20.0  | 0.20.0          | training                |

## Semantic Segmentation (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='semantic-segmentation',region='eu-central-2')
```

| Registry path                                                                 | Version | Job types (image scope) |
| ----------------------------------------------------------------------------- | ------- | ----------------------- |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/semantic-segmentation:`<tag>` | 1       | inference, training     |

## Seq2Seq (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='seq2seq',region='eu-central-2')
```

| Registry path                                                   | Version | Job types (image scope) |
| --------------------------------------------------------------- | ------- | ----------------------- |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/seq2seq:`<tag>` | 1       | inference, training     |

## Spark (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='spark',region='eu-central-2',version='3.0',image_scope='processing')
```

| Registry path                                                                      | Version | Job types (image scope) |
| ---------------------------------------------------------------------------------- | ------- | ----------------------- |
| 142351485170.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-spark-processing:`<tag>` | 3.3     | processing              |
| 142351485170.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-spark-processing:`<tag>` | 3.2     | processing              |
| 142351485170.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-spark-processing:`<tag>` | 3.1     | processing              |
| 142351485170.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-spark-processing:`<tag>` | 3.0     | processing              |
| 142351485170.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-spark-processing:`<tag>` | 2.4     | processing              |

## Tensorflow (DLC)

For information about the supported and unsupported TensorFlow versions, see the [Framework Support Policy Table](../../../deep-learning-containers/latest/devguide/dlc-framework-support-policy.md "../../../deep-learning-containers/latest/devguide/dlc-framework-support-policy.md")
in the _AWS Deep Learning Containers Developer Guide_.

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='tensorflow',region='eu-central-2',version='1.12.0',image_scope='inference',instance_type='ml.c5.4xlarge')
```

| Registry path                                                                         | Version | Job types (image scope) | Processor types | Python versions |
| ------------------------------------------------------------------------------------- | ------- | ----------------------- | --------------- | --------------- |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.19.0  | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.19.0  | training                | CPU, GPU        | py312           |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.18.0  | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.18.0  | training                | CPU, GPU        | py310           |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.16.2  | training                | CPU, GPU        | py310           |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.16.1  | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference-graviton:`<tag>` | 2.16.1  | inference_graviton      | CPU             | py310           |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.14.1  | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference-graviton:`<tag>` | 2.14.1  | inference_graviton      | CPU             | py310           |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.14.1  | training                | CPU, GPU        | py310           |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.13.0  | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference-graviton:`<tag>` | 2.13.0  | inference_graviton      | CPU             | py310           |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.13.0  | training                | CPU, GPU        | py310           |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.12.1  | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference-graviton:`<tag>` | 2.12.1  | inference_graviton      | CPU             | py310           |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.12.0  | training                | CPU, GPU        | py310           |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.11.1  | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.11.0  | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.11.0  | training                | CPU, GPU        | py39            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.10.1  | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.10.1  | training                | CPU, GPU        | py39            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.10.0  | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.9.3   | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.9.2   | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.9.2   | training                | CPU, GPU        | py39            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference-graviton:`<tag>` | 2.9.1   | inference_graviton      | CPU             | py38            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.8.4   | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.8.0   | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.8.0   | training                | CPU, GPU        | py39            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.7.1   | training                | CPU, GPU        | py38            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.7.0   | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.6.3   | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.6.3   | training                | CPU, GPU        | py38            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.6.2   | training                | CPU, GPU        | py38            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.6.0   | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.6.0   | training                | CPU, GPU        | py38            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.5.1   | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.5.1   | training                | CPU, GPU        | py37            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.5.0   | training                | CPU, GPU        | py37            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.4.3   | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.4.3   | training                | CPU, GPU        | py37            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.4.1   | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.4.1   | training                | CPU, GPU        | py37            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.3.2   | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.3.2   | training                | CPU, GPU        | py37            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.3.1   | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.3.1   | training                | CPU, GPU        | py37            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference-eia:`<tag>`      | 2.3.0   | eia                     | CPU             | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.3.0   | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.3.0   | training                | CPU, GPU        | py37            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.2.2   | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.2.2   | training                | CPU, GPU        | py37            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.2.1   | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.2.1   | training                | CPU, GPU        | py37            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.2.0   | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.2.0   | training                | CPU, GPU        | py37            |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.1.3   | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.1.3   | training                | CPU, GPU        | py3, py36       |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.1.2   | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.1.2   | training                | CPU, GPU        | py3, py36       |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.1.1   | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.1.1   | training                | CPU, GPU        | py2, py3        |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.1.0   | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.1.0   | training                | CPU, GPU        | py2, py3        |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.0.4   | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.0.4   | training                | CPU, GPU        | py3, py36       |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.0.3   | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.0.3   | training                | CPU, GPU        | py3, py36       |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.0.2   | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.0.2   | training                | CPU, GPU        | py2, py3        |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.0.1   | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.0.1   | training                | CPU, GPU        | py2, py3        |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference-eia:`<tag>`      | 2.0.0   | eia                     | CPU             | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 2.0.0   | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 2.0.0   | training                | CPU, GPU        | py2, py3        |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 1.15.5  | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 1.15.5  | training                | CPU, GPU        | py3, py36, py37 |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 1.15.4  | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 1.15.4  | training                | CPU, GPU        | py3, py36, py37 |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 1.15.3  | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 1.15.3  | training                | CPU, GPU        | py2, py3, py37  |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 1.15.2  | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 1.15.2  | training                | CPU, GPU        | py2, py3, py37  |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference-eia:`<tag>`      | 1.15.0  | eia                     | CPU             | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 1.15.0  | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 1.15.0  | training                | CPU, GPU        | py2, py3        |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference-eia:`<tag>`      | 1.14.0  | eia                     | CPU             | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 1.14.0  | inference               | CPU, GPU        | -               |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 1.14.0  | training                | CPU, GPU        | py2, py3        |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-training:`<tag>`           | 1.13.1  | training                | CPU, GPU        | py3             |
| 380420809688.dkr.ecr.eu-central-2.amazonaws.com/tensorflow-inference:`<tag>`          | 1.13.0  | inference               | CPU, GPU        | -               |

## Tensorflow Inferentia (DLC)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='inferentia-tensorflow',region='eu-central-2',version='1.15.0',instance_type='ml.inf1.6xlarge')
```

| Registry path                                                                    | Version | Job types (image scope) | Processor types | Python versions |
| -------------------------------------------------------------------------------- | ------- | ----------------------- | --------------- | --------------- |
| 010526262399.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-neo-tensorflow:`<tag>` | 2.5.2   | inference               | inf             | py3             |
| 010526262399.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-neo-tensorflow:`<tag>` | 1.15.0  | inference               | inf             | py3             |

## XGBoost (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='xgboost',region='eu-central-2',version='1.5-1')
```

| Registry path                                                             | Version | Package version | Job types (image scope) |
| ------------------------------------------------------------------------- | ------- | --------------- | ----------------------- |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.7-1   | 1.7.4           | inference               |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.7-1   | 1.7.4           | training                |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.5-1   | 1.5.2           | inference               |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.5-1   | 1.5.2           | training                |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.5-1   | 1.5.2           | inference_graviton      |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.3-1   | 1.3.3           | inference               |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.3-1   | 1.3.3           | training                |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.3-1   | 1.3.3           | inference_graviton      |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.2-2   | 1.2.0           | inference               |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.2-2   | 1.2.0           | training                |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.2-1   | 1.2.0           | inference               |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.2-1   | 1.2.0           | training                |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.0-1   | 1.0.0           | inference               |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.0-1   | 1.0.0           | training                |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/xgboost:`<tag>`           | 1       | 0.72            | inference               |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/xgboost:`<tag>`           | 1       | 0.72            | training                |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 0.90-2  | 0.90            | inference               |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 0.90-2  | 0.90            | training                |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 0.90-1  | 0.90            | inference               |
| 680994064768.dkr.ecr.eu-central-2.amazonaws.com/sagemaker-xgboost:`<tag>` | 0.90-1  | 0.90            | training                |
