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

Volume Gateway Deployed on a VM

If the gateway you want to delete are deployed on a virtual machine (VM), we
suggest that you take the following actions to clean up resources:

- Delete the gateway. For instructions, see [Deleting Your Gateway by Using the Storage Gateway
  Console](#delete-gateway-procedure "#delete-gateway-procedure").
- Delete all Amazon EBS snapshots you don't need. For instructions, see [Deleting an Amazon EBS
  Snapshot](../../../AWSEC2/latest/UserGuide/ebs-deleting-snapshot.md "../../../AWSEC2/latest/UserGuide/ebs-deleting-snapshot.md") in the _Amazon EC2 User Guide_.

## Removing Resources from a Gateway Deployed on an

Amazon EC2 Instance

If you want to delete a gateway that you deployed on an Amazon EC2 instance, we recommend
that you clean up the AWS resources that were used with the gateway, specifically the
Amazon EC2 instance, any Amazon EBS volumes, and also tapes if you deployed a Tape Gateway. Doing
so helps avoid unintended usage charges.

### Removing Resources from Your Cached Volumes

Deployed on Amazon EC2

If you deployed a gateway with cached volumes on EC2, we suggest that you take the
following actions to delete your gateway and clean up its resources:

1. In the Storage Gateway console, delete the gateway as shown in [Deleting Your Gateway by Using the Storage Gateway
   Console](#delete-gateway-procedure "#delete-gateway-procedure").
2. In the Amazon EC2 console, stop your EC2 instance if you plan on using the
   instance again. Otherwise, terminate the instance. If you plan on deleting
   volumes, make note of the block devices that are attached to the instance
   and the devices' identifiers before terminating the instance. You will need
   these to identify the volumes you want to delete.
3. In the Amazon EC2 console, remove all Amazon EBS volumes that are attached to the
   instance if you don't plan on using them again. For more information, see
   [Clean Up Your
   Instance and Volume](../../../AWSEC2/latest/UserGuide/ec2-clean-up-your-instance.md "../../../AWSEC2/latest/UserGuide/ec2-clean-up-your-instance.md") in the
   _Amazon EC2 User Guide_.
