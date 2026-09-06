

# Advanced FAQ
<a name="drs-advancved-faq"></a>

## Does AWS DRS support Nutanix?
<a name="drs-support-Nutanix"></a>

Nutanix hypervisor is supported along with other hypervisor vendors. The AWS Replication Agent is installed on the virtual machine (VM) and performs block level replication. In addition, the client ISO is booted for failback on the same VM itself.

## Does AWS DRS support VMware vSphere?
<a name="drs-support-vmware"></a>

VMware vSphere is supported (both on-premises as well as VMware on AWS). Examples of detailed walkthroughs: [Disaster recovery for VMware Cloud on AWS using AWS Elastic Disaster Recovery.](https://aws.amazon.com/blogs/storage/disaster-recovery-for-vmware-cloud-on-aws-using-aws-elastic-disaster-recovery/) [Performing a failback with the DRS Mass Failback Automation client.](https://docs.aws.amazon.com/drs/latest/userguide/failback-failover-drsfa.html)

## Does AWS DRS support Microsoft Hyper-V?
<a name="drs-support-hyper-v"></a>

Both Hyper-V and Microsoft Azure are supported. The AWS Replication Agent installation and replication follows the same process described in [Adding source servers.](https://docs.aws.amazon.com/drs/latest/userguide/adding-servers.html) For failback to Azure, review the [Building a disaster recovery site on AWS for workloads on Microsoft Azure](https://aws.amazon.com/blogs/storage/building-a-disaster-recovery-site-on-aws-for-workloads-on-microsoft-azure/) blog post.