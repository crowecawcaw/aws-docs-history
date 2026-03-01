# Requirements for AWS Elemental Inference

Your deployment might include using AWS Elemental Inference to apply foundational models to video content from AWS Elemental MediaLive channels. You must add these permissions to the MediaLiveAccessRole for the channel.

| Permissions                                                                                   | Service name in IAM | Actions                 |
| --------------------------------------------------------------------------------------------- | ------------------- | ----------------------- |
| Enables MediaLive to send content to Elemental Inference feeds and retrieve analysis results. | Elemental Inference | `PutMedia``GetMetadata` |
