# Multi-party approval for logically air-gapped

vaults

## Overview of Multi-party approval in a

logically air-gapped vault

AWS Backup offers you the option to add [Multi-party approval](../../../mpa/latest/userguide/what-is.md "../../../mpa/latest/userguide/what-is.md"), a capability from
AWS Organizations, to your logically air-gapped vaults. Multi-party approval provides an additional
option to help to protect critical operations through a distributed approval process.

Multi-party approval is designed to help protect critical resources and to minimize
the time to return to full operation, such as a disruption caused by malicious
actors or malware events. This setup can help you restore the contents of a logically
air-gapped vault that may have been compromised.

There is no additional cost for integrating and using Multi-party approval teams with AWS Backup
logically air-gapped vaults (storage and cross-region transfers charges apply,
as shown on the [pricing](https://aws.amazon.com/backup/pricing "https://aws.amazon.com/backup/pricing") page).

An an AWS Backup customer, you can use Multi-party approval to grant approval capabilities
of some operations to a group of trusted individuals who can collaboratively approve
access to a logically air-gapped vault from a separately-created recovery account in the
case of suspected malicious activity that may compromise use of the primary
account.

The following steps outline the recommended flow for setting up a recovery AWS
organization, setting up Multi-party approval, and then using Multi-party approval with
your logically air-gapped vaults:

1. An administrator [creates a new
   organization through Organizations](../../../organizations/latest/userguide/orgs_getting-started.md "../../../organizations/latest/userguide/orgs_getting-started.md") to be used for recovery operations.
2. In the management account of this new organization, the administrator creates and
   configures an IAM Identity Center (IDC) instance (to enable an organization instance,
   see [Enable IAM Identity
   Center](../../../singlesignon/latest/userguide/enable-identity-center.md "../../../singlesignon/latest/userguide/enable-identity-center.md") in the _IAM Identity Center User Guide_. See also
   the sequence to [Create a Multi-party approval identity source](../../../mpa/latest/userguide/setting-up.md "../../../mpa/latest/userguide/setting-up.md") in the _Multi-party
   approval User Guide_.
3. The administrator then will [create an approval team](../../../mpa/latest/userguide/create-team.md "../../../mpa/latest/userguide/create-team.md"), the
   core group of trusted individuals who will be the primary users of Multi-party
   approval.
4. The administrator uses AWS RAM to [share an approval team](multipartyapproval-tasks-administrator.md#share-multipartyapproval-team-using-ram "multipartyapproval-tasks-administrator.md#share-multipartyapproval-team-using-ram") with
   each account that owns at least one logically air-gapped vault (likely your primary
   account). Both the account that owns the vault and the secondary organization needs to
   have RAM set up.
5. An administrator of those accounts [associates a logically air-gapped vault
   with an approval team](multipartyapproval-tasks-requester.md#associate-multipartyapproval-team "multipartyapproval-tasks-requester.md#associate-multipartyapproval-team").
6. A recovery account [requests
   access](multipartyapproval-tasks-requester.md#create-restore-access-vault "multipartyapproval-tasks-requester.md#create-restore-access-vault") to an account that has a logically air-gapped vault with an associated
   Multi-party approval team (“team”). The team associated with the account [approves or
   denies the request](../../../mpa/latest/userguide/respond-request.md "../../../mpa/latest/userguide/respond-request.md").
7. The admin of the account of that owns the logically air-gapped vault can request
   that [the approval team be
   disassociated from the vault](multipartyapproval-tasks-requester.md#disassociate-multipartyapproval-team "multipartyapproval-tasks-requester.md#disassociate-multipartyapproval-team"). The request requires current team
   approval.
8. An administrator can [update approval team membership](../../../mpa/latest/userguide/update-team.md "../../../mpa/latest/userguide/update-team.md")
   as necessary in accordance with their security practices or when people join or leave
   your organization.

## Prerequisites and best practices for

using Multi-party approval with a logically air-gapped vault

Before you can effectively and securely use Multi-party approval with your logically
air-gapped vaults, there are prerequisites and recommended best practices.

**Best practices:**

- Two (or more) AWS organizations through Organizations. One should be your primary
  organization where you have one or more accounts that have at least one logically
  air-gapped vault. The secondary organization should be your recovery organization. It
  is in this org where your multi-party approval team will be managed.

**Prerequisites**

1. You have [Set up Multi-party approval](../../../mpa/latest/userguide/setting-up.md "../../../mpa/latest/userguide/setting-up.md") and have at least one approval team.
2. At least one account in your primary organization must have a logically air-gapped
   vault (and the original backup vault).
3. The management account in the primary organization is opted-in to Multi-party
   approval.

###### Tip

AWS Backup recommends you apply a Service Control Policy (SCP) to your primary
organization and configure it with the appropriate permissions to the organization
and to each approval team. See [Multi-party approval terms](#multipartyapproval-terms "#multipartyapproval-terms")
section for a sample policy. 4. Your Multi-party approval team from the secondary (recovery) organization is [shared through AWS RAM](multipartyapproval-tasks-administrator.md#share-multipartyapproval-team-using-ram "multipartyapproval-tasks-administrator.md#share-multipartyapproval-team-using-ram") with
both your accounts that own the logically air-gapped vault(s) and your recovery accounts.

## Cross-Region considerations and

dependencies when using Multi-party approval

When you enable Multi-party approval and your IAM Identity Center instance in
different Regions, Multi-party approval makes calls across Regions to IAM Identity Center.
This means that user and group information moves across Regions. Multi-party approval Team
resources can only be created and stored in AWS Region US East (N. Virginia).

Other AWS Regions that reference Multi-party approval team resources will depend on
AWS Region US East (N. Virginia). Accordingly, Multi-party approval will make cross-Regions
calls if your Identity Center instance and/or logically air-gapped vault is not in
US East (N. Virginia).

## Multi-party approval terms, concepts, and user

personas

Multi-party approval in your logically air-gapped vault is an integration of AWS Organizations,
AWS Account Management, and AWS Backup, along with AWS Identity and Access Management ( IAM) and AWS RAM (RAM) features. Through the
CLI, you can interact with each service to send the appropriate commands. You can also use
the console, but you will need to navigate to the appropriate service’s console to
complete specific tasks.

How you interact with Multi-party approval depends on your roles and responsibilities
at your organizations, as well as the permissions you have in your AWS Backup accounts.

As shown in the [Multi-party approval User Guide](../../../mpa/latest/userguide/what-is.md "../../../mpa/latest/userguide/what-is.md"), members of your organization who use
multi-party approval will either be a **_requester_**,
an **_administrator_**, or an
**_approver_**. Specific permissions apply to each
[job
function](../../../mpa/latest/userguide/mpa-concepts.md "../../../mpa/latest/userguide/mpa-concepts.md"). In accordance with security best practices, an user should only
fulfill one job function.

**Consoles, portals, and sessions**

AWS Backup accounts with one or more logically air-gapped vaults can use multi-party
approval.

Prior to the multi-party approval process, an administrator utilizes AWS Organizations to
create a secondary organization for recovery purposes (a **recovery
organization**) if one has not previously been set up.

Then, the administrator utilizes AWS Resource Access Manager (RAM) to set up cross-organization sharing
between the primary organization and the recovery organization.

The **primary organization** is home to accounts that own and use a
logically air-gapped vault, which stores the protected data.

The recovery organization is home to at least one **recovery
account**. This account houses an access point that can serve as a critical
‘back door’ to the shared logically air-gapped vault. This access point is called a
**restore access backup vault**. This access vault does not store data;
instead, it serves as an access or mount point that mirrors the contents of the source
logically air-gapped vault but contains no data that can be changed or deleted. For
example, if a customer goes through the restore process for a recovery point in a restore
access backup vault, it is the recovery point in the logically air-gapped vault that is
restored through cross-account restore by way of the recovery account.

To ensure extra security, customers use this recovery account to carry out protected
operations in the primary account, but only after those operations have been given
approval by the associated [approval team in an approval
session](../../../mpa/latest/userguide/mpa-concepts.md#mpa-resources "../../../mpa/latest/userguide/mpa-concepts.md#mpa-resources"). A session is created by AWS once an approval request has been sent,
and that session ends when a threshold of approval team members approves or denies the
request or when the allowed session time has passed.

A team consists of **approvers** (effectively, the
_parties_ portion of Multi-party approval) who receive email
notifications of protected operation requests. These emails confirm that an approval
session has begun for the request. Approval is granted once the required minimum threshold
of approval is reached. This threshold can be set as the **multi-party approval
team** (“Team”) is created.

Multi-party approval teams are managed through the Organizations **multi-party approval
portal** (“portal”), an AWS managed application that provides identities a
centralized location where approval team members can receive and respond to approval team
invitations and operation requests.
