# Object Detection - TensorFlow

The Amazon SageMaker AI Object Detection - TensorFlow algorithm is a supervised learning algorithm that
supports transfer learning with many pretrained models from the [TensorFlow Model Garden](https://github.com/tensorflow/models "https://github.com/tensorflow/models"). Use transfer
learning to fine-tune one of the available pretrained models on your own dataset, even if a
large amount of image data is not available. The object detection algorithm takes an image
as input and outputs a list of bounding boxes. Training datasets must consist of images in
.`jpg`, `.jpeg`, or `.png` format. This page includes
information about Amazon EC2 instance recommendations and sample notebooks for Object Detection -
TensorFlow.

###### Topics

- [How to use the SageMaker AI Object Detection - TensorFlow algorithm](object-detection-tensorflow-how-to-use.md "object-detection-tensorflow-how-to-use.md")
- [Input and output interface for
  the Object Detection - TensorFlow algorithm](object-detection-tensorflow-inputoutput.md "object-detection-tensorflow-inputoutput.md")
- [Amazon EC2 instance recommendation
  for the Object Detection - TensorFlow algorithm](#object-detection-tensorflow-instances "#object-detection-tensorflow-instances")
- [Object Detection - TensorFlow sample
  notebooks](#object-detection-tensorflow-sample-notebooks "#object-detection-tensorflow-sample-notebooks")
- [How Object Detection - TensorFlow Works](object-detection-tensorflow-HowItWorks.md "object-detection-tensorflow-HowItWorks.md")
- [TensorFlow Models](object-detection-tensorflow-Models.md "object-detection-tensorflow-Models.md")
- [Object Detection - TensorFlow
  Hyperparameters](object-detection-tensorflow-Hyperparameter.md "object-detection-tensorflow-Hyperparameter.md")
- [Tune an Object Detection - TensorFlow model](object-detection-tensorflow-tuning.md "object-detection-tensorflow-tuning.md")

## Amazon EC2 instance recommendation

for the Object Detection - TensorFlow algorithm

The Object Detection - TensorFlow algorithm supports all GPU instances for training,
including:

- `ml.p2.xlarge`
- `ml.p2.16xlarge`
- `ml.p3.2xlarge`
- `ml.p3.16xlarge`

We recommend GPU instances with more memory for training with large batch sizes. Both
CPU (such as M5) and GPU (P2 or P3) instances can be used for inference. For a
comprehensive list of SageMaker training and inference instances across AWS Regions, see
[Amazon SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/").

## Object Detection - TensorFlow sample

notebooks

For more information about how to use the SageMaker AI Object Detection - TensorFlow algorithm
for transfer learning on a custom dataset, see the [Introduction to SageMaker TensorFlow - Object Detection](https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/object_detection_tensorflow/Amazon_Tensorflow_Object_Detection.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/object_detection_tensorflow/Amazon_Tensorflow_Object_Detection.ipynb") notebook.

For instructions how to create and access Jupyter notebook instances that you can use to
run the example in SageMaker AI, see [Amazon SageMaker notebook instances](nbi.md "nbi.md"). After you have
created a notebook instance and opened it, select the **SageMaker AI
Examples** tab to see a list of all the SageMaker AI samples. To open a notebook,
choose its **Use** tab and choose **Create copy**.
