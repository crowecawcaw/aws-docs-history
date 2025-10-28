# AMS Automated IAM Provisioning permission boundary check

AMS permission boundary checks help you adhere to the default permission boundary policy provided by AMS. This policy is a list of actions denied by AMS Automated IAM Provisioning. Provisioning policies that contain these restricted actions require additional explicit risk acceptance. Download the policy here:
[boundary-policy.zip](samples/boundary-policy.md "samples/boundary-policy.md").

Use customer-defined permission boundary policy checks to customize deny actions beyond the AMS permission boundary policy defaults. When you onboard to AMS Automated IAM Provisioning using the following change type: Management | Managed account | AMS Automated IAM Provisioning with read-write permissions | [Enable (managed automation)](../ctref/management-managed-automated-iam-provisioning-with-read-write-permissions-enable-review-required.md "../ctref/management-managed-automated-iam-provisioning-with-read-write-permissions-enable-review-required.md") (ct-1706xvvk6j9hf), you can include a list of custom deny actions that specify additional restricted actions.

You can update the list of deny actions using the change type: Management | Managed account | Automated IAM provisioning with read-write permissions | [Update custom deny list](../ctref/management-managed-automated-iam-provisioning-with-read-write-permissions-update-custom-deny-list-review-required.md "../ctref/management-managed-automated-iam-provisioning-with-read-write-permissions-update-custom-deny-list-review-required.md") (ct-2r9xvd3sdsic0). You must use the dedicated IAM role `AWSManagedServicesIAMProvisionAdminRole` to run this change type.

###### Note

- You must provide a comprehensive list of deny actions for each update. The previous list is replaced by the new list.
- The list of deny actions must contain only actions to be denied. Allow actions aren't supported.
- The list of deny actions resides within the account as an IAM managed policy named `AWSManagedServicesIAMProvisionCustomerBoundaryPolicy`. The policy must not be attached to any role.
- The term _permission boundary_ used to denote denied actions in AMS Automated IAM Provisioning has a different contextual meaning compared to the IAM permission boundary. The IAM permission boundary sets the maximum permission that a policy can grant at runtime to an IAM entity. For more information on IAM permission boundary see [Policy types](../../../IAM/latest/UserGuide/access_policies.md#access_policy-types "../../../IAM/latest/UserGuide/access_policies.md#access_policy-types") in the _AWS Identity and Access Management User Guide_. The permission boundary in AMS Automated IAM Provisioning prevents you from provisioning an IAM policy that contains a certain set of permissions, for example, a denied list of actions.
