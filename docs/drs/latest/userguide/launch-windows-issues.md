

# Windows post-launch issues
<a name="launch-windows-issues"></a>

This topic covers Windows-specific issues that can occur after you launch drill or recovery instances with AWS Elastic Disaster Recovery.

**Topics**
+ [Windows license activation failure](#Windows-License-Activation)
+ [Windows drive letter reassignment](#Windows-Drive-Changes)
+ [Windows Dynamic Disk shows as Foreign](#Windows-Dynamic-Disk)

## Windows license activation failure
<a name="Windows-License-Activation"></a>

**Cause:** AWS Elastic Disaster Recovery converts Windows OS licenses to AWS licenses and activates them against AWS KMS. Activation can fail if the recovery instance cannot reach the AWS KMS endpoint.

**Resolution:** Follow the AWS guide to resolve this issue: [Troubleshooting Windows activation](https://aws.amazon.com/premiumsupport/knowledge-center/windows-activation-fails/).

**Important**  
During failback, AWS Elastic Disaster Recovery does not have access to customer licenses and cannot activate them. After failback completes, activate licenses manually or by using post-launch scripts.

## Windows drive letter reassignment
<a name="Windows-Drive-Changes"></a>

**Symptom:** Drive letters change after launch (for example, D: becomes E:).

**Cause:** Windows reconfigures drive letter assignments when a machine starts on new infrastructure, especially if the source server had drive letters mapped to disks that were not replicated (such as network drives or excluded volumes).

**Resolution:** Remap the drive letters on the recovery instance after launch by using **Disk Management** (diskmgmt.msc) or diskpart. This is a one-time post-launch step.

## Windows Dynamic Disk shows as Foreign
<a name="Windows-Dynamic-Disk"></a>

**Symptom:** After launch, a Dynamic Disk shows status `Foreign` in **Disk Management**.

**Cause:** Moving a Windows Dynamic Disk between computers changes the disk status to Foreign. This is normal Windows behavior when disks are presented to a different machine.

**Resolution:** Import the foreign disk by using **Disk Management**:

1. Open diskmgmt.msc.

1. Right-click the disk showing `Foreign` and choose **Import Foreign Disks**.

For more information, see [Microsoft Dynamic Disk troubleshooting](https://docs.microsoft.com/en-us/windows-server/storage/disk-management/troubleshooting-disk-management#a-dynamic-disks-status-is-foreign).