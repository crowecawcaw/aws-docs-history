# Data encryption in AWS IoT

Data protection refers to protecting data while in-transit (as it travels to and from
AWS IoT Core) and at rest (while it is stored on devices or by other AWS services). All data sent
to AWS IoT Core is sent over an TLS connection using MQTT, HTTPS, and WebSocket protocols, making
it secure by default while in transit. AWS IoT Core collects data from devices and then sends it to other
AWS services for further processing. For more information about data encryption on other
AWS services, see the security documentation for that service. For more information, see [Data encryption at rest](encryption-at-rest.md "encryption-at-rest.md").

FreeRTOS provides a PKCS#11 library that abstracts key storage, accessing cryptographic
objects and managing sessions. It is your responsibility to use this library to encrypt data
at rest on your devices. For more information, see [FreeRTOS Public Key Cryptography Standard (PKCS)
#11 Library](../../../freertos/latest/userguide/security-pkcs.md "../../../freertos/latest/userguide/security-pkcs.md").
