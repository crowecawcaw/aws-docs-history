End of support notice: On October 31, 2025, AWS
will discontinue support for Amazon Lookout for Vision. After October 31, 2025, you will
no longer be able to access the Lookout for Vision console or Lookout for Vision resources.
For more information, visit this [blog post](https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision "https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision").

# Creating your dataset

A dataset contains the images and assigned labels that you use to train and test a
model. You create the dataset for your project with the Amazon Lookout for Vision console or with the
[CreateDataset](../APIReference/API_CreateDataset.md "../APIReference/API_CreateDataset.md") operation. The
dataset images must be labeled according to the type of model that you want to create
(image classification or image segmentation).

###### Topics

- [Preparing images for a dataset](#model-prepare-images "#model-prepare-images")
- [Creating the dataset](#model-creating-dataset "#model-creating-dataset")
- [Creating a dataset using images
  stored on your local computer](create-dataset-computer-upload.md "create-dataset-computer-upload.md")
- [Creating a dataset using images stored in an
  Amazon S3 bucket](create-dataset-s3.md "create-dataset-s3.md")
- [Creating a dataset using an Amazon SageMaker AI
  Ground Truth manifest file](create-dataset-ground-truth.md "create-dataset-ground-truth.md")

## Preparing images for a dataset

You need a collection of images to create a dataset. Your images must be PNG or JPEG
format files. The number and type of images you need depends on if your project has a single
a single dataset or separate training and test datasets.

### Single dataset project

To create an image classification model, you need the following to start training:

- At least 20 images of normal objects.
- At least 10 images of anomalous objects.

To create an image segmentation model, you need the following to start training:

- At least 20 images of each anomaly type.
- Each anomalous image (image with anomaly types present) must have only one type of anomaly.
- At least 20 images of normal objects.

### Separate training and test dataset project

To create an image classification model, you need the following:

- At least 10 images of normal objects in the training dataset.
- At least 10 images of normal objects in the test dataset.
- At least 10 images of anomalous objects in the test dataset.

To create an image
segmentation model, you need the following:

- Each dataset needs at least 10 images of each anomaly type.
- Each anomalous image (image with anomaly types present) must contain only one type of anomaly.
- Each dataset must have at least 10 images of normal objects.

To create a higher quality model, use more than the minimum number of images. If
you are creating a segmentation model, we recommend including images with multiple
anomaly types, but these don't count towards the minimum that Lookout for Vision needs to start
training.

Your images should be of a single type of object. Also, you should have consistent
image capture conditions, such as camera positioning, lighting, and object pose.

All images in the training and test datasets must have the same dimensions. Later,
the images that you analyze with your trained model must have the same dimensions as
the training and test dataset images. For more information, see [Detecting anomalies in an image](inference-detect-anomalies.md "inference-detect-anomalies.md").

All training and test images must be unique images, preferably of unique objects.
Normal images should capture the normal variations of the object being analyzed.
Anomalous images should capture a diverse sampling of anomalies.

Amazon Lookout for Vision provides example images that you can use. For more information, see [Image classification
dataset](example-datasets.md#example-datasets-classification "example-datasets.md#example-datasets-classification").

For image limits, see [Quotas in Amazon Lookout for Vision](limits.md "limits.md").

## Creating the dataset

When you create the dataset for your project, you choose the initial dataset
configuration of your project. You also choose where Lookout for Vision imports the images from.

### Choosing a dataset configuration for your project

When you create the first dataset in your project, you choose one of the
following dataset configurations:

- **Single dataset** – A single dataset
  project uses a single dataset to train and test your model. Using a single
  dataset simplifies training by letting Amazon Lookout for Vision choose the training and test
  images. During training, Amazon Lookout for Vision, internally splits the dataset into a
  training dataset and a test dataset. You don't have access to the split
  datasets. We recommend using a single dataset project for most scenarios.
- **Separate training and test datasets** –
  If you want finer control over training, testing, and performance tuning, you
  can configure your project to have separate training and test datasets. Use a
  separate test dataset if you want control over the images used for testing, or
  if you already have a benchmark set of images that you want to use.

You can add a test dataset to an existing single dataset project. The single dataset
then becomes the training dataset. If you remove the test dataset from a project with
separate training and test datasets, the project becomes a single dataset project. For
more information, see [Deleting a dataset](delete-dataset.md "delete-dataset.md").

### Importing images

When you create a dataset, you choose where to import the images from. Depending on how you
import the images, the images might already be labeled. If the images aren't labeled
after creating the dataset, see [Labeling images](model-labelling-overview.md "model-labelling-overview.md").

You create a dataset and import its images in one of the following ways:

- [Import images from your
  local computer](create-dataset-computer-upload.md "create-dataset-computer-upload.md"). The images aren't labeled. You add
  or labels by using the Lookout for Vision console.
- [Import images from an S3
  bucket](create-dataset-s3.md "create-dataset-s3.md"). Amazon Lookout for Vision can classify images by using
  the folder names to label the images. Use `normal` for normal
  images. Use `anomaly` for anomalous images. You can't automatically
  assign segmentation labels.
- [Import an Amazon SageMaker AI Ground
  Truth manifest file](create-dataset-ground-truth.md "create-dataset-ground-truth.md"), which includes labeled images. You can
  create and import your own manifest file. If you have many images,
  consider using the SageMaker AI Ground Truth labeling service. You then import
  the output manifest file from the Amazon SageMaker AI Ground Truth job. If
  necessary, you can use the Lookout for Vision console to add or change
  labels.

If you're using the AWS SDK, you create a dataset with an Amazon SageMaker AI Ground
Truth manifest file. For more information, see [Creating a dataset using an Amazon SageMaker AI
Ground Truth manifest file](create-dataset-ground-truth.md "create-dataset-ground-truth.md").

If, after creating your dataset, your images are labeled, you can [train the model](model-train.md "model-train.md").
If the images aren't labeled, add the labels according to the type of model that
you want to create. For more information, see
[Labeling images](model-labelling-overview.md "model-labelling-overview.md").

You can add more images to an existing dataset. For more information,
see [Adding images to your dataset](edit-dataset.md "edit-dataset.md").
