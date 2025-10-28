# Creating StackSet constraints

AWS CloudFormation StackSets enable users to create and deploy products across multiple
accounts and Regions.

###### \*\*To apply a stack set constraint to a Service Catalog

product\*\*

1. As a catalog admin in Service Catalog, choose the portfolio that contains the
   product.
2. Expand **Constraints** and choose **Add constraints**.
3. Choose the product from **Product** and set **Constraint type** to **Stack
   Set**. Choose **Continue**.
4. On the StackSet constraint page, enter a description.
5. Choose the account(s) in which you want to create products.
6. Choose the Region(s) in which you want to deploy products. Products deploy
   in these Regions in the order you specify.
7. Choose the following:

**`AWSCloudFormationStackSetAdministrationRole`**
to manage your target accounts.

**`AWSCloudFormationStackSetExecutionRole`**
for the role the Administrator will assume. 8. Choose **Submit**.
