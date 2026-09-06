

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Customer Managed application accounts
<a name="application-account-cust-man"></a>

You can create accounts that AMS doesn't manage in the standard way. Those accounts are called Customer Managed accounts and they give you full control to self-operate the infrastructure within the accounts while enjoying the benefits of the centralized architecture managed by AMS. 

Customer Managed accounts do not have access to the AMS console or any of the services we provide (patch, backup, and so on).

Customer Managed accounts can only be provisioned from your AMS multi-account landing zone management account.

Different AMS modes work with Application accounts differently; to learn more about the modes, see [AWS Managed Services modes](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ams-modes.html).

To create your Customer Managed application account, see [ Management account \| Create Customer-Managed Application Account](https://docs.aws.amazon.com/managedservices/latest/ctref/deployment-managed-management-account-create-customer-managed-application-account.html).

To delete a Customer Managed application account, use [ Management account \| Offboard Application Account](https://docs.aws.amazon.com/managedservices/latest/ctref/management-managed-management-account-offboard-application-account.html). (The [ Confirm Offboarding](https://docs.aws.amazon.com/managedservices/latest/ctref/management-managed-application-account-confirm-offboarding.html) CT does not apply to Customer Managed application accounts.)