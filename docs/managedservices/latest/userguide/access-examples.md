

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Instance access examples in AMS
<a name="access-examples"></a>

These examples show how to log in to an instance in your AMS account by using a bastion after you've been granted access through an RFC. For information about getting access granted, see [Requesting instance access](access-justification.md#req-instance-access).

**Note**  
For information on moving files to an EC2 instance, see [File transfer: Local Windows or MAC PC to Linux Amazon EC2](https://docs.aws.amazon.com/managedservices/latest/appguide/qs-file-transfer.html).

Required data:
+ **Bastion DNS friendly name or IP address**: Use a DNS friendly name as described in [DNS friendly bastion names](dns-bastions.md) or find bastion IP addresses as described in [Using bastion IP addresses](find-bastions.md).
**Note**  
An Amazon EC2 instance created through an Amazon EC2 Auto Scaling group will have an IP address that cycles in and out and you have to use your Amazon EC2 console to find that IP address.
+ **User name** (for example {{DOMAIN\_FQDN\\}}\\{{USERNAME}}) and **Password**: Credentials for the account. The {{USERNAME}} must be your Active Directory user name.

  Note that a user name in the format username@customerdomain.com can be used but can cause trouble with your PBIS setup.
+ **Stack IP address**: Find this by looking at the run output for the RFC that you submitted to launch the stack, or look up the Amazon EC2 instance IP address in the Amazon EC2 console. For a single Amazon EC2 instance, you can also use the AMS SKMS command ListStackSummaries to find the stack ID and then GetStack to find the stack IP address. For the AMS SKMS API reference, see the **Reports** tab in the AWS Artifact Console. 

Access the bastion IP address, either SSH or RDP, as appropriate, and log in using one of the following procedures.

**Note**  
RDP bastions only allow two simultaneous connections. So, in the best case scenario, only 4 admins are able to connect to windows stacks at the same time. If you require more connections for RDP, see [AMS Bastion Options during Application Migrations/Onboarding](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/bastion-options.html) in the *AMS onboarding guide*.