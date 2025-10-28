# Create an S3 Access Grants instance

To get started with using AmazonS3 Access Grants, you first create an S3 Access Grants instance. You can create
only one S3 Access Grants instance per AWS Region per account. The S3 Access Grants instance serves as the container
for your S3 Access Grants resources, which include registered locations and grants.

With S3 Access Grants, you can create permission grants to your S3 data for AWS Identity and Access Management (IAM) users and
roles. If you've [added your
corporate identity directory](../../../singlesignon/latest/userguide/manage-your-identity-source-idp.md "../../../singlesignon/latest/userguide/manage-your-identity-source-idp.md") to AWS IAM Identity Center, you can associate this IAM Identity Center instance
of your corporate directory with your S3 Access Grants instance. After you've done so, you can create
access grants for your corporate users and groups. If you haven't yet added your corporate
directory to IAM Identity Center, you can associate your S3 Access Grants instance with an IAM Identity Center instance later.

You can create an S3 Access Grants instance by using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, and AWS SDKs.

Before you can grant access to your S3 data with S3 Access Grants, you must first create an
S3 Access Grants instance in the same AWS Region as your S3 data.

###### Prerequisites

If you want to grant access to your S3 data by using identities from your
corporate directory, [add
your corporate identity directory](../../../singlesignon/latest/userguide/manage-your-identity-source-idp.md "../../../singlesignon/latest/userguide/manage-your-identity-source-idp.md") to AWS IAM Identity Center. If you're not yet
ready to do so, you can associate your S3 Access Grants instance with an IAM Identity Center instance
later.

###### To create an S3 Access Grants instance

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation bar, choose the name of the currently displayed AWS Region. Next, choose the Region that you want to switch to.
3. In the left navigation pane, choose **Access
   Grants**.
4. On the **S3 Access Grants** page, choose **Create
   S3 Access Grants instance**.
   1. In **Step 1** of the **Set up
      Access Grants instance** wizard, verify that you want to
      create the instance in the current AWS Region. Make sure that this is
      the same AWS Region where your S3 data is located. You can create one
      S3 Access Grants instance per AWS Region per account.
   2. (Optional) If you've [added your corporate identity directory](../../../singlesignon/latest/userguide/manage-your-identity-source-idp.md "../../../singlesignon/latest/userguide/manage-your-identity-source-idp.md") to AWS IAM Identity Center,
      you can associate this IAM Identity Center instance of your corporate directory
      with your S3 Access Grants instance.

   To do so, select **Add IAM Identity Center instance in
   `region`**. Then enter the
   IAM Identity Center instance Amazon Resource Name (ARN).

   If you haven't yet added your corporate directory to IAM Identity Center, you
   can associate your S3 Access Grants instance with an IAM Identity Center instance later. 3. To create the S3 Access Grants instance, choose **Next**.
   To register a location, see [Step
   2 - register a location](access-grants-instance.md "access-grants-instance.md").

5. If **Next** or **Create S3 Access Grants
   instance** is disabled:

###### Cannot create instance

    * You might already have an S3 Access Grants instance in the same
     AWS Region. In the left navigation pane, choose **Access
     Grants**. On the **S3 Access Grants** page,
     scroll down to the **S3 Access Grants instance in your
     account** section o determine if an instance already
     exists.
    * You might not have the `s3:CreateAccessGrantsInstance`
     permission which is required to create an S3 Access Grants instance. Contact
     your account administrator. For additional permissions that are
     required if you are associating an IAM Identity Center instance, with your S3 Access Grants
     instance, see [CreateAccessGrantsInstance](../API/API_control_CreateAccessGrantsInstance.md "../API/API_control_CreateAccessGrantsInstance.md") .

To install the AWS CLI, see [Installing the
AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

To use the following example command, replace the `user input
 placeholders` with your own information.

###### Example Create an S3 Access Grants instance

```
aws s3control create-access-grants-instance \
--account-id `111122223333` \
--region `us-east-2`

```

Response:

```
{
    "CreatedAt": "2023-05-31T17:54:07.893000+00:00",
    "AccessGrantsInstanceId": "default",
    "AccessGrantsInstanceArn": "arn:aws:s3:`us-east-2`:`111122223333`:access-grants/default"
}
```

You can use the Amazon S3 REST API to create an S3 Access Grants instance. For information on the REST
API support for managing an S3 Access Grants instance, see the following sections in the
_Amazon Simple Storage Service API Reference_:

- [AssociateAccessGrantsIdentityCenter](../API/API_control_AssociateAccessGrantsIdentityCenter.md "../API/API_control_AssociateAccessGrantsIdentityCenter.md")
- [CreateAccessGrantsInstance](../API/API_control_CreateAccessGrantsInstance.md "../API/API_control_CreateAccessGrantsInstance.md")
- [DeleteAccessGrantsInstance](../API/API_control_DeleteAccessGrantsInstance.md "../API/API_control_DeleteAccessGrantsInstance.md")
- [DissociateAccessGrantsIdentityCenter](../API/API_control_DissociateAccessGrantsIdentityCenter.md "../API/API_control_DissociateAccessGrantsIdentityCenter.md")
- [GetAccessGrantsInstance](../API/API_control_GetAccessGrantsInstance.md "../API/API_control_GetAccessGrantsInstance.md")
- [GetAccessGrantsInstanceForPrefix](../API/API_control_GetAccessGrantsInstanceForPrefix.md "../API/API_control_GetAccessGrantsInstanceForPrefix.md")
- [GetAccessGrantsInstanceResourcePolicy](../API/API_control_GetAccessGrantsInstanceResourcePolicy.md "../API/API_control_GetAccessGrantsInstanceResourcePolicy.md")
- [ListAccessGrantsInstances](../API/API_control_ListAccessGrantsInstances.md "../API/API_control_ListAccessGrantsInstances.md")
- [PutAccessGrantsInstanceResourcePolicy](../API/API_control_PutAccessGrantsInstanceResourcePolicy.md "../API/API_control_PutAccessGrantsInstanceResourcePolicy.md")
  This section provides an example of how to create an S3 Access Grants instance by using the AWS
  SDKs.

Java
This example creates the S3 Access Grants instance, which serves as a container for your
individual access grants. You can have one S3 Access Grants instance per AWS Region in
your account. The response includes the instance ID `default`
and an Amazon Resource Name (ARN) that's generated for your S3 Access
Grants instance.

###### Example Create an S3 Access Grants instance request

```
public void createAccessGrantsInstance() {
CreateAccessGrantsInstanceRequest createRequest = CreateAccessGrantsInstanceRequest.builder().accountId("`111122223333`").build();
CreateAccessGrantsInstanceResponse createResponse = s3Control.createAccessGrantsInstance(createRequest);LOGGER.info("CreateAccessGrantsInstanceResponse: " + createResponse);
}
```

Response:

```
CreateAccessGrantsInstanceResponse(
CreatedAt=2023-06-07T01:46:20.507Z,
AccessGrantsInstanceId=default,
AccessGrantsInstanceArn=arn:aws:s3:`us-east-2`:`111122223333`:access-grants/default)
```
