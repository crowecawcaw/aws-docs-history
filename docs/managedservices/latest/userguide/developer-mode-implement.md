# Getting started with AMS Advanced Developer mode

Learn the various AMS Advanced accounts with AMS Advanced Developer mode and how to successfully implement Developer mode.

###### Topics

- [Before you begin](developer-mode-faqs.md "developer-mode-faqs.md")
- [Prerequisites for Developer mode](#developer-mode-implement-prerequisites "#developer-mode-implement-prerequisites")
- [How to implement Developer mode](#developer-mode-implement-steps "#developer-mode-implement-steps")
- [Developer mode permissions](#developer-mode-role "#developer-mode-role")

## Prerequisites for AMS Developer mode

The following are the prerequisites for implementing Developer mode:

- You must be an AMS Advanced customer with at least one onboarded AMS Advanced Plus or Premium account.
- Any account you use must be an AMS Advanced Plus or Premium account.
- **Multi-Account Landing Zone (MALZ)**: You must use the `AWSManagedServicesDevelopmentRole` predefined AWS Identity and Access Management
  (IAM) role. You request this role. The next section describes how to acquire Developer mode permissions.
- **Single-Account Landing Zone (SALZ)**: You must use the `customer_developer_role` predefined AWS Identity and Access Management
  (IAM) role. You request this role. The next section describes how to acquire Developer mode permissions.

## How to implement AMS Advanced Developer mode

You implement Developer mode by requesting that your eligible AMS Advanced account be provisioned with the predefined IAM role:

- **MALZ**: `AWSManagedServicesDevelopmentRole`
- **SALZ**: `customer_developer_role`

You then assign the role to the relevant users in your federated network.

AMS Advanced recommends that you ensure that your use of Developer mode complies with your internal control frameworks and standards as Developer mode creates two vectors
of change: AMS Advanced change management for AMS Advanced-managed resources and customer-managed role
federation for resources that you, as our customer, manage. While AMS Advanced processes
remain compliant with our declarations, customer processes and control frameworks might need to be updated.

###### To implement Developer mode in your AMS Advanced account

1. Confirm the account that you want to use with Developer mode meets the requirements listed in
   [Prerequisites for AMS Developer mode](#developer-mode-implement-prerequisites "#developer-mode-implement-prerequisites").
2. Submit a request for change (RFC) using the change type (CT) Management | Managed account | Developer mode | Enable (managed automation).
   For an example of how to use this CT, see
   [Developer Mode | Enable (Managed Automation)](../ctref/management-managed-developer-mode-enable-review-required.md "../ctref/management-managed-developer-mode-enable-review-required.md").

After the CT is processed, the predefined IAM role, (`AWSManagedServicesDevelopmentRole` for **MALZ**,
`customer_developer_role` for **SALZ**), is provisioned in the requested account. 3. Assign the appropriate role to the users that require Developer mode access using your internal federation process.

AMS Advanced recommends that you limit access to prevent unwanted or unapproved provisioning of, or changes to, resources.

## AMS Advanced Developer mode permissions

The predefined role (`AWSManagedServicesDevelopmentRole` for **MALZ**,
`customer_developer_role` for **SALZ**), grants permission to create application infrastructure resources within
the AMS Advanced VPC, including IAM roles, while restricting access to _shared service_ components
that are operated by AMS Advanced (for example, management hosts, domain controllers, Trend Micro EPS, bastions, and unsupported AWS services). The role also restricts access
to the following AWS services: Amazon GuardDuty, AWS Organizations, AWS Directory Service APIs, and AMS Advanced logs.

While the role allows you to create additional IAM roles, the same permissions boundaries included in Developer mode access are
enforced on any IAM role created by the `AWSManagedServicesDevelopmentRole`.
