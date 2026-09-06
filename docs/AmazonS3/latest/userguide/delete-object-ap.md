

# Delete an object through an access point for a general purpose bucket
<a name="delete-object-ap"></a>

This section explains how to delete an object through an access point for a general purpose bucket using the AWS Management Console, AWS Command Line Interface, or REST API.

## Using the S3 console
<a name="delete-object-ap-console"></a>

**To delete an object or objects through an access point in your AWS account**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the navigation bar on the top of the page, choose the name of the currently displayed AWS Region. Next, choose the Region that you want to list access points for. 

1. In the navigation pane on the left side of the console, choose **Access Points**.

1. (Optional) Search for access points by name. Only access points in your selected AWS Region will appear here.

1. Choose the name of the access point you want to manage or use.

1. Under the **Objects** tab, select the name of the object or objects you wish to delete.

1. Review the objects listed for deletion, and type *delete* in the confirmation box.

1. Choose **Delete objects**.

## Using the AWS CLI
<a name="delete-object-ap-cli"></a>

The following `delete-object` example command shows how you can use the AWS CLI to delete an object through an access point.

The following command deletes the existing object `puppy.jpg` using access point {{my-access-point}}.

```
aws s3api delete-object --bucket arn:aws:s3:{{AWS Region}}:111122223333:accesspoint/{{my-access-point}} --key {{puppy.jpg}}      
```

**Note**  
S3 automatically generate access point aliases for all access points and access point aliases can be used anywhere a bucket name is used to perform object-level operations. For more information, see [Access point aliases](access-points-naming.md#access-points-alias).

For more information and examples, see [delete-object](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-object.html) in the *AWS CLI Command Reference*.

## Using the REST API
<a name="delete-object-ap-rest"></a>

You can use the REST API to delete an object through an access point. For more information, see [DeleteObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html) in the *Amazon Simple Storage Service API Reference*.