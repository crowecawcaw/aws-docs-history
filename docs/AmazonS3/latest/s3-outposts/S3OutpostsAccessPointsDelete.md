# Deleting an access point

Access points simplify managing data access at
scale for shared datasets in Amazon S3. Access points are named network endpoints that are
attached to buckets that you can use to perform Amazon S3 object operations, such as
`GetObject` and `PutObject`. With S3 on Outposts, you must use access points to access any object in an Outposts bucket. Access
points support only virtual-host-style addressing.

The following examples show you how to delete an access point by using the AWS Management Console and the
AWS Command Line Interface (AWS CLI).

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Outposts
   access points**.
3. In the **Outposts access points** section, choose the Outposts access point
   that you want to delete.
4. Choose **Delete**.
5. Confirm the deletion.
   The following AWS CLI example deletes an Outposts access point. To run this command,
   replace the `user input placeholders` with
   your own information.

```
aws s3control delete-access-point --account-id `123456789012` --name arn:aws:s3-outposts:`region`:`123456789012`:outpost/`op-01ac5d28a6a232904`/accesspoint/`example-outposts-access-point`
```
