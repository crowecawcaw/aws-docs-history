# Step 6: Add a Launch constraint to your Terraform product

###### Important

You must create a launch constraint for HashiCorp Terraform products. Without a launch constraint,
end users cannot provision the product.

After creating a launch role in your administrator account, you are ready to associate the
launch role to a launch constraint on your External or Terraform Cloud product.

This launch constraint enables the end user to launch the product and, after launch, manage
it as a provisioned product. For more information, see [AWS Service Catalog Launch
Constraints](constraints-launch.md "constraints-launch.md").

Using a launch constraint allows you follow the IAM best practice of keeping end user IAM permissions to a minimum.
For more information, see [Grant least privilege](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege") in
the _IAM User Guide_.

###### To assign a launch constraint to the product

1. Open the AWS Service Catalog console at [https://console.aws.amazon.com/servicecatalog](https://console.aws.amazon.com/servicecatalog. "https://console.aws.amazon.com/servicecatalog.").
2. In the left navigation console, choose **Portfolio**.
3. Choose the **S3 bucket** portfolio.
4. On the **Portfolio details** page, choose the
   **Constraints** tab, and then choose **Create
   constraint**.
5. For **Product**, choose **Simple S3 bucket**.
   AWS Service Catalog automatically selects the **Launch** constraint type.
6. Choose **Enter role name**, and then choose
   **SCLaunch-S3product**.
7. Choose **Create**.

###### Note

The given role name must exist in the account that created the launch constraint and
the account of the user who launches a product with this launch constraint.
