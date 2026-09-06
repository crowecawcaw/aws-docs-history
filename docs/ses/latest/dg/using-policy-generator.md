

# Using the policy generator
<a name="using-policy-generator"></a>

You can use the policy generator to create a simple authorization policy by following these steps.

**To create a policy by using the policy generator**

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/).

1. In the navigation pane, under **Configuration**, choose **Identities**.

1. In the **Identities** container on the **Identities** screen, select the verified identity you wish to create an authorization policy for.

1. In the details screen of the verified identity you selected in the previous step, choose the **Authorization** tab.

1. In the **Authorization policies** pane, choose **Create policy** and select **Use policy generator** from the dropdown.

1. In the **Create statement** pane, choose **Allow** in the **Effect** field. (If you want to create a policy to restrict this identity, choose **Deny** instead.)

1. In the **Principals** field, enter the *AWS account ID*, *IAM user ARN*, or AWS service to receive the permissions you want to authorize for this identity, then choose **Add**. (If you wish to authorize more than one, repeat this step for each one.)

1. In the **Actions** field, select the check box for each action you would like to authorize for your principals.

1. (Optional) Expand **Specify conditions** if you wish to add a qualifying statement to the permission.

   1. Select an operator from the **Operator** dropdown.

   1. Select a type from the **Key** dropdown.

   1. Respective to the key type you selected, enter its value in the **Value** field. (If you wish to add more conditions, choose **Add new condition** and repeat this step for each additional one.)

1. Choose **Save statement**.

1. (Optional) Expand **Create another statement** if you wish to add more statements to your policy and repeat steps 6 - 10.

1. Choose **Next** and on the **Customize policy** screen, the **Edit policy details** container has fields where you can change or customize the policy’s **Name** and the **Policy document** itself.

1. Choose **Next** and on the **Review and apply** screen, the **Overview** container will show the verified identity you’re authorizing as well as the name of this policy. In the **Policy document** pane will be the actual policy you just wrote along with any conditions you added - review the policy and if it looks correct, choose **Apply policy**. (If you need to change or correct something, choose **Previous** and work in the **Edit policy details** container.)