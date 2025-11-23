# Working with the Object ACL field

An Amazon S3 Inventory report contains a list of the objects in the S3 source bucket and
metadata for each object. The Object access control list (ACL) field is a metadata field
that is available in Amazon S3 Inventory. Specifically, the Object ACL field contains the access
control list (ACL) for each object. The ACL for an object defines which AWS accounts or
groups are granted access to this object and the type of access that is granted. For more
information, see [Access control list (ACL) overview](acl-overview.md "acl-overview.md") and [Amazon S3 Inventory list](storage-inventory.md#storage-inventory-contents "storage-inventory.md#storage-inventory-contents").

The Object ACL field in Amazon S3 Inventory reports is defined in JSON format. The JSON data includes the following fields:

- `version` – The version of the Object ACL field format in the
  inventory reports. It's in date format `yyyy-mm-dd`.
- `status` – Possible values are `AVAILABLE` or
  `UNAVAILABLE` to indicate whether an Object ACL is available for an
  object. When the status for the Object ACL is `UNAVAILABLE`, the value of
  the Object Owner field in the inventory report is also
  `UNAVAILABLE`.
- `grants` – Grantee-permission pairs that list the permission
  status of each grantee that is granted by the Object ACL. The available values for a
  grantee are `CanonicalUser` and `Group`. For more information
  about grantees, see [Grantees in
  access control lists](acl-overview.md#specifying-grantee "acl-overview.md#specifying-grantee").

For a grantee with the `Group` type, a grantee-permission pair includes
the following attributes:

    + `uri` – A predefined Amazon S3 group.
    + `permission` – The ACL permissions that are granted on
     the object. For more information, see [ACL
     permissions on an object](acl-overview.md#permissions "acl-overview.md#permissions").
    + `type` – The type `Group`, which denotes that
     the grantee is group.

For a grantee with the `CanonicalUser` type, a grantee-permission pair
includes the following attributes:

    + `canonicalId` – An obfuscated form of the AWS account
     ID. The canonical user ID for an AWS account is specific to that account.
     You can retrieve the canonical user ID. For more information, see [Find the canonical user ID for your AWS account](../../../accounts/latest/reference/manage-acct-identifiers.md#FindCanonicalId "../../../accounts/latest/reference/manage-acct-identifiers.md#FindCanonicalId") in the
     *AWS Account Management Reference
     Guide*.
    + `permission` – The ACL permissions that are granted on
     the object. For more information, see [ACL
     permissions on an object](acl-overview.md#permissions "acl-overview.md#permissions").
    + `type` – The type `CanonicalUser`, which
     denotes that the grantee is an AWS account.

The following example shows possible values for the Object ACL field in JSON format:

```
{
    "version": "2022-11-10",
    "status": "AVAILABLE",
    "grants": [{
        "uri": "http://acs.amazonaws.com/groups/global/AllUsers",
        "permission": "READ",
        "type": "Group"
    }, {
        "canonicalId": "example-canonical-id",
        "permission": "FULL_CONTROL",
        "type": "CanonicalUser"
    }]
}
```

###### Note

The Object ACL field is defined in JSON format. An inventory report displays the value
for the Object ACL field as a base64-encoded string.

For example, suppose that you have the following Object ACL field in JSON
format:

```
{
        "version": "2022-11-10",
        "status": "AVAILABLE",
        "grants": [{
            "canonicalId": "example-canonical-user-ID",
            "type": "CanonicalUser",
            "permission": "READ"
        }]
}
```

The Object ACL field is encoded and shown as the following base64-encoded
string:

```
eyJ2ZXJzaW9uIjoiMjAyMi0xMS0xMCIsInN0YXR1cyI6IkFWQUlMQUJMRSIsImdyYW50cyI6W3siY2Fub25pY2FsSWQiOiJleGFtcGxlLWNhbm9uaWNhbC11c2VyLUlEIiwidHlwZSI6IkNhbm9uaWNhbFVzZXIiLCJwZXJtaXNzaW9uIjoiUkVBRCJ9XX0=
```

To get the decoded value in JSON for the Object ACL field, you can query this field in
Amazon Athena. For query examples, see [Querying Amazon S3 Inventory with Amazon Athena](storage-inventory-athena-query.md "storage-inventory-athena-query.md").
