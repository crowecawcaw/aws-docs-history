Defect Detection App is in preview release and is subject to change.

# Viewing performance metrics

After training is complete, the console displays the performance metrics.

The Defect Detection App console shows the following performance metrics for the classifications made
during testing:

- [Precision](dda-performance-metrics.md#dda-precision-metric "dda-performance-metrics.md#dda-precision-metric")
- [Recall](dda-performance-metrics.md#dda-recall-metric "dda-performance-metrics.md#dda-recall-metric")
- [F1 score](dda-performance-metrics.md#dda-f1-metric "dda-performance-metrics.md#dda-f1-metric")
  The test results overview section shows you the total correct and incorrect predictions for
  images in the test dataset. You can also see the predicted and actual label assignments for
  individual images in the test dataset.

The following procedure shows how to get the performance metrics from a project's model
list view.

###### To view performance metrics

1. If you're not on the project details page, do the following:
   1. [Sign in](dda-signin-dda-web-app.md "dda-signin-dda-web-app.md") to the Defect Detection App Console.
   2. In the top navigation pane, choose **Projects**.
   3. On the projects page, choose the project. The console opens the project details page.

2. From the **Model versions** tab,choose the model that you want to view.
3. On the model page, view the performance metrics in the model details panel.
   The panel displays the overall model metrics (precision, recall, F1 score)
   for the test images.
4. Note the following:

The **Test results overview** section provides the results for each
test image that Defect Detection App uses to evaluate the model. It includes the following:

    * The total number of correct (true positive) and incorrect (false negative)
     classification predictions (normal or anomaly) for all test images.
    * The classification prediction for each test image. If you see
     **Prediction correct** under an image, the predicted classification matches the
     actual classification for the image. Otherwise the model didn't correctly classify the
     image.
    * With an image segmentation model, you see anomaly labels that the model assigned to
     the image and masks on the image that match the colors of the anomaly labels.
