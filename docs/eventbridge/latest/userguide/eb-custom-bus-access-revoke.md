

# Revoking a subscriber or an event source
<a name="eb-custom-bus-access-revoke"></a>

`RevokeResource` withdraws one subscriber or one event source from a bus. It is the only control a bus owner has over a resource that another account owns, and it needs no cooperation from that account. It is authorized against the bus, and only the account that owns the bus can call it. The account that owns the subscriber cannot revoke its own subscriber.

**Note**  
You revoke with the AWS CLI (`aws eventsv2 revoke-resource`), the API, or an SDK. The console does not offer revocation.

Revocation is terminal and cannot be undone. A revoked subscriber stops delivering and refuses mutating operations with `InvalidStateException`. A revoked event source stops ingesting: each event it would have forwarded is refused as it arrives. `DeleteSubscriber` and `DeleteEventSource` stay available so that the resource's owner can clean it up. `DescribeSubscriber`, `DescribeEventSource`, and both list operations return a `Revoked` field that is present only when it is `true`.

**Important**  
There is no undo, so confirm the target with `DescribeSubscriber` or `DescribeEventSource` before you revoke. Check the ARN, the bus, and the target.

Revocation covers one resource, not the account that created it. That account can create another subscriber or event source and carry on. To stop the account, also deny it `events:CreateSubscriber` and `events:CreateEventSource` in the bus resource policy, or delete the AWS RAM share. Deleting the resource is not an alternative: `DeleteSubscriber` and `DeleteEventSource` are authorized against the resource named in the request, so only its owner can delete it.