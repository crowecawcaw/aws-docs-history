# Cross-region inference in Amazon Quick Suite integrations

With cross-region inference, Amazon Quick Suite automatically selects the optimal region within your geography to process your inference requests, maximizing available compute resources and model availability, and providing the best customer experience. With cross-region inference, you get:

- Complete access to the most advanced Amazon Quick Suite AI capabilities and features
- Access to a variety of models suitable for different tasks
- Improved performance for all your applications and integrations
  Cross-region inference requests are kept within the AWS Regions that are part of the geography where the data originally resides. For example, a request made within the US is kept within the AWS Regions in the US. Although the data remains stored only in the primary region, when using cross-region inference, your input prompts and output results may move outside of your primary region. All data will be transmitted encrypted across Amazon's secure network.

###### Note

There's no additional cost for using cross-region inference.

Amazon CloudWatch and AWS CloudTrail logs won't specify the AWS Region in which data inference occurs.

## Supported regions for Amazon Quick Suite cross-region inference

| Supported Amazon Quick Suite Cross-Region Inference Regions | Supported Amazon Quick Suite geography                                                                                                                                                                                                                                                                                                         | Inference regions |
| ----------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| United States                                               | US East (N. Virginia) (us-east-1)<br>US East (Ohio) (us-east-2)<br>US West (Oregon) (us-west-2)                                                                                                                                                                                                                                                |
| Europe                                                      | Europe (Frankfurt) (eu-central-1)<br>Europe (Stockholm) (eu-north-1)<br>Europe (Milan) (eu-south-1)<br>Europe (Spain) (eu-south-2)<br>Europe (Ireland) (eu-west-1)<br>Europe (Paris) (eu-west-3)                                                                                                                                               |
| Australia                                                   | Asia Pacific (Tokyo) (ap-northeast-1)<br>Asia Pacific (Seoul) (ap-northeast-2)<br>Asia Pacific (Osaka) (ap-northeast-3)<br>Asia Pacific (Mumbai) (ap-south-1)<br>Asia Pacific (Singapore) (ap-southeast-1)<br>Asia Pacific (Singapore) (ap-southeast-1)<br>Asia Pacific (Sydney) (ap-southeast-2)<br>Asia Pacific (Melbourne) (ap-southeast-2) |
