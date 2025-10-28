# Understanding multi-Region trails and

opt-in Regions

A trail can be applied to all AWS Regions that are [enabled](../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-enable-standalone "../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-enable-standalone") in your AWS account, or can be applied to a single Region. A trail
that applies to all AWS Regions that are enabled in your AWS account is referred to as a
_multi-Region trail_. As a best practice, we recommend creating a
multi-Region trail because it captures activity in all enabled Regions. All trails created
using the CloudTrail console are multi-Region trails. You can only create a single-Region trail
using the AWS CLI or [`CreateTrail`](../APIReference/API_CreateTrail.md "../APIReference/API_CreateTrail.md") API operation.

Although most AWS Regions are enabled by default for your AWS account, you must
manually enable certain Regions (also referred to as _opt-in Regions_).
For information about which Regions are enabled by default, see [Considerations before enabling and disabling Regions](../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-considerations "../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-considerations") in the
_AWS Account Management Reference Guide_. For the list of Regions CloudTrail supports,
see [CloudTrail supported Regions](cloudtrail-supported-regions.md "cloudtrail-supported-regions.md").

###### Topics

- [What are the advantages of
  multi-Region trails?](#cloudtrail-multi-region-trails-advantages "#cloudtrail-multi-region-trails-advantages")
- [What happens when you create a
  multi-Region trail?](#cloudtrail-multi-region-trails-create "#cloudtrail-multi-region-trails-create")
- [What happens when you enable an
  opt-in Region?](#cloudtrail-multi-region-trails-optin "#cloudtrail-multi-region-trails-optin")
- [What happens when you disable
  an opt-in Region?](#cloudtrail-multi-region-trails-disable "#cloudtrail-multi-region-trails-disable")

## What are the advantages of

multi-Region trails?

A multi-Region trail has the following advantages:

- The configuration settings for the trail apply consistently across all [enabled](../../../accounts/latest/reference/manage-acct-regions.md "../../../accounts/latest/reference/manage-acct-regions.md")
  AWS Regions.
- You receive CloudTrail events from all enabled AWS Regions in a single Amazon S3 bucket
  and, optionally, in a CloudWatch Logs log group.
- You manage trail configurations for all enabled AWS Regions from one
  location.

## What happens when you create a

multi-Region trail?

Creating a multi-Region trail, has the following effects:

- CloudTrail delivers log files for account activity from all [enabled](../../../accounts/latest/reference/manage-acct-regions.md "../../../accounts/latest/reference/manage-acct-regions.md")
  AWS Regions to the single Amazon S3 bucket that you specify, and, optionally, to a
  CloudWatch Logs log group.
- If you configured an Amazon SNS topic for the trail, SNS notifications about log
  file deliveries in all enabled AWS Regions are sent to that single SNS
  topic.
- You can see the multi-Region trail in all enabled AWS Regions, but you can
  only modify the trail in the home Region where it was created.

## What happens when you enable an

opt-in Region?

After you enable an opt-in Region, CloudTrail creates an identical copy of each multi-Region
trail in the opt-in Region that you enabled.

CloudTrail uses a distributed computing model called [eventual consistency](cloudtrail-data-consistency.md "cloudtrail-data-consistency.md"). Because enabling
a Region takes a few minutes to several hours, you may not immediately see all events in
the logs for the newly enabled Region. It may take up to several hours for CloudTrail to
deliver all logs for the newly enabled Region. During this time, you can view the last
90 days of management events logged in that Region by viewing the CloudTrail [**Event History**](view-cloudtrail-events-console.md "view-cloudtrail-events-console.md"), or by running the [**aws
cloudtrail lookup-events --region <region>**](view-cloudtrail-events-cli.md "view-cloudtrail-events-cli.md") command. Event
history is active by default in your AWS account, captures the last 90 days of
management events logged in a Region, and does not require a trail.

For information about enabling an opt-in Region for your AWS account, see [Enable or disable a Region for standalone accounts](../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-enable-standalone "../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-enable-standalone") or [Enable or disable a Region in your organization](../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-enable-organization "../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-enable-organization").

## What happens when you disable

an opt-in Region?

Because your account may have activity in the Region you disabled, such as actions by
AWS services to remove resources, CloudTrail will continue to capture activity and attempt
to deliver events to the S3 bucket for any trails that are not deleted before the Region
is disabled.
