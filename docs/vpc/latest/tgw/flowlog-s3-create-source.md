# Create the AWS Transit Gateway Flow Logs source account role for Amazon S3

From the source account, create the source role in the AWS Identity and Access Management console.

###### To create the source account role

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**.
3. Choose **Create policy**.
4. On the Create policy page, do the following:
   1. Choose **JSON**.
   2. Replace the contents of this window with the permissions
      policy at the start of this section.
   3. Choose **Next: Tags** and **Next:
      Review**.
   4. Enter a name for your policy and an optional description, and
      then choose **Create policy**.

5. In the navigation pane, choose **Roles**.
6. Choose **Create role**.
7. For the **Trusted entity type**, choose **Custom
   trust policy**. For **Custom trust
   policy**, replace `"Principal": {},` with the
   following, which specifies the log delivery service. Choose
   **Next**.

```
"Principal": {
   "Service": "delivery.logs.amazonaws.com"
},
```

8. On the **Add permissions** page, select the checkbox for the
   policy that you created earlier in this procedure, and then choose
   **Next**.
9. Enter a name for your role and optionally provide a description.
10. Choose **Create role**.
