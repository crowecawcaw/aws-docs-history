# Manage your Amazon GameLift Servers hosting costs

Your AWS bill reflects your game hosting costs. You can view estimated charges for the
current month, and final charges for previous months on the Billing console at
[https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/"). For more information about tools and resources to help you
manage your AWS costs, see the [AWS Billing User Guide](../../../awsaccountbilling/latest/aboutv2/billing-what-is.md "../../../awsaccountbilling/latest/aboutv2/billing-what-is.md").
This guide can help you review your resource consumption, establish future usage, and
determine your scaling needs.

Consider these tips to help you manage the cost of Amazon GameLift Servers services.

## Create billing alerts to monitor usage

Set up an AWS Free Tier usage alert to notify you when your usage is nearing or
exceeding the Free Tier limits for Amazon GameLift Servers and other AWS services. You can configure
the alerts to take action based on your usage levels. For example, you can automatically
set your budget to zero when your reach a Free Tier limit.

You can also set Amazon CloudWatch billing alerts to get notifications when usage hits custom thresholds.

For more information, see these topics in the _AWS Billing User Guide_:

- [Tracking your AWS Free Tier usage](../../../awsaccountbilling/latest/aboutv2/tracking-free-tier-usage.md "../../../awsaccountbilling/latest/aboutv2/tracking-free-tier-usage.md")
- [Billing alert preferences](../../../awsaccountbilling/latest/aboutv2/billing-pref.md "../../../awsaccountbilling/latest/aboutv2/billing-pref.md")

## Track costs per Amazon GameLift Servers fleet

Use AWS cost allocation tags to organize and track your game hosting costs based on
Amazon GameLift Servers Amazon EC2 fleets and other resources. By tagging your fleets, either individually or
by groups, you can create cost allocation reports that categorize costs based on the
assigned tag. You can use this type of report to identify how fleets are contributing to
your hosting costs. You can also use tags to filter views in AWS Cost Explorer.

For more information, see these topics:

- [Using AWS cost
  allocation tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md"), _AWS Billing User Guide_
- [Analyzing your costs
  with AWS Cost Explorer](../../../cost-management/latest/userguide/ce-what-is.md "../../../cost-management/latest/userguide/ce-what-is.md"), _AWS Cost Management User Guide_

## Set managed fleet capacity to zero

Managed fleets can continue to incur costs even when they're not being used to host
game sessions. To avoid incurring unnecessary charges, [scale your fleet down](fleets-updating-capacity.md "fleets-updating-capacity.md") to zero when not in
use. If you use auto scaling, suspend this activity and manually set the fleet
capacity.
