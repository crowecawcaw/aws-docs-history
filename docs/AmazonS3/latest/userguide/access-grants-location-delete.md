

# Delete a registered location
<a name="access-grants-location-delete"></a>

You can delete a location registration from an Amazon S3 Access Grants instance. Deleting the location deregisters it from the S3 Access Grants instance. 

Before you can remove a location registration from an S3 Access Grants instance, you must delete all of the grants that are associated with this location. For information about how to delete grants, see [Delete a grant](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-grant-delete.html). 

You can delete a location in your S3 Access Grants instance by using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, and the AWS SDKs.

## Using the S3 console
<a name="access-grants-location-delete-console"></a>

**To delete a location registration from your S3 Access Grants instance**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the left navigation pane, choose **Access Grants**.

1. On the **S3 Access Grants** page, choose the Region that contains the S3 Access Grants instance that you want to work with.

1. Choose **View details** for the instance.

1. On the details page for the instance, choose the **Locations** tab.

1. Find the location that you want to update. To filter the list of locations, use the search box.

1. Choose the option button next to the registered location that you want to delete.

1. Choose **Deregister**.

1. A dialog box appears that warns you that this action can't be undone. To delete the location, choose **Deregister**.

## Using the AWS CLI
<a name="access-grants-location-delete-cli"></a>

To install the AWS CLI, see [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*. 

To use the following example command, replace the `{{user input placeholders}}` with your own information.

**Example – Delete a location registration**  

```
aws s3control delete-access-grants-location \
--account-id {{111122223333}} \
--access-grants-location-id  {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} 
 // No response body
```

## Using the REST API
<a name="access-grants-location-delete-rest-api"></a>

For information about the Amazon S3 REST API support for deleting a location from an S3 Access Grants instance, see [DeleteAccessGrantsLocation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessGrantsLocation.html) in the *Amazon Simple Storage Service API Reference*.

## Using the AWS SDKs
<a name="access-grants-location-delete-using-sdk"></a>

This section provides an example of how to delete a location by using the AWS SDKs.

To use the following example, replace the `{{user input placeholders}}` with your own information.

------
#### [ Java ]

**Example – Delete a location registration**  

```
public void deleteAccessGrantsLocation() {
DeleteAccessGrantsLocationRequest deleteRequest = DeleteAccessGrantsLocationRequest.builder()
.accountId("{{111122223333}}")
.accessGrantsLocationId("{{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}")
.build();
DeleteAccessGrantsLocationResponse deleteResponse = s3Control.deleteAccessGrantsLocation(deleteRequest);
LOGGER.info("DeleteAccessGrantsLocationResponse: " + deleteResponse);
}
```
Response:  

```
DeleteAccessGrantsLocationResponse()
```

------