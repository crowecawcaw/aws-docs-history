# View a grant

You can view the details of an access grant in your Amazon S3 Access Grants instance by using the Amazon S3
console, the AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, and the AWS SDKs.

###### To view the details of an access grant

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose
   **Access Grants**.
3. On the **S3 Access Grants** page, choose the Region that contains
   the S3 Access Grants instance that you want to work with.
4. Choose **View details** for the instance.
5. On the details page, choose the **Grants** tab.
6. In the **Grants** section, find the access grant that you
   want to view. To filter the list of grants, use the search box.
   To install the AWS CLI, see [Installing the
   AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

To use the following example commands, replace the `user input
 placeholders` with your own information.

###### Example– Get the details of an access grant

```
aws s3control get-access-grant \
--account-id `111122223333` \
--access-grant-id `a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`
```

Response:

```
{
    "CreatedAt": "`2023-05-31T18:41:34.663000+00:00`",
    "AccessGrantId": "`a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`",
    "AccessGrantArn": "arn:aws:s3:`us-east-2`:`111122223333`:access-grants/default/grant-`a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`",
    "Grantee": {
        "GranteeType": "`IAM`",
        "GranteeIdentifier": "arn:aws:iam::`111122223333`:user/`data-consumer-3`"
    },
    "Permission": "`READ`",
    "AccessGrantsLocationId": "`12a6710f-5af8-41f5-b035-0bc795bf1a2b`",
    "AccessGrantsLocationConfiguration": {
        "S3SubPrefix": "`prefixB*`"
    },
    "GrantScope": "s3://`amzn-s3-demo-bucket`/"
}
```

###### Example– List all of the access grants in an S3 Access Grants instance

You can optionally use the following parameters to restrict the results to an
S3 prefix or AWS Identity and Access Management (IAM) identity:

- **Subprefix** –
  `--grant-scope
s3://`bucket-name/prefix\*``
- **IAM identity** –
  `--grantee-type IAM` and `--grantee-identifier
arn:aws:iam::`123456789000`:role/`accessGrantsConsumerRole``

```
aws s3control list-access-grants \
--account-id `111122223333`
```

Response:

```
{
    "AccessGrantsList": [{"CreatedAt": "`2023-06-14T17:54:46.542000+00:00`",
            "AccessGrantId": "`dd8dd089-b224-4d82-95f6-975b4185bbaa`",
            "AccessGrantArn": "arn:aws:s3:`us-east-2`:`111122223333`:access-grants/default/grant/`dd8dd089-b224-4d82-95f6-975b4185bbaa`",
            "Grantee": {
                "GranteeType": "`IAM`",
                "GranteeIdentifier": "arn:aws:iam::`111122223333`:user/`data-consumer-3`"
            },
            "Permission": "`READ`",
            "AccessGrantsLocationId": "`23514a34-ea2e-4ddf-b425-d0d4bfcarda1`",
            "GrantScope": "s3://`amzn-s3-demo-bucket`/`prefixA*`"
        },
        {"CreatedAt": "`2023-06-24T17:54:46.542000+00:00`",
            "AccessGrantId": "`ee8ee089-b224-4d72-85f6-975b4185a1b2`",
            "AccessGrantArn": "arn:aws:s3:`us-east-2`:`111122223333`:access-grants/default/grant/`ee8ee089-b224-4d72-85f6-975b4185a1b2`",
            "Grantee": {
                "GranteeType": "`IAM`",
                "GranteeIdentifier": "arn:aws:iam::`111122223333`:user/`data-consumer-9`"
            },
            "Permission": "`READ`",
            "AccessGrantsLocationId": "`12414a34-ea2e-4ddf-b425-d0d4bfcacao0`",
            "GrantScope": "s3://`amzn-s3-demo-bucket/prefixB*`"
        },

    ]
}
```

You can use Amazon S3 API operations to view the details of an access grant and list all access
grants in an S3 Access Grants instance. For information about the REST API support for
managing access grants, see the following sections in the
_Amazon Simple Storage Service API Reference_:

- [GetAccessGrant](../API/API_control_GetAccessGrant.md "../API/API_control_GetAccessGrant.md")
- [ListAccessGrants](../API/API_control_ListAccessGrants.md "../API/API_control_ListAccessGrants.md")
  This section provides examples of how to get the details of an access grant by
  using the AWS SDKs.

To use the following examples, replace the `user input
 placeholders` with your own information.

Java

###### Example– Get the details of an access grant

```
public void getAccessGrant() {
GetAccessGrantRequest getRequest = GetAccessGrantRequest.builder()
.accountId("`111122223333`")
.accessGrantId("`a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`")
.build();
GetAccessGrantResponse getResponse = s3Control.getAccessGrant(getRequest);
LOGGER.info("GetAccessGrantResponse: " + getResponse);
}
```

Response:

```
GetAccessGrantResponse(
CreatedAt=`2023-06-07T05:20:26.330Z`,
AccessGrantId=`a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`,
AccessGrantArn=arn:aws:s3:`us-east-2`:`111122223333`:access-grants/default/grant-`fd3a5086-42f7-4b34-9fad-472e2942c70e`,
Grantee=Grantee(
GranteeType=`IAM`,
GranteeIdentifier=arn:aws:iam::`111122223333`:user/`data-consumer-3`
),
Permission=`READ`,
AccessGrantsLocationId=`12a6710f-5af8-41f5-b035-0bc795bf1a2b`,
AccessGrantsLocationConfiguration=AccessGrantsLocationConfiguration(
S3SubPrefix=`prefixB*`
),
GrantScope=s3://`amzn-s3-demo-bucket/`
)

```

###### Example– List all of the access grants in an S3 Access Grants instance

You can optionally use these parameters to restrict the results to
an S3 prefix or IAM identity:

- **Scope** –
  `GrantScope=s3://`bucket-name/prefix\*``
- **Grantee** –
  `GranteeType=IAM` and
  `GranteeIdentifier=
arn:aws:iam::``111122223333``:role/`accessGrantsConsumerRole``

```
public void listAccessGrants() {
ListAccessGrantsRequest listRequest = ListAccessGrantsRequest.builder()
.accountId("`111122223333`")
.build();
ListAccessGrantsResponse listResponse = s3Control.listAccessGrants(listRequest);
LOGGER.info("ListAccessGrantsResponse: " + listResponse);
}


```

Response:

```
ListAccessGrantsResponse(
AccessGrantsList=[
ListAccessGrantEntry(
CreatedAt=`2023-06-14T17:54:46.540z`,
AccessGrantId=`dd8dd089-b224-4d82-95f6-975b4185bbaa`,
AccessGrantArn=arn:aws:s3:`us-east-2`:`111122223333`:access-grants/default/grant/`dd8dd089-b224-4d82-95f6-975b4185bbaa`,
Grantee=Grantee(
GranteeType=`IAM`, GranteeIdentifier= arn:aws:iam::`111122223333`:user/`data-consumer-3`
),
Permission=`READ`,
AccessGrantsLocationId=`23514a34-ea2e-4ddf-b425-d0d4bfcarda1`,
GrantScope=s3://`amzn-s3-demo-bucket/prefixA`
),
ListAccessGrantEntry(
CreatedAt=`2023-06-24T17:54:46.540Z`,
AccessGrantId=`ee8ee089-b224-4d72-85f6-975b4185a1b2`,
AccessGrantArn=arn:aws:s3:`us-east-2`:`111122223333`:access-grants/default/grant/`ee8ee089-b224-4d72-85f6-975b4185a1b2`,
Grantee=Grantee(
GranteeType=`IAM`, GranteeIdentifier= arn:aws:iam::`111122223333`:user/`data-consumer-9`
),
Permission=`READ`,
AccessGrantsLocationId=`12414a34-ea2e-4ddf-b425-d0d4bfcacao0`,
GrantScope=s3://`amzn-s3-demo-bucket/prefixB*`
)
]
)

```
