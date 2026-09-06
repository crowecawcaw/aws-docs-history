

# Step 6: Add a Launch constraint to your Terraform product
<a name="getstarted-launchconstraint-Terraform"></a>

**Important**  
You must create a launch constraint for HashiCorp Terraform products. Without a launch constraint, end users cannot provision the product. 

After creating a launch role in your administrator account, you are ready to associate the launch role to a launch constraint on your External or Terraform Cloud product. 

This launch constraint enables the end user to launch the product and, after launch, manage it as a provisioned product. For more information, see [AWS Service Catalog Launch Constraints](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/constraints-launch.html).

Using a launch constraint allows you follow the IAM best practice of keeping end user IAM permissions to a minimum. For more information, see [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) in the *IAM User Guide*.

**To assign a launch constraint to the product**

1. Open the AWS Service Catalog console at [https://console.aws.amazon.com/servicecatalog](https://console.aws.amazon.com/servicecatalog.).

1. In the left navigation console, choose **Portfolio**. 

1. Choose the **S3 bucket** portfolio.

1. On the **Portfolio details** page, choose the **Constraints** tab, and then choose **Create constraint**.

1. For **Product**, choose **Simple S3 bucket**. AWS Service Catalog automatically selects the **Launch** constraint type.

1. Choose **Enter role name**, and then choose **SCLaunch-S3product**. 

1. Choose ** Create**. 

**Note**  
The given role name must exist in the account that created the launch constraint and the account of the user who launches a product with this launch constraint. 