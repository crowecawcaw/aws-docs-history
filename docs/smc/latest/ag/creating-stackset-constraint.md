

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Creating Stack Set Constraint
<a name="creating-stackset-constraint"></a>

CloudFormation StackSets enable users to create products that deploy across multiple accounts and Regions. In Service Catalog, a stack set constraint allows you to configure product deployment options.

**To apply a stack set constraint to a Service Catalog product**

1. As an AWS Service Catalog administrator, choose the portfolio that contains the product you want to apply a constraint.

1. Expand **Constraints** and choose **Add constraints**.

1. Choose the product from **Product** and set **Constraint type** to **Stack Set**. Then choose **Continue**.

1. On the **Stack set constraint** page, enter a description.

1. Choose the accounts in which you want to create products.

1. Choose the Regions in which you want to deploy products. Products deploy in these Regions in the order that you specify.

1. Choose the **AWSCloudFormationStackSetAdministratorRole** role to manage your target accounts.

1. Choose the **AWSCloudFormationStackSetExecutionRole** role that the administrator role will assume.

1. Choose **Submit**.
**Note**  
You can use the available AWS CloudFormation templates for the JSM connector to configure your AWS account to enable AWS Service Catalog integration. For more information, see [Baseline Permissions](https://docs.aws.amazon.com/smc/latest/ag/jsd-baseline-permissions.html).

   Example stack set outputs:

   ```
   SCStackSetAdministratorRoleARN 
   arn:aws:iam::123456789123:role/AWSCloudFormationStackSetAdministrationRole SCIAMStackSetExecutionRoleName 
   AWSCloudFormationStackSetExecutionRole  
   SCIAMAdminRoleARN 
   arn:aws:iam::123456789123:role/AWSCloudFormationStackSetAdministrationRole
   ```

   Note that Service Catalog products can have either a stack set or a launch constraint, but not both.