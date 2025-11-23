# AWS managed policies for AWS Service Catalog AppRegistry

## AWS managed policy: `AWSServiceCatalogAdminFullAccess`

You can attach `AWSServiceCatalogAdminFullAccess` to your IAM entities. AppRegistry also attaches this policy to
a service role that allows AppRegistry to perform actions on your behalf.

This policy grants `administrative` permissions that allow full access to the
administrator console view and grants permission to create and manage products and portfolios.

**Permissions details**

This policy includes the following permissions.

- `servicecatalog` – Allows principals full permissions to the administrator console view
  and the ability to create and manage portfolios and products, manage constraints, grant access to end users,
  and perform other administrative tasks within AWS Service Catalog.
- `cloudformation`– Allows AWS Service Catalog full permissions to list, read,
  write, and tag AWS CloudFormation stacks.
- `config`– Allows AWS Service Catalog limited permissions to portfolios, products, and
  provisioned products via AWS Config.
- `iam`– Allows principals full permissions to view and create service users, gropus, or roles
  that are required for creating and managing products and portfolios.
- `ssm` – Allows AWS Service Catalog to use AWS Systems Manager to list and read Systems Manager documents in
  the current AWS account and AWS Region.

View the policy: [AWSServiceCatalogAdminFullAccess](../../../aws-managed-policy/latest/reference/AWSServiceCatalogAdminFullAccess.md "../../../aws-managed-policy/latest/reference/AWSServiceCatalogAdminFullAccess.md").

## AWS managed policy: `AWSServiceCatalogAdminReadOnlyAccess`

You can attach `AWSServiceCatalogAdminReadOnlyAccess` to your IAM entities. AppRegistry also attaches this policy to
a service role that allows AppRegistry to perform actions on your behalf.

This policy grants `read-only` permissions that allow full access to the administrator
console view. This policy does not grant access to create or manage products and portfolios.

**Permissions details**

This policy includes the following permissions.

- `servicecatalog` – Allows principals read-only permissions to the administrator console view.
- `cloudformation`– Allows AWS Service Catalog limited permissions to list and read AWS CloudFormation stacks.
- `config`– Allows AWS Service Catalog limited permissions to portfolios, products, and
  provisioned products via AWS Config.
- `iam`– Allows principals limited permissions to view service users, groups, or roles
  that are required for creating and managing products and portfolios.
- `ssm` – Allows AWS Service Catalog to use AWS Systems Manager to list and read Systems Manager documents in
  the current AWS account and AWS Region.

View the policy: [AWSServiceCatalogAdminReadOnlyAccess](../../../aws-managed-policy/latest/reference/AWSServiceCatalogAdminReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AWSServiceCatalogAdminReadOnlyAccess.md").

## AWS managed policy: `AWSServiceCatalogEndUserFullAccess`

You can attach `AWSServiceCatalogEndUserFullAccess` to your IAM entities. AppRegistry also attaches this policy to
a service role that allows AppRegistry to perform actions on your behalf.

This policy grants `contributor` permissions that allow full access to the end user console view and
grants permission to launch products and manage provisioned products.

**Permissions details**

This policy includes the following permissions.

- `servicecatalog` – Allows principals full permissions to the end user console view
  and the ability to launch products and manage provisioned products.
- `cloudformation`– Allows AWS Service Catalog full permissions to list, read,
  write, and tag AWS CloudFormation stacks.
- `config`– Allows AWS Service Catalog limited permissions to list and read details about portfolios, products,
  and provisioned products via AWS Config.
- `ssm` – Allows AWS Service Catalog to use AWS Systems Manager to read Systems Manager documents in
  the current AWS account and AWS Region.

View the policy: [AWSServiceCatalogEndUserFullAccess](../../../aws-managed-policy/latest/reference/AWSServiceCatalogEndUserFullAccess.md "../../../aws-managed-policy/latest/reference/AWSServiceCatalogEndUserFullAccess.md").

## AWS managed policy: `AWSServiceCatalogEndUserReadOnlyAccess`

You can attach `AWSServiceCatalogEndUserReadOnlyAccess` to your IAM entities. AppRegistry also attaches this policy to
a service role that allows AppRegistry to perform actions on your behalf.

This policy grants `read-only` permissions that allow read-only access to the end user
console view. This policy does not grant permission to launch products or manage provisioned products.

**Permissions details**

This policy includes the following permissions.

- `servicecatalog` – Allows principals read-only permissions to the end user console view.
- `cloudformation`– Allows AWS Service Catalog limited permissions to list and read AWS CloudFormation stacks.
- `config`– Allows AWS Service Catalog limited permissions to list and read details about portfolios, products,
  and provisioned products via AWS Config.
- `ssm` – Allows AWS Service Catalog to use AWS Systems Manager to read Systems Manager documents in
  the current AWS account and AWS Region.

View the policy: [AWSServiceCatalogEndUserReadOnlyAccess](../../../aws-managed-policy/latest/reference/AWSServiceCatalogEndUserReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AWSServiceCatalogEndUserReadOnlyAccess.md").

## AWS managed policy: `AWSServiceCatalogSyncServiceRolePolicy`

AWS Service Catalog attaches this policy to the `AWSServiceRoleForServiceCatalogSync` service-linked role (SLR),
allowing AWS Service Catalog to sync templates in an external repository to AWS Service Catalog products.

This policy grants permissions that allows limited access to AWS Service Catalog actions (for example, API calls), and to other
AWS service actions that AWS Service Catalog depends on.

**Permissions details**

This policy includes the following permissions.

- `servicecatalog` – Allows the AWS Service Catalog artifact sync role limited access to AWS Service Catalog
  public APIs.
- `codeconnections`– Allows the AWS Service Catalog artifact sync role limited access to
  CodeConnections public APIs.
- `cloudformation`– Allows the AWS Service Catalog artifact sync role limited access to AWS CloudFormation
  public APIs.

View the policy: [AWSServiceCatalogSyncServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSServiceCatalogSyncServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSServiceCatalogSyncServiceRolePolicy.md").

**Service-linked role details**

AWS Service Catalog uses the permission details above for the `AWSServiceRoleForServiceCatalogSync` service-linked role
that is created when a user creates or updates a AWS Service Catalog product that uses CodeConnections. You can modify this policy using the
AWS CLI, AWS API, or through the AWS Service Catalog console. For more information on how to create, edit, and delete service-linked
roles, refer to [Using service-linked roles (SLRs) for AWS Service Catalog](using-service-linked-roles.md "using-service-linked-roles.md").

The permissions included in the `AWSServiceRoleForServiceCatalogSync` service-linked role
allow AWS Service Catalog to perform the following actions on behalf of the customer.

- `servicecatalog:ListProvisioningArtifacts` — Allows the AWS Service Catalog artifact sync role
  to list the provisioning artifacts for a given AWS Service Catalog product that is synced to a template file
  in a repository.
- `servicecatalog:DescribeProductAsAdmin` — Allows the AWS Service Catalog artifact sync role to
  use the `DescribeProductAsAdmin` API to get details for a AWS Service Catalog product and its associated
  provisioned artifacts that are synced to a template file in a repository. The artifact sync role uses
  the output from this call to verify the product's service quota limit for provisioning artifacts.
- `servicecatalog:DeleteProvisioningArtifact` — Allows the AWS Service Catalog artifact sync role
  to delete a provisioned artifact.
- `servicecatalog:ListServiceActionsForProvisioningArtifact` — Allows the AWS Service Catalog artifact
  sync role to determine if Service Actions are associated with a provisioning artifact and
  ensure that the provisioning artifact is not deleted if a Service Action is associated.
- `servicecatalog:DescribeProvisioningArtifact` — Allows the AWS Service Catalog artifact sync role
  to retrieve details from the `DescribeProvisioningArtifact` API, including the commit ID,
  which is provided in the `SourceRevisionInfo` output.
- `servicecatalog:CreateProvisioningArtifact` — Allows the AWS Service Catalog artifact sync role
  to create a new provisioned artifact if a change is detected (for example, a git-push is committed)
  to the source template file in the external repository.
- `servicecatalog:UpdateProvisioningArtifact` — Allows the AWS Service Catalog artifact sync role
  to update the provisioned artifact for a connected or synced product.
- `codeconnections:UseConnection` — Allows the AWS Service Catalog artifact sync role
  to use the existing connection to update and sync a product.
- `cloudformation:ValidateTemplate` — Allows the AWS Service Catalog artifact sync role limited
  access to AWS CloudFormation to validate the template format for the template that is being used in external
  repository and verify if CloudFormation can support the template.

## AWS managed policy: `AWSServiceCatalogOrgsDataSyncServiceRolePolicy`

AWS Service Catalog attaches this policy to the `AWSServiceRoleForServiceCatalogOrgsDataSync` service-linked role (SLR),
allowing AWS Service Catalog to sync with AWS Organizations.

This policy grants permissions that allows limited access to AWS Service Catalog actions (for example, API calls), and to other
AWS service actions that AWS Service Catalog depends on.

**Permissions details**

This policy includes the following permissions.

- `organizations`— Allows the AWS Service Catalog data sync role limited access to AWS Organizations
  public APIs.

View the policy: [AWSServiceCatalogOrgsDataSyncServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSServiceCatalogOrgsDataSyncServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSServiceCatalogOrgsDataSyncServiceRolePolicy.md").

**Service-linked role details**

AWS Service Catalog uses the permission details above for the `AWSServiceRoleForServiceCatalogOrgsDataSync` service-linked role
that is created when a user enables AWS Organizations shared portfolio access or creates a portfolio share. You can modify this policy using the
AWS CLI, AWS API, or through the AWS Service Catalog console. For more information on how to create, edit, and delete service-linked
roles, refer to [Using service-linked roles (SLRs) for AWS Service Catalog](using-service-linked-roles.md "using-service-linked-roles.md").

The permissions included in the `AWSServiceRoleForServiceCatalogOrgsDataSync` service-linked role
allow AWS Service Catalog to perform the following actions on behalf of the customer.

- `organizations:DescribeAccount` — Allows the AWS Service Catalog Organizations Data Sync role to retrieve
  AWS Organizations-related information about the specified account.
- `organizations:DescribeOrganization` — Allows the AWS Service Catalog Organizations Data Sync role to
  retrieve information about the organization that the user's account belongs to.
- `organizations:ListAccounts` — Allows the AWS Service Catalog Organizations Data Sync role to
  list the accounts in the user's organization.
- `organizations:ListChildren` — Allows the AWS Service Catalog Organizations Data Sync role to
  list all of the organizational units (UOs) or accounts that are contained in the specified parent OU or root.
- `organizations:ListParents` — Allows the AWS Service Catalog Organizations Data Sync role to list
  the root or OUs that serve as the immediate parent of the specified child OU or account.
- `organizations:ListAWSServiceAccessForOrganization` — Allows the AWS Service Catalog Organizations Data Sync role to
  retrieve a list of the AWS services that the user enabled to integrate with their organization.

## Deprecated policies

The following managed policies are deprecated:

- **ServiceCatalogAdminFullAccess** — Use
  **AWSServiceCatalogAdminFullAccess**
  instead.
- **ServiceCatalogAdminReadOnlyAccess** —
  Use **AWSServiceCatalogAdminReadOnlyAccess**
  instead.
- **ServiceCatalogEndUserFullAccess** —
  Use **AWSServiceCatalogEndUserFullAccess**
  instead.
- **ServiceCatalogEndUserAccess** — Use
  **AWSServiceCatalogEndUserReadOnlyAccess**
  instead.

Use the following procedure to ensure that your administrators and end users are
granted permissions using the current policies.

To migrate from the deprecated policies to the current policies, see [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console") in _AWS Identity and Access Management User Guide_.

## AppRegistry updates to AWS managed

policies

View details about updates to AWS managed policies for AppRegistry since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the AppRegistry Document history page.

| Change                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Date               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [AWSServiceCatalogSyncServiceRolePolicy](#security-iam-awsmanpol-AWSServiceCatalogSyncServiceRolePolicy "#security-iam-awsmanpol-AWSServiceCatalogSyncServiceRolePolicy") –<br>Update managed policy                      | AWS Service Catalog updated the `AWSServiceCatalogSyncServiceRolePolicy` policy to change `codestar-connections` to `codeconnections`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | May 7, 2024        |
| [AWSServiceCatalogAdminFullAccess](#security-iam-awsmanpol-AWSServiceCatalogAdminFullAccess "#security-iam-awsmanpol-AWSServiceCatalogAdminFullAccess") –<br>Update managed policy                                        | AWS Service Catalog updated the `AWSServiceCatalogAdminFullAccess` policy to include<br>permissions required for the AWS Service Catalog administrator to create the `AWSServiceRoleForServiceCatalogOrgsDataSync`<br>service-linked role (SLR) in their account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | April 14, 2023     |
| [AWSServiceCatalogOrgsDataSyncServiceRolePolicy](#security-iam-awsmanpol-AWSServiceCatalogOrgsDataSyncServiceRolePolicy "#security-iam-awsmanpol-AWSServiceCatalogOrgsDataSyncServiceRolePolicy") –<br>New managed policy | AWS Service Catalog added the `AWSServiceCatalogOrgsDataSyncServiceRolePolicy`, which is attached to the `AWSServiceRoleForServiceCatalogOrgsDataSync` service-linked role (SLR),<br>allowing AWS Service Catalog to sync with AWS Organizations. This policy allows limited access to AWS Service Catalog actions (for example, API calls), and to other<br>AWS service actions that AWS Service Catalog depends on.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | April 14, 2023     |
| [AWSServiceCatalogAdminFullAccess](#security-iam-awsmanpol-AWSServiceCatalogAdminFullAccess "#security-iam-awsmanpol-AWSServiceCatalogAdminFullAccess")<br>– Update managed policy                                        | AWS Service Catalog updated the `AWSServiceCatalogAdminFullAccess` policy to include all permissions<br>for the AWS Service Catalog Administrator and create compatibility with AppRegistry.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | January 12, 2023   |
| [AWSServiceCatalogSyncServiceRolePolicy](#security-iam-awsmanpol-AWSServiceCatalogSyncServiceRolePolicy "#security-iam-awsmanpol-AWSServiceCatalogSyncServiceRolePolicy")<br>– New managed policy                         | AWS Service Catalog added the `AWSServiceCatalogSyncServiceRolePolicy` policy, which is attached to the<br>`AWSServiceRoleForServiceCatalogSync` service-linked role (SLR). This policy allows<br>AWS Service Catalog to sync templates in an external repository to AWS Service Catalog products.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | November 18, 2022  |
| [AWSServiceRoleForServiceCatalogSync](using-service-linked-roles.md#slr-permissions "using-service-linked-roles.md#slr-permissions") –<br>New service-linked role                                                         | AWS Service Catalog added the `AWSServiceRoleForServiceCatalogSync` service-linked role (SLR). This role is required for<br>AWS Service Catalog to use CodeConnections and to create, update, and describe AWS Service Catalog Provisioning Artifacts for a product.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | November 18, 2022  |
| [AWSServiceCatalogAdminFullAccess](#security-iam-awsmanpol-AWSServiceCatalogAdminFullAccess "#security-iam-awsmanpol-AWSServiceCatalogAdminFullAccess") –<br>Updated managed policy                                       | AWS Service Catalog updated the `AWSServiceCatalogAdminFullAccess` policy to include<br>all of the required permissions for a AWS Service Catalog Administrator. The policy identifies the<br>specific actions administrator can take on all AWS Service Catalog resources, such as create, describe,<br>delete, and more. Additionally, the policy was changed to support a recently launched feature,<br>Attribute Based Access Control (ABAC) for AWS Service Catalog. ABAC allows you to use the<br>`AWSServiceCatalogAdminFullAccess` policy as a template to allow or deny actions on<br>AWS Service Catalog resources based on tags. For more information about ABAC, see [What is ABAC for AWS](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in _AWS Identity and Access Management_. | September 30, 2022 |
| AppRegistry started tracking changes                                                                                                                                                                                      | AppRegistry started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | September 15, 2022 |
