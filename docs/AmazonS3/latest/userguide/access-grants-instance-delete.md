# Delete an S3 Access Grants instance

You can delete an Amazon S3 Access Grants instance from an AWS Region in your account. However,
before you can delete an S3 Access Grants instance, you must first do the following:

- Delete all resources within the S3 Access Grants instance, including all grants and
  locations. For more information, see [Delete a
  grant](access-grants-grant-delete.md "access-grants-grant-delete.md") and [Delete a
  location](access-grants-grant-location.md "access-grants-grant-location.md").
- If you've associated an AWS IAM Identity Center instance with your S3 Access Grants instance, you must
  disassociate the IAM Identity Center instance. For more information, see [Associate or
  disassociate your IAM Identity Center instance](access-grants-instance-idc.md "access-grants-instance-idc.md").

###### Important

If you delete an S3 Access Grants instance, the deletion is permanent and can't be undone. All
grantees that were given access through the grants in this S3 Access Grants instance will lose
access to your S3 data.

You can delete an S3 Access Grants instance by using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), the Amazon S3
REST API, and the AWS SDKs.

###### To delete an S3 Access Grants instance

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose
   **Access Grants**.
3. On the **S3 Access Grants** page, choose the Region that contains
   the S3 Access Grants instance that you want to work with.
4. Choose **View details** for the instance.
5. On the instance details page, choose **Delete instance**
   in the upper-right corner.
6. In the dialog box that appears, choose **Delete**. This
   action can't be undone.
   To install the AWS CLI, see [Installing the
   AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

To use the following example command, replace the `user input
 placeholders` with your own information.

###### Note

Before you can delete an S3 Access Grants instance, you must first delete all grants and
locations created within the S3 Access Grants instance. If you have associated an IAM Identity Center
center instance with your S3 Access Grants instance, you must disassociate it
first.

###### Example– Delete an S3 Access Grants instance

```
aws s3control delete-access-grants-instance \
--account-id `111122223333` \
--profile `access-grants-profile` \
--region `us-east-2` \
--endpoint-url https://s3-control.`us-east-2`.amazonaws.com \

 // No response body
```

For information about the Amazon S3 REST API support for deleting an S3 Access Grants instance,
see [DeleteAccessGrantsInstance](../API/API_control_DeleteAccessGrantsInstance.md "../API/API_control_DeleteAccessGrantsInstance.md") in the
_Amazon Simple Storage Service API Reference_.

This section provides examples of how to delete an S3 Access Grants instance by using the
AWS SDKs.

To use the following example, replace the `user input
 placeholders` with your own information.

Java

###### Note

Before you can delete an S3 Access Grants instance, you must first delete
all grants and locations created within the S3 Access Grants instance. If you
have associated an IAM Identity Center center instance with your S3 Access Grants instance,
you must disassociate it first.

###### Example– Delete an S3 Access Grants instance

```
public void deleteAccessGrantsInstance() {
DeleteAccessGrantsInstanceRequest deleteRequest = DeleteAccessGrantsInstanceRequest.builder()
.accountId("`111122223333`")
.build();
DeleteAccessGrantsInstanceResponse deleteResponse = s3Control.deleteAccessGrantsInstance(deleteRequest);
LOGGER.info("DeleteAccessGrantsInstanceResponse: " + deleteResponse);
}
```
