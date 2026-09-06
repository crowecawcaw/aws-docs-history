

# Direct messaging policy examples
<a name="direct-messaging-policy-examples"></a>

Using direct messaging requires specific policies. Direct messaging uses the SendDirectMessage HTTP API to deliver messages from a sender to a single receiver identified by its MQTT client ID. This section presents examples of policies that allow common uses of direct messaging.

**Topics**
+ [Policy to send a direct message to a specific client on specific topics](#dm-policy-send-specific)
+ [Policy to receive direct messages](#dm-policy-receive)
+ [Policy to send a direct message to any client on specific topics](#dm-policy-send-any-client)
+ [Policy to send a direct message to any client on any topic](#dm-policy-send-any-client-any-topic)

## Policy to send a direct message to a specific client on specific topics
<a name="dm-policy-send-specific"></a>

For a sender to send direct messages, the sender must have `iot:SendDirectMessage` permission with the target client ID as the resource. The `iot:Topic` condition key (optional) restricts which topics the sender can send messages on.
+ For SigV4-authenticated backend servers, add this to an IAM policy.
+ For X.509-authenticated IoT devices, add this to an AWS IoT Core policy.
+ For custom authorizer-authenticated clients, the Lambda function must return a policy document granting `iot:SendDirectMessage` on the target client resource with the `iot:Topic` condition key

The following policy allows client `device1` to send direct messages to client `myDevice` on the topics `commands/reboot` and `commands/update`.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iot:SendDirectMessage",
            "Resource": "arn:aws:iot:us-west-2:123456789012:client/myDevice",
            "Condition": {
                "StringEquals": {
                    "iot:Topic": ["commands/reboot", "commands/update"]
                }
            }
        }
    ]
}
```

## Policy to receive direct messages
<a name="dm-policy-receive"></a>

The receiver's policy must grant `iot:Receive` on the topic. The receiver does not need `iot:Subscribe` permission — AWS IoT Core delivers direct messages without requiring a topic subscription. The receiver can authenticate using X.509 client certificate (AWS IoT Core policy) or SigV4 (IAM policy). In both cases, the `iot:Receive` permission is required on the receiving topic.

The following policy allows the receiver client `myDevice` to receive direct messages on the topics `commands/reboot` and `commands/update`.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iot:Receive",
            "Resource": "arn:aws:iot:us-west-2:123456789012:topic/commands/reboot"
        },
        {
            "Effect": "Allow",
            "Action": "iot:Receive",
            "Resource": "arn:aws:iot:us-west-2:123456789012:topic/commands/update"
        }
    ]
}
```

The following policy uses a wildcard to allow the receiver to receive direct messages on any topic under the `commands/` prefix.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iot:Receive",
            "Resource": "arn:aws:iot:us-west-2:123456789012:topic/commands/*"
        }
    ]
}
```

**Note**  
The receiver must establish an MQTT connection to AWS IoT Core before receiving a direct message. Direct messages are not queued for offline devices.

## Policy to send a direct message to any client on specific topics
<a name="dm-policy-send-any-client"></a>

The following policy allows the sender to send direct messages to any client, but only on topics matching the `commands/*` prefix. This is useful for fleet management services that need to reach any device but only for specific command topics.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iot:SendDirectMessage",
            "Resource": "arn:aws:iot:us-west-2:123456789012:client/*",
            "Condition": {
                "StringLike": {
                    "iot:Topic": "commands/*"
                }
            }
        }
    ]
}
```

**Note**  
The `iot:Topic` condition key supports wildcard matching with the `StringLike` condition operator.

## Policy to send a direct message to any client on any topic
<a name="dm-policy-send-any-client-any-topic"></a>

The following policy allows the sender to send direct messages to any client on any topic. This is suitable for administrative or fleet management use cases where a backend service needs unrestricted access.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iot:SendDirectMessage",
            "Resource": "arn:aws:iot:us-west-2:123456789012:client/*",
            "Condition": {
                "StringLike": {
                    "iot:Topic": "*"
                }
            }
        }
    ]
}
```