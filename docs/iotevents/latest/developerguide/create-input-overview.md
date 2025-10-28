End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Create an input for models in AWS IoT Events

When you construct the inputs for your models, we recommend gathering files that contain
sample message payloads that your devices or processes send to report their health status.
Having these files helps you define the inputs that are required.

You can create an input through multiple methods that are described in this
section.

## Create a JSON input file

1. To get started, create a file named `input.json` on your local
   file system with the following contents:

```
{
  "motorid": "Fulton-A32",
  "sensorData": {
    "pressure": 23,
    "temperature": 47
  }
}
```

2. Now that you have this starter `input.json` file, you can create
   an input. There are two ways to create an input. You can create an input by using the
   navigation pane in the [AWS IoT Events console](https://console.aws.amazon.com/iotevents/ "https://console.aws.amazon.com/iotevents/") . Or, you can create an input within the detector model after it's
   created.

## Create and configure an input

Learn how to create an _input_, for an alarm model or a detector
model.

1. Log into the [AWS IoT Events console](https://console.aws.amazon.com/iotevents/ "https://console.aws.amazon.com/iotevents/") or
   select the option to Create a new AWS IoT Events account.
2. In the AWS IoT Events console, in the upper left corner, select and expand the navigation
   pane.
3. In the left navigation pane, select **Inputs**.
4. In the right corner of the console, choose **Create input**.
5. Provide a unique**InputName**.
6. _Optional_ – enter a **Description** for
   your input.
7. To **Upload a JSON file**, select the
   `input.json` file that you created in the overview for [Create a JSON input file](#create-input-file "#create-input-file"). **Choose
   input attributes** appears with a list of your entered attributes.
8. For **Choose input attributes**, select the attributes to use, and
   choose **Create**. In this example, we select
   **motorid** and **sensorData.pressure**.
9. _Optional_ – Add relevant **Tags** to the
   input.

###### Note

You can also create additional inputs within the detector model in the [AWS IoT Events console](https://console.aws.amazon.com/iotevents/ "https://console.aws.amazon.com/iotevents/") . For more information, see
[Create an input within the Detector Model in AWS IoT Events](iotevents-detector-input.md "iotevents-detector-input.md").
