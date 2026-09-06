

# Considerations and recommendations for using AWS Security Incident Response with AWS Organizations
<a name="considerations_important"></a>

The following considerations and recommendations can help you understand how a delegated Security Incident Response administrator account operates in AWS Security Incident Response:

**Delegated administrator account for AWS Security Incident Response.**  
You can designate one member account as the delegated Security Incident Response administrator account. For example, if you designate a member account {{111122223333}} in {{Europe (Ireland)}}, you can't designate another member account {{555555555555}} in {{Canada (Central)}}. It is required that you use the same account as delegated Security Incident Response administrator account in all other Regions.

**You set up your delegated Security Incident Response administrator account in a specific AWS Region.**  
You designate a delegated Security Incident Response administrator account in one AWS Region during the initial setup. Although the setup is regional, AWS Security Incident Response provides organization-wide coverage across all supported AWS Regions. Security findings from Amazon GuardDuty and AWS Security Hub CSPM are ingested from all supported AWS Regions, and cases are centrally managed in the Region where you activated your subscription. The delegated Security Incident Response administrator account and member accounts must be added through AWS Organizations.

**It's not recommended to set your organization's management account as the delegated Security Incident Response administrator account.**  
Your organization's management account can be the delegated Security Incident Response administrator account. However, the AWS security best practices follow the principle of least privilege and does't recommend this configuration.

**Removing a delegated Security Incident Response administrator account from a live subscription cancels the subscription immediately.**  
If you remove a delegated Security Incident Response administrator account, AWS Security Incident Response removes all the member accounts associated with this delegated Security Incident Response administrator account. AWS Security Incident Response will no longer be enabled for all the member accounts.