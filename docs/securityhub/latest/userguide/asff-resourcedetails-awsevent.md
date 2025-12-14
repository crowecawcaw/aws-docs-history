# AwsEventBridge resources in ASFF

The following are examples of the AWS Security Finding Format (ASFF) syntax for `AwsEventBridge` resources.

AWS Security Hub CSPM normalizes findings from various sources into ASFF. For background information about ASFF, see
[AWS Security Finding Format (ASFF)](securityhub-findings-format.md "securityhub-findings-format.md").

## AwsEventSchemasRegistry

The `AwsEventSchemasRegistry` object provides information about an Amazon EventBridge
schema registry. A schema defines the structure of events that are sent to EventBridge. Schema
registries are containers that collect and logically group your schemas.

The following example shows the AWS Security Finding Format (ASFF) for the
`AwsEventSchemasRegistry` object. To view descriptions of
`AwsEventSchemasRegistry` attributes, see [AwsEventSchemasRegistry](../../1.0/APIReference/API_AwsEventSchemasRegistryDetails.md "../../1.0/APIReference/API_AwsEventSchemasRegistryDetails.md") in the _AWS Security Hub CSPM API Reference_.

**Example**

```
"AwsEventSchemasRegistry": {
    "Description": "This is an example event schema registry.",
    "RegistryArn": "arn:aws:schemas:us-east-1:123456789012:registry/schema-registry",
    "RegistryName": "schema-registry"
}
```

## AwsEventsEndpoint

The `AwsEventsEndpoint` object provides information about an Amazon EventBridge
global endpoint. The endpoint can improve your application’s availability by making it Regional-fault tolerant.

The following example shows the AWS Security Finding Format (ASFF) for the
`AwsEventsEndpoint` object. To view descriptions of
`AwsEventsEndpoint` attributes, see [AwsEventsEndpointDetails](../../1.0/APIReference/API_AwsEventsEndpointDetails.md "../../1.0/APIReference/API_AwsEventsEndpointDetails.md") in the _AWS Security Hub CSPM API Reference_.

**Example**

```
"AwsEventsEndpoint": {
    "Arn": "arn:aws:events:us-east-1:123456789012:endpoint/my-endpoint",
    "Description": "This is a sample endpoint.",
    "EndpointId": "04k1exajoy.veo",
    "EndpointUrl": "https://04k1exajoy.veo.endpoint.events.amazonaws.com",
    "EventBuses": [
        {
            "EventBusArn": "arn:aws:events:us-east-1:123456789012:event-bus/default"
        },
        {
            "EventBusArn": "arn:aws:events:us-east-2:123456789012:event-bus/default"
        }
    ],
    "Name": "my-endpoint",
    "ReplicationConfig": {
        "State": "ENABLED"
    },
    "RoleArn": "arn:aws:iam::123456789012:role/service-role/Amazon_EventBridge_Invoke_Event_Bus_1258925394",
    "RoutingConfig": {
        "FailoverConfig": {
            "Primary": {
                "HealthCheck": "arn:aws:route53:::healthcheck/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
            },
            "Secondary": {
                "Route": "us-east-2"
            }
        }
    },
    "State": "ACTIVE"
}
```

## AwsEventsEventbus

The `AwsEventsEventbus` object provides information about an Amazon EventBridge
global endpoint. The endpoint can improve your application’s availability by making it Regional-fault tolerant.

The following example shows the AWS Security Finding Format (ASFF) for the
`AwsEventsEventbus` object. To view descriptions of
`AwsEventsEventbus` attributes, see [AwsEventsEventbusDetails](../../1.0/APIReference/API_AwsEventsEventbusDetails.md "../../1.0/APIReference/API_AwsEventsEventbusDetails.md") in the _AWS Security Hub CSPM API Reference_.

**Example**

```
"AwsEventsEventbus":
    "Arn": "arn:aws:events:us-east-1:123456789012:event-bus/my-event-bus",
    "Name": "my-event-bus",
    "Policy": "{\"Version\":\"2012-10-17\",		 	 	 \"Statement\":[{\"Sid\":\"AllowAllAccountsFromOrganizationToPutEvents\",\"Effect\":\"Allow\",\"Principal\":\"*\",\"Action\":\"events:PutEvents\",\"Resource\":\"arn:aws:events:us-east-1:123456789012:event-bus/my-event-bus\",\"Condition\":{\"StringEquals\":{\"aws:PrincipalOrgID\":\"o-ki7yjtkjv5\"}}},{\"Sid\":\"AllowAccountToManageRulesTheyCreated\",\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::123456789012:root\"},\"Action\":[\"events:PutRule\",\"events:PutTargets\",\"events:DeleteRule\",\"events:RemoveTargets\",\"events:DisableRule\",\"events:EnableRule\",\"events:TagResource\",\"events:UntagResource\",\"events:DescribeRule\",\"events:ListTargetsByRule\",\"events:ListTagsForResource\"],\"Resource\":\"arn:aws:events:us-east-1:123456789012:rule/my-event-bus\",\"Condition\":{\"StringEqualsIfExists\":{\"events:creatorAccount\":\"123456789012\"}}}]}"

```
