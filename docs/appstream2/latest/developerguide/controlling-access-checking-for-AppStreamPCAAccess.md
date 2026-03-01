# Checking for the AmazonAppStreamPCAAccess Service Role and Policies

Complete the steps in this section to check whether the
**AmazonAppStreamPCAAccess** service role is present and has
the correct policies attached. If this role is not in your account and must be
created, you or an administrator with the required permissions must perform the
steps to get started with WorkSpaces Applications in your Amazon Web Services account.

###### To check whether the AmazonAppStreamPCAAccess IAM service role is present

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**.
3. In the search box, type **appstreampca** to narrow the
   list of roles to select, and then choose
   **AmazonAppStreamPCAAccess**. If this role is listed,
   select it to view the role **Summary**page.
4. On the **Permissions** tab, confirm whether the
   **AmazonAppStreamPCAAccess** permissions policy is
   attached.
5. Return to the **Role** summary page.
6. On the **Trust relationships** tab, choose **Show
   policy document**, and then confirm whether the
   **AmazonAppStreamPCAAccess** trust relationship policy
   is attached and follows the correct format. If so, the trust relationship is
   correctly configured. Choose **Cancel** and close the IAM
   console.

## AmazonAppStreamPCAAccess trust relationship policy

The **AmazonAppStreamPCAAccess** trust relationship policy
must include prod.euc.ecm.amazonaws.com as the principal. This policy must also
include the `sts:AssumeRole` action. The following policy
configuration defines ECM as a trusted entity.

###### To create the AmazonAppStreamPCAAccess trust relationship policy using the AWS CLI

1. Create a JSON file named `AmazonAppStreamPCAAccess.json` with the following
   text.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "prod.euc.ecm.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole",
 "Condition": {}
 }
 ]
}`

```

2. Adjust the `AmazonAppStreamPCAAccess.json` path as needed
   and run the following AWS CLI commands to create the trust
   relationship policy and attach the AmazonAppStreamPCAAccess managed
   policy. For more information about the managed policy, see [AWS Managed Policies Required to Access WorkSpaces Applications Resources](managed-policies-required-to-access-appstream-resources.md "managed-policies-required-to-access-appstream-resources.md").

```
aws iam create-role --path /service-role/ --role-name AmazonAppStreamPCAAccess --assume-role-policy-document file://AmazonAppStreamPCAAccess.json
```

```
aws iam attach-role-policy —role-name AmazonAppStreamPCAAccess —policy-arn arn:aws:iam::aws:policy/AmazonAppStreamPCAAccess
```
