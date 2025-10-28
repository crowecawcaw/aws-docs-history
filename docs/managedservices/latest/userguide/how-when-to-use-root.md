# How and when to use the root user account in AMS

The
[root user](../../../IAM/latest/UserGuide/id_root-user.md "../../../IAM/latest/UserGuide/id_root-user.md") is the superuser within your AWS
account. AMS monitors root usage. We recommend that you use root only for the few
tasks that require it, for example: changing your account settings, activating AWS Identity and Access Management
(IAM) access to billing and cost management, changing your root password, and enabling
multi-factor authentication (MFA). See
[Tasks that require root user credentials](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks") in the _AWS Identity and Access Management User Guide_.

###### Note

MFA is enabled during AMS Advanced onboarding to specifically disallow root user access. Root access in
AMS-managed accounts is different from other AWS accounts, and is critical to the security of your entire AMS-managed
environment. The MFA configured is a virtual MFA and is performed using an AMS-owned device. After the virtual MFA is
configured with AMS' assistance, the virtual token is immediately deleted. This ensures that neither you nor AMS retains
the ability to log in to the account as the root user. Root login can only be re-enabled on special requests (explained next) and
AMS expects such accesses to be used only when absolutely necessary. For information about MFA, see
[Secure New Account with Multi-Factor Authentication](../onboardingguide/sog-secure-new-account-with-mfa.md "../onboardingguide/sog-secure-new-account-with-mfa.md").

Root access always triggers an AMS Security and Operations team response. AMS monitors
API calls for root access, and alarms are triggered if such access is detected.

Requesting root access is slightly different between AMS account types.

**Root access with AMS Advanced single-account landing zone**:

If you have a single-account landing zone, contact your cloud service deliver manager (CSDM) and cloud architects (CAs) to advise them of the
root access work that you require. It is best to give twenty-four hours notice before the proposed activity.

**Root access with AMS Advanced multi-account landing zone**:

For multi-account landing zone Application, Shared Services, Security, or Networking accounts, use the
Management | Other | Other (ct-1e1xtak34nx76) change type. Include the date, time, and the purpose of using the root user
credentials and schedule the RFC to be sure to give twenty-four hours notice before the proposed activity.
Use your multi-account landing zone Management account to submit the RFC.

Additionally, contact your CSDM and CAs twenty-four hours in advance, to advise them of the root access work
you require.

**AMS operations and security response to root usage**:

AMS receives an alarm when the root user account is used. If the root credentials usage is
unscheduled, they contact the AMS Security team, and your account team, to verify if this is expected activity. If it is
not expected activity, AMS works with your Security team to investigate the issue.
