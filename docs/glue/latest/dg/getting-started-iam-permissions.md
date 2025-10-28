# Set up IAM permissions for

AWS Glue Studio

You can create the roles and assign policies to users and job roles by using the AWS
administrator user.

You can use the **AWSGlueConsoleFullAccess** AWS
managed policy to provide the necessary permissions for using the AWS Glue Studio console.

To create your own policy, follow the steps documented in [Create an IAM
Policy for the AWS Glue Service](create-service-policy.md "create-service-policy.md") in the _AWS Glue Developer Guide_.
Include the IAM permissions described previously in [Review IAM permissions needed for the
AWS Glue Studio user](getting-started-min-privs.md "getting-started-min-privs.md").

###### Topics

- [Attach policies to the AWS Glue Studio user](#attach-iam-policy "#attach-iam-policy")
- [Create an IAM policy for roles not named
  "AWSGlueServiceRole\*"](#create-iam-policy "#create-iam-policy")

## Attach policies to the AWS Glue Studio user

Any AWS user that signs in to the AWS Glue Studio console must have permissions to access
specific resources. You provide those permissions by using assigning IAM policies
to the user.

###### To attach the **AWSGlueConsoleFullAccess** managed policy to

a user

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**.
3. In the list of policies, select the check box next to the **AWSGlueConsoleFullAccess**. You can use the
   **Filter** menu and the search box to filter the list
   of policies.
4. Choose **Policy actions**, and then choose
   **Attach**.
5. Choose the user to attach the policy to. You can use the
   **Filter** menu and the search box to filter the list
   of principal entities. After choosing the user to attach the policy to,
   choose **Attach policy**.
6. Repeat the previous steps to attach additional policies to the user, as
   needed.

## Create an IAM policy for roles not named

"AWSGlueServiceRole\*"

###### To configure an IAM policy for roles used by AWS Glue Studio

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Add a new IAM policy. You can add to an existing policy or create a new IAM inline policy. To create an IAM policy:
   1. Choose **Policies**, and then choose **Create Policy**. If a **Get Started** button appears, choose it, and then choose **Create Policy**.
   2. Next to **Create Your Own Policy**, choose **Select**.
   3. For **Policy Name**, type any value that is easy for you to refer to later. Optionally, type descriptive text in **Description**.
   4. For **Policy Document**, type a policy statement with the following format, and then choose **Create Policy**:

3. Copy and paste the following blocks into the policy under the "Statement" array, replacing `my-interactive-session-role-prefix`
   with the prefix for all common roles to associate with permissions for AWS Glue.

```
{
    "Action": [
        "iam:PassRole"
    ],
    "Effect": "Allow",
    "Resource": "arn:aws:iam::*:role/`my-interactive-session-role-prefix`*",
    "Condition": {
        "StringLike": {
            "iam:PassedToService": [
                "glue.amazonaws.com "
            ]
        }
    }
}
```

Here is the full example with the Version and Statement arrays included in the policy

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "iam:PassRole"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:iam::*:role/`my-interactive-session-role-prefix`*",
 "Condition": {
 "StringLike": {
 "iam:PassedToService": [
 "glue.amazonaws.com "
 ]
 }
 }
 }
 ]
}`

```

4. To enable the policy for a user, choose **Users**.
5. Choose the user to whom you want to attach the policy.
