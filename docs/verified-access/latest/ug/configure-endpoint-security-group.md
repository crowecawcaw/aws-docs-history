

# Allow traffic that originates from your Verified Access endpoint
<a name="configure-endpoint-security-group"></a>

You can configure the security groups for your applications so that they allow traffic that originates from your Verified Access endpoint. You do this by adding an inbound rule that specifies the security group for the endpoint as the source. We recommend that you remove any additional inbound rules, so that your application receives traffic only from your Verified Access endpoint.

We recommend that you keep your existing outbound rules.

**To update the security group rules for your application using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Verified Access endpoints**.

1. Choose the Verified Access endpoint, find **Security group IDs** on the **Details** tab, and copy the ID of the security group for your endpoint.

1. In the navigation pane, choose **Security groups**.

1. Select the check box for the security group associated with your target, and then choose **Actions**, **Edit inbound rules**.

1. To add a security group rule that allows traffic that originates from your Verified Access endpoint, do the following:

   1. Choose **Add rule**.

   1. For **Type**, choose **All traffic** or the specific traffic to allow.

   1. For **Source**, choose **Custom** and paste the ID of the security group for your endpoint.

1. (Optional) To require that traffic originates only from your Verified Access endpoint, delete any other inbound security group rules.

1. Choose **Save rules**.

**To update the security group rules for your application using the AWS CLI**  
Use the [describe-verified-access-endpoints](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-verified-access-endpoints.html) command to get the ID of the security group and then use the [authorize-security-group-ingress](https://docs.aws.amazon.com/cli/latest/reference/ec2/authorize-security-group-ingress.html) command to add an inbound rule.