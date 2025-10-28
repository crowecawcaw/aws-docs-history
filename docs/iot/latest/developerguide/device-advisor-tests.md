# Device Advisor test cases

Device Advisor
provides prebuilt tests in six categories.

- [TLS](device-advisor-tests-tls.md "device-advisor-tests-tls.md")
- [MQTT](device-advisor-tests-mqtt.md "device-advisor-tests-mqtt.md")
- [Shadow](device-advisor-tests-shadow.md "device-advisor-tests-shadow.md")
- [Job execution](device-advisor-tests-job-execution.md "device-advisor-tests-job-execution.md")
- [Permissions and policies](device-advisor-tests-permissions-policies.md "device-advisor-tests-permissions-policies.md")
- [Long duration tests](device-advisor-tests-long-duration.md "device-advisor-tests-long-duration.md")

## Device Advisor test cases to qualify for the AWS Device Qualification Program.

Your device must pass the following tests to qualify
according
to the [AWS Device Qualification
Program](https://aws.amazon.com/partners/programs/dqp/ "https://aws.amazon.com/partners/programs/dqp/").

###### Note

This is a revised list of the qualification tests.

- [TLS Connect](device-advisor-tests-tls.md#TLS_Connect "device-advisor-tests-tls.md#TLS_Connect") ("TLS Connect")​
- [TLS Incorrect Subject Name Server Cert](device-advisor-tests-tls.md#TLS_Incorrect_Subject_Name "device-advisor-tests-tls.md#TLS_Incorrect_Subject_Name") ("Incorrect Subject Common Name (CN) / Subject Alternative Name (SAN)")
- [TLS Unsecure Server Cert](device-advisor-tests-tls.md#TLS_Unsecure_Server_Cert "device-advisor-tests-tls.md#TLS_Unsecure_Server_Cert") ("Not Signed By Recognized CA")​
- [TLS Device Support for AWS IoT Cipher Suites](device-advisor-tests-tls.md#TLS_DeviceSupport_For_IOT "device-advisor-tests-tls.md#TLS_DeviceSupport_For_IOT") ("TLS Device Support for AWS IoT recommended Cipher Suites")
- [TLS Receive Maximum Size Fragments](device-advisor-tests-tls.md#TLS_MaximumSize "device-advisor-tests-tls.md#TLS_MaximumSize")("TLS Receive Maximum Size Fragments")
- [TLS Expired Server Cert](device-advisor-tests-tls.md#TLS_Expired_Server_Cert "device-advisor-tests-tls.md#TLS_Expired_Server_Cert")("Expired server certificate")
- [TLS Large Size Server Cert](device-advisor-tests-tls.md#TLS_LargeServerCert "device-advisor-tests-tls.md#TLS_LargeServerCert")("TLS large Size Server Certificate")
- [MQTT Connect](device-advisor-tests-mqtt.md#MQTT_Connect "device-advisor-tests-mqtt.md#MQTT_Connect") ("Device send CONNECT to AWS IoT Core (Happy case)")​
- [MQTT Subscribe](device-advisor-tests-mqtt.md#MQTT_Subscribe "device-advisor-tests-mqtt.md#MQTT_Subscribe") ("Can Subscribe (Happy Case)")​
- [MQTT Publish](device-advisor-tests-mqtt.md#MQTT_Publish "device-advisor-tests-mqtt.md#MQTT_Publish") ("QoS0 (Happy Case)")​
- [MQTT Connect Jitter Retries](device-advisor-tests-mqtt.md#MQTT_ConnectJitterBackoff "device-advisor-tests-mqtt.md#MQTT_ConnectJitterBackoff")("Device connect retries with jitter backoff - No CONNACK response")​
