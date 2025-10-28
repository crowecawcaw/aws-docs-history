# Accessing container-based software

Once you purchase a container-based software product with contract pricing, you will be directed to the product’s website
for account setup and conﬁguration. The usage charges will then appear on your regular AWS account billing report.

###### To access the container-based software product

1. On the AWS Marketplace console, navigate to **View Subscription** and view the
   license for the software product.
2. On the **Procurement** page:
   1. Choose **Manage License** to view, grant access, and track usage
      of your entitlements in AWS License Manager.
   2. Choose **Continue to Configuration**.

3. On the **Launch** page, view the container image details and follow
   the provided directions.

While creating an Amazon Elastic Container Service (Amazon ECS) cluster, you must add the following AWS Identity and Access Management
(IAM) permissions to your IAM policy.

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
