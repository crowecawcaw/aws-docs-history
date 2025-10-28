Defect Detection App is in preview release and is subject to change.

# GET

/feature-configurations

Gets a list of feature configurations. Currently, the only supported feature
configuration is an Amazon Lookout for Vision model. For more information, see [FeatureConfiguration](api-dt-FeatureConfiguration.md "api-dt-FeatureConfiguration.md").

## Endpoint

```
GET /feature-configurations
```

## Request

parameters

None

## Response

A list of [FeatureConfiguration](api-dt-FeatureConfiguration.md "api-dt-FeatureConfiguration.md") objects. Each object is a
single feature configuration.

Format: JSON
