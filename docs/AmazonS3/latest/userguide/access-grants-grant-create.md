# Create grants

An individual access _grant_ in an S3 Access Grants instance allows a specific identity—an AWS Identity and Access Management (IAM) principal, or a user or group in a corporate directory—to get access within a location that is registered in your S3 Access Grants instance. A location maps buckets or prefixes to an IAM role. S3 Access Grants assumes this IAM role to vend temporary credentials to grantees.

After you [register at least one
location](access-grants-location.md "access-grants-location.md") in your S3 Access Grants instance, you can create an access grant.

The grantee can be an IAM user or role or a directory user or group. A
directory user is a user from your corporate directory or external identity source that you [associated with your
S3 Access Grants instance](access-grants-instance-idc.md "access-grants-instance-idc.md"). For more information, see [S3 Access Grants and corporate directory identities](access-grants-directory-ids.md "access-grants-directory-ids.md"). To create a grant for a specific directory user or group from IAM Identity Center, find
the GUID that IAM Identity Center uses to identify that user in IAM Identity Center, for example,
`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`. For more information about how to use IAM Identity Center to view user information, see [View user and group assignments](../../../singlesignon/latest/userguide/get-started-view-assignments.md "../../../singlesignon/latest/userguide/get-started-view-assignments.md") in the _AWS IAM Identity Center user guide_.

You can grant access to a bucket, a prefix, or an object. A prefix in Amazon S3 is a string
of characters in the beginning of an object key name that is used to organize objects within
a bucket. This can be any string of allowed characters, for example, object key names in your
bucket that start with the `engineering/` prefix.

## Subprefix

When granting access to a registered location, you can use the `Subprefix` field
to narrow the scope of access to a subset of the location scope. If the registered location that you choose for the grant is the default S3 path (`s3://`), you must narrow the grant scope. You cannot create an access grant for the default location (`s3://`), which would
give the grantee access to every bucket in an AWS Region. Instead, you must narrow the grant scope to one of the following:

- A bucket: `s3://`bucket`/*`
- A prefix within a bucket:
  `s3://`bucket`/`prefix`*`
- A prefix within a prefix:
  `s3://`bucket`/`prefixA`/`prefixB`*`
- An object:
  `s3://`bucket`/`object-key-name``

If you are creating an access grant where the registered location is a bucket, you can pass
one of the following in the `Subprefix` field to narrow the grant scope:

- A prefix within the bucket: ``prefix`\*`
- A prefix within a prefix:
  `prefixA/`prefixB`*`
- An object: `/`object-key-name``

After you create the grant, the grant scope that's displayed in the Amazon S3 console or the `GrantScope` that is returned in
the API or AWS Command Line Interface (AWS CLI) response is the result of concatenating the location path
with the `Subprefix`. Make sure that this concatenated path maps correctly to
the S3 bucket, prefix, or object to which you want to grant access.

###### Note

- If you need to create an access grant that grants access to only one object, you must specify that the grant type is for an object. To do this in an
  API call or a CLI command, pass the `s3PrefixType` parameter with the value
  `Object`. In the Amazon S3 console, when you create the grant, after you select a location, under **Grant Scope**, select the **Grant scope is an object** checkbox.
- You cannot create a grant to a bucket if the bucket does not yet exist. However, you can create a grant
  to a prefix that does not yet exist.
- For the maximum number of grants that you can create in your S3 Access Grants instance, see [S3 Access Grants limitations](access-grants-limitations.md "access-grants-limitations.md").

You can create an access grant by using the Amazon S3 console, AWS CLI, the Amazon S3 REST API, and AWS
SDKs.

###### To create an access grant

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Access
   Grants**.
3. On the **S3 Access Grants** page, choose the Region that contains
   the S3 Access Grants instance that you want to work with.

If you're using the S3 Access Grants instance for the first time, make sure that you
have completed [Step 2 -
register a location](access-grants-location.md "access-grants-location.md") and navigated to **Step 3**
of the **Set up Access Grants instance** wizard. If you
already have an S3 Access Grants instance, choose **View details**,
and then from the **Grants** tab, choose **Create
grant**.

    1. In the **Grant scope** section, select or enter a
     registered location.


    If you selected the default `s3://` location, use the
     **Subprefix** box to can narrow the scope of
     the access grant. For more information, see [Subprefix](access-grants-grant.md#subprefix "access-grants-grant.md#subprefix"). If you're granting access only to an object,
     select **Grant scope is an object**.
    2. Under **Permissions and access**, select the
     **Permission** level, either
     **Read**, **Write**, or both.


    Then choose the **Grantee type**. If you have
     added your corporate directory to IAM Identity Center and associated this IAM Identity Center
     instance with your S3 Access Grants instance, you can choose
     **Directory identity from IAM Identity Center**. If you
     choose this option, get the ID of the user or group from IAM Identity Center and
     enter it in this section.


    If the **Grantee type** is an IAM user or role,
     choose **IAM principal**. Under **IAM
     principal type**, choose **User** or
     **Role**. Then, under **IAM principal
     user**, either choose from the list or enter the
     identity's ID.
    3. To create the S3 Access Grants grant, choose **Next** or
     **Create grant**.

4. If **Next** or **Create grant** is
   disabled:

###### Cannot create grant

    * You might need to [register a location](access-grants-location.md "access-grants-location.md") first in your S3 Access Grants
     instance.
    * You might not have the `s3:CreateAccessGrant` permission to
     create an access grant. Contact your account administrator.

To install the AWS CLI, see [Installing the
AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

The following examples show how to create an access grant request for an IAM
principal and how to create an access grant request for a corporate directory user
or group.

To use the following example commands, replace the `user input
 placeholders` with your own information.

###### Note

If you're creating an access grant that grants access to only one object,
include the required parameter `--s3-prefix-type Object`.

###### Example Create an access grant request for an IAM principal

```
aws s3control create-access-grant \
--account-id `111122223333` \
--access-grants-location-id `a1b2c3d4-5678-90ab-cdef-EXAMPLE22222` \
--access-grants-location-configuration `S3SubPrefix=prefixB*` \
--permission `READ` \
--grantee GranteeType=`IAM`,GranteeIdentifier=arn:aws:iam::`123456789012`:`user`/`data-consumer-3`
```

###### Example Create an access grant response

```
{"CreatedAt": "2023-05-31T18:41:34.663000+00:00",
    "AccessGrantId": "`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`",
    "AccessGrantArn": "arn:aws:s3:`us-east-2`:`111122223333`:access-grants/default/grant/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`",
    "Grantee": {
        "GranteeType": "IAM",
        "GranteeIdentifier": "arn:aws:iam::`111122223333`:user/data-consumer-3"
    },
    "AccessGrantsLocationId": "`a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`",
    "AccessGrantsLocationConfiguration": {
        "S3SubPrefix": "prefixB*"
    },
    "GrantScope": "s3://amzn-s3-demo-bucket/prefix*",
    "Permission": "READ"
}

```

###### Create an access grant request for a directory user or group

To create an access grant request for a directory user or group, you must
first get the GUID for the directory user or group by running one of the
following commands.

###### Example Get a GUID for a directory user or group

You can find the GUID of an IAM Identity Center user through the IAM Identity Center console or by using
the AWS CLI or AWS SDKs. The following command lists the users in he specified
IAM Identity Center instance, with their names and identifiers.

```
aws identitystore list-users --identity-store-id `d-1a2b3c4d1234`

```

This command lists the groups in the specified IAM Identity Center instance.

```
aws identitystore list-groups --identity-store-id `d-1a2b3c4d1234`

```

###### Example Create an access grant for a directory user or group

This command is similar to creating a grant for IAM users or roles, except
the grantee type is `DIRECTORY_USER` or `DIRECTORY_GROUP`,
and the grantee identifier is the GUID for the directory user or group.

```
aws s3control create-access-grant \
--account-id `123456789012` \
--access-grants-location-id `default` \
--access-grants-location-configuration `S3SubPrefix="`amzn-s3-demo-bucket`/rafael/*`" \
--permission `READWRITE` \
--grantee GranteeType=`DIRECTORY_USER`,GranteeIdentifier=`83d43802-00b1-7054-db02-f1d683aacba5` \
```

For information about the Amazon S3 REST API support for managing access grants, see the
following sections in the _Amazon Simple Storage Service API Reference_:

- [CreateAccessGrant](../API/API_control_CreateAccessGrant.md "../API/API_control_CreateAccessGrant.md")
- [DeleteAccessGrant](../API/API_control_DeleteAccessGrant.md "../API/API_control_DeleteAccessGrant.md")
- [GetAccessGrant](../API/API_control_GetAccessGrant.md "../API/API_control_GetAccessGrant.md")
- [ListAccessGrants](../API/API_control_ListAccessGrants.md "../API/API_control_ListAccessGrants.md")
  This section provides examples of how to create an access grant by using the AWS
  SDKs.

Java
To use the following example, replace the `user input
 placeholders` with your own
information:

###### Note

If you are creating an access grant that grants access to only one object, include the
required parameter
`.s3PrefixType(S3PrefixType.Object)`.

###### Example Create an access grant request

```
public void createAccessGrant() {
CreateAccessGrantRequest createRequest = CreateAccessGrantRequest.builder()
.accountId("`111122223333`")
.accessGrantsLocationId("`a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa`")
.permission("`READ`")
.accessGrantsLocationConfiguration(AccessGrantsLocationConfiguration.builder().s3SubPrefix("`prefixB*`").build())
.grantee(Grantee.builder().granteeType("`IAM`").granteeIdentifier("arn:aws:iam::`111122223333`:user/`data-consumer-3`").build())
.build();
CreateAccessGrantResponse createResponse = s3Control.createAccessGrant(createRequest);
LOGGER.info("CreateAccessGrantResponse: " + createResponse);
}

```

###### Example Create an access grant response

```
CreateAccessGrantResponse(
CreatedAt=2023-06-07T05:20:26.330Z,
AccessGrantId=a1b2c3d4-5678-90ab-cdef-EXAMPLE33333,
AccessGrantArn=arn:aws:s3:`us-east-2`:`444455556666`:access-grants/default/grant/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333,
Grantee=Grantee(
GranteeType=IAM,
GranteeIdentifier=arn:aws:iam::`111122223333`:user/data-consumer-3
),
AccessGrantsLocationId=a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa,
AccessGrantsLocationConfiguration=AccessGrantsLocationConfiguration(
S3SubPrefix=prefixB*
),
GrantScope=s3://amzn-s3-demo-bucket/prefixB,
Permission=READ
)

```
