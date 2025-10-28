# List objects through an access point for a general purpose bucket

This section explains how to list your objects through an access point for a general purpose bucket using the AWS Management Console,
AWS Command Line Interface, or REST API.

###### To list your objects through an access point in your AWS account

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation bar on the top of the page, choose the name of the
   currently displayed AWS Region. Next, choose the Region that you want to
   list access points for.
3. In the navigation pane on the left side of the console, choose
   **Access Points**.
4. (Optional) Search for access points by name. Only access points in your selected AWS Region will appear here.
5. Choose the name of the access point you want to manage or use.
6. Under the **Objects** tab, you can view the name of
   objects that you want to access through the access point. While you're using the
   access point, you can only perform the object operations that are allowed by the
   access point permissions.

###### Note

    * The console view always shows all objects in the bucket. Using an
     access point as described in this procedure restricts the operations
     you can perform on those objects, but not whether you can see that
     they exist in the bucket.
    * The AWS Management Console doesn't support using virtual private
     cloud (VPC) access points to access bucket resources. To access
     bucket resources from a VPC access point, use the AWS CLI, AWS SDKs,
     or Amazon S3 REST APIs.

The following `list-objects-v2` example command shows how you can
use the AWS CLI to list your object through an access point.

The following command lists objects for AWS account
`111122223333` using access point
`my-access-point`.

```
aws s3api list-objects-v2 --bucket arn:aws:s3:`AWS Region`:111122223333:accesspoint/`my-access-point`
```

###### Note

S3 automatically generate access point aliases for all access points and these aliases can be used
anywhere a bucket name is used to perform object-level operations. For more
information, see [Access point aliases](access-points-naming.md#access-points-alias "access-points-naming.md#access-points-alias").

For more information and examples, see [list-access-points](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-objects-v2.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-objects-v2.html") in the
_AWS CLI Command Reference_.

You can use the REST API to list your access points. For more information, see [ListObjectsV2](../API/API_ListObjectsV2.md "../API/API_ListObjectsV2.md") in the _Amazon Simple Storage Service API Reference_.
