

# Attachments in AWS Cloud WAN
<a name="cloudwan-create-attachment"></a>

You can work with core network attachments using the Amazon VPC Console or the command line or API. 

Attachment states can be one of the following. Attachment states appear on the Attachments page of the AWS Cloud WAN console.
+ **Creating** — Creation of an attachment is in process.
+ **Deleting** — Deletion of an attachment is in process.
+ **Pending network update** — Waiting for the connection of attachments to the core network.
+ **Pending tag acceptance** — Waiting for the core network owner to review the tag change for an attachment.
+ **Pending attachment acceptance** — Waiting for the core network owner to accept or reject an attachment.
+ **Rejected** — The core network owner rejected the attachment.
+ **Available** — The attachment is fully functional.
+ **Failed** — The attachment failed to attach to the core network. For example, this might be due to an input error or a service linked role issue.

The following are the supported core network attachment types. 
+ Direct Connect
+ Connect

  You can also create a Connect peer through the Network Manager console. 
+ VPC
+ Transit gateway route table

You can create an attachment using either using the Network Manager console or by using the command line or API.

**Topics**
+ [Connect attachments and Connect peers](cloudwan-connect-attachment.md)
+ [Direct Connect gateway attachments](cloudwan-dxattach-about.md)
+ [VPC attachments](cloudwan-vpc-attachment.md)
+ [Site-to-Site VPN attachments in Cloud WAN](cloudwan-s2s-vpn-attachment.md)
+ [Transit gateway route table attachments](cloudwan-tgw-attachment.md)
+ [Accept or reject a core network attachment](cloudwan-attachments-acceptance.md)
+ [Delete an attachment](cloudwan-attachments-deleting.md)