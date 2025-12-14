**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Tracking Shield Advanced resource protection changes in AWS Config

This page explains how to record changes to the AWS Shield Advanced protection of your resources using AWS Config. You can
then use this information to maintain a configuration change history for audit and
troubleshooting purposes.

To record protection changes, enable AWS Config for each resource that you want to track. For more
information, see [Getting Started with
AWS Config](../../../config/latest/developerguide/getting-started.md "../../../config/latest/developerguide/getting-started.md") in the _AWS Config Developer Guide_.

You must enable AWS Config for each AWS Region that contains the tracked resources. You can
enable AWS Config manually, or you can use the CloudFormation template "Enable AWS Config" at [CloudFormation StackSets Sample
Templates](../../../AWSCloudFormation/latest/UserGuide/stacksets-sampletemplates.md "../../../AWSCloudFormation/latest/UserGuide/stacksets-sampletemplates.md") in the _CloudFormation User Guide_.

If you enable AWS Config, you're charged as detailed on the [AWS Config Pricing](https://aws.amazon.com/config/pricing/ "https://aws.amazon.com/config/pricing/") page.

###### Note

If you already have AWS Config enabled for the necessary Regions and resources, you don't need to do
anything. AWS Config logs regarding protection changes to your resources start populating
automatically.

After enabling AWS Config, use the US East (N. Virginia) Region in the AWS Config console to view the
configuration change history for AWS Shield Advanced global resources.

View the change history for AWS Shield Advanced regional resources via the AWS Config console in the
US East (N. Virginia), US East (Ohio), US West (Oregon), US West (N. California),
Europe (Ireland), Europe (Frankfurt), Asia Pacific (Tokyo), and
Asia Pacific (Sydney) Regions.
