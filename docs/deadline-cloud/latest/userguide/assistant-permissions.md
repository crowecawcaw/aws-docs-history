# Required permissions

Monitor users need the `bedrock:InvokeModelWithResponseStream` permission
to use the assistant. When an administrator enables the assistant, Deadline Cloud
automatically attaches the required Amazon Bedrock IAM policy to the
monitor user role.

For information about Deadline Cloud IAM permissions, see [Identity-based
policy examples for Deadline Cloud](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Amazon Bedrock IAM policy

When an administrator enables the assistant, the following IAM policy is attached
to the monitor user role. The policy grants permission to invoke Amazon Bedrock models through
cross-region inference profiles scoped to your monitor's geographic Region.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "GrantCrisInferenceProfileAccess",
            "Effect": "Allow",
            "Action": "bedrock:InvokeModelWithResponseStream",
            "Resource": "arn:aws:bedrock:`Region`:`AccountId`:inference-profile/`InferenceProfilePrefix`.*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestedRegion": `RequestedRegions`
                }
            }
        },
        {
            "Sid": "GrantCrisModelAccess",
            "Effect": "Allow",
            "Action": "bedrock:InvokeModelWithResponseStream",
            "Resource": "arn:aws:bedrock:*::foundation-model/*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestedRegion": `RequestedRegions`
                },
                "ArnLike": {
                    "bedrock:InferenceProfileArn": "arn:aws:bedrock:`Region`:`AccountId`:inference-profile/`InferenceProfilePrefix`.*"
                }
            }
        }
    ]
}
```

The policy only grants `bedrock:InvokeModelWithResponseStream` – no
other Amazon Bedrock actions are permitted.

## Cross-region inference

The assistant uses Amazon Bedrock [cross-region inference](../../../bedrock/latest/userguide/cross-region-inference.md "../../../bedrock/latest/userguide/cross-region-inference.md")
to optimize model availability and throughput. When you invoke the assistant, Amazon Bedrock might
route your request to a different AWS Region within the same geographic area to process
the inference request.

- Requests are routed to AWS Regions within a geographic boundary determined by
  your monitor's Region.
- All data transmitted between Regions remains on the AWS network and does not
  traverse the public internet.
- Data is encrypted in transit between AWS Regions.
- There is no additional routing cost for cross-region inference. Pricing is based
  on the Region from which you call the inference profile.
- Cross-region inference requests are logged in CloudTrail in your source
  Region. The `additionalEventData.inferenceRegion` field identifies where
  the request was processed.

The following table shows which geographic inference profile and destination Regions
are used based on your monitor's Region:

Cross-region inference profile mapping| Monitor Region | Inference profile prefix | Destination Regions |
| --- | --- | --- |
| us-east-1 | `us` | us-east-1, us-east-2, us-west-2 |
| us-east-2 | `us` | us-east-1, us-east-2, us-west-2 |
| us-west-2 | `us` | us-east-1, us-east-2, us-west-2 |
| eu-central-1 | `eu` | eu-central-1, eu-north-1, eu-south-1, eu-south-2, eu-west-1, eu-west-3 |
| eu-west-1 | `eu` | eu-central-1, eu-north-1, eu-south-1, eu-south-2, eu-west-1, eu-west-3 |
| eu-west-2 | `eu` | eu-central-1, eu-north-1, eu-south-1, eu-south-2, eu-west-1, eu-west-2,<br>eu-west-3 |
| ap-northeast-1 | `jp` | ap-northeast-1, ap-northeast-3 |
| ap-southeast-2 | `au` | ap-southeast-2, ap-southeast-4 |
| ap-northeast-2 | `global` | ap-northeast-2 |
| ap-southeast-1 | `global` | ap-southeast-1 |

For Regions using the `global` inference profile prefix, Amazon Bedrock might route
requests to any supported commercial AWS Region worldwide.
