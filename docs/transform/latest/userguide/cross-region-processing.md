# Cross-region processing in AWS Transform

The following sections describe how cross-region inference and cross-region calls are
used to provide the AWS Transform service.

## Cross-region inference

AWS Transform is powered by Amazon Bedrock, and uses cross-region inference to
distribute traffic across different AWS Regions to enhance large language model (LLM)
inference performance and reliability. With cross-region inference, you get:

- Increased throughput and resilience during high demand periods
- Improved performance
- Access to newly launched AWS Transform capabilities and features that rely on
  the most powerful LLMs hosted on Amazon Bedrock

Cross-region inference requests are kept within the AWS Regions that are part of the
geography where the data originally resides. For example, a request made from a
AWS Transform configuration in the US is kept within the AWS Regions in the US. Although
cross-region inferencing doesn’t change where your data is stored, your requests and
output results may move outside of the Region where the data originally resides. All
data will be encrypted while transmitted across Amazon's secure network. There's no
additional cost for using cross-region inference.

Cross region inference doesn’t affect where your data is stored. For information on
where data is stored when you use AWS Transform, see
[Data protection in AWS Transform](data-protection.md "data-protection.md").

### Supported regions for AWS Transform cross-region inference

The following table describes what Regions your requests may be routed to
depending on the geography where the request originated.

| **Source Region**                        | **Destination Regions**                                                                                                            |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| US East (N. Virginia) (us-east-1)        | US East (N. Virginia) (us-east-1)<br>US East (Ohio) (us-east-2)<br>US West (Oregon) (us-west-2)                                    |
| Europe (Frankfurt) Region (eu-central-1) | Europe (Frankfurt) (eu-central-1)<br>Europe (Stockholm) (eu-north-1)<br>Europe (Ireland) (eu-west-1)<br>Europe (Paris) (eu-west-3) |

For a complete list of Regions where you can use AWS Transform, see
[Supported Regions for AWS Transform](regions.md "regions.md").
