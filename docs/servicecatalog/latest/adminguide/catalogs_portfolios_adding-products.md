#

Adding products
to portfolios

You can add products
to any number
of portfolios.
When a product is updated,
all
of the
portfolios
(including shared portfolios)
that contain the product
automatically receive the new version.

######

To add a product from your catalog to a portfolio

1. Navigate
   to the **Products list** page.
2. Select a product,
   and then choose **Actions**.
   From the dropdown menu,
   choose **Add product to portfolio**.
   You're directed
   to the **Add `name-of-product` to portfolio** page.
3. Choose a portfolio,
   and then choose **Add product to portfolio**.
   When adding a Terraform product to a portfolio, the product requires a launch constraint.
   You must select an IAM role from your account, enter an IAM role ARN, or enter a role name. If you specify
   a role name and if an account uses the launch constraint, the account uses that name for the IAM role.
   This allows launch-role constraints to be account-agnostic, ensuring you can create fewer resources per
   shared account. For
   details and instructions, review [Step 6: Add a Launch constraint to your Terraform product](getstarted-launchconstraint-Terraform.md "getstarted-launchconstraint-Terraform.md")

A portfolio can contain numerous products that are mix of AWS CloudFormation and Terraform product types.
