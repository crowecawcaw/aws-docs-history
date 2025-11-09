# Attribute mappings between IAM Identity Center and External

Identity Providers directory

Attribute mappings are used to map attribute types that exist in IAM Identity Center with like
attributes in your external identity source such as Google Workspace, Microsoft Active Directory
(AD), and Okta. IAM Identity Center retrieves user attributes from your identity source and maps
them to IAM Identity Center user attributes.

If your IAM Identity Center is synchronized to use an **external identity provider**
(IdP), like Google Workspace, Okta, or Ping as the identity source, you'll need to map
your attributes in your IdP.

IAM Identity Center prefills a set of attributes for you under the **Attribute
mappings** tab found on its configuration page. IAM Identity Center uses these user attributes to
populate SAML assertions (as SAML attributes) that are sent to the application. These user
attributes are in turn retrieved from your identity source. Each application determines the
list of SAML 2.0 attributes it needs for successful single sign-on. For more information, see
[Map attributes in your application to IAM Identity Center
attributes](mapawsssoattributestoapp.md "mapawsssoattributestoapp.md").

IAM Identity Center also manages a set of attributes for you under the **Attribute
mappings** section of your **Active Directory configuration page**
if you're using Active Directory as an identity source. For more information, see [Mapping user attributes between IAM Identity Center and
Microsoft AD directory](mapssoattributestocdattributes.md "mapssoattributestocdattributes.md").

## Supported external identity provider

attributes

The following table lists all external identity provider (IdP) attributes supported and
can be mapped to attributes you can use when configuring [Attributes for access control](attributesforaccesscontrol.md "attributesforaccesscontrol.md") in
IAM Identity Center. When using SAML assertions, you can use whichever attributes your IdP
supports.

| Supported attributes in your IdP                  |
| ------------------------------------------------- |
| `${path:userName}`                                |
| `${path:name.familyName}`                         |
| `${path:name.givenName}`                          |
| `${path:displayName}`                             |
| `${path:nickName}`                                |
| `${path:emails[primary eq true].value}`           |
| `${path:addresses[type eq "work"].streetAddress}` |
| `${path:addresses[type eq "work"].locality}`      |
| `${path:addresses[type eq "work"].region}`        |
| `${path:addresses[type eq "work"].postalCode}`    |
| `${path:addresses[type eq "work"].country}`       |
| `${path:addresses[type eq "work"].formatted}`     |
| `${path:phoneNumbers[type eq "work"].value}`      |
| `${path:userType}`                                |
| `${path:title}`                                   |
| `${path:locale}`                                  |
| `${path:timezone}`                                |
| `${path:enterprise.employeeNumber}`               |
| `${path:enterprise.costCenter}`                   |
| `${path:enterprise.organization}`                 |
| `${path:enterprise.division}`                     |
| `${path:enterprise.department}`                   |
| `${path:enterprise.manager.value}`                |

## Default mappings between IAM Identity Center and

Microsoft AD

The following table lists the default mappings for user attributes in IAM Identity Center to the user
attributes in your Microsoft AD directory. IAM Identity Center only supports the list of
attributes in the **User attribute in IAM Identity Center** column.

| User attribute in IAM Identity Center | Maps to this attribute in your Active Directory |
| ------------------------------------- | ----------------------------------------------- |
| `displayname`                         | `${displayname}`                                |
| `emails[?primary].value *`            | `${mail}`                                       |
| `externalid`                          | `${objectguid}`                                 |
| `name.givenname`                      | `${givenname}`                                  |
| `name.familyname`                     | `${sn}`                                         |
| `name.middlename`                     | `${initials}`                                   |
| `sid`                                 | `${objectsid}`                                  |
| `username`                            | `${userprincipalname}`                          |

\* The email attribute in IAM Identity Center must be unique within the directory.

| Group attribute in IAM Identity Center | Maps to this attribute in your Active Directory |
| -------------------------------------- | ----------------------------------------------- |
| `externalid`                           | `${objectguid}`                                 |
| `description`                          | `${description}`                                |
| `displayname`                          | `${samaccountname}@{associateddomain}`          |

###### Considerations

- If you do not have any assignments for your users and groups in IAM Identity Center when you enable
  configurable AD sync, the default mappings in the previous tables are used. For
  information about how to customize these mappings, see [Configure
  attribute mappings for your sync](manage-sync-configure-attribute-mapping-configurable-ADsync.md "manage-sync-configure-attribute-mapping-configurable-ADsync.md").
- Certain IAM Identity Center attributes cannot be modified because they are immutable and mapped by
  default to specific Microsoft AD directory attributes.

For example, "username" is a mandatory attribute in IAM Identity Center. If you map "username" to
an AD directory attribute with an empty value, IAM Identity Center will consider the
`windowsUpn` value as the default value for "username". If you want to
change the attribute mapping for "username" from your current mapping, confirm IAM Identity Center
flows with dependency on "username" will continue to work as expected, before making the
change.

## Supported Microsoft AD

attributes for IAM Identity Center

The following table lists all Microsoft AD directory attributes that are
supported and that can be mapped to user attributes in IAM Identity Center.

| Supported attributes in your Microsoft AD directory |
| --------------------------------------------------- |
| `${samaccountname}`                                 |
| `${description}`                                    |
| `${objectguid}`                                     |
| `${objectsid}`                                      |
| `${givenname}`                                      |
| `${sn}`                                             |
| `${initials}`                                       |
| `${mail}`                                           |
| `${userprincipalname}`                              |
| `${displayname}`                                    |
| `${distinguishedname}`                              |
| `${proxyaddresses[?type == "SMTP"].value}`          |
| `${proxyaddresses[?type == "smtp"].value}`          |
| `${useraccountcontrol}`                             |
| `${associateddomain}`                               |

###### Considerations

- You can specify any combination of supported Microsoft AD directory
  attributes to map to a single mutable attribute in IAM Identity Center.

## Supported IAM Identity Center attributes for Microsoft

AD

The following table lists all IAM Identity Center attributes that are supported and that can be mapped
to user attributes in your Microsoft AD directory. After you set up your
application attribute mappings, you can use these same IAM Identity Center attributes to map to actual
attributes used by that application.

| Supported attributes in IAM Identity Center for Active Directory |
| ---------------------------------------------------------------- |
| `${user:AD_GUID}`                                                |
| `${user:AD_SID}`                                                 |
| `${user:email}`                                                  |
| `${user:familyName}`                                             |
| `${user:givenName}`                                              |
| `${user:middleName}`                                             |
| `${user:name}`                                                   |
| `${user:preferredUsername}`                                      |
| `${user:subject}`                                                |
