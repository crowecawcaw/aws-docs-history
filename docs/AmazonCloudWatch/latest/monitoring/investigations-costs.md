# Costs associated with CloudWatch investigations

CloudWatch investigations might incur AWS service usage including telemetry and resource queries and
other API usage. While the majority of these will not be charged to your AWS bill,
there are exceptions including, but not limited to:

- CloudWatch APIs (`ListMetrics`, `GetDashboard`,
  `ListDashboards`, and `GetInsightRuleReport`)
- X-Ray APIs (`GetServiceGraph`, `GetTraceSummaries`, and
  `BatchGetTraces`)
- CloudWatch investigations also uses AWS Cloud Control APIs which might incur usage of AWS
  services such as Amazon Kinesis Data Streams and AWS Lambda.
- Additionally, if you choose to integrate CloudWatch investigations in chat applications you might
  incur usage of Amazon Simple Notification Service.
  For usage of these services exceeding the AWS Free Tier, you will see charges on
  your AWS bill. These charges are expected to be minimal for normal usage of CloudWatch investigations. For
  more information, see [Amazon Kinesis Data Streams pricing](https://aws.amazon.com/kinesis/data-streams/pricing/ "https://aws.amazon.com/kinesis/data-streams/pricing/"), [AWS Lambda
  pricing for Automation](https://aws.amazon.com/lambda/pricing/ "https://aws.amazon.com/lambda/pricing/"), and [Amazon Simple Notification Service pricing](https://aws.amazon.com/sns/pricing/ "https://aws.amazon.com/sns/pricing/").
