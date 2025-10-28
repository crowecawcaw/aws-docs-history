Defect Detection App is in preview release and is subject to change.

# Analyzing images with the Defect Detection Station App

After deploying your model to a station, you use the Station App to analyze and process
images. A workflow on the Station App defines the steps taken to analyze an image and process
the analysis results. You configure the workflow according to your business needs. You can
configure a workflow to be triggered manually from within the Station App. You can also trigger
a workflow automatically by using a digit input signal.

The image the workflow analyzes can be obtained from a camera attached to the
station, or retrieved from a local folder on the device. You specify which by creating an
image source and attaching it to the workflow. If the image source is a folder, the workflow
analyzes the oldest image in the folder that hasn't yet been analyzed. After analyzing the
image, the workflow deletes the image from the folder. If the image source is a camera, the
workflow takes an image from the camera and analyzes that image. Optionally, you can trigger
a digital output signal based on the analysis results from the workflow. You can configure
the workflow with the Station App.

After you configure the workflow, it analyzes images according to its configuration. The
Station App allows you to see the results for the most recently analyzed image. You can
also access information about all analyzed image from a folder on the station.

You specify the number of workflows that your station has when you create the [station](dda-set-up-station.md "dda-set-up-station.md").

To change the number of workflows, edit the station in the Defect Detection App.

###### Important

You are charged a monthly subscription fee for each active workflow.

###### Topics

- [Configuring a workflow](dda-configure-workflow.md "dda-configure-workflow.md")
- [Running a workflow manually](dda-run-workflow.md "dda-run-workflow.md")
- [Viewing digital input signal results](dda-run-workflow-view-results.md "dda-run-workflow-view-results.md")
- [Getting all workflow results](dda-run-workflow-results.md "dda-run-workflow-results.md")
