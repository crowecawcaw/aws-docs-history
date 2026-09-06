

# Internet of Things services
<a name="sns-event-sources-iot"></a>

The following table descrives how Amazon SNS integrates with AWS IoT services, such as AWS IoT Core, AWS IoT Device Defender, AWS IoT Events, and AWS IoT Greengrass, to provide notifications for IoT events and alerts. 

These integrations allow you to effectively monitor device behavior, receive alerts for abnormal activities, and manage IoT devices with real-time updates and actions.


| AWS service | Benefit of using with Amazon SNS | 
| --- | --- | 
| [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html) – Provides the cloud services that connect your IoT devices to other devices and AWS Cloud services. | Receive notifications of AWS IoT Core events. For more information, see [Creating an Amazon SNS rule](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sns-rule.html) in the *AWS IoT Developer Guide*. | 
| [AWS IoT Device Defender](https://docs.aws.amazon.com/iot/latest/developerguide/device-defender.html) – Allows you to audit the configuration of your devices, monitor connected devices to detect abnormal behavior, and mitigate security risks. | Receive alarms when a device violates a behavior. For more information, see [How to use AWS IoT Device Defender detect](https://docs.aws.amazon.com/iot/latest/developerguide/detect-HowToHowTo.html) in the *AWS IoT Developer Guide*. | 
| [AWS IoT Events](https://docs.aws.amazon.com/iotevents/latest/developerguide/what-is-iotevents.html) – Lets you monitor your equipment or device fleets for failures or changes in operation, and trigger actions when such events occur. | Receive notifications of AWS IoT Events events. For more information, see [Amazon Simple Notification Service](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-other-aws-services.html#iotevents-sns) in the *AWS IoT Events Developer Guide*. | 
| [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v1/developerguide/what-is-iot-greengrass.html) – Extends AWS onto physical devices so they can act locally on the data they generate, while still using the cloud for management, analytics, and durable storage. | Receive notifications of AWS IoT Greengrass events. For more information, see [SNS connector](https://docs.aws.amazon.com/greengrass/v1/developerguide/sns-connector.html) in the *AWS IoT Greengrass Version 1 Developer Guide*. | 