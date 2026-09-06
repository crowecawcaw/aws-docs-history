

# AWS IoT policy potentially misconfigured
<a name="audit-chk-iot-misconfigured-policies"></a>

An AWS IoT policy was identified as potentially misconfigured. Misconfigured policies, including overly permissive policies, can cause security incidents like allowing devices access to unintended resources.

The **AWS IoT policy potentially misconfigured** check is a warning for you to make sure that only intended actions are allowed before updating the policy.

In the CLI and API, this check appears as `IOT_POLICY_POTENTIAL_MISCONFIGURATION_CHECK`.

Severity: **Medium**

## Details
<a name="audit-chk-iot-misconfigured-policies-details"></a>

AWS IoT returns the following reason code when this check finds a potentially misconfigured AWS IoT policy:
+ POLICY\_CONTAINS\_MQTT\_WILDCARDS\_IN\_DENY\_STATEMENT
+ TOPIC\_FILTERS\_INTENDED\_TO\_DENY\_ALLOWED\_USING\_WILDCARDS

## Why it matters
<a name="audit-chk-iot-misconfigured-policies-why-it-matters"></a>

Misconfigured policies can lead to unintended consequences by providing more permissions to devices than required. We recommend careful consideration of the policy to limit access to resources and prevent security threats.

### Policy contains MQTT wildcards in deny statement example
<a name="example-section-id"></a>

The **AWS IoT policy potentially misconfigured** check inspects for MQTT wildcard characters (`+` or `#`) in deny statements. Wildcards are treated as literal strings by AWS IoT policies and can make the policy overly permissive.

The following example is intended to deny subscribing to topics related to `building/control_room` by using the MQTT wildcard `#` in policies. However, MQTT wildcards don't have a wildcard meaning in AWS IoT policies and devices can subscribe to `building/control_room/data1`.

The **AWS IoT policy potentially misconfigured** check will flag this policy with reason code `POLICY_CONTAINS_MQTT_WILDCARDS_IN_DENY_STATEMENT`.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iot:Subscribe",
            "Resource": "arn:aws:iot:us-east-1:123456789012:topicfilter/building/*"
        },
        {
            "Effect": "Deny",
            "Action": "iot:Subscribe",
            "Resource": "arn:aws:iot:us-east-1:123456789012:topicfilter/building/control_room/#"
        },
        {
            "Effect": "Allow",
            "Action": "iot:Receive",
            "Resource": "arn:aws:iot:us-east-1:123456789012:topic/building/*"
        }
    ]
}
```

------

The following is an example of a properly configured policy. Devices don't have permission to subscribe to subtopics of `building/control_room/` and don't have permissions to receive messages from subtopics of `building/control_room/`.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "iot:Subscribe",
      "Resource": "arn:aws:iot:us-east-1:123456789012:topicfilter/building/*"
    },
    {
      "Effect": "Deny",
      "Action": "iot:Subscribe",
      "Resource": "arn:aws:iot:us-east-1:123456789012:topicfilter/building/control_room/*"
    },
    {
      "Effect": "Allow",
      "Action": "iot:Receive",
      "Resource": "arn:aws:iot:us-east-1:123456789012:topic/building/*"
    },
    {
      "Effect": "Deny",
      "Action": "iot:Receive",
      "Resource": "arn:aws:iot:us-east-1:123456789012:topic/building/control_room/*"
    }
  ]
}
```

------

### Topic filters intended to deny allowed using wildcards example
<a name="example-section-id2"></a>

The following example policy is intended to deny subscribing to topics related to `building/control_room` by denying the resource `building/control_room/*`. However, devices can send requests to subscribe to `building/#` and receive messages from all topics related to `building`, including `building/control_room/data1`.

The **AWS IoT policy potentially misconfigured** check will flag this policy with reason code `TOPIC_FILTERS_INTENDED_TO_DENY_ALLOWED_USING_WILDCARDS`.

The following example policy has permissions to receive message on `building/control_room topics`:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iot:Subscribe",
            "Resource": "arn:aws:iot:us-east-1:123456789012:topicfilter/building/*"
        },
        {
            "Effect": "Deny",
            "Action": "iot:Subscribe",
            "Resource": "arn:aws:iot:us-east-1:123456789012:topicfilter/building/control_room/*"
        },
        {
            "Effect": "Allow",
            "Action": "iot:Receive",
            "Resource": "arn:aws:iot:us-east-1:123456789012:topic/building/*"
        }
    ]
}
```

------

The following is an example of a properly configured policy. Devices don't have permission to subscribe to subtopics of `building/control_room/` and don't have permissions to receive messages from subtopics of `building/control_room/`.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iot:Subscribe",
            "Resource": "arn:aws:iot:us-east-1:123456789012:topicfilter/building/*"
        },
        {
            "Effect": "Deny",
            "Action": "iot:Subscribe",
            "Resource": "arn:aws:iot:us-east-1:123456789012:topicfilter/building/control_room/*"
        },
        {
            "Effect": "Allow",
            "Action": "iot:Receive",
            "Resource": "arn:aws:iot:us-east-1:123456789012:topic/building/*"
        },
        {
            "Effect": "Deny",
            "Action": "iot:Receive",
            "Resource": "arn:aws:iot:us-east-1:123456789012:topic/building/control_room/*"
        }
    ]
}
```

------

**Note**  
This check might report false positives. We recommend that you evaluate any flagged policies and mark false positives resources using audit suppressions.

## How to fix it
<a name="audit-chk-iot-misconfigured-policies-how-to-fix"></a>

This check flags potentially misconfigured policies so there might be false positives. Mark any false positives using [audit suppressions](audit-finding-suppressions.md) so they aren't flagged in the future.

You can also follow these steps to fix any noncompliant policies attached to things, thing groups, or other entities:

1. Use [CreatePolicyVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_CreatePolicyVersion.html) to create a new, compliant version of the policy. Set the `setAsDefault` flag to true. (This makes this new version operative for all entities that use the policy.)

   For examples of creating AWS IoT policies for common use cases, see [Publish/Subscribe policy examples](https://docs.aws.amazon.com/iot/latest/developerguide/pub-sub-policy.html) in the *AWS IoT Core Developer Guide*.

1. Verify that all associated devices are able to connect to AWS IoT. If a device is unable to connect, use [ SetPolicyVersion](https://docs.aws.amazon.com/iot/latest/apireference/API_SetPolicyVersion.html) to roll back the default policy to the previous version, revise the policy, and try again. 

You can use mitigation actions to:
+ Apply the `REPLACE_DEFAULT_POLICY_VERSION` mitigation action on your audit findings to make this change. 
+ Apply the `PUBLISH_FINDINGS_TO_SNS` mitigation action if you want to implement a custom response in response to the Amazon SNS message. 

For more information, see [Mitigation actions](dd-mitigation-actions.md). 

Use [IoT Core policy variables](https://docs.aws.amazon.com/iot/latest/developerguide/iot-policy-variables.html) in the *AWS IoT Core Developer Guide* to dynamically reference AWS IoT resources in your policies.