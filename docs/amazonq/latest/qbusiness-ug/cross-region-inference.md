# Cross-region inference in Amazon Q Business

With cross-region inference, Amazon Q Business will automatically select the optimal
region within your geography (as described in more detail below) to process your inference
request, maximizing available compute resources and model availability, and providing the best
customer experience. With cross-region inference, you get:

- Complete access to most advanced Amazon Q Business AI capabilities and
  features
- Access to a variety of models suitable for different tasks
- Improved performance for all your applications
  Cross-region inference requests are kept within the AWS Regions that are part of the
  geography where the data originally resides. For example, a request made within the US is kept
  within the AWS Regions in the US. Although the data remains stored only in the primary
  region, when using cross-region inference, your input prompts and output results may move
  outside of your primary region. All data will be transmitted encrypted across Amazon's secure
  network.

###### Important

Cross-region inference is enabled by default for Amazon Q Business applications.
For customers with highly regulated workloads that need to keep data processing resident
in-country, contact [AWS
Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

###### Note

There's no additional cost for using cross-region inference.

Amazon CloudWatch and AWS CloudTrail logs won't specify the AWS Region in which data inference
occurs.

## Supported regions for Amazon Q Business cross-region inference

For a list of Region codes and endpoints supported in Amazon Q Business, see
[Amazon Q Business endpoints and quotas](quotas-regions.md#regions "quotas-regions.md#regions").

| Supported Amazon Q Business geography | Inference regions                                                                                                                                                                                                                     |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| United States                         | US East (N. Virginia) (us-east-1) US West (Oregon) (us-west-2)                                                                                                                                                                        |
| Europe                                | Europe (Frankfurt) (eu-central-1) Europe (Ireland) (eu-west-1) Europe (Paris) (eu-west-3)                                                                                                                                             |
| Australia                             | Asia Pacific (Tokyo) (ap-northeast-1) Asia Pacific (Seoul) (ap-northeast-2) Asia Pacific (Osaka) (ap-northeast-3) Asia Pacific (Mumbai) (ap-south-1) Asia Pacific (Singapore) (ap-southeast-1) Asia Pacific (Sydney) (ap-southeast-2) |
