# Enabling Amazon CloudWatch Logs for a Neptune notebook

CloudWatch Logs for Neptune notebooks are disabled by default. Follow these steps to
enable them, for debugging or other purposes:

###### Using the AWS Management Console to enable CloudWatch Logs for a Neptune notebook

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the navigation pane on the left, choose **Notebook**,
   then **Notebook Instances**. Look for the name of the Neptune
   notebook for which you would like to enable logs.
3. Go to the details page by choosing the name of the notebook
   instance mentioned in the above step.
4. If the notebook instance is running, select the **Stop**
   button, at the top right of the notebook details page.
5. Under **Permissions and encryption** there is a
   field for **IAM role ARN**. Select the link in this field
   to go to the IAM role for this notebook.
6. Create the following policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogDelivery",
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:DeleteLogDelivery",
 "logs:Describe*",
 "logs:GetLogDelivery",
 "logs:GetLogEvents",
 "logs:ListLogDeliveries",
 "logs:PutLogEvents",
 "logs:PutResourcePolicy",
 "logs:UpdateLogDelivery"
 ],
 "Resource": "*"
 }
 ]
}`

```

7. Save this new policy, and attach it to the IAM role in step 4.
8. Select **Start** at the top right of the SageMaker AI
   notebook instance details page.
9. Once logs start flowing, you should see a **View Logs**
   link underneath the field labeled **Lifecycle configuration** near
   the bottom left of the **Notebook instance settings** section of
   the details page.
   If your notebook fails to start there will be a message in the notebook details
   page on the SageMaker AI console stating that the notebook instance took more than 5 minutes
   to start. The CloudWatch Logs relevant to this issue can be found under the name:
   ``(your-notebook-name)`/LifecycleConfigOnStart`.

See [Log Amazon SageMaker
Events with Amazon CloudWatch](../../../sagemaker/latest/dg/logging-cloudwatch.md "../../../sagemaker/latest/dg/logging-cloudwatch.md") for more details, if necessary.
