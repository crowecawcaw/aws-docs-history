

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Onboarding to AMS Automated IAM Provisioning in AMS
<a name="aip-onboarding"></a>

To use the new change types, first enable AMS Automated IAM Provisioning by submitting an RFC using the following change type: Management \| Managed account \| AMS Automated IAM Provisioning with read-write permissions \| [Enable (managed automation)](https://docs.aws.amazon.com/managedservices/latest/ctref/management-managed-automated-iam-provisioning-with-read-write-permissions-enable-review-required.html) (ct-1706xvvk6j9hf). AWS requires that your organization go through a customer security risk management (CSRM) process to ensure that the use of these change types are aligned with your organizational policies. The AWS operations team works with you to acquire explicit approval from your security team contact in the form of risk acceptance as part of the required review. To learn more, see the [RFC customer risk management (CSRM) process](https://docs.aws.amazon.com/managedservices/latest/userguide/rfc-security.html).

After the RFC for turning on AMS Automated IAM Provisioning with read-write permissions feature is successful, AMS enables the AMS Automated IAM Provisioning change types in the account used to submit the enable RFC. To confirm that an account has AMS Automated IAM Provisioning turned on, check the IAM console for the `AWSManagedServicesIAMProvisionAdminRole` role.

As part of onboarding, AMS provisions IAM Access Analyzer in the same AWS Region of the account to leverage its access preview capability. IAM Access Analyzer helps identify resources in your organization and accounts that are shared with an external entity, validates IAM policies against policy grammar and best practices, and generates IAM policies based on access activity in your AWS CloudTrail logs. To learn more, see [Using AWS Identity and Access Management Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html).

Once onboarded, the `AWSManagedServicesIAMProvisionAdminRole` is deployed to the enabled accounts. If you choose to use this role through SAML federation, then you must onboard the role to your federation solution. 

As part of onboarding, you can request to update AWSManagedServicesIAMProvisionAdminRole’s trust policy to grant another IAM role ARN to assume this role using AWS Security Token Service.