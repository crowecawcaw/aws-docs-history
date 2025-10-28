# Trigger custom actions on

anomalous behavior (AWS Management Console)

You can enable **custom actions in response to anomalous
behavior** by using **AWS IoT SiteWise MQTT notifications** in
combination with **AWS IoT Core**.

Follow these steps to configure MQTT notifications in AWS IoT SiteWise, and trigger a custom action
in AWS IoT Core based on inference results:

- Locate the asset in AWS IoT SiteWise, where the inference runs.
- Identify the property you used as the `resultProperty` when creating the
  computation model. Enable **MQTT Notification** for this property.
- Once you enable **MQTT Notification**, copy the
  **Notification Topic** that AWS IoT SiteWise generates.
- Navigate to AWS IoT Core. Under MQTT test client, subscribe to the copied
  **Notification Topic** to monitor the incoming messages.
- Create an **AWS IoT Core Rule** to **Process Inference
  Results**. (This ensures that actions are triggered only if the system detects
  an anomaly). Replace `notification-topic` with the **Notification
  Topic** that AWS IoT SiteWise generates.

```
SELECT * FROM "notification-topic"
  WHERE indexof(get(get(payload.values, 0).value, 'stringValue'), "NO_ANOMALY_DETECTED") < 0
```

Configure the rule to trigger any of the actions that AWS IoT Core supports. Learn more about
the actions supported by [AWS IoT Core](../../../iot/latest/developerguide/iot-rule-actions.md "../../../iot/latest/developerguide/iot-rule-actions.md").
