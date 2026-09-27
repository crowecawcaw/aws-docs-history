

# Names, endpoints, and IAM permissions for the Custom Event Bus
<a name="eb-custom-bus-names"></a>

The Custom Event Bus has its own AWS CLI command, SDK client, and endpoint, and it shares its IAM namespace and service principal with Custom Event Bus - Classic. The following table shows which name to use where.

## Names to use for each interface
<a name="eb-custom-bus-names-table"></a>


| Interface | Name | Example | 
| --- | --- | --- | 
| AWS CLI command | eventsv2 | aws eventsv2 put-events | 
| SDK client | EventBridgeV2 | EventBridgeV2Client in the AWS SDK for Java | 
| Endpoint | eventsv2 | eventsv2.us-east-1.amazonaws.com | 
| VPC endpoint service | eventsv2 | com.amazonaws.us-east-1.eventsv2, or com.amazonaws.us-east-1.eventsv2-fips | 
| Dual-stack endpoint | eventsv2 | eventsv2.us-east-1.api.aws | 
| IAM actions | events:, shared with Custom Event Bus - Classic | events:PutRawEvents, events:CreateSubscriber | 
| Service principal | events.amazonaws.com, shared with Custom Event Bus - Classic | The principal in a delivery role's trust policy | 
| Resource ARNs | event-busv2 | arn:aws:events:us-east-1:111122223333:event-busv2/orders/EXAMPLE1234567890abcdef | 
| CloudFormation resource types | AWS::EventsV2 | Resource types in the AWS::EventsV2 namespace | 

## Why the IAM namespace is shared with Custom Event Bus - Classic
<a name="eb-custom-bus-names-shared"></a>

EventBridge keeps the `events:` namespace and the `events.amazonaws.com` principal for the Custom Event Bus so that you can move from Custom Event Bus - Classic without rewriting three things:
+ Identity-based policies that grant `events:` actions.
+ Bus resource policies.
+ The roles that deliver to your targets. A role that Custom Event Bus - Classic can assume today can deliver from a Custom Event Bus subscriber with no change to its trust policy.

**Important**  
Write every IAM action with the `events:` prefix, for example `events:PutRawEvents` and `events:CreateSubscriber`. The `eventsv2` name is for the CLI command, the SDK client, and the endpoint only. IAM accepts a policy that names `eventsv2:PutEvents`, but no such action exists, so the policy grants nothing and the caller receives `AccessDeniedException`. When a call to `aws eventsv2` is denied, check the action prefix in the policy first.

The following identity-based policy allows a producer to publish to one bus with either publish API. For the full action list, condition keys, and cross-account grants, see [Access control for the Custom Event Bus](eb-custom-bus-access.md); the authoritative list of actions, resources, and condition keys is in the [Service Authorization Reference](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazoneventbridge.html).

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "events:PutEvents",
                "events:PutRawEvents"
            ],
            "Resource": "arn:aws:events:us-east-1:111122223333:event-busv2/orders/EXAMPLE1234567890abcdef"
        }
    ]
}
```

Publishing is authorized against the bus ARN for every entry in the request. If one entry fails an authorization condition, EventBridge denies the whole request.