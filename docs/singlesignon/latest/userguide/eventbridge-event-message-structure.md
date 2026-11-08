

# EventBridge event message structure
<a name="eventbridge-event-message-structure"></a>

The event message that the IAM Identity Center Identity Store sends to Amazon EventBridge (EventBridge) is in JSON format. Every event contains the following fields.
+ `version` – Currently 0 (zero) for all events. This is an Amazon EventBridge envelope field and isn't used for schema versioning. For event schema versioning, see the `event-version` field in the `detail` field.
+ `id` – A UUID generated for every event.
+ `detail-type` – The type of event that's being sent. For the list of event types, see [IAM Identity Center event notifications](event-notifications.md).
+ `source` – Identifies the service that generated the event. For Identity Store events, this is `aws.identitystore`.
+ `account` – The 12-digit AWS account ID of the account that owns the identity store.
+ `time` – The time the event occurred.
+ `region` – The AWS Region where the event was sent. If your IAM Identity Center instance is replicated to additional AWS Regions, an event sent in an additional AWS Region contains that AWS Region, not the primary AWS Region. For example, if your identity store is in US East (N. Virginia) and is replicated to US West (Oregon), the event sent in US West (Oregon) contains `us-west-2`.
+ `resources` – A JSON array that contains the Amazon Resource Names (ARNs) of the resources involved in the event. The first entry is always the ARN of the identity store. User, group and group membership events also include the ARN of the user, group or membership. Group membership events include the ARNs of the membership, the group and the member.
+ `detail` – A JSON object that contains information about the event. For more information about what can be included in this field, see [Event message detail field](#eventbridge-event-message-detail).

## Event message structure examples
<a name="eventbridge-event-message-examples"></a>

The following are examples of the event messages that the Identity Store sends to Amazon EventBridge, one for each event type.

**User created**

```
{
  "version": "0",
  "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "detail-type": "User Created",
  "source": "aws.identitystore",
  "account": "111122223333",
  "time": "2026-10-30T17:22:25Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:identitystore::111122223333:identitystore/d-1234567890",
    "arn:aws:identitystore:::user/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
  ],
  "detail": {
    "identity-store": {
      "id": "d-1234567890",
      "tenants": {
        "identity-center": [
          "arn:aws:sso:::instance/ssoins-1234567890abcdef"
        ]
      }
    },
    "user": {
      "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    },
    "event-version": "0.1",
    "request-id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555"
  }
}
```

**User updated**

```
{
  "version": "0",
  "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "detail-type": "User Updated",
  "source": "aws.identitystore",
  "account": "111122223333",
  "time": "2026-10-30T17:22:25Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:identitystore::111122223333:identitystore/d-1234567890",
    "arn:aws:identitystore:::user/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
  ],
  "detail": {
    "identity-store": {
      "id": "d-1234567890",
      "tenants": {
        "identity-center": [
          "arn:aws:sso:::instance/ssoins-1234567890abcdef"
        ]
      }
    },
    "user": {
      "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    },
    "event-version": "0.1",
    "request-id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555"
  }
}
```

**User deleted**

```
{
  "version": "0",
  "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "detail-type": "User Deleted",
  "source": "aws.identitystore",
  "account": "111122223333",
  "time": "2026-10-30T17:22:25Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:identitystore::111122223333:identitystore/d-1234567890",
    "arn:aws:identitystore:::user/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
  ],
  "detail": {
    "identity-store": {
      "id": "d-1234567890",
      "tenants": {
        "identity-center": [
          "arn:aws:sso:::instance/ssoins-1234567890abcdef"
        ]
      }
    },
    "user": {
      "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    },
    "event-version": "0.1",
    "request-id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555"
  }
}
```

**Group created**

```
{
  "version": "0",
  "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "detail-type": "Group Created",
  "source": "aws.identitystore",
  "account": "111122223333",
  "time": "2026-10-30T17:22:25Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:identitystore::111122223333:identitystore/d-1234567890",
    "arn:aws:identitystore:::group/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
  ],
  "detail": {
    "identity-store": {
      "id": "d-1234567890",
      "tenants": {
        "identity-center": [
          "arn:aws:sso:::instance/ssoins-1234567890abcdef"
        ]
      }
    },
    "group": {
      "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
    },
    "event-version": "0.1",
    "request-id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555"
  }
}
```

**Group updated**

```
{
  "version": "0",
  "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "detail-type": "Group Updated",
  "source": "aws.identitystore",
  "account": "111122223333",
  "time": "2026-10-30T17:22:25Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:identitystore::111122223333:identitystore/d-1234567890",
    "arn:aws:identitystore:::group/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
  ],
  "detail": {
    "identity-store": {
      "id": "d-1234567890",
      "tenants": {
        "identity-center": [
          "arn:aws:sso:::instance/ssoins-1234567890abcdef"
        ]
      }
    },
    "group": {
      "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
    },
    "event-version": "0.1",
    "request-id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555"
  }
}
```

**Group deleted**

```
{
  "version": "0",
  "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "detail-type": "Group Deleted",
  "source": "aws.identitystore",
  "account": "111122223333",
  "time": "2026-10-30T17:22:25Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:identitystore::111122223333:identitystore/d-1234567890",
    "arn:aws:identitystore:::group/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
  ],
  "detail": {
    "identity-store": {
      "id": "d-1234567890",
      "tenants": {
        "identity-center": [
          "arn:aws:sso:::instance/ssoins-1234567890abcdef"
        ]
      }
    },
    "group": {
      "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
    },
    "event-version": "0.1",
    "request-id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555"
  }
}
```

**Group membership created**

```
{
  "version": "0",
  "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "detail-type": "GroupMembership Created",
  "source": "aws.identitystore",
  "account": "111122223333",
  "time": "2026-10-30T17:22:25Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:identitystore::111122223333:identitystore/d-1234567890",
    "arn:aws:identitystore:::membership/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
    "arn:aws:identitystore:::group/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "arn:aws:identitystore:::user/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
  ],
  "detail": {
    "identity-store": {
      "id": "d-1234567890",
      "tenants": {
        "identity-center": [
          "arn:aws:sso:::instance/ssoins-1234567890abcdef"
        ]
      }
    },
    "group": {
      "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
    },
    "member": {
      "user": {
        "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
      }
    },
    "membership": {
      "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333"
    },
    "event-version": "0.1",
    "request-id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555"
  }
}
```

**Group membership deleted**

```
{
  "version": "0",
  "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "detail-type": "GroupMembership Deleted",
  "source": "aws.identitystore",
  "account": "111122223333",
  "time": "2026-10-30T17:22:25Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:identitystore::111122223333:identitystore/d-1234567890",
    "arn:aws:identitystore:::membership/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
    "arn:aws:identitystore:::group/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "arn:aws:identitystore:::user/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
  ],
  "detail": {
    "identity-store": {
      "id": "d-1234567890",
      "tenants": {
        "identity-center": [
          "arn:aws:sso:::instance/ssoins-1234567890abcdef"
        ]
      }
    },
    "group": {
      "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
    },
    "member": {
      "user": {
        "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
      }
    },
    "membership": {
      "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333"
    },
    "event-version": "0.1",
    "request-id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555"
  }
}
```

**Identity store created**

```
{
  "version": "0",
  "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "detail-type": "IdentityStore Created",
  "source": "aws.identitystore",
  "account": "111122223333",
  "time": "2026-10-30T17:22:25Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:identitystore::111122223333:identitystore/d-1234567890"
  ],
  "detail": {
    "identity-store": {
      "id": "d-1234567890",
      "tenants": {
        "identity-center": [
          "arn:aws:sso:::instance/ssoins-1234567890abcdef"
        ]
      }
    },
    "event-version": "0.1",
    "request-id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555"
  }
}
```

**Identity store updated**

```
{
  "version": "0",
  "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "detail-type": "IdentityStore Updated",
  "source": "aws.identitystore",
  "account": "111122223333",
  "time": "2026-10-30T17:22:25Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:identitystore::111122223333:identitystore/d-1234567890"
  ],
  "detail": {
    "identity-store": {
      "id": "d-1234567890",
      "tenants": {
        "identity-center": [
          "arn:aws:sso:::instance/ssoins-1234567890abcdef"
        ]
      }
    },
    "event-version": "0.1",
    "request-id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555"
  }
}
```

**Identity store deleted**

```
{
  "version": "0",
  "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
  "detail-type": "IdentityStore Deleted",
  "source": "aws.identitystore",
  "account": "111122223333",
  "time": "2026-10-30T17:22:25Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:identitystore::111122223333:identitystore/d-1234567890"
  ],
  "detail": {
    "identity-store": {
      "id": "d-1234567890",
      "tenants": {
        "identity-center": [
          "arn:aws:sso:::instance/ssoins-1234567890abcdef"
        ]
      }
    },
    "event-version": "0.1",
    "request-id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555"
  }
}
```

## Event message detail field
<a name="eventbridge-event-message-detail"></a>

The `detail` field contains a JSON object with information about the event. The following fields can be present in the `detail` field.
+ `event-version` – The event schema version in the form `major.minor` (for example, 0.1). See [Event schema versioning](#eventbridge-event-schema-versioning).
+ `identity-store` – Information about the identity store involved in the event. Present in all events. Contains `id`, the identity store ID (for example, `d-1234567890`), and `tenants`. In `tenants`, `identity-center` is a JSON array of the ARNs of the IAM Identity Center instances that use this identity store.
+ `user` – For `User Created`, `User Updated` and `User Deleted` events, the user involved in the event. Contains `id`, the user ID in the identity store.
+ `group` – For `Group` and `GroupMembership` events, the group involved in the event. Contains `id`, the group ID in the identity store.
+ `member` – For `GroupMembership` events, the member that was added to or removed from the group. Contains `user`, which holds `id`, the user ID in the identity store.
+ `membership` – For `GroupMembership` events, the group membership involved in the event. Contains `id`, the membership ID in the identity store.
+ `request-id` – The ID of the request that caused the change.

## Event schema versioning
<a name="eventbridge-event-schema-versioning"></a>

The major version is incremented if the Identity Store makes a change to the event structure that's not backward compatible. This includes removing a JSON field that's already present or changing how the contents of a field are represented (for example, a date format).

The minor version is incremented if the Identity Store makes a backward-compatible change to the event structure. This includes adding new fields to the event structure or introducing new event types. To stay compatible with new minor versions of the event structure, we recommend that your applications ignore new fields.

To make sure that your applications can parse the event structure correctly, we recommend that you do an equal-to comparison on the major version number. To make sure that the fields that your application expects are present, we also recommend doing a greater-than-or-equal-to comparison on the minor version.

**Note**  
Events identify the resource that changed but don't include its attributes. For example, a `User Updated` event contains the user ID, but not the user name, email or which attributes changed. To get the current attributes, call the Identity Store API, for example `DescribeUser`, `DescribeGroup` or `DescribeGroupMembership`. After a `Deleted` event, the resource no longer exists and can't be described.