

# Connect Customer service quotas
<a name="amazon-connect-service-limits"></a>

**Note**  
End of support notice: On May 20, 2026, AWS will end support for Amazon Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Amazon Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [Amazon Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html). 

**All service quotas can be adjusted unless otherwise noted.**

Your AWS account has default quotas, formerly referred to as limits, for each AWS service. 

To request a quota increase, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*.

**Topics**
+ [Important things to know](#important-quota-info)
+ [Connect Customer quotas](#connect-quotas)
+ [AppIntegrations quotas](#app-integration-quotas)
+ [agent assist quotas](#connect-ai-agents-quotas)
+ [Cases quotas](#cases-quotas)
+ [Conversational analytics quotas](#contactlens-quotas)
+ [Customer Profiles quotas](#customer-profiles-quotas)
+ [Outbound campaigns quotas](#outbound-communications-quotas)
+ [Voice ID quotas](#voiceid-quotas)
+ [How contacts are counted](#contact-counting-criteria)
+ [Plan ahead with quotas](plan-ahead-quotas.md)
+ [Feature specifications](feature-limits.md)
+ [Countries that call centers using Connect Customer can call by default](country-code-allow-list.md)
+ [API throttling quotas](#api-throttling-quotas)

## Important things to know
<a name="important-quota-info"></a>
+ You must create your instance before you can request a service quota increase.
+ We recommend you [plan for quota changes](plan-ahead-quotas.md). This will help support the lifecyle of your contact center.
+ We review each request for a quota increase. For smaller increase requests, we can approve in hours. Larger increase requests take time to review, process, approve, and deploy. Depending on your specific implementation, your resource, and the size of quota that you want, a request can take up to 3 weeks. An extra-large worldwide increase can potentially take months. If you're increasing your quotas as part of a larger project, keep this information in mind and [plan accordingly](plan-ahead-quotas.md). 
+ There are two types of quota adjustability: account level and resource-level.
  + Account level quotas, when adjusted, apply to all Connect Customer instances in this account and Region. For example, the maximum transactions per second (TPS) limits for a specific API.
  + Resource level quotas, when adjusted, only apply to resources within a specific Connect Customer instance. For example, the maximum number of users per instance. Resource level quotas cannot be adjusted at the account level.
+ The quotas apply per [AWS Region](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html#intro_getting-started). You can have multiple Connect Customer instances in each Region. It's possible to raise quotas for all instances in a Region.
+ Default quota values in this documentation are specifically for new accounts. Because quota defaults have been adjusted over time, the default and applied quota values for your account might be lower than the default values described in this topic. 
+ Not all quotas can be adjusted.
+ You need AWS CLI version 2.13.20 or higher to view and manage resource-level quotas such as **Phone numbers per instance** for Connect Customer.
+ Use the same form to submit a request to port your US phone number from your current carrier to Connect Customer. For more information about porting phone numbers, see [Port a current phone number to Connect Customer](port-phone-number.md).

## Connect Customer quotas
<a name="connect-quotas"></a>


| Name | Default | Adjustable | Adjustability | 
| --- | --- | --- | --- | 
| Active email contact expiry | 14 days (Default)<br />Customizable up to 90 days using the [Flow block in Connect Customer: Set contact attributes](set-contact-attributes.md) flow block or [Expiry](https://docs.aws.amazon.com/connect/latest/APIReference/API_Expiry.html) API to update the connect:ContactExpiry [segment attribute](connect-attrib-list.md#attribs-segment-attributes).<br />This determines how long an email contact can remain active (for example, waiting in queue or assigned to an agent) before expiring and closing automatically. "No" for adjustability means that you cannot customize or increase this attribute to be greater than 90 days. | No | Resource Level | 
| Active email conversation (thread) expiry | 90 days<br />Meaning if an end customer (using their email client) or an agent (using their agent application) replies to an email as part of an ongoing conversation (thread) within 90 days, the email reply will automatically be included within that same [email conversation (thread)](email-capabilities.md#email-capabilities-howthreadsmanaged) in Connect Customer. If they reply after 90 days, it will start a new [email conversation (thread)](email-capabilities.md#email-capabilities-howthreadsmanaged) in Connect Customer. | No | Resource Level | 
| AWS Lambda functions per instance | 50 | Yes | Resource Level | 
| Agent status per instance | 50 | No | Not Adjustable | 
| Connect Customer instances per Region | 2 | Yes | Account Level | 
| Amazon Lex bots per instance | 70 | No | Resource Level | 
| Amazon Lex V2 bot aliases per instance | 100 | Yes  | Resource Level | 
| Concurrent active calls per instance | 10<br />This includes PSTN and WebRTC calls.<br />For more information, see [How contacts are counted](#contact-counting-criteria). | Yes | Resource Level | 
| Concurrent active chats per instance | 500<br />This includes SMS, WhatsApp, and Apple Messages for Business. It also includes chats that are waiting.<br />If the customer has initiated a chat and has gone silent for hours, this idle chat is counted against the quota. To avoid having idle chats count against your quota, we recommend using [persistent chats](chat-persistence.md). <br />If this quota is exceeded, the API call fails with a quota exceeded error. | Yes | Resource Level | 
| Concurrent active emails per instance | 1000 (Default)<br />This is the total of all email contacts in a Connect Customer instance in an active state. An email contact in an active state includes:+  emails that are currently executing through a flow <br />+  emails waiting in queue waiting to be assigned <br />+  emails assigned to agents (either actively being worked on or in ACW state) <br />+  email replies or agent-initiated emails being composed by agents or automated services <br />Example: 200 emails in queue \+ 10 emails assigned to 10 agents \+ 5 outbound emails being sent by an agent (either a reply or agent-initiated) = 215 Concurrent active emails in the instance<br />This service limit should be monitored by the [Connect Customer metrics sent to CloudWatch](monitoring-cloudwatch.md#connect-metrics-cloudwatch) using ConcurrentEmails and ConcurrentEmailsPercentage to ensure adequate scaling of your Connect Customer instance. If this quota is exceeded by your Connect Customer instance, Email API calls will fail with a quota exceeded error. We recommend following the Connect Customer [ongoing operations management](plan-ahead-quotas.md#production-environment-go-live-quotas) approach of configuring alerts at 80% of quota limits to notify you when to [request a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html). | Yes | Resource Level | 
| Concurrent active tasks per instance | 2500 concurrent active tasks<br />All tasks that have not yet ended are considered active and are counted as concurrent tasks: tasks that are being routed in flows, waiting in a queue for an agent, being handled by agents, or being run in After Contact Work (ACW). | Yes | Resource Level | 
| Custom Metrics per instance  | 1000 | No | Resource Level | 
| Data tables per instance | 100 | Yes | Resource Level | 
| Primary attributes per data table | 5 | No | Not Adjustable | 
| Attributes per data table | 100 | No | Not Adjustable | 
| Values per data table | 1000 | Yes | Resource Level | 
| Email addresses per instance | 100 email addresses (Default)<br />Can be increased up to 500 email addresses per instance. | Yes | Resource Level | 
| Email addresses per email (contact) message | 50 email addresses per email contact (message) total across To and CC.<br />Inbound email contacts (messages) support any combination of 50 email addresses total across To and CC.<br />Outbound email contacts (messages) support only 1 email address in To and up to 49 email addresses in CC.<br />BCC email addresses are not supported in Connect Customer. | No | Not Adjustable | 
| Email domains per instance | 1 Connect Customer email domain<br />100 custom email domains | No | Resource Level | 
| Maximum individual attachments size | 20 MB (configurable up to 100 MB) Administrators can configure up to 100 MB through the Connect Customer admin website or the Connect Customer API.  | Yes | Resource Level | 
| Flows per instance | 100 | Yes | Resource Level | 
| Hours of operation per instance | 100 | Yes | Resource Level | 
| Overrides per hours of operation | 50 | No | Not Adjustable | 
| Associations to inherit recurring overrides per hours of operation | 3 | No | Not Adjustable | 
| Maximum duration that a task can be scheduled in future | 90 days | No | Not Adjustable | 
| Maximum number of reschedules allowed for a task scheduled for a future time | 20 | No | Not Adjustable | 
| Modules per instance | 200 | Yes | Resource Level | 
| Phone numbers per instance | 5<br />It's possible to get an error message that "You've reached the limit of Phone Numbers," even if it's the first time you've claimed a phone number. All the issues that cause this error message require help from Support to resolve. | Yes | Resource Level | 
| Predefined attributes per instance | 150 | Yes | Resource Level | 
| Proficiencies per agent | 10 | Yes | Resource Level | 
| Prompts per instance | 500 | Yes | Resource Level | 
| Queues per instance | 100 | Yes | Resource Level | 
| Maximum contacts in an agent queue per instance | 10<br />This quota applies to the maximum contacts you can have queued at once in a single [agent queue](concepts-queues-standard-and-agent.md). The same quota applies to every agent queue in your instance. | Yes | Resource Level | 
| Queues per routing profile per instance | 50<br />This quota refers to number of queue/channel combinations per routing profile. For example, in the following image there are two queues, but there are three queue-channel combinations: Escalation queue Voice, Escalation queue Chat, and BasicQueue Voice. This counts three towards the service quota of 50.<br />This same quota also applies to manually assigned queues; each of these two types of queue have up to this limit, independent of each other. For example, it's possible to have a max of 50 queue-channel combinations for queues and another 50 queue-channel combinations for manual assignment queues.![The Routing profiles page, the routing profiles queues section, voice and chat queues.](http://docs.aws.amazon.com/connect/latest/adminguide/images/routing-profile-queue-channel-combinations.png) | Yes | Resource Level | 
| Quick connects per instance | 100 | Yes | Resource Level | 
| Rate of API requests | See [Connect Customer API throttling quotas](#connect-api-quotas). | Yes | Account Level | 
| Reports per instance | 2,000<br />Personal saved reports count towards the reports per instance. For example, if one of your supervisors saves a report every day, it will count towards your overall number of saved reports per instance.<br />As a best practice, we recommend you implement policies so reports don't pile up.  | Yes | Resource Level | 
| Routing profiles per instance | 500 | Yes | Resource Level | 
| Scheduled reports per instance | 100 | Yes | Resource Level | 
| Security profiles per instance | 100 | Yes | Resource Level | 
| Task templates per instance | 50 | No | Not Adjustable | 
| Task template customized fields per template | 50 | No | Not Adjustable | 
| Theme detection reports generated within 30 minutes per instance | 6 | No | Resource Level | 
| User hierarchy groups per instance | 500<br />This quota applies to the total number of hierarchy groups you have, across all levels. There is no feature limit for how many hierarchy groups you can have for each level. For example, one level could have 500 hierarchy groups, which would reach the quota for your instance. | Yes | Resource Level | 
| Users per instance | 500<br />The maximum number of users you can create in this instance in the current Region. All 500 users can be logged into Connect Customer concurrently as agents and handling contacts. | Yes | Resource Level | 

## Connect Customer AppIntegrations service quotas
<a name="app-integration-quotas"></a>

All AppIntegrations quotas are at the Account level. 


| Name | Default | Adjustable | 
| --- | --- | --- | 
| Data integration associations per data integration | 10 | Yes | 
| Data integrations per Region | 20 | Yes | 
| Event integration associations per event integration | 10 | Yes | 
| Event integrations per Region | 10 | Yes | 
| Applications per Region | 50 | Yes | 

## Connect Customer agent assist service quotas
<a name="connect-ai-agents-quotas"></a>

All Amazon Q quotas are at the Account level. 

**Note**  
To request a quota adjustment, please contact [AWS Support](https://console.aws.amazon.com/support/home).


| Item | Default quotas  | Adjustable | 
| --- | --- | --- | 
| Assistants | 5 | No | 
| Knowledge bases | 10 | Yes | 
| Assistant associations | 20 | No | 
| Quick responses per knowledge base | 1,000 | Yes | 
| Content per knowledge base | 5,000<br />Examples of content are frequently asked questions (FAQs), wikis, articles, and step-by-step instructions for handling different customer issues. | Yes | 
| Maximum size per document | 5MB | Yes | 
| Number of message (email, SMS, WhatsApp) templates per knowledge base | 200 | Yes | 
| Number of versions per message (email, SMS, WhatsApp) template | 20 | No | 
| Number of attachments per email message template | 10 | No | 
| Maximum size per attachment in an email message template | 1 MB | No | 
| Maximum number of characters in an email message template | 5,000,000 | No | 
| Maximum number of characters in an SMS message template | 800 | No | 
| Number of assigned routing profiles per quick response or email template | 40 | No | 
| RateLimit for all APIs | 10 TPS except,+  DeleteQuickResponse 20 TPS <br />+  SearchQuickResponses 20 TPS <br />+  SendMessage 1-2 TPS, depending on region  | Yes | 

## Connect Customer Cases service quotas
<a name="cases-quotas"></a>

All the Cases quotas are at the Account level.


| Name | Default | Adjustable | 
| --- | --- | --- | 
| Cases domains per AWS account | 5 | Yes | 
| Fields in a Cases domain | 500 | Yes | 
| Field options per single-select field in the Cases domain | 500 | Yes | 
| Layouts in a Cases domain | 100 | Yes | 
| Templates in a Cases domain | 100 | Yes | 
| Related items that can be attached to a case | 200 | Yes | 
| Files that can be attached to a case | 50 | Yes | 
| Case fields per case layout | 100 | No | 
|  SLAs that can be attached to a case | 10 | Yes | 
| Fields in a Custom type related item | 5 | Yes | 

## Conversational analytics service quotas
<a name="contactlens-quotas"></a>

All conversational analytics quotas are at the Account level. 


| Name | Default | Adjustable | 
| --- | --- | --- | 
| Concurrent real-time calls with analytics | 300 | Yes | 
| Concurrent post-call analytics jobs | 200<br /> See [Derive Concurrent post-call analytics jobs based on your Connect Customer call volume](#contactlens-concurrent-analytics-jobs).  | Yes | 
| Concurrent chat analytics jobs | 200 | Yes | 
| Concurrent automated interaction analytics jobs | 20 | Yes | 
| Concurrent post-contact agent conversation summary jobs (shared between all supported channels - voice, chat) | 10 | Yes | 
| Concurrent post-contact automated interaction summary jobs (shared between all supported channels - voice, chat) | 2 | Yes | 
| Concurrent after-call agent conversation summary jobs (shared between all supported channels - voice, chat) | 2 | Yes | 
| External voice analytics connectors | 0 | Yes | 
| Maximum active recording sessions from external voice systems per instance | 10 | Yes | 
| Number of evaluation questions answered with AI assistance on a single contact (manually initiated) | 30 | Yes\* | 
| Number of evaluation questions on a single contact completed automatically by generative AI (automated evaluations) | 15 | Yes\* | 
| Maximum number of evaluations (manual and automated) per contact | 10 | No | 

\*Through a support ticket. 

### Derive Concurrent post-call analytics jobs based on your Connect Customer call volume
<a name="contactlens-concurrent-analytics-jobs"></a>

A post-call analytics job is kicked off after the completion of each contact that has conversational analytics [enabled](enable-analytics.md) on it. The time to complete a post-call analytics job can vary, but for planning purposes, you can estimate that it usually takes about 40% of the call length. If you choose 40% for your estimate, to calculate concurrent post-call analytics jobs, you would use the following formula: 

`(average call duration in minutes) * (0.4) * (calls per hour) / (60)`

The following table shows some examples of what the approximate number of concurrent post call jobs would be if you assume the time to complete the analysis is 40%. 


| Average call duration (in minutes) | Calls per hour\* | Approximate Concurrent post-call jobs | 
| --- | --- | --- | 
| 5 | 1000 | 33 | 
| 10 | 500 | 33 | 
| 10 | 1000 | 67 | 
| 10 | 3000 | 200 | 

\*For the example calculations in the preceding table, we assume a fairly uniform distribution of calls during the hour. If you have more complex traffic patterns, [contact Support](https://console.aws.amazon.com/support/home) with details about your anticipated traffic pattern.

## Connect Customer Customer Profiles service quotas
<a name="customer-profiles-quotas"></a>

All Customer Profiles quotas are at the Account level. 


| Name | Default | Adjustable | Description | 
| --- | --- | --- | --- | 
| Connect Customer Customer Profiles domain count | Each supported Region: 100 |  Yes  | The maximum number of Connect Customer Customer Profiles domains you can create in this account in the current AWS Region. | 
| Keys per object type | Each supported Region: 10 |  Yes  | The maximum number of keys that can be defined per object type in the current AWS Region. | 
| Maximum expiration in days | Each supported Region: 1,098 |  Yes  | The maximum expiration, in days, that can be defined for an object or profile in the current AWS Region. | 
| Maximum number of calculated attributes per domain | Each supported Region: 50 | No | The maximum number of calculated attributes per domain in the current AWS Region. | 
| Maximum number of event stream per domain | Each supported Region: 1 | No | The maximum number of event streams per domain in the current AWS Region. | 
| Maximum number of event triggers per domain | Each supported Region: 50 | Yes | The maximum number of event triggers per domain in the current AWS Region. | 
| Maximum number of integrations | Each supported Region: 50 |  Yes  | The maximum number of integrations per domain in the current AWS Region. | 
| Maximum number of segment snapshots per day | Each supported Region: 200 |  Yes  | The maximum number of segment snapshots per domain in the current AWS Region. | 
| Maximum size of all objects for a profile | Each supported Region: 51,200 Kilobytes |  Yes  | The total size of a profile, including all of its related objects, in the current AWS Region. | 
| Object and profile maximum size | Each supported Region: 250 Kilobytes | No | The maximum size of a single profile or profile object in the current AWS Region. | 
| Object types per domain | Each supported Region: 100 |  Yes  | The maximum number of object types you can define per domain in the current AWS Region. | 
| Objects per profile | Each supported Region: 1,000 |  Yes  | The maximum number of objects that can be attached to a single profile in the current AWS Region. | 
| Concurrent bulk export jobs | 20 |  No  | The maximum number of concurrent bulk export jobs per AWS Region per account. After a bulk export job completes or fails, it no longer counts towards the concurrency quota. | 

## Connect Customer Outbound campaigns service quotas
<a name="outbound-communications-quotas"></a>

All outbound campaigns quotas are at the Account level. 


| Name | Default | Adjustable | Adjustability | 
| --- | --- | --- | --- | 
| Active campaigns per instance | 50<br />The maximum number of active campaigns that an AWS account can configure per Connect Customer instance. | Yes | Account Level | 
| Total campaigns per instance | 500<br />The maximum total number of campaigns that an AWS account can configure per Connect Customer instance. | Yes | Account Level | 
| Concurrent campaign active calls per instance | 0<br />The maximum number of concurrent campaign active calls you can have in this instance in the current Region. If this is exceeded, contacts will get a fast busy tone, which indicates the transmission path to the called number is not available.  | Yes | Resource Level | 

## Connect Customer Voice ID service quotas
<a name="voiceid-quotas"></a>

All Voice ID quotas are at the Account level. 


| Item | Default quotas  | 
| --- | --- | 
| Domains | 3<br />This quota applies per account. | 
| Concurrent active sessions per domain | 50<br />See the following [table](#voiceid-concurrent-active-sessions) for information about how to derive your **Concurrent active sessions** quota based on your Connect Customer call volume. | 
| Maximum number of fraudsters per watchlist | 500 | 
| Maximum number of watchlists per domain | 3, including the default watchlist of a domain | 
| Maximum number of speakers per domain | 100,000 | 
| Active Batch Speaker Enrollment Jobs per domain | 1 | 
| Active Batch Fraudster Registration Jobs per domain | 1 | 
| Speakers per Batch Speaker Enrollment Job | 10,000 | 
| Fraudsters per Batch Fraudster Registration Job | 500 | 

### Derive Concurrent active sessions based on your Connect Customer call volume
<a name="voiceid-concurrent-active-sessions"></a>

Use the information in the following table to derive your quota for Voice ID **Concurrent active sessions per domain**. Base your quota on the number of voice calls handled by your Connect Customer contact center where Voice ID is enabled.


| Connect Customer Voice Contacts (Calls)/Hour\* | Voice ID Concurrent active sessions | 
| --- | --- | 
| 1,000 | 50 | 
| 5,000 | 250 | 
| 10,000 | 500 | 
| 20,000 | 1,000 | 
| 50,000 | 2,500 | 

\*For the calculations in the preceding table, we assume a fairly uniform distribution of calls during the hour. If you have more complex traffic patterns, [contact Support](https://console.aws.amazon.com/support/home) with details about your anticipated traffic pattern.

## How contacts are counted
<a name="contact-counting-criteria"></a>

The following contacts are counted in **Concurrent active calls per instance**:
+ Handled by a flow
+ Waiting in queue
+ Handled by an agent
+ Outbound call

The following contacts are not counted:
+ Callbacks waiting in a callback queue are not counted until the callback is offered to an available agent.
+ External transfers

If the quota for **Concurrent active calls per instance** is exceeded, contacts get a reorder tone (also known as a fast busy tone), which indicates that there is no available transmission path to the called number.

You can calculate your configured quota using CloudWatch metrics. For instructions, see [Use CloudWatch metrics to calculate concurrent call quota](monitoring-cloudwatch.md#connect-cloudwatch-concurrent-call-quota). 

If you're only taking calls you can also determine your **Concurrent active calls per instance** quota by doing the following:

1. Navigate to the **Edit a queue** page: choose **Routing**, **Queues**, and choose a queue.

1. Choose **Set a limit across all channels**. 

1. Enter an exceptionally large number in the **Maximum contacts in queue** box for the contact limit.

The resulting error message displays your quota as less than the sum of the following quotas combined: **Concurrent calls per instance** \+ **Concurrent active chats per instance** \+ **Concurrent active tasks per instance**. 

For example, in the following image from the **Edit queues** page, you add 1 to the error message, to get **Concurrent calls per instance** \+ **Concurrent active chats per instance** \+ **Concurrent active tasks per instance** quota = 3010.

![The edit queue page, Maximum contacts in queue.](http://docs.aws.amazon.com/connect/latest/adminguide/images/concurrent-call-quota.png)


The error message shows 3009 because you must set always set **Maximum contacts in queue** to a number that is at least 1 *less than* your combined quota (which is the default limit).

## API throttling quotas
<a name="api-throttling-quotas"></a>

### Connect Customer API throttling quotas
<a name="connect-api-quotas"></a>

Connect Customer throttling quotas are by account, and per Region, not by user and not by instance. For example: 
+ If different users from the same account make requests, they are sharing a throttle bucket. 
+ If multiple requests are sent from different instances from the same account, they are also sharing a throttle bucket. 

 When you use the [Connect Customer Service API](https://docs.aws.amazon.com/connect/latest/APIReference/welcome.html), all operations have a `RateLimit` of 2 requests per second and a `BurstLimit` of 5 requests per second, **with the following exceptions**:


| Operation | Rate limit | Burst limit | 
| --- | --- | --- | 
| For all [Evaluations actions](https://docs.aws.amazon.com/connect/latest/APIReference/evaluation-api.html) | 3 | 5 | 
| \*[GetMetricData ](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetMetricData.html) | 5 | 8 | 
| \*[GetMetricDataV2 ](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetMetricDataV2.html) | 10 | 10 | 
| \*[GetCurrentMetricData](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetCurrentMetricData.html) | 5 | 8 | 
| [SearchContacts](https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchContacts.html) | .5 | 1 | 
| [StartContactStreaming](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartContactStreaming.html) | 5 | 8 | 
| [StartChatContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartChatContact.html) | 5 | 8 | 
| [CreatePersistentContactAssociation](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreatePersistentContactAssociation.html) | 5 | 8 | 
| [UpdateParticipantRoleConfig](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateParticipantRoleConfig.html) | 5 | 8 | 
| [StopContactStreaming](https://docs.aws.amazon.com/connect/latest/APIReference/API_StopContactStreaming.html) | 5 | 8 | 
| [CreateParticipant](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateParticipant.html) | 5 | 8 | 
| [GetContactAttributes](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetContactAttributes.html) | 10 | 15 | 
| [UpdateContactAttributes ](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateContactAttributes .html) | 10 | 15 | 
| [DescribeContact ](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeContact .html) | 10 | 15 | 
| [StopContact ](https://docs.aws.amazon.com/connect/latest/APIReference/API_StopContact .html) | 10 | 15 | 
| [UpdateContact ](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateContact .html) | 10 | 15 | 
| [ListContactReferences ](https://docs.aws.amazon.com/connect/latest/APIReference/API_ListContactReferences .html) | 10 | 15 | 
| [BatchPutContact ](https://docs.aws.amazon.com/connect/latest/APIReference/API_BatchPutContact .html) | 10 | 15 | 
| [TagContact ](https://docs.aws.amazon.com/connect/latest/APIReference/API_TagContact .html) | 20 | 25 | 
| [UntagContact ](https://docs.aws.amazon.com/connect/latest/APIReference/API_UntagContact .html) | 20 | 25 | 
| [UpdateContactRoutingData](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetContactAttributes.html) | 20 | 20 | 
| [SendChatIntegrationEvent](https://docs.aws.amazon.com/connect/latest/APIReference/API_SendChatIntegrationEvent) | 17 | 26 | 
| SendIntegrationEvent (this is a separate permission-only API used by AWS End User Messaging Social) | 10 | 15 | 
| [CreateIntegrationAssociation](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateIntegrationAssociation.html), [DeleteIntegrationAssociation](https://docs.aws.amazon.com/connect/latest/APIReference/API_DeleteIntegrationAssociation.html)  | 2<br />1 for the SES\_IDENTITY IntegrationType field | 5 | 
| [ListIntegrationAssociations](https://docs.aws.amazon.com/connect/latest/APIReference/API_ListIntegrationAssociations.html)  | 25 | 50 | 

**Important**  
\* [GetCurrentMetricData](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetCurrentMetricData.html), [GetMetricDataV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetMetricDataV2.html), and [GetCurrentUserData](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetCurrentUserData.html) might incorrectly display 200 as their throttling quota in the Service Quotas console. We recommend using the default quotas specified here, or opening a ticket.

### Connect Customer Cases API throttling quotas
<a name="cases-api-quotas"></a>


| API | Default Rate Limit | Default Burst Limit | Adjustable | 
| --- | --- | --- | --- | 
| CreateCase, SearchCases, ListTemplates, ListLayouts, CreateRelatedItems, SearchRelatedItems, ListCaseRules, ListTagsForResource, TagResource, UntagResource, GetCaseAuditEvents, GetCaseEventConfiguration, PutCaseEventConfiguration | 2 | 10 | yes | 
| GetCase | 4 | 10 | yes | 
| UpdateCase, ListCasesForContact | 2 | 2 | yes | 
| CreateField, ListFields, UpdateField, BatchPutFieldOptions, CreateDomain, GetDomain, ListDomains, CreateTemplate, UpdateTemplate, CreateLayout, UpdateLayout, CreateCaseRule, UpdateCaseRule, DeleteCaseRules | 2 | 5 | yes | 
| BatchGetField, BatchGetCaseRule | 8 | 25 | yes | 
| ListFieldOptions | 6 | 16 | yes | 
| GetTemplate, GetLayout | 6 | 20 | yes | 

### Connect Customer conversational analytics Service API throttling quotas
<a name="connect-contactlens-api-quotas"></a>

Connect Customer conversational analytics throttling quotas are by account, not by user and not by instance. For example:
+ If different users from the same account make requests, they are sharing a throttle bucket.
+ If multiple requests are sent from different instances from the same account, they are also sharing a throttle bucket. 

When you use the [Connect Customer conversational analytics API](https://docs.aws.amazon.com/contact-lens/latest/APIReference/Welcome.html), the number of requests per second is limited to the following:
+ [ListRealtimeContactAnalysisSegments](https://docs.aws.amazon.com/contact-lens/latest/APIReference/ListRealtimeContactAnalysisSegments.html): a `RateLimit` of 1 request per second, and a `BurstLimit` of 2 requests per second.
+ [ListRealtimeContactAnalysisSegmentsV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_ListRealtimeContactAnalysisSegmentsV2.html): a `RateLimit` of 2 request per second, and a `BurstLimit` of 5 requests per second. 

### Connect Customer Customer Profiles API throttling quotas
<a name="customer-profile-api-quotas"></a>


| API | Default TPS throttling limits | 
| --- | --- | 
| ListDomains | 5 | 
| GetDomain | 5 | 
| CreateDomain | 1 | 
| UpdateDomain | 1 | 
| DeleteDomain | 1 | 
| ListProfileObjectTypes | 5 | 
| GetProfileObjectType | 10 | 
| PutProfileObjectType | 1 | 
| DeleteProfileObjectType | 1 | 
| ListProfileObjectTypeTemplates | 5 | 
| GetProfileObjectTypeTemplate | 5 | 
| ListIntegrations | 5 | 
| GetIntegration | 5 | 
| PutIntegration | 1 | 
| DeleteIntegration | 1 | 
| ListIdentityResolutionJobs | 5 | 
| GetIdentityResolutionJob | 5 | 
| GetAutoMergingPreview | 1 | 
| CreateEventStream | 1 | 
| ListEventStreams | 5 | 
| DeleteEventStream | 5 | 
| GetEventStream | 5 | 
| CreateCalculatedAttributeDefinition | 1 | 
| GetCalculatedAttributeDefinition | 5 | 
| UpdateCalculatedAttributeDefinition | 1 | 
| DeleteCalculatedAttributeDefinition | 5 | 
| ListCalculatedAttributeDefinitions | 5 | 
| CreateIntegrationWorkflow | 5 | 
| DeleteWorkflow | 5 | 
| ListWorkflows | 5 | 
| GetWorkflow | 5 | 
| GetWorkflowSteps | 5 | 
| SearchProfiles | 100 | 
| ListProfileObjects | 100 | 
| GetMatches | 100 | 
| GetSimilarProfiles | 100 | 
| ListRuleBasedMatches | 5 | 
| GetCalculatedAttributeForProfile | 100 | 
| ListCalculatedAttributesForProfile | 100 | 
| CreateProfile | 100 | 
| UpdateProfile | 100 | 
| PutProfileObject | 100 | 
| AddProfileKey | 100 | 
| DeleteProfile | 100 | 
| DeleteProfileObject | 100 | 
| DeleteProfileKey | 100 | 
| MergeProfiles | 100 | 
| TagResource | 5 | 
| UntagResource | 5 | 
| ListTagsForResource | 5 | 
| ListAccountIntegrations | 100 | 

### Connect Customer Outbound Campaigns Service API throttling quotas
<a name="campaigns-api-quotas"></a>

Outbound campaigns throttling quotas are by account, and per Region, not by user and not by instance. For example: 
+ If different users from the same account make requests, they share a throttle bucket. 
+ If multiple requests are sent from different instances from the same account, they also share a throttle bucket. 

When you use the [Connect Customer Outbound Campaigns Service](https://docs.aws.amazon.com/connect/latest/APIReference/Welcome.html#Welcome_Amazon_Connect_Outbound_Campaigns) API, the number of requests per second is limited to the following:
+ The following APIs have a `RateLimit` of 1 request per second, and a `BurstLimit` of 2 requests per second:
  + [CreateCampaign](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_CreateCampaign.html)
  + [DeleteCampaign](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_DeleteCampaign.html)
  + [PauseCampaign](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_PauseCampaign.html)
  + [ResumeCampaign](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_ResumeCampaign.html)
  + [StartCampaign](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_StartCampaign.html)
  + [StopCampaign](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_StopCampaign.html)
  + [UpdateCampaignDialerConfig](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_UpdateCampaignDialerConfig.html)
  + [UpdateCampaignName](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_UpdateCampaignName.html)
  + [UpdateCampaignOutboundCallConfig](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_UpdateCampaignOutboundCallConfig.html)
  + [ListTagsForResource](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_ListTagsForResource.html)
  + [TagResource](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_TagResource.html)
  + [UntagResource](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_UntagResource.html)
+ The following APIs have a `RateLimit` of 5 requests per second, and a `BurstLimit` of 10 requests per second:
  + [GetCampaignState](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_GetCampaignState.html)
  + [GetCampaignStateBatch](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_GetCampaignStateBatch.html)
  + [ListCampaigns](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_ListCampaigns.html)
+ The following APIs have a RateLimit of 10 requests per second, and a BurstLimit of 10 requests per second:
  + [PutDialRequestBatch](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns_PutDialRequestBatch.html)
  + [PutOutboundRequestBatch](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_PutOutboundRequestBatch.html)
  + [PutProfileOutboundRequestBatch](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_PutProfileOutboundRequestBatch.html)
+ For [DescribeCampaign](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_DescribeCampaign.html) API, a `RateLimit` of 25 requests per second, and a `BurstLimit` of 35 requests per second.
+ For all other operations, a `RateLimit` of 2 requests per second, and a `BurstLimit` of 5 requests per second.

### Connect Customer Participant Service API throttling quotas
<a name="connect-participant-api-quotas"></a>

For the Connect Customer Participant Service, the quotas are by instance.

 When you use the [Connect Customer Participant Service API](https://docs.aws.amazon.com/connect-participant/latest/APIReference/Welcome.html), the number of requests per second is limited to the following:
+  [CompleteAttachmentUpload](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-participant_CompleteAttachmentUpload.html): a `RateLimit` of 2 requests per second, and a `BurstLimit` of 5 requests per second.
+  [CreateParticipantConnection](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-participant_CreateParticipantConnection.html): a `RateLimit` of 6 requests per second, and a `BurstLimit` of 9 requests per second.
+  [DisconnectParticipant](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-participant_DisconnectParticipant.html): a `RateLimit` of 3 requests per second, and a `BurstLimit` of 5 requests per second.
+  [GetAttachment](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-participant_GetAttachment.html): a `RateLimit` of 8 requests per second, and a `BurstLimit` of 12 requests per second.
+  [GetTranscript](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-participant_GetTranscript.html): a `RateLimit` of 8 requests per second, and a `BurstLimit` of 12 requests per second.
+  [SendEvent](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-participant_SendEvent.html) and [SendMessage](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-participant_SendMessage.html): a `RateLimit` of 10 requests per second, and a `BurstLimit` of 15 requests per second.
+  [StartAttachmentUpload](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-participant_StartAttachmentUpload.html): a `RateLimit` of 2 requests per second, and a `BurstLimit` of 5 requests per second.

### Connect Customer Voice ID Service API throttling quotas
<a name="voiceid-api-quotas"></a>


| API | Default TPS throttling limits | 
| --- | --- | 
| EvaluateSession | 60 | 
| Domain APIs: CreateDomain, DescribeDomain, UpdateDomain, DeleteDomain, ListDomains<br />Batch APIs: StartSpeakerEnrollmentJob, DescribeSpeakerEnrollmentJob, ListSpeakerEnrollmentJobs, StartFraudsterRegistrationJob, DescribeFraudsterRegistrationJob, ListFraudsterRegistrationJobs | 2 | 
| ListSpeakers | 5 | 
| DescribeSpeaker, OptOutSpeaker, DeleteSpeaker, DescribeFraudster, DeleteFraudster | 10 | 
| TagResource, UnTagResource, ListTagsForResource | 2 | 

### agent assist Service API throttling quotas
<a name="q-in-connect-api-quotas"></a>


| API | Default TPS throttling limits | 
| --- | --- | 
| DeleteMessageTemplate | 10 | 
| DeleteMessageTemplateAttachment | 10 | 
| GetMessageTemplate | 10 | 
| ListMessageTemplates | 10 | 
| ListMessageTemplateVersions | 10 | 
| RenderMessageTemplate | 10 | 
| SearchMessageTemplates | 10 | 
| ActivateMessageTemplate | 3 | 
| CreateMessageTemplate | 3 | 
| CreateMessageTemplateAttachment | 3 | 
| CreateMessageTemplateVersion | 3 | 
| UpdateMessageTemplate | 3 | 
| UpdateMessageTemplateMetadata | 3 | 
| DeactivateMessageTemplate | 3 | 