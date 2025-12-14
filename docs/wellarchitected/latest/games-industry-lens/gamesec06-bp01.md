# GAMESEC06-BP01 Use tools for detecting and responding to

threats to your infrastructure

To continuously monitor for malicious activities and unauthorized
behaviors within your AWS environment, consider
using [Amazon GuardDuty](https://aws.amazon.com/guardduty/ "https://aws.amazon.com/guardduty/"). GuardDuty identifies threats by monitoring
account behavior, network activity, and data access patterns
within your environment. It analyzes events across multiple data
sources, such as CloudTrail event logs, Amazon VPC Flow Logs, and
DNS logs for potential threats. By integrating with Amazon CloudWatch Events and Lambda, GuardDuty alerts can be
automatically forwarded to relevant security teams for further
analysis.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

[AWS Security Hub CSPM](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/") provides a comprehensive view of your security
state in AWS and check your environment against security industry
standards and best practices. Security Hub CSPM collects security data
from across AWS accounts, services, and supported third-party
partner products and analyzes your security trends and identify
the highest priority security issues.
The [Amazon GuardDuty](../../../securityhub/latest/userguide/securityhub-internal-providers.md "../../../securityhub/latest/userguide/securityhub-internal-providers.md")
[integration
with Security Hub CSPM](../../../securityhub/latest/userguide/securityhub-internal-providers.md "../../../securityhub/latest/userguide/securityhub-internal-providers.md") enables you to send findings from
GuardDuty to Security Hub CSPM. Security Hub CSPM can then include those
findings in its analysis of your security posture.

It's common for bad actors to employ bots to take over accounts
and cheat in
games. [WAF
Bot Control](https://aws.amazon.com/waf/features/bot-control/ "https://aws.amazon.com/waf/features/bot-control/") gives you visibility and control over common
and pervasive bot traffic that can consume excess resources, skew
metrics, cause downtime, or perform other undesired activities. 

Ransomware is malicious code designed to gain unauthorized access
to systems and datasets and encrypt that data to block access by
legitimate players. After ransomware has locked players out of
their systems and encrypted their sensitive data, cyber criminals
demand a ransom before providing a decryption key to unlock the
data. Organizations can be completely shut down by a malicious
event, incurring significant costs and loss of business
productivity. Refer
to [Securing
your AWS Cloud environment from ransomware](https://d1.awsstatic.com/WWPS/pdf/AWSPS_ransomware_ebook_Apr-2020.pdf "https://d1.awsstatic.com/WWPS/pdf/AWSPS_ransomware_ebook_Apr-2020.pdf") for best
practices that you can apply to strengthen your ability to fight
ransomware before, during, and after an incident takes place.

Your game may provide players with the ability to contact player
support agents through a call center such
as [Amazon
Connect](https://aws.amazon.com/connect/ "https://aws.amazon.com/connect/") or chat bots using Amazon Lex. Amazon Connect
provides support
for [monitoring
live and](../../../connect/latest/adminguide/monitoring-amazon-connect.md "../../../connect/latest/adminguide/monitoring-amazon-connect.md")
[recorded
conversations](../../../connect/latest/adminguide/monitoring-amazon-connect.md "../../../connect/latest/adminguide/monitoring-amazon-connect.md"). To analyze interactions between players and
player support chat bots built with Amazon Lex, you can store the
[conversation
logs](../../../lex/latest/dg/conversation-logs-cw.md "../../../lex/latest/dg/conversation-logs-cw.md") from these interactions in Amazon CloudWatch Logs
which can be exported to Amazon S3 and analyzed as described
previously.

Finally, conduct penetration testing exercises as part of your
infrastructure protection strategy. Whether you are performing
these assessments in-house or through an AWS Partner, adhere to
the
[AWS customer support policies for penetration testing](https://aws.amazon.com/security/penetration-testing/ "https://aws.amazon.com/security/penetration-testing/").

### Implementation steps

- Use Amazon GuardDuty to monitor account behavior, network
  activity, and data access patterns for threats, and
  integrate with Security Hub CSPM for a unified security view.
- Implement AWS WAF Bot Control to help detect and mitigate
  bot traffic that can harm resources and player experiences.
- Conduct penetration testing exercises regularly, adhering to
  AWS customer support policies, to assess and strengthen your
  security posture.
