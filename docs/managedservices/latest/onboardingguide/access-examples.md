# Access examples

These examples show how to log in to an instance via a bastion once you have been granted access through an RFC. For details on getting access granted,
see [Access requests](../userguide/ex-access-request.md "../userguide/ex-access-request.md").

###### Note

An EC2 instance created through an Auto Scaling group will have an IP address that cycles in and out and you will have to use your EC2 console
to find that IP address.

Required data:

- **Bastion DNS friendly name or IP address**: Use a DNS friendly name as described in [DNS friendly bastion names](og-validate-service.md#dns-bastions "og-validate-service.md#dns-bastions")
  or find bastion IP addresses as described in [Finding bastion IP addresses](og-validate-service.md#skms-find-bastions "og-validate-service.md#skms-find-bastions").
- **Username** (for example username@customerdomain.com) and **Password**: Credentials for the account.
- **Stack IP address**: Get this by looking at the AMS console **Stacks** page for the stack you want to log
  into and then filtering on that stack ID in the EC2 console for your account. For a single EC2 instance, you can also use the AMS SKMS
  command For the AMS SKMS API reference, see the **Reports** tab in the AWS Artifact Console. to find the stack ID and then For the AMS SKMS API reference, see the **Reports** tab in the AWS Artifact Console. to find the stack IP address.
  Access the bastion IP address, either SSH or RDP, as appropriate, and log in using one of the following procedures.
