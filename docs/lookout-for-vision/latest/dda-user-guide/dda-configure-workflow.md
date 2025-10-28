Defect Detection App is in preview release and is subject to change.

# Configuring a workflow

You configure a workflow with the Station App. Configure the workflow
according to your business needs. You have the following configuration choices.

- **Workflow name and description** — The name and optional description for the workflow.
- **Image source** — An image source is where the workflow gets images that it analyzes with a model. An image source can be
  a camera or a local folder on the edge device. If the image source is a folder, the process for adding images to the folder is determined by the needs of your business and is outside the scope
  this documentation.
- **Model** — The Amazon Lookout for Vision [model](dda-components.md#dda-component-model "dda-components.md#dda-component-model") that the workflow uses to analyze images.
- **Manual workflow trigger** — You can run
  a workflow manually by using the Station App. This lets your line operators choose when a workflow should run.
- **Digital input trigger** — A digital signal that triggers the running of a workflow. For example, you can specify that
  you want a _GPIO.FALLING_ signal to start the workflow running. If you specify a digital input,
  you can still manually run the workflow.
- **Outputs** — Analysis results from the running of a workflow is stored on edge device for later use. You can get the location
  from the Station App. The analysis results include a predicted classification for the model and the model's
  confidence in the accuracy of its prediction. If the model is a segmentation model, you can
  see the masks and anomaly labels for any predicted anomalies.

Optionally, you can configure a digital signal that a workflow sends when it completes
analysis of an image with the model. You can also apply a rule that determines if the signal is sent. For example, you can specify that you want a
_Falling edge_ signal sent when the model predicts that an image contains an anomaly.
Before you can configure the workflow, make sure you have an image source and have deployed a model to the
edge device. For more information, see [Adding an image source](dda-configure-image-source.md "dda-configure-image-source.md")
and [Deploying your model to a station](dda-deploy-model.md "dda-deploy-model.md").

###### To configure a workflow (Station App)

1. Open the Station App on your edge device by opening a browser and navigating to
   `x.x.x.x`:3000. For `x.x.x.x`, use the IP address of
   your edge device.
2. From the left menu, choose **Management** and then **Workflows**.
3. In the **Workflows** section, select the workflow that you want to configure.
4. Choose **Edit workflow**.
5. In **Workflow details** enter a name and optional description for the workflow.
6. In **Image source and model**, choose the image source (**Image source**) and
   model (**Model**) that you want to use in the workflow.
7. For **Workflow trigger**, choose one of the following:
   - If you want a line operator to manually trigger the running of the
     workflow in the Station App, choose **Line operator or API
     call.**
   - If you want a device pin signal to trigger the workflow, do the following:
     1. choose **Digital input**.
     2. For **Signal type** choose the type of signal that triggers the workflow
        (**Rising edge** or **Falling edge**).
     3. For **Pin value**, enter the input pin that sends the signal.
     4. For **Debounce time** enter the amount of time, in mulliseconds, that the workflow ignores
        repeated signals.

8. (Optional) If you want the workflow to send a digital signal after analyzing the image, do the following:
   1. In the **Outputs** section choose **Add output**.
   2. For **Signal type** choose the type of signal that you want the workflow to send.
      (**Rising edge** or **Falling edge**).
   3. For **Pin value**, enter the input pin that you want to workflow to send the signal to.
   4. For **Pulse width** enter the amount of time, in mulliseconds, that the workflow sends the signal for.
   5. For **Rule**, choose the rule that runs the workflow. You can choose to run the rule if the model
      predicts an anomalous image, a normal image, or all images, regardless of the model's prediction.
   6. Choose **Save** and to add the output.

   ###### Note

   The digital signal can trigger the workflow as soon as you add the output.

9. Choose **Save** to save the workflow
