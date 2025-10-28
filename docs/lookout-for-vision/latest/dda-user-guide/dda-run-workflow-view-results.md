Defect Detection App is in preview release and is subject to change.

# Viewing digital input signal results

If a digital input signal triggers the running of a
workflow, you can use the Station App to see the analysis results for the last image analyzed. To get
the analysis information for older images, you need to look at the analysis files that
the workflow stores for each image. For more information, see [Getting all workflow results](dda-run-workflow-results.md "dda-run-workflow-results.md").

You can use the Station App to view the analysis results for the last image
the workflow has analyzed. The Station App polls for new analysis results at 500 millisecond intervals.

###### To view workflow results (Station App)

1.  Open the Station App on your edge device by opening a browser and navigating to
    `x.x.x.x`:3000. Change `x.x.x.x` to the IP address of
    your edge device.
2.  On the left of the application, choose **Results** and then **Monitor live results**.
3.  In the **Live results** section, choose the workflow that that you want to use.
4.  View the analysis results for the latest image.

        * **Prediction** is the classification that the model predicts
         for the image (**Normal** for a normal
         image, **Anomaly** for an anomalous image).
        * **Confidence** is the model's confidence in the
         accuracy of the **Prediction**.
        * **Anomaly score** quantifies how much anomalies
         predicted for the image deviate from an images without anomalies.
         **anomaly\_score** is a float value ranging from
         `0.0` to (lowest deviation from a normal image) to `1.0`
         (highest deviation from a normal image).
        * **Anomaly threshold** is a number in the anomaly
         score range that determines the boundary between an anomalous image or a
         normal image. The model predicts the image is anomalous if the **anomaly
         score** is higher than the **anomaly threshold**. The
         value is calculated during the training of the model and you are not able to can't set a
         specific value for a model.
        * If the model is a [segmentation](dda-components.md#dda-ud-image-segmentation "dda-components.md#dda-ud-image-segmentation") model or a [heatmap](dda-components.md#dda-ud-image-segmentation-heatmap "dda-components.md#dda-ud-image-segmentation-heatmap") model,
         **Anomaly labels** lists the types of predicted
         anomalies and draws masks around the anomalies on the image. Each type
         of anomaly is shown in a different color. With a heatmap model the
         anomaly label is alway **Anomaly**.


        You can show or hide the masks
         with the **Show anomaly masks** toggle.
        * The name of the model that analyzed the image.
        * **Result date** is the date and time that the model
         analyzed the image.
        * **Model** is the name of the model that analyzed the
         image.
        * **Workflow trigger** is the trigger that made the
         workflow run (Line operater/API call or line input).
        * **processing time** is the time, in milliseconds, that
         it took to run the workflow with the image.
        * **Output file** is the location where the workflow
         saves the analyzed image file.

    You can use the following commands to pan and zoom the image.

        * Pan image — Choose the pan button (
        ![Pan](images/pan.png)
        ). Click and hold the mouse button and then drag the
         mouse to pan across the image.
        * Zoom image — Zoom in an out of the image with the zoom in button (
        ![Zoom in](images/zoom-in.png)
        ) and the zoom out button
        ![Zoom out](/images/lookout-for-vision/latest/dda-user-guide/images/zoom-out.png)
        . Double-click the image to zoom 2x into to the
         image. Use the mouse scroll wheel to zoom in and out of the image. The
         mouse cursor position is the center position for zooming (in or
         out).
        * Reset image size — Choose the reset button (
        ![Reset image](/images/lookout-for-vision/latest/dda-user-guide/images/reset.png)
        ) or press Ctrl + 0.
