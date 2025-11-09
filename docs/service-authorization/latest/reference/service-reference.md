# Simplified AWS service information for programmatic

access

AWS provides service reference information in JSON format to streamline the automation
of policy management workflows. With the service reference information, you can access
available operations, actions, resources, and condition keys across AWS services from machine-readable
files. Service reference information includes metadata beyond authorization details,
including IAM action last accessed information and IAM Access Analyzer policy generation
data.

Security administrators can establish guardrails and developers can ensure appropriate
access to applications by identifying the available actions, resources, and condition keys
for each AWS service. AWS provides service reference information for AWS services to
allow you to incorporate the metadata into your policy management workflows.

- For an inventory of actions, resources, and condition keys for use in IAM
  policies, see the [Service Authorization Reference](reference_policies_actions-resources-contextkeys.md "reference_policies_actions-resources-contextkeys.md") page for the AWS service. Actions, resources, and
  condition keys for services that share a service prefix may be split across multiple
  pages in the Service Authorization Reference.
- For a list of AWS services and actions for which IAM action last accessed
  information is displayed, see [IAM action last accessed information services and actions](../../../IAM/latest/UserGuide/access_policies_last-accessed-action-last-accessed.md "../../../IAM/latest/UserGuide/access_policies_last-accessed-action-last-accessed.md") in the
  IAM User Guide.
- For a list of AWS services and actions for which IAM Access Analyzer generates
  policies with action-level information, see [IAM Access Analyzer policy generation services](../../../IAM/latest/UserGuide/access-analyzer-policy-generation-action-last-accessed-support.md "../../../IAM/latest/UserGuide/access-analyzer-policy-generation-action-last-accessed-support.md") in the
  IAM User Guide.
  The content presented in the Service Authorization Reference may be presented differently or contain different
  metadata. For more information, see [Additional field
  definitions](#service-reference-additional-field-definitions "#service-reference-additional-field-definitions").

The service reference information also offers metadata on operations, including information on authorized actions and the method names in SDKs.

Additional context of the value of condition keys may be available to assist in scoping permissions. For example, the value of `iam:PassedToService` may appear when the action `iam:PassRole` is authorized by an operation.

This operation to action mapping is not supported for all services. Services that don't yet support this mapping will omit the AuthorizedAction property. Additionally, authorized action information for operations does not include permissions that might be required for operations called on your behalf with [Forward Access Sessions](../../../IAM/latest/UserGuide/access_forward_access_sessions.md "../../../IAM/latest/UserGuide/access_forward_access_sessions.md").

###### Note

Changes to the service reference information may take up to 24 hours to be reflected
in the list of metadata for the service.

###### Accessing AWS service reference information

1. Navigate to the service reference information to access the list of AWS services for
   which reference information is available.

There are two main entry points:

[http://servicereference.us-east-1.amazonaws.com/](http://servicereference.us-east-1.amazonaws.com/ "http://servicereference.us-east-1.amazonaws.com/") displays a list of AWS services for which reference information is available.

The following example shows a partial list of services and URLs for their
respective reference information:

```
[
    {
        "service": "s3",
        "url": "https://servicereference.us-east-1.amazonaws.com/v1/s3/s3.json"
    },
    {
        "service": "dynamodb",
        "url": "https://servicereference.us-east-1.amazonaws.com/v1/dynamodb/dynamodb.json"
    },
    …
]
```

[https://servicereference.us-east-1.amazonaws.com/v1/mapping.json](https://servicereference.us-east-1.amazonaws.com/v1/mapping.json "https://servicereference.us-east-1.amazonaws.com/v1/mapping.json") displays a mapping from SDK services to the location in the service reference that information can be found under.

The following example shows a partial list of mappings:

```
{
  "SDK" : {
    "Python" : {
      "Boto3" : {
        "accessanalyzer" : {
          "service" : "access-analyzer",
          "url" : "https://servicereference.us-east-1.amazonaws.com/v1/access-analyzer/access-analyzer.json"
        },
        "account" : {
          "service" : "account",
          "url" : "https://servicereference.us-east-1.amazonaws.com/v1/account/account.json"
        },
        "amp" : {
          "service" : "aps",
          "url" : "https://servicereference.us-east-1.amazonaws.com/v1/aps/aps.json"
        },
        ...
      }
    }
  }
}
```

2. Choose a service and navigate to the service information page in the
   `url` field for the service to view a list of actions, resources, and
   condition keys for the service.

The following example shows a partial list of service reference information for
Amazon S3:

```
{
    "Name": "s3",
    "Actions": [
        {
            "Name": "GetObject",
            "ActionConditionKeys": [
                "s3:AccessGrantsInstanceArn",
                "s3:AccessPointNetworkOrigin",
                "s3:DataAccessPointAccount",
                "s3:DataAccessPointArn",
                "s3:ExistingObjectTag/key",
                "s3:ResourceAccount",
                "s3:TlsVersion",
                "s3:authType",
                "s3:if-match",
                "s3:if-none-match",
                "s3:signatureAge",
                "s3:signatureversion",
                "s3:x-amz-content-sha256"
            ],
            "Annotations" : {
            "Properties" : {
                    "IsList" : false,
                    "IsPermissionManagement" : false,
                    "IsTaggingOnly" : false,
                    "IsWrite" : false
                }
            },
            "Resources": [
                {
                    "Name": "object"
                }
            ],
            "SupportedBy" : {
                "IAM Access Analyzer Policy Generation" : false,
                "IAM Action Last Accessed" : false
            }
        },
        {
            "Name": "ListBucket",
            "ActionConditionKeys": [
                "s3:AccessGrantsInstanceArn",
                "s3:AccessPointNetworkOrigin",
                "s3:DataAccessPointAccount",
                "s3:DataAccessPointArn",
                "s3:ResourceAccount",
                "s3:TlsVersion",
                "s3:authType",
                "s3:delimiter",
                "s3:max-keys",
                "s3:prefix",
                "s3:signatureAge",
                "s3:signatureversion",
                "s3:x-amz-content-sha256"
            ],
            "Annotations" : {
                "Properties" : {
                    "IsList" : true,
                    "IsPermissionManagement" : false,
                    "IsTaggingOnly" : false,
                    "IsWrite" : false
                }
            },
            "Resources": [
                {
                    "Name": "bucket"
                }
            ],
            "SupportedBy" : {
                "IAM Access Analyzer Policy Generation" : false,
                "IAM Action Last Accessed" : false
            }
        },
        ...
    ],
    "ConditionKeys": [
        {
            "Name": "s3:TlsVersion",
            "Types": [
                "Numeric"
            ]
        },
        {
            "Name": "s3:authType",
            "Types": [
                "String"
            ]
        },
        ...
    ],
    "Operations": [
        {
            "Name" : "GetObject",
            "AuthorizedActions" : [
                {
                    "Name" : "GetObject",
                    "Service" : "s3"
                }, {
                    "Name" : "GetObject",
                    "Service" : "s3-object-lambda"
                }, {
                    "Name" : "GetObjectLegalHold",
                    "Service" : "s3"
                }, {
                    "Name" : "GetObjectRetention",
                    "Service" : "s3"
                }, {
                    "Name" : "GetObjectTagging",
                    "Service" : "s3"
                }, {
                    "Name" : "GetObjectVersion",
                    "Service" : "s3"
                }
            ],
            "SDK" : [
                {
                    "Name" : "s3",
                    "Method" : "get_object",
                    "Package" : "Boto3"
                }
            ]
        },
        ...
    ],
    "Resources": [
        {
            "Name": "accesspoint",
            "ARNFormats": [
                "arn:${Partition}:s3:${Region}:${Account}:accesspoint/${AccessPointName}"
            ]
        },
        {
            "Name": "bucket",
            "ARNFormats": [
                "arn:${Partition}:s3:::${BucketName}"
            ]
        }
        ...
    ],
    "Version": "v1.4"
}
```

3. Download the JSON file from the service URL to use in your policy authoring
   workflows.

## Glossary

- Operation - An API that can be called, usually through an SDK
- Action - Permission that is authorized when performing an operation

## Additional field

definitions

**Action properties** provide additional metadata about
service actions to help categorize them based on their permission scope. These
properties are found under the `Annotations` field for each action. The
metadata consists of four boolean values:

- `IsList` – Provides permissions to discover and list
  resources, including basic metadata, without accessing resource contents.

**Example** – This property is
`true` for the Amazon S3 `ListBucket` action, allowing
users to view bucket listings without accessing the objects themselves.

- `IsPermissionManagement` – Provides permissions to modify
  IAM permissions or access credentials.

**Example** – This property is
`true` for most IAM and AWS Organizations actions, as well as Amazon S3
actions like `PutBucketPolicy` and
`DeleteBucketPolicy`.

- `IsTaggingOnly` – Provides permissions only for modifying
  tags.

**Example** – This property is
`true` for IAM actions `TagRole` and
`UntagRole`, while this property is `false` for
`CreateRole` since it provides broader permissions beyond
tagging.

- `IsWrite` – Provides permissions to modify resources, which
  may include tag modifications.

**Example** – This property is
`true` for Amazon S3 actions `CreateBucket`,
`DeleteBucket`, and `PutObject` since they allow
resource modification.

###### Note

These properties are not mutually exclusive. An action may have multiple
properties set to `true`.

It's also possible for all properties to be `false`, as seen with
Amazon S3's `GetObject` action. This indicates the action only grants read
permissions on an object.

These properties can be used to generate insights for services. The following example
shows which permissions with the `s3` prefix allow mutating resources:

```
> curl https://servicereference.us-east-1.amazonaws.com/v1/s3/s3.json | \
    jq '.Actions[] | select(.Annotations.Properties.IsWrite == true) | .Name'

"AssociateAccessGrantsIdentityCenter"
"BypassGovernanceRetention"
"CreateAccessGrant"
"CreateAccessGrantsInstance"
"CreateAccessGrantsLocation"
...
```

The following example shows which action condition keys with the `lambda`
prefix you can use to limit access to permission management actions:

```
> curl https://servicereference.us-east-1.amazonaws.com/v1/lambda/lambda.json | \
    jq '.Actions[] | select(.Annotations.Properties.IsPermissionManagement == true) | {Name: .Name, ActionConditionKeys: (.ActionConditionKeys // [])}'

{
   "Name": "AddLayerVersionPermission",
    "ActionConditionKeys": []
}
{
    "Name": "AddPermission",
    "ActionConditionKeys": [
        "lambda:FunctionUrlAuthType",
        "lambda:Principal"
    ]
}
{
    "Name": "DisableReplication",
    "ActionConditionKeys": []
}
{
    "Name": "EnableReplication",
    "ActionConditionKeys": []
}
{
    "Name": "RemoveLayerVersionPermission",
    "ActionConditionKeys": []
}
{
    "Name": "RemovePermission",
    "ActionConditionKeys": [
        "lambda:FunctionUrlAuthType",
        "lambda:Principal"
    ]
}
```
