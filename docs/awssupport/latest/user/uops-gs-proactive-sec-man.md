

# Unified Operations Getting started: Onboard your account to proactive security incident management

Unified Operations entitles you to AWS Security Incident Response to help you quickly prepare for, respond to, and recover from security incidents, such as account takeovers, data breaches, and ransomware attacks. AWS Security Incident Response triages findings, escalates events, and manages critical cases, while also providing access to the AWS Customer Incident Response Team (CIRT) to investigate impacted resources. This access helps you to effectively mitigate and resolve security incidents, minimizing the impact on your operations. To onboard to this service feature, complete the following steps.

After you sign up, AWS Security Incident Response automatically monitors and triages alerts from Amazon GuardDuty and AWS Security Hub CSPM integrations across the accounts that your membership covers. For more information, see [Proactive response and alert triaging](https://docs.aws.amazon.com/security-ir/latest/userguide/proactive-response-alert-triaging.html) in the *AWS Security Incident Response User Guide*.

You can also turn on proactive containment. With proactive containment, AWS can take containment actions to quickly mitigate impact, such as isolating compromised hosts or rotating credentials.

1. To set up AWS Security Incident Response, create a centralized AWS account to use as your Security Incident Response membership account. For instructions on signing up and choosing your membership account, see [Sign up and choose your membership account](https://docs.aws.amazon.com/security-ir/latest/userguide/deploy-configure.html#deploy-configure-signup) in the *AWS Security Incident Response User Guide*.

   You use this account to configure the other AWS accounts that you want monitored. You also use it to manage your incident response team and to create and view security events. Align this account with the account that you use for other security services, such as Amazon GuardDuty and AWS Security Hub CSPM. You can use an [AWS Organizations](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/aws-organizations.html) management account or an AWS Organizations delegated administrator account as the membership account.

   1. Choose basic membership details. For instructions on configuring membership details and account scope, see [Configure membership details and account scope](https://docs.aws.amazon.com/security-ir/latest/userguide/deploy-configure.html#deploy-configure-membership-details) in the *AWS Security Incident Response User Guide*.

   1. Choose how you want to associate accounts with AWS Organizations. For instructions on associating accounts with AWS Organizations, see [Account association to AWS Organizations](https://docs.aws.amazon.com/security-ir/latest/userguide/managing-associated-accounts.html) in the *AWS Security Incident Response User Guide*.

   1. Review the service permissions.

   1. Complete signup.

1. (Optional) To turn on proactive containment, deploy an [AWS CloudFormation StackSet](https://docs.aws.amazon.com/security-ir/latest/userguide/working-with-stacksets.html) that grants Security Incident Response the necessary permissions.