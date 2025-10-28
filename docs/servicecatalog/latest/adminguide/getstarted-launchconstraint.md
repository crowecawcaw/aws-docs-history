# Step 6: Add a launch constraint to assign an IAM role

A launch constraint designates an IAM role
that AWS Service Catalog assumes
when an end user launches a product.

For this step,
you add a launch constraint
to the Linux Desktop product,
so AWS Service Catalog can use the IAM resources
that make up the product's AWS CloudFormation template.

The IAM role
that you assign
to a product as a launch constraint
must have
the following permissions

1. AWS CloudFormation
2. Services in the AWS CloudFormation template for the product
3. Read access to the AWS CloudFormation template in a service-owned Amazon S3 bucket.
   This launch constraint enables the end user to launch the product and, after launch, manage
   it as a provisioned product. For more information, see [AWS Service Catalog Launch
   Constraints](constraints-launch.md "constraints-launch.md").

Without a launch constraint, you need to grant additional IAM permissions to
your end users before they can use the Linux Desktop product. For example, the
`ServiceCatalogEndUserAccess` policy grants the minimum IAM
permissions required to access the AWS Service Catalog end user console view.

Using a launch constraint allows you follow the IAM best practice of keeping end user IAM permissions to a minimum.
For more information, see [Grant least privilege](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege") in
the _IAM User Guide_.

######

To add a launch constraint

1. Follow the instructions to [Create new policies on the JSON tab](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the _IAM User guide_.
2. Paste the following JSON policy document:
   - `cloudformation`–
     Allows AWS Service Catalog full permissions
     to create, read, update, delete, list, and tag AWS CloudFormation stacks.
   - `ec2`—
     Allows AWS Service Catalog full permissions
     to list, read, write, provision, and tag Amazon Elastic Compute Cloud (Amazon EC2) resources
     that are part
     of the AWS Service Catalog product.
     Depending on the AWS resource
     that you want to deploy,
     this permission might change.
   - `ec2`–
     Creates a new managed policy
     for you AWS account and
     attaches the specified managed policy
     to the specified IAM role.
   - `s3`—
     Allows access to Amazon S3 buckets owned by AWS Service Catalog.
     To deploy the product, AWS Service Catalog requires access to provisioning artifacts.
   - `servicecatalog`—
     Allows AWS Service Catalog permissions
     to list, read, write, tag, and launch resources
     on behalf
     of the end-user.
   - `sns`—
     Allows AWS Service Catalog permissions
     to list, read, write, and tag Amazon SNS topics
     for the launch constraint.

###### Note

Depending
on the underlying resources
that you want
to deploy,
you might need
to modify
the example JSON policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudformation:CreateStack",
 "cloudformation:DeleteStack",
 "cloudformation:DescribeStackEvents",
 "cloudformation:DescribeStacks",
 "cloudformation:GetTemplateSummary",
 "cloudformation:SetStackPolicy",
 "cloudformation:ValidateTemplate",
 "cloudformation:UpdateStack",
 "ec2:*",
 "servicecatalog:*",
 "sns:*"
 ],
 "Resource": "*"
 },
 {
 "Effect":"Allow",
 "Action":[
 "s3:GetObject"
 ],
 "Resource":"*",
 "Condition":{
 "StringEquals":{
 "s3:ExistingObjectTag/servicecatalog:provisioning":"true"
 }
 }
 }
 ]
}`

```

3. Choose **Next**, **Tags**.
4. Choose **Next,**
   **Review**.
5. In the **Review policy** page, for the **Name**, enter `linuxDesktopPolicy`.
6. Choose **Create policy**.
7. In the navigation pane, choose **Roles**. Then choose
   **Create role** and do the following:
   1. For **Select trusted entity**, choose **AWS service** and then under **Use case for
      other AWS services** choose **Service
      Catalog**. Select the Service Catalog use case and then choose **Next**.
   2. Search for the **linuxDesktopPolicy** policy and then select the checkbox.
   3. Choose **Next**.
   4. For **Role name**, type `linuxDesktopLaunchRole`.
   5. Choose **Create role**.

8. Open the AWS Service Catalog console at [https://console.aws.amazon.com/servicecatalog](https://console.aws.amazon.com/servicecatalog. "https://console.aws.amazon.com/servicecatalog.").
9. Choose the **Engineering Tools** portfolio.
10. On the **Portfolio details** page, choose the
    **Constraints** tab, and then choose **Create
    constraint**.
11. For **Product**, choose **Linux Desktop**, and for
    **Constraint type**, choose **Launch**.
12. Choose **Select IAM role**. Next choose
    **linuxDesktopLaunchRole**, and then choose **Create**.
