

# Quotas in AWS Elemental MediaTailor
<a name="quotas"></a>

MediaTailor resources and operations requests are subject to the following quotas (formerly referred to as "limits").

 You can use the AWSService Quotas service to view quotas and request quota increases for MediaTailor, as well as many other AWS services. For more information, see the [Service Quotas User Guide](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html).

## Quotas on ad insertion
<a name="ad-insertion-quotas"></a>

The following table describes the quotas on AWS Elemental MediaTailor ad insertion. Unless otherwise noted, the quotas are not adjustable.


| Name | Default quota value | Description | 
| --- | --- | --- | 
| Ad decision server (ADS) length | 25,000  | The maximum number of characters in an ad decision server (ADS) specification.  | 
| Ad decision server (ADS) redirects | 7 | The maximum depth of redirects that MediaTailor follows in VAST wrapper tags. MediaTailor gives up if there are additional redirects. | 
| Ad decision server (ADS) timeout | 3 seconds (default) | The maximum number of seconds that MediaTailor waits before timing out on an open connection to an ad decision server (ADS). When a connection times out due to no response from the ADS, MediaTailor is unable to fill the ad avail with ads. This timeout is configurable through the Individual ADS request timeout setting (range: 250–6,000 ms). For more information, see [Advanced settings](configurations-create.md#configurations-advanced-settings). | 
| Ad Insertion Requests | 10,000 | The maximum requests per second to make for personalized manifests when performing server side ad insertion. Ad insertion handles incoming requests for manifests, session initialization, tracking data, and ad segments. This quota is [adjustable](https://console.aws.amazon.com/servicequotas/home/services/mediatailor/quotas). | 
| Configurations | 1,000 | The maximum number of configurations that MediaTailor allows.  | 
| Content origin length | 512  | The maximum number of characters in a content origin specification.  | 
| Content origin server timeout | 2 | The maximum number of seconds that MediaTailor waits before timing out on an open connection to the content origin server when requesting template manifests. Timeouts generate HTTP 504 (GatewayTimeoutException) response errors.  | 
| Manifest size | 2 | The maximum size, in MB, of any origin playback manifest. To ensure that you stay under the quota, use gzip to compress your input manifests into MediaTailor. | 
| Package configurations | 5 | The maximum number of package configurations per source (whether live or video on demand). | 
| Prefetch schedules | 25 | The maximum number of active prefetch schedules per playback configuration. Expired prefetch schedules don't count towards this limit.  | 
| Server side reporting beacon request timeout | 3 seconds | The maximum number of seconds that MediaTailor waits before timing out on an open connection to the server when firing a beacon for server side reporting. When a connection times out, MediaTailor is unable to fire the beacon and the service logs an ERROR\_FIRING\_BEACON\_FAILED message to the MediaTailor/AdDecisionServerInteractions log in CloudWatch. | 
| PRE\_SESSION\_INITIALIZATION hook timeout | 2 seconds | The maximum number of seconds that a PRE\_SESSION\_INITIALIZATION hook execution can take, including all function steps and HTTP calls. If the hook exceeds its timeout, MediaTailor discards all output and proceeds as if no function was executed. | 
| PRE\_ADS\_REQUEST hook timeout | 2 seconds | The maximum number of seconds that a PRE\_ADS\_REQUEST hook execution can take, including all function steps and HTTP calls. If the hook exceeds its timeout, MediaTailor discards all output and proceeds as if no function was executed. | 
| Maximum functions per hook | 20 | The maximum number of total function executions allowed per hook. | 
| Session expiration  | 10 times the manifest duration | The maximum amount of time that MediaTailor allows a session to remain inactive before ending the session. Session activity can be a player request or an advance by the origin server. When the session expires, MediaTailor returns an HTTP 400 (Bad Request) response error. | 

## Quotas on channel assembly
<a name="channel-assembly-quotas"></a>

The following table describes the quotas on AWS Elemental MediaTailor channel assembly. Unless otherwise noted, the quotas are [adjustable](https://console.aws.amazon.com/servicequotas/home/services/mediatailor/quotas).


| Name | Default quota value | Description | 
| --- | --- | --- | 
| Channel manifest requests, per account | 400 | The maximum number of egress manifest requests per second for all Channel Assembly channels on an account.  | 
| Channel manifest requests, per channel | 50 | The maximum number of egress manifest requests per second for any single Channel Assembly channel.  | 
| Channel outputs | 5 | The maximum number of outputs per channel. | 
| Channels per account | 100 | The maximum number of channels per account. | 
| Live sources | 50 | The maximum number of live sources for the source location. | 
| Programs per channel | 400 | The maximum number of programs per channel. | 
| Segment delivery configurations | 5 | The maximum number of segment delivery configurations per source location. | 
| Source locations | 50 | The maximum number of source locations per account. | 
| VOD Sources | 1,000 | The maximum number of video on demand (VOD) sources for the source location. | 

The following table describes the throttling limits on AWS Elemental MediaTailor channel assembly. Unless otherwise noted, the quotas are [adjustable](https://console.aws.amazon.com/servicequotas/home/services/mediatailor/quotas).


| Name | Default transactions-per-second maximum limit | Description | 
| --- | --- | --- | 
| ConfigureLogsForChannel | 1 | Configure logs for the channel. | 
| CreateChannel | 1 | Create a channel. | 
| CreateLiveSource | 1 | Create a live source. | 
| CreateProgram | 3 | Create a program. | 
| CreateSourceLocation | 1 | Create a Source Location. | 
| CreateVodSource | 1 | Create a VOD source. | 
| DeleteChannel | 1 | Delete a channel. | 
| DeleteChannelPolicy | 1 | Delete a channel policy. | 
| DeleteLiveSource | 1 | Delete a live source. | 
| DeleteProgram | 3 | Delete a program. | 
| DeleteSourceLocation | 1 | Delete a source location. | 
| DeleteVodSource | 1 | Delete a VOD source. | 
| DescribeChannel | 5 | Describe a channel. | 
| DescribeLiveSoure | 5 | Describe a live source. | 
| DescribeProgram | 5 | Describe a program. | 
| DescribeSourceLocation | 5 | Describe a source location. | 
| DescribeVodSource | 5 | Describe a VOD source. | 
| GetChannelPolicy | 5 | Get a channel policy. | 
| GetChannelSchedule | 5 | Get a channel schedule. | 
| ListAlerts | 5 | List alerts. | 
| ListChannels | 5 | List channels. | 
| ListLiveSources | 5 | List live sources. | 
| ListPrograms | 5 | List programs. | 
| ListSourceLocations | 5 | List source locations. | 
| ListTagsForResource | 5 | List tags for a resource. | 
| ListVodSources | 5 | List VOD sources. | 
| PutChannelPolicy | 3 | Put a channel policy. | 
| StartChannel | 1 | Start a channel. | 
| StopChannel | 1 | Stop a channel. | 
| TagResource | 1 | Tag a resource. | 
| UntagResource | 1 | Untag a resource. | 
| UpdateChannel | 1 | Update a channel. | 
| UpdateLiveSource | 1 | Update a live source. | 
| UpdateProgram | 1 | Update a program. | 
| UpdateSourceLocation | 1 | Update a source location. | 
| UpdateVodSource | 1 | Update a VOD source. | 