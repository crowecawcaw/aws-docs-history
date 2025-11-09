# Docker Registry Paths and Example Code for Europe (Paris) (eu-west-3)

The following topics list parameters for each of the algorithms and deep learning containers that are provided by Amazon SageMaker AI in this AWS Region.

###### Topics

- [AutoGluon (algorithm)](#autogluon-eu-west-3 "#autogluon-eu-west-3")
- [BlazingText (algorithm)](#blazingtext-eu-west-3 "#blazingtext-eu-west-3")
- [Chainer (DLC)](#chainer-eu-west-3 "#chainer-eu-west-3")
- [Clarify (algorithm)](#clarify-eu-west-3 "#clarify-eu-west-3")
- [DJL DeepSpeed (algorithm)](#djl-deepspeed-eu-west-3 "#djl-deepspeed-eu-west-3")
- [Data Wrangler (algorithm)](#data-wrangler-eu-west-3 "#data-wrangler-eu-west-3")
- [Debugger (algorithm)](#debugger-eu-west-3 "#debugger-eu-west-3")
- [DeepAR Forecasting (algorithm)](#forecasting-deepar-eu-west-3 "#forecasting-deepar-eu-west-3")
- [Factorization Machines (algorithm)](#factorization-machines-eu-west-3 "#factorization-machines-eu-west-3")
- [Hugging Face (algorithm)](#huggingface-eu-west-3 "#huggingface-eu-west-3")
- [IP Insights (algorithm)](#ipinsights-eu-west-3 "#ipinsights-eu-west-3")
- [Image classification (algorithm)](#image-classification-eu-west-3 "#image-classification-eu-west-3")
- [Inferentia MXNet (DLC)](#inferentia-mxnet-eu-west-3 "#inferentia-mxnet-eu-west-3")
- [Inferentia PyTorch (DLC)](#inferentia-pytorch-eu-west-3 "#inferentia-pytorch-eu-west-3")
- [K-Means (algorithm)](#kmeans-eu-west-3 "#kmeans-eu-west-3")
- [KNN (algorithm)](#knn-eu-west-3 "#knn-eu-west-3")
- [Linear Learner (algorithm)](#linear-learner-eu-west-3 "#linear-learner-eu-west-3")
- [MXNet (DLC)](#mxnet-eu-west-3 "#mxnet-eu-west-3")
- [MXNet Coach (DLC)](#coach-mxnet-eu-west-3 "#coach-mxnet-eu-west-3")
- [Model Monitor (algorithm)](#model-monitor-eu-west-3 "#model-monitor-eu-west-3")
- [NTM (algorithm)](#ntm-eu-west-3 "#ntm-eu-west-3")
- [Neo Image Classification (algorithm)](#image-classification-neo-eu-west-3 "#image-classification-neo-eu-west-3")
- [Neo MXNet (DLC)](#neo-mxnet-eu-west-3 "#neo-mxnet-eu-west-3")
- [Neo PyTorch (DLC)](#neo-pytorch-eu-west-3 "#neo-pytorch-eu-west-3")
- [Neo Tensorflow (DLC)](#neo-tensorflow-eu-west-3 "#neo-tensorflow-eu-west-3")
- [Neo XGBoost (algorithm)](#xgboost-neo-eu-west-3 "#xgboost-neo-eu-west-3")
- [Object Detection (algorithm)](#object-detection-eu-west-3 "#object-detection-eu-west-3")
- [Object2Vec (algorithm)](#object2vec-eu-west-3 "#object2vec-eu-west-3")
- [PCA (algorithm)](#pca-eu-west-3 "#pca-eu-west-3")
- [PyTorch (DLC)](#pytorch-eu-west-3 "#pytorch-eu-west-3")
- [PyTorch Neuron (DLC)](#pytorch-neuron-eu-west-3 "#pytorch-neuron-eu-west-3")
- [PyTorch Training Compiler (DLC)](#pytorch-training-compiler-eu-west-3 "#pytorch-training-compiler-eu-west-3")
- [Random Cut Forest (algorithm)](#randomcutforest-eu-west-3 "#randomcutforest-eu-west-3")
- [Scikit-learn (algorithm)](#sklearn-eu-west-3 "#sklearn-eu-west-3")
- [Semantic Segmentation (algorithm)](#semantic-segmentation-eu-west-3 "#semantic-segmentation-eu-west-3")
- [Seq2Seq (algorithm)](#seq2seq-eu-west-3 "#seq2seq-eu-west-3")
- [Spark (algorithm)](#spark-eu-west-3 "#spark-eu-west-3")
- [SparkML Serving (algorithm)](#sparkml-serving-eu-west-3 "#sparkml-serving-eu-west-3")
- [Tensorflow (DLC)](#tensorflow-eu-west-3 "#tensorflow-eu-west-3")
- [Tensorflow Coach (DLC)](#coach-tensorflow-eu-west-3 "#coach-tensorflow-eu-west-3")
- [Tensorflow Inferentia (DLC)](#inferentia-tensorflow-eu-west-3 "#inferentia-tensorflow-eu-west-3")
- [Tensorflow Ray (DLC)](#ray-tensorflow-eu-west-3 "#ray-tensorflow-eu-west-3")
- [XGBoost (algorithm)](#xgboost-eu-west-3 "#xgboost-eu-west-3")

## AutoGluon (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='autogluon',region='eu-west-3',image_scope='inference',version='0.4')
```

| Registry path                                                            | Version | Job types (image scope) |
| ------------------------------------------------------------------------ | ------- | ----------------------- |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/autogluon-training:`<tag>`  | 1.3.0   | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/autogluon-inference:`<tag>` | 1.3.0   | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/autogluon-training:`<tag>`  | 1.2.0   | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/autogluon-inference:`<tag>` | 1.2.0   | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/autogluon-training:`<tag>`  | 1.1.1   | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/autogluon-inference:`<tag>` | 1.1.1   | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/autogluon-training:`<tag>`  | 1.1.0   | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/autogluon-inference:`<tag>` | 1.1.0   | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/autogluon-training:`<tag>`  | 1.0.0   | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/autogluon-inference:`<tag>` | 1.0.0   | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/autogluon-training:`<tag>`  | 0.8.2   | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/autogluon-inference:`<tag>` | 0.8.2   | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/autogluon-training:`<tag>`  | 0.7.0   | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/autogluon-inference:`<tag>` | 0.7.0   | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/autogluon-training:`<tag>`  | 0.6.2   | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/autogluon-inference:`<tag>` | 0.6.2   | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/autogluon-training:`<tag>`  | 0.6.1   | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/autogluon-inference:`<tag>` | 0.6.1   | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/autogluon-training:`<tag>`  | 0.5.2   | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/autogluon-inference:`<tag>` | 0.5.2   | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/autogluon-training:`<tag>`  | 0.4.3   | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/autogluon-inference:`<tag>` | 0.4.3   | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/autogluon-training:`<tag>`  | 0.4.2   | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/autogluon-inference:`<tag>` | 0.4.2   | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/autogluon-training:`<tag>`  | 0.4.0   | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/autogluon-inference:`<tag>` | 0.4.0   | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/autogluon-training:`<tag>`  | 0.3.2   | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/autogluon-inference:`<tag>` | 0.3.2   | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/autogluon-training:`<tag>`  | 0.3.1   | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/autogluon-inference:`<tag>` | 0.3.1   | inference               |

## BlazingText (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='blazingtext',region='eu-west-3')
```

| Registry path                                                    | Version | Job types (image scope) |
| ---------------------------------------------------------------- | ------- | ----------------------- |
| 749696950732.dkr.ecr.eu-west-3.amazonaws.com/blazingtext:`<tag>` | 1       | inference, training     |

## Chainer (DLC)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='chainer',region='eu-west-3',version='5.0.0',py_version='py3',image_scope='inference',instance_type='ml.c5.4xlarge')
```

| Registry path                                                          | Version | Job types (image scope) | Processor types | Python versions |
| ---------------------------------------------------------------------- | ------- | ----------------------- | --------------- | --------------- |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-chainer:`<tag>` | 5.0.0   | inference, training     | CPU, GPU        | py2, py3        |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-chainer:`<tag>` | 4.1.0   | inference, training     | CPU, GPU        | py2, py3        |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-chainer:`<tag>` | 4.0.0   | inference, training     | CPU, GPU        | py2, py3        |

## Clarify (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='clarify',region='eu-west-3',version='1.0',image_scope='processing')
```

| Registry path                                                                     | Version | Job types (image scope) |
| --------------------------------------------------------------------------------- | ------- | ----------------------- |
| 341593696636.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-clarify-processing:`<tag>` | 1.0     | processing              |

## DJL DeepSpeed (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='djl-deepspeed', region='us-west-2',py_version='py3',image_scope='inference')
```

| Registry path                                                                                   | Version | Job types (image scope) |
| ----------------------------------------------------------------------------------------------- | ------- | ----------------------- |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/djl-inference:0.27.0-deepspeed0.12.6-cu121-`<tag>` | 0.27.0  | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/djl-inference:0.26.0-deepspeed0.12.6-cu121-`<tag>` | 0.26.0  | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/djl-inference:0.25.0-deepspeed0.11.0-cu118-`<tag>` | 0.25.0  | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/djl-inference:0.24.0-deepspeed0.10.0-cu118-`<tag>` | 0.24.0  | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/djl-inference:0.23.0-deepspeed0.9.5-cu118-`<tag>`  | 0.23.0  | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/djl-inference:0.22.1-deepspeed0.9.2-cu118-`<tag>`  | 0.22.1  | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/djl-inference:0.21.0-deepspeed0.8.3-cu117-`<tag>`  | 0.21.0  | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/djl-inference:0.20.0-deepspeed0.7.5-cu116-`<tag>`  | 0.20.0  | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/djl-inference:0.19.0-deepspeed0.7.3-cu113-`<tag>`  | 0.19.0  | inference               |

## Data Wrangler (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='data-wrangler',region='eu-west-3')
```

| Registry path                                                                          | Version | Job types (image scope) |
| -------------------------------------------------------------------------------------- | ------- | ----------------------- |
| 807237891255.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-data-wrangler-container:`<tag>` | 3.x     | processing              |
| 807237891255.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-data-wrangler-container:`<tag>` | 2.x     | processing              |
| 807237891255.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-data-wrangler-container:`<tag>` | 1.x     | processing              |

## Debugger (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='debugger',region='eu-west-3')
```

| Registry path                                                                 | Version | Job types (image scope) |
| ----------------------------------------------------------------------------- | ------- | ----------------------- |
| 447278800020.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-debugger-rules:`<tag>` | latest  | debugger                |

## DeepAR Forecasting (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='forecasting-deepar',region='eu-west-3')
```

| Registry path                                                           | Version | Job types (image scope) |
| ----------------------------------------------------------------------- | ------- | ----------------------- |
| 749696950732.dkr.ecr.eu-west-3.amazonaws.com/forecasting-deepar:`<tag>` | 1       | inference, training     |

## Factorization Machines (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='factorization-machines',region='eu-west-3')
```

| Registry path                                                               | Version | Job types (image scope) |
| --------------------------------------------------------------------------- | ------- | ----------------------- |
| 749696950732.dkr.ecr.eu-west-3.amazonaws.com/factorization-machines:`<tag>` | 1       | inference, training     |

## Hugging Face (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='huggingface',region='eu-west-3',version='4.4.2',image_scope='training',base_framework_version='tensorflow2.4.1')
```

| Registry path                                                                         | Version | Job types (image scope) |
| ------------------------------------------------------------------------------------- | ------- | ----------------------- |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.49.0  | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-pytorch-inference:`<tag>`    | 4.49.0  | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.48.0  | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-pytorch-inference:`<tag>`    | 4.48.0  | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.46.1  | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-pytorch-inference:`<tag>`    | 4.37.0  | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.36.0  | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.28.1  | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-pytorch-inference:`<tag>`    | 4.28.1  | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.26.0  | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-pytorch-inference:`<tag>`    | 4.26.0  | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-tensorflow-inference:`<tag>` | 4.26.0  | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.17.0  | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-tensorflow-training:`<tag>`  | 4.17.0  | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-pytorch-inference:`<tag>`    | 4.17.0  | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-tensorflow-inference:`<tag>` | 4.17.0  | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.12.3  | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-tensorflow-training:`<tag>`  | 4.12.3  | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-pytorch-inference:`<tag>`    | 4.12.3  | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-tensorflow-inference:`<tag>` | 4.12.3  | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.11.0  | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-tensorflow-training:`<tag>`  | 4.11.0  | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-pytorch-inference:`<tag>`    | 4.11.0  | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-tensorflow-inference:`<tag>` | 4.11.0  | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.10.2  | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.10.2  | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-tensorflow-training:`<tag>`  | 4.10.2  | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-tensorflow-training:`<tag>`  | 4.10.2  | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-pytorch-inference:`<tag>`    | 4.10.2  | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-pytorch-inference:`<tag>`    | 4.10.2  | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-tensorflow-inference:`<tag>` | 4.10.2  | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-tensorflow-inference:`<tag>` | 4.10.2  | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.6.1   | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.6.1   | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.6.1   | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-tensorflow-training:`<tag>`  | 4.6.1   | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-pytorch-inference:`<tag>`    | 4.6.1   | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-tensorflow-inference:`<tag>` | 4.6.1   | inference               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.5.0   | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-tensorflow-training:`<tag>`  | 4.5.0   | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-pytorch-training:`<tag>`     | 4.4.2   | training                |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/huggingface-tensorflow-training:`<tag>`  | 4.4.2   | training                |

## IP Insights (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='ipinsights',region='eu-west-3')
```

| Registry path                                                   | Version | Job types (image scope) |
| --------------------------------------------------------------- | ------- | ----------------------- |
| 749696950732.dkr.ecr.eu-west-3.amazonaws.com/ipinsights:`<tag>` | 1       | inference, training     |

## Image classification (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='image-classification',region='eu-west-3')
```

| Registry path                                                             | Version | Job types (image scope) |
| ------------------------------------------------------------------------- | ------- | ----------------------- |
| 749696950732.dkr.ecr.eu-west-3.amazonaws.com/image-classification:`<tag>` | 1       | inference, training     |

## Inferentia MXNet (DLC)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='inferentia-mxnet',region='eu-west-3',version='1.5.1',instance_type='ml.inf1.6xlarge')
```

| Registry path                                                            | Version | Job types (image scope) | Processor types | Python versions |
| ------------------------------------------------------------------------ | ------- | ----------------------- | --------------- | --------------- |
| 254080097072.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-neo-mxnet:`<tag>` | 1.8     | inference               | inf             | py3             |
| 254080097072.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-neo-mxnet:`<tag>` | 1.5.1   | inference               | inf             | py3             |

## Inferentia PyTorch (DLC)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='inferentia-pytorch',region='eu-west-3',version='1.9',py_version='py3')
```

| Registry path                                                              | Version | Job types (image scope) | Processor types | Python versions |
| -------------------------------------------------------------------------- | ------- | ----------------------- | --------------- | --------------- |
| 254080097072.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-neo-pytorch:`<tag>` | 1.9     | inference               | inf             | py3             |
| 254080097072.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-neo-pytorch:`<tag>` | 1.8     | inference               | inf             | py3             |
| 254080097072.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-neo-pytorch:`<tag>` | 1.7     | inference               | inf             | py3             |

## K-Means (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='kmeans',region='eu-west-3')
```

| Registry path                                               | Version | Job types (image scope) |
| ----------------------------------------------------------- | ------- | ----------------------- |
| 749696950732.dkr.ecr.eu-west-3.amazonaws.com/kmeans:`<tag>` | 1       | inference, training     |

## KNN (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='knn',region='eu-west-3')
```

| Registry path                                            | Version | Job types (image scope) |
| -------------------------------------------------------- | ------- | ----------------------- |
| 749696950732.dkr.ecr.eu-west-3.amazonaws.com/knn:`<tag>` | 1       | inference, training     |

## Linear Learner (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='linear-learner',region='eu-west-3')
```

| Registry path                                                       | Version | Job types (image scope) |
| ------------------------------------------------------------------- | ------- | ----------------------- |
| 749696950732.dkr.ecr.eu-west-3.amazonaws.com/linear-learner:`<tag>` | 1       | inference, training     |

## MXNet (DLC)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='mxnet',region='eu-west-3',version='1.4.1',py_version='py3',image_scope='inference', instance_type='ml.c5.4xlarge')
```

| Registry path                                                                    | Version | Job types (image scope) | Processor types | Python versions |
| -------------------------------------------------------------------------------- | ------- | ----------------------- | --------------- | --------------- |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/mxnet-training:`<tag>`              | 1.9.0   | training                | CPU, GPU        | py38            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/mxnet-inference:`<tag>`             | 1.9.0   | inference               | CPU, GPU        | py38            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/mxnet-training:`<tag>`              | 1.8.0   | training                | CPU, GPU        | py37            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/mxnet-inference:`<tag>`             | 1.8.0   | inference               | CPU, GPU        | py37            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/mxnet-training:`<tag>`              | 1.7.0   | training                | CPU, GPU        | py3             |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/mxnet-inference:`<tag>`             | 1.7.0   | inference               | CPU, GPU        | py3             |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/mxnet-inference-eia:`<tag>`         | 1.7.0   | eia                     | CPU             | py3             |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/mxnet-training:`<tag>`              | 1.6.0   | training                | CPU, GPU        | py2, py3        |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/mxnet-inference:`<tag>`             | 1.6.0   | inference               | CPU, GPU        | py2, py3        |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/mxnet-inference-eia:`<tag>`         | 1.5.1   | eia                     | CPU             | py2, py3        |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-mxnet:`<tag>`             | 1.4.1   | training                | CPU, GPU        | py2             |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/mxnet-training:`<tag>`              | 1.4.1   | training                | CPU, GPU        | py3             |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-mxnet-serving:`<tag>`     | 1.4.1   | inference               | CPU, GPU        | py2             |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/mxnet-inference:`<tag>`             | 1.4.1   | inference               | CPU, GPU        | py3             |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/mxnet-inference-eia:`<tag>`         | 1.4.1   | eia                     | CPU             | py2, py3        |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-mxnet:`<tag>`             | 1.4.0   | training                | CPU, GPU        | py2, py3        |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-mxnet-serving:`<tag>`     | 1.4.0   | inference               | CPU, GPU        | py2, py3        |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-mxnet-serving-eia:`<tag>` | 1.4.0   | eia                     | CPU             | py2, py3        |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-mxnet:`<tag>`             | 1.3.0   | training                | CPU, GPU        | py2, py3        |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-mxnet:`<tag>`             | 1.3.0   | inference               | CPU, GPU        | py2, py3        |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-mxnet-eia:`<tag>`         | 1.3.0   | eia                     | CPU             | py2, py3        |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-mxnet:`<tag>`             | 1.2.1   | training                | CPU, GPU        | py2, py3        |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-mxnet:`<tag>`             | 1.2.1   | inference               | CPU, GPU        | py2, py3        |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-mxnet:`<tag>`             | 1.1.0   | training                | CPU, GPU        | py2, py3        |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-mxnet:`<tag>`             | 1.1.0   | inference               | CPU, GPU        | py2, py3        |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-mxnet:`<tag>`             | 1.0.0   | training                | CPU, GPU        | py2, py3        |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-mxnet:`<tag>`             | 1.0.0   | inference               | CPU, GPU        | py2, py3        |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-mxnet:`<tag>`             | 0.12.1  | training                | CPU, GPU        | py2, py3        |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-mxnet:`<tag>`             | 0.12.1  | inference               | CPU, GPU        | py2, py3        |

## MXNet Coach (DLC)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='coach-mxnet',region='eu-west-3',version='0.11',py_version='py3',image_scope='training',instance_type='ml.c5.4xlarge')
```

| Registry path                                                                       | Version | Job types (image scope) | Processor types | Python versions |
| ----------------------------------------------------------------------------------- | ------- | ----------------------- | --------------- | --------------- |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-rl-mxnet:coach0.11.0-`<tag>` | 0.11.0  | training                | CPU, GPU        | py3             |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-rl-mxnet:coach0.11-`<tag>`   | 0.11    | training                | CPU, GPU        | py3             |

## Model Monitor (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='model-monitor',region='eu-west-3')
```

| Registry path                                                                         | Version | Job types (image scope) |
| ------------------------------------------------------------------------------------- | ------- | ----------------------- |
| 680080141114.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-model-monitor-analyzer:`<tag>` |         | monitoring              |

## NTM (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='ntm',region='eu-west-3')
```

| Registry path                                            | Version | Job types (image scope) |
| -------------------------------------------------------- | ------- | ----------------------- |
| 749696950732.dkr.ecr.eu-west-3.amazonaws.com/ntm:`<tag>` | 1       | inference, training     |

## Neo Image Classification (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='image-classification-neo',region='eu-west-3')
```

| Registry path                                                                 | Version | Job types (image scope) |
| ----------------------------------------------------------------------------- | ------- | ----------------------- |
| 254080097072.dkr.ecr.eu-west-3.amazonaws.com/image-classification-neo:`<tag>` | latest  | inference               |

## Neo MXNet (DLC)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='neo-mxnet',region='eu-west-3',version='1.8',py_version='py3',image_scope='inference', instance_type='ml.c5.4xlarge')
```

| Registry path                                                                  | Version | Job types (image scope) | Processor types | Python versions |
| ------------------------------------------------------------------------------ | ------- | ----------------------- | --------------- | --------------- |
| 254080097072.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-inference-mxnet:`<tag>` | 1.8     | inference               | CPU, GPU        | py3             |

## Neo PyTorch (DLC)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='neo-pytorch',region='eu-west-3',version='1.6',image_scope='inference',instance_type='ml.c5.4xlarge')
```

| Registry path                                                                    | Version | Job types (image scope) | Processor types | Python versions |
| -------------------------------------------------------------------------------- | ------- | ----------------------- | --------------- | --------------- |
| 254080097072.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-inference-pytorch:`<tag>` | 2.0     | inference               | CPU, GPU        | py3             |
| 254080097072.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-inference-pytorch:`<tag>` | 1.13    | inference               | CPU, GPU        | py3             |
| 254080097072.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-inference-pytorch:`<tag>` | 1.12    | inference               | CPU, GPU        | py3             |
| 254080097072.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-inference-pytorch:`<tag>` | 1.8     | inference               | CPU, GPU        | py3             |
| 254080097072.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-inference-pytorch:`<tag>` | 1.7     | inference               | CPU, GPU        | py3             |
| 254080097072.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-inference-pytorch:`<tag>` | 1.6     | inference               | CPU, GPU        | py3             |
| 254080097072.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-inference-pytorch:`<tag>` | 1.5     | inference               | CPU, GPU        | py3             |
| 254080097072.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-inference-pytorch:`<tag>` | 1.4     | inference               | CPU, GPU        | py3             |

## Neo Tensorflow (DLC)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='neo-tensorflow',region='eu-west-3',version='1.15.3',py_version='py3',instance_type='ml.c5.4xlarge')
```

| Registry path                                                                       | Version | Job types (image scope) | Processor types | Python versions |
| ----------------------------------------------------------------------------------- | ------- | ----------------------- | --------------- | --------------- |
| 254080097072.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-inference-tensorflow:`<tag>` | 2.9.2   | inference               | CPU, GPU        | py3             |
| 254080097072.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-inference-tensorflow:`<tag>` | 1.15.3  | inference               | CPU, GPU        | py3             |

## Neo XGBoost (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='xgboost-neo',region='eu-west-3')
```

| Registry path                                                    | Version | Job types (image scope) |
| ---------------------------------------------------------------- | ------- | ----------------------- |
| 254080097072.dkr.ecr.eu-west-3.amazonaws.com/xgboost-neo:`<tag>` | latest  | inference               |

## Object Detection (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='object-detection',region='eu-west-3')
```

| Registry path                                                         | Version | Job types (image scope) |
| --------------------------------------------------------------------- | ------- | ----------------------- |
| 749696950732.dkr.ecr.eu-west-3.amazonaws.com/object-detection:`<tag>` | 1       | inference, training     |

## Object2Vec (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='object2vec',region='eu-west-3')
```

| Registry path                                                   | Version | Job types (image scope) |
| --------------------------------------------------------------- | ------- | ----------------------- |
| 749696950732.dkr.ecr.eu-west-3.amazonaws.com/object2vec:`<tag>` | 1       | inference, training     |

## PCA (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='pca',region='eu-west-3')
```

| Registry path                                            | Version | Job types (image scope) |
| -------------------------------------------------------- | ------- | ----------------------- |
| 749696950732.dkr.ecr.eu-west-3.amazonaws.com/pca:`<tag>` | 1       | inference, training     |

## PyTorch (DLC)

For information about the supported and unsupported PyTorch versions, see the [Framework Support Policy Table](../../../deep-learning-containers/latest/devguide/dlc-framework-support-policy.md "../../../deep-learning-containers/latest/devguide/dlc-framework-support-policy.md")
in the _AWS Deep Learning Containers Developer Guide_.

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='pytorch',region='eu-west-3',version='1.8.0',py_version='py3',image_scope='inference', instance_type='ml.c5.4xlarge')
```

| Registry path                                                                   | Version | Job types (image scope) | Processor types | Python versions |
| ------------------------------------------------------------------------------- | ------- | ----------------------- | --------------- | --------------- |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-training:`<tag>`           | 2.7.1   | training                | CPU, GPU        | py312           |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-inference:`<tag>`          | 2.6.0   | inference               | CPU, GPU        | py312           |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-training:`<tag>`           | 2.6.0   | training                | CPU, GPU        | py312           |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-inference:`<tag>`          | 2.5.1   | inference               | CPU, GPU        | py311           |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-training:`<tag>`           | 2.5.1   | training                | CPU, GPU        | py311           |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-inference:`<tag>`          | 2.4.0   | inference               | CPU, GPU        | py311           |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-inference-graviton:`<tag>` | 2.4.0   | inference_graviton      | CPU             | py311           |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-training:`<tag>`           | 2.4.0   | training                | CPU, GPU        | py311           |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-inference:`<tag>`          | 2.3.0   | inference               | CPU, GPU        | py311           |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-inference-graviton:`<tag>` | 2.3.0   | inference_graviton      | CPU             | py311           |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-training:`<tag>`           | 2.3.0   | training                | CPU, GPU        | py311           |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-inference-graviton:`<tag>` | 2.2.1   | inference_graviton      | CPU             | py310           |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-inference:`<tag>`          | 2.2.0   | inference               | CPU, GPU        | py310           |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-training:`<tag>`           | 2.2.0   | training                | CPU, GPU        | py310           |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-inference:`<tag>`          | 2.1.0   | inference               | CPU, GPU        | py310           |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-inference-graviton:`<tag>` | 2.1.0   | inference_graviton      | CPU             | py310           |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-training:`<tag>`           | 2.1.0   | training                | CPU, GPU        | py310           |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-inference:`<tag>`          | 2.0.1   | inference               | CPU, GPU        | py310           |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-inference-graviton:`<tag>` | 2.0.1   | inference_graviton      | CPU             | py310           |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-training:`<tag>`           | 2.0.1   | training                | CPU, GPU        | py310           |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-inference:`<tag>`          | 2.0.0   | inference               | CPU, GPU        | py310           |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-inference-graviton:`<tag>` | 2.0.0   | inference_graviton      | CPU             | py310           |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-training:`<tag>`           | 2.0.0   | training                | CPU, GPU        | py310           |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-inference:`<tag>`          | 1.13.1  | inference               | CPU, GPU        | py39            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-training:`<tag>`           | 1.13.1  | training                | CPU, GPU        | py39            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-inference:`<tag>`          | 1.12.1  | inference               | CPU, GPU        | py38            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-inference-graviton:`<tag>` | 1.12.1  | inference_graviton      | CPU             | py38            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-training:`<tag>`           | 1.12.1  | training                | CPU, GPU        | py38            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-inference:`<tag>`          | 1.12.0  | inference               | CPU, GPU        | py38            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-training:`<tag>`           | 1.12.0  | training                | CPU, GPU        | py38            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-inference:`<tag>`          | 1.11.0  | inference               | CPU, GPU        | py38            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-training:`<tag>`           | 1.11.0  | training                | CPU, GPU        | py38            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-inference:`<tag>`          | 1.10.2  | inference               | CPU, GPU        | py38            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-training:`<tag>`           | 1.10.2  | training                | CPU, GPU        | py38            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-inference:`<tag>`          | 1.10.0  | inference               | CPU, GPU        | py38            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-training:`<tag>`           | 1.10.0  | training                | CPU, GPU        | py38            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-inference:`<tag>`          | 1.9.1   | inference               | CPU, GPU        | py38            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-training:`<tag>`           | 1.9.1   | training                | CPU, GPU        | py38            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-inference:`<tag>`          | 1.9.0   | inference               | CPU, GPU        | py38            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-training:`<tag>`           | 1.9.0   | training                | CPU, GPU        | py38            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-inference:`<tag>`          | 1.8.1   | inference               | CPU, GPU        | py3, py36       |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-training:`<tag>`           | 1.8.1   | training                | CPU, GPU        | py3, py36       |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-inference:`<tag>`          | 1.8.0   | inference               | CPU, GPU        | py3, py36       |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-training:`<tag>`           | 1.8.0   | training                | CPU, GPU        | py3, py36       |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-inference:`<tag>`          | 1.7.1   | inference               | CPU, GPU        | py3, py36       |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-training:`<tag>`           | 1.7.1   | training                | CPU, GPU        | py3, py36       |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-inference:`<tag>`          | 1.6.0   | inference               | CPU, GPU        | py3, py36       |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-training:`<tag>`           | 1.6.0   | training                | CPU, GPU        | py3, py36       |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-inference:`<tag>`          | 1.5.0   | inference               | CPU, GPU        | py3, py36       |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-training:`<tag>`           | 1.5.0   | training                | CPU, GPU        | py3, py36       |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-inference:`<tag>`          | 1.4.0   | inference               | CPU, GPU        | py3, py36       |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-training:`<tag>`           | 1.4.0   | training                | CPU, GPU        | py2, py3, py36  |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-inference:`<tag>`          | 1.3.1   | inference               | CPU, GPU        | py2, py3        |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-training:`<tag>`           | 1.3.1   | training                | CPU, GPU        | py2, py3        |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-inference:`<tag>`          | 1.2.0   | inference               | CPU, GPU        | py2, py3        |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-training:`<tag>`           | 1.2.0   | training                | CPU, GPU        | py2, py3        |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-pytorch:`<tag>`          | 1.1.0   | inference               | CPU, GPU        | py2, py3        |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-pytorch:`<tag>`          | 1.1.0   | training                | CPU, GPU        | py2, py3        |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-pytorch:`<tag>`          | 1.0.0   | inference               | CPU, GPU        | py2, py3        |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-pytorch:`<tag>`          | 1.0.0   | training                | CPU, GPU        | py2, py3        |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-pytorch:`<tag>`          | 0.4.0   | inference               | CPU, GPU        | py2, py3        |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-pytorch:`<tag>`          | 0.4.0   | training                | CPU, GPU        | py2, py3        |

## PyTorch Neuron (DLC)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='pytorch-neuron',region='us-west-2', image_scope='inference')
```

| Registry path                                                                | Version | Job types (image scope) | Processor types | Python versions |
| ---------------------------------------------------------------------------- | ------- | ----------------------- | --------------- | --------------- |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-training-neuron:`<tag>` | 1.11.0  | training                | TRN             | py38            |

## PyTorch Training Compiler (DLC)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='pytorch-training-compiler',region='us-west-2', version='py38')
```

| Registry path                                                                | Version | Job types (image scope) | Processor types | Python versions |
| ---------------------------------------------------------------------------- | ------- | ----------------------- | --------------- | --------------- |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-trcomp-training:`<tag>` | 1.13.1  | training                | GPU             | py39            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/pytorch-trcomp-training:`<tag>` | 1.12.0  | training                | GPU             | py38            |

## Random Cut Forest (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='randomcutforest',region='eu-west-3')
```

| Registry path                                                        | Version | Job types (image scope) |
| -------------------------------------------------------------------- | ------- | ----------------------- |
| 749696950732.dkr.ecr.eu-west-3.amazonaws.com/randomcutforest:`<tag>` | 1       | inference, training     |

## Scikit-learn (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='sklearn',region='eu-west-3',version='0.23-1',image_scope='inference')
```

| Registry path                                                               | Version | Package version | Job types (image scope) |
| --------------------------------------------------------------------------- | ------- | --------------- | ----------------------- |
| 659782779980.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-scikit-learn:`<tag>` | 1.2-1   | 1.2.1           | inference               |
| 659782779980.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-scikit-learn:`<tag>` | 1.2-1   | 1.2.1           | training                |
| 659782779980.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-scikit-learn:`<tag>` | 1.0-1   | 1.0.2           | inference               |
| 659782779980.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-scikit-learn:`<tag>` | 1.0-1   | 1.0.2           | training                |
| 659782779980.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-scikit-learn:`<tag>` | 1.0-1   | 1.0.2           | inference_graviton      |
| 659782779980.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-scikit-learn:`<tag>` | 0.23-1  | 0.23.2          | inference               |
| 659782779980.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-scikit-learn:`<tag>` | 0.23-1  | 0.23.2          | training                |
| 659782779980.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-scikit-learn:`<tag>` | 0.20.0  | 0.20.0          | inference               |
| 659782779980.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-scikit-learn:`<tag>` | 0.20.0  | 0.20.0          | training                |

## Semantic Segmentation (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='semantic-segmentation',region='eu-west-3')
```

| Registry path                                                              | Version | Job types (image scope) |
| -------------------------------------------------------------------------- | ------- | ----------------------- |
| 749696950732.dkr.ecr.eu-west-3.amazonaws.com/semantic-segmentation:`<tag>` | 1       | inference, training     |

## Seq2Seq (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='seq2seq',region='eu-west-3')
```

| Registry path                                                | Version | Job types (image scope) |
| ------------------------------------------------------------ | ------- | ----------------------- |
| 749696950732.dkr.ecr.eu-west-3.amazonaws.com/seq2seq:`<tag>` | 1       | inference, training     |

## Spark (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='spark',region='eu-west-3',version='3.0',image_scope='processing')
```

| Registry path                                                                   | Version | Job types (image scope) |
| ------------------------------------------------------------------------------- | ------- | ----------------------- |
| 136845547031.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-spark-processing:`<tag>` | 3.3     | processing              |
| 136845547031.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-spark-processing:`<tag>` | 3.2     | processing              |
| 136845547031.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-spark-processing:`<tag>` | 3.1     | processing              |
| 136845547031.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-spark-processing:`<tag>` | 3.0     | processing              |
| 136845547031.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-spark-processing:`<tag>` | 2.4     | processing              |

## SparkML Serving (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='sparkml-serving',region='eu-west-3',version='2.4')
```

| Registry path                                                                  | Version | Job types (image scope) |
| ------------------------------------------------------------------------------ | ------- | ----------------------- |
| 659782779980.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-sparkml-serving:`<tag>` | 3.3     | inference               |
| 659782779980.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-sparkml-serving:`<tag>` | 2.4     | inference               |
| 659782779980.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-sparkml-serving:`<tag>` | 2.2     | inference               |

## Tensorflow (DLC)

For information about the supported and unsupported TensorFlow versions, see the [Framework Support Policy Table](../../../deep-learning-containers/latest/devguide/dlc-framework-support-policy.md "../../../deep-learning-containers/latest/devguide/dlc-framework-support-policy.md")
in the _AWS Deep Learning Containers Developer Guide_.

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='tensorflow',region='eu-west-3',version='1.12.0',image_scope='inference',instance_type='ml.c5.4xlarge')
```

| Registry path                                                                         | Version | Job types (image scope) | Processor types | Python versions |
| ------------------------------------------------------------------------------------- | ------- | ----------------------- | --------------- | --------------- |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.19.0  | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 2.19.0  | training                | CPU, GPU        | py312           |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.18.0  | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 2.18.0  | training                | CPU, GPU        | py310           |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 2.16.2  | training                | CPU, GPU        | py310           |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.16.1  | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference-graviton:`<tag>`    | 2.16.1  | inference_graviton      | CPU             | py310           |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.14.1  | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference-graviton:`<tag>`    | 2.14.1  | inference_graviton      | CPU             | py310           |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 2.14.1  | training                | CPU, GPU        | py310           |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.13.0  | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference-graviton:`<tag>`    | 2.13.0  | inference_graviton      | CPU             | py310           |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 2.13.0  | training                | CPU, GPU        | py310           |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.12.1  | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference-graviton:`<tag>`    | 2.12.1  | inference_graviton      | CPU             | py310           |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 2.12.0  | training                | CPU, GPU        | py310           |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.11.1  | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.11.0  | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 2.11.0  | training                | CPU, GPU        | py39            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.10.1  | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 2.10.1  | training                | CPU, GPU        | py39            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.10.0  | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.9.3   | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.9.2   | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 2.9.2   | training                | CPU, GPU        | py39            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference-graviton:`<tag>`    | 2.9.1   | inference_graviton      | CPU             | py38            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.8.4   | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.8.0   | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 2.8.0   | training                | CPU, GPU        | py39            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 2.7.1   | training                | CPU, GPU        | py38            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.7.0   | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.6.3   | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 2.6.3   | training                | CPU, GPU        | py38            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 2.6.2   | training                | CPU, GPU        | py38            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.6.0   | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 2.6.0   | training                | CPU, GPU        | py38            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.5.1   | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 2.5.1   | training                | CPU, GPU        | py37            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 2.5.0   | training                | CPU, GPU        | py37            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.4.3   | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 2.4.3   | training                | CPU, GPU        | py37            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.4.1   | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 2.4.1   | training                | CPU, GPU        | py37            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.3.2   | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 2.3.2   | training                | CPU, GPU        | py37            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.3.1   | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 2.3.1   | training                | CPU, GPU        | py37            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference-eia:`<tag>`         | 2.3.0   | eia                     | CPU             | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.3.0   | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 2.3.0   | training                | CPU, GPU        | py37            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.2.2   | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 2.2.2   | training                | CPU, GPU        | py37            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.2.1   | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 2.2.1   | training                | CPU, GPU        | py37            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.2.0   | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 2.2.0   | training                | CPU, GPU        | py37            |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.1.3   | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 2.1.3   | training                | CPU, GPU        | py3, py36       |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.1.2   | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 2.1.2   | training                | CPU, GPU        | py3, py36       |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.1.1   | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 2.1.1   | training                | CPU, GPU        | py2, py3        |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.1.0   | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 2.1.0   | training                | CPU, GPU        | py2, py3        |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.0.4   | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 2.0.4   | training                | CPU, GPU        | py3, py36       |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.0.3   | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 2.0.3   | training                | CPU, GPU        | py3, py36       |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.0.2   | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 2.0.2   | training                | CPU, GPU        | py2, py3        |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.0.1   | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 2.0.1   | training                | CPU, GPU        | py2, py3        |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference-eia:`<tag>`         | 2.0.0   | eia                     | CPU             | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 2.0.0   | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 2.0.0   | training                | CPU, GPU        | py2, py3        |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 1.15.5  | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 1.15.5  | training                | CPU, GPU        | py3, py36, py37 |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 1.15.4  | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 1.15.4  | training                | CPU, GPU        | py3, py36, py37 |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 1.15.3  | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 1.15.3  | training                | CPU, GPU        | py2, py3, py37  |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 1.15.2  | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 1.15.2  | training                | CPU, GPU        | py2, py3, py37  |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference-eia:`<tag>`         | 1.15.0  | eia                     | CPU             | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 1.15.0  | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 1.15.0  | training                | CPU, GPU        | py2, py3        |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference-eia:`<tag>`         | 1.14.0  | eia                     | CPU             | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 1.14.0  | inference               | CPU, GPU        | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 1.14.0  | training                | CPU, GPU        | py2, py3        |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-tensorflow-scriptmode:`<tag>`  | 1.13.1  | training                | CPU, GPU        | py2             |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-training:`<tag>`              | 1.13.1  | training                | CPU, GPU        | py3             |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-tensorflow-serving-eia:`<tag>` | 1.13.0  | eia                     | CPU             | -               |
| 763104351884.dkr.ecr.eu-west-3.amazonaws.com/tensorflow-inference:`<tag>`             | 1.13.0  | inference               | CPU, GPU        | -               |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-tensorflow-serving-eia:`<tag>` | 1.12.0  | eia                     | CPU             | -               |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-tensorflow-serving:`<tag>`     | 1.12.0  | inference               | CPU, GPU        | -               |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-tensorflow-scriptmode:`<tag>`  | 1.12.0  | training                | CPU, GPU        | py2, py3        |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-tensorflow-serving-eia:`<tag>` | 1.11.0  | eia                     | CPU             | -               |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-tensorflow-serving:`<tag>`     | 1.11.0  | inference               | CPU, GPU        | -               |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-tensorflow-scriptmode:`<tag>`  | 1.11.0  | training                | CPU, GPU        | py2, py3        |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-tensorflow-eia:`<tag>`         | 1.10.0  | eia                     | CPU             | py2             |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-tensorflow:`<tag>`             | 1.10.0  | inference               | CPU, GPU        | py2             |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-tensorflow:`<tag>`             | 1.10.0  | training                | CPU, GPU        | py2             |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-tensorflow:`<tag>`             | 1.9.0   | inference               | CPU, GPU        | py2             |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-tensorflow:`<tag>`             | 1.9.0   | training                | CPU, GPU        | py2             |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-tensorflow:`<tag>`             | 1.8.0   | inference               | CPU, GPU        | py2             |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-tensorflow:`<tag>`             | 1.8.0   | training                | CPU, GPU        | py2             |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-tensorflow:`<tag>`             | 1.7.0   | inference               | CPU, GPU        | py2             |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-tensorflow:`<tag>`             | 1.7.0   | training                | CPU, GPU        | py2             |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-tensorflow:`<tag>`             | 1.6.0   | inference               | CPU, GPU        | py2             |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-tensorflow:`<tag>`             | 1.6.0   | training                | CPU, GPU        | py2             |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-tensorflow:`<tag>`             | 1.5.0   | inference               | CPU, GPU        | py2             |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-tensorflow:`<tag>`             | 1.5.0   | training                | CPU, GPU        | py2             |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-tensorflow:`<tag>`             | 1.4.1   | inference               | CPU, GPU        | py2             |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-tensorflow:`<tag>`             | 1.4.1   | training                | CPU, GPU        | py2             |

## Tensorflow Coach (DLC)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='coach-tensorflow',region='eu-west-3',version='1.0.0',image_scope='training',instance_type='ml.c5.4xlarge')
```

| Registry path                                                                            | Version | Job types (image scope) | Processor types | Python versions |
| ---------------------------------------------------------------------------------------- | ------- | ----------------------- | --------------- | --------------- |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-rl-tensorflow:coach0.11.1-`<tag>` | 0.11.1  | training                | CPU, GPU        | py3             |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-rl-tensorflow:coach0.11.0-`<tag>` | 0.11.0  | training                | CPU, GPU        | py3             |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-rl-tensorflow:coach0.11-`<tag>`   | 0.11    | training                | CPU, GPU        | py3             |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-rl-tensorflow:coach0.10.1-`<tag>` | 0.10.1  | training                | CPU, GPU        | py3             |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-rl-tensorflow:coach0.10-`<tag>`   | 0.10    | training                | CPU, GPU        | py3             |

## Tensorflow Inferentia (DLC)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='inferentia-tensorflow',region='eu-west-3',version='1.15.0',instance_type='ml.inf1.6xlarge')
```

| Registry path                                                                 | Version | Job types (image scope) | Processor types | Python versions |
| ----------------------------------------------------------------------------- | ------- | ----------------------- | --------------- | --------------- |
| 254080097072.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-neo-tensorflow:`<tag>` | 2.5.2   | inference               | inf             | py3             |
| 254080097072.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-neo-tensorflow:`<tag>` | 1.15.0  | inference               | inf             | py3             |

## Tensorflow Ray (DLC)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='ray-tensorflow',region='eu-west-3',version='0.8.5',instance_type='ml.c5.4xlarge')
```

| Registry path                                                                         | Version | Job types (image scope) | Processor types | Python versions |
| ------------------------------------------------------------------------------------- | ------- | ----------------------- | --------------- | --------------- |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-rl-tensorflow:ray0.6.5-`<tag>` | 0.6.5   | training                | CPU, GPU        | py3             |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-rl-tensorflow:ray0.6-`<tag>`   | 0.6     | training                | CPU, GPU        | py3             |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-rl-tensorflow:ray0.5.3-`<tag>` | 0.5.3   | training                | CPU, GPU        | py3             |
| 520713654638.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-rl-tensorflow:ray0.5-`<tag>`   | 0.5     | training                | CPU, GPU        | py3             |

## XGBoost (algorithm)

The following SageMaker AI Python SDK example shows how to retrieve a specific registry path.

```
from sagemaker import image_uris
image_uris.retrieve(framework='xgboost',region='eu-west-3',version='1.5-1')
```

| Registry path                                                          | Version | Package version | Job types (image scope) |
| ---------------------------------------------------------------------- | ------- | --------------- | ----------------------- |
| 659782779980.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.7-1   | 1.7.4           | inference               |
| 659782779980.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.7-1   | 1.7.4           | training                |
| 659782779980.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.5-1   | 1.5.2           | inference               |
| 659782779980.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.5-1   | 1.5.2           | training                |
| 659782779980.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.5-1   | 1.5.2           | inference_graviton      |
| 659782779980.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.3-1   | 1.3.3           | inference               |
| 659782779980.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.3-1   | 1.3.3           | training                |
| 659782779980.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.3-1   | 1.3.3           | inference_graviton      |
| 659782779980.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.2-2   | 1.2.0           | inference               |
| 659782779980.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.2-2   | 1.2.0           | training                |
| 659782779980.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.2-1   | 1.2.0           | inference               |
| 659782779980.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.2-1   | 1.2.0           | training                |
| 659782779980.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.0-1   | 1.0.0           | inference               |
| 659782779980.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-xgboost:`<tag>` | 1.0-1   | 1.0.0           | training                |
| 749696950732.dkr.ecr.eu-west-3.amazonaws.com/xgboost:`<tag>`           | 1       | 0.72            | inference               |
| 749696950732.dkr.ecr.eu-west-3.amazonaws.com/xgboost:`<tag>`           | 1       | 0.72            | training                |
| 659782779980.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-xgboost:`<tag>` | 0.90-2  | 0.90            | inference               |
| 659782779980.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-xgboost:`<tag>` | 0.90-2  | 0.90            | training                |
| 659782779980.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-xgboost:`<tag>` | 0.90-1  | 0.90            | inference               |
| 659782779980.dkr.ecr.eu-west-3.amazonaws.com/sagemaker-xgboost:`<tag>` | 0.90-1  | 0.90            | training                |
