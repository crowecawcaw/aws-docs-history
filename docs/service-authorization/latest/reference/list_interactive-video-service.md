

# Actions, resources, and condition keys for Amazon Interactive Video Service
<a name="list_interactive-video-service"></a>

Amazon Interactive Video Service (service prefix: `ivs`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/what-is.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/ivs/ivs.json) for this service.

**Topics**
+ [API operations defined by Amazon Interactive Video Service](#list_interactive-video-service-operations)
+ [Actions defined by Amazon Interactive Video Service](#list_interactive-video-service-actions-as-permissions)
+ [Resource types defined by Amazon Interactive Video Service](#list_interactive-video-service-resources-for-iam-policies)
+ [Condition keys for Amazon Interactive Video Service](#list_interactive-video-service-policy-keys)

## API operations defined by Amazon Interactive Video Service
<a name="list_interactive-video-service-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_interactive-video-service-actions-as-permissions).




- **   BatchGetChannel  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:BatchGetChannel](#list_interactive-video-service-action-BatchGetChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetStreamKey  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:BatchGetStreamKey](#list_interactive-video-service-action-BatchGetStreamKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchStartViewerSessionRevocation  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:BatchStartViewerSessionRevocation](#list_interactive-video-service-action-BatchStartViewerSessionRevocation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAdConfiguration  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:CreateAdConfiguration](#list_interactive-video-service-action-CreateAdConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ivs:TagResource](#list_interactive-video-service-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateChannel  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:CreateChannel](#list_interactive-video-service-action-CreateChannel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ivs:TagResource](#list_interactive-video-service-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreatePlaybackRestrictionPolicy  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:CreatePlaybackRestrictionPolicy](#list_interactive-video-service-action-CreatePlaybackRestrictionPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ivs:TagResource](#list_interactive-video-service-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRecordingConfiguration  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:CreateRecordingConfiguration](#list_interactive-video-service-action-CreateRecordingConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ivs:TagResource](#list_interactive-video-service-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateStreamKey  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:CreateStreamKey](#list_interactive-video-service-action-CreateStreamKey)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ivs:TagResource](#list_interactive-video-service-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteAdConfiguration  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:DeleteAdConfiguration](#list_interactive-video-service-action-DeleteAdConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteChannel  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:DeleteChannel](#list_interactive-video-service-action-DeleteChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePlaybackKeyPair  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:DeletePlaybackKeyPair](#list_interactive-video-service-action-DeletePlaybackKeyPair) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePlaybackRestrictionPolicy  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:DeletePlaybackRestrictionPolicy](#list_interactive-video-service-action-DeletePlaybackRestrictionPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRecordingConfiguration  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:DeleteRecordingConfiguration](#list_interactive-video-service-action-DeleteRecordingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteStreamKey  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:DeleteStreamKey](#list_interactive-video-service-action-DeleteStreamKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAdConfiguration  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:GetAdConfiguration](#list_interactive-video-service-action-GetAdConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetChannel  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:GetChannel](#list_interactive-video-service-action-GetChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPlaybackKeyPair  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:GetPlaybackKeyPair](#list_interactive-video-service-action-GetPlaybackKeyPair) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPlaybackRestrictionPolicy  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:GetPlaybackRestrictionPolicy](#list_interactive-video-service-action-GetPlaybackRestrictionPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRecordingConfiguration  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:GetRecordingConfiguration](#list_interactive-video-service-action-GetRecordingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetStream  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:GetStream](#list_interactive-video-service-action-GetStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetStreamKey  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:GetStreamKey](#list_interactive-video-service-action-GetStreamKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetStreamSession  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:GetStreamSession](#list_interactive-video-service-action-GetStreamSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ImportPlaybackKeyPair  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:ImportPlaybackKeyPair](#list_interactive-video-service-action-ImportPlaybackKeyPair)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ivs:TagResource](#list_interactive-video-service-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   InsertAdBreak  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:InsertAdBreak](#list_interactive-video-service-action-InsertAdBreak) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListAdConfigurations  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:ListAdConfigurations](#list_interactive-video-service-action-ListAdConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListChannels  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:ListChannels](#list_interactive-video-service-action-ListChannels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPlaybackKeyPairs  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:ListPlaybackKeyPairs](#list_interactive-video-service-action-ListPlaybackKeyPairs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPlaybackRestrictionPolicies  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:ListPlaybackRestrictionPolicies](#list_interactive-video-service-action-ListPlaybackRestrictionPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRecordingConfigurations  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:ListRecordingConfigurations](#list_interactive-video-service-action-ListRecordingConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStreamKeys  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:ListStreamKeys](#list_interactive-video-service-action-ListStreamKeys) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStreamSessions  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:ListStreamSessions](#list_interactive-video-service-action-ListStreamSessions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStreams  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:ListStreams](#list_interactive-video-service-action-ListStreams) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:ListTagsForResource](#list_interactive-video-service-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutMetadata  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:PutMetadata](#list_interactive-video-service-action-PutMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartViewerSessionRevocation  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:StartViewerSessionRevocation](#list_interactive-video-service-action-StartViewerSessionRevocation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopStream  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:StopStream](#list_interactive-video-service-action-StopStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:TagResource](#list_interactive-video-service-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:UntagResource](#list_interactive-video-service-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAdConfiguration  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:UpdateAdConfiguration](#list_interactive-video-service-action-UpdateAdConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateChannel  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:UpdateChannel](#list_interactive-video-service-action-UpdateChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePlaybackRestrictionPolicy  **
  - **SDK client:** ivs
  - **IAM action:**  [ivs:UpdatePlaybackRestrictionPolicy](#list_interactive-video-service-action-UpdatePlaybackRestrictionPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateEncoderConfiguration  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:CreateEncoderConfiguration](#list_interactive-video-service-action-CreateEncoderConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ivs:TagResource](#list_interactive-video-service-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateIngestConfiguration  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:CreateIngestConfiguration](#list_interactive-video-service-action-CreateIngestConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ivs:TagResource](#list_interactive-video-service-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateParticipantToken  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:CreateParticipantToken](#list_interactive-video-service-action-CreateParticipantToken) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateStage  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:CreateStage](#list_interactive-video-service-action-CreateStage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ivs:TagResource](#list_interactive-video-service-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateStorageConfiguration  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:CreateStorageConfiguration](#list_interactive-video-service-action-CreateStorageConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ivs:TagResource](#list_interactive-video-service-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteEncoderConfiguration  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:DeleteEncoderConfiguration](#list_interactive-video-service-action-DeleteEncoderConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIngestConfiguration  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:DeleteIngestConfiguration](#list_interactive-video-service-action-DeleteIngestConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePublicKey  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:DeletePublicKey](#list_interactive-video-service-action-DeletePublicKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteStage  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:DeleteStage](#list_interactive-video-service-action-DeleteStage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteStorageConfiguration  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:DeleteStorageConfiguration](#list_interactive-video-service-action-DeleteStorageConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisconnectParticipant  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:DisconnectParticipant](#list_interactive-video-service-action-DisconnectParticipant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetComposition  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:GetComposition](#list_interactive-video-service-action-GetComposition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEncoderConfiguration  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:GetEncoderConfiguration](#list_interactive-video-service-action-GetEncoderConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIngestConfiguration  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:GetIngestConfiguration](#list_interactive-video-service-action-GetIngestConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetParticipant  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:GetParticipant](#list_interactive-video-service-action-GetParticipant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPublicKey  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:GetPublicKey](#list_interactive-video-service-action-GetPublicKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetStage  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:GetStage](#list_interactive-video-service-action-GetStage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetStageSession  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:GetStageSession](#list_interactive-video-service-action-GetStageSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetStorageConfiguration  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:GetStorageConfiguration](#list_interactive-video-service-action-GetStorageConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ImportPublicKey  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:ImportPublicKey](#list_interactive-video-service-action-ImportPublicKey)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ivs:TagResource](#list_interactive-video-service-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   ListCompositions  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:ListCompositions](#list_interactive-video-service-action-ListCompositions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEncoderConfigurations  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:ListEncoderConfigurations](#list_interactive-video-service-action-ListEncoderConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIngestConfigurations  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:ListIngestConfigurations](#list_interactive-video-service-action-ListIngestConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListParticipantEvents  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:ListParticipantEvents](#list_interactive-video-service-action-ListParticipantEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListParticipantReplicas  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:ListParticipantReplicas](#list_interactive-video-service-action-ListParticipantReplicas) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListParticipants  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:ListParticipants](#list_interactive-video-service-action-ListParticipants) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPublicKeys  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:ListPublicKeys](#list_interactive-video-service-action-ListPublicKeys) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStageSessions  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:ListStageSessions](#list_interactive-video-service-action-ListStageSessions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStages  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:ListStages](#list_interactive-video-service-action-ListStages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStorageConfigurations  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:ListStorageConfigurations](#list_interactive-video-service-action-ListStorageConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:ListTagsForResource](#list_interactive-video-service-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartComposition  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:StartComposition](#list_interactive-video-service-action-StartComposition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ivs:TagResource](#list_interactive-video-service-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   StartParticipantReplication  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:StartParticipantReplication](#list_interactive-video-service-action-StartParticipantReplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopComposition  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:StopComposition](#list_interactive-video-service-action-StopComposition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopParticipantReplication  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:StopParticipantReplication](#list_interactive-video-service-action-StopParticipantReplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:TagResource](#list_interactive-video-service-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:UntagResource](#list_interactive-video-service-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateIngestConfiguration  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:UpdateIngestConfiguration](#list_interactive-video-service-action-UpdateIngestConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateStage  **
  - **SDK client:** ivs-realtime
  - **IAM action:**  [ivs:UpdateStage](#list_interactive-video-service-action-UpdateStage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Interactive Video Service
<a name="list_interactive-video-service-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchGetChannel](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_BatchGetChannel.html)  **
  - **Description:** Grants permission to get multiple channels simultaneously by channel ARN
  - **Resource types (\*required):** [Channel\*](#list_interactive-video-service-resource-Channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetStreamKey](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_BatchGetStreamKey.html)  **
  - **Description:** Grants permission to get multiple stream keys simultaneously by stream key ARN
  - **Resource types (\*required):** [Stream-Key\*](#list_interactive-video-service-resource-Stream-Key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchStartViewerSessionRevocation](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_BatchStartViewerSessionRevocation.html)  **
  - **Description:** Grants permission to perform StartViewerSessionRevocation on multiple channel ARN and viewer ID pairs simultaneously
  - **Resource types (\*required):** [Channel\*](#list_interactive-video-service-resource-Channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAdConfiguration](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_CreateAdConfiguration.html)  **
  - **Description:** Grants permission to create a new ad configuration
  - **Resource types (\*required):** [Ad-Configuration\*](#list_interactive-video-service-resource-Ad-Configuration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Access level:** Write

- **   [CreateChannel](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_CreateChannel.html)  **
  - **Description:** Grants permission to create a new channel and an associated stream key
  - **Resource types (\*required):** [Channel\*](#list_interactive-video-service-resource-Channel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Stream-Key\*](#list_interactive-video-service-resource-Stream-Key) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Access level:** Write

- **   [CreateEncoderConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_CreateEncoderConfiguration.html)  **
  - **Description:** Grants permission to create a new encoder configuration
  - **Resource types (\*required):** [Encoder-Configuration\*](#list_interactive-video-service-resource-Encoder-Configuration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Access level:** Write

- **   [CreateIngestConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_CreateIngestConfiguration.html)  **
  - **Description:** Grants permission to create a new ingest configuration
  - **Resource types (\*required):** [Ingest-Configuration\*](#list_interactive-video-service-resource-Ingest-Configuration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Access level:** Write

- **   [CreateParticipantToken](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_CreateParticipantToken.html)  **
  - **Description:** Grants permission to create a participant token
  - **Resource types (\*required):** [Stage\*](#list_interactive-video-service-resource-Stage)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePlaybackRestrictionPolicy](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_CreatePlaybackRestrictionPolicy.html)  **
  - **Description:** Grants permission to create a playback restriction policy
  - **Resource types (\*required):** [Playback-Restriction-Policy\*](#list_interactive-video-service-resource-Playback-Restriction-Policy)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRecordingConfiguration](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_CreateRecordingConfiguration.html)  **
  - **Description:** Grants permission to create a a new recording configuration
  - **Resource types (\*required):** [Recording-Configuration\*](#list_interactive-video-service-resource-Recording-Configuration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Access level:** Write

- **   [CreateStage](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_CreateStage.html)  **
  - **Description:** Grants permission to create a stage
  - **Resource types (\*required):** [Stage\*](#list_interactive-video-service-resource-Stage)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Access level:** Write

- **   [CreateStorageConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_CreateStorageConfiguration.html)  **
  - **Description:** Grants permission to create a new storage configuration
  - **Resource types (\*required):** [Storage-Configuration\*](#list_interactive-video-service-resource-Storage-Configuration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Access level:** Write

- **   [CreateStreamKey](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_CreateStreamKey.html)  **
  - **Description:** Grants permission to create a stream key
  - **Resource types (\*required):** [Stream-Key\*](#list_interactive-video-service-resource-Stream-Key)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAdConfiguration](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_DeleteAdConfiguration.html)  **
  - **Description:** Grants permission to delete an ad configuration for the specified ARN
  - **Resource types (\*required):** [Ad-Configuration\*](#list_interactive-video-service-resource-Ad-Configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteChannel](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_DeleteChannel.html)  **
  - **Description:** Grants permission to delete a channel and channel's stream keys
  - **Resource types (\*required):** [Channel\*](#list_interactive-video-service-resource-Channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Stream-Key\*](#list_interactive-video-service-resource-Stream-Key) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEncoderConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_DeleteEncoderConfiguration.html)  **
  - **Description:** Grants permission to delete an encoder configuration for the specified ARN
  - **Resource types (\*required):** [Encoder-Configuration\*](#list_interactive-video-service-resource-Encoder-Configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIngestConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_DeleteIngestConfiguration.html)  **
  - **Description:** Grants permission to delete an ingest configuration for the specified ARN
  - **Resource types (\*required):** [Ingest-Configuration\*](#list_interactive-video-service-resource-Ingest-Configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePlaybackKeyPair](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_DeletePlaybackKeyPair.html)  **
  - **Description:** Grants permission to delete the playback key pair for a specified ARN
  - **Resource types (\*required):** [Playback-Key-Pair\*](#list_interactive-video-service-resource-Playback-Key-Pair)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePlaybackRestrictionPolicy](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_DeletePlaybackRestrictionPolicy.html)  **
  - **Description:** Grants permission to delete the playback restriction policy for a specified ARN
  - **Resource types (\*required):** [Playback-Restriction-Policy\*](#list_interactive-video-service-resource-Playback-Restriction-Policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePublicKey](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_DeletePublicKey.html)  **
  - **Description:** Grants permission to delete the public key for the specified ARN
  - **Resource types (\*required):** [Public-Key\*](#list_interactive-video-service-resource-Public-Key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRecordingConfiguration](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_DeleteRecordingConfiguration.html)  **
  - **Description:** Grants permission to delete a recording configuration for the specified ARN
  - **Resource types (\*required):** [Recording-Configuration\*](#list_interactive-video-service-resource-Recording-Configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteStage](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_DeleteStage.html)  **
  - **Description:** Grants permission to delete the stage for a specified ARN
  - **Resource types (\*required):** [Stage\*](#list_interactive-video-service-resource-Stage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteStorageConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_DeleteStorageConfiguration.html)  **
  - **Description:** Grants permission to delete an storage configuration for the specified ARN
  - **Resource types (\*required):** [Storage-Configuration\*](#list_interactive-video-service-resource-Storage-Configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteStreamKey](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_DeleteStreamKey.html)  **
  - **Description:** Grants permission to delete the stream key for a specified ARN
  - **Resource types (\*required):** [Stream-Key\*](#list_interactive-video-service-resource-Stream-Key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisconnectParticipant](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_DisconnectParticipant.html)  **
  - **Description:** Grants permission to disconnect a participant from for the specified stage ARN
  - **Resource types (\*required):** [Stage\*](#list_interactive-video-service-resource-Stage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAdConfiguration](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_GetAdConfiguration.html)  **
  - **Description:** Grants permission to get the ad configuration for the specified ARN
  - **Resource types (\*required):** [Ad-Configuration\*](#list_interactive-video-service-resource-Ad-Configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetChannel](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_GetChannel.html)  **
  - **Description:** Grants permission to get the channel configuration for a specified channel ARN
  - **Resource types (\*required):** [Channel\*](#list_interactive-video-service-resource-Channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetComposition](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_GetComposition.html)  **
  - **Description:** Grants permission to get the composition for the specified ARN
  - **Resource types (\*required):** [Composition\*](#list_interactive-video-service-resource-Composition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEncoderConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_GetEncoderConfiguration.html)  **
  - **Description:** Grants permission to get the encoder configuration for the specified ARN
  - **Resource types (\*required):** [Encoder-Configuration\*](#list_interactive-video-service-resource-Encoder-Configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetIngestConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_GetIngestConfiguration.html)  **
  - **Description:** Grants permission to get the ingest configuration for the specified ARN
  - **Resource types (\*required):** [Ingest-Configuration\*](#list_interactive-video-service-resource-Ingest-Configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetParticipant](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_GetParticipant.html)  **
  - **Description:** Grants permission to get participant information for a specified stage ARN, session, and participant
  - **Resource types (\*required):** [Stage\*](#list_interactive-video-service-resource-Stage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPlaybackKeyPair](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_GetPlaybackKeyPair.html)  **
  - **Description:** Grants permission to get the playback keypair information for a specified ARN
  - **Resource types (\*required):** [Playback-Key-Pair\*](#list_interactive-video-service-resource-Playback-Key-Pair)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPlaybackRestrictionPolicy](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_GetPlaybackRestrictionPolicy.html)  **
  - **Description:** Grants permission to get the playback restriction policy for a specified ARN
  - **Resource types (\*required):** [Playback-Restriction-Policy\*](#list_interactive-video-service-resource-Playback-Restriction-Policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPublicKey](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_GetPublicKey.html)  **
  - **Description:** Grants permission to get the public key for the specified ARN
  - **Resource types (\*required):** [Public-Key\*](#list_interactive-video-service-resource-Public-Key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRecordingConfiguration](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_GetRecordingConfiguration.html)  **
  - **Description:** Grants permission to get the recording configuration for the specified ARN
  - **Resource types (\*required):** [Recording-Configuration\*](#list_interactive-video-service-resource-Recording-Configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetStage](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_GetStage.html)  **
  - **Description:** Grants permission to get stage information for a specified ARN
  - **Resource types (\*required):** [Stage\*](#list_interactive-video-service-resource-Stage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetStageSession](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_GetStageSession.html)  **
  - **Description:** Grants permission to get stage session information for a specified stage ARN and session
  - **Resource types (\*required):** [Stage\*](#list_interactive-video-service-resource-Stage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetStorageConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_GetStorageConfiguration.html)  **
  - **Description:** Grants permission to get the storage configuration for the specified ARN
  - **Resource types (\*required):** [Storage-Configuration\*](#list_interactive-video-service-resource-Storage-Configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetStream](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_GetStream.html)  **
  - **Description:** Grants permission to get information about the active (live) stream on a specified channel
  - **Resource types (\*required):** [Channel\*](#list_interactive-video-service-resource-Channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetStreamKey](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_GetStreamKey.html)  **
  - **Description:** Grants permission to get stream-key information for a specified ARN
  - **Resource types (\*required):** [Stream-Key\*](#list_interactive-video-service-resource-Stream-Key)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetStreamSession](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_GetStreamSession.html)  **
  - **Description:** Grants permission to get information about the stream session on a specified channel
  - **Resource types (\*required):** [Channel\*](#list_interactive-video-service-resource-Channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ImportPlaybackKeyPair](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_ImportPlaybackKeyPair.html)  **
  - **Description:** Grants permission to import the public key
  - **Resource types (\*required):** [Playback-Key-Pair\*](#list_interactive-video-service-resource-Playback-Key-Pair)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Access level:** Write

- **   [ImportPublicKey](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ImportPublicKey.html)  **
  - **Description:** Grants permission to import a public key
  - **Resource types (\*required):** [Public-Key\*](#list_interactive-video-service-resource-Public-Key)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Access level:** Write

- **   [InsertAdBreak](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_InsertAdBreak.html)  **
  - **Description:** Grants permission to request an ad insertion on a channel using an associated ad configuration
  - **Resource types (\*required):** [Channel\*](#list_interactive-video-service-resource-Channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListAdConfigurations](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_ListAdConfigurations.html)  **
  - **Description:** Grants permission to get summary information about ad configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListChannels](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_ListChannels.html)  **
  - **Description:** Grants permission to get summary information about channels
  - **Resource types (\*required):** [Channel\*](#list_interactive-video-service-resource-Channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCompositions](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ListCompositions.html)  **
  - **Description:** Grants permission to get summary information about compositions
  - **Resource types (\*required):** [Encoder-Configuration](#list_interactive-video-service-resource-Encoder-Configuration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Stage](#list_interactive-video-service-resource-Stage) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListEncoderConfigurations](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ListEncoderConfigurations.html)  **
  - **Description:** Grants permission to get summary information about encoder configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListIngestConfigurations](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ListIngestConfigurations.html)  **
  - **Description:** Grants permission to get summary information about ingest configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListParticipantEvents](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ListParticipantEvents.html)  **
  - **Description:** Grants permission to list participant events for a specified stage ARN, session, and participant
  - **Resource types (\*required):** [Stage\*](#list_interactive-video-service-resource-Stage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListParticipantReplicas](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ListParticipantReplicas.html)  **
  - **Description:** Grants permission to get summary information about participant replicas
  - **Resource types (\*required):** [Stage\*](#list_interactive-video-service-resource-Stage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListParticipants](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ListParticipants.html)  **
  - **Description:** Grants permission to list participants for a specified stage ARN and session
  - **Resource types (\*required):** [Stage\*](#list_interactive-video-service-resource-Stage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPlaybackKeyPairs](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_ListPlaybackKeyPairs.html)  **
  - **Description:** Grants permission to get summary information about playback key pairs
  - **Resource types (\*required):** [Playback-Key-Pair\*](#list_interactive-video-service-resource-Playback-Key-Pair)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPlaybackRestrictionPolicies](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_ListPlaybackRestrictionPolicies.html)  **
  - **Description:** Grants permission to get summary information about playback restriction policies
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPublicKeys](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ListPublicKeys.html)  **
  - **Description:** Grants permission to get summary information about public keys
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRecordingConfigurations](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_ListRecordingConfigurations.html)  **
  - **Description:** Grants permission to get summary information about recording configurations
  - **Resource types (\*required):** [Recording-Configuration\*](#list_interactive-video-service-resource-Recording-Configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListStageSessions](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ListStageSessions.html)  **
  - **Description:** Grants permission to list stage sessions for a specified stage ARN
  - **Resource types (\*required):** [Stage\*](#list_interactive-video-service-resource-Stage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListStages](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ListStages.html)  **
  - **Description:** Grants permission to get summary information about stages
  - **Resource types (\*required):** [Stage\*](#list_interactive-video-service-resource-Stage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListStorageConfigurations](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ListStorageConfigurations.html)  **
  - **Description:** Grants permission to get summary information about storage configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListStreamKeys](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_ListStreamKeys.html)  **
  - **Description:** Grants permission to get summary information about stream keys
  - **Resource types (\*required):** [Channel\*](#list_interactive-video-service-resource-Channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Stream-Key\*](#list_interactive-video-service-resource-Stream-Key) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListStreamSessions](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_ListStreamSessions.html)  **
  - **Description:** Grants permission to get summary information about streams sessions on a specified channel
  - **Resource types (\*required):** [Channel\*](#list_interactive-video-service-resource-Channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListStreams](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_ListStreams.html)  **
  - **Description:** Grants permission to get summary information about live streams
  - **Resource types (\*required):** [Channel\*](#list_interactive-video-service-resource-Channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to get information about the tags for a specified ARN
  - **Resource types (\*required):** [Ad-Configuration](#list_interactive-video-service-resource-Ad-Configuration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Channel](#list_interactive-video-service-resource-Channel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Composition](#list_interactive-video-service-resource-Composition) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Encoder-Configuration](#list_interactive-video-service-resource-Encoder-Configuration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Ingest-Configuration](#list_interactive-video-service-resource-Ingest-Configuration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Playback-Key-Pair](#list_interactive-video-service-resource-Playback-Key-Pair) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Playback-Restriction-Policy](#list_interactive-video-service-resource-Playback-Restriction-Policy) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Public-Key](#list_interactive-video-service-resource-Public-Key) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Recording-Configuration](#list_interactive-video-service-resource-Recording-Configuration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Stage](#list_interactive-video-service-resource-Stage) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Storage-Configuration](#list_interactive-video-service-resource-Storage-Configuration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Stream-Key](#list_interactive-video-service-resource-Stream-Key) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Access level:** Read

- **   [PutMetadata](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_PutMetadata.html)  **
  - **Description:** Grants permission to insert metadata into an RTMP stream for a specified channel
  - **Resource types (\*required):** [Channel\*](#list_interactive-video-service-resource-Channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartComposition](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_StartComposition.html)  **
  - **Description:** Grants permission to start a new composition
  - **Resource types (\*required):** [Channel](#list_interactive-video-service-resource-Channel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Encoder-Configuration\*](#list_interactive-video-service-resource-Encoder-Configuration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Stage\*](#list_interactive-video-service-resource-Stage) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Storage-Configuration](#list_interactive-video-service-resource-Storage-Configuration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Access level:** Write

- **   [StartParticipantReplication](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_StartParticipantReplication.html)  **
  - **Description:** Grants permission to start a new participant replication
  - **Resource types (\*required):** [Stage\*](#list_interactive-video-service-resource-Stage)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Access level:** Write

- **   [StartViewerSessionRevocation](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_StartViewerSessionRevocation.html)  **
  - **Description:** Grants permission to start the process of revoking the viewer session associated with a specified channel ARN and viewer ID
  - **Resource types (\*required):** [Channel\*](#list_interactive-video-service-resource-Channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopComposition](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_StopComposition.html)  **
  - **Description:** Grants permission to stop the composition for the specified ARN
  - **Resource types (\*required):** [Composition\*](#list_interactive-video-service-resource-Composition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopParticipantReplication](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_StopParticipantReplication.html)  **
  - **Description:** Grants permission to stop the participant replication for the specified ARN
  - **Resource types (\*required):** [Stage\*](#list_interactive-video-service-resource-Stage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopStream](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_StopStream.html)  **
  - **Description:** Grants permission to disconnect a streamer on a specified channel
  - **Resource types (\*required):** [Channel\*](#list_interactive-video-service-resource-Channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add or update tags for a resource with a specified ARN
  - **Resource types (\*required):** [Ad-Configuration](#list_interactive-video-service-resource-Ad-Configuration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Channel](#list_interactive-video-service-resource-Channel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Composition](#list_interactive-video-service-resource-Composition) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Encoder-Configuration](#list_interactive-video-service-resource-Encoder-Configuration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Ingest-Configuration](#list_interactive-video-service-resource-Ingest-Configuration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Playback-Key-Pair](#list_interactive-video-service-resource-Playback-Key-Pair) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Playback-Restriction-Policy](#list_interactive-video-service-resource-Playback-Restriction-Policy) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Public-Key](#list_interactive-video-service-resource-Public-Key) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Recording-Configuration](#list_interactive-video-service-resource-Recording-Configuration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Stage](#list_interactive-video-service-resource-Stage) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Storage-Configuration](#list_interactive-video-service-resource-Storage-Configuration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Stream-Key](#list_interactive-video-service-resource-Stream-Key) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_interactive-video-service-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags for a resource with a specified ARN
  - **Resource types (\*required):** [Ad-Configuration](#list_interactive-video-service-resource-Ad-Configuration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Channel](#list_interactive-video-service-resource-Channel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Composition](#list_interactive-video-service-resource-Composition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Encoder-Configuration](#list_interactive-video-service-resource-Encoder-Configuration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Ingest-Configuration](#list_interactive-video-service-resource-Ingest-Configuration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Playback-Key-Pair](#list_interactive-video-service-resource-Playback-Key-Pair) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Playback-Restriction-Policy](#list_interactive-video-service-resource-Playback-Restriction-Policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Public-Key](#list_interactive-video-service-resource-Public-Key) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Recording-Configuration](#list_interactive-video-service-resource-Recording-Configuration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Stage](#list_interactive-video-service-resource-Stage) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Storage-Configuration](#list_interactive-video-service-resource-Storage-Configuration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Resource types (\*required):** [Stream-Key](#list_interactive-video-service-resource-Stream-Key) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_interactive-video-service-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAdConfiguration](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_UpdateAdConfiguration.html)  **
  - **Description:** Grants permission to update an ad configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateChannel](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_UpdateChannel.html)  **
  - **Description:** Grants permission to update a channel's configuration
  - **Resource types (\*required):** [Channel\*](#list_interactive-video-service-resource-Channel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateIngestConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_UpdateIngestConfiguration.html)  **
  - **Description:** Grants permission to update ingest configuration for a specified ARN
  - **Resource types (\*required):** [Ingest-Configuration\*](#list_interactive-video-service-resource-Ingest-Configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePlaybackRestrictionPolicy](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_UpdatePlaybackRestrictionPolicy.html)  **
  - **Description:** Grants permission to update a playback restriction policy for a specified ARN
  - **Resource types (\*required):** [Playback-Restriction-Policy\*](#list_interactive-video-service-resource-Playback-Restriction-Policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateStage](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_UpdateStage.html)  **
  - **Description:** Grants permission to update a stage's configuration
  - **Resource types (\*required):** [Stage\*](#list_interactive-video-service-resource-Stage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Interactive Video Service
<a name="list_interactive-video-service-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Ad-Configuration](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_AdConfiguration.html)  | arn:${Partition}:ivs:${Region}:${Account}:ad-configuration/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_) | 
|  [Channel](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_Channel.html)  | arn:${Partition}:ivs:${Region}:${Account}:channel/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_) | 
|  [Composition](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_Composition.html)  | arn:${Partition}:ivs:${Region}:${Account}:composition/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_) | 
|  [Encoder-Configuration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_EncoderConfiguration.html)  | arn:${Partition}:ivs:${Region}:${Account}:encoder-configuration/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_) | 
|  [Ingest-Configuration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_IngestConfiguration.html)  | arn:${Partition}:ivs:${Region}:${Account}:ingest-configuration/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_) | 
|  [Playback-Key-Pair](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_PlaybackKeyPair.html)  | arn:${Partition}:ivs:${Region}:${Account}:playback-key/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_) | 
|  [Playback-Restriction-Policy](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_PlaybackRestrictionPolicy.html)  | arn:${Partition}:ivs:${Region}:${Account}:playback-restriction-policy/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_) | 
|  [Public-Key](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_PublicKey.html)  | arn:${Partition}:ivs:${Region}:${Account}:public-key/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_) | 
|  [Recording-Configuration](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_RecordingConfiguration.html)  | arn:${Partition}:ivs:${Region}:${Account}:recording-configuration/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_) | 
|  [Stage](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_Stage.html)  | arn:${Partition}:ivs:${Region}:${Account}:stage/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_) | 
|  [Storage-Configuration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_StorageConfiguration.html)  | arn:${Partition}:ivs:${Region}:${Account}:storage-configuration/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_) | 
|  [Stream-Key](https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_StreamKey.html)  | arn:${Partition}:ivs:${Region}:${Account}:stream-key/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_interactive-video-service-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Interactive Video Service
<a name="list_interactive-video-service-policy-keys"></a>

Amazon Interactive Video Service defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags associated with the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 