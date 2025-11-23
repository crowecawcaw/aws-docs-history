# Instance access examples in AMS

These examples show how to log in to an instance in your AMS account by using a bastion after you've
been granted access through an RFC. For information about getting access granted,
see [Requesting instance access](access-justification.md#req-instance-access "access-justification.md#req-instance-access").

###### Note

For information on moving files to an EC2 instance, see
[File transfer: Local Windows or MAC PC to Linux Amazon EC2](../appguide/qs-file-transfer.md "../appguide/qs-file-transfer.md").

Required data:

- **Bastion DNS friendly name or IP address**: Use a DNS friendly name as described in
  [DNS friendly bastion names](dns-bastions.md "dns-bastions.md") or find bastion IP addresses as described in
  [Using bastion IP addresses](find-bastions.md "find-bastions.md").

###### Note

An Amazon EC2 instance created through an Amazon EC2 Amazon EC2 Auto Scaling group will have an IP address that cycles
in and out and you have to use your Amazon EC2 console to find that IP address.

- **User name** (for example `DOMAIN_FQDN\`\`USERNAME`) and 
**Password**: Credentials for the account. The `USERNAME` must be your Active Directory user name.

Note that a user name in the format username@customerdomain.com can be used but can cause trouble with your PBIS setup.

- **Stack IP address**: Find this by looking at the run output for the RFC that you submitted to launch
  the stack, or look up the Amazon EC2 instance IP address in the Amazon EC2 console. For a single Amazon EC2 instance, you can also use the AMS SKMS
  command ListStackSummaries to find the stack ID and then GetStack to find the stack IP address. For the AMS SKMS API reference, see the **Reports** tab in the AWS Artifact Console.
  Access the bastion IP address, either SSH or RDP, as appropriate, and log in using one of the following procedures.

###### Note

RDP bastions only allow two simultaneous connections. So, in the best case scenario, only 4 admins are able to connect
to windows stacks at the same time. If you require more connections for RDP, see
[AMS Bastion Options during Application Migrations/Onboarding](../onboardingguide/bastion-options.md "../onboardingguide/bastion-options.md") in the
_AMS onboarding guide_.
