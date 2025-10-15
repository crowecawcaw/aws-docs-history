# Deleting a Multi-Region Access Point

The following procedure explains how to delete a Multi-Region Access Point by using the Amazon S3
 console. Be aware that deleting a Multi-Region Access Point doesn't delete the buckets associated with the Multi-Region Access Point. Instead, it only deletes the
 Multi-Region Access Point itself.

###### Note

S3 Multi-Region Access Points using buckets in AWS opt-in Regions is currently only supported through
 AWS SDKs and the AWS CLI. To delete a Multi-Region Access Point using buckets in an opt-in Region,
 make sure to specify which AWS opt-in Regions your account can use first.
 Otherwise, if you try to delete a Multi-Region Access Point that uses buckets in disabled AWS opt-in
 Regions, you'll receive an error.

###### To delete a Multi-Region Access Point

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose
 **Multi-Region Access Points**.
3. Select the option button next to the name of your Multi-Region Access Point.
4. Choose **Delete**.
5. In the **Delete Multi-Region Access Point** dialog
 box, enter the name of the AWS bucket that you want to delete.


###### Note

Make sure to enter a valid bucket name. Otherwise, the
 **Delete** button will be disabled.
6. Choose **Delete** to confirm deletion of your
 Multi-Region Access Point.
You can use the AWS CLI to delete a Multi-Region Access Point. This action does not delete the
 buckets associated with the Multi-Region Access Point, only the Multi-Region Access Point itself. To use this example
 command, replace the ``user input
 placeholders`` with your own information.


```
aws s3control delete-multi-region-access-point --account-id `123456789012` --details Name=`example-multi-region-access-point-name`
```
