

# MQCS metrics
<a name="eml-metrics-quality-score"></a>

MQCS metrics relate to the media quality confidence score that MediaLive generates for specific outputs. For more information about MQCS, see [Working with MQCS](mqcs.md).

**Topics**
+ [Minimum MQCS](#mqcs-min-mqcs)
+ [MQCS black frame detected](#mqcs-black-frame)
+ [MQCS continuity counter errors](#mqcs-continuity-counter)
+ [MQCS fill frame insertions](#mqcs-fill-frame)
+ [MQCS freeze frame detected](#mqcs-freeze-frame)
+ [MQCS SVQ](#mqcs-svq)
+ [MQCS video frame drop](#mqcs-video-frame-drop)

## Minimum MQCS
<a name="mqcs-min-mqcs"></a>

The minimum media quality confidence score (MQCS) in the period.

MQCS is a value from 0 to 100, with 0 being the lowest quality. The quality of the source directly affects the quality of each output encode that MediaLive sends to the downstream packager. The quality score is an amalgamation of the individual scores of each video and audio encode. 
+ Name: MinMQCS
+ Units: None
+ Meaning of no datapoints: The channel doesn’t have any output groups in which MediaLive is generating an MQCS. For example, the channel doesn’t have any CMAF Ingest output groups.
+ Meaning of zero: At least one encode in at least one output has a quality score of 0.
+ Supported dimension sets: ChannelD, Pipeline, OutputGroupName
+ Recommended statistic: Minimum, which identifies the lowest quality score during the period. 

## MQCS black frame detected
<a name="mqcs-black-frame"></a>

The black frame portion of the MQCS (media quality confidence score). 

This portion is calculated as follows: The input has transmitted one or more sequential video frames that are valid but black. The score gets lower as long as the problem persists. As soon as MediaLive receives one frame without this problem, the score reverts to 100.
+ Name: MqcsBlackFrameDetected
+ Units: None
+ Meaning of no datapoints: The channel doesn’t have any output groups in which MediaLive is generating an MQCS. For example, the channel doesn’t have any CMAF Ingest output groups.
+ Meaning of zero: At least one encode in at least one output has a quality score of 0.
+ Supported dimension sets: ChannelD, Pipeline
+ Recommended statistic: Minimum, which identifies the lowest quality score during the period. 

## MQCS continuity counter errors
<a name="mqcs-continuity-counter"></a>

The continuity counter errors portion of the MQCS (media quality confidence score). 

This portion is calculated as follows: The input has transmitted one or more sequential segments that contain continuity errors. The score gets lower as long as the problem persists. As soon as MediaLive receives one frame without this problem, the score reverts to 100.


+ Name: MqcsContinuityCounterErrors
+ Units: Percentage
+ Meaning of no datapoints: The channel doesn’t have any output groups in which MediaLive is generating an MQCS. For example, the channel doesn’t have any CMAF Ingest output groups.
+ Meaning of zero: At least one encode in at least one output has a quality score of 0.
+ Supported dimension sets: ChannelD, Pipeline
+ Recommended statistic: Minimum, which identifies the lowest quality score during the period. 

## MQCS fill frame insertions
<a name="mqcs-fill-frame"></a>

 The fill frame portion of the MQCS (media quality confidence score). 

This portion is calculated as follows: The input has transmitted one or more sequential video frames that are "fill frames". The score gets lower as long as the problem persists. As soon as MediaLive receives one frame without this problem, the score reverts to 100.
+ Name: MqcsFillFrameInsertion
+ Units: None
+ Meaning of no datapoints: The channel doesn’t have any output groups in which MediaLive is generating an MQCS. For example, the channel doesn’t have any CMAF Ingest output groups.
+ Meaning of zero: At least one encode in at least one output has a quality score of 0.
+ Supported dimension sets: ChannelD, Pipeline
+ Recommended statistic: Minimum, which identifies the lowest quality score during the period. 

## MQCS freeze frame detected
<a name="mqcs-freeze-frame"></a>

The freeze frame portion of the MQCS (media quality confidence score). 

This portion is calculated as follows: The input has transmitted one or more sequential video frames that are valid but frozen. The score gets lower as long as the problem persists. As soon as MediaLive receives one non-frozen frame, the score reverts to 100.


+ Name: MqcsFreezeFrameDetected
+ Units: None
+ Meaning of no datapoints: The channel doesn’t have any output groups in which MediaLive is generating an MQCS. For example, the channel doesn’t have any CMAF Ingest output groups.
+ Meaning of zero: At least one encode in at least one output has a quality score of 0.
+ Supported dimension sets: ChannelD, Pipeline
+ Recommended statistic: Minimum, which identifies the lowest quality score during the period. 

## MQCS SVQ
<a name="mqcs-svq"></a>

The SVQ portion of the MQCS (media quality confidence score). 

This portion is calculated as follows: The input has transmitted one or more sequential video frames that are affected by an SVQ (speed versus quality) problem. The score gets lower as long as the problem persists. As soon as MediaLive receives one frame without this problem, the score reverts to 100.
+ Name: MqcsSvq
+ Units: None
+ Meaning of no datapoints: The channel doesn’t have any output groups in which MediaLive is generating an MQCS. For example, the channel doesn’t have any CMAF Ingest output groups.
+ Meaning of zero: At least one encode in at least one output has a quality score of 0.
+ Supported dimension sets: ChannelD, Pipeline
+ Recommended statistic: Minimum, which identifies the lowest quality score during the period. 

## MQCS video frame drop
<a name="mqcs-video-frame-drop"></a>

The video frame drop portion of the MQCS (media quality confidence score). 

This portion is calculated as follows: The input has transmitted one or more sequential segments that contain dropped frames. The score gets lower as long as the problem persists. As soon as MediaLive receives one segment without dropped frames, the score reverts to 100.
+ Name: MqcsVideoFrameDrops
+ Units: None
+ Meaning of no datapoints: The channel doesn’t have any output groups in which MediaLive is generating an MQCS. For example, the channel doesn’t have any CMAF Ingest output groups.
+ Meaning of zero: At least one encode in at least one output has a quality score of 0.
+ Supported dimension sets: ChannelD, Pipeline
+ Recommended statistic: Minimum, which identifies the lowest quality score during the period. 