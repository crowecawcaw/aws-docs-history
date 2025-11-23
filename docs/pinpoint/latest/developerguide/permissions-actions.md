**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Amazon Pinpoint actions for IAM policies

To manage access to Amazon Pinpoint resources in your AWS account, you can add Amazon Pinpoint
actions to AWS Identity and Access Management (IAM) policies. By using actions in policies, you can control what
users can do on the Amazon Pinpoint console. You can also control what users can do programmatically
by using the AWS SDKs, the AWS Command Line Interface (AWS CLI), or the Amazon Pinpoint APIs directly.

In a policy, you specify each action with the appropriate Amazon Pinpoint namespace followed by
a colon and the name of the action, such as `GetSegments`. Most actions
correspond to a request to the Amazon Pinpoint API using a specific URI and HTTP method. For example,
if you allow the `mobiletargeting:GetSegments` action in a user's policy, the
user is allowed to retrieve information about all the segments for a project by submitting
an HTTP GET request to the [`/apps/`projectId`/segments`](https://docs.aws.amazon.compinpoint/latest/apireference/rest-api-segments.html#rest-api-segments-list "https://docs.aws.amazon.compinpoint/latest/apireference/rest-api-segments.html#rest-api-segments-list") URI.
This policy also allows the user to view that information on the console, and retrieve that
information by using an AWS SDK or the AWS CLI.

Each action is performed on a specific Amazon Pinpoint resource, which you identify in a policy
statement by its Amazon Resource Name (ARN). For example, the
`mobiletargeting:GetSegments` action is performed on a specific project,
which you identify with the ARN,
`arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId``.

This topic identifies Amazon Pinpoint actions that you can add to IAM policies for your AWS
account. To see examples that demonstrate how you can use actions in policies to manage
access to Amazon Pinpoint resources, see [Amazon Pinpoint identity-based
policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

###### Topics

- [Amazon Pinpoint API actions](#permissions-actions-apiactions "#permissions-actions-apiactions")
- [Amazon Pinpoint SMS and voice version 1
  API actions](#permissions-actions-sms-voice-apiactions "#permissions-actions-sms-voice-apiactions")

## Amazon Pinpoint API actions

This section identifies actions for features that are available from the Amazon Pinpoint API,
which is the primary API for Amazon Pinpoint. To learn more about this API, see the
[Amazon Pinpoint API Reference](../apireference.md "../apireference.md").

###### Categories:

- [Analytics and
  metrics](#permissions-actions-apiactions-metrics "#permissions-actions-apiactions-metrics")
- [Campaigns](#permissions-actions-apiactions-campaigns "#permissions-actions-apiactions-campaigns")
- [Channels](#permissions-actions-apiactions-channels "#permissions-actions-apiactions-channels")
- [Endpoints](#permissions-actions-apiactions-endpoints "#permissions-actions-apiactions-endpoints")
- [Event streams](#permissions-actions-apiactions-event-streams "#permissions-actions-apiactions-event-streams")
- [Events](#permissions-actions-apiactions-events "#permissions-actions-apiactions-events")
- [Export jobs](#permissions-actions-apiactions-export-jobs "#permissions-actions-apiactions-export-jobs")
- [Import jobs](#permissions-actions-apiactions-import-jobs "#permissions-actions-apiactions-import-jobs")
- [Journeys](#permissions-actions-apiactions-journeys "#permissions-actions-apiactions-journeys")
- [Message
  templates](#permissions-actions-apiactions-templates-messages "#permissions-actions-apiactions-templates-messages")
- [Messages](#permissions-actions-apiactions-messages "#permissions-actions-apiactions-messages")
- [One-time passwords](#permissions-actions-apiactions-otp "#permissions-actions-apiactions-otp")
- [Phone number
  validation](#permissions-actions-apiactions-phone-number-validate "#permissions-actions-apiactions-phone-number-validate")
- [Projects](#permissions-actions-apiactions-projects "#permissions-actions-apiactions-projects")
- [Recommender
  models](#permissions-actions-apiactions-recommenders "#permissions-actions-apiactions-recommenders")
- [Segments](#permissions-actions-apiactions-segments "#permissions-actions-apiactions-segments")
- [Tags](#permissions-actions-apiactions-tags "#permissions-actions-apiactions-tags")
- [Users](#permissions-actions-apiactions-users "#permissions-actions-apiactions-users")

### Analytics and

metrics

The following permissions are related to viewing analytics data on the Amazon Pinpoint
console. They're also related to retrieving (querying) aggregated data for standard
metrics, also referred to as _key performance indicators (KPIs)_,
that apply to projects, campaigns, and journeys.

**`mobiletargeting:GetReports`**

View analytics data on the Amazon Pinpoint console. This permission is also
required in order to create segments that contain custom attributes
using the Amazon Pinpoint console. It's also required to obtain an estimate of the
size of a segment in the Amazon Pinpoint console.

- URI – Not applicable
- Method – Not applicable
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:*`

**`mobiletargeting:GetApplicationDateRangeKpi`**

Retrieve (query) aggregated data for a standard application metric.
This is a metric that applies to all the campaigns or transactional
messages that are associated with a project.

- URI – [`/apps/`projectId`/kpis/daterange/`kpi-name``](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-kpis-daterange-kpi-name.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-kpis-daterange-kpi-name.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/kpis/daterange/`kpi-name``

**`mobiletargeting:GetCampaignDateRangeKpi`**

Retrieve (query) aggregated data for a standard campaign metric. This
is a metric that applies to an individual campaign.

- URI – [`/apps/`projectId`/campaigns/`campaignId`/kpis/daterange/`kpi-name``](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-campaigns-campaign-id-kpis-daterange-kpi-name.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-campaigns-campaign-id-kpis-daterange-kpi-name.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/campaigns/`campaignId`/kpis/daterange/`kpi-name``

**`mobiletargeting:GetJourneyDateRangeKpi`**

Retrieve (query) aggregated data for a standard journey engagement
metric. This is an engagement metric that applies to an individual
journey—for example, the number of messages that were opened by
participants for all the activities in a journey.

- URI – [`/apps/`projectId`/journeys/`journeyId`/kpis/daterange/`kpi-name``](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-journeys-journey-id-kpis-daterange-kpi-name.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-journeys-journey-id-kpis-daterange-kpi-name.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/journeys/`journeyId`/kpis/daterange/`kpi-name``

**`mobiletargeting:GetJourneyExecutionMetrics`**

Retrieve (query) aggregated data for standard execution metrics that
apply to an individual journey—for example, the number of
participants who are actively proceeding through all the activities in a
journey.

- URI – [`/apps/`projectId`/journeys/`journeyId`/execution-metrics`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-journeys-journey-id-execution-metrics.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-journeys-journey-id-execution-metrics.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/journeys/`journeyId`/execution-metrics`

**`mobiletargeting:GetJourneyExecutionActivityMetrics`**

Retrieve (query) aggregated data for standard execution metrics that
apply to an individual activity in a journey—for example, the
number of participants who started or completed an activity.

- URI – [`/apps/`projectId`/journeys/`journeyId`/activities/`journey-activity-id`/execution-metrics`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-journeys-journey-id-activities-journey-activity-id-execution-metrics.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-journeys-journey-id-activities-journey-activity-id-execution-metrics.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/journeys/`journeyId`/activities/`journey-activity-id`/execution-metrics`

### Campaigns

The following permissions are related to managing campaigns in your Amazon Pinpoint
account.

**`mobiletargeting:CreateCampaign`**

Create a campaign for a project.

- URI – [`/apps/`projectId`/campaigns`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-campaigns.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-campaigns.html")
- Method – POST
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/campaigns`

**`mobiletargeting:DeleteCampaign`**

Delete a specific campaign.

- URI – [`/apps/`projectId`/campaigns/`campaignId``](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-campaigns.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-campaigns.html")
- Method – DELETE
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/campaigns/`campaignId``

**`mobiletargeting:GetCampaign`**

Retrieve information about a specific campaign.

- URI – [`/apps/`projectId`/campaigns/`campaignId``](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-campaigns.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-campaigns.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/campaigns/`campaignId``

**`mobiletargeting:GetCampaignActivities`**

Retrieve information about the activities performed by a
campaign.

- URI – [`/apps/`projectId`/campaigns/`campaignId`/activities`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-campaigns.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-campaigns.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/campaigns/`campaignId``

**`mobiletargeting:GetCampaigns`**

Retrieve information about all campaigns for a project.

- URI – [`/apps/`projectId`/campaigns`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-campaigns.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-campaigns.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId``

**`mobiletargeting:GetCampaignVersion`**

Retrieve information about a specific campaign version.

- URI – [`/apps/`projectId`/campaigns/`campaignId`/versions/`versionId``](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-campaigns-campaign-id-versions-version.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-campaigns-campaign-id-versions-version.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/campaigns/`campaignId``

**`mobiletargeting:GetCampaignVersions`**

Retrieve information about the current and prior versions of a
campaign.

- URI – [`/apps/`projectId`/campaigns/`campaignId`/versions`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-campaigns-campaign-id-versions-version.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-campaigns-campaign-id-versions-version.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/campaigns/`campaignId``

**`mobiletargeting:UpdateCampaign`**

Update a specific campaign.

- URI – [`/apps/`projectId`/campaigns/`campaignId``](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-campaigns.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-campaigns.html")
- Method – PUT
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/campaigns/`campaignId``

### Channels

The following permissions are related to managing channels in your Amazon Pinpoint account.
In Amazon Pinpoint, _channels_ refer to the methods that you use to contact
your customers, such as sending email, SMS messages, or push notifications.

`**mobiletargeting:DeleteAdmChannel**`

Disable the Amazon Device Messaging (ADM) channel for a
project.

- URI – [`/apps/`projectId`/channels/adm`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-adm.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-adm.html")
- Method – DELETE
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/channels/adm`

`**mobiletargeting:GetAdmChannel**`

Retrieve information about the ADM channel for a project.

- URI – [`/apps/`projectId`/channels/adm`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-adm.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-adm.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/channels/adm`

`**mobiletargeting:UpdateAdmChannel**`

Enable or update the ADM channel for a project.

- URI – [`/apps/`projectId`/channels/adm`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-adm.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-adm.html")
- Method – PUT
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/channels/adm`

**`mobiletargeting:DeleteApnsChannel`**

Disable the Apple Push Notification service (APNs) channel for a project.

- URI – [`/apps/`projectId`/channels/apns`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-apns.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-apns.html")
- Method – DELETE
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/channels/apns`

**`mobiletargeting:GetApnsChannel`**

Retrieve information about the APNs channel for a project.

- URI – [`/apps/`projectId`/channels/apns`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-apns.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-apns.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/channels/apns`

**`mobiletargeting:UpdateApnsChannel`**

Enable or update the APNs channel for a project.

- URI – [`/apps/`projectId`/channels/apns`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-apns.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-apns.html")
- Method – PUT
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/channels/apns`

**`mobiletargeting:DeleteApnsSandboxChannel`**

Disable the APNs sandbox channel for a project.

- URI – [`/apps/`projectId`/channels/apns_sandbox`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-apns.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-apns.html")
- Method – DELETE
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/channels/apns_sandbox`

**`mobiletargeting:GetApnsSandboxChannel`**

Retrieve information about the APNs sandbox channel for a
project.

- URI – [`/apps/`projectId`/channels/apns_sandbox`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-apns_sandbox.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-apns_sandbox.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/channels/apns_sandbox`

**`mobiletargeting:UpdateApnsSandboxChannel`**

Enable or update the APNs sandbox channel for a project.

- URI – [`/apps/`projectId`/channels/apns_sandbox`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-apns_sandbox.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-apns_sandbox.html")
- Method – PUT
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/channels/apns_sandbox`

**`mobiletargeting:DeleteApnsVoipChannel`**

Disable the APNs VoIP channel for a project.

- URI – [`/apps/`projectId`/channels/apns_voip`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-apns_voip.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-apns_voip.html")
- Method – DELETE
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/channels/apns_voip`

**`mobiletargeting:GetApnsVoipChannel`**

Retrieve information about the APNs VoIP channel for a
project.

- URI – [`/apps/`projectId`/channels/apns_voip`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-apns_voip.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-apns_voip.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/channels/apns_voip`

**`mobiletargeting:UpdateApnsVoipChannel`**

Enable or update the APNs VoIP channel for a project.

- URI – [`/apps/`projectId`/channels/apns_voip`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-apns_voip.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-apns_voip.html")
- Method – PUT
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/channels/apns_voip`

**`mobiletargeting:DeleteApnsVoipSandboxChannel`**

Disable the APNs VoIP sandbox channel for a project.

- URI – [`/apps/`projectId`/channels/apns_voip_sandbox`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-apns_voip_sandbox.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-apns_voip_sandbox.html")
- Method – DELETE
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/channels/apns_voip_sandbox`

**`mobiletargeting:GetApnsVoipSandboxChannel`**

Retrieve information about the APNs VoIP sandbox channel for a
project.

- URI – [`/apps/`projectId`/channels/apns_voip_sandbox`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-apns_voip_sandbox.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-apns_voip_sandbox.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/channels/apns_voip_sandbox`

**`mobiletargeting:UpdateApnsVoipSandboxChannel`**

Enable or update the APNs VoIP sandbox channel for a project.

- URI – [`/apps/`projectId`/channels/apns_voip_sandbox`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-apns_voip_sandbox.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-apns_voip_sandbox.html")
- Method – PUT
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/channels/apns_voip_sandbox`

**`mobiletargeting:DeleteBaiduChannel`**

Disable the Baidu Cloud Push channel for a project.

- URI – [`/apps/`projectId`/channels/baidu`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-baidu.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-baidu.html")
- Method – DELETE
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/channels/baidu`

**`mobiletargeting:GetBaiduChannel`**

Retrieve information about the Baidu Cloud Push channel for a
project.

- URI – [`/apps/`projectId`/channels/baidu`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-baidu.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-baidu.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/channels/baidu`

**`mobiletargeting:UpdateBaiduChannel`**

Enable or update the Baidu Cloud Push channel for a project.

- URI – [`/apps/`projectId`/channels/baidu`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-baidu.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-baidu.html")
- Method – PUT
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/channels/baidu`

**`mobiletargeting:DeleteEmailChannel`**

Disable the email channel for a project.

- URI – [`/apps/`projectId`/channels/email`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-email.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-email.html")
- Method – DELETE
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/channels/email`

**`mobiletargeting:GetEmailChannel`**

Retrieve information about the email channel for a project.

- URI – [`/apps/`projectId`/channels/email`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-email.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-email.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/channels/email`

**`mobiletargeting:UpdateEmailChannel`**

Enable or update the email channel for a project.

- URI – [`/apps/`projectId`/channels/email`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-email.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-email.html")
- Method – PUT
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/channels/email`

**`mobiletargeting:DeleteGcmChannel`**

Disable the Firebase Cloud Messaging (FCM) channel for a project. This channel
allows Amazon Pinpoint to send push notifications to an Android app through the
FCM service, which replaces the Google Cloud Messaging (GCM)
service.

- URI – [`/apps/`projectId`/channels/gcm`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-gcm.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-gcm.html")
- Method – DELETE
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/channels/gcm`

**`mobiletargeting:GetGcmChannel`**

Retrieve information about the FCM channel for a project. This
channel allows Amazon Pinpoint to send push notifications to an Android app
through the FCM service, which replaces the Google Cloud Messaging
(GCM) service.

- URI – [`/apps/`projectId`/channels/gcm`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-gcm.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-gcm.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/channels/gcm`

**`mobiletargeting:UpdateGcmChannel`**

Enable or update the FCM channel for a project. This channel allows
Amazon Pinpoint to send push notifications to an Android app through the FCM
service, which replaces the Google Cloud Messaging (GCM) service.

- URI – [`/apps/`projectId`/channels/gcm`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-gcm.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-gcm.html")
- Method – PUT
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/channels/gcm`

**`mobiletargeting:DeleteSmsChannel`**

Disable the SMS channel for a project.

- URI – [`/apps/`projectId`/channels/sms`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-sms.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-sms.html")
- Method – DELETE
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/channels/sms`

**`mobiletargeting:GetSmsChannel`**

Retrieve information about the SMS channel for a project.

- URI – [`/apps/`projectId`/channels/sms`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-sms.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-sms.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/channels/sms`

**`mobiletargeting:UpdateSmsChannel`**

Enable or update the SMS channel for a project.

- URI – [`/apps/`projectId`/channels/sms`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-sms.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-sms.html")
- Method – PUT
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/channels/sms`

**`mobiletargeting:GetChannels`**

Retrieves information about the history and status of each channel for
an application.

- URI – [`/apps/`application-id`/channels`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels.html#apps-application-id-channelsget "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels.html#apps-application-id-channelsget")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:region:`accountId`:apps/`projectId`/channels`

**`mobiletargeting:DeleteVoiceChannel`**

Disables the voice channel for an application and deletes any existing
settings for the channel.

- URI – [`/apps/`application-id`/channels/voice`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-voice.html#apps-application-id-channels-voicedelete "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-voice.html#apps-application-id-channels-voicedelete")
- Method – DELETE
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectid`/channels/voice`

**`mobiletargeting:GetVoiceChannel`**

Retrieves information about the status and settings of the voice
channel for an application.

- URI – [`/apps/`application-id`/channels/voice`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-voice.html#apps-application-id-channels-voiceget "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-voice.html#apps-application-id-channels-voiceget")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectid`/channels/voice`

**`mobiletargeting:UpdateVoiceChannel`**

Enables the voice channel for an application or updates the status and
settings of the voice channel for an application.

- URI – [`/apps/`application-id`/channels/voice`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-voice.html#apps-application-id-channels-voiceput "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-channels-voice.html#apps-application-id-channels-voiceput")
- Method – PUT
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectid`/channels/voice`

### Endpoints

The following permissions are related to managing endpoints in your Amazon Pinpoint account.
In Amazon Pinpoint, an _endpoint_ is a single destination for your
messages. For example, an endpoint could be a customer's email address, telephone
number, or mobile device token.

**`mobiletargeting:DeleteEndpoint`**

Delete an endpoint.

- URI – [`/apps/`projectId`/endpoints/`endpointId``](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-endpoints-endpoint-id.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-endpoints-endpoint-id.html")
- Method – DELETE
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/endpoints/`endpointId``

**`mobiletargeting:GetEndpoint`**

Retrieve information about a specific endpoint.

- URI – [`/apps/`projectId`/endpoints/`endpointId``](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-endpoints-endpoint-id.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-endpoints-endpoint-id.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/endpoints/`endpointId``

**`mobiletargeting:RemoveAttributes`**

Removes one or more attributes, of the same attribute type, from all
the endpoints that are associated with an application.

- URI – [`apps`/application-id`/attributes/`attribute-type``](../apireference/apps-application-id-attributes-attribute-type.md#apps-application-id-attributes-attribute-typeput "../apireference/apps-application-id-attributes-attribute-type.md#apps-application-id-attributes-attribute-typeput")
- Method – PUT
- Resource ARN –
  `arn:aws:mobiletargeting:region:`accountId`:apps/`projectId`/attributes/`attribute-type``

**`mobiletargeting:UpdateEndpoint`**

Create an endpoint or update the information for an endpoint.

- URI – [`/apps/`projectId`/endpoints/`endpointId``](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-endpoints-endpoint-id.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-endpoints-endpoint-id.html")
- Method – PUT
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/endpoints/`endpointId``

**`mobiletargeting:UpdateEndpointsBatch`**

Create or update endpoints as a batch operation.

- URI – [`/apps/`projectId`/endpoints`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-endpoints-endpoint-id.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-endpoints-endpoint-id.html")
- Method – PUT
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId``

### Event streams

The following permissions are related to managing event streams for your Amazon Pinpoint
account.

**`mobiletargeting:DeleteEventStream`**

Delete the event stream for a project.

- URI – [`/apps/`projectId`/eventstream/`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-eventstream.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-eventstream.html")
- Method – DELETE
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/eventstream`

**`mobiletargeting:GetEventStream`**

Retrieve information about the event stream for a project.

- URI – [`/apps/`projectId`/eventstream/`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-eventstream.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-eventstream.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/eventstream`

**`mobiletargeting:PutEventStream`**

Create or update an event stream for a project.

- URI – [`/apps/`projectId`/eventstream/`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-eventstream.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-eventstream.html")
- Method – POST
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/eventstream`

### Events

The following permissions are related to managing events jobs in your Amazon Pinpoint
account. In Amazon Pinpoint, you create _import jobs_ to create segments
based on endpoint definitions that are stored in an Amazon S3 bucket.

**`mobiletargeting:PutEvents`**

Creates a new event to record for endpoints, or creates or updates
endpoint data that existing events are associated with.

- URI – [`/apps/`application-id`/events`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-events.html#apps-application-id-eventspost "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-events.html#apps-application-id-eventspost")
- Method – POST
- Resource ARN –
  `arn:aws:mobiletargeting:region:`accountId`:apps/`projectId`/events`

### Export jobs

The following permissions are related to managing export jobs in your Amazon Pinpoint
account. In Amazon Pinpoint, you create _export jobs_ to send information
about endpoints to an Amazon S3 bucket for storage or analysis.

**`mobiletargeting:CreateExportJob`**

Create an export job for exporting endpoint definitions to
Amazon S3.

- URI – [`/apps/`projectId`/jobs/export`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-jobs-export.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-jobs-export.html")
- Method – POST
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/jobs/export`

**`mobiletargeting:GetExportJob`**

Retrieve information about a specific export job for a project.

- URI – [`/apps/`projectId`/jobs/export/`jobId``](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-jobs-export.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-jobs-export.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/jobs/export/`jobId``

**`mobiletargeting:GetExportJobs`**

Retrieve a list of all the export jobs for a project.

- URI – [`/apps/`projectId`/jobs/export`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-jobs-export.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-jobs-export.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/jobs/export`

### Import jobs

The following permissions are related to managing import jobs in your Amazon Pinpoint
account. In Amazon Pinpoint, you create _import jobs_ to create segments
based on endpoint definitions that are stored in an Amazon S3 bucket.

**`mobiletargeting:CreateImportJob`**

Import endpoint definitions from Amazon S3 to create a segment.

- URI – [`/apps/`projectId`/jobs/import`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-jobs-import.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-jobs-import.html")
- Method – POST
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId``

**`mobiletargeting:GetImportJob`**

Retrieve information about a specific import job for a project.

- URI – [`/apps/`projectId`/jobs/import/`jobId``](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-jobs-import.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-jobs-import.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/jobs/import/`jobId``

**`mobiletargeting:GetImportJobs`**

Retrieve information about all the import jobs for a project.

- URI – [`/apps/`projectId`/jobs/import`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-jobs-import.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-jobs-import.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId``

### Journeys

The following permissions are related to managing journeys in your Amazon Pinpoint
account.

**`mobiletargeting:CreateJourney`**

Create a journey for a project.

- URI – [`/apps/`projectId`/journeys`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-journeys.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-journeys.html")
- Method – POST
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/journeys`

**`mobiletargeting:GetJourney`**

Retrieve information about a specific journey.

- URI – [`/apps/`projectId`/journeys/`journeyId``](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-journeys-journey-id.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-journeys-journey-id.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/journeys/`journeyId``

**`mobiletargeting:ListJourneys`**

Retrieve information about all the journeys for a project.

- URI – [`/apps/`projectId`/journeys`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-journeys.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-journeys.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/journeys`

**`mobiletargeting:UpdateJourney`**

Update the configuration and other settings for a specific
journey.

- URI – [`/apps/`projectId`/journeys/`journeyId``](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-journeys-journey-id.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-journeys-journey-id.html")
- Method – PUT
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/journeys/`journeyId``

**`mobiletargeting:UpdateJourneyState`**

Cancel an active journey.

- URI – [`/apps/`projectId`/journeys/`journeyId`/state`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-journeys-journey-id-state.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-journeys-journey-id-state.html")
- Method – PUT
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/journeys/`journeyId`/state`

**`mobiletargeting:DeleteJourney`**

Delete a specific journey.

- URI – [`/apps/`projectId`/journeys/`journeyId``](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-journeys-journey-id.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-journeys-journey-id.html")
- Method – DELETE
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/journeys/`journeyId``

### Message

templates

The following permissions are related to creating and managing message templates
for your Amazon Pinpoint account. A _message template_ is a
set of content and settings that you can define, save, and reuse in messages that
you send for any of your Amazon Pinpoint projects.

**`mobiletargeting:ListTemplates`**

Retrieve information about all the message templates that are
associated with your Amazon Pinpoint account.

- URI – [`/templates`](https://docs.aws.amazon.compinpoint/latest/apireference/templates.html "https://docs.aws.amazon.compinpoint/latest/apireference/templates.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:templates`

**`mobiletargeting:ListTemplateVersions`**

Retrieve information about all the versions of a specific message
template.

- URI – [`/templates/`template-name`/`template-type`/versions`](https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-template-type-versions.html "https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-template-type-versions.html")
- Method – GET
- Resource ARN – Not applicable

**`mobiletargeting:UpdateTemplateActiveVersion`**

Designate a specific version of a message template as the active
version of the template.

- URI – [`/templates/`template-name`/`template-type`/active-version`](https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-template-type-active-version.html "https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-template-type-active-version.html")
- Method – GET
- Resource ARN – Not applicable

**`mobiletargeting:GetEmailTemplate`**

Retrieve information about a message template for messages that are
sent through the email channel.

- URI – [`/templates/`template-name`/email`](https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-email.html "https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-email.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:templates/`template-name`/EMAIL`

**`mobiletargeting:CreateEmailTemplate`**

Create a message template for messages that are sent through the email
channel.

- URI – [`/templates/`template-name`/email`](https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-email.html "https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-email.html")
- Method – POST
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:templates/`template-name`/EMAIL`

**`mobiletargeting:UpdateEmailTemplate`**

Update an existing message template for messages that are sent through
the email channel.

- URI – [`/templates/`template-name`/email`](https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-email.html "https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-email.html")
- Method – PUT
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:templates/`template-name`/EMAIL`

**`mobiletargeting:DeleteEmailTemplate`**

Delete a message template for messages that were sent through the
email channel.

- URI – [`/templates/`template-name`/email`](https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-email.html "https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-email.html")
- Method – DELETE
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:templates/`template-name`/EMAIL`

**`mobiletargeting:GetPushTemplate`**

Retrieve information about a message template for messages that are
sent through a push notification channel.

- URI – [`/templates/`template-name`/push`](https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-push.html "https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-push.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:templates/`template-name`/PUSH`

**`mobiletargeting:CreatePushTemplate`**

Create a message template for messages that are sent through a push
notification channel.

- URI – [`/templates/`template-name`/push`](https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-push.html "https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-push.html")
- Method – POST
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:templates/`template-name`/PUSH`

**`mobiletargeting:UpdatePushTemplate`**

Update an existing message template for messages that are sent through
a push notification channel.

- URI – [`/templates/`template-name`/push`](https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-push.html "https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-push.html")
- Method – PUT
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:templates/`template-name`/PUSH`

**`mobiletargeting:DeletePushTemplate`**

Delete a message template for messages that were sent through a push
notification channel.

- URI – [`/templates/`template-name`/push`](https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-push.html "https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-push.html")
- Method – DELETE
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:templates/`template-name`/PUSH`

**`mobiletargeting:GetSmsTemplate`**

Retrieve information about a message template for messages that are
sent through the SMS channel.

- URI – [`/templates/`template-name`/sms`](https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-sms.html "https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-sms.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:templates/`template-name`/SMS`

**`mobiletargeting:CreateSmsTemplate`**

Create a message template for messages that are sent through the SMS
channel.

- URI – [`/templates/`template-name`/sms`](https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-sms.html "https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-sms.html")
- Method – POST
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:templates/`template-name`/SMS`

**`mobiletargeting:UpdateSmsTemplate`**

Update an existing message template for messages that are sent through
the SMS channel.

- URI – [`/templates/`template-name`/sms`](https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-sms.html "https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-sms.html")
- Method – PUT
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:templates/`template-name`/SMS`

**`mobiletargeting:DeleteSmsTemplate`**

Delete a message template for messages that were sent through the SMS
channel.

- URI – [`/templates/`template-name`/sms`](https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-sms.html "https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-sms.html")
- Method – DELETE
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:templates/`template-name`/SMS`

**`mobiletargeting:GetVoiceTemplate`**

Retrieve information about a message template for messages that are
sent through the voice channel.

- URI – [`/templates/`template-name`/voice`](https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-voice.html "https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-voice.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:templates/`template-name`/VOICE`

**`mobiletargeting:CreateVoiceTemplate`**

Create a message template for messages that are sent through the voice
channel.

- URI – [`/templates/`template-name`/voice`](https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-voice.html "https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-voice.html")
- Method – POST
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:templates/`template-name`/VOICE`

**`mobiletargeting:UpdateVoiceTemplate`**

Update an existing message template for messages that are sent through
the voice channel.

- URI – [`/templates/`template-name`/voice`](https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-voice.html "https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-voice.html")
- Method – PUT
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:templates/`template-name`/VOICE`

**`mobiletargeting:DeleteVoiceTemplate`**

Delete a message template for messages that were sent through the
voice channel.

- URI – [`/templates/`template-name`/voice`](https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-voice.html "https://docs.aws.amazon.compinpoint/latest/apireference/templates-template-name-voice.html")
- Method – DELETE
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:templates/`template-name`/VOICE`

### Messages

The following permissions are related to sending messages and push notifications
from your Amazon Pinpoint account. You can use the `SendMessages` and
`SendUsersMessages` operations to send messages to specific endpoints
without creating segments and campaigns first.

**`mobiletargeting:SendMessages`**

Send a message or push notification to specific endpoints.

- URI – [`/apps/`projectId`/messages`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-messages.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-messages.html")
- Method – POST
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/messages`

**`mobiletargeting:SendUsersMessages`**

Send a message or push notification to all the endpoints that are
associated with a specific user ID.

- URI – [`/apps/`projectId`/users-messages`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-users-messages.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-users-messages.html")
- Method – POST
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/messages`

### One-time passwords

The following permissions are related to sending and validating one-time passwords
(OTPs) in Amazon Pinpoint.

**`mobiletargeting:SendOTPMessage`**

Send a text message that contains a one-time password.

- URI – [`/apps/`projectId`/otp`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-otp.html#apps-application-id-otppost "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-otp.html#apps-application-id-otppost")
- Method – POST
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/otp`

**`mobiletargeting:VerifyOTPMessage`**

Check the validity of a one-time password (OTP) that was generated
using the SendOTPMessage operation.

- URI – [`/apps/`projectId`/verify-otp`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-verify-otp.html#apps-application-id-verify-otppost "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-verify-otp.html#apps-application-id-verify-otppost")
- Method – POST
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/verify-otp`

### Phone number

validation

The following permissions are related to using the phone number validation service
in Amazon Pinpoint.

**`mobiletargeting:PhoneNumberValidate`**

Retrieve information about a phone number.

- URI – [`/phone/number/validate`](https://docs.aws.amazon.compinpoint/latest/apireference/phone-number-validate.html "https://docs.aws.amazon.compinpoint/latest/apireference/phone-number-validate.html")
- Method – POST
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:phone/number/validate`

### Projects

The following permissions are related to managing projects in your Amazon Pinpoint account.
Originally, projects were referred to as _applications_. For the
purposes of these operations, an Amazon Pinpoint application is the same as an Amazon Pinpoint
project.

**`mobiletargeting:CreateApp`**

Create an Amazon Pinpoint project.

- URI – [`/apps`](https://docs.aws.amazon.compinpoint/latest/apireference/apps.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps.html")
- Method – POST
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps`

**`mobiletargeting:DeleteApp`**

Delete an Amazon Pinpoint project.

- URI – [`/apps/`projectId``](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id.html")
- Method – DELETE
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId``

**`mobiletargeting:GetApp`**

Retrieve information about an Amazon Pinpoint project.

- URI – [`/apps/`projectId``](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId``

**`mobiletargeting:GetApps`**

Retrieve information about all the projects that are associated with
your Amazon Pinpoint account.

- URI – [`/apps`](https://docs.aws.amazon.compinpoint/latest/apireference/apps.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps`

**`mobiletargeting:GetApplicationSettings`**

Retrieve the default settings for an Amazon Pinpoint project.

- URI – [`/apps/`projectId`/settings`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-settings.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-settings.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId``

**`mobiletargeting:UpdateApplicationSettings`**

Update the default settings for an Amazon Pinpoint project.

- URI – [`/apps/`projectId`/settings`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-settings.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-settings.html")
- Method – PUT
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId``

### Recommender

models

The following permissions are related to managing Amazon Pinpoint configurations for
retrieving and processing recommendation data from recommender models. A _recommender model_ is a type of machine learning model
that predicts and generates personalized recommendations by finding patterns in
data.

**`mobiletargeting:CreateRecommenderConfiguration`**

Create an Amazon Pinpoint configuration for a recommender model.

- URI – [`/recommenders`](https://docs.aws.amazon.compinpoint/latest/apireference/recommenders.html "https://docs.aws.amazon.compinpoint/latest/apireference/recommenders.html")
- Method – POST
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:recommenders`

**`mobiletargeting:GetRecommenderConfigurations`**

Retrieve information about all the recommender model configurations
that are associated with your Amazon Pinpoint account.

- URI – [`/recommenders`](https://docs.aws.amazon.compinpoint/latest/apireference/recommenders.html "https://docs.aws.amazon.compinpoint/latest/apireference/recommenders.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:recommenders`

**`mobiletargeting:GetRecommenderConfiguration`**

Retrieve information about an individual Amazon Pinpoint configuration for a
recommender model.

- URI – [`/recommenders/`recommenderId``](https://docs.aws.amazon.compinpoint/latest/apireference/recommenders-recommender-id.html "https://docs.aws.amazon.compinpoint/latest/apireference/recommenders-recommender-id.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:recommenders/`recommenderId``

**`mobiletargeting:UpdateRecommenderConfiguration`**

Update an Amazon Pinpoint configuration for a recommender model.

- URI – [`/recommenders/`recommenderId``](https://docs.aws.amazon.compinpoint/latest/apireference/recommenders-recommender-id.html "https://docs.aws.amazon.compinpoint/latest/apireference/recommenders-recommender-id.html")
- Method – PUT
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:recommenders/`recommenderId``

**`mobiletargeting:DeleteRecommenderConfiguration`**

Delete an Amazon Pinpoint configuration for a recommender model.

- URI – [`/recommenders/`recommenderId``](https://docs.aws.amazon.compinpoint/latest/apireference/recommenders-recommender-id.html "https://docs.aws.amazon.compinpoint/latest/apireference/recommenders-recommender-id.html")
- Method – DELETE
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:recommenders/`recommenderId``

### Segments

The following permissions are related to managing segments in your Amazon Pinpoint account.
In Amazon Pinpoint, _segments_ are groups of recipients for your campaigns
that share certain attributes that you define.

**`mobiletargeting:CreateSegment`**

Create a segment. To allow a user to create a segment by importing
endpoint data from outside Amazon Pinpoint, allow the
`mobiletargeting:CreateImportJob` action.

- URI – [`/apps/`projectId`/segments`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-segments.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-segments.html")
- Method – POST
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId``

**`mobiletargeting:DeleteSegment`**

Delete a segment.

- URI – [`/apps/`projectId`/segments/`segmentId``](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-segments.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-segments.html")
- Method – DELETE
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/segments/`segmentId``

**`mobiletargeting:GetSegment`**

Retrieve information about a specific segment.

- URI – [`/apps/`projectId`/segments/`segmentId``](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-segments.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-segments.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/segments/`segmentId``

**`mobiletargeting:GetSegmentExportJobs`**

Retrieve information about jobs that export endpoint definitions for a
segment.

- URI – [`/apps/`projectId`/segments/`segmentId`/jobs/export`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-segments-segment-id-jobs-export.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-segments-segment-id-jobs-export.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/segments/`segmentId`/jobs/export`

**`mobiletargeting:GetSegments`**

Retrieve information about all the segments for a project.

- URI – [`/apps/`projectId`/segments`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-segments.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-segments.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId``

**`mobiletargeting:GetSegmentImportJobs`**

Retrieve information about jobs that create segments by importing
endpoint definitions from Amazon S3.

- URI – [`/apps/`projectId`/segments/`segmentId`/jobs/import`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-segments-segment-id-jobs-import.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-segments-segment-id-jobs-import.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/segments/`segmentId``

**`mobiletargeting:GetSegmentVersion`**

Retrieve information about a specific segment version.

- URI – [`/apps/`projectId`/segments/`segmentId`/versions/`versionId``](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-segments-segment-id-versions-version.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-segments-segment-id-versions-version.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/segments/`segmentId``

**`mobiletargeting:GetSegmentVersions`**

Retrieve information about the current and prior versions of a
segment.

- URI – [`/apps/`projectId`/segments/`segmentId`/versions`](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-segments-segment-id-versions.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-segments-segment-id-versions.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/segments/`segmentId``

**`mobiletargeting:UpdateSegment`**

Update a specific segment.

- URI – [`/apps/`projectId`/segments/`segmentId``](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-segments-segment-id.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-segments-segment-id.html")
- Method – PUT
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/segments/`segmentId``

### Tags

The following permissions are related to viewing and managing tags for Amazon Pinpoint
resources.

**`mobiletargeting:ListTagsForResource`**

Retrieve information about the tags that are associated with a
project, campaign, message template, or segment.

- URI – [`/tags/`resource-arn``](https://docs.aws.amazon.compinpoint/latest/apireference/tags-resource-arn.html "https://docs.aws.amazon.compinpoint/latest/apireference/tags-resource-arn.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:*`

**`mobiletargeting:TagResource`**

Add one or more tags to a project, campaign, message template, or
segment.

- URI – [`/tags/`resource-arn``](https://docs.aws.amazon.compinpoint/latest/apireference/tags-resource-arn.html "https://docs.aws.amazon.compinpoint/latest/apireference/tags-resource-arn.html")
- Method – POST
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:*`

**`mobiletargeting:UntagResource`**

Remove one or more tags from a project, campaign, message template, or
segment.

- URI – [`/tags/`resource-arn``](https://docs.aws.amazon.compinpoint/latest/apireference/tags-resource-arn.html "https://docs.aws.amazon.compinpoint/latest/apireference/tags-resource-arn.html")
- Method – DELETE
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:*`

### Users

The following permissions are related to managing users. In Amazon Pinpoint,
_users_ correspond to individuals who receive messages from
you. A single user might be associated with more than one endpoint.

**`mobiletargeting:DeleteUserEndpoints`**

Delete all the endpoints that are associated with a user ID.

- URI – [`/apps/`projectId`/users/`userId``](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-users-user-id.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-users-user-id.html")
- Method – DELETE
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/users/`userId``

**`mobiletargeting:GetUserEndpoints`**

Retrieve information about all the endpoints that are associated with
a user ID.

- URI – [`/apps/`projectId`/users/`userId``](https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-users-user-id.html "https://docs.aws.amazon.compinpoint/latest/apireference/apps-application-id-users-user-id.html")
- Method – GET
- Resource ARN –
  `arn:aws:mobiletargeting:`region`:`accountId`:apps/`projectId`/users/`userId``

## Amazon Pinpoint SMS and voice version 1

API actions

This section identifies actions for features that are available from the
Amazon Pinpoint SMS and Voice API. This is a supplemental API that provides advanced options for using
and managing the SMS and voice channels in Amazon Pinpoint. To learn more about this API, see the
[Amazon Pinpoint SMS and voice API
reference](../../../pinpoint-sms-voice/latest/APIReference.md "../../../pinpoint-sms-voice/latest/APIReference.md").

**`sms-voice:CreateConfigurationSet`**

Create a configuration set for sending voice messages.

- URI – `/sms-voice/configuration-sets`
- Method – POST
- Resource ARN – Not available. Use `*`.

**`sms-voice:DeleteConfigurationSet`**

Delete a configuration set for sending voice messages.

- URI –
  /sms-voice/configuration-sets/`ConfigurationSetName`
- Method – DELETE
- Resource ARN – Not available. Use `*`.

**`sms-voice:GetConfigurationSetEventDestinations`**

Retrieve information about a configuration set and the event destinations
that it contains.

- URI –
  /sms-voice/configuration-sets/`ConfigurationSetName`/event-destinations
- Method – GET
- Resource ARN – Not available. Use `*`.

**`sms-voice:CreateConfigurationSetEventDestination`**

Create an event destination for voice events.

- URI –
  /sms-voice/configuration-sets/`ConfigurationSetName`/event-destinations
- Method – POST
- Resource ARN – Not available. Use `*`.

**`sms-voice:UpdateConfigurationSetEventDestination`**

Update an event destination for voice events.

- URI –
  /sms-voice/configuration-sets/`ConfigurationSetName`/event-destinations/`EventDestinationName`
- Method – PUT
- Resource ARN – Not available. Use `*`.

**`sms-voice:DeleteConfigurationSetEventDestination`**

Delete an event destination for voice events.

- URI –
  /sms-voice/configuration-sets/`ConfigurationSetName`/event-destinations/`EventDestinationName`
- Method – DELETE
- Resource ARN – Not available. Use `*`.

**`sms-voice:SendVoiceMessage`**

Create and send voice messages.

- URI – /sms-voice/voice/message
- Method – POST
- Resource ARN – Not available. Use `*`.
