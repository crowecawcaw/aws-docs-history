# Example: Run additional scripts for AWS PCS from an S3 bucket

Provide this script as the value of `"userData"` in your launch template. For more information, see [Working with Amazon EC2 user data for AWS PCS](working-with_ec2-user-data.md "working-with_ec2-user-data.md").

The following user data script uses **cloud-config** to import a script from an S3 bucket and
run it on node group instances at launch.
For more information, see the [User data formats](https://cloudinit.readthedocs.io/en/latest/explanation/format.html "https://cloudinit.readthedocs.io/en/latest/explanation/format.html")
in the _cloud-init documentation_.

Replace the following values with your own details:

- `amzn-s3-demo-bucket` – The name of an S3 bucket your account can read from.
- `object-key` – The S3 object key of the script to import. This includes the name of the script
  and its location in the folder structure of the bucket. For example, `scripts/script.sh`.
  For more information, see [Organizing
  objects in the Amazon S3 console by using folders](../../../AmazonS3/latest/userguide/using-folders.md "../../../AmazonS3/latest/userguide/using-folders.md") in the _Amazon Simple Storage Service User Guide_.
- `shell` – The Linux shell to use to run the script, such as `bash`.

```
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="==MYBOUNDARY=="

--==MYBOUNDARY==
Content-Type: text/cloud-config; charset="us-ascii"

runcmd:
- aws s3 cp s3://`amzn-s3-demo-bucket`/`object-key` /tmp/script.sh
- /usr/bin/`shell` /tmp/script.sh

--==MYBOUNDARY==--
```

The IAM instance profile for the node group must have access to the bucket. The following IAM policy is an example
for the bucket in the user data script above.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ]
 }
 ]
}`

```
