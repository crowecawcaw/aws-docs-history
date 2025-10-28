# Updating the IAM Role for the customer managed configuration recorder

You can update the IAM role used by the customer managed configuration recorder. Before you update the IAM role,
ensure that you have created a new role to replace the old one. You must attach policies to the
new role that grant permissions to AWS Config to record configurations and deliver them to your
delivery channel.

For information about creating an IAM
role and attaching the required policies to the IAM role, see [Step 3: Creating an IAM Role](gs-cli-prereq.md#gs-cli-create-iamrole "gs-cli-prereq.md#gs-cli-create-iamrole").

###### Note

To find the ARN of an existing IAM role, go to the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/"). Choose
**Roles** in the navigation pane. Then choose the name of the desired role
and find the ARN at the top of the **Summary** page.

## Updating the IAM Role

You can update your IAM role using the AWS Management Console or the AWS CLI.

To update the IAM role (Console)

1. Sign in to the AWS Management Console and open the AWS Config console at
   [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home "https://console.aws.amazon.com/config/home").
2. Choose **Settings** in the navigation pane.
3. On the **Customer managed recorder** tab, choose **Edit** on the Settings page.
4. In the **Data governance**, section, choose the IAM role for AWS Config:
   - **Use an existing AWS Config service-linked role** – AWS Config creates a role that has the
     required permissions.
   - **Choose a role from your account** – For **Existing roles**, choose an IAM role in your account.

5. Choose **Save**.

To update the IAM role (AWS CLI)
Use the [`put-configuration-recorder`](../../../cli/latest/reference/configservice/put-configuration-recorder.md "../../../cli/latest/reference/configservice/put-configuration-recorder.md") command and specify the Amazon
Resource Name (ARN) of the new role:

```
$ **aws configservice put-configuration-recorder --configuration-recorder name=`configRecorderName`,roleARN=`arn:aws:iam::012345678912:role/myConfigRole`**
```
