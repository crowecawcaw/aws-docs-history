# CloudFormation template examples for Deadline Cloud

The deadline-cloud-samples repository contains CloudFormation templates
that deploy Deadline Cloud farms and supporting infrastructure. Use these templates
as a starting point and adapt them to your environment. For the templates,
see the
[cloudformation](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation")
directory on the GitHub website.

To compare CloudFormation with the AWS CDK and Terraform for managing Deadline Cloud
infrastructure, see [Manage Deadline Cloud infrastructure as code](infrastructure-as-code.md "infrastructure-as-code.md").

###### Topics

- [Deploy a starter Deadline Cloud farm with CloudFormation](examples-cfn-starter-farm.md "examples-cfn-starter-farm.md")
- [Deploy a Deadline Cloud CUDA farm with CloudFormation](examples-cfn-cuda-farm.md "examples-cfn-cuda-farm.md")
- [Connect a Deadline Cloud fleet to FSx for OpenZFS through a VPC resource endpoint](examples-cfn-vpc-fsx.md "examples-cfn-vpc-fsx.md")
- [Manage hybrid Wait and Save plus Spot fleet capacity with CloudFormation](examples-cfn-capacity-manager.md "examples-cfn-capacity-manager.md")
- [Schedule standby workers for a Deadline Cloud fleet with CloudFormation](examples-cfn-standby-scheduling.md "examples-cfn-standby-scheduling.md")
- [Monitor a Deadline Cloud customer-managed fleet health check with CloudFormation](examples-cfn-cmf-health-check.md "examples-cfn-cmf-health-check.md")
- [Budget threshold notifications to email and Slack with CloudFormation](examples-cfn-budget-notifications.md "examples-cfn-budget-notifications.md")
- [Job event Slack notifications with Lambda and EventBridge](examples-cfn-slack-notifications.md "examples-cfn-slack-notifications.md")
