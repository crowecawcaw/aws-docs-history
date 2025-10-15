# List your access points for general purpose buckets

This section explains how to list your access points for general purpose buckets using the AWS Management Console, AWS Command Line Interface, or REST API.

###### To list access points in your AWS account

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation bar on the top of the page, choose the name of the
 currently displayed AWS Region. Next, choose the Region that you want to
 list access points for.
3. In the navigation pane on the left side of the console, choose
 **Access Points**.
4. (Optional) Search for access points by name. Only access points in your selected AWS Region will appear here.
5. Choose the name of the access point you want to manage or use.
The following `list-access-points` example command shows how you can use
 the AWS CLI to list your access points.

The following command lists access points for AWS account `111122223333`.


```
aws s3control list-access-points --account-id `111122223333`      
```
The following command lists access points for AWS account `111122223333` that are attached to bucket `amzn-s3-demo-bucket`.


```
aws s3control list-access-points --account-id `111122223333` --bucket `amzn-s3-demo-bucket`     
```
For more information and examples, see [list-access-points](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/list-access-points.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/list-access-points.html") in the
 *AWS CLI Command Reference*.

You can use the REST API to list your access points. For more information, see [ListAccessPoints](../API/API_control_ListAccessPoints.md "../API/API_control_ListAccessPoints.md") in the *Amazon Simple Storage Service API Reference*.
