AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Delete a Distributor

package

This section describes how to a delete a package. You can't delete a version of a
package, only the entire package.

## Deleting a package using the

console

You can use the AWS Systems Manager console to delete a package or a package version
from Distributor, a tool in AWS Systems Manager. Deleting a package deletes all versions of a
package from Distributor.

###### To delete a package using the console

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Distributor**.
3. On the **Distributor** home page, choose the package
   that you want to delete.
4. On the package's details page, choose **Delete
   package**.
5. When you're prompted to confirm the deletion, choose **Delete
   package**.

## Deleting a package

version using the console

You can use the Systems Manager console to delete a package version from
Distributor.

###### To delete a package version using the console

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Distributor**.
3. On the **Distributor** home page, choose the package
   that you want to delete a version of.
4. On the versions page for the package, choose the version to delete and
   choose **Delete version**.
5. When you're prompted to confirm the deletion, choose **Delete
   package version**.

## Deleting a package using the

command line

You can use your preferred command line tool to delete a package from
Distributor.

Linux & macOS

###### To delete a package using the AWS CLI

1. Run the following command to list documents for specific
   packages. In the results of this command, look for the
   package that you want to delete.

```
aws ssm list-documents \
    --filters Key=Name,Values=`package-name`
```

2. Run the following command to delete a package. Replace
   `package-name` with the package
   name.

```
aws ssm delete-document \
    --name "`package-name`"
```

3. Run the **list-documents** command again to
   verify that the package was deleted. The package you deleted
   shouldn't be included in the list.

```
aws ssm list-documents \
    --filters Key=Name,Values=`package-name`
```

Windows

###### To delete a package using the AWS CLI

1. Run the following command to list documents for specific
   packages. In the results of this command, look for the
   package that you want to delete.

```
aws ssm list-documents ^
    --filters Key=Name,Values=`package-name`
```

2. Run the following command to delete a package. Replace
   `package-name` with the package
   name.

```
aws ssm delete-document ^
    --name "`package-name`"
```

3. Run the **list-documents** command again to
   verify that the package was deleted. The package you deleted
   shouldn't be included in the list.

```
aws ssm list-documents ^
    --filters Key=Name,Values=`package-name`
```

PowerShell

###### To delete a package using Tools for PowerShell

1. Run the following command to list documents for specific
   packages. In the results of this command, look for the
   package that you want to delete.

```
$filter = New-Object Amazon.SimpleSystemsManagement.Model.DocumentKeyValuesFilter
$filter.Key = "Name"
$filter.Values = "`package-name`"

Get-SSMDocumentList `
    -Filters @($filter)
```

2. Run the following command to delete a package. Replace
   `package-name` with the package
   name.

```
Remove-SSMDocument `
    -Name "`package-name`"
```

3. Run the **Get-SSMDocumentList** command
   again to verify that the package was deleted. The package
   you deleted shouldn't be included in the list.

```
$filter = New-Object Amazon.SimpleSystemsManagement.Model.DocumentKeyValuesFilter
$filter.Key = "Name"
$filter.Values = "`package-name`"

Get-SSMDocumentList `
    -Filters @($filter)
```

## Deleting a package version

using the command line

You can use your preferred command line tool to delete a package version from
Distributor.

Linux & macOS

###### To delete a package version using the AWS CLI

1. Run the following command to list the versions of your
   package. In the results of this command, look for the
   package version that you want to delete.

```
aws ssm list-document-versions \
    --name "`package-name`"
```

2. Run the following command to delete a package version.
   Replace `package-name` with the
   package name and `version` with the
   version number.

```
aws ssm delete-document \
    --name "`package-name`" \
    --document-version `version`
```

3. Run the **list-document-versions** command
   to verify that the version of the package was deleted. The
   package version that you deleted shouldn't be found.

```
aws ssm list-document-versions \
    --name "`package-name`"
```

Windows

###### To delete a package version using the AWS CLI

1. Run the following command to list the versions of your
   package. In the results of this command, look for the
   package version that you want to delete.

```
aws ssm list-document-versions ^
    --name "`package-name`"
```

2. Run the following command to delete a package version.
   Replace `package-name` with the
   package name and `version` with the
   version number.

```
aws ssm delete-document ^
    --name "`package-name`" ^
    --document-version `version`
```

3. Run the **list-document-versions** command
   to verify that the version of the package was deleted. The
   package version that you deleted shouldn't be found.

```
aws ssm list-document-versions ^
    --name "`package-name`"
```

PowerShell

###### To delete a package version using Tools for PowerShell

1. Run the following command to list the versions of your
   package. In the results of this command, look for the
   package version that you want to delete.

```
Get-SSMDocumentVersionList `
    -Name "`package-name`"
```

2. Run the following command to delete a package version.
   Replace `package-name` with the
   package name and `version` with the
   version number.

```
Remove-SSMDocument `
    -Name "`package-name`" `
    -DocumentVersion `version`
```

3. Run the **Get-SSMDocumentVersionList**
   command to verify that the version of the package was
   deleted. The package version that you deleted shouldn't be
   found.

```
Get-SSMDocumentVersionList `
    -Name "`package-name`"
```

For information about other options you can use with the
**list-documents** command, see [**list-documents**](../../../cli/latest/reference/ssm/list-documents.md "../../../cli/latest/reference/ssm/list-documents.md") in the AWS Systems Manager section of the
_AWS CLI Command Reference_. For information about other options
you can use with the **delete-document** command, see [**delete-document**](../../../cli/latest/reference/ssm/delete-document.md "../../../cli/latest/reference/ssm/delete-document.md").
