

# Actions, resources, and condition keys for AWS Elemental MediaTailor
<a name="list_mediatailor"></a>

AWS Elemental MediaTailor (service prefix: `mediatailor`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/mediatailor/latest/ug/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/mediatailor/latest/apireference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/mediatailor/latest/ug/setting-up-non-admin-policies.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/mediatailor/mediatailor.json) for this service.

**Topics**
+ [API operations defined by AWS Elemental MediaTailor](#list_mediatailor-operations)
+ [Actions defined by AWS Elemental MediaTailor](#list_mediatailor-actions-as-permissions)
+ [Resource types defined by AWS Elemental MediaTailor](#list_mediatailor-resources-for-iam-policies)
+ [Condition keys for AWS Elemental MediaTailor](#list_mediatailor-policy-keys)

## API operations defined by AWS Elemental MediaTailor
<a name="list_mediatailor-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_mediatailor-actions-as-permissions).




- **   ConfigureLogsForChannel  **
  - **IAM action:**  [mediatailor:ConfigureLogsForChannel](#list_mediatailor-action-ConfigureLogsForChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ConfigureLogsForPlaybackConfiguration  **
  - **IAM action:**  [mediatailor:ConfigureLogsForPlaybackConfiguration](#list_mediatailor-action-ConfigureLogsForPlaybackConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateChannel  **
  - **IAM action:**  [mediatailor:CreateChannel](#list_mediatailor-action-CreateChannel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediatailor:TagResource](#list_mediatailor-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateLiveSource  **
  - **IAM action:**  [mediatailor:CreateLiveSource](#list_mediatailor-action-CreateLiveSource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediatailor:TagResource](#list_mediatailor-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreatePrefetchSchedule  **
  - **IAM action:**  [mediatailor:CreatePrefetchSchedule](#list_mediatailor-action-CreatePrefetchSchedule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediatailor:TagResource](#list_mediatailor-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateProgram  **
  - **IAM action:**  [mediatailor:CreateProgram](#list_mediatailor-action-CreateProgram)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediatailor:TagResource](#list_mediatailor-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSourceLocation  **
  - **IAM action:**  [mediatailor:CreateSourceLocation](#list_mediatailor-action-CreateSourceLocation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediatailor:TagResource](#list_mediatailor-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateVodSource  **
  - **IAM action:**  [mediatailor:CreateVodSource](#list_mediatailor-action-CreateVodSource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediatailor:TagResource](#list_mediatailor-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteChannel  **
  - **IAM action:**  [mediatailor:DeleteChannel](#list_mediatailor-action-DeleteChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteChannelPolicy  **
  - **IAM action:**  [mediatailor:DeleteChannelPolicy](#list_mediatailor-action-DeleteChannelPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteLiveSource  **
  - **IAM action:**  [mediatailor:DeleteLiveSource](#list_mediatailor-action-DeleteLiveSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePlaybackConfiguration  **
  - **IAM action:**  [mediatailor:DeletePlaybackConfiguration](#list_mediatailor-action-DeletePlaybackConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePrefetchSchedule  **
  - **IAM action:**  [mediatailor:DeletePrefetchSchedule](#list_mediatailor-action-DeletePrefetchSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProgram  **
  - **IAM action:**  [mediatailor:DeleteProgram](#list_mediatailor-action-DeleteProgram) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSourceLocation  **
  - **IAM action:**  [mediatailor:DeleteSourceLocation](#list_mediatailor-action-DeleteSourceLocation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteVodSource  **
  - **IAM action:**  [mediatailor:DeleteVodSource](#list_mediatailor-action-DeleteVodSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeChannel  **
  - **IAM action:**  [mediatailor:DescribeChannel](#list_mediatailor-action-DescribeChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeLiveSource  **
  - **IAM action:**  [mediatailor:DescribeLiveSource](#list_mediatailor-action-DescribeLiveSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeProgram  **
  - **IAM action:**  [mediatailor:DescribeProgram](#list_mediatailor-action-DescribeProgram) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSourceLocation  **
  - **IAM action:**  [mediatailor:DescribeSourceLocation](#list_mediatailor-action-DescribeSourceLocation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeVodSource  **
  - **IAM action:**  [mediatailor:DescribeVodSource](#list_mediatailor-action-DescribeVodSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetChannelPolicy  **
  - **IAM action:**  [mediatailor:GetChannelPolicy](#list_mediatailor-action-GetChannelPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetChannelSchedule  **
  - **IAM action:**  [mediatailor:GetChannelSchedule](#list_mediatailor-action-GetChannelSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPlaybackConfiguration  **
  - **IAM action:**  [mediatailor:GetPlaybackConfiguration](#list_mediatailor-action-GetPlaybackConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPrefetchSchedule  **
  - **IAM action:**  [mediatailor:GetPrefetchSchedule](#list_mediatailor-action-GetPrefetchSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAlerts  **
  - **IAM action:**  [mediatailor:ListAlerts](#list_mediatailor-action-ListAlerts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListChannels  **
  - **IAM action:**  [mediatailor:ListChannels](#list_mediatailor-action-ListChannels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListLiveSources  **
  - **IAM action:**  [mediatailor:ListLiveSources](#list_mediatailor-action-ListLiveSources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListPlaybackConfigurations  **
  - **IAM action:**  [mediatailor:ListPlaybackConfigurations](#list_mediatailor-action-ListPlaybackConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPrefetchSchedules  **
  - **IAM action:**  [mediatailor:ListPrefetchSchedules](#list_mediatailor-action-ListPrefetchSchedules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSourceLocations  **
  - **IAM action:**  [mediatailor:ListSourceLocations](#list_mediatailor-action-ListSourceLocations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [mediatailor:ListTagsForResource](#list_mediatailor-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListVodSources  **
  - **IAM action:**  [mediatailor:ListVodSources](#list_mediatailor-action-ListVodSources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutChannelPolicy  **
  - **IAM action:**  [mediatailor:PutChannelPolicy](#list_mediatailor-action-PutChannelPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   PutFunction  **
  - **IAM action:**  [mediatailor:TagResource](#list_mediatailor-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   PutPlaybackConfiguration  **
  - **IAM action:**  [mediatailor:PutPlaybackConfiguration](#list_mediatailor-action-PutPlaybackConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [mediatailor:TagResource](#list_mediatailor-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   StartChannel  **
  - **IAM action:**  [mediatailor:StartChannel](#list_mediatailor-action-StartChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopChannel  **
  - **IAM action:**  [mediatailor:StopChannel](#list_mediatailor-action-StopChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [mediatailor:TagResource](#list_mediatailor-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [mediatailor:UntagResource](#list_mediatailor-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateChannel  **
  - **IAM action:**  [mediatailor:UpdateChannel](#list_mediatailor-action-UpdateChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateLiveSource  **
  - **IAM action:**  [mediatailor:UpdateLiveSource](#list_mediatailor-action-UpdateLiveSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateProgram  **
  - **IAM action:**  [mediatailor:UpdateProgram](#list_mediatailor-action-UpdateProgram) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSourceLocation  **
  - **IAM action:**  [mediatailor:UpdateSourceLocation](#list_mediatailor-action-UpdateSourceLocation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateVodSource  **
  - **IAM action:**  [mediatailor:UpdateVodSource](#list_mediatailor-action-UpdateVodSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Elemental MediaTailor
<a name="list_mediatailor-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [ConfigureLogsForChannel](https://docs.aws.amazon.com/mediatailor/latest/apireference/configurelogs-channel.html)  **
  - **Description:** Grants permission to configure logs on the channel with the specified channel name
  - **Resource types (\*required):** [channel\*](#list_mediatailor-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ConfigureLogsForPlaybackConfiguration](https://docs.aws.amazon.com/mediatailor/latest/apireference/configurelogs-playbackconfiguration.html)  **
  - **Description:** Grants permission to configure logs for a playback configuration
  - **Resource types (\*required):** [playbackConfiguration\*](#list_mediatailor-resource-playbackConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateChannel](https://docs.aws.amazon.com/mediatailor/latest/apireference/channel-channelname.html)  **
  - **Description:** Grants permission to create a new channel
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediatailor-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_mediatailor-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLiveSource](https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname-livesource-livesourcename.html)  **
  - **Description:** Grants permission to create a new live source on the source location with the specified source location name
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediatailor-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_mediatailor-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePrefetchSchedule](https://docs.aws.amazon.com/mediatailor/latest/apireference/prefetchschedule-playbackconfigurationname-name.html)  **
  - **Description:** Grants permission to create a prefetch schedule for the playback configuration with the specified playback configuration name
  - **Resource types (\*required):** [playbackConfiguration\*](#list_mediatailor-resource-playbackConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateProgram](https://docs.aws.amazon.com/mediatailor/latest/apireference/channel-channelname-program-programname.html)  **
  - **Description:** Grants permission to create a new program on the channel with the specified channel name
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateSourceLocation](https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname.html)  **
  - **Description:** Grants permission to create a new source location
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediatailor-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_mediatailor-aws_TagKeys)
  - **Access level:** Write

- **   [CreateVodSource](https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname-vodsource-vodsourcename.html)  **
  - **Description:** Grants permission to create a new VOD source on the source location with the specified source location name
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediatailor-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_mediatailor-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteChannel](https://docs.aws.amazon.com/mediatailor/latest/apireference/channel-channelname.html)  **
  - **Description:** Grants permission to delete the channel with the specified channel name
  - **Resource types (\*required):** [channel\*](#list_mediatailor-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteChannelPolicy](https://docs.aws.amazon.com/mediatailor/latest/apireference/channel-channelname-policy.html)  **
  - **Description:** Grants permission to delete the IAM policy on the channel with the specified channel name
  - **Resource types (\*required):** [channel\*](#list_mediatailor-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeleteLiveSource](https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname-livesource-livesourcename.html)  **
  - **Description:** Grants permission to delete the live source with the specified live source name on the source location with the specified source location name
  - **Resource types (\*required):** [liveSource\*](#list_mediatailor-resource-liveSource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePlaybackConfiguration](https://docs.aws.amazon.com/mediatailor/latest/apireference/playbackconfiguration-name.html)  **
  - **Description:** Grants permission to delete the specified playback configuration
  - **Resource types (\*required):** [playbackConfiguration\*](#list_mediatailor-resource-playbackConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePrefetchSchedule](https://docs.aws.amazon.com/mediatailor/latest/apireference/prefetchschedule-playbackconfigurationname-name.html)  **
  - **Description:** Grants permission to delete a prefetch schedule for a playback configuration with the specified prefetch schedule name
  - **Resource types (\*required):** [playbackConfiguration\*](#list_mediatailor-resource-playbackConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [prefetchSchedule\*](#list_mediatailor-resource-prefetchSchedule) / **Condition keys:**  
  - **Access level:** Write

- **   [DeleteProgram](https://docs.aws.amazon.com/mediatailor/latest/apireference/channel-channelname-program-programname.html)  **
  - **Description:** Grants permission to delete the program with the specified program name on the channel with the specified channel name
  - **Resource types (\*required):** [program\*](#list_mediatailor-resource-program)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteSourceLocation](https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname.html)  **
  - **Description:** Grants permission to delete the source location with the specified source location name
  - **Resource types (\*required):** [sourceLocation\*](#list_mediatailor-resource-sourceLocation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteVodSource](https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname-vodsource-vodsourcename.html)  **
  - **Description:** Grants permission to delete the VOD source with the specified VOD source name on the source location with the specified source location name
  - **Resource types (\*required):** [vodSource\*](#list_mediatailor-resource-vodSource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeChannel](https://docs.aws.amazon.com/mediatailor/latest/apireference/channel-channelname.html)  **
  - **Description:** Grants permission to retrieve the channel with the specified channel name
  - **Resource types (\*required):** [channel\*](#list_mediatailor-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeLiveSource](https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname-livesource-livesourcename.html)  **
  - **Description:** Grants permission to retrieve the live source with the specified live source name on the source location with the specified source location name
  - **Resource types (\*required):** [liveSource\*](#list_mediatailor-resource-liveSource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeProgram](https://docs.aws.amazon.com/mediatailor/latest/apireference/channel-channelname-program-programname.html)  **
  - **Description:** Grants permission to retrieve the program with the specified program name on the channel with the specified channel name
  - **Resource types (\*required):** [program\*](#list_mediatailor-resource-program)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeSourceLocation](https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname.html)  **
  - **Description:** Grants permission to retrieve the source location with the specified source location name
  - **Resource types (\*required):** [sourceLocation\*](#list_mediatailor-resource-sourceLocation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeVodSource](https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname-vodsource-vodsourcename.html)  **
  - **Description:** Grants permission to retrieve the VOD source with the specified VOD source name on the source location with the specified source location name
  - **Resource types (\*required):** [vodSource\*](#list_mediatailor-resource-vodSource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetChannelPolicy](https://docs.aws.amazon.com/mediatailor/latest/apireference/channel-channelname-policy.html)  **
  - **Description:** Grants permission to read the IAM policy on the channel with the specified channel name
  - **Resource types (\*required):** [channel\*](#list_mediatailor-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetChannelSchedule](https://docs.aws.amazon.com/mediatailor/latest/apireference/channel-channelname-schedule.html)  **
  - **Description:** Grants permission to retrieve the schedule of programs on the channel with the specified channel name
  - **Resource types (\*required):** [channel\*](#list_mediatailor-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPlaybackConfiguration](https://docs.aws.amazon.com/mediatailor/latest/apireference/playbackconfiguration-name.html)  **
  - **Description:** Grants permission to retrieve the configuration for the specified name
  - **Resource types (\*required):** [playbackConfiguration\*](#list_mediatailor-resource-playbackConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPrefetchSchedule](https://docs.aws.amazon.com/mediatailor/latest/apireference/prefetchschedule-playbackconfigurationname-name.html)  **
  - **Description:** Grants permission to retrieve prefetch schedule for a playback configuration with the specified prefetch schedule name
  - **Resource types (\*required):** [playbackConfiguration\*](#list_mediatailor-resource-playbackConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [prefetchSchedule\*](#list_mediatailor-resource-prefetchSchedule) / **Condition keys:**  
  - **Access level:** Read

- **   [ListAlerts](https://docs.aws.amazon.com/mediatailor/latest/apireference/alerts.html)  **
  - **Description:** Grants permission to retrieve the list of alerts on a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListChannels](https://docs.aws.amazon.com/mediatailor/latest/apireference/channels.html)  **
  - **Description:** Grants permission to retrieve the list of existing channels
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListLiveSources](https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname-livesources.html)  **
  - **Description:** Grants permission to retrieve the list of existing live sources on the source location with the specified source location name
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListPlaybackConfigurations](https://docs.aws.amazon.com/mediatailor/latest/apireference/playbackconfigurations.html)  **
  - **Description:** Grants permission to retrieve the list of available configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPrefetchSchedules](https://docs.aws.amazon.com/mediatailor/latest/apireference/prefetchschedule-playbackconfigurationname.html)  **
  - **Description:** Grants permission to retrieve the list of prefetch schedules for a playback configuration
  - **Resource types (\*required):** [playbackConfiguration\*](#list_mediatailor-resource-playbackConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSourceLocations](https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocations.html)  **
  - **Description:** Grants permission to retrieve the list of existing source locations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/mediatailor/latest/apireference/tags-resourcearn.html)  **
  - **Description:** Grants permission to list the tags assigned to the specified playback configuration resource
  - **Resource types (\*required):** [channel](#list_mediatailor-resource-channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [liveSource](#list_mediatailor-resource-liveSource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [playbackConfiguration](#list_mediatailor-resource-playbackConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [sourceLocation](#list_mediatailor-resource-sourceLocation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [vodSource](#list_mediatailor-resource-vodSource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListVodSources](https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname-vodsources.html)  **
  - **Description:** Grants permission to retrieve the list of existing VOD sources on the source location with the specified source location name
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [PutChannelPolicy](https://docs.aws.amazon.com/mediatailor/latest/apireference/channel-channelname-policy.html)  **
  - **Description:** Grants permission to set the IAM policy on the channel with the specified channel name
  - **Resource types (\*required):** [channel\*](#list_mediatailor-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [PutPlaybackConfiguration](https://docs.aws.amazon.com/mediatailor/latest/apireference/playbackconfiguration.html)  **
  - **Description:** Grants permission to add a new configuration
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediatailor-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_mediatailor-aws_TagKeys)
  - **Access level:** Write

- **   [StartChannel](https://docs.aws.amazon.com/mediatailor/latest/apireference/channel-channelname-start.html)  **
  - **Description:** Grants permission to start the channel with the specified channel name
  - **Resource types (\*required):** [channel\*](#list_mediatailor-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopChannel](https://docs.aws.amazon.com/mediatailor/latest/apireference/channel-channelname-stop.html)  **
  - **Description:** Grants permission to stop the channel with the specified channel name
  - **Resource types (\*required):** [channel\*](#list_mediatailor-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/mediatailor/latest/apireference/tags-resourcearn.html)  **
  - **Description:** Grants permission to add tags to the specified playback configuration resource
  - **Resource types (\*required):** [channel](#list_mediatailor-resource-channel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediatailor-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediatailor-aws_TagKeys)
  - **Resource types (\*required):** [liveSource](#list_mediatailor-resource-liveSource) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediatailor-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediatailor-aws_TagKeys)
  - **Resource types (\*required):** [playbackConfiguration](#list_mediatailor-resource-playbackConfiguration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediatailor-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediatailor-aws_TagKeys)
  - **Resource types (\*required):** [sourceLocation](#list_mediatailor-resource-sourceLocation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediatailor-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediatailor-aws_TagKeys)
  - **Resource types (\*required):** [vodSource](#list_mediatailor-resource-vodSource) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_mediatailor-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediatailor-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/mediatailor/latest/apireference/tags-resourcearn.html)  **
  - **Description:** Grants permission to remove tags from the specified playback configuration resource
  - **Resource types (\*required):** [channel](#list_mediatailor-resource-channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediatailor-aws_TagKeys)
  - **Resource types (\*required):** [liveSource](#list_mediatailor-resource-liveSource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediatailor-aws_TagKeys)
  - **Resource types (\*required):** [playbackConfiguration](#list_mediatailor-resource-playbackConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediatailor-aws_TagKeys)
  - **Resource types (\*required):** [sourceLocation](#list_mediatailor-resource-sourceLocation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediatailor-aws_TagKeys)
  - **Resource types (\*required):** [vodSource](#list_mediatailor-resource-vodSource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mediatailor-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateChannel](https://docs.aws.amazon.com/mediatailor/latest/apireference/channel-channelname.html)  **
  - **Description:** Grants permission to update the channel with the specified channel name
  - **Resource types (\*required):** [channel\*](#list_mediatailor-resource-channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateLiveSource](https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname-livesource-livesourcename.html)  **
  - **Description:** Grants permission to update the live source with the specified live source name on the source location with the specified source location name
  - **Resource types (\*required):** [liveSource\*](#list_mediatailor-resource-liveSource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateProgram](https://docs.aws.amazon.com/mediatailor/latest/apireference/channel-channelname-program-programname.html)  **
  - **Description:** Grants permission to update the program with the specified program name on the channel with the specified channel name
  - **Resource types (\*required):** [program\*](#list_mediatailor-resource-program)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateSourceLocation](https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname.html)  **
  - **Description:** Grants permission to update the source location with the specified source location name
  - **Resource types (\*required):** [sourceLocation\*](#list_mediatailor-resource-sourceLocation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateVodSource](https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname-vodsource-vodsourcename.html)  **
  - **Description:** Grants permission to update the VOD source with the specified VOD source name on the source location with the specified source location name
  - **Resource types (\*required):** [vodSource\*](#list_mediatailor-resource-vodSource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Elemental MediaTailor
<a name="list_mediatailor-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [channel](https://docs.aws.amazon.com/mediatailor/latest/apireference/channel-channelname.html)  | arn:${Partition}:mediatailor:${Region}:${Account}:channel/${ChannelName} | [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_) | 
|  [liveSource](https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname-livesource-livesourcename.html)  | arn:${Partition}:mediatailor:${Region}:${Account}:liveSource/${SourceLocationName}/${LiveSourceName} | [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_) | 
|  [playbackConfiguration](https://docs.aws.amazon.com/mediatailor/latest/apireference/playbackconfiguration.html)  | arn:${Partition}:mediatailor:${Region}:${Account}:playbackConfiguration/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_) | 
|  [prefetchSchedule](https://docs.aws.amazon.com/mediatailor/latest/apireference/prefetchschedule-playbackconfigurationname-name.html)  | arn:${Partition}:mediatailor:${Region}:${Account}:prefetchSchedule/${ResourceId} |   | 
|  [program](https://docs.aws.amazon.com/mediatailor/latest/apireference/channel-channelname-program-programname.html)  | arn:${Partition}:mediatailor:${Region}:${Account}:program/${ChannelName}/${ProgramName} |   | 
|  [sourceLocation](https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname.html)  | arn:${Partition}:mediatailor:${Region}:${Account}:sourceLocation/${SourceLocationName} | [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_) | 
|  [vodSource](https://docs.aws.amazon.com/mediatailor/latest/apireference/sourcelocation-sourcelocationname-vodsource-vodsourcename.html)  | arn:${Partition}:mediatailor:${Region}:${Account}:vodSource/${SourceLocationName}/${VodSourceName} | [aws:ResourceTag/${TagKey}](#list_mediatailor-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Elemental MediaTailor
<a name="list_mediatailor-policy-keys"></a>

AWS Elemental MediaTailor defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 