

# Understand asset properties in MQTT topics
<a name="mqtt-topics"></a>

Every asset property has a unique MQTT topic path in the following format.

```
$aws/sitewise/asset-models/{{assetModelId}}/assets/{{assetId}}/properties/{{propertyId}}
```

**Note**  
AWS IoT SiteWise doesn't support the `#` (multi-level) topic filter wildcard in the AWS IoT Core rules engine. You can use the `+` (single-level) wildcard. For example, you can use the following topic filter to match all updates for a particular asset model.  

```
$aws/sitewise/asset-models/{{assetModelId}}/assets/+/properties/+
```
To learn more about topic filter wildcards, see [Topics](https://docs.aws.amazon.com/iot/latest/developerguide/topics.html) in the *AWS IoT Core Developer Guide*.