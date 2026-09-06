

# Setting Up Manual Remediation for AWS Config
<a name="setup-manualremediation"></a>

To apply remediation on noncompliant resources, you can either choose the remediation action you want to associate from a prepopulated list or create your own custom remediation actions using SSM documents. AWS Config provides a recommended list of remediation action in the AWS Management Console. 

------
#### [ Setting Up Manual Remediation (Console) ]

In the AWS Management Console, you can either choose to manually remediate noncompliant resources by associating remediation actions with AWS Config rules. With all remediation actions, you can either choose manual or automatic remediation.

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home).

1. Choose **Rules** on the left and then on the **Rules** page, choose **Add Rule** to add new rules to the rule list 

   For existing rules, select the noncompliant rule from the rule list and choose the **Actions** dropdown list.

1. From the **Actions** dropdown list, choose **Manage remediation**. Select "Manual remediation" and then choose the appropriate remediation action from the recommended list.
**Note**  
You can only manage remediations for non-service linked AWS Config rules. For more information, see [ Service-Linked AWS Rules](https://docs.aws.amazon.com/config/latest/developerguide/service-linked-awsconfig-rules.html).

   Depending on the selected remediation action, you see specific parameters or no parameters.

1. (Optional): If you want to pass the resource ID of noncompliant resources to the remediation action, choose **Resource ID parameter**. If selected, at runtime that parameter is substituted with the ID of the resource to be remediated.

   Each parameter has either a static value or a dynamic value. If you do not choose a specific resource ID parameter from the dropdown list, you can enter values for each key. If you choose a resource ID parameter from the dropdown list, you can enter values for all the other keys except the selected resource ID parameter. 

1. Choose **Save**. The **Rules** page is displayed.

For troubleshooting failed remediation actions, you can run the AWS Command Line Interface command `describe-remediation-execution-status` to get detailed view of a Remediation Execution for a set of resources. The details include state, timestamps for remediation execution steps, and any error messages for the failed steps.

------
#### [ Setting Up Manual Remediation (API) ]

Use the following AWS Config API operation to set up manual remediation:
+ [PutRemediationConfigurations](https://docs.aws.amazon.com/config/latest/APIReference/API_PutRemediationConfigurations.html), adds or updates the remediation configuration with a specific AWS Config rule with the selected target or action.
+ [StartRemediationExecution](https://docs.aws.amazon.com/config/latest/APIReference/API_StartRemediationExecution.html), runs an on-demand remediation for the specified AWS Config rules against the last known remediation configuration. 
+ [DescribeRemediationExecutionStatus](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeRemediationExecutionStatus.html), provides a detailed view of a Remediation Execution for a set of resources including state, timestamps for when steps for the remediation execution occur, and any error messages for steps that have failed. 
+ [DescribeRemediationConfigurations](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeRemediationConfigurations.html), returns the details of one or more remediation configurations.

------