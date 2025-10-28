# Adding context

_Context_ is the information that's relevant to policy
decisions, but not part of the identity of your principal, action, or resource. Access token
claim are context. You might want to allow an action only from a set of source IP addresses,
or only if your user has signed in with MFA. Your application has access to this contextual
session data and must populate it to authorization requests. The context data in a Verified Permissions
authorization request must be JSON-formatted in a `contextMap` element.

The examples that illustrate this content come from a [sample policy store](policy-stores-create.md "policy-stores-create.md"). To follow along, create the
**DigitalPetStore** sample policy store in your testing environment.

The following context object declares one of each Cedar data type for an application
based on the sample **DigitalPetStore** policy store.

```
"context": {
  "contextMap": {
    "AccountCodes": {
      "set": [
        {
          "long": 111122223333
        },
        {
          "long": 444455556666
        },
        {
          "long": 123456789012
        }
      ]
    },
    "approvedBy": {
    "entityIdentifier": {
      "entityId": "Bob",
      "entityType": "DigitalPetStore::User"
    }
    },
    "MfaAuthorized": {
      "boolean": true
    },
    "NetworkInfo": {
      "record": {
        "IPAddress": {
          "string": "192.0.2.178"
        },
        "Country": {
          "string": "United States of America"
        },
        "SSL": {
          "boolean": true
        }
    }
    },
    "RequestedOrderCount": {
      "long": 4
    },
    "UserAgent": {
      "string": "My UserAgent 1.12"
    }
  }
}
```

###### Data types in authorization context

**Boolean**

A binary `true` or `false` value. In the example, the
boolean value of `true` for `MfaAuthenticated` indicates
that the customer has performed multi-factor authentication before requesting to
view their order.

**Set**

A collection of context elements. Set members can be all the same type, like
in this example, or of different types, including a nested set. In the example,
the customer is associated with 3 different accounts.

**String**

A sequence of letters, numbers, or symbols, enclosed in `"`
characters. In the example, the `UserAgent` string represents the
browser that the customer used to request to view their order.

**Long**

An integer. In the example, the `RequestedOrderCount` indicates
that this request is part of a batch that resulted from the customer asking to
view four of their past orders.

**Record**

A collection of attributes. You must declare these attributes in the request
context. A policy store with a schema must include this entity and the attributes of the
entity in the schema. In the example, the `NetworkInfo` record
contains information about the user's originating IP, the geolocation of that IP
as determined by the client, and encryption in transit.

**EntityIdentifier**

A reference to an entity and attributes declared in the `entities`
element of the request. In the example, the user's order was approved by
employee `Bob`.

To test this example context in the example **DigitalPetStore** app, you
must update your request `entities`, your policy store schema, and the static policy with the
description **Customer Role - Get Order**.

## Modifying DigitalPetStore to accept

authorization context

Initially, **DigitalPetStore** is not a very complex policy store. It doesn't
include any preconfigured policies or context attributes to support the context that we
have presented. To evaluate an example authorization request with this context
information, make the following modifications to your policy store and your authorization
request. For context examples with access token information as the context, see [Mapping Amazon Cognito access tokens](cognito-map-token-to-schema.md#cognito-map-access-token "cognito-map-token-to-schema.md#cognito-map-access-token") and
[Mapping OIDC access tokens](oidc-map-token-to-schema.md#oidc-map-access-token "oidc-map-token-to-schema.md#oidc-map-access-token").

Schema
Apply the following updates to your policy store schema to support the new context
attributes. Update `GetOrder` in `actions` as
follows.

```
"GetOrder": {
  "memberOf": [],
  "appliesTo": {
    "resourceTypes": [
      "Order"
    ],
    "context": {
      "type": "Record",
      "attributes": {
        "AccountCodes": {
          "type": "Set",
          "required": true,
          "element": {
            "type": "Long"
          }
        },
        "approvedBy": {
          "name": "User",
          "required": true,
          "type": "Entity"
        },
        "MfaAuthorized": {
          "type": "Boolean",
          "required": true
        },
        "NetworkInfo": {
          "type": "NetworkInfo",
          "required": true
        },
        "RequestedOrderCount": {
          "type": "Long",
          "required": true
        },
        "UserAgent": {
          "required": true,
          "type": "String"
        }
      }
    },
    "principalTypes": [
      "User"
    ]
  }
}
```

To reference the `record` data type named
`NetworkInfo` in your request context, create a [commonType](https://docs.cedarpolicy.com/schema/schema.html#schema-commonTypes "https://docs.cedarpolicy.com/schema/schema.html#schema-commonTypes") construct in your schema by adding the following to your schema before `actions`. A
`commonType` construct is a shared set of attributes that you
can apply to different entities.

```
"commonTypes": {
  "NetworkInfo": {
    "attributes": {
      "IPAddress": {
        "type": "String",
        "required": true
      },
      "SSL": {
        "required": true,
        "type": "Boolean"
      },
      "Country": {
        "required": true,
        "type": "String"
      }
    },
    "type": "Record"
  }
},
```

Policy
The following policy sets up conditions that must be fulfilled by each of
the provided context elements. It builds on the existing static policy with the
description **Customer Role - Get Order**. This policy
initially only requires that the principal that makes a request is the owner
of the resource.

```
permit (
    principal in DigitalPetStore::Role::"Customer",
    action in [DigitalPetStore::Action::"GetOrder"],
    resource
) when {
    principal == resource.owner &&
    context.AccountCodes.contains(111122223333) &&
    context.approvedBy in DigitalPetStore::Role::"Employee" &&
    context.MfaAuthorized == true &&
    context.NetworkInfo.Country like "*United States*" &&
    context.NetworkInfo.IPAddress like "192.0.2.*" &&
    context.NetworkInfo.SSL == true &&
    context.RequestedOrderCount <= 4 &&
    context.UserAgent like "*My UserAgent*"
};
```

We have now required that the request to retrieve an order meets the
additional context conditions that we added to the request.

1. The user must have signed in with MFA.
2. The user's web browser `User-Agent` must contain the
   string `My UserAgent`.
3. The user must have requested to view 4 or fewer orders.
4. One of the user's account codes must be
   `111122223333`.
5. The user's IP address must originate in the United States, they
   must be on an encrypted session, and their IP address must begin
   with `192.0.2.`.
6. An employee must have approved their order. In the
   `entities` element of the authorization request, we
   will declare a user `Bob` who has the role of
   `Employee`.

Request body
After you configure your policy store with the appropriate schema and policy, you
can present this authorization request to the Verified Permissions API operation [IsAuthorized](../apireference/API_IsAuthorized.md "../apireference/API_IsAuthorized.md"). Note that the `entities` segment
contains a definition of `Bob`, a user with a role of
`Employee`.

```
{
  "principal": {
    "entityType": "DigitalPetStore::User",
    "entityId": "Alice"
  },
  "action": {
    "actionType": "DigitalPetStore::Action",
    "actionId": "GetOrder"
  },
  "resource": {
    "entityType": "DigitalPetStore::Order",
    "entityId": "1234"
  },
  "context": {
    "contextMap": {
      "AccountCodes": {
        "set": [
          {"long": 111122223333},
          {"long": 444455556666},
          {"long": 123456789012}
        ]
      },
      "approvedBy": {
        "entityIdentifier": {
          "entityId": "Bob",
          "entityType": "DigitalPetStore::User"
        }
      },
      "MfaAuthorized": {
        "boolean": true
      },
      "NetworkInfo": {
        "record": {
          "Country": {"string": "United States of America"},
          "IPAddress": {"string": "192.0.2.178"},
          "SSL": {"boolean": true}
        }
      },
      "RequestedOrderCount":{
        "long": 4
      },
      "UserAgent": {
        "string": "My UserAgent 1.12"
      }
    }
  },
  "entities": {
    "entityList": [
      {
        "identifier": {
          "entityType": "DigitalPetStore::User",
          "entityId": "Alice"
        },
        "attributes": {
          "memberId": {
            "string": "801b87f2-1a5c-40b3-b580-eacad506d4e6"
          }
        },
        "parents": [
          {
            "entityType": "DigitalPetStore::Role",
            "entityId": "Customer"
          }
        ]
      },
      {
        "identifier": {
          "entityType": "DigitalPetStore::User",
          "entityId": "Bob"
        },
        "attributes": {
          "memberId": {
            "string": "49d9b81e-735d-429c-989d-93bec0bcfd8b"
          }
        },
        "parents": [
          {
            "entityType": "DigitalPetStore::Role",
            "entityId": "Employee"
          }
        ]
      },
      {
        "identifier": {
          "entityType": "DigitalPetStore::Order",
          "entityId": "1234"
        },
        "attributes": {
          "owner": {
            "entityIdentifier": {
              "entityType": "DigitalPetStore::User",
              "entityId": "Alice"
            }
          }
        },
        "parents": []
      }
     ]
   },
   "policyStoreId": "PSEXAMPLEabcdefg111111"
}
```
