# Cross-region inference in AWS Database Migration Service

Certain AWS Database Migration Service features use cross-region AI inference to automatically select the optimal AWS Region within your
geography to process inference requests, maximizing available compute resources and model availability, and providing the
best customer experience. With cross-region inference, you get:

- Access to the most advanced AI capabilities and features
- Increased throughput and resilience during high demand periods

Cross-region AI inference requests are kept within the AWS Regions that are part of the same geography as your primary
AWS Region. For example, a request made from a primary AWS Region in the US is kept within the AWS Regions in the US.
Your data remains stored only in your primary AWS Region. All data is transmitted encrypted across Amazon's secure network.

###### Note

Amazon CloudWatch and AWS CloudTrail logs don't specify the AWS Region in which AI inference occurs.

## Cross-region inference in DMS Schema Conversion

When you use Generative AI features in DMS Schema Conversion, anonymized code fragments and related schema metadata might be sent to
other AWS Regions within the same geography for AI processing. Your production data remains in your primary AWS Region
and is never accessed or transmitted.

###### Important

Cross-region inference is always enabled when you use Generative AI features in DMS Schema Conversion. To keep schema conversion
processing resident in your primary AWS Region, use schema conversion with disabled Generative AI features.

Generative AI features in DMS Schema Conversion are currently available in a limited number of regions. The following table describes
what AWS Regions your requests may be routed to depending on your primary AWS Region.

| Primary AWS Region                | Inference AWS Regions                                                                                                                                                                            |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| US East (N. Virginia) (us-east-1) | US East (N. Virginia) (us-east-1)<br>US East (Ohio) (us-east-2)<br>US West (Oregon) (us-west-2)                                                                                                  |
| US West (Oregon) (us-west-2)      | US East (N. Virginia) (us-east-1)<br>US East (Ohio) (us-east-2)<br>US West (Oregon) (us-west-2)                                                                                                  |
| Europe (Frankfurt) (eu-central-1) | Europe (Frankfurt) (eu-central-1)<br>Europe (Stockholm) (eu-north-1)<br>Europe (Milan) (eu-south-1)<br>Europe (Spain) (eu-south-2)<br>Europe (Ireland) (eu-west-1)<br>Europe (Paris) (eu-west-3) |
