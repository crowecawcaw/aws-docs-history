# Creating Stack Set

Constraint

CloudFormation StackSets enable users to create products that deploy across
multiple accounts and Regions. In Service Catalog, a stack set constraint allows
you to configure product deployment options.

###### To apply a stack set constraint to a Service Catalog product

1. As an AWS Service Catalog administrator, choose the portfolio that contains
   the product you want to apply a constraint.
2. Expand **Constraints** and choose **Add
   constraints**.
3. Choose the product from **Product** and set
   **Constraint type** to **Stack
   Set**. Then choose **Continue**.
4. On the **Stack set constraint** page, enter a
   description.
5. Choose the accounts in which you want to create products.
6. Choose the Regions in which you want to deploy products.
   Products deploy in these Regions in the order that you
   specify.
7. Choose the
   **AWSCloudFormationStackSetAdministratorRole**
   role to manage your target accounts.
8. Choose the
   **AWSCloudFormationStackSetExecutionRole** role
   that the administrator role will assume.
9. Choose **Submit**.

###### Note

You can use the available AWS CloudFormation templates for the JSM
connector to configure your AWS account to enable AWS Service Catalog
integration. For more information, see [Baseline Permissions](jsd-baseline-permissions.md "jsd-baseline-permissions.md").

Example stack set outputs:

```

SCStackSetAdministratorRoleARN
arn:aws:iam::123456789123:role/AWSCloudFormationStackSetAdministrationRole SCIAMStackSetExecutionRoleName
AWSCloudFormationStackSetExecutionRole
SCIAMAdminRoleARN
arn:aws:iam::123456789123:role/AWSCloudFormationStackSetAdministrationRole

```

Note that Service Catalog products can have either a stack set or a launch
constraint, but not both.
