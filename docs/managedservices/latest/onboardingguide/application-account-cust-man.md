# Customer Managed application accounts

You can create accounts that AMS doesn't manage in the standard way. Those accounts are called
Customer Managed accounts and they give you full control to self-operate the infrastructure within
the accounts while enjoying the benefits of the centralized architecture managed by AMS.

Customer Managed accounts do not have access to the AMS console or any of the services we provide
(patch, backup, and so on).

Customer Managed accounts can only be provisioned from your AMS multi-account landing zone management account.

Different AMS modes work with Application accounts differently; to learn more about the modes, see
[AWS Managed Services modes](ams-modes.md "ams-modes.md").

To create your Customer Managed application account, see
[Management account | Create Customer-Managed Application Account](../ctref/deployment-managed-management-account-create-customer-managed-application-account.md "../ctref/deployment-managed-management-account-create-customer-managed-application-account.md").

To delete a Customer Managed application account, use [Management account | Offboard Application Account](../ctref/management-managed-management-account-offboard-application-account.md "../ctref/management-managed-management-account-offboard-application-account.md"). (The [Confirm Offboarding](../ctref/management-managed-application-account-confirm-offboarding.md "../ctref/management-managed-application-account-confirm-offboarding.md") CT does not apply to Customer Managed application
accounts.)
