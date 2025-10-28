# Deleting your gateway and removing associated

resources

If you don't plan to continue using your gateway, consider deleting the gateway and its
associated resources. Removing resources avoids incurring charges for resources you don't
plan to continue using and helps reduce your monthly bill.

When you delete a gateway, it no longer appears on the AWS Storage Gateway Management Console and
its iSCSI connection to the initiator is closed. The procedure for deleting a gateway is the
same for all gateway types; however, depending on the type of gateway you want to delete and
the host it is deployed on, you follow specific instructions to remove associated
resources.

###### Note

When you delete a Tape Gateway, any tapes that are currently in the
`AVAILABLE` status are also deleted, and any data on those tapes is lost.
If you want to retain data from tapes that are being used by a gateway that you want to
delete, you must archive the tapes before you delete the gateway. For more information,
see [Archiving Virtual Tapes](archiving-tapes-vtl.md "archiving-tapes-vtl.md").

You can delete a gateway using the Storage Gateway console or programmatically. You can find
information following about how to delete a gateway using the Storage Gateway console. If you
want to programmatically delete your gateway, see _[AWS Storage Gateway API Reference](../APIReference.md "../APIReference.md")._

###### Topics

- [Deleting Your Gateway by Using the Storage Gateway
  Console](#delete-gateway-procedure "#delete-gateway-procedure")
- [Removing Resources from a Gateway Deployed
  On-Premises](#remove-resources-onpremise "#remove-resources-onpremise")
- [Removing Resources from a Gateway Deployed on an
  Amazon EC2 Instance](#EC2GatewayCleanup "#EC2GatewayCleanup")

## Deleting Your Gateway by Using the Storage Gateway

Console

The procedure for deleting a gateway is the same for all gateway types. However,
depending on the type of gateway you want to delete and the host the gateway is deployed
on, you might have to perform additional tasks to remove resources associated with the
gateway. Removing these resources helps you avoid paying for resources you don't plan to
use.

###### Note

For gateways deployed on an Amazon EC2 instance, the instance continues to exist until
you delete it.

For gateways deployed on a virtual machine (VM), after you delete your gateway the
gateway VM still exists in your virtualization environment. To remove the VM, use
the VMware vSphere client, Microsoft Hyper-V Manager, or Linux Kernel-based Virtual
Machine (KVM) client to connect to the host and remove the VM. Note that you can't
reuse the deleted gateway's VM to activate a new gateway.

###### To delete a gateway

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. Choose **Gateways**, then select one or more gateways to
   delete.
3. For **Actions**, choose **Delete gateway**.
   The confirmation dialog box appears.

###### Warning

Before you do this step, make sure that there are no applications
currently writing to the gateway's volumes. If you delete the gateway while
it is in use, data loss can occur. When a gateway is deleted, there is no
way to get it back. 4. Verify that you want to delete the specified gateways, then type the word
_delete_ in the confirmation box, and
choose **Delete**. 5. (Optional) If you want to provide feedback about your deleted gateway,
complete the feedback dialog box, then choose **Submit**.
Otherwise, choose **Skip**.

###### Important

You no longer pay software charges after you delete a gateway, but resources such
as virtual tapes, Amazon Elastic Block Store (Amazon EBS) snapshots, and Amazon EC2 instances persist. You will
continue to be billed for these resources. You can choose to remove Amazon EC2 instances
and Amazon EBS snapshots by canceling your Amazon EC2 subscription. If you want to keep your
Amazon EC2 subscription, you can delete your Amazon EBS snapshots using the Amazon EC2
console.

## Removing Resources from a Gateway Deployed

On-Premises

You can use the instructions following to remove resources from a gateway that is
deployed on-premises.

### Removing Resources from a

Tape Gateway Deployed on a VM

When you delete a gateway–virtual tape library (VTL), you perform
additional cleanup steps before and after you delete the gateway. These additional
steps help you remove resources you don't need so you don't continue to pay for
them.

If the Tape Gateway you want to delete is deployed on a virtual machine (VM), we
suggest that you take the following actions to clean up resources.

###### Important

Before you delete a Tape Gateway, you must cancel all tape retrieval
operations and eject all retrieved tapes.

After you have deleted the Tape Gateway, you must remove any resources
associated with the Tape Gateway that you don't need to avoid paying for those
resources.

When you delete a Tape Gateway, you can encounter one of two scenarios.

- **The Tape Gateway is connected
  to AWS** – If the Tape Gateway is
  connected to AWS and you delete the gateway, the iSCSI targets associated
  with the gateway (that is, the virtual tape drives and media changer) will
  no longer be available.
- **The Tape Gateway is not
  connected to AWS** – If the Tape Gateway
  is not connected to AWS, for example if the underlying VM is turned off or
  your network is down, then you cannot delete the gateway. If you attempt to
  do so, after your environment is back up and running you might have a
  Tape Gateway running on-premises with available iSCSI targets. However, no
  Tape Gateway data will be uploaded to, or downloaded from, AWS.

If the Tape Gateway you want to delete is not functioning, you must first
deactivate it before you delete it, as described following:

- To delete tapes that have the RETRIEVED status from the library, eject the
  tape using your backup software. For instructions, see [Archiving the Tape](backup_netbackup-vtl.md#GettingStarted-archiving-tapes-vtl "backup_netbackup-vtl.md#GettingStarted-archiving-tapes-vtl").

After deactivating the Tape Gateway and deleting tapes, you can delete the
Tape Gateway. For instructions on how to delete a gateway, see [Deleting Your Gateway by Using the Storage Gateway
Console](#delete-gateway-procedure "#delete-gateway-procedure").

If you have tapes archived, those tapes remain and you continue to pay for storage
until you delete them. For instruction on how to delete tapes from a archive. see
[Deleting virtual tapes from your
Tape Gateway](deleting-tapes-vtl.md "deleting-tapes-vtl.md").

###### Important

You are charged for a minimum of 90 days storage for virtual tapes in a
archive. If you retrieve a virtual tape that has been stored in the archive for
less than 90 days, you are still charged for 90 days storage.

## Removing Resources from a Gateway Deployed on an

Amazon EC2 Instance

If you want to delete a gateway that you deployed on an Amazon EC2 instance, we recommend
that you clean up the AWS resources that were used with the gateway, specifically the
Amazon EC2 instance, any Amazon EBS volumes, and also tapes if you deployed a Tape Gateway. Doing
so helps avoid unintended usage charges.

### Removing Resources from Your Tape Gateway Deployed

on Amazon EC2

If you deployed a Tape Gateway, we suggest that you take the following actions to
delete your gateway and clean up its resources:

1. Delete all virtual tapes that you have retrieved to your Tape Gateway.
   For more information, see [Deleting virtual tapes from your
   Tape Gateway](deleting-tapes-vtl.md "deleting-tapes-vtl.md").
2. Delete all virtual tapes from the tape library. For more information, see
   [Deleting virtual tapes from your
   Tape Gateway](deleting-tapes-vtl.md "deleting-tapes-vtl.md").
3. Delete the Tape Gateway. For more information, see [Deleting Your Gateway by Using the Storage Gateway
   Console](#delete-gateway-procedure "#delete-gateway-procedure").
4. Terminate all Amazon EC2 instances, and delete all Amazon EBS volumes. For more
   information, see [Clean Up Your Instance and Volume](../../../AWSEC2/latest/UserGuide/ec2-clean-up-your-instance.md "../../../AWSEC2/latest/UserGuide/ec2-clean-up-your-instance.md") in the
   _Amazon EC2 User Guide_.
5. Delete all archived virtual tapes. For more information, see [Deleting virtual tapes from your
   Tape Gateway](deleting-tapes-vtl.md "deleting-tapes-vtl.md").

###### Important

You are charged for a minimum of 90 days storage for virtual tapes in
the archive. If you retrieve a virtual tape that has been stored in the
archive for less than 90 days, you are still charged for 90 days
storage.
