

# Migrate servers
<a name="transform-vmware-migrate-servers"></a>

AWS Transform automates the rehosting of your servers to Amazon EC2 at scale. The AI-powered agent guides you through each migration wave, from inventory validation and replication agent deployment through testing and final cutover. AWS Transform handles the orchestration across hundreds of servers while you maintain control over configuration and approval decisions. Internally, AWS Transform uses AWS Transform MGN (MGN) for data replication. For more information about MGN, see [What is AWS Transform MGN?](https://docs.aws.amazon.com/mgn/latest/ug/what-is-mgn.html) in the *MGN User Guide*.

You can migrate servers from virtually any source environment, including on-premises data centers, other cloud providers, or other AWS Regions. AWS Transform supports both physical servers and virtual servers running on VMware, Hyper-V, KVM, or other virtualization platforms. The source infrastructure and hypervisor are not important as long as the source operating system is supported.

Server migration has the following parts:
+ [Prerequisites](transform-vmware-ms-prerequisites.md) – Make sure your target accounts, network infrastructure, and inventory file are in place.
+ [Configure Migration Defaults](transform-vmware-ms-migration-defaults.md) – Configure how instances are launched and how replication is set up, including post-launch actions. AWS Transform provides intelligent defaults so you can get started quickly.
+ [Wave execution](transform-vmware-ms-wave-execution.md) – Migrate your servers wave by wave, from wave setup through testing and cutover.
+ [Server lifecycle states](transform-vmware-ms-server-lifecycle.md) – Track the state of each server as it moves through the migration.

## Deployment approvals
<a name="transform-vmware-ms-approvals"></a>

AWS Transform includes built-in approval workflows to ensure production changes go through your organization's review process. When an operation requires approval, AWS Transform routes the request to authorized approvers through the Approvals tab. Only users with the Admin role in AWS Transform can approve deployment requests. Deployments proceed only after receiving confirmation.