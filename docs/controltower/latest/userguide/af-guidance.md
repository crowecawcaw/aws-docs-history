

# Account Factory guidance
<a name="af-guidance"></a>

**Note**  
Single account provision, update and customization must target an organizational unit (OU) with AWSControlTowerBaseline enabled. If an OU does not have the AWSControlTowerBaseline enabled, you can activate account auto-enrollment or use ResetEnabledBaseline and ResetEnabledControl APIs on EnabledBaselines and EnabledControls on that OU to enroll accounts. For details of AWSControlTowerBaseline, see: [Baseline types that apply at the OU level](types-of-baselines.md#ou-baseline-types). 

 You can encounter issues when using Account Factory to provision a new account in AWS Control Tower. For information about how to troubleshoot these issues, see the section [New Account Provisioning Failed](troubleshooting.md#account-provisioning-failed) in [Troubleshooting](https://docs.aws.amazon.com/controltower/latest/userguide/troubleshooting.html) of the *AWS Control Tower User Guide*. 

 We recommend that you create federated users or IAM roles instead of IAM users. Federated users and IAM roles provide you with temporary credentials. IAM users have long-term credentials that can be difficult to manage. For more information, see [IAM identities (users, user groups, and roles)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html) in the *IAM User Guide*. 

 If you're authenticated as an IAM user or IAM Identity Center user when provisioning a new account in Account Factory or when using the *Enroll account* feature AWS Control Tower, verify that your user has access to your AWS Service Catalog portfolio. Otherwise, you might receive an error message from Service Catalog. For more information, see [No Launch Paths Found Error](troubleshooting.md#no-launch-paths-found) in [the Troubleshooting section](https://docs.aws.amazon.com/controltower/latest/userguide/troubleshooting.html) of the *AWS Control Tower User Guide*. 

**Note**  
**With auto-enrollment disabled:** Up to five accounts can be provisioned simultaneously.  
**With auto-enrollment enabled:** Up to 5 accounts can be provisioned simultaneously, but any active account move operation for the destination OU blocks all provisioning on the same OU until it completes.