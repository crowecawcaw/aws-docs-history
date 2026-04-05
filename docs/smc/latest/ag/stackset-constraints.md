End of support notice: On March 31, 2027, AWS
will end support for AWS Service Management Connector. After March 31, 2027, you will
no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources.
For more information, see [AWS Service Management Connector end of support](smc-end-of-support.md "smc-end-of-support.md").

# Creating stack set constraints

CloudFormation StackSets enable users to create and deploy products across multiple
accounts and Regions.

###### **To apply a stack set constraint to a Service Catalog product**

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

###### Note

The available template for baseline permissions creates the permissions as well as the outputs
needed for stack set constraints.

Example stack set outputs

```

                  SCStackSetAdministratorRoleARN
                  arn:aws:iam::123456789123:role/AWSCloudFormationStackSetAdministrationRole
                  SCIAMStackSetExecutionRoleName
                  AWSCloudFormationStackSetExecutionRole
                  SCIAMAdminRoleARN
                  arn:aws:iam::123456789123:role/AWSCloudFormationStackSetAdministrationRole

```

The AWS Service Catalog products can have either a set set or a launch constraint, but not both.
