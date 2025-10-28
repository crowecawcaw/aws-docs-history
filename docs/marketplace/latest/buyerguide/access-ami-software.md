# Accessing AMI-based software

Once you purchase an Amazon Machine Image (AMI)-based software product with contract pricing, you will be directed to the product’s website for account setup and conﬁguration. The
usage charges will then appear on your regular AWS account billing report.

###### To access the AMI-based software product

1. On the AWS Marketplace console, navigate to **View Subscription** and view the
   license for the software product.
2. On the **Procurement** page:
   1. Choose **Manage License** to view, grant access, and track usage
      of your entitlements in AWS License Manager.
   2. Choose **Continue to Configuration**.

3. On the **Launch** page, review your configuration and choose how you
   want to launch the software under **Choose Action**.
4. On the **Choose an Instance Type**, choose an Amazon Elastic Compute Cloud (Amazon EC2)
   instance, and then choose **Next: Configure Instance Details**.
5. On the **Configure Instance Details** page, for **IAM
   role,** choose an existing AWS Identity and Access Management (IAM) role from your AWS account.

If you don't have an IAM role, choose the **Create new IAM role
manually** link and follow the instructions.

###### Note

When you purchase a product with contract pricing, a license is created by AWS Marketplace on
the AWS account that your software can check using the License Manager API. You will need an
IAM role to launch an instance of the AMI-based product.

The following IAM permissions are required in the IAM policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"VisualEditorO",
 "Effect":"Allow",
 "Action":[
 "license-manager:CheckoutLicense",
 "license-manager:GetLicense",
 "license-manager:CheckInLicense",
 "license-manager:ExtendLicenseConsumption",
 "license-manager:ListReceivedLicenses"
 ],
 "Resource":"*"
 }
 ]
}`

```

6. After the instance details are configured, choose **Review and
   Launch**.
7. On the **Review Instance Launch** page, select an existing key pair
   or create a new key pair, and then choose **Launch Instances**.

The **Initiating Instance Launches** progress window appears. 8. After the instance is initiated, go to the EC2 dashboard, and under
**Instances**, see that the **Instance state**
displays **Running**.
