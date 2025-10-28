# Image Classification - TensorFlow

The Amazon SageMaker Image Classification - TensorFlow algorithm is a supervised learning algorithm
that supports transfer learning with many pretrained models from the [TensorFlow Hub](https://tfhub.dev/s?fine-tunable=yes&module-type=image-classification&subtype=module,placeholder&tf-version=tf2 "https://tfhub.dev/s?fine-tunable=yes&module-type=image-classification&subtype=module,placeholder&tf-version=tf2"). Use transfer learning to fine-tune one of the available pretrained
models on your own dataset, even if a large amount of image data is not available. The image
classification algorithm takes an image as input and outputs a probability for each provided
class label. Training datasets must consist of images in .jpg, .jpeg, or .png format. This
page includes information about Amazon EC2 instance recommendations and sample notebooks for
Image Classification - TensorFlow.

###### Topics

- [How to use the SageMaker Image Classification - TensorFlow algorithm](IC-TF-how-to-use.md "IC-TF-how-to-use.md")
- [Input and output interface for the Image
  Classification - TensorFlow algorithm](IC-TF-inputoutput.md "IC-TF-inputoutput.md")
- [Amazon EC2 instance recommendation for the Image
  Classification - TensorFlow algorithm](#IC-TF-instances "#IC-TF-instances")
- [Image Classification - TensorFlow sample
  notebooks](#IC-TF-sample-notebooks "#IC-TF-sample-notebooks")
- [How Image Classification - TensorFlow Works](IC-TF-HowItWorks.md "IC-TF-HowItWorks.md")
- [TensorFlow Hub Models](IC-TF-Models.md "IC-TF-Models.md")
- [Image Classification - TensorFlow
  Hyperparameters](IC-TF-Hyperparameter.md "IC-TF-Hyperparameter.md")
- [Tune an Image Classification - TensorFlow model](IC-TF-tuning.md "IC-TF-tuning.md")

## Amazon EC2 instance recommendation for the Image

Classification - TensorFlow algorithm

The Image Classification - TensorFlow algorithm supports all CPU and GPU instances for
training, including:

- `ml.p2.xlarge`
- `ml.p2.16xlarge`
- `ml.p3.2xlarge`
- `ml.p3.16xlarge`
- `ml.g4dn.xlarge`
- `ml.g4dn.16.xlarge`
- `ml.g5.xlarge`
- `ml.g5.48xlarge`

We recommend GPU instances with more memory for
training with large batch sizes. Both CPU (such as M5) and GPU (P2, P3, G4dn, or G5)
instances can be used for inference.

## Image Classification - TensorFlow sample

notebooks

For more information about how to use the SageMaker Image Classification - TensorFlow algorithm for transfer learning on a custom dataset, see the [Introduction to SageMaker TensorFlow - Image Classification](https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/image_classification_tensorflow/Amazon_TensorFlow_Image_Classification.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/image_classification_tensorflow/Amazon_TensorFlow_Image_Classification.ipynb") notebook.

For instructions how to create and access Jupyter notebook instances that you can use to
run the example in SageMaker AI, see [Amazon SageMaker notebook instances](nbi.md "nbi.md"). After you have
created a notebook instance and opened it, select the **SageMaker AI
Examples** tab to see a list of all the SageMaker AI samples. To open a notebook,
choose its **Use** tab and choose **Create copy**.
