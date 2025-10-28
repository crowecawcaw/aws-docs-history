End of support notice: On October 31, 2025, AWS
will discontinue support for Amazon Lookout for Vision. After October 31, 2025, you will
no longer be able to access the Lookout for Vision console or Lookout for Vision resources.
For more information, visit this [blog post](https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision "https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision").

# Verifying your model with a trial detection

task

If you want to verify or improve the quality of your model, you can run a trial
detection task. A trial detection task detects anomalies in new images that you supply.

You can verify the detection results and add the verified images to your dataset. If you
have separate training and test datasets, the verified images are added to the training
dataset.

You can verify images from your local computer or images located in an Amazon S3 bucket.
If you want to add verified images to the dataset, images located in an S3 bucket
must be in the same S3 bucket as the images in your dataset.

###### Note

To run a trial detection task, ensure that your S3 bucket has versioning enabled. For more information,
see [Using versioning](../../../AmazonS3/latest/dev/Versioning.md "../../../AmazonS3/latest/dev/Versioning.md").
The console bucket is created with versioning enabled.

By default your images are encrypted with a key that AWS owns and manages. You can also
choose to use your own AWS Key Management Service (KMS) key. For more information, see [AWS Key Management Service concepts](../../../kms/latest/developerguide/concepts.md#master_keys "../../../kms/latest/developerguide/concepts.md#master_keys").

###### Topics

- [Running a trial detection task](#run-trial-detection "#run-trial-detection")
- [Verifying trial detection
  results](#verify-trial-detection-results "#verify-trial-detection-results")
- [Correcting segmentation labels with the annotation tool](#verify-trial-detection-results-annotation-tool "#verify-trial-detection-results-annotation-tool")

## Running a trial detection task

Perform the following steps to run a trial detection task.

###### To run a trial detection (console)

1. Open the Amazon Lookout for Vision console at [https://console.aws.amazon.com/lookoutvision/](https://console.aws.amazon.com/lookoutvision/ " https://console.aws.amazon.com/lookoutvision/").
2. Choose **Get started**.
3. In the left navigation pane, choose **Projects**.
4. In the projects view, choose the project that contains the version of the model that you want to view.
5. In the left navigation pane, under the project name, choose **Trial detections**.
6. In the trial detections view, choose the **Run trial detection**.
7. On the **Run trial detection** page, enter a name for your trial detection
   task in **Task name**.
8. In **Choose model**, choose the version of that model that you want to
   use.
9. Import the images according to the source of the images as follows:
   - If you are importing your source images from an Amazon S3 bucket, enter the **S3
     URI**.

   ###### Tip

   If you're using the Getting Started example images, use the _extra_images_ folder. The Amazon S3 URI is `s3://`your bucket`/circuitboard/extra_images`.
   - If you are uploading images from your computer, add the images after you choose
     **Detect anomalies**.

10. (Optional) If you want to use your own AWS KMS encryption key, do the following:
    1. For **Image data encryption**, choose **Customize encryption settings
       (advanced)**.
    2. In **encryption.aws_kms_key**, enter the Amazon Resource Name (ARN) of your
       key, or choose an existing AWS KMS key. To create a new key, choose
       **Create an AWS IMS key**.

11. Choose **Detect anomalies** and then choose **Run trial
    detection** to start the trial detection task.
12. Check the current status in the trial detections view. The trial detection might take a while
    to complete.

## Verifying trial detection

results

Verifying the results of a trial detection can help you improve your model.

If the performance metrics are poor, improve your model by running a trial detection and then add
verified images to the dataset (training dataset, if you have a separate datasets).

If the model's performance metrics are good, but the results of a trial
detection are poor, you can improve your model by adding verified images to the
dataset (training dataset). If you have a separate test dataset, consider adding
more images to the test dataset.

After you add verified images to your dataset, retrain and re-evaluate your model.
For more information, see [Training your model](model-train.md "model-train.md").

###### To verify the results of a trial detection

1. Open the Amazon Lookout for Vision console at [https://console.aws.amazon.com/lookoutvision/](https://console.aws.amazon.com/lookoutvision/ " https://console.aws.amazon.com/lookoutvision/").
2. In the left navigation pane, choose **Projects**.
3. In the **Projects** page, choose the project that you want to use.
   The dashboard for your project is displayed.
4. In the left navigation pane, choose **Trial detections**.
5. Choose the trial detection that you want to verify.
6. On the trial detection page, choose **Verify machine predictions**.
7. Choose **Select all images on this page**.
8. If the predictions are correct, choose **Verify as correct**. Otherwise,
   choose **Verify as incorrect**. The prediction and
   prediction confidence score is shown under each image.
9. If you need to change the label for an image, do the following:
   1. Choose **Correct** or **Incorrect** under the image.
   2. If you can't determine the correct label for an image, magnify the image by choosing the image
      in the gallery.###### Note

You can filter image labels by choosing the desired label, or label state, in the
**Filters** section. You can sort by confidence
score in the **Sorting options** section. 10. If your model is a segmentation model and the mask or anomaly label for an
image is wrong, choose **Anomalous area** under the image
and open the annotation tool. Update the segmentation information by doing
[Correcting segmentation labels with the annotation tool](#verify-trial-detection-results-annotation-tool "#verify-trial-detection-results-annotation-tool"). 11. Repeat steps 7-10 on each page as necessary until all the images have been verified. 12. Choose **Add verified images to dataset**. If you have separate datasets, the
images are added to the training dataset. 13. Retrain your model. For more information, see [Training your model](model-train.md "model-train.md").

## Correcting segmentation labels with the annotation tool

You use the annotation tool to segment an image by marking anomalous areas with a mask.

###### To correct the segmentation labels for an image with the annotation tool

1. Open the annotation tool by selecting **anomalous area** under an image in the dataset gallery.
2. If the anomaly label for a mask isn't correct, choose the mask and then choose the correct
   anomaly label under **Anomaly labels**. If necessary, choose **Add anomaly label** to add a new anomaly label.
3. If the mask isn't correct, choose a drawing tool at the bottom of the page and draw masks that tightly covers anomalous areas for the anomaly label.
   The following image is an example of a mask that tightly covers an anomaly.

![Car exterior with blue paint scratch marks on white body panel near headlight.](images/good-mask.png)

The following is an example of a poor mask that doesn't tightly cover an anomaly.

![Car panel with visible damage and scratches near the headlight, highlighted by blue outline.](images/poor-mask.png) 4. If you have more images to correct, choose **Next** and repeat steps 2 and 3. 5. Choose **Submit and close** to finish updating images.
