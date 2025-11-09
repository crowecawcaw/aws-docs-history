# Using AWS CloudFormation to Set Up Neptune-to-Neptune

Replication with the Streams Consumer Application

You can use an AWS CloudFormation template to set up the Neptune streams consumer application to
support Neptune-to-Neptune replication.

###### Topics

- [Choose an AWS CloudFormation template for Your
  Region](#streams-consumer-cfn-by-region "#streams-consumer-cfn-by-region")
- [Add details About the Neptune streams
  consumer stack you're creating](#streams-consumer-cfn-stack-details "#streams-consumer-cfn-stack-details")
- [Run the AWS CloudFormation Template](#streams-consumer-cfn-complete "#streams-consumer-cfn-complete")
- [To update the stream poller with the
  latest Lambda artifacts](#streams-consumer-cfn-update "#streams-consumer-cfn-update")

## Choose an AWS CloudFormation template for Your

Region

To launch the appropriate AWS CloudFormation stack on the AWS CloudFormation console, choose one of the
**Launch Stack** buttons in the following table, depending on the AWS
Region that you want to use.

| Region                    | View                                                                                                                                                                                                | View in Designer                                                                                                                                                                                                                                                                                                                                                                                                      | Launch                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| US East (N. Virginia)     | [View](https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json") | [View in Designer](https://console.aws.amazon.com/cloudformation/designer/home?region=us-east-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/designer/home?region=us-east-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")                     | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")                     |
| US East (Ohio)            | [View](https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json") | [View in Designer](https://console.aws.amazon.com/cloudformation/designer/home?region=us-east-2&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/designer/home?region=us-east-2&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")                     | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")                     |
| US West (N. California)   | [View](https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json") | [View in Designer](https://console.aws.amazon.com/cloudformation/designer/home?region=us-west-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/designer/home?region=us-west-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")                     | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=us-west-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/home?region=us-west-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")                     |
| US West (Oregon)          | [View](https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json") | [View in Designer](https://console.aws.amazon.com/cloudformation/designer/home?region=us-west-2&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/designer/home?region=us-west-2&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")                     | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")                     |
| Canada (Central)          | [View](https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json") | [View in Designer](https://console.aws.amazon.com/cloudformation/designer/home?region=us-west-2&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/designer/home?region=us-west-2&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")                     | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=ca-central-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/home?region=ca-central-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")               |
| South America (São Paulo) | [View](https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json") | [View in Designer](https://console.aws.amazon.com/cloudformation/designer/home?region=sa-east-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/designer/home?region=sa-east-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")                     | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=sa-east-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/home?region=sa-east-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")                     |
| Europe (Stockholm)        | [View](https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json") | [View in Designer](https://console.aws.amazon.com/cloudformation/designer/home?region=eu-north-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/designer/home?region=eu-north-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")                   | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=eu-north-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/home?region=eu-north-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")                   |
| Europe (Ireland)          | [View](https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json") | [View in Designer](https://console.aws.amazon.com/cloudformation/designer/home?region=eu-west-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/designer/home?region=eu-west-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")                     | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")                     |
| Europe (London)           | [View](https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json") | [View in Designer](https://console.aws.amazon.com/cloudformation/designer/home?region=eu-west-2&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/designer/home?region=eu-west-2&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")                     | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=eu-west-2#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/home?region=eu-west-2#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")                     |
| Europe (Paris)            | [View](https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json") | [View in Designer](https://console.aws.amazon.com/cloudformation/designer/home?region=eu-west-3&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/designer/home?region=eu-west-3&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")                     | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=eu-west-3#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/home?region=eu-west-3#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")                     |
| Europe (Frankfurt)        | [View](https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json") | [View in Designer](https://console.aws.amazon.com/cloudformation/designer/home?region=eu-central-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/designer/home?region=eu-central-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")               | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")               |
| Middle East (Bahrain)     | [View](https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json") | [View in Designer](https://console.aws.amazon.com/cloudformation/designer/home?region=me-south-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/designer/home?region=me-south-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")                   | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=me-south-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/home?region=me-south-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")                   |
| Middle East (UAE)         | [View](https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json") | [View in Designer](https://console.aws.amazon.com/cloudformation/designer/home?region=me-central-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/designer/home?region=me-central-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")               | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=me-central-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/home?region=me-central-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")               |
| Israel (Tel Aviv)         | [View](https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json") | [View in Designer](https://console.aws.amazon.com/cloudformation/designer/home?region=il-central-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/designer/home?region=il-central-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")               | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=il-central-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/home?region=il-central-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")               |
| Africa (Cape Town)        | [View](https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json") | [View in Designer](https://console.aws.amazon.com/cloudformation/designer/home?region=af-south-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/designer/home?region=af-south-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")                   | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=af-south-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/home?region=af-south-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")                   |
| Asia Pacific (Tokyo)      | [View](https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json") | [View in Designer](https://console.aws.amazon.com/cloudformation/designer/home?region=ap-northeast-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/designer/home?region=ap-northeast-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")           | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")           |
| Asia Pacific (Hong Kong)  | [View](https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json") | [View in Designer](https://console.aws.amazon.com/cloudformation/designer/home?region=ap-east-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/designer/home?region=ap-east-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")                     | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=ap-east-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/home?region=ap-east-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")                     |
| Asia Pacific (Seoul)      | [View](https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json") | [View in Designer](https://console.aws.amazon.com/cloudformation/designer/home?region=ap-northeast-2&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/designer/home?region=ap-northeast-2&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")           | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-2#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-2#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")           |
| Asia Pacific (Singapore)  | [View](https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json") | [View in Designer](https://console.aws.amazon.com/cloudformation/designer/home?region=ap-southeast-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/designer/home?region=ap-southeast-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")           | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")           |
| Asia Pacific (Sydney)     | [View](https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json") | [View in Designer](https://console.aws.amazon.com/cloudformation/designer/home?region=ap-southeast-2&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/designer/home?region=ap-southeast-2&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")           | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")           |
| Asia Pacific (Mumbai)     | [View](https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json") | [View in Designer](https://console.aws.amazon.com/cloudformation/designer/home?region=ap-south-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/designer/home?region=ap-south-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")                   | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.aws.amazon.com/cloudformation/home?region=ap-south-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.aws.amazon.com/cloudformation/home?region=ap-south-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")                   |
| China (Beijing)           | [View](https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json") | [View in Designer](https://console.amazonaws.cn/cloudformation/designer/home?region=cn-north-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.amazonaws.cn/cloudformation/designer/home?region=cn-north-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")                       | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.amazonaws.cn/cloudformation/home?region=cn-north-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.amazonaws.cn/cloudformation/home?region=cn-north-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")                       |
| China (Ningxia)           | [View](https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json") | [View in Designer](https://console.amazonaws.cn/cloudformation/designer/home?region=cn-northwest-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.amazonaws.cn/cloudformation/designer/home?region=cn-northwest-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")               | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.amazonaws.cn/cloudformation/home?region=cn-northwest-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.amazonaws.cn/cloudformation/home?region=cn-northwest-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json")               |
| AWS GovCloud (US-West)    | [View](https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json") | [View in Designer](https://console.amazonaws-us-gov.com/cloudformation/designer/home?region=us-gov-west-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.amazonaws-us-gov.com/cloudformation/designer/home?region=us-gov-west-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json") | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.amazonaws-us-gov.com/cloudformation/home?region=us-gov-west-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.amazonaws-us-gov.com/cloudformation/home?region=us-gov-west-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json") |
| AWS GovCloud (US-East)    | [View](https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json") | [View in Designer](https://console.amazonaws-us-gov.com/cloudformation/designer/home?region=us-gov-east-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.amazonaws-us-gov.com/cloudformation/designer/home?region=us-gov-east-1&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json") | [Orange button labeled "Launch Stack" with an arrow icon.](https://console.amazonaws-us-gov.com/cloudformation/home?region=us-gov-east-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json "https://console.amazonaws-us-gov.com/cloudformation/home?region=us-gov-east-1#/stacks/new?stackName=NeptuneStreamPoller&templateURL=https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json") |

On the **Create Stack** page, choose **Next**.

## Add details About the Neptune streams

consumer stack you're creating

The **Specify Stack Details** page provides properties and parameters
that you can use to control the setup of the application:

**Stack Name**   –  
The name of the new AWS CloudFormation stack that you're creating. You can generally use
the default value, `NeptuneStreamPoller`.

Under **Parameters**, provide the following:

###### Network configuration for the VPC Where the streams consumer runs

- **`VPC`**   –  
  Provide the name of the VPC where the polling Lambda function will run.
- **`SubnetIDs`**   –  
  The subnets to which a network interface is established. Add subnets corresponding
  to your Neptune cluster.
- **`SecurityGroupIds`**   –  
  Provide the IDs of security groups that grant write inbound access
  to your source Neptune DB cluster.
- **`RouteTableIds`**   –  
  This is needed to create an Amazon DynamoDB endpoint in your Neptune VPC,
  if you do not already have one. You must provide a comma-separated
  list of route table IDs associated with the subnets.
- **`CreateDDBVPCEndPoint`**   –  
  A Boolean value that defaults to `true`, indicating whether or not it is
  necessary to create a Dynamo DB VPC endpoint. You only need to change it to `false`
  if you have already created a DynamoDB endpoint in your VPC.
- **`CreateMonitoringEndPoint`**   –  
  A Boolean value that defaults to `true`, indicating whether or not it is
  necessary to create a monitoring VPC endpoint.. You only need to change it to `false`
  if you have already created a monitoring endpoint in your VPC.

###### Stream Poller

- **`ApplicationName`**   –  
  You can generally leave this set to the default (`NeptuneStream`).
  If you use a different name, it must be unique.
- **`LambdaMemorySize`**   –  
  Used to set the memory size available to the Lambda poller function.
  The default value is 2,048 megabytes.
- **`LambdaRuntime`**   –  
  The language used in the Lambda function that retrieves items from the Neptune
  stream. You can set this either to `python3.9` or to `java8`.
- **`LambdaS3Bucket`**   –  
  The Amazon S3 bucket that contains Lambda code artifacts. Leave this blank unless you are using a
  custom Lambda polling function that loads from a different Amazon S3 bucket.
- **`LambdaS3Key`**   –  
  The Amazon S3 key that corresponds to your Lambda code artifacts. Leave this blank unless you are
  using a custom Lambda polling function.
- **`LambdaLoggingLevel`**   –  
  In general, leave this set to the default value, which is `INFO`.
- **`ManagedPolicies`**   –  
  Lists the managed policies to use for execution of your Lambda function. In general, leave this
  blank unless you are using a custom Lambda polling function.
- **`StreamRecordsHandler`**   –  
  In general, leave this blank unless you are using a custom handler for the records in Neptune streams.
- **`StreamRecordsBatchSize`**   –  
  The maximum number of records to be fetched from stream. You can use this parameter to tune performance.
  The default (`5000`) is a good place to start. The maximum allowable is 10,000.
  The higher the number, the fewer network calls are needed to read records from the stream,
  but the more memory is required to process the records. Lower values of this parameter result
  in lower throughput.
- **`MaxPollingWaitTime`**   –  
  The maximum wait time between two polls (in seconds). Determines how frequently the Lambda poller is
  invoked to poll the Neptune streams. Set this value to 0 for continuous polling. The maximum value
  is 3,600 seconds (1 hour). The default value (60 seconds) is a good place to start, depending on how
  fast your graph data changes.
- **`MaxPollingInterval`**   –  
  The maximum continuous polling period (in seconds). Use this to set a timeout for the Lambda polling function.
  The value should be in the range between 5 seconds and 900 seconds. The default value (600 seconds)
  is a good place to start.
- **`StepFunctionFallbackPeriod`**   –  
  The number of units of step-function-fallback-period to wait for the poller, after which
  the step function is called through Amazon CloudWatch Events to recover from a failure. The default
  (5 minutes) is a good place to start.
- **`StepFunctionFallbackPeriodUnit`**   –  
  The time units used to measure the preceding `StepFunctionFallbackPeriodUnit` (`minutes`,
  `hours`, or `days`). The default (`minutes`) is generally sufficient.
- **`StartingCheckpoint`**   –  
  The starting checkpoint for the stream poller. The default is `0:0`, which signifies starting from the
  beginning of the Neptune stream.
- **`StreamPollerInitialState`**   –  
  The initial state of the poller. The default is `ENABLED`, which means that the stream replication will start as
  soon as the entire stack creation is complete.

###### Neptune stream

- **`NeptuneStreamEndpoint`**   –  
  (_Required_) The endpoint of the Neptune source stream. This takes one of two forms:
  - **`https://`your DB cluster`:`port`/propertygraph/stream`**
    (or its alias, `https://`your DB cluster`:`port`/pg/stream`).
  - **`https://`your DB cluster`:`port`/sparql/stream`**.

- **`Neptune Query Engine`**   –  
  Choose Gremlin, openCypher, or SPARQL.
- **`IAMAuthEnabledOnSourceStream`**   –  
  If your Neptune DB cluster is using IAM authentication, set this parameter to `true`.
- **`StreamDBClusterResourceId`**   –  
  If your Neptune DB cluster is using IAM authentication, set this parameter to the
  cluster resource ID. The resource ID is not the same as the cluster ID. Instead, it
  takes the form: `cluster-` followed by 28 alpha-numeric characters.
  It can be found under **Cluster Details** in the Neptune console.

###### Target Neptune DB cluster

- **`TargetNeptuneClusterEndpoint`**   –  
  The cluster endpoint (hostname only) of the target backup cluster.

Note that if you specify `TargetNeptuneClusterEndpoint`, you
cannot also specify `TargetSPARQLUpdateEndpoint`.

- **`TargetNeptuneClusterPort`**   –  
  The port number for the target cluster.

Note that if you specify `TargetSPARQLUpdateEndpoint`, the
setting for `TargetNeptuneClusterPort` is ignored.

- **`IAMAuthEnabledOnTargetCluster`**   –  
  Set to true if IAM authentication is to be enabled on the target cluster.
- **`TargetAWSRegion`**   –  
  The target backup cluster's AWS region, such as `us-east-1`).
  You must provide this parameter only when the AWS region of the target backup
  cluster is different from the region of the Neptune source cluster, as in
  the case of cross-region replication. If the source and target regions
  are the same, this parameter is optional.

Note that if the `TargetAWSRegion` value is not a [valid AWS region that Neptune supports](limits.md#limits-regions "limits.md#limits-regions"),
the process fails.

- **`TargetNeptuneDBClusterResourceId`**   –  
  _Optional_: this is only needed when IAM authentication is enabled on
  the target DB cluster. Set to the resource ID of the target cluster.
- **`SPARQLTripleOnlyMode`**   –  
  Boolean flag that determines whether triple-only mode is enabled. In triple-only
  mode, there is no named-graph replication. The default value is `false`.
- **`TargetSPARQLUpdateEndpoint`**   –  
  URL of the target endpoint for SPARQL update, such as `https://abc.com/xyz`.
  This endpoint can be any SPARQL store that supports quad or triples.

Note that if you specify `TargetSPARQLUpdateEndpoint`, you
cannot also specify `TargetNeptuneClusterEndpoint`, and the setting of
`TargetNeptuneClusterPort` is ignored.

- **`BlockSparqlReplicationOnBlankNode`**   –  
  Boolean flag which, if set to `true`, stops replication for BlankNode in
  SPARQL (RDF) data. The default value is `false`.

###### Alarm

- **`Required to create Cloud watch Alarm`**   –  
  Set this to `true` if you want to create a CloudWatch alarm for the new stack.
- **`SNS Topic ARN for Cloudwatch Alarm Notifications`**   –  
  The SNS topic ARN where CloudWatch alarm notifications should be sent (only needed if alarms are enabled).
- **`Email for Alarm Notifications`**   –  
  The email address to which alarm notifications should be sent (only needed if alarms are enabled).

For destination of the alarm notification, you can add SNS only, email only, or
both SNS and email.

## Run the AWS CloudFormation Template

Now you can complete the process of provisioning a Neptune streams consumer
application instance as follows:

1. In AWS CloudFormation, on the **Specify Stack Details** page, choose
   **Next**.
2. On the **Options** page, choose **Next**.
3. On the **Review** page, select the first check box to acknowledge that
   AWS CloudFormation will create IAM resources. Select the second check box to acknowledge
   `CAPABILITY_AUTO_EXPAND` for the new stack.

###### Note

`CAPABILITY_AUTO_EXPAND` explicitly acknowledges that macros will be expanded when
creating the stack, without prior review. Users often create a change set from a
processed template so that the changes made by macros can be reviewed before actually
creating the stack. For more information, see the AWS CloudFormation [CreateStack](../../../AWSCloudFormation/latest/APIReference/API_CreateStack.md "../../../AWSCloudFormation/latest/APIReference/API_CreateStack.md") API in the
_AWS CloudFormation API Reference_.

Then choose **Create**.

## To update the stream poller with the

latest Lambda artifacts

You can update the stream poller with the latest Lambda code artifacts as follows:

1. In the AWS Management Console, navigate to AWS CloudFormation and select the main parent AWS CloudFormation stack.
2. Select the **Update** option for the stack.
3. Select **Replace current template**.
4. For the template source, choose **Amazon S3 URL** and enter
   the following S3 URL:

```
https://aws-neptune-customer-samples.s3.amazonaws.com/neptune-stream/neptune_to_neptune.json
```

5. Select **Next** without changing any AWS CloudFormation parameters.
6. Choose **Update Stack**.

The stack will now update the Lambda artifacts with the most recent ones.
