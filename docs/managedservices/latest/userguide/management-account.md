

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Management account
<a name="management-account"></a>

The management account is your initial AWS account when you begin onboarding with AMS. It utilizes AWS Organizations as a management account (also known as the payer account that pays the charges of all the member accounts), which gives the account the ability to create and financially manage member accounts. It contains the AWS landing zone (ALZ) framework, account configuration stack sets, AWS Organization service control policies (SCPs), etc.

For more information on using a management account, see [Best practices for the management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html).

The following diagram provides a high-level overview of the resources contained in the management account. 

![Management account overview showing AMS Customer Region and various AWS services and features.](http://docs.aws.amazon.com/managedservices/latest/userguide/images/management-account.png)


## Resources in the management account
<a name="management-account-resources"></a>

Other than the above standard services, no additional AWS resources are created in the management account during onboarding. The following inputs are required during onboarding to AMS: 
+ *Management account ID*: AWS Account ID that is created initially by you.
+ *Core Accounts emails*: Provide the emails to be associated with each of the core accounts: Networking, Shared Services, Logging, and Security account.
+ *Service Region*: Provide the AWS region to which all resources of your AMS landing zone will be deployed.