# Onboard to AWS CloudTrail Lake

This section describes the prerequisites and steps to onboard your partner application to CloudTrail Lake.

###### Topics

- [Prerequisites](#lake-partner-onboarding-prerequisites "#lake-partner-onboarding-prerequisites")
- [Step 1: Partner registration](#lake-onboarding-step1 "#lake-onboarding-step1")
- [Step 2: Build the integration](#lake-onboarding-step2 "#lake-onboarding-step2")
- [Best practices and quotas](#lake-onboarding-best-practices-quotas "#lake-onboarding-best-practices-quotas")

## Prerequisites

The following are requirements for performing tasks in this guide.

- AWS provides tiers (Select, Advanced, Premier) to recognize organizations that have proven technical expertise and demonstrated customer experience. You must be at least an [AWS Select
  Tier Partner](https://aws.amazon.com/partners/services-tiers/ "https://aws.amazon.com/partners/services-tiers/"). To become an AWS Partner, you must first meet all [requirements](https://aws.amazon.com/partners/services-tiers/#Requirements "https://aws.amazon.com/partners/services-tiers/#Requirements") for the tier.

For more information about how to become an AWS
Select Tier partner, see [Become an AWS
Partner](https://partnercentral.awspartner.com/partnercentral2/s/SelfRegister "https://partnercentral.awspartner.com/partnercentral2/s/SelfRegister").

## Step 1: Partner registration

To get started, register as an AWS Partner in the AWS Partner Network.

Be sure to meet the requirements of partner intake forms. The partner CloudTrail Lake intake forms collect information that the
AWS Partner Network uses to create your partner product profile. This profile gives
the CloudTrail team information that we add to your partner provider description that is
displayed in the CloudTrail console. Your profile also includes information that CloudTrail uses to
confirm the integrity of the event source as CloudTrail Lake receives events the from a
partner application.

1. Get started by [joining the AWS Partner
   Network](https://partnercentral.awspartner.com/partnercentral2/s/login "https://partnercentral.awspartner.com/partnercentral2/s/login"), and informing your AWS Partner Network team that you want
   to become a partner with CloudTrail Lake.
2. Get onboarding materials—including partner onboarding forms and the CloudTrail event
   schema—from the AWS Partner Network team.
3. Complete the partner onboarding forms, and share the completed forms with your AWS Partner Network team. You might not
   yet have all required details. If you have questions, contact your AWS Partner
   Network team.

## Step 2: Build the integration

Build the integration that is required to send event logs to CloudTrail Lake.

1. Review the [CloudTrail integration event
   schema](lake-onboarding-cloudtrail-event-schema.md "lake-onboarding-cloudtrail-event-schema.md") in this guide. The CloudTrail event schema provides a consistent way
   to log activity events for audit needs. This eliminates the need for
   time-consuming data standardization efforts before a cross-source analysis. CloudTrail
   Lake cannot accept events that do not follow the prescribed schema.
2. Determine the events that you want to send. CloudTrail Lake only accepts activity events, or events
   that help customers understand who did what, and when. Typically, partners have
   existing mechanisms to provide their customers access to activity logs. The
   schema mapping exercise helps you exclude non-activity events. Contact your
   AWS Partner Network team if you need help narrowing down event types.
3. Build your integration architecture to send activity events to CloudTrail Lake. This includes offering
   a setup framework (GUI is preferred) and documentation for customers to enable
   your partner application to send events to CloudTrail Lake. A partner customer must
   share a CloudTrail channel Amazon Resource Number (ARN) with the partner as part of
   the integration process.
   1. To send events to CloudTrail Lake, the partner calls the [`PutAuditEvents` API](../../../awscloudtraildata/latest/APIReference/API_PutAuditEvents.md "../../../awscloudtraildata/latest/APIReference/API_PutAuditEvents.md"),
      specifying the channel ARN provided by the customer. If the channel's
      resource policy includes an external ID, you must also pass the external ID
      when you call `PutAuditEvents`.
   2. The partner checks transfer results for failures, and
      tries to resend failed events by calling the `PutAuditEvents` API again.

## Best practices and quotas

As you integrate partner solution events, be aware of the following best practices, quotas,
and limitations.

- **Schema mapping:** Be sure that you have the key required fields included in the `eventData` block. Missing
  required fields results in errors. For information about required fields, see [Understanding the CloudTrail Lake event schema](lake-onboarding-cloudtrail-event-schema.md "lake-onboarding-cloudtrail-event-schema.md")

You can add event fields that do not map to the schema to the
`additionalEventData` field. Some partners use this field to
include the entire, raw event.

- **Batching events:** When you call the `PutAuditEvents` API, you can batch up to
  100 events in a single API call, as long as each event is not greater than
  256 kB in size, and the total size of all events is less than 1 MB. For more information about
  quotas in CloudTrail, see [Quotas in AWS CloudTrail](../userguide/WhatIsCloudTrail-Limits.md "../userguide/WhatIsCloudTrail-Limits.md") in the _AWS CloudTrail User Guide_.
