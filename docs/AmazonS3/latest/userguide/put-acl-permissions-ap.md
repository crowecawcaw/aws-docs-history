# Configure access control lists (ACLs) through an access point for a general purpose bucket

This section explains how to configure ACLs through an access point for a general purpose bucket using the AWS Management Console,
 AWS Command Line Interface, or REST API. For more information about ACLs, see [Access control list (ACL) overview](acl-overview.md "acl-overview.md"). 

###### To configure ACLs through an access point in your AWS account

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation bar on the top of the page, choose the name of the
 currently displayed AWS Region. Next, choose the Region that you want to
 list access points for.
3. In the navigation pane on the left side of the console, choose
 **Access Points**.
4. (Optional) Search for access points by name. Only access points in your selected AWS Region will appear here.
5. Choose the name of the access point you want to manage or use.
6. Under the **Objects** tab, select the name of
 the object you wish to configure an ACL for.
7. Under the **Permissions** tab, select
 **Edit** to configure the object ACL.


###### Note

Amazon S3 currently doesn't support changing an access point's block public
 access settings after the access point has been created.
The following `put-object-acl` example command shows how you can
 use the AWS CLI to configure access permissions through an access point using an ACL.

The following command applies an ACL to an existing object `puppy.jpg` through an access point owned by AWS account
 `111122223333`.


```
aws s3api put-object-acl --bucket arn:aws:s3:`AWS Region`:111122223333:accesspoint/`my-access-point` --key puppy.jpg --acl private      
```
###### Note

S3 automatically generate access point aliases for all access points and these aliases can be used
 anywhere a bucket name is used to perform object-level operations. For more
 information, see [Access point aliases](access-points-naming.md#access-points-alias "access-points-naming.md#access-points-alias").

For more information and examples, see [put-object-acl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object-acl.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object-acl.html") in the
 *AWS CLI Command Reference*.

You can use the REST API to configure access permissions through an access point using an ACL. For more information, see [PutObjectAcl](../API/API_PutObjectAcl.md "../API/API_PutObjectAcl.md") in the *Amazon Simple Storage Service API Reference*.
