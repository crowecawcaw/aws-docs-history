# Principals

The `Principal` element specifies the user, account, service, or other
entity that is allowed or denied access to a resource. For more
information, see [Principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md")
in the _IAM User Guide_.

## Grant permissions to an AWS account

To grant permissions to an AWS account, identify the account using the
following format.

```
"AWS":"`account-ARN`"
```

The following are examples.

```
"Principal":{"AWS":"arn:aws:iam::`AccountIDWithoutHyphens`:root"}
```

```
"Principal":{"AWS":["arn:aws:iam::`AccountID1WithoutHyphens`:root","arn:aws:iam::`AccountID2WithoutHyphens`:root"]}
```

## Grant permissions to an IAM user

To grant permission to an IAM user within your account, you must provide an
`"AWS":"`user-ARN`"` name-value
pair.

```
"Principal":{"AWS":"arn:aws:iam::`account-number-without-hyphens`:user/`username`"}
```

###### Note

If an IAM identity is deleted after you update your resource policy, the resource policy
will show a unique identifier in the principal element instead of an ARN.
These unique IDs are never reused, so you can safely remove principals with
unique identifiers from all of your policy statements. For more information
about unique identifiers, see [IAM identifiers](../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-unique-ids "../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-unique-ids") in the _IAM User Guide_.

## Grant anonymous permissions

To grant permission to everyone, also referred as anonymous access, you set
the wildcard (`"*"`) as the `Principal` value. For
example, if you want to use clients with no AWS authorization to their origin endpoints.

```
"Principal":"*"
```

```
"Principal":{"AWS":"*"}
```

Using `"Principal": "*"` with an `Allow` effect in a
resource-based policy allows anyone, even if they’re not signed in to AWS, to
access your resource.

Using `"Principal" : { "AWS" : "*" }` with an `Allow`
effect in a resource-based policy allows any root user, IAM user, assumed-role
session, or federated user in any account in the same partition to access your
resource.

For anonymous users, these two methods are equivalent. For more information, see [All principals](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#principal-anonymous "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#principal-anonymous") in the _IAM User Guide_.

You cannot use a wildcard to match part of a principal name or ARN.

###### Important

Because anyone can create an AWS account, the **security level** of these two methods is equivalent, even
though they function differently.

###### Warning

Use caution when granting anonymous access to your MediaPackage origin endpoints. When you
grant anonymous access, anyone in the world can access your bucket. We
highly recommend that you never grant any kind of anonymous write access to
your origin endpoints.
