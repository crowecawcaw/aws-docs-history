

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Managing EC2 instance access
<a name="transition-managing-ec2-access-accelerate"></a>

As part of your move to AMS Accelerate, AMS removes the bastion hosts and the management host from your accounts and hands the Active Directory (AD) infrastructure over to you. Instance access changes from a prescriptive, request-based model to one that you own and operate.

This section covers how you reach your Amazon EC2 instances before, during, and after the transition. It explains what changes, what AMS needs from you beforehand, what becomes your responsibility afterward, and how access remains available throughout.

## What changes, and what stays the same
<a name="transition-ec2-access-changes"></a>

You keep signing in to your instances with the same AD credentials you use today. What changes is how you reach an instance and how access is granted, not the identity you sign in with. The following table compares each part of the access model before and after the transition.


| Access model component | Before (AMS Advanced) | After (AMS Accelerate) | 
| --- | --- | --- | 
| **Requesting access** | You submit a request for change (RFC `ct-1dmlg9g1l91h6`) and wait 5 to 10 minutes. | No request needed. You grant and maintain access yourself. | 
| **How long access lasts** | Time limited. A dynamic group expires after the number of hours you requested. | Permanent, until you remove the member from the group. | 
| **Connection path** | From your network to a bastion host, then from the bastion host to the instance (two hops). | From your network to the instance (one hop). | 
| **Adding and removing users** | You submit an RFC and AMS automation runs it. | You do it yourself. For example, you can use Active Directory Users and Computers (ADUC) or AWS Systems Manager Run Command. | 
| **Administering Active Directory** | Through the AMS management host. | You administer AD from a directory administration EC2 instance that you run. | 
| **Domain join for existing instances** | The AMS AMI bootstrap code ran at first boot. | No change. Existing instances stay domain joined, and you don't need to rejoin them. | 
| **Domain join for new instances** | The AMS AMI bootstrap code ran automatically. | Your own bootstrap code joins the domain on Windows and Linux, and installs the PBIS (AD Bridge) agent on Linux. Seamless domain join is another option. | 
| **How AMS operations reaches your instances** | Through a DMZ bastion host. | As a temporary local user through AWS Systems Manager Session Manager. | 
| **PBIS (AD Bridge) license** | AMS renewed it from the management host. | The current term stays active until it expires on June 1, 2027. After that, you renew it yourself with a new license key. For more information, see [PBIS (AD Bridge) license](#transition-ec2-access-pbis). | 

The following parts of your environment aren't affected by the transition:
+ Your existing one-way forest trust, in which the AMS directory trusts yours.
+ Your existing instances. They keep running, they stay domain joined, and the AMS bootstrap scripts and PBIS (AD Bridge) agent on them stay in place and keep working.
+ Your internet-facing load balancers.
+ Restoring a volume in place from a backup, which preserves the domain join.

The transition is designed to keep your access available throughout. AMS validated it on both the multi-account landing zone (MALZ) and the single-account landing zone (SALZ), with no interruption to access when you complete the preparation described in [What AMS needs from you before the transition](#transition-ec2-access-before) while the bastion hosts are still running.

## What AMS needs from you before the transition
<a name="transition-ec2-access-before"></a>

Your Cloud Architect (CA) or Cloud Service Delivery Manager (CSDM) sends you an intake questionnaire before the transition starts. AMS uses your answers to build the new access path while the bastion hosts are still running, so that direct access works on the day the old path is removed. This is a one-time set of details. After the transition, Active Directory is yours, and you make every later change to users, groups, and access yourself. The following table lists what the questionnaire asks for and why AMS needs it.


| What the questionnaire asks for | Why AMS needs it | 
| --- | --- | 
| The on-premises IP address ranges that connect to your instances over SSH or RDP. | AMS adds these ranges to the security groups on your instances so that you can connect directly. The ranges can differ from one account to another, for example between production and development. | 
| The AD users who need permanent, account-wide access, as fully qualified names such as `john_stiles@example.com`. | AMS adds these users to the account-wide access group before handover, so that access works immediately after handover. List individual users rather than groups. On Linux, PBIS resolves each user individually and doesn't grant access through group membership alone, so every Linux user needs an entry of their own. The fully qualified name is required so that the provisioning automation resolves the correct domain when it creates the cross-forest foreign security principal (FSP). | 
| Your AD domain names. | AMS confirms which of your domains are trusted. | 
| The network path from your network to each application account VPC. | Managed application accounts in a multi-account landing zone already have this path. For customer-managed and DevMode accounts, the path has to be verified or established before the transition starts. | 

## What access looks like after the transition
<a name="transition-ec2-access-after"></a>

Once the transition is complete, the day-to-day experience is as follows.

**Connecting to an instance**  
You connect over SSH or RDP from your on-premises workstation to the instance's private IP address. You connect across your existing Direct Connect connection or VPN, and you sign in with your AD credentials. There's no request to submit, no bastion host in the path, and no time limit on the session.

**Adding a user to instance access**  
You add the user to the account-wide AD group yourself, using either ADUC on a directory administration EC2 instance or SSM Run Command. On Windows, group membership is all that's needed. On Linux, the user also needs a PBIS cell entry, because PBIS resolves Linux identities one user at a time and group membership alone doesn't resolve for SSH. Provision Linux users individually.

**Administering Active Directory**  
You manage users, groups, and Group Policy from a directory administration EC2 instance, which is a domain-joined Windows instance with the Remote Server Administration Tools (RSAT) installed. You can also use SSM Run Command against any domain-joined Windows instance. There's no AMS management host after the transition.

**Launching a new instance that joins the domain**  
New instances use a standard AWS AMI or an image of your own, together with bootstrap code that you provide. They no longer depend on AMS AMIs or the AMS bootstrap scripts. On Windows, join the domain from your bootstrap, for example with `Add-Computer` in user data, a Systems Manager State Manager association, or your existing configuration management tooling. On Linux, install the PBIS (AD Bridge) agent and join the domain from your bootstrap with `domainjoin-cli join`, so that AD sign-ins work on the new host.  
How you run that bootstrap is your choice. Common options are EC2 user data, State Manager or Run Command, a golden AMI with the agent already installed, or a configuration management tool such as Ansible, Chef, Puppet, or Terraform. AWS Directory Service seamless domain join is one of those options.

**How AMS reaches your instances**  
AMS operations connects with Session Manager, as a temporary local user. The SSM Agent has to be installed and running on any instance you want AMS to manage.

## What becomes your responsibility
<a name="transition-ec2-access-responsibility"></a>

At handover, AMS stops running the automation that manages your directory, and the management host that ran that automation is removed. The following table lists what you take over, the method to use, and where to find more information.


| Task you take over | Method | 
| --- | --- | 
| Add and remove users from AD groups. | ADUC on a directory administration EC2 instance, or SSM Run Command. For more information, see [Manage users and groups](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_manage_users_groups.html) in the *AWS Directory Service Administration Guide*. | 
| Create PBIS cell entries for new Linux users. | SSM Run Command on a domain-joined Windows instance. | 
| Write bootstrap code that joins new instances to the domain on Windows and Linux, and installs the PBIS (AD Bridge) agent on Linux. | Your own bootstrap: EC2 user data, State Manager or Run Command, a golden AMI, or your configuration management tooling. Seamless domain join is an option for the join step only. For more information, see [Join an Amazon EC2 instance to your AWS Directory Service directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_join_instance.html) in the *AWS Directory Service Administration Guide*. | 
| Configure local group membership on new instances. | Map the account-scoped Admin and Remote AD groups to new instance's administrator and logon rights through bootstrap code or an SSM association. | 
| Renew the PBIS Enterprise license when it expires. | SSM Run Command, writing the new license key to Active Directory. | 
| Launch and maintain a directory administration EC2 instance. | A domain-joined Windows instance with RSAT installed. For more information, see [Installing Active Directory Administration Tools for AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_install_ad_tools.html) in the *AWS Directory Service Administration Guide*. | 

## PBIS (AD Bridge) license
<a name="transition-ec2-access-pbis"></a>

PBIS (AD Bridge) is what lets your Linux instances authenticate SSH sign-ins against Active Directory. The Enterprise license is stored in the directory itself, in `CN=$LikewiseEnterpriseLicenses`, and every domain-joined instance reads it from there. The current license term stays active through and after the transition. It's valid until it expires on June 1, 2027, and nothing about the migration changes or shortens that. Your existing Linux instances keep authenticating with AD credentials as they do today.

Renewing the license after it expires is yours to do. By then the directory is yours, and there's no AMS management host to do it for you. To renew, write the new license key into the directory with SSM Run Command, running PowerShell on any domain-joined Windows instance, following the BeyondTrust AD Bridge documentation. If you let the license lapse, Linux AD authentication stops working. Session Manager stays available as a fallback path for your access, as described in [Frequently asked questions](#transition-ec2-access-faq), and you can move your Linux hosts to another AD integration mechanism such as winbind or SSSD instead of PBIS.

The license key AMS holds today might not entitle you to BeyondTrust support. If you need help from BeyondTrust directly, confirm with them whether you need a license key of your own.

## How access works in your landing zone
<a name="transition-ec2-access-landing-zone"></a>

AMS makes these changes for you. You act on only one item, which appears under the multi-account landing zone. AMS opens SSH on TCP port 22 and RDP on TCP port 3389 to your IP address ranges, and adds your users to the account-wide Active Directory access group, which is already mapped to the local administrators and sudoers groups on your instances. What differs by landing zone is the network path your traffic takes to the instance, and the name and scope of that access group. Your CA confirms which landing zone applies to you at intake.

**Multi-account landing zone (MALZ)**  
Currently, you reach an instance in an application account in two hops. First, you connect from your network to a bastion host in the Shared Services account. Then you connect from the bastion host to the instance. After the transition, you reach it in one hop. The connection goes over your existing Direct Connect connection or VPN, through the transit gateway, and into the application account VPC. The account-wide access group for each application account is named `All-Instance-{AccountId}-Admin`. Before the first application account moves, AMS changes the scope of that group once so that it can hold users from your own Active Directory forest. This is a one-time change that AMS makes for you, and it doesn't affect existing access for your users.  
If you have customer-managed or DevMode accounts, confirm that a network route already exists from your network to those account VPCs.

**Single-account landing zone (SALZ)**  
Your instances and your directory are in the same account and VPC, so there's no transit gateway in the path. After the transition, you connect straight to an instance over your existing Direct Connect connection or VPN, with no bastion host hop. The account-wide access group is named `vpc-{VpcId}-Admin`. It already accepts users from your own forest directly, so no scope change is needed.

**Standalone customer Active Directory account**  
Most customers don't have one of these. Skip this item unless AMS has confirmed that a standalone customer-managed Active Directory account is part of your landing zone.  
Your directory, its networking, and the one-way trust from the AMS directory in the landing zone it serves are all retained, so authentication doesn't change. Because the directory is already yours, AMS doesn't need to create an administrator account or hand over a credential. You keep using your existing AD administrator accounts.  
The preferred outcome is that AMS removes its operational baseline from the account and hands the account over to you in full. Keeping AMS Accelerate services running in the account is a secondary option, if you want them.  
Before AMS removes its operational baseline, it preserves the log and audit data in the account, including your AWS CloudTrail logs and AWS Config history, and hands the storage over to you. The encryption key protecting those logs is retained along with them, because the objects can't be read without it. Your CA gives you the specific bucket, key, and secret identifiers as part of the handover.

## How the transition runs
<a name="transition-ec2-access-sequence"></a>

The EC2 access changes run per account, and they run early: days or weeks before that account moves to AMS Accelerate. The bastion hosts remain running throughout that period, so your current access path remains available as a fallback while you test the new one. For each account, the sequence is as follows.

1. **Intake.** Your CA or CSDM sends you the questionnaire, and you return the details.

1. **Preparation.** AMS adds your IP address ranges to the security groups on your instances and adds your users to the Active Directory access group.

1. **Validation.** You confirm that you can connect directly to your instances, while the bastion hosts are still available as a fallback. AMS doesn't remove bastion hosts until you verify direct access.

1. **Transition.** After you confirm that direct access works (for MALZ, after all your application accounts are transitioned to Accelerate), AMS removes the AMS Advanced management layer from the account, including the bastion hosts and the management host, and enables AMS Accelerate.

The following table describes what happens if a step doesn't succeed.


| Scenario | What happens | 
| --- | --- | 
| Direct access doesn't work before the transition. | You and AMS fix the security group or routing first. The bastion hosts are still running, so there's no impact on your access. | 
| A user loses access after the transition. | You add them back to the account-wide AD group. | 

## Securing the new direct access path
<a name="transition-ec2-access-securing"></a>

Removing the bastion hosts moves the security boundary. Ports 22 and 3389 on your instances now accept connections from your network directly. Before, these ports accepted connections only from a bastion host inside the AMS environment. The directory administration instance you run also holds administrative capability over your directory. Apply standard AWS host and network hardening to both. The following practices matter most for this access model.
+ Keep security group ingress as narrow as possible. Allow TCP 22 and TCP 3389 only from the specific on-premises management ranges that need them, not from broad ranges, and use different ranges per account where production and development differ. For more information, see [Control traffic to your AWS resources using security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) in the *Amazon Virtual Private Cloud User Guide*. To manage those ranges as a single reusable object that you can reference from many security groups, see [Consolidate and manage network CIDR blocks with managed prefix lists](https://docs.aws.amazon.com/vpc/latest/userguide/managed-prefix-lists.html) in the *Amazon Virtual Private Cloud User Guide*.
+ Reduce what each instance exposes. Disable direct sign-in as `root` or `Administrator`, keep running services to a minimum, and close unused ports. For more information, see [Best practices for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-best-practices.html) in the *Amazon EC2 User Guide*.
+ Monitor sign-in activity. Send SSH and RDP authentication logs to Amazon CloudWatch Logs, and alarm on unauthorized attempts. For more information, see [Install the CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/installing-cloudwatch-agent-ssm.html) in the *Amazon CloudWatch Logs User Guide*. Turn on flow logs for instances that are expected to serve only administrative protocols. For more information, see [Logging IP traffic using VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) in the *Amazon Virtual Private Cloud User Guide*.
+ Require IMDSv2 on your workloads and on the directory administration instance. For more information, see [Use the Instance Metadata Service to access instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html) in the *Amazon EC2 User Guide*.
+ Treat the directory administration instance as a privileged jump host. It holds the Active Directory administrative capability that the AMS management host used to hold. Restrict who can sign in to it, keep it patched, and monitor its use.
+ Manage AWS Organizations and directory service access. The one-way trust and your existing directory links keep working through the transition. If you later turn off AD service access or remove the trust, the links that already exist stay active. However, new links can no longer be created from AWS Organizations membership. Plan any directory change of that kind explicitly.

## Frequently asked questions
<a name="transition-ec2-access-faq"></a>

These questions are grouped into three topics: keeping access during the transition, understanding what changes, and managing access afterward.

### Keeping access during the transition
<a name="transition-ec2-access-faq-keeping"></a>

**Will I lose access to my instances during the transition?**  
No. Access works continuously, provided the preparation is finished while the bastion hosts are still running.

**Can I still sign in with my AD credentials?**  
Yes. What changes is that your membership becomes permanent instead of expiring. Currently, a request for change (RFC) adds your AD user to a dynamic group that lapses after the hours you requested. After the transition, the users and groups you listed in the intake questionnaire are permanent members of the account-wide AD access group. [What changes, and what stays the same](#transition-ec2-access-changes) compares the two models, and [What access looks like after the transition](#transition-ec2-access-after) describes how you connect.

**What happens to the workflow that adds users and group memberships?**  
The RFC-based provisioning workflow (change type `ct-1dmlg9g1l91h6`) isn't available after the transition. Building your own workflow to add and remove users from AD groups becomes your responsibility. It can range from administering users by hand with ADUC on a directory administration EC2 instance to automating it with an SSM Run Command document that runs AD PowerShell operations. For more information, see [Manage users and groups](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_manage_users_groups.html) in the *AWS Directory Service Administration Guide*.

### Understanding what changes during the transition
<a name="transition-ec2-access-faq-changes"></a>

**What happens to the bastion hosts?**  
AMS terminates them. You connect to your instances directly from your on-premises network over your Direct Connect connection or VPN, with no hop in between.

**What happens to the management host?**  
AMS terminates it. To administer Active Directory afterward, launch a directory administration EC2 instance, or use SSM Run Command against any domain-joined Windows instance.

**How does AMS access my instances for operations after the transition?**  
Through Session Manager, as a temporary local user. AMS doesn't depend on Active Directory for its own access, and no bastion host is involved. The SSM Agent has to be installed and running on an instance for AMS operations access to work.

### Managing access after the transition
<a name="transition-ec2-access-faq-managing"></a>

**How do I add new users to instance access?**  
Add the user to the account-wide AD group as a foreign security principal, using ADUC on a directory administration EC2 instance or SSM Run Command.

**Does SSH with AD credentials still work on Linux?**  
Yes, for as long as the PBIS license is valid. A new user also needs a PBIS cell entry, which you create with SSM Run Command.

**What about my internet-facing load balancers?**  
They aren't affected. They stay in place regardless of the bastion host changes.

**What happens if I restore an instance from a backup?**  
Restoring a volume in place preserves the domain join.

**What do I need to provide before the transition starts?**  
Your on-premises IP address ranges, the list of users and groups that need account-wide access, and, if it doesn't already exist, a network path from your network to your application accounts.

**What happens to the AMS bootstrap script and PBIS on my existing instances?**  
Both stay in place and keep working on every existing instance, as listed in [What changes, and what stays the same](#transition-ec2-access-changes). The bootstrap script doesn't run again after first boot.

**What about new instances I launch after the transition?**  
New instances use standard AWS AMIs or your own custom AMIs, and you're responsible for three things:  
+ Joining the instance to the domain.
+ Configuring local group membership, with GPO restricted groups or an SSM association.
+ Installing PBIS, if you want AD authentication on Linux. This one is optional and it's your choice.
AMS AMIs with PBIS and bootstrap logic preinstalled aren't used after the transition, because they depend on the AMS Advanced change management system, which isn't part of AMS Accelerate. For more information, see [Join an Amazon EC2 instance to your AWS Directory Service directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_join_instance.html) in the *AWS Directory Service Administration Guide*.

**We are adding a brand-new account after the transition. Can instances in it be domain joined right away?**  
Not right away. A newly vended account contains none of the objects that domain join depends on. The automation that used to create them ran on the management host, which is gone. Before the first join, the account needs the following:  
+ A network path from its VPC to the directory's domain controllers, and a return path.
+ DNS resolution for the AD domain, which means a DHCP option set and, if your environment uses them, resolver-rule associations.
+ A per-account organizational unit (OU) with at least one child OU for computer objects.
+ A `join-{AccountId}` service account with delegated computer-object rights on that OU.
+ The account-wide access groups, with your users added.
+ The join credential readable from the account, and an instance profile that can read it.
You do this work once for each account. Accounts that were already in your landing zone at the transition keep the objects AMS created for them and don't need this.

**If I decommission Active Directory, how do I connect to an instance, and how do I remove the old PBIS and AMS bootstrap scripts?**  
Use Session Manager to connect, either interactively or by port-forwarding SSH and RDP. To remove the old mechanism, leave the domain with `domainjoin-cli leave`, uninstall the `pbis-enterprise` package, remove the PBIS `sudoers` drop-in files, and delete the AMS bootstrap script artifacts, which no longer run after first boot.

**How and when is the PBIS (AD Bridge) Enterprise license renewed?**  
The Enterprise license is stored in Active Directory and read by every domain-joined instance. The current term expires on June 1, 2027. After the transition, you renew it yourself, following the BeyondTrust AD Bridge documentation. For more information, see [PBIS (AD Bridge) license](#transition-ec2-access-pbis).

**What happens to shared AMS AMIs, and how does it affect EC2 access?**  
AMI sharing is governed by the broader AMS Advanced end of support. Two points matter for access:  
+ For new workloads, use a standard AWS AMI with your own bootstrap code to join the domain and to install and configure PBIS, or an alternative such as winbind or SSSD on Linux.
+ For existing workloads, plan to move off the AMS shared AMIs after you transition to AMS Accelerate. AMS stops sharing updated AMIs, and eventually unshares the older ones, tentatively starting June 30, 2028.

**Can existing EC2 instances that were launched from AMS-created AMIs keep running as-is after we move to Accelerate? Are there any dependencies, restrictions, or actions required because of their underlying AMS AMI?**  
Yes, they keep running exactly as they are, and you don't need to do anything to keep them running.  
An AMI is a launch-time template only. Once an instance is running, it has no runtime dependency on that AMI continuing to exist, continuing to be shared with your account, or continuing to be updated. You can stop, start, and reboot the instance as usual. AMS stopping AMI publication, and eventually unsharing the older AMIs (tentatively starting June 30, 2028), doesn't stop or degrade a running instance, and there's no forced relaunch or reimage.  
The AMI ID still matters at launch time. Auto Scaling groups, launch templates, and launch configurations that reference an AMS AMI ID fail to launch new or replacement instances once that AMI is unshared or deregistered. Before AMS unshares the AMIs, repoint those Auto Scaling groups and launch templates to an AMI of your own, either a standard AWS AMI plus your bootstrap or your own hardened build. Running instances aren't affected. Only scale-out and instance replacement depend on the AMI.  
What's already installed on those instances is unchanged by the migration and keeps working:  
+ The AMS bootstrap script stays on the instance. It doesn't run again after first boot.
+ PBIS (AD Bridge) and the domain join persist and keep working while the PBIS Enterprise license is valid, which is until June 1, 2027. You renew it after the transition, as described in [PBIS (AD Bridge) license](#transition-ec2-access-pbis). Restoring a volume in place from a backup preserves the domain join.
+ The AMS agents, including the SSM Agent, stay installed. Keep the SSM Agent, because it's how AMS operations reaches the instance, and it's a potential fallback path for your own access.
If you no longer want the AMS scaffolding on an existing instance, you can remove the AMS bootstrap scripts and PBIS. This is optional, and it isn't required for the instance to keep running.  
Plan for the following:  
+ Move any Auto Scaling groups and launch templates off AMS AMI IDs before AMS unshares them.
+ Take over patching, endpoint protection, and monitoring through AMS Accelerate.