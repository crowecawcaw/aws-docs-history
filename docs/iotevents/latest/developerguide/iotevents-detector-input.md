End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Create an input within the Detector Model in AWS IoT Events

Detector inputs in AWS IoT Events serve as the bridge between your data sources and detector
models. Detector inputs provide the raw data that powers the event detection and automation
capabilities of AWS IoT Events. Learn to configure detector inputs to help your models respond
accurately to real-world events and conditions in your IoT ecosystem.

This section shows how to define an _input_ for a detector model to
receive telemetry data, or messages.

###### To define an input for a detector model

1. Open the [AWS IoT Events console](https://console.aws.amazon.com/iotevents/ "https://console.aws.amazon.com/iotevents/").
2. In the AWS IoT Events console, choose **Create detector model**.
3. Choose **Create new**.
4. Choose **Create input**.
5. For the input, enter an **InputName**, an optional
   **Description**, and choose **Upload file**. In the
   dialog box that displays, select the `input.json` file that you
   created in the overview for [Create a JSON input file](create-input-overview.md#create-input-file "create-input-overview.md#create-input-file").
6. For **Choose input attributes**, select the attributes to use, and
   choose **Create**. In this example, we select
   **motorId** and **sensorData.pressure**.
