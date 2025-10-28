# Tutorial: Check the IAM execution role

Use the following procedure to check that your account already has the IAM execution role and
attach the managed IAM policy, if needed.

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**.
3. Search the list of roles for `ecsTaskExecutionRole`. If you can't find the
   role, see [Tutorial: Create the IAM execution role](create-execution-role.md "create-execution-role.md"). If
   you found the role, choose the role to view the attached policies.
4. On the **Permissions** tab, verify that the
   **AmazonECSTaskExecutionRolePolicy** managed policy is attached to the
   role. If the policy is attached, your execution role is properly configured. If not, follow
   the substeps below to attach the policy.
   1. Choose **Add permissions**, then choose **Attach
      policies**.
   2. Search for **AmazonECSTaskExecutionRolePolicy**.
   3. Check the box to the left of the
      **AmazonECSTaskExecutionRolePolicy** policy and choose
      **Attach policies**.

5. Choose **Trust relationships**.
6. Verify that the trust relationship contains the following policy. If the trust
   relationship matches the policy below, the role is configured correctly. If the trust
   relationship does not match, choose **Edit trust policy**, enter the
   following, and choose **Update policy**.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": "ecs-tasks.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```
