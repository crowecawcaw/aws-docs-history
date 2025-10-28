Defect Detection App is in preview release and is subject to change.

# Understanding Defect Detection App

A Defect Detection App solution uses an edge device to perform offline analysis and processing of
images from a production line, with an Amazon Lookout for Vision model. You use the Defect Detection App Console to train and
deploy a model to a station hosted on the edge device. You then use an application ([Defect Detection Station App](dda-components.md#dda-component-ddainf "dda-components.md#dda-component-ddainf")) at the station
to manage and run [workflows](dda-components.md#dda-component-workflow "dda-components.md#dda-component-workflow"). A
workflow defines the steps taken to analyze an image and process the analysis results.
With a workflow, you can analyze images from cameras on the station, or with images
retrieved from a folder on the edge device. You can automate image analysis by using a
digital signal input trigger to run a workflow, or run the workflow manually from the
Station App. The analysis results are saved to a local folder on the edge device.
Optionally, you can send digital signals based on the results of the prediction that the
model makes.

###### Important

Before you can use Defect Detection App, you need your tenant sign in details. For more information,
see [Signing into the Defect Detection App Console](dda-signin-dda-web-app.md "dda-signin-dda-web-app.md").

###### Topics

- [Set up the edge device](#dda-understanding-edge-device-setup "#dda-understanding-edge-device-setup")
- [Train and deploy an Amazon Lookout for Vision model](#dda-understanding-model "#dda-understanding-model")
- [Running a workflow](#dda-understanding-workflow "#dda-understanding-workflow")

## Set up the edge device

An edge device that you use with Defect Detection App is an Industrial PC (IPC) that hosts a Defect Detection App [station](dda-components.md#dda-component-station "dda-components.md#dda-component-station"). The edge device is located where
you need to analyze images, such as a production line where you want to find
manufacturing flaws on completed circuit boards. The edge device has one or more
attached cameras that provide images for analysis with the model.

You create a station by using the Defect Detection App Console. When you create a
station, you specify the number of [workflows](dda-components.md#dda-component-workflow "dda-components.md#dda-component-workflow") that you want your station to have.

###### Important

You are charged a monthly subscription for each active workflow.

As part of station creation, you deploy the station software to your edge device.
Once completed, you can use the Defect Detection App Console to deploy models to the station. You
also need to set up the image source on the station. An image source is the
location where a workflow gets images from. An image source can be a [camera](dda-components.md#dda-component-camera "dda-components.md#dda-component-camera") on the edge device, or a folder on
the edge device. You set up the image source using the
[Defect Detection Station App](dda-components.md#dda-component-ddainf "dda-components.md#dda-component-ddainf"). If the image source is a
camera, you also use the Station App to configure the camera settings, such as the
exposure time for image capture.

**More information:** [Setting up a station](dda-setting-up-station.md "dda-setting-up-station.md")

## Train and deploy an Amazon Lookout for Vision model

An Amazon Lookout for Vision [model](dda-components.md#dda-component-model "dda-components.md#dda-component-model") is a machine learning model that can find anomalies in
images. You can train an Amazon Lookout for Vision model to classify images as normal or anomalous. You can also train a model
to find the location of anomalies on an image (segmentation).

You use the Defect Detection App Console to train and manage the Amazon Lookout for Vision models that you deploy an
edge device.

You train the model with a [dataset](dda-components.md#dda-component-dataset "dda-components.md#dda-component-dataset")
of images that you supply and label. You can capture images for your dataset by using the Station App.

After you train a model, you can deploy the model to a station on the desired edge
device.

**More information:**
[Training and deploying a model](dda-train-deploy-model.md "dda-train-deploy-model.md")

## Running a workflow

You use a [workflow](dda-components.md#dda-component-workflow "dda-components.md#dda-component-workflow") to analyze an image and process the analysis results. The workflow steps are:

- Getting an image from an [image
  source](dda-components.md#dda-component-image-source "dda-components.md#dda-component-image-source"). An image source can be a camera on the same network as
  the edge device or an image folder on the edge device.
- Analyzing the image for anomalies with a [model](dda-components.md#dda-component-model "dda-components.md#dda-component-model") that you create. You can
  manually analyze an image or use a digital signal to trigger the running of
  a workflow. If the image source is a camera, the workflow captures an image
  and then analyzes the image. If the image source is a folder, the workflow
  analyzes the oldest image in the folder that it hasn't yet analyzed.
- Performing output tasks based on the analysis results. For example, you
  can trigger an output device if the model predicts an anomaly within an
  image.

You specify the number of workflows you need for a station when you create or edit
a station. You use the Station App on the station to configure the workflow settings,
such as setting the image source or setting a digital signal that triggers the
running of a workflow.

When a workflow runs, Station App stores the results on the edge device for later
use. You can use the Station App or API to view the results for the last analyzed
image.

**More information:**
[Analyzing images with the Defect Detection Station App](dda-inference.md "dda-inference.md")
