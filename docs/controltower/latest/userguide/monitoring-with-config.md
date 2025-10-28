# Monitor resource changes with AWS Config

AWS Control Tower enables AWS Config on all enrolled accounts, so that it can monitor compliance through
detective controls, record resource changes, and deliver resource change logs to the log archive
account.

**If your landing zone version is earlier than 3.0**: For your
enrolled accounts, AWS Config logs all changes to resources, for all Regions in which the account
operates. Each change is modeled as a configuration item (CI), which contains information such
as the resource identifier, the Region, the date that each change was recorded, and whether the
change relates to a known resource or a newly discovered one.

**If your landing zone version is 3.0 or later**: AWS Control Tower
limits recording for global resources, such as IAM users, groups, roles, and customer managed
polices, to your home Region only. Copies of global resource changes are not stored in every
Region. This limitation of resource recording conforms with AWS Config [best practices](https://aws.amazon.com/blogs/mt/aws-config-best-practices/ "https://aws.amazon.com/blogs/mt/aws-config-best-practices/"). A [full list of
global resources](../../../config/latest/developerguide/select-resources.md "../../../config/latest/developerguide/select-resources.md") is available in AWS Config documentation.

- To learn more about AWS Config, see [How AWS Config works](../../../config/latest/developerguide/how-does-config-work.md "../../../config/latest/developerguide/how-does-config-work.md").
- For a list of resources that AWS Config can support, see [Supported resource
  types](../../../config/latest/developerguide/resource-config-reference.md "../../../config/latest/developerguide/resource-config-reference.md").
- To learn about how to customize resource tracking in the AWS Control Tower environment, see the
  blog post entitled [Customize AWS Config resource tracking in AWS Control Tower](https://aws.amazon.com/blogs/mt/customize-aws-config-resource-tracking-in-aws-control-tower-environment "https://aws.amazon.com/blogs/mt/customize-aws-config-resource-tracking-in-aws-control-tower-environment").
  AWS Control Tower sets up an AWS Config delivery channel in all enrolled accounts. Through this delivery
  channel, it logs all changes recorded by AWS Config in the log archive account, where they are stored
  to a folder in an Amazon Simple Storage Service bucket.

## View the AWS Config recorder data on enrolled accounts

AWS Config is integrated with CloudWatch so that you can view AWS Config CIs in a dashboard. For more
information, see the blog post entitled [AWS Config
supports Amazon CloudWatch metrics](https://aws.amazon.com/about-aws/whats-new/2022/05/aws-config-supports-amazon-cloudwatch-metrics "https://aws.amazon.com/about-aws/whats-new/2022/05/aws-config-supports-amazon-cloudwatch-metrics").

Programmatically, to view AWS Config data, you can work with the AWS CLI, or you can utilize
other AWS tools.

### Query the AWS Config recorder data on a

specific resource

You can use the AWS CLI to retrieve a list of the most recent changes for a
resource.

**Resource history command:**

- `aws configservice get-resource-config-history --resource-type
`RESOURCE-TYPE`--resource-id`RESOURCE-ID`--region`REGION``

To learn more, see [the API
documentation for `get-config-history`](../../../cli/latest/reference/configservice/get-resource-config-history.md "../../../cli/latest/reference/configservice/get-resource-config-history.md").

### Visualize AWS Config data with

Quick Suite

You can visualize and query resources recorded by AWS Config across your entire organization.
For more information, see the [Config Resource Compliance Dashboard](https://catalog.workshops.aws/awscid/en-US/dashboards/additional/config-resource-compliance-dashboard "https://catalog.workshops.aws/awscid/en-US/dashboards/additional/config-resource-compliance-dashboard") and [Visualizing AWS Config data using Amazon Athena and Quick Suite](https://aws.amazon.com/blogs/mt/visualizing-aws-config-data-using-amazon-athena-and-amazon-quicksight/ "https://aws.amazon.com/blogs/mt/visualizing-aws-config-data-using-amazon-athena-and-amazon-quicksight/").

## Troubleshooting AWS Config in AWS Control Tower

This section gives information about some problems you may encounter when using AWS Config with
AWS Control Tower.

### High AWS Config costs

If your workflow includes processes that create, update, or delete resources frequently,
or if it handles resources in large numbers, that workflow may generate large numbers of
CIs. If you run these processes in a non-production account, consider unenrolling the
account. You may need to de-activate the AWS Config recorder for that account manually.

###### Note

After you unenroll the account, AWS Control Tower cannot enforce detective controls or log
account events, such as AWS Config activities, for resources in that account.

For more information, see [Unmanage an enrolled
account](unmanage-account.md "unmanage-account.md"). To learn how to deactivate the AWS Config recorder, see [Managing
the configuration recorder](../../../config/latest/developerguide/stop-start-recorder.md "../../../config/latest/developerguide/stop-start-recorder.md").

### The same resource is recorded multiple

times

Check whether the resource is a [global resource](../../../config/latest/developerguide/select-resources.md "../../../config/latest/developerguide/select-resources.md"). For
AWS Control Tower landing zones prior to version 3.0, AWS Config may record certain global resources once
for each Region in which AWS Config is operating. For example, if AWS Config is enabled on eight
Regions, each role is recorded eight times.

###### The following resources are recorded once for each Region in which AWS Config is

operating:

- `AWS::IAM::Group`
- `AWS::IAM::Policy`
- `AWS::IAM::Role`
- `AWS::IAM::User`

###### Other global resources are recorded only once. Here are some examples of resources

that are recorded once:

- `AWS::Route53::HostedZone`
- `AWS::Route53::HealthCheck`
- `AWS::ECR::PublicRepository`
- `AWS::GlobalAccelerator::Listener`
- `AWS::GlobalAccelerator::EndpointGroup`
- `AWS::GlobalAccelerator::Accelerator`

### AWS Config did not record a resource

Certain resources have dependency relationships with other resources. These
relationships may be _direct_ or _indirect_.

You can find a list of deprecated indirect relationships in [the AWS Config FAQ](../../../config/latest/developerguide/faq.md#faq-2 "../../../config/latest/developerguide/faq.md#faq-2").
