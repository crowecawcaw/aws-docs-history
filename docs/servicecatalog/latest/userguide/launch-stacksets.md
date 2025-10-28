# Launching products as stack sets in multiple accounts and

Regions

AWS Service Catalog enables you to launch a product in one or more accounts and AWS
Regions. To do this, administrators must apply a stack set constraint to the product with the
accounts and Regions, where it can launch as a stack set. For more information, see [AWS Service Catalog Stack Set Constraints](../adminguide/constraints-stackset.md "../adminguide/constraints-stackset.md") in the _AWS Service Catalog
Administrator Guide_.

When you launch a product as a stack set, AWS Service Catalog by default,
selects all of the accounts and Regions where that product can launch. You can remove accounts
and Regions as needed. You can select the order of the Regions where you want to deploy the
product while products deploy across accounts. Products deploy across accounts
simultaneously.

**(Optional) Setting maximum concurrent options and failure
tolerance**

You can choose the number of accounts per Region where you want to deploy stack instances
of the product at one time, using the maximum concurrent options optional parameter. You can
set the number of accounts as a percentage or a range from a minimum of one to a maximum of
the total number of accounts that the administrator has defined in the stack set
constraint.

You can also select the number of accounts per Region in which AWS Service Catalog
allows deployments to fail before AWS Service Catalog stops the deployment operation in that
Region by using the failure tolerance optional parameter. You can set the number of accounts
as a percentage or a range from a minimum of zero to a maximum of the total number of accounts
that the administrator defined in the stack set constraint.

This tolerance value is the number of accounts per Region that fail to
deploy before AWS CloudFormation stops deployment. You can set the maximum tolerance of the
total number of accounts that the administrator has defined in the stack set
constraint.

**Changing provisioned product parameters**

After you launch the product, you can update the provisioned product to change the
parameters of that product.

For example, if you launch an Amazon Elastic Compute Cloud (Amazon EC2) instance as a
stack set, you can update the provisioned product to select a different instance type, such as
t3.micro instead of t2.micro. This action updates all of the provisioned Stack Instances with
the new instance type.

**Using stack sets versus stack instances**

A stack set enables you to create stacks in AWS accounts across Regions by using a single
AWS CloudFormation template.

A stack instance refers to a stack in a target account in a Region. It
associates with only one stack set.

For more information, see [Stack set concepts](https://docs.amazonaws.cn/en_us/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html "https://docs.amazonaws.cn/en_us/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html").
