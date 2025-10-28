Defect Detection App is in preview release and is subject to change.

# Workflow

Specifies a Defect Detection App workflow.

Workflows define the steps taken to analyze an image and process the analysis
results. The steps are:

- Getting an image from an image source. An image source can be a camera
  on the same network as the edge device or an image folder on the edge
  device.
- Analyzing the image for anomalies with a [model](dda-components.md#dda-component-model "dda-components.md#dda-component-model") that you create. You can manually analyze an image
  or use a digital signal to trigger the automatic analysis of an image.
- Performing an output task based on the analysis results. For example,
  you can trigger an output device if the model predicts an anomaly within
  an image.
  You specify the number of workflows you need for a station when you [create the station](dda-set-up-station.md "dda-set-up-station.md"). You can update a
  workflow with the [PATCH /workflows/{workflowId}](api-patch-workflow.md "api-patch-workflow.md") operation. You can't create or delete a
  workflow with the API. To manage the number of workflows, edit the station in the
  Defect Detection App.

To manually run a workflow, use the [POST /workflows/{workflowId}/run](api-post-workflow-run.md "api-post-workflow-run.md") operation. You can also specify a
digital input and workflow trigger with the `inputConfigurations`
field. The digital input becomes active as soon as you update the workflow. To
deactivate a digital input, update the workflow by removing the input
configuration. Note that if you create a digital input for a workflow with the
`inputConfiguration` field, you can still manually run the
workflow.

A workflow automatically saves analysis results to a folder on the edge
device. To get the location, call [GET /workflows/{workflowId}](api-get-workflow.md "api-get-workflow.md") and check the
`workflowOutputPath` field. If you want your workflow to
also send one or more digital signals,
specify the `outputConfigurations` field.

###### Important

You are charged a monthly subscription for each workflow that you create.

## creationTime

The unix timestamp for the creation of the workflow. Defect Detection App creates this value.

Type: Timestamp

## description

The description for the workflow.

Type: String

## featureConfigurations

A list of feature configurations for the workflow. Currently the only
feature configuration that Defect Detection App supports is an Amazon Lookout for Vision model.

Type: [[FeatureConfiguration](api-dt-FeatureConfiguration.md "api-dt-FeatureConfiguration.md")]

## inputConfigurations

A list of input configurations for the workflow. Currently, Defect Detection App
supports one input configuration which you you use to create a trigger from
a digital input. Only specify `inputConfigurations` if you
workflow needs to accept a digital signal.

Type: [[InputConfiguration](api-dt-InputConfiguration.md "api-dt-InputConfiguration.md")]

Required: No

## imageSources

A list of image sources for the workflow. Currently, Defect Detection App supports
only one image source.

Type: [[ImageSource](api-dt-ImageSource.md "api-dt-ImageSource.md")]

## lastUpdateTime

The Unix timestamp for the last update of the workflow. Defect Detection App creates this value.

Type: Timestamp

Required: No

## name

The name for the workflow.

Type: String

## outputConfigurations

A list of output configurations for where the workflow sends a digital
signal based on the model's prediction for an analyzed image. Only specify
`outputConfigurations` if you workflow needs to send a
digital signal.

Type: [[OutputConfiguration](api-dt-OutputConfiguration.md "api-dt-OutputConfiguration.md")]

Required: No

## workflowId

The a unique ID for the workflow. Defect Detection App assigns an ID to each workflow
you create the station. You can't change the ID for a workflow.

Type: String

## workflowOutputPath

The folder location where the workflow stores its output. Defect Detection App
assigns the folder location when you create the station. You can't change
the folder location.

Type: String
