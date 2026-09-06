

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Deleting parameters from Parameter Store
<a name="deleting-parameters"></a>

This topic describes how to delete parameters that you have created in Parameter Store, a tool in AWS Systems Manager.

**Warning**  
Deleting a parameter removes all versions of it. Once deleted, the parameter and its versions can't be restored.

**To delete a parameter using the console**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Parameter Store**.

1. On the **My parameters** tab, select the check box next to each parameter to delete.

1. Choose **Delete**.

1. On the confirmation dialog, choose **Delete parameters**.

**To delete a parameter using the AWS CLI**
+ Run the following command:

  ```
  aws ssm delete-parameter --name "{{my-parameter}}"
  ```

  Replace {{my-parameter}} with the name of your parameter to be deleted.

  For information about all options available for use with the `delete-parameter` command, see [delete-parameter](https://docs.aws.amazon.com/cli/latest/reference/ssm/delete-parameter.html) in the *AWS Systems Manager section of the AWS CLI Command Reference*.