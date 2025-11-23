# AWS Service Catalog Launch Constraints

A launch constraint specifies the AWS Identity and Access Management (IAM) role that AWS Service Catalog assumes when an end user
launches, updates, or terminates a product. An IAM role is a collection of permissions that a user or AWS
service can assume temporarily to use AWS services. For an introductory example, see:

- CloudFormation product type: [Step 6: Add a launch constraint to assign an IAM role](getstarted-launchconstraint.md "getstarted-launchconstraint.md")
- Terraform Open Source or Terraform Cloud product type: [Step 5: Create launch roles](getstarted-launchrole-Terraform.md "getstarted-launchrole-Terraform.md")
  Launch constraints apply to products in the portfolio (product-portfolio association).
  Launch constraints do not apply at the portfolio level or to a product across all portfolios. To
  associate a launch constraint with all products in a portfolio, you must apply the launch
  constraint to each product individually.

Without a launch constraint, end users must launch and manage products using their own IAM
credentials. To do so, they must have permissions for CloudFormation, AWS services that the products
use, and AWS Service Catalog. By using a launch role, you can instead limit the end users' permissions to the
minimum they require for that product. For more information about end user permissions, see
[Identity and Access Management in
AWS Service Catalog](controlling_access.md "controlling_access.md").

To create and assign IAM roles, you must have the following IAM administrative
permissions:

- `iam:CreateRole`
- `iam:PutRolePolicy`
- `iam:PassRole`
- `iam:Get*`
- `iam:List*`

## Configuring a Launch Role

The IAM role that you assign to a product as a launch constraint must have permissions
to use the following:

**For Cloudformation products**

- The `arn:aws:iam::aws:policy/AWSCloudFormationFullAccess` CloudFormation managed policy
- Services in the AWS CloudFormation template for the product
- Read access to the AWS CloudFormation template in a service-owned Amazon S3 bucket.

**For Terraform products**

- Services in the Amazon S3 template for the product
- Read access to the Amazon S3 template in a service-owned Amazon S3 bucket.
- `resource-groups:Tag`for tagging in an Amazon EC2 instance (assumed by the Terraform provisioning engine when performing provisioning operations)
- `resource-groups:CreateGroup` for resource group tagging (assumed by AWS Service Catalog to create resource groups and assign tags)

The IAM role's trust policy must allow AWS Service Catalog to assume the role. In the
procedure below, the trust policy will be set automatically when you select AWS Service Catalog as the role type. If you are not using the console,
see the section _Creating trust policies for AWS services that assume roles_ in [How to
use trust policies with IAM roles](https://aws.amazon.com/blogs/security/how-to-use-trust-policies-with-iam-roles/ "https://aws.amazon.com/blogs/security/how-to-use-trust-policies-with-iam-roles/").

###### Note

The `servicecatalog:ProvisionProduct`,
`servicecatalog:TerminateProvisionedProduct`, and
`servicecatalog:UpdateProvisionedProduct` permissions cannot be assigned in a
launch role. You must use IAM roles, as shown in the inline policy steps in
the section [Grant Permissions to
AWS Service Catalog End Users.](getstarted-iamenduser.md "getstarted-iamenduser.md")

###### Note

To view provisioned Cloudformation products and resources in the AWS Service Catalog console, end users need CloudFormation read access.
Viewing provisioned products and resources in the console does **not** use the launch role.

###### To create a launch role

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").

Terraform products require additional launch role configurations. For more information, review
[Step 5: Create launch roles](getstarted-launchrole-Terraform.md "getstarted-launchrole-Terraform.md") in
_Getting Started with a Terraform Open Source product_. 2. Choose **Roles**. 3. Choose **Create New Role**. 4. Enter a role name and choose **Next Step**. 5. Under **AWS Service Roles** next to **AWS Service Catalog**, choose **Select**. 6. On the **Attach Policy** page, Choose **Next
Step**. 7. To create the role, choose **Create Role**.

###### To attach a policy to the new role

1. Choose the role that you created to view the role details page.
2. Choose the **Permissions** tab, and expand the **Inline
   Policies** section. Then, choose **click here**.
3. Choose **Custom Policy**, and then choose
   **Select**.
4. Enter a name for the policy, and then paste the following into the **Policy
   Document** editor:

```

          "Statement":[
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
   ]
}

```

###### Note

When you configure a launch role for a launch constraint, you must use this string:
`"s3:ExistingObjectTag/servicecatalog:provisioning":"true"`. 5. Add a line to the policy for each additional service the product uses. For example, to
add permission for Amazon Relational Database Service (Amazon RDS), enter a comma at the end of the last line in the
`Action` list, and then add the following line:

```
"rds:*"
```

6. Choose **Apply Policy**.

## Applying a Launch Constraint

After you configure the launch role, assign the role to the product as a launch
constraint. This action tells AWS Service Catalog to assume the role when an end user launches the product.

###### To assign the role to a product

1. Open the Service Catalog console at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/ "https://console.aws.amazon.com/servicecatalog/").
2. Choose the portfolio that contains the product.
3. Choose the **Constraints** tab and choose **Create constraint**.
4. Choose the product from **Product** and choose **Launch** under **Constraint type**. Choose **Continue**.
5. In the **Launch constraint** section, you can select an IAM role from
   your account and enter an IAM role ARN, or enter the role name.

If you specify the role name and if an account uses the launch constraint, the account
uses that name for the IAM role. This approach allows launch-role constraints to be
account-agnostic so you can create fewer resources per shared account.

###### Note

The given role name must exist in the account that created the launch constraint and the
account of the user who launches a product with this launch constraint. 6. After specifying the IAM role, choose **Create**.

## Adding Confused Deputy to Launch Constraint

AWS Service Catalog supports [Confused
Deputy](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md") protection for the APIs that run with an Assume Role request. When you add a
launch constraint, you can restrict the launch role access by using `sourceAccount`
and `sourceArn` conditions in the launch role trust policy. It ensures that the
launch role is called by a trusted source.

In the following example, the AWS Service Catalog end-user belongs to account 111111111111. When the
AWS Service Catalog administrator creates a `LaunchConstraint` for a product, the
end-user can specify the following conditions in the launch role trust policy to restrict the
assume role to account 111111111111.

```
"Condition":{
   "ArnLike":{
      "aws:SourceArn":"arn:aws:servicecatalog:us-east-1:111111111111:*"
   },
   "StringEquals":{
      "aws:SourceAccount":"111111111111"
   }

}
```

A user who provisions a product with the `LaunchConstraint` must have the same `AccountId` (111111111111).
If not, the operation fails with an `AccessDenied` error, preventing launch role misuse.

The following AWS Service Catalog APIs are secured for Confused Deputy protection:

- `LaunchConstraint`
- `ProvisionProduct`
- `UpdateProvisionedProduct`
- `TerminateProvisionedProduct`
- `ExecuteProvisionedProductServiceAction`
- `CreateProvisionedProductPlan`
- `ExecuteProvisionedProductPlan`

The `sourceArn` protection for AWS Service Catalog only supports templated ARNs, such as
"`arn:<aws-partition>:servicecatalog:<region>:<accountId>:`" It does not support
specific resource ARNs.

## Verifying the Launch Constraint

To verify AWS Service Catalog uses the role to launch the product and successfully
provisions the product, launch the product from the AWS Service Catalog console. To test a constraint prior
to releasing it to users, create a test portfolio that contains the same products and test the
constraints with that portfolio.

###### To launch the product

1. In the menu for the AWS Service Catalog console, choose **Service Catalog**,
   **End user**.
2. Choose the product to open the **Product details** page. In the
   **Launch options** table, verify the Amazon Resource Name (ARN) of the role
   appears.
3. Choose **Launch product**.
4. Proceed through the launch steps, filling in any required information.
5. Verify that the product starts successfully.
