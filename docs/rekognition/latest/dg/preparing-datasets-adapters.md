# Preparing your datasets

Creating an adapter requires you to provide Rekognition with two datasets, a training
dataset and a testing dataset. Each dataset is comprised of provide two elements:
images and annotations/labels. The following sections explain what labels and images
are used for and how they come together to create datasets.

## Images

You will need to train an adapter on representative samples of your images. When
you select images for training, try to include at least a few images that
demonstrate the expected response for each of the labels you are targeting with your
adapter.

To create a training dataset, you need to provide one of the following two
image types:

- Images with False Positive predictions. For example, when a base model
  predicts that an image has alcohol, but it doesn't.
- Images with False Negative predictions. For example, when a base model
  predicts that an image doesn't have alcohol, but it does.

To create a balanced dataset, it is recommended that you provide one of the
following two image types:

- Images with True Positive predictions. For example, when a base model
  correctly predicts that an image has alcohol. It is recommended to
  provide these images if you provide False Positive images.
- Images with True Negative predictions. For example, when a base model
  correctly predicts that an image doesn't have alcohol. It is recommended
  to provide these images if you provide False Negative images.

## Labels

A label refers to any of the following: objects, events, concepts or activities.
For Content Moderation, a label is an instance of content that is inappropriate,
unwanted, or offensive.

In the context of creating an adapter by training Rekognition’s base model, when a label
is assigned to an image it’s called an annotation. When training an adapter with the
Rekognition Console, you’ll use the Console to add annotations to your images by choosing
a label and then tagging images that corresponds with the label. Through this
process, the model learns to identify elements of your images based on the assigned
label. This linking process allows the model to focus on the most relevant content
when an adapter is created, leading to improved accuracy for image analysis.

Alternatively, you can provide a manifest files, which contains information on
images and the annotations that go with them.

## Training and testing datasets

The training dataset is the basis for fine-tuning the model and creating a custom adapter.
You must provide an annotated training dataset for the model to learn from. The model learns from this dataset
to improve its performance on the type of images you provide.

To improve accuracy, you must create your training dataset by annotation/labeling images. You can accomplish this in two ways:

- Manual label assignment - You can use the Rekognition Console to create a training dataset by
  uploading the images you want your dataset to contain and then manually
  assign labels to these images.
- Manifest file — You can use a manifest file to train your adapter. The manifest file
  contains information on the ground-truth annotations for your training and
  testing images, as well as the location of your training images. You can provide the manifest file
  when training an adapter using the Rekognition APIs or when using the AWS Console.

The testing dataset is used to evaluate the adapter’s performance after training.
To ensure reliable evaluation, the testing dataset is created by using a slice of
the original training dataset that the model hasn’t seen before. This process
ensures that the adapter’s performance is assessed with new data, creating accurate
measurements and metrics. For optimal accuracy improvements see [Best practices for training
adapters](using-adapters-best-practices.md "using-adapters-best-practices.md") .
