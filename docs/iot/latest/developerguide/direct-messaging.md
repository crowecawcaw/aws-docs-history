

# Direct Messaging
<a name="direct-messaging"></a>

AWS IoT Core now supports Direct Messaging. You can send a message to a single connected device by its MQTT client ID, without requiring the device to subscribe to a topic.

Previously, sending a message to a specific device required publishing to a topic the device subscribed to, with no built-in way to confirm the delivery. The sender calls the SendDirectMessage HTTP API, specifying the receiver's client ID and a target topic. When `confirmation=true`, AWS IoT Core delivers at QoS 1 and waits for the receiver's PUBACK before returning a successful response. This gives you end-to-end delivery acknowledgment. API response and Amazon CloudWatch Logs provide full visibility into delivery status and failure reasons.

Direct messages are not processed by AWS IoT Rules for rule execution, are not queued for offline devices, and do not support retained messages.

**Topics**
+ [Prerequisites](#direct-messaging-prerequisites)
+ [SendDirectMessage API](#direct-messaging-api)
+ [Receiver client behavior](#direct-messaging-receiver)

## Prerequisites
<a name="direct-messaging-prerequisites"></a>

Both the sender and the receiver require specific policy actions to use direct messaging. The sender must have `iot:SendDirectMessage` permission. The target client ID is specified as the resource and the `iot:Topic` condition key (optional) restricts which topics a sender can send direct messages. The receiver must have `iot:Receive` permission on the target topic. The receiver does not need `iot:Subscribe` permission — AWS IoT Core delivers direct messages without requiring a topic subscription. For more details and example policies, see [Direct messaging policy examples](direct-messaging-policy-examples.md).

For the authentication and port mappings used by HTTP requests, see [Protocols, port mappings, and authentication](protocols.md#protocol-mapping).

## SendDirectMessage API
<a name="direct-messaging-api"></a>

Senders can send Direct Messages by making HTTP POST requests to a client-specific URL:

```
https://{{IoT_data_endpoint}}/connections/{{client_id}}/messages?topic={{topic_name}}&confirmation=true&timeout=10
```
+ {{IoT\_data\_endpoint}} is the [AWS IoT device data endpoint](iot-connect-devices.md#iot-connect-device-endpoints). See [AWS IoT device data and service endpoints](iot-connect-devices.md#iot-connect-device-endpoints) to find your endpoint.
+ {{client\_id}} is unique identifier of the MQTT client to send the message to. Client IDs must not exceed 128 characters and can't start with a dollar sign ($). MQTT client IDs must be URL encoded (percent-encoded) when they contain characters that are not valid in HTTP requests, such as spaces, forward slashes (/), and UTF-8 characters. For more information, see [AWS IoT Core message broker and protocol limits and quotas](https://docs.aws.amazon.com/general/latest/gr/iot-core.html#message-broker-limits).
+ {{topic\_name}} is the topic on which the receiver receives the message, URL-encoded. Must not start with $. Must not be an AWS IoT Core Reserved Topic. Refer to the AWS IoT Core service quotas page for topic length and depth limits. For more information, see [AWS IoT Core message broker and protocol limits and quotas](https://docs.aws.amazon.com/general/latest/gr/iot-core.html#message-broker-limits).
+ {{confirmation}} is a Boolean. When set to `true`, the API delivers the message at QoS 1 and waits for the MQTT client to send a delivery confirmation (PUBACK) before returning a successful response. If delivery confirmation is not received within the specified timeout period, the API returns HTTP 504.
+ {{timeout}} is an integer that represents the maximum time, in seconds, to wait for a delivery confirmation (PUBACK) from the receiving client after the message has been delivered. This parameter is only used when `confirmation` is set to `true`. If `confirmation` is `false`, this parameter is ignored. The total API response time may be higher than this value due to internal processing. Set your HTTP client timeout to a value greater than this parameter.

### API response status codes
<a name="direct-messaging-response-codes"></a>

The following table lists the HTTP status codes returned by the SendDirectMessage API and the recommended actions for each. Enable AWS IoT Core CloudWatch logs to see detailed SendDirectMessage event logs including the reason field for programmatic error handling.


**SendDirectMessage API response status codes**  

| HTTP code | Recommended action | 
| --- | --- | 
| 200 OK | If delivery confirmation was requested with confirmation=true, this indicates the receiver has acknowledged the message receipt. Otherwise, this indicates the message was dispatched successfully. | 
| 400 Bad Request | This means one of the parameters are invalid. Review the HTTP response message or CloudWatch logs to identify specific failure and fix. Ensure topic name and Client-id are valid and URL-encoded correctly. | 
| 403 Forbidden | This means the sender's policy does not grant iot:SendDirectMessage on the target client and topic, or the receiver's policy does not grant iot:Receive on the topic. Review the HTTP response message or CloudWatch logs to identify specific failure, and update the corresponding policy. See [Direct messaging policy examples](direct-messaging-policy-examples.md). | 
| 404 Not Found | This means the target client ID is not connected to AWS IoT Core. Review the HTTP response message or CloudWatch logs for the specific reason, verify the receiver is connected, and try again. If the response message states "The target client ID is not connected, but it has an active persistent session," the target client has an unexpired persistent session but is currently offline. | 
| 413 Payload Too Large | Payload exceeds maximum size allowed. Reduce the payload size and retry. See [AWS IoT Core service quotas](https://docs.aws.amazon.com/general/latest/gr/iot-core.html). | 
| 429 Too Many Requests | This means the account has exceeded the SendDirectMessage requests-per-second limit or the receiver connection has exceeded the outbound publish limit. Review the HTTP response message or CloudWatch logs for the specific reason, reduce the request rate and implement exponential backoff. See [AWS IoT Core service quotas](https://docs.aws.amazon.com/general/latest/gr/iot-core.html). | 
| 500 Internal Server Error | This indicates an unexpected server-side error. Retry the request with exponential backoff. If the issue persists, contact AWS Support with the traceId from the response. | 
| 504 Gateway Timeout | This means the receiver did not send PUBACK within the specified timeout period. Increase the timeout value, verify the receiver's MQTT client sends PUBACK for QoS 1 messages, or check if the receiver is processing messages slowly. | 

### Examples
<a name="direct-messaging-examples"></a>

------
#### [ AWS CLI ]

```
aws iot-data send-direct-message \
    --client-id myDevice \
    --topic commands/reboot \
    --confirmation \
    --timeout 10 \
    --payload '{"action": "reboot"}' \
    --cli-binary-format raw-in-base64-out \
    --region us-west-2 \
    --endpoint-url https://{{IoT_data_endpoint}}
```

The `--cli-binary-format` option is required if you're using AWS Command Line Interface version 2. To make this the default setting, run `aws configure set cli-binary-format raw-in-base64-out`. For more information, see [AWS CLI supported global command line options](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-options.html#cli-configure-options-list) in the *AWS Command Line Interface User Guide for Version 2*.

------
#### [ curl (X.509 client certificate, port 8443) ]

```
curl --tlsv1.2 \
    --cacert Amazon-root-CA-1.pem \
    --cert device.pem.crt \
    --key private.pem.key \
    --request POST \
    --data '{"action": "reboot"}' \
    "https://{{IoT_data_endpoint}}:8443/connections/myDevice/messages?topic=commands%2Freboot&confirmation=true&timeout=10"
```

------

## Receiver client behavior
<a name="direct-messaging-receiver"></a>

Direct Messaging delivers messages to MQTT clients (receivers) without requiring a topic subscription. To fully benefit from Direct Messaging, the receiver must support the following behaviors:
+ **Receive messages on topics not explicitly subscribed to** — The receiver's Direct messaging can deliver messages to topics the receiver has not explicitly subscribed to. However, some MQTT client implementations filter or discard messages on unsubscribed topics. If your client discards these messages, direct messaging will only work on topics the receiver has also subscribed to. To receive direct messages on any topic, verify that your client's message handler processes messages regardless of subscription state.
+ **Handle QoS determined by the API** — The QoS level of the delivered message is set by the `confirmation` parameter in the sender's API request, not by the receiver's subscription. When `confirmation=true`, the message arrives at QoS 1 and the receiver's client must send a PUBACK to acknowledge delivery. When `confirmation=false`, the message arrives at QoS 0 with no acknowledgment required. Ensure your client's MQTT implementation handles both QoS 0 and QoS 1 incoming messages correctly.