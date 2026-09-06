

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Framework sharing concepts and terminology
<a name="share-custom-framework-concepts-and-terminology"></a>



If you learn about the following key concepts, you can get more out of the AWS Audit Manager custom framework sharing feature.

## Key points
<a name="share-custom-framework-concepts-and-terminology-key-points"></a>

**Sender**  
This is the creator of a share request and the AWS account where the custom framework exists. Senders can share custom frameworks with any AWS account. Or, they replicate a custom framework to any supported AWS Region under their own account. 

**Recipient**  
This is the consumer of the shared framework. Recipients can either accept or decline a share request from a sender.   
A recipient can be a delegated administrator account. However, you can't share custom frameworks with an AWS Organizations management account.

**Framework eligibility**  
You can only share custom frameworks. By default, standard frameworks are already present in all AWS accounts and AWS Regions where AWS Audit Manager is enabled. In addition, the custom frameworks that you share must not contain sensitive data. This includes data found within the framework itself, its control sets, and any of the custom controls that are part of the custom framework.   
Some of the standard frameworks that are offered by AWS Audit Manager contain copyrighted material that’s subject to license agreements. Custom frameworks might contain content that’s derived from these frameworks. You may not share a custom framework that's derived from a standard framework if the standard framework is designated as not eligible for sharing by AWS, unless you have obtained permission to do so from the owner of the standard framework.   
To learn which standard frameworks are eligible for sharing, refer to the following table.     
[See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/share-custom-framework-concepts-and-terminology.html)

**Share request**  
To share a custom framework, you create a *share request*. The share request specifies a recipient and notifies them that a custom framework is available. Recipients have 120 days to respond to a share request by accepting or declining. If no action is taken in 120 days, the share request expires and the recipient loses the ability to add the custom framework to their framework library. Senders and recipients can view and take action on share requests from the share requests page of the framework library.

**Share request status**  
Share requests can have any of the following statuses.      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/share-custom-framework-concepts-and-terminology.html)

**Share request notifications**  
Audit Manager notifies recipients when they receive a share request. Both recipients and senders receive a notification when a share request is due to expire sometime in the next 30 days.  
+ For recipients, a blue notification dot appears next to received requests with an **Active** or **Expiring** status. The recipient can resolve the notification by accepting or declining the share request.
+ For senders, a blue notification dot appears next to sent requests with an **Expiring** status. The notification is resolved when the recipient accepts or declines the request. Otherwise, it's resolved when the request expires. Additionally, the sender can resolve the notification by revoking the share request.

**Sender ownership**  
Senders maintain full access over the custom frameworks that they share. They can cancel active share requests at any time by [revoking the share request](https://docs.aws.amazon.com/audit-manager/latest/userguide/framework-sharing.html#framework-sharing-step-4) before it expires. However, after a recipient accepts a share request, the sender can no longer revoke the recipient’s access to that custom framework. This is because when the recipient accepts the request, Audit Manager creates an independent copy of the custom framework in the recipient’s framework library.   
In addition to replicating the sender’s custom framework, Audit Manager also replicates any custom control sets and custom controls that are part of that framework. However, Audit Manager doesn’t replicate any tags that are attached to the custom framework.

**Recipient ownership**  
Recipients have full access over the custom frameworks that they accept. When recipient accepts the request, Audit Manager replicates the custom framework to the custom frameworks tab of their framework library. Recipients can then manage the shared custom framework in the same way as any other custom framework. Recipients can share the custom frameworks that they receive from other senders. Recipients can’t block senders from sending share requests.

**Shared framework expiration**  
When a sender creates a share request, Audit Manager sets the request to expire after 120 days. Recipients can accept and gain access to the shared framework before the request expires. If a recipient doesn’t accept during this time, the share request expires. After this point, a record of the expired share request remains in their history. Snapshots of expired shared frameworks are archived to an S3 bucket with a one-year TTL for audit purposes.   
Senders can choose to [revoke a share request](https://docs.aws.amazon.com/audit-manager/latest/userguide/framework-sharing.html#framework-sharing-step-4) at any time before it’s due to expire.

**Shared framework data storage and backup**  
When you create a share request, Audit Manager stores a snapshot of your custom framework in the US East (N. Virginia) AWS Region. Audit Manager also stores a backup of the same snapshot in the US West (Oregon) AWS Region.  
Audit Manager deletes the snapshot and the backup snapshot when one of the following events occurs:  
+ The sender revokes the share request.
+ The recipient declines the share request.
+ The recipient encounters an error and doesn't successfully accept the share request.
+ The share request expires before the recipient responds to the request.
When a sender [resends a share request](https://docs.aws.amazon.com/audit-manager/latest/userguide/framework-sharing.html#framework-sharing-resend), the snapshot is replaced with an updated version that corresponds with the latest version of the custom framework.   
When a recipient accepts a share request, the snapshot is replicated into their AWS account under the AWS Region that was specified in the share request. 

**Shared framework versioning**  
When you share a custom framework, Audit Manager creates an independent copy of that framework in the specified AWS account and Region. This means that you should keep in mind the following points:  
+ The shared framework that a recipient accepts is a snapshot of the framework at the time of the share request creation. If you update the original custom framework after sending a share request, the request isn't automatically updated. To share the latest version of the updated framework, you can [resend the share request](https://docs.aws.amazon.com/audit-manager/latest/userguide/framework-sharing.html#framework-sharing-resend). The expiration date of this new snapshot is 120 days from the re-share date.
+ When you share a custom framework with another AWS account and then delete it from your framework library, the shared custom framework remains in the recipient's framework library.
+ When you share a custom framework to another AWS Region under your account and then delete that custom framework in the first AWS Region, the custom framework remains in the second Region.
+ When you delete a shared custom framework after accepting it, any custom controls that were replicated as part of the custom framework remain in your control library.

## Additional resources
<a name="share-custom-framework-concepts-and-terminology-additional-resources"></a>
+ [Sending request to share a custom framework in AWS Audit Manager](framework-sharing.md)
+ [Responding to share requests in AWS Audit Manager](responding-to-shared-framework-requests.md)
+ [Deleting share requests in AWS Audit Manager](deleting-shared-framework-requests.md)
+ [Troubleshooting framework issues](framework-issues.md)