# Log Amazon Bedrock AgentCore Gateway API calls with CloudTrail

Amazon Bedrock AgentCore Gateway is integrated with AWS CloudTrail, a service that provides a record of actions taken by
a user, role, or an AWS service in Gateway. CloudTrail captures all API calls for
Gateway as events, including calls from the Gateway console and code calls to the
Gateway APIs. Using the information collected by CloudTrail, you can determine the request that
was made to Gateway, who made the request, when it was made, and additional details.
There are two types of events: **Management events** and **Data events**.

For more information about using CloudTrail with Gateway, see the following resources:

- [AWS CloudTrail
  User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md")
- [Creating a Trail for Your AWS Account](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [AWS CloudTrail
  API Reference](../../../awscloudtrail/latest/APIReference.md "../../../awscloudtrail/latest/APIReference.md")
- [AWS CloudTrail CLI Reference](../../../cli/latest/reference/cloudtrail/index.md "../../../cli/latest/reference/cloudtrail/index.md")

###### Topics

- [Amazon Bedrock AgentCore Gateway event types](gateway-event-types.md "gateway-event-types.md")
- [Enable CloudTrail data event logging for Amazon Bedrock AgentCore Gateway resources](enabling-cloudtrail-data-event-logging.md "enabling-cloudtrail-data-event-logging.md")
- [Understanding Amazon Bedrock AgentCore Gateway CloudTrail events](understanding-gateway-cloudtrail-log-entries.md "understanding-gateway-cloudtrail-log-entries.md")
