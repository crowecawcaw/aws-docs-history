

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Application account types
<a name="application-account"></a>

Application accounts are AWS accounts within the AMS-managed landing zone architecture that you use to host your workloads. AMS offers three types of Application accounts:
+ [AMS-managed application accounts](application-account-ams-managed.md)
+ [AMS Accelerate accounts](malz-accelerate-account.md)
+ [Customer Managed application accounts](application-account-cust-man.md)

Application accounts are grouped in different OUs in AWS Organizations depending on the Application account type:
+ Root OU:

  1. Applications OU
     + Managed OU: AMS-managed accounts
     + Development OU: AMS-managed accounts with Developer mode enabled

  1. Accelerate OU: AMS Accelerate Application accounts

  1. Customer-managed OU: Customer-managed Application accounts

Application accounts are provisioned through an RFC submitted from the Management account:
+ Create Application Account With VPC [ct-1zdasmc2ewzrs](https://docs.aws.amazon.com/managedservices/latest/ctref/deployment-managed-management-account-create-application-account-with-vpc.html)
+ Create Accelerate Account [ct-2p93tyd5angmi](https://docs.aws.amazon.com/managedservices/latest/ctref/deployment-managed-management-account-create-accelerate-account.html)
+ Create Customer-Managed Application Account [ct-3pwbixz27n3tn](https://docs.aws.amazon.com/managedservices/latest/ctref/deployment-managed-management-account-create-customer-managed-application-account.html)