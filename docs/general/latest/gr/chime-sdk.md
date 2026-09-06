

# Amazon Chime SDK endpoints and quotas
<a name="chime-sdk"></a>

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints. Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md).

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account. For more information, see [AWS service quotas](aws_service_limits.md).

The following are the service endpoints and service quotas for this service.

**Contents**
+ [Service endpoints](#chime_sdk_region)
  + [Identity](#identity_endpoints)
  + [Media pipeline regional endpoints](#media_pipelines_endpoints)
  + [Messaging](#messaging_endpoints)
  + [Voice](#pstn_audio_endpoints)
  + [WebRTC media sessions](#web_rtc_media_sessions_endpoints)
  + [Legacy](#legacy_endpoints)
+ [Service quotas](#limits_chime_sdk)
  + [Amazon Chime SDK call analytics quotas](#analytics-quotas)
  + [Amazon Chime SDK Identity quotas](#chm-sdk-ident-quotas)
  + [Amazon Chime SDK Media Pipeline quotas](#media-pipeline-quotas)
  + [Amazon Chime SDK Messaging quotas](#chm-sdk-messaging-quotas)
  + [SIP trunking and voice quotas](#chm-sdk-pstn-quotas)
  + [Amazon Chime SDK WebRTC quotas](#chm-sdk-webrtc-quotas)
  + [Legacy quotas](#legacy-quotas)

## Service endpoints
<a name="chime_sdk_region"></a>

### Identity
<a name="identity_endpoints"></a>


| Region name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (N. Virginia) | `us-east-1` | identity-chime.us-east-1.amazonaws.com<br />identity-chime.us-east-1.api.aws<br />identity-chime-fips.us-east-1.amazonaws.com<br />identity-chime-fips.us-east-1.api.aws | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Europe (Frankfurt) | `eu-central-1` | identity-chime.eu-central-1.amazonaws.com<br />identity-chime.eu-central-1.api.aws | HTTPS<br />HTTPS | 

### Media pipeline regional endpoints
<a name="media_pipelines_endpoints"></a>


| Region name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (N. Virginia) | us-east-1 | media-pipelines-chime.us-east-1.amazonaws.com<br />media-pipelines-chime.us-east-1.api.aws<br />media-pipelines-chime-fips.us-east-1.amazonaws.com<br />media-pipelines-chime-fips.us-east-1.api.aws | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| US West (Oregon) | us-west-2 | media-pipelines-chime.us-west-2.amazonaws.com<br />media-pipelines-chime.us-west-2.api.aws<br />media-pipelines-chime-fips.us-west-2.amazonaws.com<br />media-pipelines-chime-fips.us-west-2.api.aws | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Asia Pacific (Mumbai) | ap-south-1 | media-pipelines-chime.ap-south-1.amazonaws.com<br />media-pipelines-chime.ap-south-1.api.aws | HTTPS<br />HTTPS | 
| Asia Pacific (Seoul) | ap-northeast-2 | media-pipelines-chime.ap-northeast-2.amazonaws.com<br />media-pipelines-chime.ap-northeast-2.api.aws | HTTPS<br />HTTPS | 
| Asia Pacific (Singapore) | ap-southeast-1 | media-pipelines-chime.ap-southeast-1.amazonaws.com<br />media-pipelines-chime.ap-southeast-1.api.aws | HTTPS<br />HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 | media-pipelines-chime.ap-southeast-2.amazonaws.com<br />media-pipelines-chime.ap-southeast-2.api.aws | HTTPS<br />HTTPS | 
| Asia Pacific (Tokyo) | ap-northeast-1 | media-pipelines-chime.ap-northeast-1.amazonaws.com<br />media-pipelines-chime.ap-northeast-1.api.aws | HTTPS<br />HTTPS | 
| Canada (Central) | ca-central-1 | media-pipelines-chime.ca-central-1.amazonaws.com<br />media-pipelines-chime.ca-central-1.api.aws<br />media-pipelines-chime-fips.ca-central-1.api.aws | HTTPS<br />HTTPS<br />HTTPS | 
| Europe (Frankfurt) | eu-central-1 | media-pipelines-chime.eu-central-1.amazonaws.com<br />media-pipelines-chime.eu-central-1.api.aws | HTTPS<br />HTTPS | 
| Europe (London) | eu-west-2 | media-pipelines-chime.eu-west-2.amazonaws.com<br />media-pipelines-chime.eu-west-2.api.aws | HTTPS<br />HTTPS | 

### Messaging
<a name="messaging_endpoints"></a>


| Region name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (N. Virginia) | us-east-1 | messaging-chime.us-east-1.amazonaws.com<br />messaging-chime.us-east-1.api.aws<br />messaging-chime-fips.us-east-1.amazonaws.com<br />messaging-chime-fips.us-east-1.api.aws | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Europe (Frankfurt) | eu-central-1 | messaging-chime.eu-central-1.amazonaws.com<br />messaging-chime.eu-central-1.api.aws | HTTPS<br />HTTPS | 

### Voice
<a name="pstn_audio_endpoints"></a>


| Region name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (N. Virginia) | us-east-1 | voice-chime.us-east-1.amazonaws.com<br />voice-chime.us-east-1.api.aws<br />voice-chime-fips.us-east-1.amazonaws.com<br />voice-chime-fips.us-east-1.api.aws | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| US West (Oregon) | us-west-2 | voice-chime.us-west-2.amazonaws.com<br />voice-chime.us-west-2.api.aws<br />voice-chime-fips.us-west-2.amazonaws.com<br />voice-chime-fips.us-west-2.api.aws | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Asia Pacific (Seoul) | ap-northeast-2 | voice-chime.ap-northeast-2.amazonaws.com<br />voice-chime.ap-northeast-2.api.aws | HTTPS<br />HTTPS | 
| Asia Pacific (Singapore) | ap-southeast-1 | voice-chime.ap-southeast-1.amazonaws.com<br />voice-chime.ap-southeast-1.api.aws | HTTPS<br />HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 | voice-chime.ap-southeast-2.amazonaws.com<br />voice-chime.ap-southeast-2.api.aws | HTTPS<br />HTTPS | 
| Asia Pacific (Tokyo) |  ap-northeast-1 | voice-chime.ap-northeast-1.amazonaws.com<br />voice-chime.ap-northeast-1.api.aws | HTTPS<br />HTTPS | 
| Canada (Central) | ca-central-1 | voice-chime.ca-central-1.amazonaws.com<br />voice-chime.ca-central-1.api.aws<br />voice-chime-fips.ca-central-1.amazonaws.com<br />voice-chime-fips.ca-central-1.api.aws | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Europe (Ireland) | eu-west-1 | voice-chime.eu-west-1.amazonaws.com<br />voice-chime.eu-west-1.api.aws | HTTPS<br />HTTPS | 
| Europe (Frankfurt) | eu-central-1 | voice-chime.eu-central-1.amazonaws.com<br />voice-chime.eu-central-1.api.aws | HTTPS<br />HTTPS | 
| Europe (London) | eu-west-2 | voice-chime.eu-west-2.amazonaws.com<br />voice-chime.eu-west-2.api.aws | HTTPS<br />HTTPS | 

### WebRTC media sessions
<a name="web_rtc_media_sessions_endpoints"></a>


| Region name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (N. Virginia) | us-east-1 | meetings-chime.us-east-1.amazonaws.com<br />meetings-chime.us-east-1.api.aws<br />meetings-chime-fips.us-east-1.amazonaws.com<br />meetings-chime-fips.us-east-1.api.aws | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| US West (Oregon) | us-west-2 | meetings-chime.us-west-2.amazonaws.com<br />meetings-chime.us-west-2.api.aws<br />meetings-chime-fips.us-west-2.amazonaws.com<br />meetings-chime-fips.us-west-2.api.aws | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Africa (Cape Town) | `af-south-1` | meetings-chime.af-south-1.amazonaws.com<br />meetings-chime.af-south-1.api.aws | HTTPS<br />HTTPS | 
| Asia Pacific (Mumbai) | ap-south-1 | meetings-chime.ap-south-1.amazonaws.com<br />meetings-chime.ap-south-1.api.aws | HTTPS<br />HTTPS | 
| Asia Pacific (Seoul) | ap-northeast-2 | meetings-chime.ap-northeast-2.amazonaws.com<br />meetings-chime.ap-northeast-2.api.aws | HTTPS<br />HTTPS | 
| Asia Pacific (Singapore) | ap-southeast-1 | meetings-chime.ap-southeast-1.amazonaws.com<br />meetings-chime.ap-southeast-1.api.aws | HTTPS<br />HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 | meetings-chime.ap-southeast-2.amazonaws.com<br />meetings-chime.ap-southeast-2.api.aws | HTTPS<br />HTTPS | 
| Asia Pacific (Tokyo) | ap-northeast-1 | meetings-chime.ap-northeast-1.amazonaws.com<br />meetings-chime.ap-northeast-1.api.aws | HTTPS<br />HTTPS | 
| Canada (Central) | ca-central-1 | meetings-chime.ca-central-1.amazonaws.com<br />meetings-chime.ca-central-1.api.aws<br />meetings-chime-fips.ca-central-1.amazonaws.com<br />meetings-chime-fips.ca-central-1.api.aws | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Europe (Frankfurt) | eu-central-1 | meetings-chime.eu-central-1.amazonaws.com<br />meetings-chime.eu-central-1.api.aws | HTTPS<br />HTTPS | 
| Europe (London) | eu-west-2 | meetings-chime.eu-west-2.amazonaws.com<br />meetings-chime.eu-west-2.api.aws | HTTPS<br />HTTPS | 
| Israel (Tel Aviv) | il-central-1 | meetings-chime.il-central-1.amazonaws.com<br />meetings-chime.il-central-1.api.aws | HTTPS<br />HTTPS | 
| AWS GovCloud (US-East) | us-gov-east-1 | meetings-chime.us-gov-east-1.amazonaws.com<br />meetings-chime.us-gov-east-1.api.aws<br />meetings-chime-fips.us-gov-east-1.amazonaws.com<br />meetings-chime-fips.us-gov-east-1.api.aws | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| AWS GovCloud (US-West) | us-gov-west-1 | meetings-chime.us-gov-west-1.amazonaws.com<br />meetings-chime.us-gov-west-1.api.aws<br />meetings-chime-fips.us-gov-west-1.amazonaws.com<br />meetings-chime-fips.us-gov-west-1.api.aws | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 

### Legacy
<a name="legacy_endpoints"></a>


| Region name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (N. Virginia) | `us-east-1` | service.chime.amazonaws.com<br />service-fips.chime.amazonaws.com | HTTPS<br />HTTPS | 

## Service quotas
<a name="limits_chime_sdk"></a>

The tables in the following sections list and describe the quotas for the Amazon Chime SDK services.

**Note**  
Service quotas are per AWS Region. If adjustable, quotas only change for the requested Region.

**Topics**
+ [Amazon Chime SDK call analytics quotas](#analytics-quotas)
+ [Amazon Chime SDK Identity quotas](#chm-sdk-ident-quotas)
+ [Amazon Chime SDK Media Pipeline quotas](#media-pipeline-quotas)
+ [Amazon Chime SDK Messaging quotas](#chm-sdk-messaging-quotas)
+ [SIP trunking and voice quotas](#chm-sdk-pstn-quotas)
+ [Amazon Chime SDK WebRTC quotas](#chm-sdk-webrtc-quotas)
+ [Legacy quotas](#legacy-quotas)

### Amazon Chime SDK call analytics quotas
<a name="analytics-quotas"></a>

Amazon Chime SDK call analytics has the following quotas.


| Resource | Default limit | Adjustable | Description | 
| --- | --- | --- | --- | 
|  Amazon Chime SDK call analytics - Maximum configurations  |  100  |  Yes  |  Maximum number of call analytics configurations per Region for the specified account.  | 
|  Amazon Chime SDK call analytics - Maximum pipelines  |  20  |  Yes  |  Maximum number of call analytics media processing pipelines per Region for the specified account.  | 
|  Amazon Chime SDK call analytics - Maximum voice profile domains  |  3  |  Yes  |  Voice analytics voice profile domains per Region for the specified account. Customers can create voice profile domains to collect a set of related voice IDs for voice analytics.  | 
|  Amazon Chime SDK call analytics - Voice profiles per voice profile domain  |  20  |  Yes  |  Maximum number of voice analytics voice profiles per voice profile domain.  | 
|  Amazon Chime SDK call analytics - Maximum voice analytics tasks  |  25  |  Yes  |  Maximum number of active voice analytics tasks per Region to perform speaker search and voice tone analysis.  | 
|  Amazon Chime SDK call analytics - Voice profile domain API rate  | 0 |  Yes  |  The maximum TPS for all voice profile domain API requests.  | 
|  Amazon Chime SDK call analytics - Voice profile API rate  | 0 |  Yes  |  The maximum TPS for all voice profile API requests.  | 
|  Amazon Chime SDK call analytics - Speaker search API rate  | 0 |  Yes  |  The maximum TPS for all speaker search API requests.  | 
|  Amazon Chime SDK call analytics - Voice tone analysis API rate  | 0 |  Yes  |  The maximum TPS for all voice tone analysis API requests.  | 
|  Amazon Chime SDK call analytics - API rate  |  5  |  Yes  |  The maximum call analytics configuration management API requests per second for this account in the current Region.  | 

**Note**  
If you exceed the quota for any Region, you receive a **Resource Limit Exceeded** exception. You can use the **Service Quotas** page in the AWS console to request an increase, or you can contact your [customer support representative](https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html).
Several of the call analytics APIs create resources and API requests for other AWS services. Those additional resources count against your account's quotas. If you request a quota or transactions-per-second increase from call analytics, you must also request increases for those other AWS services. Otherwise, your requests may be throttled and fail.

### Amazon Chime SDK Identity quotas
<a name="chm-sdk-ident-quotas"></a>

The following quotas apply for managing AppInstances, AppInstanceUsers and AppInstanceEndpoints for the [Amazon Chime SDK Identity](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Identity.html) APIs. The quotas apply on a per API basis. 

Amazon Chime SDK Identity has the following resource quotas:


| Name | Default | Adjustable | Description | 
| --- | --- | --- | --- | 
| Amazon Chime SDK Identity - Maximum `AppInstances` per AWS Account | 100 | Yes | The maximum number of `AppInstances` you can create in an AWS Account. | 
| Amazon Chime SDK Identity - Maximum `AppInstanceUsers` per `AppInstance` | 100,000 | Yes | The maximum number of `AppInstanceUsers` you can create in an `AppInstance` | 
| Amazon Chime SDK Identity - Maximum `AppInstanceUserAdmins` per `AppInstance` | 100 | Yes | The maximum number of `AppInstanceUserAdmins` you can create in an `AppInstance`. | 
| Amazon Chime SDK Identity - Maximum AppInstanceUserEndpoints per AppInstanceUser | 10 | Yes | The maximum number of `AppInstanceUserEndpoints` you can create for an `AppInstanceUser` | 

The following limits apply to the [Amazon Chime SDK Identity](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Identity.html) APIs for managing `AppInstances`, `AppInstanceUsers`, and `AppInstanceEndpoints` on a per-API basis.


| Name | Default | Adjustable | Description | 
| --- | --- | --- | --- | 
| Amazon Chime SDK Identity - Rate of [CreateAppInstance](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_CreateAppInstance.html), [UpdateAppInstance](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_UpdateAppInstance.html), and [DeleteAppInstance](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_DeleteAppInstance.html) requests | 5 requests per second per `AppInstance` | Yes | The maximum requests per second at which you can simultaneously create, update and delete `AppInstances` in your AWS account | 
| Amazon Chime SDK Identity - Rate of [CreateAppInstanceUser](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_CreateAppInstanceUser.html), [UpdateAppInstanceUser](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_UpdateAppInstanceUser.html), and [DeleteAppInstanceUser](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_DeleteAppInstanceUser.html) requests | 10 requests per second per `AppInstance` | Yes | The maximum requests per second at which you can simultaneously create, update and delete `AppInstanceUsers` in your AWS account | 
| Amazon Chime SDK Identity - Rate of DescribeAppInstance requests | 20 requests per second per AppInstance | Yes | The maximum requests per second at which you can invoke the [DescribeAppInstance](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_DescribeAppInstance.html) API for a specific `AppInstance` | 
| Amazon Chime SDK Identity - Rate of DescribeAppInstanceUser requests | 20 requests per second per `AppInstanceUser` | Yes | The maximum requests per second at which you can invoke the [DescribeAppInstanceUser](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_DescribeAppInstanceUser.html) API for a specific `AppInstanceUser` | 
| Amazon Chime SDK Identity - Rate of ListAppInstances requests | 10 requests per second per AWS Account | Yes | The maximum requests per second at which you can invoke the [ListAppInstances](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_ListAppInstances.html) API for your AWS Account | 
| Amazon Chime SDK Identity - Rate of ListAppInstanceUsers requests | 10 requests per second per AppInstanceUser | Yes | The maximum requests per second at which you can invoke the [ListAppInstanceUsers](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_ListAppInstanceUsers.html) API for a specific `AppInstance` | 
| Amazon Chime SDK Identity - Total requests per second per AWS Account | 50 requests per second per AWS account | Yes | The maximum requests per second at which you can simultaneously invoke the [ Chime SDK Identity APIs](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Identity.html) in your AWS account | 

### Amazon Chime SDK Media Pipeline quotas
<a name="media-pipeline-quotas"></a>

Amazon Chime SDK Media Pipelines have the following quotas.


| Name | Default | Adjustable | Description | 
| --- | --- | --- | --- | 
|  Amazon Chime SDK media pipeline - API rate  |  10  |  Yes  |  The maximum rate of all SDK media pipeline API requests per second that you can send in this account in the current Region.  | 
|  Amazon Chime SDK media pipeline - Maximum pipelines  | `US East (N. Virginia)`: 100<br />All others: 10 |  Yes  |  The maximum number of concurrent media pipelines that you can run for this account. Excludes media insights pipelines.  | 
|  Amazon Chime SDK media pipeline - Maximum Amazon Kinesis Video Stream pools  |  10  |  Yes  |  The maximum number of Amazon Kinesis Video Stream (KVS) pools that you can create. A pool contains multiple KVS streams. The total number of KVS streams that can be created is governed by the KVS service quota: Number of video streams.  | 
|  Amazon Chime SDK media pipeline - Amazon Kinesis Video Stream pool API rate  |  5  |  Yes  |  The maximum number of requests per second that you make to each of the following APIs: CreateMediaPipelineKinesisVideoStreamPool, UpdateMediaPipelineKinesisVideoStreamPool, and DeleteMediaPipelineKinesisVideoStreamPool.  | 

### Amazon Chime SDK Messaging quotas
<a name="chm-sdk-messaging-quotas"></a>

Amazon Chime SDK Messaging has the following quotas.


| Name | Default | Adjustable | 
| --- | --- | --- | 
|  Amazon Chime SDK Messaging - Maximum concurrent active connections per AppInstanceUser  |  10  |  Yes  | 
|  Amazon Chime SDK Messaging - Maximum ChannelFlows per AppInstance  |  100  |  Yes  | 
|  Amazon Chime SDK Messaging - Maximum ChannelMemberships per Channel  |  10,000  |  Yes  | 
|  Amazon Chime SDK Messaging - Maximum ChannelProcessors per ChannelFlow  |  1  |  Yes  | 
|  Amazon Chime SDK Messaging - Maximum Channels per AppInstance  |  10,000,000  |  Yes  | 
|  Amazon Chime SDK Messaging - Maximum ChannelModerators per Channel  |  1,000  |  Yes  | 
|  Amazon Chime SDK Messaging - Maximum ChannelProcessors per ChannelFlow  |  1  |  Yes  | 
|  Amazon Chime SDK Messaging - Maximum CHANNEL\_DETAILS events for prefetch  |  50  |  Yes  | 
|  Amazon Chime SDK Messaging - Maximum ChannelMessages in CHANNEL\_DETAILS events for prefetch  |  20  |  Yes  | 
|  Amazon Chime SDK Messaging - Maximum ChannelMemberships in CHANNEL\_DETAILS events for prefetch  |  30  |  Yes  | 
|  Amazon Chime SDK Messaging - Maximum Elastic Channels per AppInstance \* |  1  |  Yes  | 
|  Amazon Chime SDK Messaging - Maximum SubChannels per Elastic Channel \* |  100  |  Yes  | 
|  Amazon Chime SDK Messaging - Maximum ChannelMemberships per SubChannel \* |  1,000  |  Yes  The product of `MaximumSubChannelsPerElasticChannel` and `MaximumChannelMembershipsPerSubChannel` cannot exceed 1-million after a limit increase.  | 
| Amazon Chime SDK Messaging – Maximum ChannelMemberships per AppInstanceUser | 20,000 | Yes | 

**\***Only available in the US East (N. Virginia) Region.

**Note**  
Customers with large chat channels often qualify for volume discounts on pricing. Contact your account manager for more details.

In addition to the quotas listed above, Amazon Chime SDK Messaging has the following API rates.


| Name | Default | Adjustable | Description | 
| --- | --- | --- | --- | 
| Amazon Chime SDK Messaging - Rate of CreateChannel, UpdateChannel, DeleteChannel requests | 15 requests per second per `AppInstance` | Yes | The maximum requests per second at which you can simultaneously create, update, or delete Channels for a specific `AppInstance` | 
| Amazon Chime SDK Messaging - Rate of ListChannels requests | 10 requests per second per `AppInstance` | Yes | The maximum rate at which you can invoke the [ListChannels](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannels.html) API for a specific `AppInstance` | 
| Amazon Chime SDK Messaging - Rate of DescribeChannel requests | 20 requests per second per Channel | Yes | The maximum rate at which you can invoke the [DescribeChannel](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannel.html) API for a specific `AppInstance` | 
| Amazon Chime SDK Messaging - Rate of `CreateChannelMembership`, `DeleteChannelMembership`, `CreateChannelBan`, `DeleteChannelBan`, `CreateChannelModerator`, `DeleteChannelModerator` requests | `us-east-1`: 15 requests per second per Channel, 30 requests per second per Elastic Channel<br />`eu-central-1`: 10 requests per second per Channel | Yes | The maximum requests per second at which you can simultaneously create, update, or delete `Channel` memberships, bans, and moderators for a specific channel | 
| Amazon Chime SDK Messaging - Rate of `ListChannelMemberships`, `ListChannelBans`, `ListChannelModerators` requests | 15 requests per second per `Channel` and Elastic Channel | Yes | The maximum requests per second at which you can simultaneously list `Channel` memberships, bans, and moderators for a specific channel | 
| Amazon Chime SDK Messaging - Rate of `SendChannelMessage`, `UpdateChannelMessage`, `RedactChannelMessage`, `DeleteChannelMessage requests` | `us-east-1`: 30 requests per second per `Channel` or per `SubChannel` .<br />`eu-central-1`: 10 requests per second per channel  | Yes | The maximum requests per second at which you can simultaneously create, update, redact, or delete `ChannelMessages` for a specific `Channel` or `SubChannel` . This includes calls to the [ChannelFlowCallback](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelFlowCallback.html) API to update messages. | 
| Amazon Chime SDK Messaging - Rate of `ListChannelMessages` requests | 30 requests per second per `Channel` or per `SubChannel`  | Yes | The maximum requests per second at which you can invoke [ListChannelMessages](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelMessages.html) for a specific `Channel` or `SubChannel`. | 
| Amazon Chime SDK Messaging - Rate of `GetChannelMessage` requests | 30 requests per second per `Channel` or per sub-channel | Yes | The maximum requests per second at which you can invoke [GetChannelMessage](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_GetChannelMessage.html) for a specific `Channel` or `SubChannel`. | 
| Amazon Chime SDK Messaging - Rate of `ListChannelMembershipsForAppInstanceUser`, `ListChannelsModeratedByAppInstanceUser` requests | 15 requests per second per AppInstanceUser | Yes | The maximum requests per second at which you can simultaneously invoke the [ListChannelMembershipsForAppInstanceUser](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelMembershipsForAppInstanceUser.html) and [ListChannelsModeratedByAppInstanceUser](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelsModeratedByAppInstanceUser.html) APIs for a specific `AppInstance` | 
| Amazon Chime SDK Messaging - Rate of `ListSubChannels` requests | 15 requests per second per elastic channel | Yes | The maximum requests per second at which you can invoke the [ListSubChannels](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListSubChannels.html) API for a specific Elastic Channel | 

Amazon Chime SDK Messaging also has the following general API rates.


| Name | Default | Adjustable | Description | 
| --- | --- | --- | --- | 
| Amazon Chime SDK Messaging - Rate of API requests per `ChimeBearer` | `us-east-1`: 10 requests per second per `AppInstanceUser`<br />`eu-central-1`: 5 requests per second per `AppInstanceUser` | Yes | The maximum requests per second at which a specific `ChimeBearer` can simultaneously invoke the Messaging APIs. This limit prevents a single `AppInstanceUser` from consuming all of the throughput for operations on a single `Channel` in an `AppInstance`. You can request limit increases for specific `AppInstanceUsers`. | 
| Amazon Chime SDK Messaging - Rate of Batch API requests | 1 request per second per resource | No | The maximum requests per second at which each Batch API, such as [BatchCreateChannelMembership](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_BatchCreateChannelMembership.html), can be invoked | 
| Amazon Chime SDK Messaging - Rate of websocket connect requests per `AppInstanceUser` | 1 request per second per `AppInstanceUser` | No | The maximum requests per second at which an `AppInstanceUser` can establish a new websocket connection, even for different sessions | 

### SIP trunking and voice quotas
<a name="chm-sdk-pstn-quotas"></a>

Amazon Chime SDK SIP trunking and voice have the following quotas.


| Name | Default | Adjustable | Description | 
| --- | --- | --- | --- | 
|  Amazon Chime SDK SIP trunking and voice - provisioned phone numbers  |  5  |  Yes  |  The maximum number of provisioned phone numbers you can have in this account  | 
|  Amazon Chime SDK SIP trunking and voice - Voice Connectors  |  3  |  Yes  |  The maximum number of Voice Connectors you can have in the current AWS Region  | 
|  Amazon Chime SDK SIP trunking and voice - Voice Connector groups  |  3  |  Yes  |  The maximum number of Voice Connector groups you can have in this account.  | 
|  Amazon Chime SDK SIP trunking and voice - Voice Connectors per Voice Connector group  |  3  |  Yes  |  The maximum number of Voice Connectors you can have in any Voice Connector group  | 
|  Amazon Chime SDK SIP trunking and voice - calls per second (CPS)  |  1  |  Yes  |  The maximum calls per second (CPS) allowed on each Voice Connector in the current AWS Region  | 
|  Amazon Chime SDK SIP trunking and voice - SIP media applications  |  30  |  Yes  |  The maximum number of SIP media applications you can have in the current AWS Region  | 
|  Amazon Chime SDK SIP trunking and voice - SIP media applications per SIP rule  |  25  |  Yes  |  The maximum number of SIP media applications you can have in a SIP rule in the current AWS Region  | 
|  Amazon Chime SDK SIP trunking and voice - CreateSipMediaApplicationCall API rate limit  |  1  |  Yes  |  The maximum number of requests to the CreateSipMediaApplicationCall API per second allowed in the current AWS Region.  | 
|  Amazon Chime SDK SIP trunking and voice - UpdateSipMediaApplicationCall API rate limit  |  5  |  Yes  |  The maximum number of requests to the UpdateSipMediaApplicationCall API per second allowed in the current AWS Region.  | 
| Amazon Chime SDK SIP trunking and voice - StartBotConversation Amazon Lex bots | 0 | Yes | The maximum number of Amazon Lex bots you can use with the PSTN Audio [StartBotConversation](https://docs.aws.amazon.com/chime-sdk/latest/dg/start-bot-conversation.html) action in the current AWS Region. | 
| Amazon Chime SDK SIP trunking and voice - Voice Connector Active Call Count | 10 | Yes | The maximum Voice Connector concurrent call count allowed per account in the current AWS Region. | 
| Amazon Chime SDK SIP trunking and voice - SIP Media Application Active Call Count | 10 | Yes | The maximum PSTN Audio concurrent call count allowed per account in the current AWS Region. | 

### Amazon Chime SDK WebRTC quotas
<a name="chm-sdk-webrtc-quotas"></a>

Amazon Chime SDK Meetings WebRTC media sessions have the following quotas.


| Name | Default | Adjustable | 
| --- | --- | --- | 
| Amazon Chime SDK Meetings – Concurrent meeting limit | 250 | Yes | 
|  Amazon Chime SDK meetings - Attendees per meeting  |  250  |  No  | 
|  Amazon Chime SDK meetings - Replica meetings per primary meeting  |  4  |  Yes For more information, refer to the [ Chime SDK Meetings - replica meetings per primary meeting](https://console.aws.amazon.com/servicequotas/home/services/chime/quotas/L-154D84D0) page in the Service Quotas console. | 
|  Amazon Chime SDK meetings - Concurrent video streams published per meeting  |  25  | Yes. For more information, refer to the [ Chime SDK Meetings - maximum concurrent video streams published per meeting ](https://console.aws.amazon.com/servicequotas/home/services/chime/quotas/L-AC1D2091) page in the Service Quotas console. | 
|  Amazon Chime SDK meetings - Concurrent video streams subscribed per attendee  |  25  | No | 
|  Amazon Chime SDK meetings - BatchCreateAttendees API rate in requests per second  |  10  | Yes. Adjusts automatically when concurrent meeting limit is adjusted. | 
|  Amazon Chime SDK meetings - CreateAttendee API rate in requests per second  |  10  |  Yes. Adjusts automatically when concurrent meeting limit is adjusted.  | 
|  Amazon Chime SDK meetings - CreateMeeting API rate in requests per second  |  10  |  Yes. Adjusts automatically when concurrent meeting limit is adjusted.  | 
|  Amazon Chime SDK meetings - CreateMeetingWithAttendees API rate in requests per second  |  10  |  Yes. Adjusts automatically when concurrent meeting limit is adjusted.  | 
|  Amazon Chime SDK meetings - DeleteAttendee API rate in requests per second  |  10  |  Yes. Adjusts automatically when concurrent meeting limit is adjusted.  | 
|  Amazon Chime SDK meetings - DeleteMeeting API rate in requests per second  |  10  |  Yes. Adjusts automatically when concurrent meeting limit is adjusted.  | 
|  Amazon Chime SDK meetings - GetMeeting API rate in requests per second  |  10  |  Yes. Adjusts automatically when concurrent meeting limit is adjusted.  | 
|  Amazon Chime SDK meetings - ListAttendees API rate in requests per second  |  10  |  Yes. Adjusts automatically when concurrent meeting limit is adjusted.  | 

### Legacy quotas
<a name="legacy-quotas"></a>

The following quotas apply only to legacy endpoints. 


| Name | Default | Adjustable | Description | 
| --- | --- | --- | --- | 
|  Amazon Chime SDK media pipeline - Maximum pipelines  |  10  | No | The maximum rate of all media pipeline API requests that you can send in this account in the current Region. This quota is for the Amazon Chime namespace. | 
| Amazon Chime – Total active media pipelines per account | 100 | No | The total number of active media pipelines per account in a Region. This quota is for the Amazon Chime namespace. | 
| Amazon Chime SDK Media Pipelines – Rate limit for al media pipeline API requests in transactions per second | 10 | Yes | The maximum rate of all SDK media pipeline API requests that you can send in this account in the current Region This quota is for the Amazon Chime namespace. | 
|  Amazon Chime SDK Media Pipeline - Media capture API burst limit  | 10 | No | The maximum number of media capture pipeline requests that you can send in one burst. This quota is for the Amazon Chime namespace. This quota is for the Amazon Chime namespace. | 
| Amazon Chime SDK Media Pipeline - API rate limit | 10 | Yes | The maximum rate of all SDK media pipeline API requests that you can send in this account in the current Region. This quota is for the Amazon Chime namespace. | 