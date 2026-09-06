

# Data retrieval APIs for AWS Elemental MediaTailor
<a name="awselementalmediatailor"></a>

AWS Elemental MediaTailor provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="mediatailor-DescribeChannel"></a>[DescribeChannel](https://docs.aws.amazon.com/mediatailor/latest/apireference/channel-channelname.html) | Retrieve the channel with the specified channel name | Read | 
| <a name="mediatailor-DescribeLiveSource"></a>[DescribeLiveSource](https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname-livesource-livesourcename.html) | Retrieve the live source with the specified live source name on the source location with the specified source location name | Read | 
| <a name="mediatailor-DescribeProgram"></a>[DescribeProgram](https://docs.aws.amazon.com/mediatailor/latest/apireference/channel-channelname-program-programname.html) | Retrieve the program with the specified program name on the channel with the specified channel name | Read | 
| <a name="mediatailor-DescribeSourceLocation"></a>[DescribeSourceLocation](https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname.html) | Retrieve the source location with the specified source location name | Read | 
| <a name="mediatailor-DescribeVodSource"></a>[DescribeVodSource](https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname-vodsource-vodsourcename.html) | Retrieve the VOD source with the specified VOD source name on the source location with the specified source location name | Read | 
| <a name="mediatailor-GetChannelPolicy"></a>[GetChannelPolicy](https://docs.aws.amazon.com/mediatailor/latest/apireference/channel-channelname-policy.html) | Read the IAM policy on the channel with the specified channel name | Read | 
| <a name="mediatailor-GetChannelSchedule"></a>[GetChannelSchedule](https://docs.aws.amazon.com/mediatailor/latest/apireference/channel-channelname-schedule.html) | Retrieve the schedule of programs on the channel with the specified channel name | Read | 
| <a name="mediatailor-GetPlaybackConfiguration"></a>[GetPlaybackConfiguration](https://docs.aws.amazon.com/mediatailor/latest/apireference/playbackconfiguration-name.html) | Retrieve the configuration for the specified name | Read | 
| <a name="mediatailor-GetPrefetchSchedule"></a>[GetPrefetchSchedule](https://docs.aws.amazon.com/mediatailor/latest/apireference/prefetchschedule-playbackconfigurationname-name.html) | Retrieve prefetch schedule for a playback configuration with the specified prefetch schedule name | Read | 
| <a name="mediatailor-ListAlerts"></a>[ListAlerts](https://docs.aws.amazon.com/mediatailor/latest/apireference/alerts.html) | Retrieve the list of alerts on a resource | Read | 
| <a name="mediatailor-ListChannels"></a>[ListChannels](https://docs.aws.amazon.com/mediatailor/latest/apireference/channels.html) | Retrieve the list of existing channels | Read | 
| <a name="mediatailor-ListLiveSources"></a>[ListLiveSources](https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname-livesources.html) | Retrieve the list of existing live sources on the source location with the specified source location name | Read | 
| <a name="mediatailor-ListPlaybackConfigurations"></a>[ListPlaybackConfigurations](https://docs.aws.amazon.com/mediatailor/latest/apireference/playbackconfigurations.html) | Retrieve the list of available configurations | List | 
| <a name="mediatailor-ListPrefetchSchedules"></a>[ListPrefetchSchedules](https://docs.aws.amazon.com/mediatailor/latest/apireference/prefetchschedule-playbackconfigurationname.html) | Retrieve the list of prefetch schedules for a playback configuration | List | 
| <a name="mediatailor-ListSourceLocations"></a>[ListSourceLocations](https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocations.html) | Retrieve the list of existing source locations | Read | 
| <a name="mediatailor-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/mediatailor/latest/apireference/tags-resourcearn.html) | List the tags assigned to the specified playback configuration resource | Read | 
| <a name="mediatailor-ListVodSources"></a>[ListVodSources](https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname-vodsources.html) | Retrieve the list of existing VOD sources on the source location with the specified source location name | Read | 