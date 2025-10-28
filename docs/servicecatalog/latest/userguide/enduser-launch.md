# Launching a product

You can launch any product that appears in your AWS Service Catalog products list.

When you launch a product, you create a provisioned product, usually an instance of the
product in an AWS CloudFormation stack.

A provisioned product in AWS is one or more cloud resources that you manage as a single
unit such as compute instances, databases, or networking components.

###### To launch a product

1. Select the product in the AWS Service Catalog products list, then choose
   **Launch product**.
2. On the launch page, enter the name for your product. Provisioned product names must
   start with a letter and can contain only letters, numbers, and dashes. Alternatively, you
   can use an auto-generated name.
3. Choose a launch option for your product. The administrator sets constraints to launch
   options.
4. Choose the version of the product to launch.

If your product has a stack set constraint, you see the **Stack
Set** options section. Set the deployment options. If this product does not have
a stack set constraint, AWS Service Catalog skips this step.

If a product has parameters, you see the parameters section. Enter values for each
parameter the product requires. If a product has no parameters, AWS Service Catalog skips
this step.

If you define parameter rules for the product, AWS Service Catalog displays those rules and enforces them during the provisioning process. 5. Add the tags you want to your provisioned product. Tags have a key and value that help
you identify resources in your provisioned product.

**Note**: For information about tag limits, see [AWS Service Catalog Limits](../adminguide/limits.md "../adminguide/limits.md"). AWS Service Catalog automatically adds AutoTags to provisioned
resources. You cannot update or change AutoTags. AWS CloudFormation adds tags to some resources,
but these do not apply toward the limit and do not appear on this page. 6. You can optionally enable event notifications to send to an Amazon SNS topic. 7. Review your data and then choose **Launch**.

In the Provisioned product details page, choose **Refresh** to see
status message updates about resources and parameters. Note you can also choose **Create Plan** to get to the Provisioned product details page.
At the completion of the plan, you can see a summary of the resource changes.

If the product launches successfully, the status changes to **Available**.
To see output from the launch, go to the Provisioned product details page.
