# Considerations when enabling Security Lake

**Before enabling Security Lake, consider the following**:

- Security Lake provides cross-region management features, which means you can
  create your data lake and configure log collection across AWS Regions. To
  enable Security Lake in [all supported
  Regions](supported-regions.md "supported-regions.md"), you can choose any supported Regional endpoint. You can also
  add [rollup Regions](add-rollup-region.md "add-rollup-region.md") to aggregate data
  from multiple regions to a single Region.
- We recommend activating Security Lake in all of the supported AWS Regions. If you do
  this, Security Lake can collect data that's connected to unauthorized or unusual
  activity even in Regions that you aren't actively using. If Security Lake is not
  activated in all supported Regions, its ability to collect data from other
  services that you use in multiple Regions is reduced.
- When you enable Security Lake for the first time in any Region, it creates the following service-linked roles for your account:

      + [AWSServiceRoleForSecurityLake](slr-permissions.md "slr-permissions.md"):
       This role includes the
       permissions to call other AWS services on your behalf and operate the security
       data lake. If you enable Security Lake as the [delegated Security Lake administrator](multi-account-management.md#delegated-admin-important "multi-account-management.md#delegated-admin-important"), Security Lake creates the
       [service-linked role](using-service-linked-roles.md "using-service-linked-roles.md")
       in each member account in the organization.
      + [AWSServiceRoleForSecurityLakeResourceManagement](slr-permissions.md "slr-permissions.md"): Security Lake
       uses this role to perform ongoing monitoring and performance improvements, which can potentially reduce latency and costs. This service-linked role
       trusts the `resource-management.securitylake.amazonaws.com` service to assume the role. Enabling this service role
       will also grant it access to Lake Formation.


      For information about how this impacts the existing accounts that enabled Security Lake before April 17, 2025,
       see [Update for existing accounts](multi-account-management.md#security-lake-existing-account-resource-management-slr "multi-account-management.md#security-lake-existing-account-resource-management-slr").

  For information about how service-linked roles work, see [Using service-linked role permissions](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md") in the
  _IAM User Guide_.

- Security Lake doesn't support Amazon S3 Object Lock. When the data lake buckets are created, S3 Object Lock is disabled by default.
  Enabling Object Lock on a bucket interrupts the delivery of normalized log data to the data lake.
- If you are re-enabling Security Lake in a region, you must delete the region's corresponding AWS Glue database from your previous use of Security Lake.
