

# Permissions and IAM for 1:1 NAT in AWS Cloud WAN
<a name="cloudwan-nat-permissions"></a>

Only the core network owner can view or change the NAT configuration of a core network attachment. This applies to every attachment in the core network, including attachments owned by other accounts when the core network is shared through AWS RAM. Attachment owners can't view or change NAT configuration.

Attachment owners in other accounts do receive the NAT CloudWatch metrics for their attachments.

## IAM permissions
<a name="cloudwan-nat-permissions-iam"></a>


| Action | Purpose | 
| --- | --- | 
| networkmanager:UpdateAttachmentNatConfiguration | Enable or disable NAT, set NAT system route support, and set NAT rules. Also required to include a NAT configuration when you create an attachment. | 
| networkmanager:ListAttachmentNatConfigurations | View NAT configuration for one or more attachments. | 

Both actions authorize against the attachment resource: `arn:aws:networkmanager::{{account-id}}:attachment/{{attachment-id}}`. To restrict which attachments a principal can manage, specify attachment ARNs or use tag-based conditions.

## Creating an attachment with NAT configuration
<a name="cloudwan-nat-permissions-create"></a>

If you include a NAT configuration when you create an attachment, for example with `CreateVpcAttachment`, you need permission for both the create action and `networkmanager:UpdateAttachmentNatConfiguration`. If you have permission for the create action but not for `UpdateAttachmentNatConfiguration`, a create request that includes a NAT configuration is denied. A create request without a NAT configuration needs only the create permission.

The following example policy lets a principal manage NAT only on attachments tagged `environment=prod`:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "networkmanager:UpdateAttachmentNatConfiguration",
        "networkmanager:ListAttachmentNatConfigurations"
      ],
      "Resource": "arn:aws:networkmanager::*:attachment/*",
      "Condition": {
        "StringEquals": { "aws:ResourceTag/environment": "prod" }
      }
    }
  ]
}
```

The following example policy lets a principal create VPC attachments with a NAT configuration:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "networkmanager:CreateVpcAttachment",
        "networkmanager:UpdateAttachmentNatConfiguration"
      ],
      "Resource": "*"
    }
  ]
}
```

## Logging
<a name="cloudwan-nat-permissions-logging"></a>

AWS CloudTrail logs both NAT actions in the US West (Oregon) AWS Region, like other Network Manager API calls. CloudTrail logs a create request that includes a NAT configuration as the create action.