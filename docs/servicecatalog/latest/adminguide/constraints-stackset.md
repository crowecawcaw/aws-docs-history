

# AWS Service Catalog Stack Set Constraints
<a name="constraints-stackset"></a>

**Note**  
AWS Service Catalog does not support stack set constraints for Terraform Open Source products.
AutoTags are not currently supported with CloudFormation StackSets. 

A stack set constraint lets an administrator restrict the accounts and AWS Regions where end users can deploy a product as a CloudFormation stack set. The accounts and Regions in the constraint are the allowed targets. When end users launch the product, they choose which of the allowed accounts and Regions to deploy to, and the order of deployment across Regions. An administrator can also limit the product to the launching user's own account only, by specifying `self` as the account.

**To apply a stack set constraint to a product**

1. Open the Service Catalog console at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/).

1. Choose the portfolio with the product you want.

1. Choose the **Constraints** tab and then choose **Create constraints**.

1. In **Product**, choose the product. In **Constraint type**, choose **Stack Set**. 

1. Configure the accounts, regions, and permissions for your stack set constraints.
   + In **Account settings**, enter the list of accounts that end users are allowed to deploy this product to. End users can deploy to any of these accounts, or a subset of them. Alternatively, enter `self` to limit deployment to the account of the user who launches the product.
   + In **Region settings**, choose the Regions that end users are allowed to deploy this product to, and the default order in which those Regions are deployed. End users can deploy to any of these Regions, or a subset of them.
   + In **Permissions**, choose an IAM StackSet Administrator Role to manage your target accounts, either by ARN or by role name. If you specify a role name, the role with that name must exist in the account of the user who launches the product. This lets the same constraint work in every account that launches the product without maintaining a role ARN per account. If you don't choose a role, StackSets uses the default ARN. [Learn more about setting up stack set permissions.](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html)

1. Choose **Create**.