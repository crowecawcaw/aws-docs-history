# Device Advisor

[Device Advisor](https://aws.amazon.com/iot-core/features/ "https://aws.amazon.com/iot-core/features/") is a cloud-based,
fully managed test capability for validating IoT devices during device software development.
Device Advisor provides pre-built tests that you can use to validate IoT devices for reliable and
secure connectivity with AWS IoT Core, before deploying devices to production.
Device Advisor’s pre-built tests help you validate your device software against best practices for usage of
[TLS](protocols.md "protocols.md"), [MQTT](protocols.md "protocols.md"),
[Device Shadow](iot-device-shadows.md "iot-device-shadows.md"),
and [IoT Jobs](iot-jobs.md "iot-jobs.md").
You can also download signed qualification reports to submit to the
AWS Partner Network to get your device qualified for the [AWS Partner Device Catalog](https://devices.amazonaws.com/ "https://devices.amazonaws.com/") without the need
to send your device in and wait for it to be tested.

###### Note

Device Advisor is supported in us-east-1, us-west-2, ap-northeast-1, and eu-west-1 regions.

Device Advisor supports devices and clients that use the MQTT and the MQTT over WebSocket Secure (WSS) protocols
to publish and subscribe to messages. All protocols support IPv4 and IPv6.

Device Advisor supports RSA server certificates.

Any device that has been built to connect to AWS IoT Core can take advantage of Device Advisor. You
can access Device Advisor from the [AWS IoT console](https://us-east-1.console.aws.amazon.com/iot/home?region=us-east-1#/deviceadvisor/intro "https://us-east-1.console.aws.amazon.com/iot/home?region=us-east-1#/deviceadvisor/intro"), or by using the AWS CLI or SDK. When you're ready to test your
device, register it with AWS IoT Core and configure the device software with the Device Advisor
endpoint. Then choose the prebuilt tests, configure them, run the tests on your device, and
get the test results along with detailed logs or a qualification report.

Device Advisor is a test endpoint in the AWS cloud. You can test your devices by configuring them
to connect to the test endpoint provided by the Device Advisor. After a device is configured to
connect to the test endpoint, you can visit the Device Advisor’s console or use the AWS SDK to
choose the tests you want to run on your devices. Device Advisor then manages the full lifecycle of
a test, including the provisioning of resources, scheduling of the test process, managing
the state machine, recording the device behavior, logging the results, and providing the
final results in form of a test report.

**TLS protocols**

Transport Layer Security (TLS) protocol is used to encrypt confidential data over insecure
networks like the internet. The TLS protocol is the successor of the Secure Sockets Layer
(SSL) protocol.

Device Advisor supports the following TLS protocols:

- TLS 1.3 (recommended)
- TLS 1.2
  **Protocols, port mappings, and authentication**

The device communication protocol is used by a device or a client to connect
to the message broker by using a device endpoint. The following table lists the
protocols that the Device Advisor endpoints support and the authentication methods
and ports used.

| Protocols, authentication, and port mappings | Protocol           | Operations supported     | Authentication | Port             | ALPN protocol name |
| -------------------------------------------- | ------------------ | ------------------------ | -------------- | ---------------- | ------------------ |
| MQTT over WebSocket                          | Publish, Subscribe | Signature Version 4      | 443            | N/A              |
| MQTT                                         | Publish, Subscribe | X.509 client certificate | 8883           | `x-amzn-mqtt-ca` |
| MQTT                                         | Publish, Subscribe | X.509 client certificate | 443            | N/A              |

###### This chapter contains the following sections:

- [Setting up](device-advisor-setting-up.md "device-advisor-setting-up.md")
- [Getting started with Device Advisor in the console](da-console-guide.md "da-console-guide.md")
- [Device Advisor workflow](device-advisor-workflow.md "device-advisor-workflow.md")
- [Device Advisor detailed console workflow](device-advisor-console-tutorial.md "device-advisor-console-tutorial.md")
- [Long duration tests console workflow](device-advisor-long-duration-console-tutorial.md "device-advisor-long-duration-console-tutorial.md")
- [Device Advisor VPC endpoints
  (AWS PrivateLink)](device-advisor-vpc-endpoint.md "device-advisor-vpc-endpoint.md")
- [Device Advisor test cases](device-advisor-tests.md "device-advisor-tests.md")
