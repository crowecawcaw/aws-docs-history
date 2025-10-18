# CompositeAlarm

The details about a composite alarm.


## Contents





**ActionsEnabled** 


Indicates whether actions should be executed during any changes to the alarm
 state.


Type: Boolean


Required: No




**ActionsSuppressedBy** 


 When the value is `ALARM`, it means that the actions are suppressed
 because the suppressor alarm is in `ALARM` When the value is
 `WaitPeriod`, it means that the actions are suppressed because the
 composite alarm is waiting for the suppressor alarm to go into into the
 `ALARM` state. The maximum waiting time is as specified in
 `ActionsSuppressorWaitPeriod`. After this time, the composite alarm
 performs its actions. When the value is `ExtensionPeriod`, it means that the
 actions are suppressed because the composite alarm is waiting after the suppressor alarm
 went out of the `ALARM` state. The maximum waiting time is as specified in
 `ActionsSuppressorExtensionPeriod`. After this time, the composite alarm
 performs its actions. 


Type: String


Valid Values: `WaitPeriod | ExtensionPeriod | Alarm`



Required: No




**ActionsSuppressedReason** 


 Captures the reason for action suppression. 


Type: String


Length Constraints: Minimum length of 0. Maximum length of 1024.


Required: No




**ActionsSuppressor** 


 Actions will be suppressed if the suppressor alarm is in the `ALARM`
 state. `ActionsSuppressor` can be an AlarmName or an Amazon Resource Name
 (ARN) from an existing alarm. 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1600.


Required: No




**ActionsSuppressorExtensionPeriod** 


 The maximum time in seconds that the composite alarm waits after suppressor alarm
 goes out of the `ALARM` state. After this time, the composite alarm performs
 its actions. 


###### Important


`ExtensionPeriod` is required only when `ActionsSuppressor` is
 specified. 


Type: Integer


Required: No




**ActionsSuppressorWaitPeriod** 


 The maximum time in seconds that the composite alarm waits for the suppressor alarm
 to go into the `ALARM` state. After this time, the composite alarm performs
 its actions. 


###### Important


`WaitPeriod` is required only when `ActionsSuppressor` is
 specified. 


Type: Integer


Required: No




**AlarmActions** 


The actions to execute when this alarm transitions to the ALARM state from any other
 state. Each action is specified as an Amazon Resource Name (ARN).


Type: Array of strings


Array Members: Maximum number of 5 items.


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**AlarmArn** 


The Amazon Resource Name (ARN) of the alarm.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1600.


Required: No




**AlarmConfigurationUpdatedTimestamp** 


The time stamp of the last update to the alarm configuration.


Type: Timestamp


Required: No




**AlarmDescription** 


The description of the alarm.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 1024.


Required: No




**AlarmName** 


The name of the alarm.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 255.


Required: No




**AlarmRule** 


The rule that this alarm uses to evaluate its alarm state.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 10240.


Required: No




**InsufficientDataActions** 


The actions to execute when this alarm transitions to the INSUFFICIENT\_DATA state from
 any other state. Each action is specified as an Amazon Resource Name (ARN).


Type: Array of strings


Array Members: Maximum number of 5 items.


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**OKActions** 


The actions to execute when this alarm transitions to the OK state from any other
 state. Each action is specified as an Amazon Resource Name (ARN).


Type: Array of strings


Array Members: Maximum number of 5 items.


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**StateReason** 


An explanation for the alarm state, in text format.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 1023.


Required: No




**StateReasonData** 


An explanation for the alarm state, in JSON format.


Type: String


Length Constraints: Minimum length of 0. Maximum length of 4000.


Required: No




**StateTransitionedTimestamp** 


 The timestamp of the last change to the alarm's `StateValue`. 


Type: Timestamp


Required: No




**StateUpdatedTimestamp** 


Tracks the timestamp of any state update, even if `StateValue` doesn't
 change.


Type: Timestamp


Required: No




**StateValue** 


The state value for the alarm.


Type: String


Valid Values: `OK | ALARM | INSUFFICIENT_DATA`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/CompositeAlarm "https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/CompositeAlarm")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/CompositeAlarm "https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/CompositeAlarm")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/CompositeAlarm "https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/CompositeAlarm")
