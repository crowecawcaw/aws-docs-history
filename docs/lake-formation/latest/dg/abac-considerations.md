# Attribute-based access control considerations,

limitations, and supported regions

The following considerations and limitations apply to Attribute based access control
(ABAC).

- ABAC doesn’t support granting access using LF-Tag policies.
- Grantable permissions are not available with ABAC.
- ABAC doesn’t support granting permissions to IAM Identity Center users.
- When using ABAC grants on a table in Lake Formation, Lake Formation doesn't grant
  `DESCRIBE` permissions to the parent database or catalog. This differs from
  non-ABAC scenarios, where Lake Formation provides implicit `DESCRIBE`
  permissions to parent resources.
- All principals with the `AmazonDataZoneProject` tag key are always treated as opted
  in to Lake Formation for all Data Catalog resources.
- ABAC supports only string attributes.
