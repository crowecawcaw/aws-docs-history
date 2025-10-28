# What are Security Hub and Security Hub CSPM?

###### Note

Security Hub is in preview release and is subject to change.

AWS Security Hub and AWS Security Hub CSPM are AWS services that protect your cloud environment. The
services complement each other. When used together, they provide valuable insight into the
security posture of your AWS environment.

[Security Hub CSPM](what-is-securityhub.md "what-is-securityhub.md") provides a comprehensive view of your security posture and helps you
evaluate your cloud environment against security industry standards and best practices.
[Security Hub](what-is-securityhub-v2.md "what-is-securityhub-v2.md") provides
a unified experience that helps you prioritize and respond to critical security issues.
Security Hub CSPM findings are routed to Security Hub automatically, where they're correlated with findings
from other security services, such as Amazon Inspector, to generate exposures. This helps you identify
the most critical risks in your environment. Security Hub also provides automated workflow
capabilities, which help you incorporate Security Hub CSPM findings into your operational workflows.

As a best practice, we recommend enabling both services. You can enable Security Hub CSPM without
enabling Security Hub if your primary focus is identifying misconfigurations and evaluating your
security posture. However, if you enable Security Hub without enabling Security Hub CSPM, Security Hub cannot
use Security Hub CSPM findings to provide information about risks and exposures in your AWS
environment. For the optimal experience, we recommend not only enabling Security Hub and Security Hub CSPM,
but also enabling these other security services: [Amazon GuardDuty](https://aws.amazon.com/guardduty/ "https://aws.amazon.com/guardduty/"), [Amazon Inspector](https://aws.amazon.com/inspector/ "https://aws.amazon.com/inspector/"), and [Amazon Macie](https://aws.amazon.com/macie/ "https://aws.amazon.com/macie/").
