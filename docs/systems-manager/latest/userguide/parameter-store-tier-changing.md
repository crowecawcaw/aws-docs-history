

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Setting the Parameter Store default tier using the console, AWS CLI, or PowerShell
<a name="parameter-store-tier-changing"></a>

By default, Parameter Store sets the default setting to the standard parameter tier. You can set the default parameter tier for your AWS account and Region using the Systems Manager console, AWS CLI, or PowerShell. For example, you can change the default tier to advanced and then back to standard.

------
#### [ Console ]

The following procedure shows how to use the Systems Manager console to set the default parameter tier for the current AWS account and AWS Region.

**To set the Parameter Store default tier**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Parameter Store**.

1. Choose the **Settings** tab.

1. Choose **Manage settings**.

1. In the **Parameter default tier** section, choose an option. For information about these options, see [Specifying a default parameter tier for your AWS account and AWS Region](ps-default-tier.md).

1. If prompted, select the option to approve the changes and authorize charges. Choose **Save settings**.

To change the default tier setting later, repeat the preceding steps and specify a different default tier option.

------
#### [ CLI ]

The following procedure shows how to use the AWS CLI to set the default parameter tier for the current AWS account and AWS Region.

**To set the Parameter Store default tier using the AWS CLI**

1. Open the AWS CLI and run the following command to set the default parameter tier setting for a specific AWS Region in an AWS account.

   ```
   aws ssm update-service-setting \
       --region {{region}} \
       --setting-id arn:aws:ssm:{{region}}:{{account-id}}:servicesetting/ssm/parameter-store/default-parameter-tier \
       --setting-value {{tier-option}}
   ```

   {{region}} represents the identifier for an AWS Region supported by AWS Systems Manager, such as `us-east-2` for the US East (Ohio) Region. For a list of supported {{region}} values, see the **Region** column in [Systems Manager service endpoints](https://docs.aws.amazon.com/general/latest/gr/ssm.html#ssm_region) in the *Amazon Web Services General Reference*.

   {{tier-option}} values include `Standard`, `Advanced`, and `Intelligent-Tiering`. For information about these options, see [Specifying a default parameter tier for your AWS account and AWS Region](ps-default-tier.md).

   There is no output if the command succeeds.

1. Run the following command to view the current default parameter tier service settings for Parameter Store in the current AWS account and AWS Region.

   ```
   aws ssm get-service-setting \
       --region {{region}} \
       --setting-id arn:aws:ssm:{{region}}:{{account-id}}:servicesetting/ssm/parameter-store/default-parameter-tier
   ```

   The command returns output similar to the following.

   ```
   {
       "ServiceSetting": {
           "SettingId": "/ssm/parameter-store/default-parameter-tier",
           "SettingValue": "Advanced",
           "LastModifiedDate": 1556551683.923,
           "LastModifiedUser": "arn:aws:sts::123456789012:assumed-role/Administrator/Jasper",
           "ARN": "arn:aws:ssm:us-east-2:123456789012:servicesetting/ssm/parameter-store/default-parameter-tier",
           "Status": "Customized"
       }
   }
   ```

To change the default tier setting again, repeat this procedure and specify a different `SettingValue` option.

------
#### [ PowerShell ]

The following procedure shows how to use the Tools for Windows PowerShell to set the default parameter tier for a specific AWS Region in an Amazon Web Services account.

**To set the Parameter Store default tier using PowerShell**

1. Set the Parameter Store default tier in the current AWS account and AWS Region using the AWS Tools for PowerShell (Tools for PowerShell).

   ```
   Update-SSMServiceSetting -SettingId "arn:aws:ssm:{{region}}:{{account-id}}:servicesetting/ssm/parameter-store/default-parameter-tier" -SettingValue "{{tier-option}}" -Region {{region}}
   ```

   {{region}} represents the identifier for an AWS Region supported by AWS Systems Manager, such as `us-east-2` for the US East (Ohio) Region. For a list of supported {{region}} values, see the **Region** column in [Systems Manager service endpoints](https://docs.aws.amazon.com/general/latest/gr/ssm.html#ssm_region) in the *Amazon Web Services General Reference*.

   {{tier-option}} values include `Standard`, `Advanced`, and `Intelligent-Tiering`. For information about these options, see [Specifying a default parameter tier for your AWS account and AWS Region](ps-default-tier.md).

   There is no output if the command succeeds.

1. Run the following command to view the current default parameter tier service settings for Parameter Store in the current AWS account and AWS Region.

   ```
   Get-SSMServiceSetting -SettingId "arn:aws:ssm:{{region}}:{{account-id}}:servicesetting/ssm/parameter-store/default-parameter-tier" -Region {{region}}
   ```

   {{region}} represents the identifier for an AWS Region supported by AWS Systems Manager, such as `us-east-2` for the US East (Ohio) Region. For a list of supported {{region}} values, see the **Region** column in [Systems Manager service endpoints](https://docs.aws.amazon.com/general/latest/gr/ssm.html#ssm_region) in the *Amazon Web Services General Reference*.

   The command returns output similar to the following.

   ```
   ARN : arn:aws:ssm:us-east-2:123456789012:servicesetting/ssm/parameter-store/default-parameter-tier
   LastModifiedDate : 4/29/2019 3:35:44 PM
   LastModifiedUser : arn:aws:sts::123456789012:assumed-role/Administrator/Jasper
   SettingId        : /ssm/parameter-store/default-parameter-tier
   SettingValue     : Advanced
   Status           : Customized
   ```

To change the default tier setting again, repeat this procedure and specify a different `SettingValue` option.

------