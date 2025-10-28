# Checking for the

AmazonAppStreamServiceAccess Service Role and Policies

Complete the steps in this section to check whether the **AmazonAppStreamServiceAccess**
service role is present and has the correct policies attached. If this role is
not in your account and must be created, you or an administrator with the required permissions
must perform the steps to get started with AppStream 2.0 in your Amazon Web Services account.

###### To check whether the AmazonAppStreamServiceAccess IAM service role is present

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**.
3. In the search box, type **amazonappstreamservice** to narrow the list
   of roles to select, and then choose
   **AmazonAppStreamServiceAccess**. If this role is listed,
   select it to view the role **Summary** page.
4. On the **Permissions** tab, confirm whether the **AmazonAppStreamServiceAccess** permissions policy is attached.
5. Return to the role **Summary** page.
6. On the **Trust relationships** tab, choose **Show policy document**, and then confirm whether the **AmazonAppStreamServiceAccess** trust relationship policy is attached and follows the correct format. If so, the trust relationship is correctly
   configured. Choose **Cancel** and close the IAM console.

## AmazonAppStreamServiceAccess trust relationship policy

The **AmazonAppStreamServiceAccess** trust
relationship policy must include the AppStream 2.0 service as the principal. A _principal_ is an entity in AWS that can perform actions and access resources. This
policy must also include the `sts:AssumeRole` action. The following
policy configuration defines AppStream 2.0 as a trusted entity.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "appstream.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```
