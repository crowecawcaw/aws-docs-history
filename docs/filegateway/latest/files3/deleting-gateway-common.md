# Deleting your gateway and removing associated

resources

If you don't plan to continue using your gateway, consider deleting the gateway and its
associated resources. Removing resources avoids incurring charges for resources you don't
plan to continue using and helps reduce your monthly bill.

When you delete a gateway, it no longer appears on the AWS Storage Gateway Management Console and
its file share connections are closed. The procedure for deleting a gateway is the same
for all gateway types; however, depending on the type of gateway you want to delete and the
host it is deployed on, you follow specific instructions to remove associated resources.

You can delete a gateway using the Storage Gateway console or programmatically. You can find
information following about how to delete a gateway using the Storage Gateway console. If you
want to programmatically delete your gateway, see _[AWS Storage Gateway API Reference](../../../storagegateway/latest/APIReference.md "../../../storagegateway/latest/APIReference.md")._

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
as Amazon S3 bucket and Amazon EC2 instances persist. You can remove the gateway Amazon EC2
instance after the file gateway is removed. If you don't
need the data in Amazon S3 buckets associated with the file shares, you can choose to
remove your Amazon S3 buckets. For instructions, see [Deleting your bucket](../../../AmazonS3/latest/userguide/deleting-object-bucket.md#clean-up-delete-bucket "../../../AmazonS3/latest/userguide/deleting-object-bucket.md#clean-up-delete-bucket").
