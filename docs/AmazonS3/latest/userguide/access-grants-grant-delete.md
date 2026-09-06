

# Delete a grant
<a name="access-grants-grant-delete"></a>

You can delete access grants from your Amazon S3 Access Grants instance. You can't undo an access grant deletion. After you delete an access grant, the grantee will no longer have access to your Amazon S3 data.

You can delete an access grant by using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, and the AWS SDKs.

## Using the S3 console
<a name="access-grants-grant-delete-console"></a>

**To delete an access grant**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the left navigation pane, choose **Access Grants**.

1. On the **S3 Access Grants** page, choose the Region that contains the S3 Access Grants instance that you want to work with.

1. Choose **View details** for the instance.

1. On the details page, choose the **Grants** tab. 

1. Search for the grant that you want to delete. When you locate the grant, choose the radio button next to it. 

1. Choose **Delete**. A dialog box appears with a warning that your action can't be undone. Choose **Delete** again to delete the grant. 

## Using the AWS CLI
<a name="access-grants-grant-delete-cli"></a>

To install the AWS CLI, see [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*. 

To use the following example command, replace the `{{user input placeholders}}` with your own information.

**Example – Delete an access grant**  

```
aws s3control delete-access-grant \
--account-id {{111122223333}} \
--access-grant-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} 

// No response body
```

## Using the REST API
<a name="access-grants-grant-delete-rest-api"></a>

For information about the Amazon S3 REST API support for managing access grants, see [DeleteAccessGrant](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessGrant.html) in the *Amazon Simple Storage Service API Reference*.

## Using the AWS SDKs
<a name="access-grants-grant-delete-using-sdk"></a>

This section provides examples of how to delete an access grant by using the AWS SDKs. To use the following example, replace the `{{user input placeholders}}` with your own information.

------
#### [ Java ]

**Example – Delete an access grant**  

```
public void deleteAccessGrant() {
DeleteAccessGrantRequest deleteRequest = DeleteAccessGrantRequest.builder()
.accountId("{{111122223333}}")
.accessGrantId("{{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}")
.build();
DeleteAccessGrantResponse deleteResponse = s3Control.deleteAccessGrant(deleteRequest);
LOGGER.info("DeleteAccessGrantResponse: " + deleteResponse);
}
```
Response:  

```
DeleteAccessGrantResponse()
```

------