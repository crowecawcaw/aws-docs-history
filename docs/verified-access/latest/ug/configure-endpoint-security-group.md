# Allow traffic that originates from your Verified Access

endpoint

You can configure the security groups for your applications so that they allow traffic that
originates from your Verified Access endpoint. You do this by adding an inbound rule that specifies the
security group for the endpoint as the source. We recommend that you remove any additional
inbound rules, so that your application receives traffic only from your Verified Access endpoint.

We recommend that you keep your existing outbound rules.

###### To update the security group rules for your application using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Verified Access endpoints**.
3. Choose the Verified Access endpoint, find **Security group IDs** on the
   **Details** tab, and copy the ID of the security group for your endpoint.
4. In the navigation pane, choose **Security groups**.
5. Select the check box for the security group associated with your target, and then choose
   **Actions**, **Edit inbound rules**.
6. To add a security group rule that allows traffic that originates from your Verified Access endpoint,
   do the following:
   1. Choose **Add rule**.
   2. For **Type**, choose **All traffic** or the specific
      traffic to allow.
   3. For **Source**, choose **Custom** and paste the
      ID of the security group for your endpoint.

7. (Optional) To require that traffic originates only from your Verified Access endpoint, delete any
   other inbound security group rules.
8. Choose **Save rules**.

###### To update the security group rules for your application using the AWS CLI

Use the [describe-verified-access-endpoints](../../../cli/latest/reference/ec2/describe-verified-access-endpoints.md "../../../cli/latest/reference/ec2/describe-verified-access-endpoints.md") command to get the ID of the security
group and then use the [authorize-security-group-ingress](../../../cli/latest/reference/ec2/authorize-security-group-ingress.md "../../../cli/latest/reference/ec2/authorize-security-group-ingress.md") command to add an inbound rule.
