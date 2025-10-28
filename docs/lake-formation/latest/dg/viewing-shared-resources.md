# Accessing and viewing shared Data Catalog tables and

databases

For the data lake administrator and for principals who have been granted permissions,
resources that are shared with your AWS account appear in the Data Catalog as if they were resources
in your account. The console displays the account that owns the resource.

You can view resources that are shared with your account by using the Lake Formation console. You can
also use the AWS Resource Access Manager (AWS RAM) console to view both resources that are shared with your account
and resources that you've shared with other AWS accounts by using the named resource
method.

###### Important

When someone uses the named resource method to grant cross-account permissions on a Data Catalog
resource to your account or AWS organization, Lake Formation uses the AWS Resource Access Manager (AWS RAM) service to share
the resource. If your account is in the same AWS organization as the granting account, the
shared resource is available to you immediately.

However, if your account is not in the same organization, AWS RAM sends an invitation to your
account to accept or reject the resource share. Then, to make the shared resource available, the
data lake administrator in your account must use the AWS RAM console or CLI to accept the
invitation.

The Lake Formation console displays an alert if there is an AWS RAM resource share invitation waiting to
be accepted. Only users authorized to view AWS RAM invitations receive the alert.

###### See Also:

- [Sharing Data Catalog tables and databases across AWS
  Accounts](sharing-catalog-resources.md "sharing-catalog-resources.md")
- [Cross-account data sharing in Lake Formation](cross-account-permissions.md "cross-account-permissions.md")
- [Accessing the underlying data of a shared
  table](cross-account-read-data.md "cross-account-read-data.md")
- [Metadata access control](access-control-metadata.md "access-control-metadata.md") (for
  information about the named resource method versus the LF-TBAC method for sharing
  resources.)

###### Topics

- [Accepting a resource share invitation from AWS RAM](accepting-ram-invite.md "accepting-ram-invite.md")
- [Viewing shared Data Catalog tables and
  databases](viewing-available-shared-resources.md "viewing-available-shared-resources.md")
