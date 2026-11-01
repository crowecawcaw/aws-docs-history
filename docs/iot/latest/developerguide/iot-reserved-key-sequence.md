

# Reserved character sequence in AWS IoT rule actions
<a name="iot-reserved-key-sequence"></a>

AWS IoT rules reserve the `^{` character sequence. You can't use it in rule action configuration fields. For example, AWS IoT rejects a field value such as `sensor^{data`. If a configuration field contains this sequence, the `CreateTopicRule` and `ReplaceTopicRule` operations fail with an error.

To resolve this error:

1. Remove or change the `^{` sequence in the rule action configuration field.

1. Resubmit the `CreateTopicRule` or `ReplaceTopicRule` request.

For more information, see [CreateTopicRule](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateTopicRule.html) and [ReplaceTopicRule](https://docs.aws.amazon.com/iot/latest/apireference/API_ReplaceTopicRule.html) in the *AWS IoT API Reference*.