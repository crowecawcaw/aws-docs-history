# Delete your access point for a general purpose bucket

This section explains how to delete your access point for a general purpose bucket using the AWS Management Console, AWS Command Line Interface, or REST API.

###### To delete for your access points in your AWS account

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation bar on the top of the page, choose the name of the
   currently displayed AWS Region. Next, choose the Region that you want to
   list access points for.
3. In the navigation pane on the left side of the console, choose
   **Access Points**.
4. (Optional) Search for access points by name. Only access points in your selected AWS Region will appear here.
5. Choose the name of the access point you want to manage or use.
6. From the **Access Point** page, select **Delete** to delete the access point you've selected.
7. To confirm deletion, type the name of the access point and choose **Delete**.
   The following `delete-access-point` example command shows how you can use
   the AWS CLI to delete your access point.

The following command deletes the access point `my-access-point` for AWS account `111122223333`.

```
aws s3control delete-access-point --name `my-access-point` --account-id `111122223333`
```

For more information and examples, see [delete-access-point](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/delete-access-point.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/delete-access-point.html") in the
_AWS CLI Command Reference_.

You can use the REST API to view details for your access point. For more information, see [DeleteAccessPoint](../API/API_control_DeleteAccessPoint.md "../API/API_control_DeleteAccessPoint.md") in the _Amazon Simple Storage Service API Reference_.
