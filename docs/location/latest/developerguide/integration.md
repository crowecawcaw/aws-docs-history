# AWS integration for Amazon Location Service

Amazon Location Service is integrated with various AWS services for efficient authentication,
monitoring, management and development.

**Monitor**

- Amazon CloudWatch – View metrics on
  service usage and health, including requests, latency, faults, and logs.
  For more information, see [Monitor with Amazon CloudWatch](cloudwatch.md "cloudwatch.md").
- AWS CloudTrail – Log and monitor your
  API calls, which include actions taken by a user, role or an AWS
  service. For more information, see [Monitor and log with AWS CloudTrail](cloudtrail.md "cloudtrail.md").

**Manage**

- AWS CloudFormation – Amazon Location is
  integrated with AWS CloudFormation, a service that helps you to model and set up
  your AWS resources so that you can spend less time creating and
  managing your resources and infrastructure. For more information, see
  [Create resources with AWS CloudFormation](cloudformation.md "cloudformation.md").
- Service Quotas – Use the Service Quotas console
  and AWS CLI to request changes to your adjustable quotas. For more
  information, see [Manage quotas with Service Quotas](manage-quotas.md "manage-quotas.md").
- Tags – Use resource tagging in
  Amazon Location to create tags to categorize your resources by purpose, owner,
  environment, or criteria. Tagging your resources helps you manage,
  identify, organize, search, and filter your resources. For more
  information, see [Manage resources with Tags](manage-resources.md "manage-resources.md").

**Authenticate**

- Amazon Cognito – You can use
  Amazon Cognito authentication as an alternative to directly using AWS Identity and Access Management
  (IAM) with both frontend SDKs and direct
  HTTPS requests. For more information, see [Use Amazon Cognito to authenticate](authenticating-using-cognito.md "authenticating-using-cognito.md").
- IAM – AWS Identity and Access Management (IAM)
  is an AWS service that helps an administrator
  securely control access to AWS resources. IAM administrators control who
  can be authenticated (signed in) and authorized (have permissions) to
  use Amazon Location Service resources. For more information, see
  [Use AWS Identity and Access Management to authenticate](security-iam.md "security-iam.md").

**Value added**

- Amazon EventBridge – Enable an
  event-driven application architecture so you can use AWS Lambda
  functions to activate other parts of your application and work flows.
  For more information, see
  [React to Amazon Location Service events with Amazon EventBridge](location-events.md "location-events.md").
- AWS IoT – The AWS IoT Core rules
  engine stores queries about your devices' message topics and enables you
  to define actions for sending messages to other AWS services, such as
  Amazon Location Service. Devices that are aware of their location as
  coordinates can have their locations forwarded to Amazon Location
  through the rules engine. For more information, see
  [Track using AWS IoT and MQTT with Amazon Location Service](tracking-using-mqtt.md "tracking-using-mqtt.md").

**Developer tool**

- SDKs – Amazon Location Service
  offers a variety of tools for developers to build location-enabled
  applications. These include the standard AWS SDKs, mobile and web SDKs.
  For more information, see [SDKs and frameworks for Amazon Location Service](dev-sdks.md "dev-sdks.md").
- AWS CLI – The AWS Command Line Interface (AWS CLI) is an open source tool that enables you to interact
  with AWS services using commands in your command-line shell. With
  minimal configuration. For more information, see [AWS Command Line Interface](../../../cli/latest/reference/location.md "../../../cli/latest/reference/location.md") or learn more about
  [AWS CLI](../../../cli.md "../../../cli.md").
- Sample code – Sample code uses
  AWS SDKs, mobile and web SDKs, MapLibre to demonstrate how you can use
  Amazon Location. For more information, see [samples](https://location.aws.com/samples "https://location.aws.com/samples").
- Amazon Location Service console
  – Use the Amazon Location console to learn about APIs, resources,
  and to get started with a visual and interactive learning tool. For more
  information, see the [Amazon Location Service console](https://console.aws.amazon.com/location/explore/home "https://console.aws.amazon.com/location/explore/home").

**Cost and billing**

- AWS Billing and Cost Management
  – Service provides helps to you pay your bills and optimize your
  costs. Amazon Web Services bills your account for usage, which ensures
  that you pay only for what you use. For more information, see [Pricing model](pricing.md "pricing.md") or [Manage billing and costs with AWS Billing and Cost Management](manage-billing.md "manage-billing.md").
