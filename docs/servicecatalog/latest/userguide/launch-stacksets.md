

# Launching products as stack sets in multiple accounts and Regions
<a name="launch-stacksets"></a>

AWS Service Catalog enables you to launch a product in one or more accounts and AWS Regions. To do this, administrators must apply a stack set constraint to the product with the accounts and Regions, where it can launch as a stack set. For more information, see [AWS Service Catalog Stack Set Constraints](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/constraints-stackset.html) in the *AWS Service Catalog Administrator Guide*.

When you launch a product as a stack set, AWS Service Catalog shows the accounts and Regions that your administrator allows for that product. By default, all of them are selected. Clear the accounts and Regions that you don't want to deploy to. You can select the order of the Regions where you want to deploy the product. Products deploy across accounts simultaneously.

If your administrator has limited the product to your own account, the account list contains only your account, and it is already selected. The product deploys only into your account.

**(Optional) Setting maximum concurrent options and failure tolerance** 

You can choose the number of accounts per Region where you want to deploy stack instances of the product at one time, using the maximum concurrent options optional parameter. You can set the number of accounts as a percentage or a range from a minimum of one to a maximum of the total number of accounts that the administrator has defined in the stack set constraint.

You can also select the number of accounts per Region in which AWS Service Catalog allows deployments to fail before AWS Service Catalog stops the deployment operation in that Region by using the failure tolerance optional parameter. You can set the number of accounts as a percentage or a range from a minimum of zero to a maximum of the total number of accounts that the administrator defined in the stack set constraint.

This tolerance value is the number of accounts per Region that fail to deploy before CloudFormation stops deployment. You can set the maximum tolerance of the total number of accounts that the administrator has defined in the stack set constraint.

**Changing provisioned product parameters**

After you launch the product, you can update the provisioned product to change the parameters of that product. 

For example, if you launch an Amazon Elastic Compute Cloud (Amazon EC2) instance as a stack set, you can update the provisioned product to select a different instance type, such as t3.micro instead of t2.micro. This action updates all of the provisioned Stack Instances with the new instance type.

**Using stack sets versus stack instances**

A stack set enables you to create stacks in AWS accounts across Regions by using a single CloudFormation template.

A stack instance refers to a stack in a target account in a Region. It associates with only one stack set.

For more information, see [Stack set concepts](https://docs.amazonaws.cn/en_us/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html). 