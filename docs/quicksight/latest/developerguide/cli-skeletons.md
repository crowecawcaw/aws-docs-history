# Use CLI skeleton files

To run AWS CLI commands that require long and complicated strings, you can generate CLI
skeleton files . A _CLI skeleton_ is a JSON file that
provides you with an outline, or skeleton, of the command that you want to run. You can use
a CLI skeleton file for every Quick Sight command, but skeleton files are most useful when
using `Create` or `Update` commands.

## Generate a CLI skeleton file

To generate a CLI skeleton file, enter the following command into your
terminal.

```
aws quicksight `OPERATION` --generate-cli-skeleton
```

A JSON file that contains a skeleton of the command that you want to run then appears
in your terminal. Enter the required input values and save the file. The following example shows a cli example that is generated for the `UpdateDashboardPermissions` API.

```
$ aws quicksight update-dashboard-permissions --generate-cli-skeleton
{
	"AwsAccountId": "",
	"DashboardId": "",
	"GrantPermissions":[
		{
			"Principal": "",
			"Actions": [
				""
			]
		}
	],
	"RevokePermissions": [
		{
			"Principal": "",
			"Actions": [
				""
			]

		}
	]

}
```

Enter the following to make a CLI command using the saved skeleton file.

```
aws quicksight `COMMAND` --cli-input-json file://`filename`.json
```

You can update and reuse CLI skeleton files to run future commands.

## Operations that skeleton files are most useful for

You can use a CLI skeleton file for every command in Quick Sight. However, skeleton files are
most useful for commands that require long or complicated string inputs, such as a
permissions update.

Following is a list of Quick Sight operations where we recommend using a CLI skeleton
file:

###### Account customization operations

- [CreateAccountCustomization](create-account-customization.md "create-account-customization.md")
- [UpdateAccountCustomization](update-account-customization.md "update-account-customization.md")
- [UpdateAccountSettings](update-account-settings.md "update-account-settings.md")

###### Analysis operations

- [CreateAnalysis](create-analysis.md "create-analysis.md")
- [UpdateAnalysis](update-analysis.md "update-analysis.md")
- [UpdateAnalysisPermissions](update-analysis-permissions.md "update-analysis-permissions.md")

###### Dashboard operations

- [CreateDashboard](create-dashboard.md "create-dashboard.md")
- [UpdateDashboard](update-dashboard.md "update-dashboard.md")
- [UpdateDashboardPermissions](update-dashboard-permissions.md "update-dashboard-permissions.md")
- [UpdateDashboardPublishedVersion](update-dashboard-published-version.md "update-dashboard-published-version.md")

###### Dataset operations

- [CreateDataSet](create-data-set.md "create-data-set.md")
- [UpdateDataSet](update-data-set.md "update-data-set.md")
- [UpdateDataSetPermissions](update-data-set-permissions.md "update-data-set-permissions.md")

###### Data source operations

- [CreateDataSource](create-data-source.md "create-data-source.md")
- [UpdateDataSource](update-data-source.md "update-data-source.md")
- [UpdateDataSourcePermissions](update-data-source-permissions.md "update-data-source-permissions.md")

###### Folder operations

- [CreateFolder](create-folder.md "create-folder.md")
- [CreateFolderMembership](create-folder-membership.md "create-folder-membership.md")
- [UpdateFolder](update-folder.md "update-folder.md")
- [UpdateFolderPermissions](update-folder-permissions.md "update-folder-permissions.md")

###### Group operations

- [CreateGroup](create-group.md "create-group.md")
- [CreateGroupMembership](create-group-membership.md "create-group-membership.md")
- [UpdateGroup](update-group.md "update-group.md")

###### IAM policy assignment operations

- [CreateIAMPolicyAssignment](create-iam-policy-assignment.md "create-iam-policy-assignment.md")
- [UpdateIAMPolicyAssignment](update-iam-policy-assignment.md "update-iam-policy-assignment.md")

###### Ingestion operations

- [CreateIngestion](create-ingestion.md "create-ingestion.md")

###### Namespace operations

- [CreateNamespace](create-namespace.md "create-namespace.md")

###### Template operations

- [CreateTemplate](create-template.md "create-template.md")
- [UpdateTemplate](update-template.md "update-template.md")
- [UpdateTemplatePermissions](update-template-permissions.md "update-template-permissions.md")

###### Template alias operations

- [CreateTemplateAlias](create-template-alias.md "create-template-alias.md")
- [UpdateTemplateAlias](update-template-alias.md "update-template-alias.md")

###### Theme operations

- [CreateTheme](create-theme.md "create-theme.md")
- [UpdateTheme](update-theme.md "update-theme.md")
- [UpdateThemePermissions](update-theme-permissions.md "update-theme-permissions.md")

###### Theme alias permissions

- [CreateThemeAlias](create-theme-alias.md "create-theme-alias.md")
- [UpdateTemplateAlias](update-template-alias.md "update-template-alias.md")

###### User operations

- [RegisterUser](register-user.md "register-user.md")
- [UpdateUser](update-user.md "update-user.md")
