# Enabling cross account

discoverability

With AWS Resource Access Manager (AWS RAM) you can securely share the feature group catalog, which contains all
of your feature group and feature resources, with other AWS accounts. This lets members of
your team search and discover feature groups and features that span multiple accounts, promoting
data consistency, streamlining collaboration, and reducing duplication of effort.

The resource owner account can share resources with other individual AWS accounts by
granting permissions using AWS RAM. The resource consumer account is the AWS account with whom a
resource is shared, limited by the permissions granted from the resource owner account. If you
are an organization, you may want to take advantage of AWS Organizations, with which you can share
resources with individual AWS accounts, with all accounts in your organization, or in an
Organization Unit (OU), without having to apply permissions to each account. For instructional
videos and more information about AWS RAM concepts and benefits, see [What is AWS Resource Access Manager?](../../../ram/latest/userguide/what-is.md "../../../ram/latest/userguide/what-is.md") in the AWS RAM User
Guide.

This section covers how the resource owner account can choose the feature group catalog and
grant discoverability privilege to resource consumer accounts, and then how the resource
consumer accounts with the discoverability privilege can use search and discover the feature
groups within the resource owner account. The discoverability permission does not grant access
permissions (read-only, read-write, or admin). Access permissions are granted at a resource
level and not at the account level. For information about granting access permissions, see [Enabling cross account access](feature-store-cross-account-access.md "feature-store-cross-account-access.md").

The following topics discuss how to share the feature group catalog and how to search for
shared resources with discoverability permissions applied.

###### Topics

- [Share
  your feature group catalog](feature-store-cross-account-discoverability-share-feature-group-catalog.md "feature-store-cross-account-discoverability-share-feature-group-catalog.md")
- [Search discoverable
  resources](feature-store-cross-account-discoverability-use.md "feature-store-cross-account-discoverability-use.md")
