

# Apply record-based access control in Connect Customer
<a name="record-based-access-control"></a>

With record-based access control, you specify primary attributes and, for each, which primary values a user may access. The rule is applied by attribute name: wherever a data table has a primary attribute with that name, the user is limited to records whose value for it is in your allowed set. Other data tables are unaffected.

**Topics**
+ [Overview](#record-based-access-control-overview)
+ [Apply record-based access control using the Connect Customer admin website](#record-based-access-control-console)
+ [Configuration limitations](#record-based-access-control-config-limitations)

## Overview
<a name="record-based-access-control-overview"></a>

With record-based access control, you configure a set of primary attributes and, for each one, the primary values that a user is allowed to access. Access is matched by primary attribute name. Any data table that contains a primary attribute with a matching name is restricted so that the user can access only the records whose primary value for that attribute is in your configured set of values. Data tables that do not have a primary attribute with a matching name are not affected.

For example, if you configure the primary attribute `Department` with the values `Sales` and `Support`, a user with that security profile can access only the `Sales` and `Support` records in any data table that has a `Department` primary attribute. If a data table has other primary attributes that are not specified in the security profile, those attributes are not restricted.

## Apply record-based access control using the Connect Customer admin website
<a name="record-based-access-control-console"></a>

You configure record-based access control in the access control section of a security profile. For steps to create or edit a security profile, see [Create a security profile](create-security-profile.md) and [Update security profiles](update-security-profiles.md).

1. In the Connect Customer admin website, create or open the security profile that you want to configure.

1. Choose the **Access control** tab.

1. In the **Data tables** section, choose **Edit**.

1. Add primary attributes. For each primary attribute, enter its name and one or more primary values that the user is allowed to access. For applicable limits, see [Configuration limitations](#record-based-access-control-config-limitations).

1. Choose **Save** to save the security profile.

## Configuration limitations
<a name="record-based-access-control-config-limitations"></a>
+ You can configure up to five primary attributes on a single security profile. The limits are not adjustable.
+ For each primary attribute, you can specify one or more values. The number of values can vary for each attribute.
+ For each primary attribute, the total number of characters across its values must be 1,000 or less.