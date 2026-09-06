

# Delete your access point for a general purpose bucket
<a name="access-points-delete"></a>

This section explains how to delete your access point for a general purpose bucket using the AWS Management Console, AWS Command Line Interface, or REST API.

## Using the S3 console
<a name="access-points-delete-console"></a>

**To delete for your access points in your AWS account**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the navigation bar on the top of the page, choose the name of the currently displayed AWS Region. Next, choose the Region that you want to list access points for. 

1. In the navigation pane on the left side of the console, choose **Access Points**.

1. (Optional) Search for access points by name. Only access points in your selected AWS Region will appear here.

1. Choose the name of the access point you want to manage or use.

1. From the **Access Point** page, select **Delete** to delete the access point you've selected.

1. To confirm deletion, type the name of the access point and choose **Delete**.

## Using the AWS CLI
<a name="access-points-delete-cli"></a>

The following `delete-access-point` example command shows how you can use the AWS CLI to delete your access point.

The following command deletes the access point {{my-access-point}} for AWS account {{111122223333}}.

```
aws s3control delete-access-point --name {{my-access-point}} --account-id {{111122223333}}      
```

For more information and examples, see [delete-access-point](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/delete-access-point.html) in the *AWS CLI Command Reference*.

## Using the REST API
<a name="access-points-delete-rest"></a>

You can use the REST API to view details for your access point. For more information, see [DeleteAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPoint.html) in the *Amazon Simple Storage Service API Reference*.