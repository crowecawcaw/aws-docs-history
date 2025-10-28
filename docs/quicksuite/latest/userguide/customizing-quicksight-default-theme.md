# Setting a default theme for

Amazon Quick Suite analyses with the Amazon Quick Suite APIs

###### To set a default theme by using the API

1. Identify the custom theme that you want to use as the default, and locate its
   theme ID. If you want to use one of the QuickSight starter themes, skip this step.

To get the theme ID of a custom theme, use the [ListThemes](../../../quicksight/latest/APIReference/API_ListThemes.md "../../../quicksight/latest/APIReference/API_ListThemes.md") API operation for the Region where the theme is. Make sure
that the theme is in the same Region with the users or groups
that need to use it.

The following example shows a shell script that uses the `list-themes`
command in the AWS CLI. It sets the AWS account ID and the AWS Region as
variables. If you previously used `aws configure` to set a default
Region, adding the `--region` variable to your command overrides your
default setting.

```
#declare variables
awsacct1='111122223333'
region='us-west-2'

aws quicksight list-themes \
--region `$region` \
--aws-account-id `$awsacct1` \
--type 'CUSTOM'
```

2. Use the [ListUsers](../../../quicksight/latest/APIReference/API_ListUsers.md "../../../quicksight/latest/APIReference/API_ListUsers.md") or [ListGroups](../../../quicksight/latest/APIReference/API_ListGroups.md "../../../quicksight/latest/APIReference/API_ListGroups.md") API
   operation
   to collect the Amazon Resource Names (ARNs) for users or
   groups that need to use the theme as a default. You need only
   the top-level ARN. If all your users are part of the same group, use the group ARN.

For more information on Amazon Quick Suite ARNs, see [ARN
formats](../../../quicksight/latest/APIReference/qs-arn-format.md "../../../quicksight/latest/APIReference/qs-arn-format.md") in the _Quick Suite API
Reference._ 3. If you're using a custom theme, grant access to the theme for the ARNs that you
collected in the previous step. If you're using a starter theme, skip this step
because all users have access to starter themes.

The following example shows a shell script that uses the [update-theme-permissions](../../../quicksight/latest/APIReference/API_UpdateThemePermissions.md "../../../quicksight/latest/APIReference/API_UpdateThemePermissions.md") command The `grant-permissions`
parameter is shown using shorthand syntax. You can use JSON or YAML instead. For
more information, see [Specifying
parameter values](../../../cli/latest/userguide/cli-usage-parameters.md "../../../cli/latest/userguide/cli-usage-parameters.md") in the _AWS Command Line Interface User Guide._

```
#declare variables
awsacct1='111122223333'
namespace='default'
region='us-west-2'
theme-id='bdb844d0-0fe9-4d9d-b520-0fe602d93639' #Find this with list-themes

aws quicksight update-theme-permissions \
#Specify region if necessary: --region `$region` \
--aws-account-id `$awsacct1` \
--theme-id `$theme-id` \
--grant-permissions Principal="arn:aws:quicksight:`$region`:`$awsacct1`:group/`$namespace`/`QuickSight_Group_Name`",Actions="quicksight:DescribeTheme","quicksight:ListThemeVersions","quicksight:ListThemeAliases","quicksight:DescribeThemeAlias"
```

4. Assign the theme as the default for the same ARN or ARNs.

```
#declare variables
awsacct1='111122223333'
namespace='default'
region='us-west-2'
theme-id='bdb844d0-0fe9-4d9d-b520-0fe602d93639'

aws quicksight create-account-customization \
#Specify region if necessary: --region `$region` \
--aws-account-id `$awsacct1` \
--namespace `$namespace` \
--account-customization DefaultTheme="arn:aws:quicksight:`$region`:`$awsacct1`:theme/`$theme-id`"
```

Currently, there are three starter themes: Classic, Midnight, and Seaside. Their ARNs are
the capitalized spelling of their theme name. If you are using a starter theme instead of a
custom theme, use one of the following theme ARNs:

- `arn:aws:quicksight::aws:theme/CLASSIC`
- `arn:aws:quicksight::aws:theme/MIDNIGHT`
- `arn:aws:quicksight::aws:theme/SEASIDE`
- `arn:aws:quicksight::aws:theme/RAINIER`
