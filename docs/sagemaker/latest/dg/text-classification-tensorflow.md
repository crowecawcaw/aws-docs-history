# Text Classification - TensorFlow

The Amazon SageMaker AI Text Classification - TensorFlow algorithm is a supervised learning algorithm that
supports transfer learning with many pretrained models from the [TensorFlow Hub](https://tfhub.dev/ "https://tfhub.dev/"). Use transfer learning to fine-tune one of
the available pretrained models on your own dataset, even if a large amount of text data is
not available. The text classification algorithm takes a text string as input and outputs a
probability for each of the class labels. Training datasets must be in CSV format. This page
includes information about Amazon EC2 instance recommendations and sample notebooks for Text
Classification - TensorFlow.

###### Topics

- [How to use the SageMaker AI Text Classification - TensorFlow algorithm](text-classification-tensorflow-how-to-use.md "text-classification-tensorflow-how-to-use.md")
- [Input and output interface
  for the Text Classification - TensorFlow algorithm](text-classification-tensorflow-inputoutput.md "text-classification-tensorflow-inputoutput.md")
- [Amazon EC2 instance recommendation
  for the Text Classification - TensorFlow algorithm](#text-classification-tensorflow-instances "#text-classification-tensorflow-instances")
- [Text Classification - TensorFlow sample
  notebooks](#text-classification-tensorflow-sample-notebooks "#text-classification-tensorflow-sample-notebooks")
- [How Text Classification - TensorFlow Works](text-classification-tensorflow-HowItWorks.md "text-classification-tensorflow-HowItWorks.md")
- [TensorFlow Hub Models](text-classification-tensorflow-Models.md "text-classification-tensorflow-Models.md")
- [Text Classification - TensorFlow
  Hyperparameters](text-classification-tensorflow-Hyperparameter.md "text-classification-tensorflow-Hyperparameter.md")
- [Tune a Text Classification -
  TensorFlow model](text-classification-tensorflow-tuning.md "text-classification-tensorflow-tuning.md")

## Amazon EC2 instance recommendation

for the Text Classification - TensorFlow algorithm

The Text Classification - TensorFlow algorithm supports all CPU and GPU instances for
training, including:

- `ml.p2.xlarge`
- `ml.p2.16xlarge`
- `ml.p3.2xlarge`
- `ml.p3.16xlarge`
- `ml.g4dn.xlarge`
- `ml.g4dn.16.xlarge`
- `ml.g5.xlarge`
- `ml.g5.48xlarge`

We recommend GPU instances with more memory for training with large batch sizes. Both
CPU (such as M5) and GPU (P2, P3, G4dn, or G5) instances can be used for inference. For
a comprehensive list of SageMaker training and inference instances across AWS Regions, see [Amazon SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/").

## Text Classification - TensorFlow sample

notebooks

For more information about how to use the SageMaker AI Text Classification - TensorFlow algorithm
for transfer learning on a custom dataset, see the [Introduction to JumpStart - Text Classification](https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/jumpstart_text_classification/Amazon_JumpStart_Text_Classification.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/jumpstart_text_classification/Amazon_JumpStart_Text_Classification.ipynb") notebook.

For instructions how to create and access Jupyter notebook instances that you can use to
run the example in SageMaker AI, see [Amazon SageMaker notebook instances](nbi.md "nbi.md"). After you have
created a notebook instance and opened it, select the **SageMaker AI
Examples** tab to see a list of all the SageMaker AI samples. To open a notebook,
choose its **Use** tab and choose **Create copy**.
