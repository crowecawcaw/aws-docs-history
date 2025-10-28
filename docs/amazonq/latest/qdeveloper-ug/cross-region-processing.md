# Cross-region processing in Amazon Q Developer

The following sections describe how cross-region inference and cross-region calls are
used to provide the Amazon Q Developer service.

## Cross-region inference

Amazon Q Developer is powered by Amazon Bedrock, and uses cross-region inference to
distribute traffic across different AWS Regions to enhance large language model (LLM)
inference performance and reliability. With cross-region inference, you get:

- Increased throughput and resilience during high demand periods
- Improved performance
- Access to newly launched Amazon Q Developer capabilities and features that rely on
  the most powerful LLMs hosted on Amazon Bedrock

Cross-region inference requests are kept within the AWS Regions that are part of the
geography where the data originally resides. For example, a request made from a
Amazon Q Developer profile created in the US is kept within the AWS Regions in the US. Some
Amazon Q Developer features and integrations may perform inference in Regions other than
where your Q Developer profile was created. For more information, see
[Supported regions for Amazon Q Developer cross-region inference](#inference-regions "#inference-regions").

Although cross-region inferencing doesn’t change where your data is stored, your
requests and output results may move outside of the Region where the data originally
resides. All data is encrypted while transmitted across Amazon's secure network.
There's no additional cost for using cross-region inference.

Cross region inference doesn’t affect where your data is stored. For information on
where data is stored when you use Amazon Q Developer, see
[Data protection in Amazon Q Developer](data-protection.md "data-protection.md").

### Supported regions for Amazon Q Developer cross-region inference

The following table describes what Regions your requests may be routed to
depending on the geography where the request originated.

| **Supported Amazon Q Developer geography** | **Inference regions**                                                                                                                                                                           |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| United States                              | US East (N. Virginia) (us-east-1) US West (Oregon) (us-west-2) US East (Ohio) (us-east-2)                                                                                                       |
| Europe                                     | Europe (Frankfurt) (eu-central-1) Europe (Ireland) (eu-west-1) Europe (Paris) (eu-west-3) Europe (Stockholm) (eu-north-1)                                                                       |
| Asia Pacific\*                             | Asia Pacific (Mumbai) (ap-south-1) Asia Pacific (Seoul) (ap-northeast-2) Asia Pacific (Singapore) (ap-southeast-1) Asia Pacific (Sydney) (ap-southeast-2) Asia Pacific (Tokyo) (ap-northeast-1) | \*Cross-region inferencing in the Asia Pacific Regions is only supported when you use Amazon Q generative SQL in the Asia Pacific (Seoul) Region. For a complete list of Regions where you can use Amazon Q Developer, see [Supported Regions for Amazon Q Developer](regions.md "regions.md"). ## Cross-region calls Certain requests that you make to Amazon Q Developer may require cross-region calls. Cross-region calls are API calls made by Amazon Q from one AWS Region to another AWS Region. Amazon Q makes cross-region calls when your request requires it to retrieve information from a Region different from your current Region. For example, when you ask Amazon Q questions about your AWS resources that are located in different Regions, it will make a cross-region call to access your resources and retrieve the relevant data to respond to your question. In addition, if a response from Amazon Q requires information from a global AWS service endpoint, Amazon Q may make calls outside of the Region where your data is stored. For more information on global services, see [Global services](../../../whitepapers/latest/aws-fault-isolation-boundaries/global-services.md "../../../whitepapers/latest/aws-fault-isolation-boundaries/global-services.md") in the _AWS Fault Isolation Boundaries AWS Whitepaper_. If you’d like to disable cross-region calls made by Amazon Q Developer, you can create a policy that prevents Amazon Q from making API calls on your behalf. By doing so, you won’t have access to features that require Amazon Q to make API calls on your behalf, even if Amazon Q is making calls within your current Region. For an IAM policy that prevents Amazon Q from making API calls on your behalf, including cross-region calls, see [Deny Amazon Q permission to perform actions on your behalf](id-based-policy-examples-users.md#id-based-policy-examples-deny-actions "id-based-policy-examples-users.md#id-based-policy-examples-deny-actions"). |
