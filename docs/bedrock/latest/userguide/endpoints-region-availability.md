# Regional availability by endpoints

The following tables show which AWS Regions support each Amazon Bedrock inference endpoint, organized by geography. The `bedrock-runtime` endpoint is available in every AWS Region where Amazon Bedrock is offered. The `bedrock-mantle` endpoint is available in a subset of those Regions. To choose between endpoints, see [Endpoints supported by Amazon Bedrock](endpoints.md "endpoints.md"); for model-level Regional availability, see [Regional availability by models](models-region-compatibility.md "models-region-compatibility.md").

## United States

| **Region**                  | **`bedrock-runtime`** | **`bedrock-mantle`** |
| --------------------------- | --------------------- | -------------------- |
| `us-east-1` (N. Virginia)   | supported             | supported            |
| `us-east-2` (Ohio)          | supported             | supported            |
| `us-west-1` (N. California) | supported             | not-supported        |
| `us-west-2` (Oregon)        | supported             | supported            |

## Canada

| **Region**              | **`bedrock-runtime`** | **`bedrock-mantle`** |
| ----------------------- | --------------------- | -------------------- |
| `ca-central-1` (Canada) | supported             | not-supported        |
| `ca-west-1` (Calgary)   | supported             | not-supported        |

## Europe

| **Region**                 | **`bedrock-runtime`** | **`bedrock-mantle`** |
| -------------------------- | --------------------- | -------------------- |
| `eu-central-1` (Frankfurt) | supported             | supported            |
| `eu-central-2` (Zurich)    | supported             | not-supported        |
| `eu-north-1` (Stockholm)   | supported             | supported            |
| `eu-south-1` (Milan)       | supported             | supported            |
| `eu-south-2` (Spain)       | supported             | not-supported        |
| `eu-west-1` (Ireland)      | supported             | supported            |
| `eu-west-2` (London)       | supported             | supported            |
| `eu-west-3` (Paris)        | supported             | not-supported        |

## Asia Pacific

| **Region**                     | **`bedrock-runtime`** | **`bedrock-mantle`** |
| ------------------------------ | --------------------- | -------------------- |
| `ap-east-2` (Taipei)           | supported             | not-supported        |
| `ap-northeast-1` (Tokyo)       | supported             | supported            |
| `ap-northeast-2` (Seoul)       | supported             | not-supported        |
| `ap-northeast-3` (Osaka)       | supported             | not-supported        |
| `ap-south-1` (Mumbai)          | supported             | supported            |
| `ap-south-2` (Hyderabad)       | supported             | not-supported        |
| `ap-southeast-1` (Singapore)   | supported             | not-supported        |
| `ap-southeast-2` (Sydney)      | supported             | supported            |
| `ap-southeast-3` (Jakarta)     | supported             | supported            |
| `ap-southeast-4` (Melbourne)   | supported             | not-supported        |
| `ap-southeast-5` (Malaysia)    | supported             | not-supported        |
| `ap-southeast-6` (New Zealand) | supported             | not-supported        |
| `ap-southeast-7` (Thailand)    | supported             | not-supported        |

## Middle East

| **Region**                | **`bedrock-runtime`** | **`bedrock-mantle`** |
| ------------------------- | --------------------- | -------------------- |
| `il-central-1` (Tel Aviv) | supported             | not-supported        |
| `me-central-1` (UAE)      | supported             | not-supported        |
| `me-south-1` (Bahrain)    | supported             | not-supported        |

## Africa

| **Region**               | **`bedrock-runtime`** | **`bedrock-mantle`** |
| ------------------------ | --------------------- | -------------------- |
| `af-south-1` (Cape Town) | supported             | not-supported        |

## South America

| **Region**              | **`bedrock-runtime`** | **`bedrock-mantle`** |
| ----------------------- | --------------------- | -------------------- |
| `sa-east-1` (São Paulo) | supported             | supported            |

## AWS GovCloud (US)

AWS GovCloud (US) Regions have separate access requirements. For details on enabling Bedrock in GovCloud, see [Access Amazon Bedrock foundation models in AWS GovCloud (US)](model-access.md#model-access-govcloud "model-access.md#model-access-govcloud").

| **Region**                         | **`bedrock-runtime`** | **`bedrock-mantle`** |
| ---------------------------------- | --------------------- | -------------------- |
| `us-gov-east-1` (GovCloud US-East) | supported             | not-supported        |
| `us-gov-west-1` (GovCloud US-West) | supported             | supported            |
