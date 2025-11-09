# Limitations from SCIM specification

The IAM Identity Center SCIM implementation supports only a subset of the SCIM specifications. This section
lists the limitations that the IAM Identity Center SCIM implementation has in comparison to the SCIM
specifications. These include the following:

- **Filter limitations** – Only `eq` with
  `and` is supported. We currently do not support any other filters.
- **Endpoint limitations** – Some SCIM protocol endpoints
  are not supported, such as `/Me`, `/Bulk`, and `/Search`.
  IAM Identity Center supports `/ServiceProviderConfig.` However, `/Schemas` and
  `/ResourceTypes` are currently supported.
- **Attribute limitations** – IAM Identity Center currently does not
  support multi-valued attributes in general for users. Examples include multiple emails,
  addresses, and phone numbers.
- **Functionality limitations** – The `PatchGroup` API doesn't support `remove all` or `replace` operations.
  In addition, IAM Identity Center also has some attributes that are not supported. The following tables
  describe which attributes are currently supported.

**User attributes – Single valued**

| Attribute           | Subattributes (if applicable) | Supported |
| ------------------- | ----------------------------- | --------- |
| `userName`          |                               | Yes       |
| `name`              | `formatted`                   | Yes       |
|                     | `familyName`                  | Yes       |
|                     | `givenName`                   | Yes       |
|                     | `middleName`                  | Yes       |
|                     | `honorificPrefix`             | Yes       |
|                     | `honorificSuffix`             | Yes       |
| `displayName`       |                               | Yes       |
| `nickName`          |                               | Yes       |
| `profileUrl`        |                               | Yes       |
| `title`             |                               | Yes       |
| `userType`          |                               | Yes       |
| `preferredLanguage` |                               | Yes       |
| `locale`            |                               | Yes       |
| `timezone`          |                               | Yes       |
| `active`            |                               | Yes       |
| `password`          |                               | No        |

**User attributes – Multi-valued**

| Attribute          | Subattributes (if applicable) | Supported                   |
| ------------------ | ----------------------------- | --------------------------- |
| `emails`           |                               | Partial (single value only) |
|                    | `display`                     | No                          |
|                    | `type`                        | Yes                         |
|                    | `values`                      | Yes                         |
|                    | `primary`                     | Yes                         |
| `phoneNumbers`     |                               | Partial (single value only) |
|                    | `display`                     | No                          |
|                    | `type`                        | Yes                         |
|                    | `values`                      | Yes                         |
| `ims`              |                               | No                          |
| `photos`           |                               | No                          |
| `addresses`        |                               | Yes (single value only)     |
|                    | `formatted`                   | Yes                         |
|                    | `streetAddress`               | Yes                         |
|                    | `locality`                    | Yes                         |
|                    | `region`                      | Yes                         |
|                    | `postalCode`                  | Yes                         |
|                    | `Country`                     | Yes                         |
| `groups`           |                               | No                          |
| `entitlements`     |                               | No                          |
| `roles`            |                               | Yes                         |
| `x509Certificates` |                               | No                          |

**Group resource schema attributes – Single value**

| Attribute     | Supported |
| ------------- | --------- |
| `displayName` | Yes       |

**Group resource schema attributes – Multi-value**

| Attribute | Subattributes (if applicable) | Supported                             |
| --------- | ----------------------------- | ------------------------------------- |
| `members` |                               | Yes, but cannot be read in a response |
|           | `value`                       | Yes                                   |
|           | `type`                        | Yes                                   |
|           | `$ref`                        | Yes                                   |
|           | `display`                     | No                                    |

The [GetGroup](getgroup.md "getgroup.md") and [ListGroups](listgroups.md "listgroups.md") return an empty member list. To see group information for a certain
member, call [ListGroups](listgroups.md "listgroups.md") with a member filter.

**Enterprise user schema extension attributes – Single
value**

| Attribute        | Subattributes (if applicable) | Supported |
| ---------------- | ----------------------------- | --------- |
| `employeeNumber` |                               | Yes       |
| `costCenter`     |                               | Yes       |
| `organization`   |                               | Yes       |
| `division`       |                               | Yes       |
| `department`     |                               | Yes       |
| `manager`        | `value`                       | Yes       |
|                  | `$ref`                        | Yes       |
|                  | `displayName`                 | No        |
