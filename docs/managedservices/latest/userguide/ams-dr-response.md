# Disaster recovery response

In addition to the options described in the following sections, it is good for you to know what steps to take to
initiate a disaster recovery (DR) with AMS.

If you experience a disaster and need to initiate a recovery, follow these general guidelines:

1. Open a **High** priority incident with the **Availability** category.
   AMS will open a conference bridge and invite your team to join.
2. Know the list of resources you need to recover.
3. Know the target landing zone (LZ) you need to recover to (for example, the same account, different AZ
   or different account and different region).
4. Submit recover requests for each resource in the target landing zone.
   Follow your existing DR plan or see the options in the following section
   (for example, [Disaster protection for EC2 with EBS snapshots on AMS](ams-disaster-recovery.md#ams-dr-ebs-snapshots "ams-disaster-recovery.md#ams-dr-ebs-snapshots"), or
   [Disaster protection for EC2 with Elastic Disaster Recovery on AMS](ams-disaster-recovery.md#ams-dr-ebs-snapshots-ce "ams-disaster-recovery.md#ams-dr-ebs-snapshots-ce")).
5. Restore the application functionality and use AMS assistance to troubleshoot infrastructure-related
   issues.
   AMS can help you with preparing for this event and with creating a DR plan for your organization to cover
   these questions. For more details, contact your cloud service delivery manager (CSDM) or cloud architect (CA).
