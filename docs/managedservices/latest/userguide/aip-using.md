# Using AMS Automated IAM Provisioning in AMS

You can create RFCs with the following AMS Automated IAM Provisioning change types.

###### Note

- Only provisioning on roles and policies are supported.

While updating roles, the Update CT replaces the existing list of managed policy Amazon resource names (ARNs) and the "assume role" policy document,
with the provided list of managed policy ARNs and "assume role" policy document. In a partial update; for example, adding or removing an ARN in the existing list
of managed policy ARNs, adding or removing individual policy statements to the "assume role" policy document is not allowed. Similarly, while updating policies, the
Update CT replaces the existing policy document and does not allow adding or removing individual policy statement in the existing policy document.

- When the “validate only” option is selected, run-time checks are performed without provisioning any IAM entity or policy. Regardless of any findings, the RFC status is “success”. The "success" status indicates a successful validation against the provided IAM entity or policy.

- Deployment | Advanced Stack Components | Identity and Access Management (IAM) | [Create entity or policy (read-write permissions)](../ctref/deployment-advanced-identity-and-access-management-iam-create-entity-or-policy-read-write-permissions.md "../ctref/deployment-advanced-identity-and-access-management-iam-create-entity-or-policy-read-write-permissions.md")(ct-1n9gfnog5x7fl):
  A new IAM entity or policy is validated and provisioned automatically.
- Management | Advanced Stack Components | Identity and Access Management (IAM) | [Update entity or policy (read-write permissions)](../ctref/management-advanced-identity-and-access-management-iam-update-entity-or-policy-read-write-permissions.md "../ctref/management-advanced-identity-and-access-management-iam-update-entity-or-policy-read-write-permissions.md")(ct-1e0xmuy1diafq):
  An existing IAM entity or policy is updated and validated automatically.
- Management | Advanced Stack Components | Identity and Access Management (IAM) | [Delete entity or policy (read-write permissions)](../ctref/management-advanced-identity-and-access-management-iam-delete-entity-or-policy-read-write-permissions.md "../ctref/management-advanced-identity-and-access-management-iam-delete-entity-or-policy-read-write-permissions.md")(ct-17cj84y7632o6):
  An existing IAM entity or policy that's provisioned using the automated create entity or policy change type is deleted.
  You can only call the preceding three CTs using a dedicated IAM role: `AWSManagedServicesIAMProvisionAdminRole`. This role is available only in the accounts that
  have been onboarded to the feature using the Management | Managed account | AMS Automated IAM Provisioning read-write permissions | [Enable (managed automation)](../ctref/management-managed-automated-iam-provisioning-with-read-write-permissions-enable-review-required.md "../ctref/management-managed-automated-iam-provisioning-with-read-write-permissions-enable-review-required.md") (ct-1706xvvk6j9hf).

###### Important

The Create, Update, and Delete change types are always visible in your account, but they aren't turned on by default. If you try submit an RFC using one of these change types
without first enabling the AMS Automated IAM Provisioning feature, then an "unauthorized" error displays.

**Limitations**:

- The Create CT might allow you to create an IAM role or policy with permission to create AWS resources. However, AWS resources created by these roles and policies aren't managed by AMS. It's a best practice to adhere to your organizational control to limit creation of such roles or policies.
- The Update CT can not modify IAM roles and policies created with CFN Ingest, Direct Change Mode, Developer Mode, or, in some cases,
  through existing AMS Advanced manual or automated CTs.
- The Delete CT can not delete existing roles or policies that are not created with the AMS Automated IAM Provisioning Create CT.
- The AMS Automated IAM Provisioning with read-write permissions feature isn't supported in Direct Change Mode roles. This means that you can't provision or update IAM roles and policies with read-write permissions using these roles.
- AMS Automated IAM Provisioning with read-write permissions Create, Update, and Delete change types are not compatible with the ServiceNow Connector.
