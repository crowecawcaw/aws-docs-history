# Creating training and test datasets

A dataset is a set of images and labels that describe
those images. Your project needs a training dataset and a test dataset. Amazon Rekognition Custom Labels uses the training dataset
to train your model. After training, Amazon Rekognition Custom Labels uses the test dataset to verify how well the trained model predicts the correct
labels.

You can create datasets with the Amazon Rekognition Custom Labels console or with the AWS SDK. Before
creating a dataset, we recommend reading [Understanding Amazon Rekognition Custom Labels](understanding-custom-labels.md "understanding-custom-labels.md"). For other dataset tasks, see [Managing datasets](managing-dataset.md "managing-dataset.md").

The steps creating training and tests datasets for a project are:

###### To create training and test datasets for your project

1. Determine how you need to label your training and test datasets. For more information, [Purposing datasets](md-dataset-purpose.md "md-dataset-purpose.md").
2. Collect the images for your training and test datasets. For more information, see [Preparing images](md-prepare-images.md "md-prepare-images.md").
3. Create the training and test datasets. For more information, see [Creating training and test datasets with images](md-create-dataset.md "md-create-dataset.md").
   If you're using the AWS SDK, see [Create training and test datasets (SDK)](md-create-dataset.md#cd-create-dataset-sdk "md-create-dataset.md#cd-create-dataset-sdk") .
4. If necesessary, add image-level labels or bounding boxes to your dataset images. For more information, see [Labeling images](md-labeling-images.md "md-labeling-images.md").
   After you create the datasets, you can [train](training-model.md "training-model.md") the model.

###### Topics

- [Purposing datasets](md-dataset-purpose.md "md-dataset-purpose.md")
- [Preparing images](md-prepare-images.md "md-prepare-images.md")
- [Creating training and test datasets with images](md-create-dataset.md "md-create-dataset.md")
- [Labeling images](md-labeling-images.md "md-labeling-images.md")
- [Debugging datasets](debugging-datasets.md "debugging-datasets.md")
