

# Setting up cross-account access
<a name="setting-up-cross-account-access"></a>

 Delegated administrator and member accounts can access organization-wide AWS Cost Explorer data from the management account by configuring a cross-account IAM role. This configuration allows these accounts to view actual usage data without switching to the management account. 

## Prerequisites
<a name="cross-account-prerequisites"></a>

 The following items and information are needed in advance of setting up cross-account access for the cost estimator: 
+ Management account must have AWS Cost Explorer enabled.
+ IAM permissions to create roles in the management account.
+ Knowledge of the delegated administrator or member account ID that will be granted cross-account access.

## Setup steps
<a name="cross-account-setup-process"></a>

 The cost estimator provides guided setup instructions directly in the console. To access the instructions navigate to the cost estimator page at [https://console.aws.amazon.com/securityhub/v2/home\#/costEstimator](https://console.aws.amazon.com/securityhub/v2/home#/costEstimator) in your organization management account. Locate the **Cross-account access** section and follow the steps outlined for setting up the cross account role. 

## Role configuration
<a name="cross-account-role-configuration"></a>

 Cross account access for the cost estimator requires setting up an IAM role with a trust policy and a permissions policy. The cross-account role must be created in the management account with the following configuration: 

**Role name (exact name required)** – AwsSecurityHubCostEstimatorCrossAccountRole

**Recommended trust policy:**

```
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
            "AWS": "arn:aws:iam::{ACCOUNT_ID}:role/{ROLE_NAME}"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

 Edit the policy by replacing the following values in the policy example: 
+  Replace {{{ACCOUNT\_ID}}} with the delegated administrator or member account ID that you are granting cross-account access to. 
+  Replace {{{ROLE\_NAME}}} with the IAM role name in the delegated administrator or member account that you are granting access to. 

**Recommended permissions policy:**

```
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "ce:GetCostAndUsage",
            "Resource": "*"
        }
    ]
}
```

**Note**  
 The trust policy restricts access to a specific account and role. Only the specified IAM principal can assume this role, preventing unauthorized access. 

## Verification
<a name="cross-account-verification"></a>

 After creating the role in the management account use the following steps to confirm the setup is working. 

1.  Sign into the delegated administrator or member account. 

1.  Navigate to the Security Hub cost estimator at [https://console.aws.amazon.com/securityhub/v2/home\#/costEstimator](https://console.aws.amazon.com/securityhub/v2/home#/costEstimator) 

1.  The page should automatically: 

   1.  Detect the management account in your organization. 

   1.  Assume the cross-account role. 

   1.  Load Cost Explorer data with organization-wide usage. 

 If successful, actual usage data appears instead of manual entry fields. 

## Troubleshooting
<a name="cross-account-troubleshooting"></a>

 This section covers common issues and solutions that can occur when setting up cross-account access. 

### Organizational usage data is not available for this account
<a name="org-usage-data-not-available"></a>

 This alert indicates the cross-account role is not accessible. Possible causes of this alert are: 

1.  **Role does not exist:** Management account has not created the role yet. 

   1.  **Solution:** Contact your management account administrator to create the role using the setup guidance. 

1.  **Role name mismatch:** Role name does not match exactly. 

   1.  **Solution:** Verify role name is `AwsSecurityHubCostEstimatorCrossAccountRole`. 

1.  **Trust policy incorrect:** Trust policy does not allow your account to assume the role. 

   1.  **Solution:** Verify trust policy includes your account ID and role name. 

1.  **Missing AssumeRole permission:** Your IAM principal lacks `sts:AssumeRole`. 

   1.  **Solution:** Contact your administrator to add `sts:AssumeRole` permission. 

 **To view detailed setup instructions:** Choose **View instructions** in the alert to open a modal with step-by-step guidance and policy templates. 

 **Workaround:** You can still use the Cost Estimator by manually entering usage values in edit mode. 