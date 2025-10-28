# Grant Your Users Permissions to Send

Predictions to Quick Suite

You must grant your SageMaker Canvas users permissions to send batch predictions to Quick Suite. In Quick Suite,
users can create analyses and reports with a dataset and prepare dashboards to share their
results. For more information about sending prediction to QuickSight for analysis, see [Send predictions to Quick Suite](canvas-send-predictions.md "canvas-send-predictions.md").

To grant the necessary permissions to share batch predictions with users in QuickSight, you
must add a permissions policy to the AWS Identity and Access Management (IAM) execution role that you’ve used for the
user profile. The following section shows you how to attach a least-permissions policy to your
role.

**Add the permissions policy to your IAM role**

###### To add the permissions policy, use the following procedure:

1. Sign in to the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Roles**.
3. In the search box, search for the user's IAM role by name and select it.
4. On the page for the user's role, under **Permissions**, choose
   **Add permissions**.
5. Choose **Create inline policy**.
6. Select the JSON tab, and then paste the following least-permissions policy into the
   editor. Replace the placeholders
   `<your-account-number>` with your own
   AWS account number.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "quicksight:CreateDataSet",
 "quicksight:ListUsers",
 "quicksight:ListNamespaces",
 "quicksight:CreateDataSource",
 "quicksight:PassDataSet",
 "quicksight:PassDataSource"
 ],
 "Resource": [
 "arn:aws:quicksight:*:`111122223333`:datasource/*",
 "arn:aws:quicksight:*:`111122223333`:user/*",
 "arn:aws:quicksight:*:`111122223333`:namespace/*",
 "arn:aws:quicksight:*:`111122223333`:dataset/*"
 ]
 }
 ]
}`

```

7. Choose **Review policy**.
8. Enter a **Name** for the policy.
9. Choose **Create policy**.
   You should now have a customer-managed IAM policy attached to your execution role that
   grants your Canvas users the necessary permissions to send batch predictions to users in
   QuickSight.
