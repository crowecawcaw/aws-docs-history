

# Create the AWS Transit Gateway Flow Logs destination account role for Amazon Data Firehose
<a name="flowlog-fh-create-destination"></a>

From the destination account, create the destination role in the AWS Identity and Access Management console. 

**To create the destination account role**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Policies**.

1. Choose **Create policy**.

1. On the Create policy page, do the following:

   1. Choose **JSON**.

   1. Replace the contents of this window with the permissions policy at the start of this section.

   1. Choose **Next: Tags** and **Next: Review**.

   1. Enter a name for your policy that starts with **AWSLogDeliveryFirehoseCrossAccountRole**, and then choose **Create policy**.

1. In the navigation pane, choose **Roles**.

1. Choose **Create role**.

1. For the **Trusted entity type**, choose **Custom trust policy**. For** Custom trust policy**, replace `"Principal": {},` with the following, which specifies the log delivery service. Choose **Next**.

   ```
   "Principal": {
      "AWS": "arn:aws:iam::source-account:role/mySourceRole"
   },
   ```

1. On the **Add permissions** page, select the checkbox for the policy that you created earlier in this procedure, and then choose **Next**.

1. Enter a name for your role and optionally provide a description.

1. Choose **Create role**.