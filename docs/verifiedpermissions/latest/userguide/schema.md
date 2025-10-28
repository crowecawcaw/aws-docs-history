# Amazon Verified Permissions policy store schema

A _[schema](https://docs.cedarpolicy.com/overview/terminology.html#schema "https://docs.cedarpolicy.com/overview/terminology.html#schema")_ is a declaration of the structure of the entity types
supported by your application, and the actions your application may provide in authorization
requests. To see the difference between how Verified Permissions and Cedar handles schemas, see [Schema support](terminology-differences-avp-cedar.md#differences-templates "terminology-differences-avp-cedar.md#differences-templates").

For more information, see [Cedar schema
format](https://docs.cedarpolicy.com/schema/schema.html "https://docs.cedarpolicy.com/schema/schema.html") in the Cedar policy language Reference Guide.

###### Note

The use of schemas in Verified Permissions is optional, but they are highly recommended for
production software. When you create a new policy, Verified Permissions can use the schema to validate
the entities and attributes referenced in the scope and conditions to avoid typos and
mistakes in policies that can lead to confusing system behavior. If you activate [policy validation](policy-validation-mode.md "policy-validation-mode.md"), then all new policies
must conform with the schema.

AWS Management Console

###### To create a schema

1. Open the [Verified Permissions console](https://console.aws.amazon.com/verifiedpermissions/ "https://console.aws.amazon.com/verifiedpermissions/"). Choose your policy store.
2. In the navigation pane on the left, choose
   **Schema**.
3. Choose **Create schema**.

AWS CLI

###### To submit a new schema, or overwrite an existing schema by using the

AWS CLI.

You can create a policy store by running a AWS CLI command similar to the
following example.

Consider a schema that contains the following Cedar content:

```
{
    "MySampleNamespace": {
        "actions": {
            "remoteAccess": {
                "appliesTo": {
                    "principalTypes": [ "Employee" ]
                }
            }
        },
        "entityTypes": {
            "Employee": {
                "shape": {
                    "type": "Record",
                    "attributes": {
                        "jobLevel": {"type": "Long"},
                        "name": {"type": "String"}
                    }
                }
            }
        }
    }
}
```

You must first escape the JSON into a single line string, and preface it with
a declaration of its data type: `cedarJson`. The following example
uses the following contents of `schema.json` file that
contains the escaped version of the JSON schema.

###### Note

The example here is line wrapped for readability. You must have the entire
file on a single line for the command to accept it.

```
{"cedarJson": "{\"MySampleNamespace\": {\"actions\": {\"remoteAccess\": {\"appliesTo\":
{\"principalTypes\": [\"Employee\"]}}},\"entityTypes\": {\"Employee\": {\"shape\":
{\"attributes\": {\"jobLevel\": {\"type\": \"Long\"},\"name\": {\"type\": \"String\"}},
\"type\": \"Record\"}}}}}"}
```

```
`$` `aws verifiedpermissions put-schema \
 --definition file://schema.json \
 --policy-store PSEXAMPLEabcdefg111111``{
 "policyStoreId": "PSEXAMPLEabcdefg111111",
 "namespaces": [
 "MySampleNamespace"
 ],
 "createdDate": "2023-07-17T21:07:43.659196+00:00",
 "lastUpdatedDate": "2023-08-16T17:03:53.081839+00:00"
}`
```

AWS SDKs
You can create a policy store using the `PutSchema` API. For more
information, see [PutSchema](../apireference/API_PutSchema.md "../apireference/API_PutSchema.md") in the
Amazon Verified Permissions API Reference Guide.
