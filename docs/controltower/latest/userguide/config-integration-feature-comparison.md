

# Feature comparison with and without AWS Config integration
<a name="config-integration-feature-comparison"></a>

 With Landing Zone 4.0, you can disable the AWS Config integration. The following table summarizes the AWS Control Tower features that are available with and without the AWS Config integration enabled on the landing zone. 


| Features | AWS Config Integration Enabled | AWS Config Integration Disabled | 
| --- | --- | --- | 
| [Preventive controls](https://docs.aws.amazon.com/controltower/latest/controlreference/preventive-controls.html) | ✓ | ✓ | 
| [Proactive controls](https://docs.aws.amazon.com/controltower/latest/controlreference/proactive-controls.html) | ✓ | ✓ | 
| [Region Deny control applied to OUs](https://docs.aws.amazon.com/controltower/latest/controlreference/ou-region-deny.html) | ✓ | ✓ | 
| [Region Deny control applied to landing zone](https://docs.aws.amazon.com/controltower/latest/userguide/region-deny.html) | ✓ |  | 
| [Detective controls](https://docs.aws.amazon.com/controltower/latest/controlreference/detective-controls.html) | ✓ |  | 
| [Account Factory](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html) | ✓ | See alternative | 
| [Account Factory for Terraform (AFT)](https://docs.aws.amazon.com/controltower/latest/userguide/aft-overview.html) | ✓ |  | 
| [Account Factory Customizations (AFC)](https://docs.aws.amazon.com/controltower/latest/userguide/af-customization-page.html) | ✓ |  | 
| [AWS Service Catalog integration](https://docs.aws.amazon.com/controltower/latest/userguide/service-catalog.html) with [Account Factory](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html) | ✓ |  | 
| [Customizations for AWS Control Tower (CfCT)](https://docs.aws.amazon.com/controltower/latest/userguide/cfct-customizations-dev-guide.html) | ✓ |  | 
| [Baselines applied to OUs](https://docs.aws.amazon.com/controltower/latest/userguide/types-of-baselines.html#ou-baseline-types) | ✓ |  | 
| [AWS CloudTrail integration and baselines](https://docs.aws.amazon.com/controltower/latest/userguide/cloudtrail.html) | ✓ | ✓ | 
| [AWS Backup integration and baselines](https://docs.aws.amazon.com/controltower/latest/userguide/with-backup.html) | ✓ |  | 
| [AWS IAM Identity Center integration and baselines](https://docs.aws.amazon.com/controltower/latest/userguide/sso.html) | ✓ |  | 
| [AWS SNS integration for drift notifications](https://docs.aws.amazon.com/controltower/latest/userguide/sns.html) | ✓ |  | 
| [Amazon EventBridge integration for drift notifications](https://docs.aws.amazon.com/controltower/latest/userguide/governance-drift.html#eventbridge-creation) | ✓ | ✓ | 
| [Register OU](https://docs.aws.amazon.com/controltower/latest/userguide/importing-existing.html) | ✓ | See alternative | 

 **Alternatives** 

 <a name="config-integration-disabled-alternative-af"></a>**Account Factory** 

 If you have the AWS Config integration disabled, you can enable [auto-enrollment](https://docs.aws.amazon.com/controltower/latest/userguide/account-auto-enrollment.html) and use AWS Organizations to create and move accounts. The accounts will inherit the controls applied to the parent OU. 

 <a name="config-integration-disabled-alternative-register-ou"></a>**Register OU** 

 If you have the AWS Config integration disabled, you can use AWS Organizations to create OUs. Then, enable controls through the Control Catalog page in the AWS Control Tower console, reset controls on the Organization page, or use AWS Control Tower APIs. 