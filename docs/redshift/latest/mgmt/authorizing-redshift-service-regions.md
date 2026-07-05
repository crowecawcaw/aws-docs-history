Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Restricting an IAM role to an AWS Region

You can restrict an IAM role to only be accessible in a certain AWS Region. By
default, IAM roles for Amazon Redshift are not restricted to any single region.

To restrict use of an IAM role by region, take the following steps.

###### To identify permitted regions for an IAM role

1. Open the [IAM console](https://console.aws.amazon.com/iam/home?#home "https://console.aws.amazon.com/iam/home?#home")
   at [https://console.aws.amazon.com/](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").
2. In the navigation pane, choose **Roles**.
3. Choose the role that you want to modify with specific regions.
4. Choose the **Trust Relationships** tab and then choose
   **Edit Trust Relationship**. A new IAM role that allows
   Amazon Redshift to access other AWS services on your behalf has a trust relationship as
   follows:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "redshift.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

5. Modify the `Service` list for the `Principal` with the
   list of the specific regions that you want to permit use of the role for. Each
   region in the `Service` list must be in the following format:
   `redshift.`region`.amazonaws.com`.

For example, the following edited trust relationship permits the use of the
IAM role in the `us-east-1` and `us-west-2` regions
only.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "redshift.us-east-1.amazonaws.com",
 "redshift.us-west-2.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

6. Choose **Update Trust Policy**
