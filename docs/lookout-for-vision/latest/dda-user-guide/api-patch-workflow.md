Defect Detection App is in preview release and is subject to change.

# PATCH /workflows/{workflowId}

Updates an individual workflow. For more information, see [Workflow](api-dt-Workflow.md "api-dt-Workflow.md").

## Endpoint

```
PATCH /workflows/{workflowId}
```

`workflowId` is the identifier for the workflow that you want
to update.

## Request parameters

Information about the workflow that you want to update.

Type: JSON

Required: Yes

### description

The description for the workflow.

Type: String

Required: No

### featureConfigurations

A list of feauture configurations for the workflow. Currently the only
feature configuration that Defect Detection App supports is an Amazon Lookout for Vision
model.

Type: [[FeatureConfiguration](api-dt-FeatureConfiguration.md "api-dt-FeatureConfiguration.md")]

Required: Yes

### inputConfigurations

A list of input configurations for the workflow. Currently, Defect Detection App
supports one input configuration.

Type: [[InputConfiguration](api-dt-InputConfiguration.md "api-dt-InputConfiguration.md")]

Required: No

### imageSources

A list of image sources for the workflow. Currently, Defect Detection App
supports only one image source.

Type: [[ImageSource](api-dt-ImageSource.md "api-dt-ImageSource.md")]

Required: Yes

### name

The name for the workflow.

Type: String

Required: Yes

### outputConfigurations

A list of output configurations for where the workflow stores the
inference results for images analyzed by the model.

Type: [[OutputConfiguration](api-dt-OutputConfiguration.md "api-dt-OutputConfiguration.md")]

Required: No

## Response

The ID for the updated workflow.

Format: JSON
