# Domain-Joined WorkSpaces Applications Streaming Instances

SAML 2.0-based user federation is required for application streaming from
domain-joined Always-On and On-Demand fleets. You cannot launch sessions to
domain-joined instances by using [CreateStreamingURL](../APIReference/API_CreateStreamingURL.md "../APIReference/API_CreateStreamingURL.md") or the WorkSpaces Applications
user pool.

Also, you must use an image that supports joining image builders and fleets to an
Active Directory domain. All public images published on or after July 24, 2017
support joining an Active Directory domain. For more information, see [WorkSpaces Applications Base Image and Managed Image Update Release Notes](base-image-version-history.md "base-image-version-history.md") and [Tutorial: Setting Up Active Directory](active-directory-directory-setup.md "active-directory-directory-setup.md").

###### Note

You can join Always-On and On-Demand fleet streaming instances to an
Active Directory domain. Supported operating systems include Windows, Red Hat
Enterprise Linux, and Rocky Linux.
