

# Reserved character sequence in AWS IoT rule actions
<a name="iot-reserved-key-sequence"></a>

AWS IoT rules reserve the `^{` character sequence. You can't use it in rule action configuration fields. If a configuration field contains this sequence, the `CreateTopicRule` and `ReplaceTopicRule` operations fail with an error. Remove or change the sequence, then resubmit the request.