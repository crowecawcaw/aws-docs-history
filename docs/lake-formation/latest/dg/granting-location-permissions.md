# Granting data location permissions

Data location permissions in AWS Lake Formation enable principals to create and alter Data Catalog
resources that point to designated registered Amazon S3 locations. Data location permissions work
in addition to Lake Formation data permissions to secure information in your data lake.

Lake Formation does not use the AWS Resource Access Manager (AWS RAM) service for data location permission grants, so
you don't need to accept resource share invitations for data location permissions.

You can grant data location permissions by using the Lake Formation console, API, or AWS Command Line Interface
(AWS CLI).

###### Note

For a grant to succeed, you must first register the data location with Lake Formation.

###### See Also:

- [Underlying data access control](access-control-underlying-data.md#data-location-permissions "access-control-underlying-data.md#data-location-permissions")

###### Topics

- [Granting data location permissions (same
  account)](granting-location-permissions-local.md "granting-location-permissions-local.md")
- [Granting data location permissions
  (external account)](granting-location-permissions-external.md "granting-location-permissions-external.md")
- [Granting permissions on a data location shared with your
  account](regranting-locations.md "regranting-locations.md")
