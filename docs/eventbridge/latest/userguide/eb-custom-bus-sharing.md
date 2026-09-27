

# Sharing a Custom Event Bus with other accounts
<a name="eb-custom-bus-sharing"></a>

To let another account publish to your bus, attach subscribers to it, or attach event sources to it, share the bus with AWS Resource Access Manager (AWS RAM) and choose one of the four managed permissions. For example, share the `orders` bus with account `444455556666` using `AWSRAMEventBridgeEventBusV2SubscribeOnly`, and that account can create subscribers on it. Write a resource policy on the bus instead when you need an explicit `Deny`, a condition key, or a grant that no managed permission expresses. The other account still needs the same actions in its own identity policies, because both sides must allow.

## Prerequisites for sharing a bus
<a name="eb-custom-bus-access-ram-prereq"></a>
+ You must own the bus. A consumer account cannot share a bus onward.
+ To share with accounts in your organization without an invitation, enable sharing with AWS Organizations in AWS RAM. To share with an account outside your organization, the account must accept the resource share invitation before it can use the bus.
+ The bus and the consumer's subscribers are in the same Region and partition. A consumer publishes to the bus and creates subscribers on it in the bus's Region.

## Sharing a bus
<a name="eb-custom-bus-access-ram"></a>

We recommend AWS RAM over a resource policy that you write yourself. AWS RAM gives you one place to see and to revoke what you have shared, it works with AWS Organizations, and it writes the bus's `AWS_RAM` resource policy for you. Create a resource share that names the bus ARN, the consumer accounts or organizational units, and one of the four AWS managed permissions for the bus resource type, each at `arn:aws:ram::aws:permission/{{name}}`.


| Managed permission | What the consumer account can do | 
| --- | --- | 
| AWSRAMEventBridgeEventBusV2PublishOnly | Publish to the bus | 
| AWSRAMEventBridgeEventBusV2SubscribeOnly | Attach subscribers to the bus | 
| AWSRAMEventBridgeEventBusV2EventSourceAccess | Attach and update event sources, and describe the bus | 
| AWSRAMEventBridgeEventBusV2FullAccess | Publish with either API, describe the bus, and create, update, and delete its own subscribers and event sources | 

```
aws ram create-resource-share \
    --name orders-bus-share \
    --resource-arns arn:aws:events:us-east-1:111122223333:event-busv2/orders/EXAMPLE1234567890abcdef \
    --principals 444455556666 \
    --permission-arns arn:aws:ram::aws:permission/AWSRAMEventBridgeEventBusV2SubscribeOnly
```

To grant less than a managed permission, or to add a condition key, author an AWS RAM customer managed permission. AWS RAM rejects one that names a bus owner only action. Read a permission back with the AWS RAM `GetPermission` operation rather than assume its exact action list.

## Unsharing a bus
<a name="eb-custom-bus-access-ram-unshare"></a>

To stop sharing, remove the bus or the principal from the resource share, or delete the share. EventBridge authorizes a subscriber or event source when it is created, so a subscriber the consumer created while the share was active keeps delivering after you unshare. To stop it, revoke it with `RevokeResource`; see [Revoking a subscriber or an event source](eb-custom-bus-access-revoke.md). The consumer can no longer publish or create new subscribers once the share is gone.

## Working with a bus that is shared with you
<a name="eb-custom-bus-access-consumer"></a>

A bus shared with your account appears in your `ListEventBuses` results with the owner's account in its ARN, and you use it by that ARN, in the bus's Region. What you create on it belongs to you: when you list subscribers on the shared bus you see only your own subscribers, while the bus owner sees all of them. Sharing one bus exposes only that bus; you never see the owner's other buses. You cannot update or delete the bus, change its resource policy, or share it onward, and you cannot act on a subscriber that another account owns. The bus owner can withdraw any of your subscribers or event sources with `RevokeResource`; a revoked resource stops permanently and you can only delete it.

## Billing and metering
<a name="eb-custom-bus-access-ram-billing"></a>

Sharing a bus has no charge of its own. Publishing, delivery, and retention are billed as described on the [Amazon EventBridge pricing](https://aws.amazon.com/eventbridge/pricing/) page. The bus owner can see delivery volume per consumer account in the `EventsDelivered` and `EgressBytes` metrics with the `SubscriberAccount` dimension; see [Observability for the Custom Event Bus: metrics, logs, and CloudTrail](eb-custom-bus-observability.md).

## Write a custom resource policy
<a name="eb-custom-bus-access-policy"></a>

An event bus is the only Custom Event Bus resource that takes a resource policy; EventBridge rejects any other resource ARN. A bus holds two named policies. `default` is the one you write, in full IAM policy language including `Deny`. `AWS_RAM` is written only by AWS RAM and reflects your resource shares. EventBridge evaluates both when it authorizes a caller from another account, and an explicit `Deny` in either overrides an `Allow` in the other. When a cross-account caller is denied and the policy you wrote appears to allow them, read the other policy.

The following `default` policy on the `orders` bus lets account `444455556666` attach subscribers and read the bus, and nothing else.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowPartnerAccountToSubscribe",
            "Effect": "Allow",
            "Principal": { "AWS": "arn:aws:iam::444455556666:root" },
            "Action": [
                "events:CreateSubscriber",
                "events:DescribeEventBus"
            ],
            "Resource": "arn:aws:events:us-east-1:111122223333:event-busv2/orders/EXAMPLE1234567890abcdef"
        }
    ]
}
```

Manage the policies with `PutResourcePolicy`, `GetResourcePolicy`, `DeleteResourcePolicy`, and `ListResourcePolicies`. Each takes the bus ARN in `--resource-arn`, and each acts on `default` when you omit `--policy-name`. You cannot write or delete `AWS_RAM`: naming it fails with `AccessDeniedException`. `GetResourcePolicy` fails with `ResourceNotFoundException` when the named policy does not exist, rather than returning an empty document, so treat that as no policy. A bus that you shared only through AWS RAM has no `default` policy, so `get-resource-policy` without `--policy-name` returns that error; pass `--policy-name AWS_RAM` to read the policy AWS RAM wrote. `ListResourcePolicies` returns policy names and revision IDs only, never documents. To make a write or delete conditional, pass the policy's current revision in `--expected-revision-id`; on a mismatch the operation fails with `ConflictException`. A `default` policy document can be up to 20 KB; a larger policy fails with `PolicyLengthExceededException`. This quota is adjustable in Service Quotas.

EventBridge rejects a `default` policy that would grant public access, with `PublicPolicyException`, and does not attach it. This check is always on. A statement grants public access when its principal is a wildcard and no condition limits the callers to specific accounts or principals. A condition on event content, such as `events:source`, does not identify the caller. A condition such as `aws:PrincipalOrgID` does. A policy you write is invisible to AWS RAM, so you own tracking it.

## Events that arrive without a publish call
<a name="eb-custom-bus-access-forwarded"></a>

Events also arrive on a bus without a direct `PutEvents` or `PutRawEvents` call: from an event source, or from a rule or a subscriber on another bus whose target is this bus. An event source is authorized once, when you create it, and nothing is checked again as events arrive, so a bus policy cannot filter that traffic afterwards. See [Event sources for a Custom Event Bus](eb-custom-bus-event-sources.md). A rule or subscriber that you point at a bus yourself is authorized at ingestion, under the role you supplied, once for every event. EventBridge chooses the action per event: `events:PutEvents` for a genuine AWS service or partner event, and `events:PutRawEvents` for an event you originated. You cannot choose the action used, so a forwarder carrying both kinds of events through one path must be granted both actions, in the role's identity policy and in the destination bus's resource policy. Granting only one denies half the stream.