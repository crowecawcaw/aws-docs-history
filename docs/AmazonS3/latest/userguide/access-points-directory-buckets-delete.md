

# Delete your access point for directory buckets
<a name="access-points-directory-buckets-delete"></a>

This section explains how to delete your access point using the AWS Management Console, AWS Command Line Interface, REST API, or AWS SDKs.

**Note**  
Before you can delete a directory bucket attached to an access point, you must delete the access point.

## Using the S3 console
<a name="access-points-directory-buckets-delete-console"></a>

**To delete access points for directory buckets in your AWS account**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the navigation bar, choose the name of the currently displayed AWS Region. Next, choose the Region that you want to list access points for.

1. In the navigation pane on the left side of the console, choose **Access points for directory buckets**.

1. (Optional) Search for access points by name. Only access points in your selected AWS Region will appear here.

1. Choose the name of the access point you want to delete.

1. Choose **Delete**.

1. To confirm deletion, type **confirm** and choose **Delete**.

## Using the AWS CLI
<a name="access-points-directory-buckets-delete-cli"></a>

The following `delete-access-point` example command shows how you can use the AWS CLI to delete your access point.

The following command deletes the access point {{{{my-access-point}}}}--{{zoneID}}--xa-s3 for AWS account {{111122223333}}.

```
aws s3control delete-access-point --name {{{{my-access-point}}}}--{{zoneID}}--xa-s3 --account-id {{111122223333}}      
```

For more information and examples, see [delete-access-point](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/delete-access-point.html) in the *AWS CLI Command Reference*.

## Using the REST API
<a name="access-points-directory-buckets-delete-rest"></a>

You can use the REST API to delete your access point. For more information, see [DeleteAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPoint.html) in the *Amazon Simple Storage Service API Reference*.

## Using the AWS SDKs
<a name="access-points-directory-buckets-delete-sdk"></a>

You can use the AWS SDKs to delete your access points. For more information, see [list of supported SDKs](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPoint.html#API_control_DeleteAccessPoint_SeeAlso) in the Amazon Simple Storage Service API Reference.