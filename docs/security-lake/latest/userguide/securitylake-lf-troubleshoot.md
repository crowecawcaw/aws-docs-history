# Troubleshooting Lake Formation issues

Use the following information to help you diagnose and fix common issues that you might encounter when working with Security Lake and AWS Lake Formation databases or tables. For
more Lake Formation troubleshooting topics, see the [Troubleshooting](../../../lake-formation/latest/dg/troubleshooting.md "../../../lake-formation/latest/dg/troubleshooting.md") section
of the _AWS Lake Formation Developer Guide_.

## Table not found

You may receive this error when attempting to create a subscriber.

To resolve this error, make sure that you have added sources in the Region already. If you added sources when the
Security Lake service was in preview release, you must add them again before creating a subscriber. For more information on
adding sources, see [Source management in Security Lake](source-management.md "source-management.md").

## 400 AccessDenied

You may receive this error when you [add a custom source](adding-custom-sources.md "adding-custom-sources.md") and call the
`CreateCustomLogSource` API.

To resolve the error, review your Lake Formation permissions. The IAM role that's calling the API should have
**Create table** permissions for the Security Lake database. For more information, see [Granting database permissions using the Lake Formation console and the named resource method](../../../lake-formation/latest/dg/granting-database-permissions.md "../../../lake-formation/latest/dg/granting-database-permissions.md")
in the _AWS Lake Formation Developer Guide_.

## SYNTAX_ERROR: line 1:8: SELECT \*

not allowed from relation that has no columns

You may receive this error when querying a source table for the first time in
Lake Formation.

To resolve the error, grant `SELECT` permission to the IAM role
you are using when signed into your AWS account. For instructions on how to grant
`SELECT` permission, see [Granting table
permissions using the Lake Formation console and the named resource method](../../../lake-formation/latest/dg/granting-table-permissions.md "../../../lake-formation/latest/dg/granting-table-permissions.md") in the
_AWS Lake Formation Developer Guide_.

## Security Lake failed to add caller's principal ARN to Lake Formation data lake admin. Current data lake administrators may include invalid principals that no longer exist.

You may receive this error when enabling Security Lake or adding an AWS service as a log source.

To resolve the error, follow these steps:

1. Open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").
2. Sign in as an administrative user.
3. In the navigation pane, under **Permissions**, choose **Administrative roles and tasks**.
4. In the **Data lake administrators** section, choose **Choose administrators**.
5. Clear principals that are labeled **Not found in IAM**, and then choose **Save**.
6. Try the Security Lake operation again.

## Security Lake CreateSubscriber with Lake Formation didn't create a new RAM resource share invitation to be accepted

You may see this error if you shared resources with [Lake Formation version 2 or version 3 cross-account data
sharing](../../../lake-formation/latest/dg/optimize-ram.md "../../../lake-formation/latest/dg/optimize-ram.md") before creating a Lake Formation subscriber in Security Lake. This is because
Lake Formation version 2 and version 3 cross-account sharing optimizes the number of AWS RAM
resource shares by mapping multiple cross-account permission grants with one AWS RAM resource
share.

Make sure to check that the resource share name has the external ID that you specified when
creating the subscriber and the resource share ARN matches the ARN in the
`CreateSubscriber` response.
