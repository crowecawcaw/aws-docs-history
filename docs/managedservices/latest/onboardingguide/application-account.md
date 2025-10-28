# Application account types

Application accounts are AWS accounts within the AMS-managed landing zone architecture that you use to host your workloads. AMS offers
three types of Application accounts:

- [AMS-managed application accounts](application-account-ams-managed.md "application-account-ams-managed.md")
- [AMS Accelerate accounts](malz-accelerate-account.md "malz-accelerate-account.md")
- [Customer Managed application accounts](application-account-cust-man.md "application-account-cust-man.md")
  Application accounts are grouped in different OUs in AWS Organizations depending on the Application account type:

- Root OU:

      1. Applications OU




      	+ Managed OU: AMS-managed accounts
      	+ Development OU: AMS-managed accounts with Developer mode enabled
      2. Accelerate OU: AMS Accelerate Application accounts
      3. Customer-managed OU: Customer-managed Application accounts

  Application accounts are provisioned through an RFC submitted from the Management account:

- Create Application Account With VPC
  [ct-1zdasmc2ewzrs](../ctref/deployment-managed-management-account-create-application-account-with-vpc.md "../ctref/deployment-managed-management-account-create-application-account-with-vpc.md")
- Create Accelerate Account
  [ct-2p93tyd5angmi](../ctref/deployment-managed-management-account-create-accelerate-account.md "../ctref/deployment-managed-management-account-create-accelerate-account.md")
- Create Customer-Managed Application Account
  [ct-3pwbixz27n3tn](../ctref/deployment-managed-management-account-create-customer-managed-application-account.md "../ctref/deployment-managed-management-account-create-customer-managed-application-account.md")
