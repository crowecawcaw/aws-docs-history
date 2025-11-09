# Differences between

Amazon Verified Permissions and the Cedar policy language

Amazon Verified Permissions uses the Cedar policy language engine to perform its authorization tasks.
However, there are some differences between the native Cedar implementation and the
implementation of Cedar found in Verified Permissions. This topic identifies those differences.

## Namespace definition

Verified Permissions implementation of Cedar has the following differences from the native Cedar
implementation:

- Verified Permissions supports only one [namespace in
  a schema](https://docs.cedarpolicy.com/schema/schema.html#namespace "https://docs.cedarpolicy.com/schema/schema.html#namespace") defined in a policy store.
- Verified Permissions doesn't allow you to create a [namespace](https://docs.cedarpolicy.com/schema/schema.html#namespace "https://docs.cedarpolicy.com/schema/schema.html#namespace") that's an empty string or includes the following values: `aws`,
  `amazon`, or `cedar`.

## Policy template support

Both Verified Permissions and Cedar allow placeholders in the scope for only the
`principal` and `resource`. However, Verified Permissions also requires that
neither the `principal` and `resource` are unconstrained.

The following policy is valid in Cedar but is rejected by Verified Permissions because the
`principal` is unconstrained.

```
permit(principal, action == Action::"view", resource == ?resource);
```

Both of the following examples are valid in both Cedar and Verified Permissions because both the
`principal` and `resource` have constraints.

```
permit(principal == User::"alice", action == Action::"view", resource == ?resource);
```

```
permit(principal == ?principal, action == Action::"a", resource in ?resource);
```

## Schema support

Verified Permissions requires all schema JSON key names to be non-empty strings. Cedar allows empty
strings in a few cases, such as for properties or namespaces.

## Action groups definition

The Cedar authorization methods require a list of the entities to be considered when
evaluating an authorization request against the policies.

You can define the actions and action groups used by your application in the schema.
However, Cedar doesn't include the schema as part of an evaluation request. Instead,
Cedar uses the schema only to validate the policies and policy templates that you
submit. Because Cedar doesn't reference the schema during evaluation requests, even if
you defined action groups in the schema, you must also include the list of any action
groups as part of the entities list you must pass to the authorization API
operations.

Verified Permissions does this for you. Any action groups that you define in your schema are
automatically appended to the entities list that you pass to as a parameter to the
`IsAuthorized` or `IsAuthorizedWithToken` operations.

## Entity formatting

The JSON formatting of entities in Verified Permissions using the `entityList` parameter differs from Cedar in the following
ways:

- In Verified Permissions, a JSON object must have all of its key-value pairs wrapped in a JSON
  object with the name of `Record`.
- A JSON list in Verified Permissions must be wrapped in a JSON key-value pair where the key name
  is `Set` and the value is the original JSON list from Cedar.
- For `String`, `Long`, and `Boolean` type names,
  each key-value pair from Cedar is replaced by a JSON object in Verified Permissions. The name of
  the object is the original key name. Inside the JSON object, there is one key-value
  pair where the key name is the type name of the scalar value (`String`,
  `Long`, or `Boolean`) and the value is the value from the
  Cedar entity.
- The syntax formatting of Cedar entities and Verified Permissions entities differs in the
  following ways:

| **Cedar format** | **Verified Permissions format** |
| ---------------- | ------------------------------- |
| `uid`            | `Identifier`                    |
| `type`           | `EntityType`                    |
| `id`             | `EntityId`                      |
| `attrs`          | `Attributes`                    |
| `parents`        | `Parents`                       |

###### Example - Lists

The following examples show how a list of entities is expressed in Cedar and Verified Permissions,
respectively.

Cedar

```
[
  {
    "number": 1
  },
  {
    "sentence": "Here is an example sentence"
  },
  {
    "Question": false
  }
]

```

Verified Permissions

```
{
  "Set": [
    {
      "Record": {
        "number": {
          "Long": 1
        }
      }
    },
    {
      "Record": {
        "sentence": {
          "String": "Here is an example sentence"
        }
      }
    },
    {
      "Record": {
        "question": {
          "Boolean": false
        }
      }
    }
  ]
}

```

###### Example - Policy evaluation

The following examples shows how entities are formatted for evaluating a policy in an
authorization request in Cedar and Verified Permissions, respectively.

Cedar

```
[
    {
        "uid": {
            "type": "PhotoApp::User",
            "id": "alice"
        },
        "attrs": {
            "age": 25,
            "name": "alice",
            "userId": "123456789012"
        },
        "parents": [
            {
                "type": "PhotoApp::UserGroup",
                "id": "alice_friends"
            },
            {
                "type": "PhotoApp::UserGroup",
                "id": "AVTeam"
            }
        ]
    },
    {
        "uid": {
            "type": "PhotoApp::Photo",
            "id": "vacationPhoto.jpg"
        },
        "attrs": {
            "private": false,
            "account": {
                "__entity": {
                    "type": "PhotoApp::Account",
                    "id": "ahmad"
                }
            }
        },
        "parents": []
    },
    {
        "uid": {
            "type": "PhotoApp::UserGroup",
            "id": "alice_friends"
        },
        "attrs": {},
        "parents": []
    },
    {
        "uid": {
            "type": "PhotoApp::UserGroup",
            "id": "AVTeam"
        },
        "attrs": {},
        "parents": []
    }
]
```

Verified Permissions

```
[
    {
        "Identifier": {
            "EntityType": "PhotoApp::User",
            "EntityId": "alice"
        },
        "Attributes": {
            "age": {
                "Long": 25
            },
            "name": {
                "String": "alice"
            },
            "userId": {
                "String": "123456789012"
            }
        },
        "Parents": [
            {
                "EntityType": "PhotoApp::UserGroup",
                "EntityId": "alice_friends"
            },
            {
                "EntityType": "PhotoApp::UserGroup",
                "EntityId": "AVTeam"
            }
        ]
    },
    {
        "Identifier": {
            "EntityType": "PhotoApp::Photo",
            "EntityId": "vacationPhoto.jpg"
        },
        "Attributes": {
            "private": {
                "Boolean": false
            },
            "account": {
                "EntityIdentifier": {
                    "EntityType": "PhotoApp::Account",
                    "EntityId": "ahmad"
                }
            }
        },
        "Parents": []
    },
    {
        "Identifier": {
            "EntityType": "PhotoApp::UserGroup",
            "EntityId": "alice_friends"
        },
        "Parents": []
    },
    {
        "Identifier": {
            "EntityType": "PhotoApp::UserGroup",
            "EntityId": "AVTeam"
        },
        "Parents": []
    }
]
```

## Length and size limits

Verified Permissions supports storage in the form of policy stores to hold your schema, policies, and policy templates.
That storage causes Verified Permissions to impose some length and size limits that aren't relevant to
Cedar.

| Object                    | Verified Permissions limit (in bytes) | Cedar limit             |
| ------------------------- | ------------------------------------- | ----------------------- |
| Policy size¹              | 10,000                                | None                    |
| Inline policy description | 150                                   | Not applicable to Cedar |
| Policy template size      | 10,000                                | None                    |
| Schema size               | 100,000                               | None                    |
| Entity type               | 200                                   | None                    |
| Policy ID                 | 64                                    | None                    |
| Policy template ID        | 64                                    | None                    |
| Entity ID                 | 200                                   | None                    |
| Policy store ID           | 64                                    | Not applicable to Cedar |

¹ There is a limit for policies per policy store in Verified Permissions based on the combined size of
principals, actions, and resources of policies created in the policy store. The total size of
all policies pertaining to a single resource can't exceed 200,000 bytes. For template-linked policies, the
size of the policy template is counted only once, plus the size of each set of parameters used to
instantiate each template-linked policy.
