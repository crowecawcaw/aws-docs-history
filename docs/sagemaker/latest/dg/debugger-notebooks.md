# Debugger example notebooks

[SageMaker Debugger example notebooks](https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-debugger/ "https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-debugger/") are provided in the [aws/amazon-sagemaker-examples](https://github.com/aws/amazon-sagemaker-examples "https://github.com/aws/amazon-sagemaker-examples") repository. The Debugger example
notebooks walk you through basic to advanced use cases of debugging and
profiling training jobs.

We recommend that you run the example notebooks on SageMaker Studio or a SageMaker Notebook
instance because most of the examples are designed for training jobs in the SageMaker AI ecosystem,
including Amazon EC2, Amazon S3, and Amazon SageMaker Python SDK.

To clone the example repository to SageMaker Studio, follow the instructions at [Amazon SageMaker Studio Tour](gs-studio-end-to-end.md "gs-studio-end-to-end.md").

###### Important

To use the new Debugger features, you need to upgrade the SageMaker Python SDK and the
`SMDebug` client library. In your iPython kernel, Jupyter Notebook, or JupyterLab
environment, run the following code to install the latest versions of the libraries and
restart the kernel.

```
import sys
import IPython
!{sys.executable} -m pip install -U sagemaker smdebug
IPython.Application.instance().kernel.do_shutdown(True)
```

## Debugger example notebooks for profiling

training jobs

The following list shows Debugger example notebooks introducing Debugger's adaptability to
monitor and profile training jobs for various machine learning models, datasets, and
frameworks.

| Notebook Title                                                                                                                                                                                                                                                                                                                                                                                                                | Framework  | Model                            | Dataset      | Description                                                                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | -------------------------------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Amazon SageMaker Debugger Profiling Data Analysis](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-debugger/debugger_interactive_analysis_profiling/interactive_analysis_profiling_data.html "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-debugger/debugger_interactive_analysis_profiling/interactive_analysis_profiling_data.html")                                                        | TensorFlow | Keras ResNet50                   | Cifar-10     | This notebook provides an introduction to interactive analysis of profiled data<br>captured by SageMaker Debugger. Explore the full functionality of the `SMDebug`<br>interactive analysis tools.                           |
| [Profile machine learning training with Amazon SageMaker Debugger](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-debugger/tensorflow_nlp_sentiment_analysis/sentiment-analysis-tf-distributed-training-bringyourownscript.html "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-debugger/tensorflow_nlp_sentiment_analysis/sentiment-analysis-tf-distributed-training-bringyourownscript.html") | TensorFlow | 1-D Convolutional Neural Network | IMDB dataset | Profile a TensorFlow 1-D CNN for sentiment analysis of IMDB data that<br>consists of movie reviews labeled as having positive or negative sentiment. Explore<br>the Studio Debugger insights and Debugger profiling report. |
| [Profiling TensorFlow ResNet model training with various distributed training settings](https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-debugger/tensorflow_profiling "https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-debugger/tensorflow_profiling")                                                                                                                          | TensorFlow | ResNet50                         | Cifar-10     | Run TensorFlow training jobs with various distributed training settings,<br>monitor system resource utilization, and profile model performance using<br>Debugger.                                                           |
| [Profiling PyTorch ResNet model training with various distributed training settings](https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-debugger/pytorch_profiling "https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-debugger/pytorch_profiling")                                                                                                                                   | PyTorch    | ResNet50                         | Cifar-10     | Run PyTorch training jobs with various distributed training settings,<br>monitor system resource utilization, and profile model performance using<br>Debugger.                                                              |

## Debugger example notebooks for analyzing

model parameters

The following list shows Debugger example notebooks introducing Debugger's adaptability to
debug training jobs for various machine learning models, datasets, and frameworks.

| Notebook Title                                                                                                                                                                                                                                                                                                                                                                | Framework  | Model                              | Dataset                                                                                                                  | Description                                                                                                                                                                              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Amazon SageMaker Debugger<br>• Use built-in rule](https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-debugger/tensorflow_builtin_rule "https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-debugger/tensorflow_builtin_rule")                                                                                                         | TensorFlow | Convolutional Neural Network       | MNIST                                                                                                                    | Use the Amazon SageMaker Debugger built-in rules for debugging a TensorFlow<br>model.                                                                                                    |
| [Amazon SageMaker Debugger<br>• Tensorflow 2.1](https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-debugger/tensorflow2 "https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-debugger/tensorflow2")                                                                                                                                    | TensorFlow | ResNet50                           | Cifar-10                                                                                                                 | Use the Amazon SageMaker Debugger hook configuration and built-in rules for<br>debugging a model with the Tensorflow 2.1 framework.                                                      |
| [Visualizing Debugging Tensors of MXNet<br>training](https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-debugger/mnist_tensor_plot "https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-debugger/mnist_tensor_plot")                                                                                                                   | MXNet      | Gluon Convolutional Neural Network | Fashion MNIST                                                                                                            | Run a training job and configure SageMaker Debugger to store<br>all tensors from this job, then visualize those tensors ina notebook.                                                    |
| [Enable Spot Training with Amazon SageMaker Debugger](https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-debugger/mxnet_spot_training "https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-debugger/mxnet_spot_training")                                                                                                              | MXNet      | Gluon Convolutional Neural Network | Fashion MNIST                                                                                                            | Learn how Debugger collects tensor data from a training<br>job on a spot instance, and how to use the Debugger built-in rules with managed spot<br>training.                             |
| [Explain an XGBoost model that predicts an individual’s income with Amazon SageMaker Debugger](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-debugger/xgboost_census_explanations/xgboost-census-debugger-rules.html "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-debugger/xgboost_census_explanations/xgboost-census-debugger-rules.html") | XGBoost    | XGBoost Regression                 | [Adult Census<br>dataset](https://archive.ics.uci.edu/ml/datasets/adult "https://archive.ics.uci.edu/ml/datasets/adult") | Learn how to use the Debugger hook and built-in rules for<br>collecting and visualizing tensor data from an XGBoost regression model, such as loss<br>values, features, and SHAP values. |

To find advanced visualizations of model parameters and use cases, see the next topic
at [Debugger advanced demos and visualization](debugger-visualization.md "debugger-visualization.md").
