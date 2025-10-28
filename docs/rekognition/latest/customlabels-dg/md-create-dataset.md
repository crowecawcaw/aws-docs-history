# Creating training and test datasets with images

You can start with a project that has a single
dataset, or a project that has separate training and test datasets. If you
start with a single dataset, Amazon Rekognition Custom Labels splits your dataset during training to create
a training dataset (80%) and a test dataset (%20) for your project.
Start with a single dataset if you
want Amazon Rekognition Custom Labels to decide where images are used for training and testing.
For complete control over training, testing, and performance tuning, we recommend that
you start your project with separate training and test datasets.

You can create training and test datasets for a project by importing images from one of the following locations:

- [Importing images from an Amazon S3 bucket](md-create-dataset-s3.md "md-create-dataset-s3.md")
- [Importing images from a local
  computer](md-create-dataset-computer.md "md-create-dataset-computer.md")
- [Using a manifest file to import
  images](md-create-dataset-ground-truth.md "md-create-dataset-ground-truth.md")
- [Copying content from an
  existing dataset](md-create-dataset-existing-dataset.md "md-create-dataset-existing-dataset.md")
  If you start your project with separate training and test datasets, you can use different source locations for each dataset.

Depending on where you import your images from, your images might be unlabeled.
For example, images imported from a local computer aren't labeled. Images imported from
an Amazon SageMaker AI Ground Truth manifest file are labeled. You can use the Amazon Rekognition Custom Labels console
to add, change, and assign labels. For more information, see [Labeling images](md-labeling-images.md "md-labeling-images.md").

If images are uploading with errors, images are missing, or labels are missing from images,
read [Debugging a failed model training](tm-debugging.md "tm-debugging.md").

For more information about datasets, see [Managing datasets](managing-dataset.md "managing-dataset.md").

## Create training and test datasets (SDK)

You can use the AWS SDK to create training and test datasets.

The `CreateDataset` operation allows you to optionally specify tags
when creating a new dataset, for the purposes of categorizing and managing your
resources.

### Training dataset

You can use the AWS SDK to create a training dataset in the following
ways.

- Use [CreateDataset](../APIReference/API_CreateDataset.md "../APIReference/API_CreateDataset.md") with an Amazon Sagemaker format manifest file
  that you provide. For more information, see [Creating a manifest file](md-create-manifest-file.md "md-create-manifest-file.md"). For example code, see [Creating a dataset with a
  SageMaker AI Ground Truth manifest file (SDK)](md-create-dataset-ground-truth.md#md-create-dataset-ground-truth-sdk "md-create-dataset-ground-truth.md#md-create-dataset-ground-truth-sdk").
- Use `CreateDataset` to copy an existing Amazon Rekognition
  Custom Labels dataset. For example code, see [Creating a dataset using an existing dataset (SDK)](md-create-dataset-existing-dataset-sdk.md "md-create-dataset-existing-dataset-sdk.md").
- Create an empty dataset with `CreateDataset` and add
  dataset entries at a later time with [UpdateDatasetEntries](../APIReference/API_UpdateDatasetEntries.md "../APIReference/API_UpdateDatasetEntries.md"). To create an empty dataset, see [Adding a dataset to a project](md-add-dataset.md "md-add-dataset.md"). To add
  images to a dataset, see [Adding more images (SDK)](md-add-images.md#md-add-images-sdk "md-add-images.md#md-add-images-sdk"). You need to add the dataset
  entries before you can train a model.

### Test dataset

You can use the AWS SDK to create a test dataset in the following
ways:

- Use [CreateDataset](../APIReference/API_CreateDataset.md "../APIReference/API_CreateDataset.md") with an Amazon Sagemaker format manifest file
  that you provide. For more information, see [Creating a manifest file](md-create-manifest-file.md "md-create-manifest-file.md"). For example code, see [Creating a dataset with a
  SageMaker AI Ground Truth manifest file (SDK)](md-create-dataset-ground-truth.md#md-create-dataset-ground-truth-sdk "md-create-dataset-ground-truth.md#md-create-dataset-ground-truth-sdk").
- Use `CreateDataset` to copy an existing Amazon Rekognition
  Custom Labels dataset. For example code, see [Creating a dataset using an existing dataset (SDK)](md-create-dataset-existing-dataset-sdk.md "md-create-dataset-existing-dataset-sdk.md").
- Create an empty dataset with `CreateDataset` and add
  dataset entries at a later time with `UpdateDatasetEntries`.
  To create an empty dataset, see [Adding a dataset to a project](md-add-dataset.md "md-add-dataset.md"). To add images to a dataset, see
  [Adding more images (SDK)](md-add-images.md#md-add-images-sdk "md-add-images.md#md-add-images-sdk"). You need to add the dataset entries before you can train a
  model.
- Split the training dataset into separate training and test datasets.
  First create an empty test dataset with `CreateDataset`. Then
  move 20% of the training dataset entries into the test dataset by
  calling [DistributeDatasetEntries](../APIReference/API_DistributeDatasetEntries.md "../APIReference/API_DistributeDatasetEntries.md"). To create an empty dataset, see
  [Adding a dataset to a project (SDK)](md-add-dataset.md#md-add-dataset-sdk "md-add-dataset.md#md-add-dataset-sdk"). To split the training dataset,
  see [Distributing a training dataset (SDK)](md-distributing-datasets.md "md-distributing-datasets.md").
