# How and when to use the root user account in AMS

The
[root user](../../../IAM/latest/UserGuide/id_root-user.md "../../../IAM/latest/UserGuide/id_root-user.md") is the superuser within your AWS
account. AMS monitors root usage. We recommend that you use root only for the few
tasks that require it, for example: changing your account settings, activating AWS Identity and Access Management
(IAM) access to billing and cost management, changing your root password, and enabling
multi-factor authentication (MFA). See
[Tasks that require root user credentials](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks") in the _AWS Identity and Access Management User Guide_.

**Root with AMS Accelerate**:

AMS does not prohibit you from using your root user account. However,
AMS Operations and Security does treat its usage as an issue to investigate and we will reach out to your
Security team with every use.

We recommend that you contact your CSDM and CA twenty-four hours in advance, to advise
them of the root access work you intend to perform.

**AMS operations and security response to root usage**:

AMS receives an alarm when the root user account is used. If the root credentials usage is
unscheduled, they contact the AMS Security team, and your account team, to verify if this is expected activity. If it is
not expected activity, AMS works with your Security team to investigate the issue.
