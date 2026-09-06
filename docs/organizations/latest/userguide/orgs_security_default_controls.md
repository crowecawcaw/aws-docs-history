

# Default security controls in AWS Organizations
<a name="orgs_security_default_controls"></a>

Managing security in a multi-account environment requires consistent governance from the start. When you create an organization using the AWS Organizations console, the service automatically applies security controls to protect your organization from common risks. These controls establish an AWS-recommended security baseline from the moment you create your organization.

**Important**  
These controls apply only to organizations created through the AWS Organizations console after July 10, 2026, and don't affect existing organizations. Organizations doesn't currently support these controls when you create an organization using the AWS Command Line Interface (AWS CLI), AWS SDKs, or CloudFormation. If you use the `CreateOrganization` API directly or want to add these controls to an existing organization, you must configure them manually. For more information, see [Enabling a policy type](enable-policy-type.md), [Creating organization policies with AWS Organizations](orgs_policies_create.md), and [Attaching organization policies with AWS Organizations](orgs_policies_attach.md).

Organizations turns on service control policies (SCPs) and attaches an SCP to the root that denies both the `organizations:LeaveOrganization` and `account:CloseAccount` actions for all member accounts. Member accounts can't leave the organization or close without action from the management account or a delegated administrator.

The following policy shows the SCP that denies member accounts from leaving the organization or closing their accounts:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyLeaveOrganizationAndCloseAccount",
            "Effect": "Deny",
            "Action": [
                "organizations:LeaveOrganization",
                "account:CloseAccount"
            ],
            "Resource": "*"
        }
    ]
}
```

You can modify this SCP or attach it to different targets. We recommend keeping it attached at the root to protect all member accounts.