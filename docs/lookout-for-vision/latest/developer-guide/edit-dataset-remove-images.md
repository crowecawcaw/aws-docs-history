End of support notice: On October 31, 2025, AWS
will discontinue support for Amazon Lookout for Vision. After October 31, 2025, you will
no longer be able to access the Lookout for Vision console or Lookout for Vision resources.
For more information, visit this [blog post](https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision "https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision").

# Removing images from your dataset

You can't delete images directly from a dataset. Instead you must delete the existing
dataset and create a new dataset without the images that you want to remove. How you
remove images depends how you imported images into the existing dataset ([manifest file](create-dataset-use-manifest.md "create-dataset-use-manifest.md"), [Amazon S3 bucket](create-dataset-s3.md "create-dataset-s3.md"), or [local computer](create-dataset-computer-upload.md "create-dataset-computer-upload.md")).

You can also use the AWS SDK to remove images. This is useful when creating an image
segmentation model without an [image
segmentation manifest file](manifest-file-segmentation.md "manifest-file-segmentation.md"), making it unnecessary to redraw the image masks
with the Amazon Lookout for Vision console.

###### Topics

- [Removing images from a dataset (Console)](#edit-dataset-remove-images-console "#edit-dataset-remove-images-console")
- [Removing images from a dataset (SDK)](#edit-dataset-remove-images-sdk "#edit-dataset-remove-images-sdk")

## Removing images from a dataset (Console)

Use the following procedure to remove images from a dataset with the Amazon Lookout for Vision
console.

###### To remove images from a dataset (console)

1. [Open](view-datasets.md "view-datasets.md") the project's dataset gallery.
2. Note the name of each image that you want to remove.
3. [Delete](delete-dataset.md "delete-dataset.md") the existing dataset.
4. Do one of the following:
   - If you created the dataset with a manifest file, do:
     1. In a text editor, open the manifest file that you used to
        create the dataset.
     2. Remove the JSON line for each image that you noted in step
     3. You can identify the JSON line for an image by checking
        the `source-ref` field.
     4. Save the manifest file.
     5. [Create](create-dataset-use-manifest.md "create-dataset-use-manifest.md") a new
        dataset with the updated manifest file.

   - If you created the dataset from images imported from an Amazon S3 bucket,
     do:
     1. [Delete](../../../AmazonS3/latest/userguide/delete-objects.md "../../../AmazonS3/latest/userguide/delete-objects.md") the images you noted in step 2 from the
        Amazon S3 bucket.
     2. [Create](create-dataset-s3.md "create-dataset-s3.md") a new
        dataset with the remaining images in the Amazon S3 bucket.
        If you classify images by folder name, you don't need to classify images
        in the next step.
     3. Do one of the following:
        - If you are creating an image classification model, [classify](model-label.md "model-label.md")
          each unlabeled image.
        - If you are creating an image segmentation model,
          [classify and segment](segment-image.md "segment-image.md") each unlabeled image.

   - If you created the dataset from images imported from a
     local computer, do:
     1. On your computer, create a folder with the images that you
        want to use. Don't include the images you want to remove
        from the dataset. For more information, see [Creating a dataset using images
        stored on your local computer](create-dataset-computer-upload.md "create-dataset-computer-upload.md").
     2. [Create](create-dataset-computer-upload.md "create-dataset-computer-upload.md") the dataset with the images in the folder
        that you created in step 4.a.
     3. Do one of the following:
        - If you are creating an image classification model, [classify](model-label.md "model-label.md")
          each unlabeled image.
        - If you are creating an image segmentation model,
          [classify and segment](segment-image.md "segment-image.md") each unlabeled image.

5. [Train](model-train.md#create-model-sdk "model-train.md#create-model-sdk") the model.

## Removing images from a dataset (SDK)

You can use the AWS SDK to remove images from a dataset.

###### To remove images from a dataset (SDK)

1. [Open](view-datasets.md "view-datasets.md") the project's dataset gallery.
2. Note the name of each image that you want to remove.
3. Export the JSON lines for the dataset by using the [ListDatasetEntries](../APIReference/API_ListDatasetEntries.md "../APIReference/API_ListDatasetEntries.md") operation.
4. [Create](manifest-files.md "manifest-files.md") a manifest file with the exported JSON lines.
5. In a text editor, open the manifest file.
6. Remove the JSON line for each image that you noted in step
7. You can identify the JSON line for an image by checking
   the `source-ref` field.
8. Save the manifest file.
9. [Delete](delete-dataset.md#delete-dataset-sdk "delete-dataset.md#delete-dataset-sdk") the existing dataset.
10. [Create](create-dataset-sdk.md "create-dataset-sdk.md") a new
    dataset with the updated manifest file.
11. [Train](model-train.md "model-train.md") the model.
