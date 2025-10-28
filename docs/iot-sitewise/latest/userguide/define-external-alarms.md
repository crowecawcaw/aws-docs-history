# Define external alarms in AWS IoT SiteWise

External alarms contain the state of an alarm that you detect outside of AWS IoT SiteWise.

## Define an external alarm (console)

You can use the AWS IoT SiteWise console to define an external alarm on an existing asset model.
To define an external alarm on a new asset model, create the asset model, and then
complete these steps. For more information, see [Create asset models in AWS IoT SiteWise](create-asset-models.md "create-asset-models.md").

###### To define an alarm on an asset model

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Models**.
3. Choose the asset model for which to define an alarm.
4. Choose the **Alarm definitions** tab.
5. Choose **Add alarm**.
6. In **Alarm type options**, choose **External
   alarm**.
7. Enter a name for your alarm.
8. (Optional) Enter a description for your alarm.
9. Choose **Add alarm**.

## Define an external alarm (CLI)

You can use the AWS CLI to define an external alarm on a new or existing asset
model.

To add an external alarm to an asset model, you add an alarm composite model to the
asset model. An external alarm composite model specifies the `EXTERNAL` type
and doesn't specify an alarm source property. The following example composite alarm
defines an external temperature alarm.

```
{
  `...`
  "assetModelCompositeModels": [
    {
      "name": "BoilerTemperatureHighAlarm",
      "type": "AWS/ALARM",
      "properties": [
        {
          "name": "AWS/ALARM_TYPE",
          "dataType": "STRING",
          "type": {
            "attribute": {
              "defaultValue": "EXTERNAL"
            }
          }
        },
        {
          "name": "AWS/ALARM_STATE",
          "dataType": "STRUCT",
          "dataTypeSpec": "AWS/ALARM_STATE",
          "type": {
            "measurement": {}
          }
        }
      ]
    }
  ]
}
```

For more information about how to add a composite model to a new or existing asset
model, see the following:

- [Create an asset model (AWS CLI)](create-asset-models.md#create-asset-model-cli "create-asset-models.md#create-asset-model-cli")
- [Update an asset model, component model, or interface
  (AWS CLI)](update-asset-models.md#update-asset-model-cli "update-asset-models.md#update-asset-model-cli")

After you define the external alarm, you can ingest alarm state to assets based on the
asset model. For more information, see [Ingest an external alarm state in AWS IoT SiteWise](ingest-external-alarm-state.md "ingest-external-alarm-state.md").
