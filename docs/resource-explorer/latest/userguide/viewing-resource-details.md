# Viewing resource details

In the Resource Explorer console, you can view the details of a selected resource, including information
about the resource provided by other AWS services. To view a resource's details, open the **Resources** page, and select the checkbox of the desired resource.
Review each of the tabs to learn more about the resource.

###### Topics

- [Overview](#res-details-overview "#res-details-overview")
- [Relationships](#res-details-relationships "#res-details-relationships")
- [Timeline](#res-details-timeline "#res-details-timeline")
- [Compliance](#res-details-compliance "#res-details-compliance")
- [Resource shares](#res-details-shares "#res-details-shares")
- [Tags](#res-details-tags "#res-details-tags")
- [Additional properties](#res-details-addproperties "#res-details-addproperties")

## Overview

The Overview tab displays basic information about the selected resource, including the **Resource type**,
**Amazon Resource Name (ARN)**, the **AWS Region** where the resource resides,
the **Owner account**, and the **Last indexed** date and time stamp. For some resource types,
this tab also displays resource properties sourced from the AWS Cloud Control API, like public access settings for Amazon S3 buckets
or instance state for Amazon EC2 instances. This tab also includes a
link to the resource's native console.

If additional AWS services are enabled in your AWS account, the
Overview tab also displays the following information:

- **[AWS Security Hub](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md")** — This integration displays a
  total number of [Security findings](../../../securityhub/latest/userguide/securityhub-control-manage-findings.md "../../../securityhub/latest/userguide/securityhub-control-manage-findings.md")
  and a total number of Critical and High ranked findings. If available, choosing the **Total findings** link directs you to
  the Security Hub console.
- **[AWS Cost Explorer](../../../cost-management/latest/userguide/ce-what-is.md "../../../cost-management/latest/userguide/ce-what-is.md")** — This integration displays the resource's
  **Cost** over the past 14 days. Choosing the **cost value** link directs you
  to the resource's cost details page in the AWS Cost Explorer console.
- **[AWS Config](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md")** —
  This integration displays the resource's
  **Compliance** status with rules from AWS Config. Choosing the compliance status link directs you
  to the resource details **Compliance** tab.

**Minimum permissions**

To view all of the available resource details in this tab, which includes details from
other AWS services, you must have the following permissions:

- **Action**: `ce:GetCostAndUsageWithResources`
- **Action**: `cloudformation:GetResource`
- **Action**: `config:DescribeComplianceByResource`
- **Action**: `config:DescribeConfigurationRecorders`
- **Action**: `config:DescribeConfigurationRecorderStatus`
- **Action**: `config:GetComplianceDetailsByResource`
- **Action**: `securityhub:GetAdhocInsightResults`

## Relationships

The Relationships tab displays the selected resource's single-level relationships to other resources.
This tab only displays relationships for supported resource types.

**Minimum permissions**

To view resource relationships in this tab, you must have at least read-only permissions for all
resource types and underlying AWS services you want to visualize. Resource Explorer recommends using
the [`ReadOnlyAccess` general AWS managed policy](../../../aws-managed-policy/latest/reference/ReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/ReadOnlyAccess.md").
You can attach this policy to your users, groups, and roles to provide read-only access to
AWS services and resources.

## Timeline

If you have AWS Config enabled in your account, the Timeline tab displays a resource's
history of events over the past 60 days. You can filter by Configuration events, Compliance events, or CloudTrail Events.

You can learn more about [Viewing
compliance history timeline for resources and rules](../../../config/latest/developerguide/view-manage-resource-console.md "../../../config/latest/developerguide/view-manage-resource-console.md") in the _AWS Config developer guide_.

For accounts without AWS Config enabled, the Timeline tab displays AWS CloudTrail events. You can learn more about
[Understanding CloudTrail events](../../../awscloudtrail/latest/userguide/cloudtrail-events.md "../../../awscloudtrail/latest/userguide/cloudtrail-events.md")
in the _AWS CloudTrail User Guide_.

**Minimum permissions**

To view a resource's event history in this tab, you must have the following permissions:

- **Action**: `config:DescribeConfigurationRecorderStatus`
- **Action**: `cloudtrail:LookupEvents`
- **Action**: `config:GetResourceConfigHistory`

## Compliance

If your account already has AWS Config enabled, but does not include any
rules, you can choose **Add rule** to create new rules in the AWS Config console.

If the selected resource does include rules, this tab displays the
resource's **Compliant** and **Non-compliant** rules, including any known fixes
for non-compliant rules. Choosing an individual rule directs you to the rule in the AWS Config console.

You can learn more about [Evaluating resources with
AWS Config rules](../../../config/latest/developerguide/evaluate-config.md "../../../config/latest/developerguide/evaluate-config.md") in the _AWS Config developer guide_.

**Minimum permissions**

To view resource details in this tab, you must have AWS Config enabled in your AWS account
and have the following permissions:

- **Action**: `config:DescribeComplianceByResource`
- **Action**: `config:DescribeConfigurationRecorders`
- **Action**: `config:DescribeConfigurationRecorderStatus`
- **Action**: `config:DescribeRemediationConfigurations`
- **Action**: `config:GetComplianceDetailsByResource`

## Resource shares

The Resource shares tab displays any resource shares that include this resource. Use
AWS Resource Access Manager to create resource shares that make the resource available to other individual
AWS accounts, or to the accounts in an organization or an organizational unit. Review
[Sharing your AWS resources](../../../ram/latest/userguide/getting-started-sharing.md "../../../ram/latest/userguide/getting-started-sharing.md") in the
AWS Resource Access Manager user guide for more information.

**Minimum permissions**

To view resource shares in this tab, you must have the following permissions:

- **Action**: `ram:ListResources`
- **Action**: `ram:GetResourceShares`

## Tags

The Tags tab displays a list of tags attached to the selected resource. Each tag contains a
key name and an associated value that you can use to categorize your resources.

**Minimum permissions**

To view a resource's tags in this tab, you must have the following permissions:

- **Action**: `tag:GetResources`

## Additional properties

The Additional properties tab displays resource details obtained by AWS Cloud Control API, including
the availability zone, block device mappings, and more.

**Minimum permissions**

To view a resource's additional properties in this tab, you must have the following permissions:

- **Action**: `cloudformation:GetResource`
