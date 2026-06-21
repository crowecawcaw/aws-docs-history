# Enabling or disabling user and group management or AWS Directory Service Data

To use user and group management or AWS Directory Service Data, it must be enabled. Once enabled, you can manage
users and groups from the AWS Management Console, AWS CLI, or AWS Tools for PowerShell.

###### Important

- You can only enable this feature from the Primary AWS Region for your directory. For
  more information, see [Primary vs additional Regions](multi-region-global-primary-additional.md "multi-region-global-primary-additional.md").
- For a list of regions that support AWS Directory Service Data, see
  [Supported AWS Regions for Directory Service Data](regions.md#regions_directory_service_data "regions.md#regions_directory_service_data").
- Access controls for AWS Directory Service Data are different than access controls for AWS services like
  Amazon WorkSpaces, Amazon Quick, and Amazon WorkMail. For more information, see [AWS application authorization with Directory Service Data](ad_manage_apps_services_authorization.md#ad_manage_apps_services_authorization_ADSD "ad_manage_apps_services_authorization.md#ad_manage_apps_services_authorization_ADSD").

## Enabling AWS Directory Service Data

Use the following procedure to enable AWS Directory Service Data for an existing
AWS Managed Microsoft AD with the AWS Management Console, AWS CLI, or AWS Tools for PowerShell.

AWS Management Console
You can enable user and group management with the AWS Management Console.

###### To enable user and group management

1. Open the Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/").
2. On the **Directory details** page, to enable
   user and group management, select **Enable**.
3. In the **Enable user and group management** dialog box, select
   **Enable**.

AWS CLI
The following describes how to format a request that enables the AWS Directory Service Data CLI. You
must include your Directory ID number in your request.

###### Note

This command uses the [`aws ds`](../../../cli/latest/reference/ds.md "../../../cli/latest/reference/ds.md") namespace.

###### To enable AWS Directory Service Data CLI

- Open the AWS CLI, and run the following command with your Directory ID:

```
aws ds enable-directory-data-access --directory-id `d-1234567890`
```

For more information, see [`enable-directory-data-access`](../../../cli/latest/reference/ds/enable-directory-data-access.md "../../../cli/latest/reference/ds/enable-directory-data-access.md").

PowerShell

###### Note

This command uses the [`AWS.Tools.DirectoryService`](../../../powershell/latest/reference/items/DirectoryService_cmdlets.md "../../../powershell/latest/reference/items/DirectoryService_cmdlets.md") module.

###### To enable Directory Service Data with Tools for PowerShell

- Open PowerShell, and run the following command with your
  Directory ID:

```
Enable-DSDirectoryDataAccess -DirectoryId `d-1234567890`
```

For more information, see [`Enable-DSDirectoryDataAccess`](../../../powershell/latest/reference/items/Enable-DSDirectoryDataAccess.md "../../../powershell/latest/reference/items/Enable-DSDirectoryDataAccess.md").

## Disabling AWS Directory Service Data

Use the following procedure to disable AWS Directory Service Data for an existing
AWS Managed Microsoft AD with the AWS Management Console, AWS CLI, or AWS Tools for PowerShell.

AWS Management Console
You can disable user and group management with the AWS Management Console.

###### To disable user and group management

1. Open the Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/").
2. On the **Directory details** page, to disable
   user and group management, select **Disable**.
3. In the **Disable user and group management** dialog box, select
   **Disable**.

AWS CLI
The following describes how to format a request that disables the AWS Directory Service Data CLI. You
must include your Directory ID number in your request.

###### Note

This command uses the [`aws ds`](../../../cli/latest/reference/ds.md "../../../cli/latest/reference/ds.md") namespace.

###### To disable AWS Directory Service Data CLI

- Open the AWS CLI, and run the following command with your Directory ID:

```
aws ds disable-directory-data-access --directory-id `d-1234567890`
```

For more information, see [`disable-directory-data-access`](../../../cli/latest/reference/ds/disable-directory-data-access.md "../../../cli/latest/reference/ds/disable-directory-data-access.md").

PowerShell

###### Note

This command uses the [`AWS.Tools.DirectoryService`](../../../powershell/latest/reference/items/DirectoryService_cmdlets.md "../../../powershell/latest/reference/items/DirectoryService_cmdlets.md") module.

###### To disable Directory Service Data with Tools for PowerShell

- Open PowerShell, and run the following command with your
  Directory ID:

```
Disable-DSDirectoryDataAccess -DirectoryId `d-123456789`
```

For more information, see [`Disable-DSDirectoryDataAccess`](../../../powershell/latest/reference/items/Disable-DSDirectoryDataAccess.md "../../../powershell/latest/reference/items/Disable-DSDirectoryDataAccess.md").
