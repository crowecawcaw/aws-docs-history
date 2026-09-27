

# Actions, resources, and condition keys for the Custom Event Bus
<a name="eb-custom-bus-access-actions"></a>

Use this page when you write an IAM policy. It lists every `events:` action for the Custom Event Bus, the resource ARN each one is checked against, whether another account can be granted it, and the condition keys you can add. For example, to let a role attach subscribers whose `METADATA` filter names `tenant` as `acme`, grant `events:CreateSubscriber` on the bus with a `ForAnyValue:StringEquals` condition on `events:Metadata/tenant`.

## Condition keys
<a name="eb-custom-bus-access-conditions"></a>

EventBridge supplies the following condition keys from the request, so that you can narrow a grant beyond the action and the resource. For the global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.


| Condition key | Value | Supplied on | 
| --- | --- | --- | 
| events:source | The event's source, or the source being forwarded | PutEvents, CreateEventSource, UpdateEventSource | 
| events:detail-type | The event's detail type | PutEvents | 
| events:Metadata/{{key}} | The values a METADATA filter matches on that key | CreateSubscriber | 
| events:Metadata/{{key}}/Matcher | exact | CreateSubscriber | 
| events:ContentFilterPresent | true when the subscriber declares a DATA filter | CreateSubscriber | 
| aws:ResourceTag/{{key}} | A tag on the bus, subscriber, or event source being checked | Every action checked against a resource | 
| aws:RequestTag/{{key}}, aws:TagKeys | The tags in the request | The create operations and TagResource, UntagResource | 

A metadata key is supplied as a set of values, so match it with a set operator such as `ForAnyValue:StringEquals`. `METADATA` filters are exact-match only, which is why the matcher value is always `exact`. A `DATA` filter matches arbitrary JSON, so only its presence is exposed, not its content. `UpdateEventSource` re-runs the bus check with `events:source` set from the replacement configuration, so a condition on that key governs a repointed event source as well as a new one.

The following resource policy lets account `444455556666` create subscribers on the `orders` bus only when the subscriber's `METADATA` filter matches `tenant` exactly to `acme`. A subscriber with no `METADATA` filter, or one that names another tenant, is denied. EventBridge supplies a metadata condition key only for the fields a filter declares, so the `Null` condition is what denies a filter that omits `tenant`.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "SubscribeToAcmeEventsOnly",
            "Effect": "Allow",
            "Principal": { "AWS": "arn:aws:iam::444455556666:root" },
            "Action": "events:CreateSubscriber",
            "Resource": "arn:aws:events:us-east-1:111122223333:event-busv2/orders/EXAMPLE1234567890abcdef",
            "Condition": {
                "Null": { "events:Metadata/tenant": "false" },
                "ForAnyValue:StringEquals": { "events:Metadata/tenant": "acme" },
                "StringEquals": { "events:Metadata/tenant/Matcher": "exact" }
            }
        }
    ]
}
```

## Actions and the resources they are checked against
<a name="eb-custom-bus-access-actions-table"></a>

The following table lists every action, the resource ARN to put in the policy's `Resource` element, and whether a bus owner can grant the action to another account through a resource policy or an AWS RAM share. The three `List` actions are not checked against any resource, so grant them with `"Resource": "*"`.


| IAM action | Checked against | Grantable to another account | 
| --- | --- | --- | 
| events:CreateEventBus | The bus being created | No. Created in the caller's own account | 
| events:DescribeEventBus | The bus | Yes | 
| events:UpdateEventBus | The bus | No. Bus owner only | 
| events:DeleteEventBus | The bus | No. Bus owner only | 
| events:ListEventBuses | Nothing. Account-wide | No. Lists the caller's own and shared buses | 
| events:PutEvents | The bus, once per entry in the request | Yes | 
| events:PutRawEvents | The bus, once per entry in the request | Yes | 
| events:CreateSubscriber | The bus, and the subscriber being created | Yes | 
| events:DescribeSubscriber | The subscriber | The subscriber's owner authorizes it | 
| events:UpdateSubscriber | The subscriber | The subscriber's owner authorizes it | 
| events:DeleteSubscriber | The subscriber | The subscriber's owner authorizes it | 
| events:ListSubscribers | Nothing. Account-wide | No. Lists the caller's own subscribers | 
| events:RevokeResource | The bus | No. Bus owner only | 
| events:CreateEventSource | The bus, and the event source being created | Yes | 
| events:DescribeEventSource | The event source | The event source's owner authorizes it | 
| events:UpdateEventSource | The event source, and the bus again | Yes, for the bus check | 
| events:DeleteEventSource | The event source | The event source's owner authorizes it | 
| events:ListEventSources | Nothing. Account-wide | No. Lists the caller's own event sources | 
| events:PutResourcePolicy | The bus | No. Bus owner only | 
| events:GetResourcePolicy | The bus | Yes | 
| events:DeleteResourcePolicy | The bus | No. Bus owner only | 
| events:ListResourcePolicies | The bus | Yes | 
| events:TagResource | The bus, subscriber, or event source named in the request | Bus: yes. Subscriber or event source: its owner | 
| events:UntagResource | The bus, subscriber, or event source named in the request | Bus: yes. Subscriber or event source: its owner | 
| events:ListTagsForResource | The bus, subscriber, or event source named in the request | Bus: yes. Subscriber or event source: its owner | 

To create a subscriber or an event source on a bus, the caller needs the action on the bus as well as on the new resource. That is what lets a bus owner decide, in the bus's own policy, which accounts may attach anything to it. `CreateSubscriber` makes four separate authorization checks, and all four must allow: `events:CreateSubscriber` on the bus, `events:CreateSubscriber` on the subscriber, `iam:PassRole` on the role in `InvokeConfiguration.RoleArn`, and `events:TagResource` on the subscriber when the request carries tags. `CreateEventSource` runs the same checks without `iam:PassRole`, because an event source has no role.

**Note**  
A resource that does not exist yet has no complete ARN, so a create check uses an ARN ending in a wildcard, such as `arn:aws:events:us-east-1:111122223333:subscriber/{{name}}/*`. A policy scoped to one subscriber therefore matches by name prefix, not exactly. An untagged create supplies no `aws:ResourceTag` for the new resource, so a `StringEquals` condition on that key denies it.

## Example identity-based policies
<a name="eb-custom-bus-access-identity"></a>

A **producer** needs `events:PutEvents`, `events:PutRawEvents`, or both, on the bus ARN. Grant the action that matches the API it calls. A producer to a bus encrypted with a customer managed key also needs access to that key; see [Encrypting events on a Custom Event Bus](eb-custom-bus-encryption.md). A **subscriber owner** needs `events:CreateSubscriber` on the bus and on the subscriber, `iam:PassRole` on the delivery role, and the describe, update, and delete subscriber actions on the subscribers it manages. A **bus administrator** needs the create, update, and delete bus actions, the four resource policy actions, and `events:RevokeResource`.

The following policy lets a producer publish to one bus with either publish API, and read the bus so that it can confirm the bus is `ACTIVE` first. Publishing is authorized once for every entry in the request, and there is no partial authorization: if one entry fails a condition check, EventBridge denies the whole request, including the entries that would have passed.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublishToOrdersBus",
            "Effect": "Allow",
            "Action": [
                "events:PutEvents",
                "events:PutRawEvents",
                "events:DescribeEventBus"
            ],
            "Resource": "arn:aws:events:us-east-1:111122223333:event-busv2/orders/EXAMPLE1234567890abcdef"
        }
    ]
}
```

## Tagging
<a name="eb-custom-bus-access-tagging"></a>

You can tag a bus, a subscriber, or an event source. Set `Tags` on the create call, or use `TagResource`, `UntagResource`, and `ListTagsForResource` afterward. Each resource carries its own tag set, so tagging a bus does not tag the subscribers or event sources attached to it.

```
aws eventsv2 tag-resource \
    --resource-arn arn:aws:events:us-east-1:111122223333:event-busv2/orders/EXAMPLE1234567890abcdef \
    --tags team=payments,environment=production
```

A create response does not echo the tags you supplied, so read them back with `list-tags-for-resource` when you need to confirm them. Keys that begin with `aws:` are reserved for AWS and are rejected on every write, including `UntagResource`. To control who can tag, and to write policies that depend on tags, use the three tag actions in the preceding table and the `aws:RequestTag`, `aws:ResourceTag`, and `aws:TagKeys` condition keys.