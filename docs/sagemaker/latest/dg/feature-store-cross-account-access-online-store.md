# Share online feature groups with

AWS Resource Access Manager

With AWS Resource Access Manager (AWS RAM) you can securely share Amazon SageMaker Feature Store online feature groups with other
AWS accounts. Members of your team can explore and access feature groups that span multiple
accounts, promoting data consistency, streamlining collaboration, and reducing duplication of
effort.

The resource owner account can share resources with other individual AWS accounts by
granting permissions using AWS RAM. The resource consumer account is the AWS account with whom a
resource is shared, limited by the permissions granted from the resource owner account. If you are
an organization, you may want to take advantage of AWS Organizations, with which you can share resources
with individual AWS accounts, with all accounts in your organization, or in an Organization Unit
(OU), without having to apply permissions to each account. For instructional videos and more
information about AWS RAM concepts and benefits, see [What is AWS Resource Access Manager?](../../../ram/latest/userguide/what-is.md "../../../ram/latest/userguide/what-is.md") in the AWS RAM User
Guide.

Note that there is a soft maximum limit to the transactions per second (TPS) per API per
AWS account. The maximum TPS limit applies to _all_
transactions on the resources within the resource owner account, so transactions from the resource
consumer accounts also count towards this maximum limit. For information about service quotas and
how to request a quota increase, see [AWS service quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md").

This section covers how the resource owner account can choose feature groups and grant access
privileges (read-only, read-write, and admin) to resource consumer accounts, and then how the
resource consumer accounts with access privileges can use those feature groups. The access
permissions do not allow for the resource consumer accounts to search and discover feature groups.
To allow for resource consumer accounts to search and discover feature groups from the resource
owner account, the resource owner account must grant discoverability permission to the resource
consumer accounts, where all of the feature groups within the resource owner account are
discoverable by the resource consumer accounts. For more information about granting the
discoverability permission, see [Enabling cross account
discoverability](feature-store-cross-account-discoverability.md "feature-store-cross-account-discoverability.md").

The following topics show how to share Feature Store online store resources using the AWS RAM console.
For information about sharing your resources and granting permissions within AWS using the AWS RAM
console or AWS Command Line Interface (AWS CLI), see [Sharing your AWS
resources](../../../ram/latest/userguide/getting-started-sharing.md "../../../ram/latest/userguide/getting-started-sharing.md").

###### Topics

- [Share
  your feature group entities](feature-store-cross-account-access-online-store-share-feature-group.md "feature-store-cross-account-access-online-store-share-feature-group.md")
- [Use online store shared
  resources with access permissions](feature-store-cross-account-access-online-store-use.md "feature-store-cross-account-access-online-store-use.md")
