

# Actions, resources, and condition keys for the Custom Event Bus
<a name="eb-custom-bus-access-actions"></a>

Use this page when you write an IAM policy. It lists every `events:` action for the Custom Event Bus, the resource ARN each one is checked against, whether another account can be granted it, and the condition keys you can add. For example, you can limit a role to subscribers whose `METADATA` filter matches `tenant` to `acme` alone. To do so, grant `events:CreateSubscriber` and `events:UpdateSubscriber` on the bus with `Null` and `ForAllValues:StringEquals` conditions on `events:Metadata/tenant`.

## Condition keys
<a name="eb-custom-bus-access-conditions"></a>

EventBridge supplies the following condition keys from the request, so that you can narrow a grant beyond the action and the resource. For the global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.


| Condition key | Value | Supplied on | 
| --- | --- | --- | 
| events:source | The event's source, or the source being forwarded | PutEvents, CreateEventSource, UpdateEventSource | 
| events:detail-type | The event's detail type | PutEvents | 
| events:eventBusInvocation | true for a forwarded event, false for a direct publish | PutEvents, PutRawEvents | 
| events:SystemMetadata/ContentType | The content type in the event's system metadata | PutRawEvents, and PutEvents for a forwarded event | 
| events:SystemMetadata/AwsSource | The source of a forwarded event | PutEvents, PutRawEvents, for a forwarded event only | 
| events:SystemMetadata/AwsDetailType | The detail type of a forwarded event | PutEvents, PutRawEvents, for a forwarded event only | 
| events:Metadata/{{key}} | On PutRawEvents, the value of that metadata key on the event. On the subscriber actions, the values a METADATA filter matches on that key | PutRawEvents, CreateSubscriber, UpdateSubscriber | 
| events:Metadata/{{key}}/Matcher | exact | CreateSubscriber, UpdateSubscriber | 
| events:ContentFilterPresent | true when the filter configuration declares a DATA filter, otherwise false | CreateSubscriber, UpdateSubscriber | 
| events:PolicyName | The resource policy that the request acts on, default or AWS\_RAM | PutResourcePolicy, GetResourcePolicy, DeleteResourcePolicy | 
| aws:ResourceTag/{{key}} | A tag on the bus, subscriber, or event source being checked | Every action checked against a resource | 
| aws:RequestTag/{{key}} | The value of that tag in the request | The create operations and TagResource | 
| aws:TagKeys | The tag keys in the request | The create operations, TagResource, and UntagResource | 

A *forwarded event* is one that a rule or subscriber delivers to the bus, under a role that you supplied. EventBridge checks it with `events:eventBusInvocation` set to `true`; see [Events that arrive without a publish call](eb-custom-bus-sharing.md#eb-custom-bus-access-forwarded). A forwarded AWS service or partner event is checked as `PutEvents`, unless a subscriber transformed it. A subscriber transforms an event when its `Transformer.Type` is `WITH_METADATA` or `JSONATA`. A forwarded event checked as `PutEvents` carries `events:source` and `events:detail-type` with the event's source and detail type. Any other forwarded event is checked as `PutRawEvents`. Either way, `events:SystemMetadata/AwsSource` and `events:SystemMetadata/AwsDetailType` hold the event's source and detail type. Both keys are absent when the event has no source or detail type, or when a subscriber transformed it. So a `Deny` statement that tests the value of one of these keys does not apply to an event that lacks the key.

On `PutRawEvents`, `events:Metadata/{{key}}` holds a single value: the event's value for that metadata key. On `CreateSubscriber` and `UpdateSubscriber`, it holds every value that the `METADATA` filter matches on that key. A filter can match several values, so match the key with a set operator. `ForAllValues:StringEquals` matches only when every value is one that you list. `ForAnyValue:StringEquals` matches when any one value is one that you list, so it also allows a filter that adds other values. `ForAllValues` also matches when the filter does not name the key, so add a `Null` condition to require the key. `METADATA` filters are exact-match only, which is why the matcher value is always `exact`. A `DATA` filter matches arbitrary JSON, so only its presence is exposed, not its content. A `SYSTEM_METADATA` filter supplies no condition key.

`UpdateSubscriber` supplies the three filter keys only when the request includes a `FilterConfiguration`, even one that leaves the filter unchanged. That request is also checked as `events:UpdateSubscriber` against the bus. A condition in a statement that grants only `events:CreateSubscriber` does not apply to that check. So put the same conditions on `events:UpdateSubscriber`. A `FilterConfiguration` of `{}` removes every filter. It supplies `events:ContentFilterPresent` as `false` and no metadata keys, so a `Null` condition on a metadata key denies it.

When an `UpdateEventSource` request includes a `Configuration`, EventBridge also checks `events:UpdateEventSource` against the bus. It sets `events:source` from that configuration. So put the conditions that you set on `events:CreateEventSource` on `events:UpdateEventSource` as well. A condition on `events:source` then governs a repointed event source as well as a new one.

Use `events:PolicyName` to limit a principal to one of the bus's two resource policies; see [Write a custom resource policy](eb-custom-bus-sharing.md#eb-custom-bus-access-policy). The key holds the name of the policy that the request acts on. When you omit `PolicyName` in your own request, the request acts on `default`, and the key is `default`. AWS Resource Access Manager (AWS RAM) writes the `AWS_RAM` policy with the credentials of the principal that changes a resource share. EventBridge checks that write as `events:PutResourcePolicy`, with the key set to `AWS_RAM`. So a principal that you limit to `default` cannot share the bus through AWS RAM. `ListResourcePolicies` reports on both policies, so it does not supply this key. So a `StringEquals` condition on this key never matches `ListResourcePolicies`. Allow that action in a statement without that condition.

The following resource policy lets account `444455556666` create subscribers on the `orders` bus and change their filters. It allows both only when the subscriber's `METADATA` filter matches `tenant` exactly to `acme`. A subscriber with no `METADATA` filter, or with a filter that names any tenant other than `acme`, is denied. EventBridge supplies a metadata condition key only for the fields a filter declares. So the `Null` condition is what denies a filter that omits `tenant`. The conditions restrict only this statement's grant. If another statement, or an AWS RAM share, also allows `events:CreateSubscriber` for that account, the conditions do not restrict that grant.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "SubscribeToAcmeEventsOnly",
            "Effect": "Allow",
            "Principal": { "AWS": "arn:aws:iam::444455556666:root" },
            "Action": [
                "events:CreateSubscriber",
                "events:UpdateSubscriber"
            ],
            "Resource": "arn:aws:events:us-east-1:111122223333:event-busv2/orders/EXAMPLE1234567890abcdef",
            "Condition": {
                "Null": { "events:Metadata/tenant": "false" },
                "ForAllValues:StringEquals": { "events:Metadata/tenant": "acme" },
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
| events:UpdateSubscriber | The subscriber, and the bus when the request includes a FilterConfiguration | Yes, for the bus check | 
| events:DeleteSubscriber | The subscriber | The subscriber's owner authorizes it | 
| events:ListSubscribers | Nothing. Account-wide | No. Lists the caller's own subscribers | 
| events:RevokeResource | The bus | No. Bus owner only | 
| events:CreateEventSource | The bus, and the event source being created | Yes | 
| events:DescribeEventSource | The event source | The event source's owner authorizes it | 
| events:UpdateEventSource | The event source, and the bus when the request includes a Configuration | Yes, for the bus check | 
| events:DeleteEventSource | The event source | The event source's owner authorizes it | 
| events:ListEventSources | Nothing. Account-wide | No. Lists the caller's own event sources | 
| events:PutResourcePolicy | The bus | No. Bus owner only | 
| events:GetResourcePolicy | The bus | No. Bus owner only | 
| events:DeleteResourcePolicy | The bus | No. Bus owner only | 
| events:ListResourcePolicies | The bus | No. Bus owner only | 
| events:TagResource | The bus, subscriber, or event source named in the request | No. The resource's owner only | 
| events:UntagResource | The bus, subscriber, or event source named in the request | No. The resource's owner only | 
| events:ListTagsForResource | The bus, subscriber, or event source named in the request | No. The resource's owner only | 

To create a subscriber or an event source on a bus, the caller needs the action on the bus as well as on the new resource. That is what lets a bus owner decide, in the bus's own policy, which accounts may attach anything to it. `CreateSubscriber` makes four separate authorization checks, and all four must allow: `events:CreateSubscriber` on the bus, `events:CreateSubscriber` on the subscriber, `iam:PassRole` on the role in `InvokeConfiguration.RoleArn`, and `events:TagResource` on the subscriber when the request carries tags. `CreateEventSource` runs the same checks without `iam:PassRole`, because an event source has no role. `UpdateSubscriber` also checks `events:UpdateSubscriber` on the bus when the request includes a `FilterConfiguration`. It also checks `iam:PassRole` on the role in `InvokeConfiguration.RoleArn` when the request includes one. So another account needs `events:CreateSubscriber` and `events:UpdateSubscriber` on your bus to attach subscribers and to update their filters. The AWS RAM managed permissions for attaching subscribers include both.

**Note**  
A resource that does not exist yet has no complete ARN, so a create check uses an ARN ending in a wildcard, such as `arn:aws:events:us-east-1:111122223333:subscriber/{{name}}/*`. A policy scoped to one subscriber therefore matches by name prefix, not exactly. An untagged create supplies no `aws:ResourceTag` for the new resource, so a `StringEquals` condition on that key denies it.

## Example identity-based policies
<a name="eb-custom-bus-access-identity"></a>

A **producer** needs `events:PutEvents`, `events:PutRawEvents`, or both, on the bus ARN. Grant the action that matches the API it calls. A producer to a bus encrypted with a customer managed key also needs access to that key; see [Encryption at Rest for Amazon EventBridge Custom Event Bus](eb-custom-bus-encryption.md). A **subscriber owner** needs `events:CreateSubscriber` on the bus and on the subscriber, `iam:PassRole` on the delivery role, and the describe, update, and delete subscriber actions on the subscribers it manages. For an `UpdateSubscriber` request that includes a `FilterConfiguration`, it also needs `events:UpdateSubscriber` on the bus. A **bus administrator** needs the create, update, and delete bus actions, the four resource policy actions, and `events:RevokeResource`.

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