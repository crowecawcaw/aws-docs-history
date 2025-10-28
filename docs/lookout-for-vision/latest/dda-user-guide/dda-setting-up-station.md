Defect Detection App is in preview release and is subject to change.

# Setting up a station

A station is where you use a workflow to analyze images captured from your production
line and process the results. A station does the following:

- Hosts a machine learning [model](dda-components.md#dda-component-model "dda-components.md#dda-component-model") that you
  train and deploy to the station. A workflow uses the model to analyze images.
- Provides an [Station App](dda-components.md#dda-component-ddainf "dda-components.md#dda-component-ddainf") that you use to manage and run
  workflows.
  A station is hosted on an [edge
  device](dda-components.md#dda-component-edge-device "dda-components.md#dda-component-edge-device") and is designed for environments that don't have an internet
  connection. You don't need an internet connection to analyze images with your model,
  or to use the Station App.

You do need an internet connection for the following:

- Create a station on an
  edge device
- Create and deploy a model to a station
- Manage the number of workflows on a station.

###### Important

Before you can use Defect Detection App, you need a Defect Detection App tenant account.
To create a tenant account, contact your provider.

###### Topics

- [Setting up an edge device](dda-set-up-device-station.md "dda-set-up-device-station.md")
- [Signing into the Defect Detection App Console](dda-signin-dda-web-app.md "dda-signin-dda-web-app.md")
- [Creating the station for your edge device](dda-set-up-station.md "dda-set-up-station.md")
- [Adding an image source](dda-configure-image-source.md "dda-configure-image-source.md")
- [Configuring the camera](dda-set-up-camera-position.md "dda-set-up-camera-position.md")
