# TLS

Use these tests to determine if the transport layer security protocol (TLS) between your devices and AWS IoT is secure.

###### Note

Device Advisor now supports TLS 1.3.

## Happy Path

**TLS Connect**

Validates if the device under test can complete the TLS handshake
to AWS IoT. This test doesn't validate the MQTT implementation of the
client device.

###### Example API test case definition:

###### Note

`EXECUTION_TIMEOUT` has a default value of 5
minutes. For best results, we recommend a timeout value of 2
minutes.

```
"tests":[
   {
      "name":"`my_tls_connect_test`",
      "configuration": {
         // optional:
         "EXECUTION_TIMEOUT":"`300`",  //in seconds
      },
      "test":{
         "id":"TLS_Connect",
         "version":"0.0.0"
      }
   }
]
```

###### Example Test case outputs:

- Pass — The device under test completed TLS handshake
  with AWS IoT.
- Pass with warnings — The device under test completed TLS
  handshake with AWS IoT, but there were TLS warning
  messages from the device or AWS IoT.
- Fail — The device under test failed to complete TLS
  handshake with AWS IoT due to handshake error.

**TLS Receive Maximum Size Fragments**

This test case validates that your device can receive and process
TLS maximum size fragments. Your test device must subscribe to a
pre-configured topic with QoS 1 to receive a large payload. You can
customize the payload with the configuration
`${payload}`.

###### Example API test case definition:

###### Note

`EXECUTION_TIMEOUT` has a default value of 5 minutes.
For best results, we recommend a timeout value of 2 minutes.

```
"tests":[
   {
      "name":"TLS Receive Maximum Size Fragments",
      "configuration": {
         // optional:
         "EXECUTION_TIMEOUT":"`300`",  //in seconds
         "PAYLOAD_FORMAT":"{"message":"${payload}"}", // A string with a placeholder ${payload}, or leave it empty to receive a plain string.
         "TRIGGER_TOPIC": "test_1" // A topic to which a device will subscribe, and to which a test case will publish a large payload.
      },
      "test":{
         "id":"TLS_Receive_Maximum_Size_Fragments",
         "version":"0.0.0"
      }
   }
]
```

## Cipher Suites

**TLS Device Support for AWS IoT recommended Cipher Suites**

Validates that the cipher suites in the TLS Client Hello message from
the device under test contains the recommended [AWS IoT cipher suites](transport-security.md "transport-security.md"). It
provides more insights into cipher suites supported by the
device.

###### Example API test case definition:

###### Note

`EXECUTION_TIMEOUT` has a default value of 5
minutes. We recommend a timeout value of 2 minutes.

```
"tests":[
   {
      "name":"`my_tls_support_aws_iot_cipher_suites_test`",
      "configuration": {
         // optional:
         "EXECUTION_TIMEOUT":"`300`",  // in seconds
      },
      "test":{
         "id":"TLS_Support_AWS_IoT_Cipher_Suites",
         "version":"0.0.0"
      }
   }
]
```

###### Example Test case outputs:

- Pass — The device under test cipher suites contain at
  least one of the recommended AWS IoT cipher suite and
  don't contain any unsupported cipher suites.
- Pass with warnings
  — The device cipher suites contain at least one
  AWS IoT cipher suite but:

      1. It doesn't contain any of the recommended
       cipher suites
      2. It contains cipher suites that aren't
       supported by AWS IoT.

  We suggest that you verify that any unsupported cipher
  suites are safe.

- Fail — The device under test cipher suites doesn't
  contain any of the AWS IoT supported cipher suites.

## Larger Size Server Certificate

**TLS large Size Server Certificate**

Validates at your device can complete the TLS handshake with AWS IoT
when it receives and processes a larger size server certificate. The
size of the server certificate (in bytes) used by this test is
larger than what is currently used in the **TLS
Connect** test case and IoT Core by 20 During this test
case, AWS IoT tests your device’s buffer space for TLS If the buffer
space is large enough, the TLS handshake ompletes without errors.
This test esn't validate the MQTT implementation of the device. The
test case ds after the TLS handshake process completes.

###### Example API test case definition:

###### Note

`EXECUTION_TIMEOUT` has a default value of 5
minutes. For best results, we recommend a timeout value of 2
minutes. If this test case fails but the **TLS Connect** test case passes, we
recommend you increase your device’s buffer space limit for
TLS Increasing the buffer space limit sures that your device
can process a larger size server certificate in case the
size increases.

```
"tests":[
   {
      "name":"`my_tls_large_size_server_cert_test`",
      "configuration": {
         // optional:
         "EXECUTION_TIMEOUT":"`300`",  // in seconds
      },
      "test":{
         "id":"TLS_Large_Size_Server_Cert",
         "version":"0.0.0"
      }
   }
]
```

###### Example Test case outputs:

- Pass — The
  device under test completed the TLS handshake with
  AWS IoT.
- Pass with warnings
  — The device under test completed the TLS
  handshake with AWS IoT, but there are TLS warning messages
  either from the device or AWS IoT.
- Fail — The
  device under test failed to complete the TLS handshake
  with AWS IoT because of an error during the handshake
  process.

## TLS Unsecure Server Cert

**Not Signed By Recognized CA**

Validates that the device under test closes the connection if it's
presented with a server certificate without a valid signature from
the ATS CA. A device should only connect to an endpoint that
presents a valid certificate.

###### Example API test case definition:

###### Note

`EXECUTION_TIMEOUT` has a default value of 5
minutes. We recommend a timeout value of 2 minutes.

```
"tests":[
   {
      "name":"`my_tls_unsecure_server_cert_test`",
      "configuration": {
         // optional:
         "EXECUTION_TIMEOUT":"`300`",  //in seconds
      },
      "test":{
         "id":"TLS_Unsecure_Server_Cert",
         "version":"0.0.0"
      }
   }
]
```

###### Example Test case outputs:

- Pass — The device under test closed the
  connection.
- Fail — The device under test completed TLS handshake
  with AWS IoT.

**TLS Incorrect Subject Name Server Cert / Incorrect Subject Common Name
(CN) / Subject Alternative Name (SAN)**

Validates that the device under test closes the connection if it's
presented with a server certificate for a domain name that is different
than the one requested.

###### Example API test case definition:

###### Note

`EXECUTION_TIMEOUT` has a default value of 5
minutes. We recommend a timeout value of 2 minutes.

```
"tests":[
   {
      "name":"`my_tls_incorrect_subject_name_cert_test`",
      "configuration": {
         // optional:
         "EXECUTION_TIMEOUT":"`300`",   // in seconds
      },
      "test":{
         "id":"TLS_Incorrect_Subject_Name_Server_Cert",
         "version":"0.0.0"
      }
   }
]
```

###### Example Test case outputs:

- Pass — The device under test closed the
  connection.
- Fail — The device under test completed the TLS handshake
  with AWS IoT.

## TLS Expired Server Certificate

**Expired server certificate**

Validates that the device under test closes the connection if it's
presented with an expired server certificate.

###### Example API test case definition:

###### Note

`EXECUTION_TIMEOUT` has a default value of 5
minutes. We recommend a timeout value of 2 minutes.

```
"tests":[
   {
      "name":"`my_tls_expired_cert_test`",
      "configuration": {
         // optional:
         "EXECUTION_TIMEOUT":"`300`",  //in seconds
      },
      "test":{
         "id":"TLS_Expired_Server_Cert",
         "version":"0.0.0"
      }
   }
]
```

###### Example Test case outputs:

- **Pass** — The device under test refuses to complete the
  TLS handshake with AWS IoT. The device sends a TLS alert
  message before it closes the connection.
- **Pass with warnings** — The device under test refuses to
  complete the TLS handshake with AWS IoT. However, it
  doesn’t send a TLS alert message before it closes the
  connection.
- **Fail** — The device under test completes
  the TLS handshake with AWS IoT.
