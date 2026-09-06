

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# AMS Automated IAM Provisioning permission boundary check
<a name="aip-runtime-checks-perm-boundary"></a>

AMS permission boundary checks help you adhere to the default permission boundary policy provided by AMS. This policy is a list of actions denied by AMS Automated IAM Provisioning. Provisioning policies that contain these restricted actions require additional explicit risk acceptance. Download the policy here: [boundary-policy.zip](samples/boundary-policy.zip).

Use customer-defined permission boundary policy checks to customize deny actions beyond the AMS permission boundary policy defaults. When you onboard to AMS Automated IAM Provisioning using the following change type: Management \| Managed account \| AMS Automated IAM Provisioning with read-write permissions \| [Enable (managed automation)](https://docs.aws.amazon.com/managedservices/latest/ctref/management-managed-automated-iam-provisioning-with-read-write-permissions-enable-review-required.html) (ct-1706xvvk6j9hf), you can include a list of custom deny actions that specify additional restricted actions. 

You can update the list of deny actions using the change type: Management \| Managed account \| Automated IAM provisioning with read-write permissions \| [Update custom deny list](https://docs.aws.amazon.com/managedservices/latest/ctref/management-managed-automated-iam-provisioning-with-read-write-permissions-update-custom-deny-list-review-required.html) (ct-2r9xvd3sdsic0). You must use the dedicated IAM role `AWSManagedServicesIAMProvisionAdminRole` to run this change type.

**Note**  
You must provide a comprehensive list of deny actions for each update. The previous list is replaced by the new list.
The list of deny actions must contain only actions to be denied. Allow actions aren't supported. 
The list of deny actions resides within the account as an IAM managed policy named `AWSManagedServicesIAMProvisionCustomerBoundaryPolicy`. The policy must not be attached to any role.
The term *permission boundary* used to denote denied actions in AMS Automated IAM Provisioning has a different contextual meaning compared to the IAM permission boundary. The IAM permission boundary sets the maximum permission that a policy can grant at runtime to an IAM entity. For more information on IAM permission boundary see [Policy types](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policy-types) in the *AWS Identity and Access Management User Guide*. The permission boundary in AMS Automated IAM Provisioning prevents you from provisioning an IAM policy that contains a certain set of permissions, for example, a denied list of actions.