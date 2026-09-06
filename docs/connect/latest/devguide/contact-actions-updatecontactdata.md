

# UpdateContactData
<a name="contact-actions-updatecontactdata"></a>

Sets a collection of connect defined attributes on specified contact. With this type of operation, either all attributes are set or none are set.

## Parameter object
<a name="updatecontactdata-parameter"></a>

```
"Parameters": 
{
        "Name": [Optional] The name of the contact. It is a string. May be set statically or dynamically.
        "Description": [Optional] The description of the contact. It is a string. 
        "LanguageCode": [Optional] The language to use for current contact.
        "CustomerId": [Optional] The customer id associated with the contact.
        "References": [Optional] { an Object that holds the references to be set. 
          "Type": "Value" Both the key and value may be defined statically or dynamically.
        },
        "IsVoiceIdStreamingEnabled": [Optional] Enable to start streaming audio from customer channel to Voice ID. It is a string. "TRUE" and "FALSE" are the only valid values.
        "IsVoiceAuthenticationEnabled": [Optional] Enable authentication by comparing voiceprint of the caller to the enrolled voiceprint of the claimed identity.It is a string. "TRUE" and "FALSE" are the only valid values.
        "IsFraudDetectionEnabled": [Optional] Enable detection for impersonation attempts and presence of known fraudsters. It is a string. "TRUE" and "FALSE" are the only valid values.
        "VoiceAuthenticationThreshold": [Optional] Threshold to validate against confidence score of a voice match. It is a string. Value must be between 0 and 100.
        "VoiceAuthenticationResponseTime": [Optional] Define required minimum caller speech seconds for voice authentication. It is a string. Value must be between 5 and 10.
        "FraudDetectionThreshold": [Optional] The threshold you set for fraud detection is used to measure risk. Scores higher than the threshold are reported as higher risk. Scores lower than the threshold are reported as lower risk. Raising the threshold lowers false positive rates (makes result more certain), but raises false negative rates. It is a string. Value must be between 0 and 100.
        "WatchlistId": [Optional] Identifier of watchlist to use when evaluating the voice session. It is a string. Value must be between 0 and 100.
        "WisdomSessionArn": [Optional] A session ARN provided by Connect Customer Wisdom for agent assistance. It is a string.
        "TargetContact": [Required] Target contact on which given attributes should be set. It is a string. "Current" or "Related" are the only valid values.    
}
```

## Results and conditions
<a name="updatecontactdata-results"></a>

None. No conditions are supported.

## Errors
<a name="updatecontactdata-errors"></a>
+ NoMatchingError - if no other Error matches.

## Restrictions
<a name="updatecontactdata-restrictions"></a>

This action is supported on all channels and in all flow types.

## Corresponding blocks in the UI
<a name="updatecontactdata-ui"></a>
+  [Set contact attributes](https://docs.aws.amazon.com/connect/latest/adminguide/set-contact-attributes.html) 