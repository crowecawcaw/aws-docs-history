# Detect metrics export pricing

When you publish cloud-side, device-side, or custom metrics to an MQTT
topic that you configure, you will not incur charges for this step of the export
process. However, in the subsequent steps when you transfer the
published metrics to a destination of your choice, by using Rules Engine or
Messaging, you will incur costs based on the transfer method you choose. AWS IoT Device Defender publishes batched metrics to MQTT topics as a single message that
contains metrics data for multiple devices, which helps control costs. For more information regarding pricing, see the [AWS Pricing Calculator.](https://calculator.aws/#/addService "https://calculator.aws/#/addService")
