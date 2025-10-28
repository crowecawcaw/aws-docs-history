End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# Setting up permissions for

Amazon CloudWatch

Use AWS Identity and Access Management (IAM) to create a role that gives AWS Elemental MediaStore access to
Amazon CloudWatch. You must perform these steps for CloudWatch Logs to be published for your
account. CloudWatch automatically publishes metrics for your account.

###### To allow MediaStore access to CloudWatch

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the IAM console, choose
   **Policies**, and then choose **Create
   policy**.
3. Choose the **JSON** tab and paste the following
   policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogGroups",
 "logs:CreateLogGroup"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogStream",
 "logs:DescribeLogStreams",
 "logs:PutLogEvents"
 ],
 "Resource": "arn:aws:logs:*:*:log-group:/aws/mediastore/*"
 }
 ]
}`

```

This policy allows MediaStore to create log groups and log streams
for any containers in any Region within your AWS account. 4. Choose **Review policy**. 5. On the **Review policy** page, for
**Name**, enter
`MediaStoreAccessLogsPolicy`, and then choose
**Create policy**. 6. In the navigation pane of the IAM console, choose
**Roles**, and then choose **Create
role**. 7. Choose the **Another AWS account** role type. 8. For **Account ID**, enter your AWS account
ID. 9. Choose **Next: Permissions**. 10. In the search box, enter
`MediaStoreAccessLogsPolicy`. 11. Select the check box next to your new policy, and then choose
**Next: Tags**. 12. Choose **Next: Review** to preview your new
user. 13. For **Role name**, enter
`MediaStoreAccessLogs`, and then choose
**Create role**. 14. In the confirmation message, choose the name of the role that you just
created (`MediaStoreAccessLogs`). 15. On the role's **Summary** page, choose the
**Trust relationships** tab. 16. Choose **Edit trust relationship**. 17. In the policy document, change the principal to the MediaStore
service. It should look like this:

```
"Principal": {
   "Service": "mediastore.amazonaws.com"
},
```

The entire policy should read as follows:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "mediastore.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {}
 }
 ]
}`

```

18. Choose **Update Trust Policy**.
