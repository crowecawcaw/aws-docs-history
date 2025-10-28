Defect Detection App is in preview release and is subject to change.

# FeatureConfiguration

Specifies a feature configuration that's used in a workflow. Currently only Amazon
Lookout for Vision models are supported. To get a list of feature
configurations, call [GET
/feature-configurations](api-get-feature-configurations.md "api-get-feature-configurations.md").

Defect Detection App creates and manages feature configurations. You can't use the
API to create or manage feature configurations.

## modelName

The name of the Amazon Lookout for Vision model.

Type: String

Required: Yes, if the value of `type` is `LFVModel`.

## type

The type of the feature configuration.

Type: String

Pattern: `LFVModel`
