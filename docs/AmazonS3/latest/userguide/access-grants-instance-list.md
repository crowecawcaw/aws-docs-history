# List your S3 Access Grants instances

You can list your S3 Access Grants instances, including the instances that have been shared with you
through AWS Resource Access Manager (AWS RAM).

You can list your S3 Access Grants instances by using the
Amazon S3 console, the AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, and the AWS SDKs.

###### To list your S3 Access Grants instances

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose
   **Access Grants**.
3. On the **S3 Access Grants** page, choose the Region that contains
   the S3 Access Grants instance that you want to work with.
4. The **S3 Access Grants** page lists your S3 Access Grants instances
   and any cross-account instances that have been shared with your account. To
   view the details of an instance, choose **View details**.
   To install the AWS CLI, see [Installing the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

To use the following example command, replace the `user input
 placeholders` with your own information.

###### Example – List all S3 Access Grants instances for an account

This action lists the S3 Access Grants instances for an account. You can only have one S3 Access Grants
instance per AWS Region. This action also lists other cross-account S3 Access Grants
instances that your account has access to.

```
aws s3control list-access-grants-instances \
 --account-id `111122223333` \
 --region `us-east-2`
```

Response:

```
{
    "AccessGrantsInstanceArn": "arn:aws:s3:`us-east-2`: `111122223333`:access-grants/default",
    "AccessGrantsInstanceId": "default",
    "CreatedAt": "`2023-05-31T17:54:07.893000+00:00`"
}
```

For information about the Amazon S3 REST API support for managing an S3 Access Grants instance, see the
following sections in the _Amazon Simple Storage Service API Reference_:

- [ListAccessGrantsInstances](../API/API_control_ListAccessGrantsInstances.md "../API/API_control_ListAccessGrantsInstances.md")
  This section provides examples of how to get the details of an S3 Access Grants instance by
  using the AWS SDKs.

To use the following examples, replace the `user input
 placeholders` with your own information.

Java

###### Example – List all S3 Access Grants instances for an account

This action lists the S3 Access Grants instances for an account. You can
only have one S3 Access Grants instance per Region. This action can also list
other cross-account S3 Access Grants instances that your account has access
to.

```
public void listAccessGrantsInstances() {
ListAccessGrantsInstancesRequest listRequest = ListAccessGrantsInstancesRequest.builder()
.accountId("`111122223333`")
.build();
ListAccessGrantsInstancesResponse listResponse = s3Control.listAccessGrantsInstances(listRequest);
LOGGER.info("ListAccessGrantsInstancesResponse: " + listResponse);
}
```

Response:

```
ListAccessGrantsInstancesResponse(
AccessGrantsInstancesList=[
ListAccessGrantsInstanceEntry(
AccessGrantsInstanceId=default,
AccessGrantsInstanceArn=arn:aws:s3:`us-east-2`:`111122223333`:access-grants/default,
CreatedAt=`2023-06-07T04:28:11.728Z`
)
]
)
```
