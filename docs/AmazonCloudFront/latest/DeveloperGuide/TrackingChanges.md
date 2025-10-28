# Track configuration changes with AWS Config

To record and evaluate configurations of your AWS resources, you can use AWS Config, which provides you with a detailed view of the configuration of your distributions. This includes how the resources are related to one another and how they were configured in the past, so you can review changes over time.

You can also use AWS Config to record configuration changes to your CloudFront distribution settings.
You can capture changes to distribution states, price classes, origins, geographic
restriction settings, and Lambda@Edge configurations.

###### Note

AWS Config does not record key–value tags for CloudFront streaming distributions.

###### Contents

- [Set up AWS Config with CloudFront](TrackingChanges.md#TrackingChangesSettings "TrackingChanges.md#TrackingChangesSettings")
- [View CloudFront configuration history](TrackingChanges.md#TrackingChangesGetHistory "TrackingChanges.md#TrackingChangesGetHistory")
- [Evaluate CloudFront configurations with AWS Config Rules](TrackingChanges.md#cloudfront-config-rules "TrackingChanges.md#cloudfront-config-rules")

## Set up AWS Config with CloudFront

When you set up AWS Config, you can choose to record all supported AWS resources or
record only some specified resources, such as recording changes for CloudFront only. For a
list of supported CloudFront resources, see the [Amazon CloudFront](../../../config/latest/developerguide/resource-config-reference.md#amazoncloudfront "../../../config/latest/developerguide/resource-config-reference.md#amazoncloudfront") section of the Supported Resource Types topic in the
_AWS Config Developer Guide_.

###### Notes

- To track configuration changes to your CloudFront distribution, you must
  sign in to the CloudFront console in the US East (N. Virginia)
  AWS Region.
- There might be a delay in recording resources with AWS Config. AWS Config records
  resources only after it discovers the resources.

Console

###### To set up AWS Config with

CloudFront

1. Sign in to the AWS Management Console and open the [AWS Config
   console](https://console.aws.amazon.com/config/home "https://console.aws.amazon.com/config/home").
2. Choose **Get Started Now**.
3. On the **Settings** page, for
   **Resource types to record**, specify the
   AWS resource types that you want AWS Config to record. If you want
   to record only CloudFront changes, choose **Specific
   types**, and then, under **CloudFront**,
   choose the distribution or streaming distribution that you want
   to track changes for.

To add or change which distributions to track, choose
**Settings** on the left, after completing
your initial setup. 4. Specify additional required options for AWS Config: set up a
notification, specify a location for the configuration
information, and add rules for evaluating resource types.

For more information, see [Setting up AWS Config with the Console](../../../config/latest/developerguide/gs-console.md "../../../config/latest/developerguide/gs-console.md") in the
_AWS Config Developer Guide_.

AWS CLI
To set up AWS Config with CloudFront using the AWS CLI, see [Setting up AWS Config with the AWS CLI](../../../config/latest/developerguide/gs-cli.md "../../../config/latest/developerguide/gs-cli.md") in the
_AWS Config Developer Guide_.

AWS Config API
To set up AWS Config with CloudFront using the AWS Config API, see the [StartConfigurationRecorder](../../../config/latest/APIReference/API_StartConfigurationRecorder.md "../../../config/latest/APIReference/API_StartConfigurationRecorder.md") API
operation in the _AWS Config API Reference_.

## View CloudFront configuration history

After AWS Config starts recording configuration changes to your distributions, you can
get the configuration history of any distribution that you have configured for
CloudFront.

You can view configuration histories in the following ways.

Console
For each recorded resource, you can view a timeline page that provides
a history of configuration details. To view this page, choose the gray
icon in the **Config Timeline** column of the
**Dedicated Hosts** page.

For more information, see [Viewing
Configuration Details in the AWS Config Console](../../../config/latest/developerguide/view-manage-resource-console.md "../../../config/latest/developerguide/view-manage-resource-console.md") in the
_AWS Config Developer Guide_.

AWS CLI
To get a list of all your distributions, run the [list-discovered-resources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/list-discovered-resources.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/list-discovered-resources.html") command, as shown in the
following example.

```
aws configservice list-discovered-resources --resource-type AWS::CloudFront::Distribution
```

To get the configuration details of a distribution for a specific time
interval, run the [get-resource-config-history](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-resource-config-history.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-resource-config-history.html") command.

For more information, see [View Configuration
Details Using the CLI](../../../config/latest/developerguide/resource-config-reference.md "../../../config/latest/developerguide/resource-config-reference.md") in the
_AWS Config Developer Guide_.

AWS Config API
To get a list of all your distributions, use the [ListDiscoveredResources](../../../config/latest/APIReference/API_ListDiscoveredResources.md "../../../config/latest/APIReference/API_ListDiscoveredResources.md") API operation.

To get the configuration details of a distribution for a specific time
interval, use the [GetResourceConfigHistory](../../../config/latest/APIReference/API_GetResourceConfigHistory.md "../../../config/latest/APIReference/API_GetResourceConfigHistory.md") API operation. For more
information, see the [AWS Config API Reference](../../../config/latest/APIReference.md "../../../config/latest/APIReference.md").

## Evaluate CloudFront configurations with AWS Config Rules

You can evaluate configurations against desired configurations with AWS Config Rules. For example, AWS Config Rules helps you to evaluate whether your CloudFront resources comply with common security best practices. You can choose managed rules like viewer policy HTTPS, SNI enabled, OAC enabled, origin failover enabled, AWS WAF WebACL, or AWS Shield Advanced resource policies to be triggered when the configuration changes.

Managed rules can run evaluations periodically, at a frequency that you choose. AWS Firewall Manager relies on AWS Config for automatic alerts and remediations. For more information, see [Evaluating Resources with AWS Config Rules](../../../config/latest/developerguide/evaluate-config.md "../../../config/latest/developerguide/evaluate-config.md") and [List of AWS Config Managed Rules](../../../config/latest/developerguide/managed-rules-by-aws-config.md "../../../config/latest/developerguide/managed-rules-by-aws-config.md") in the _AWS Config Developer Guide_.
