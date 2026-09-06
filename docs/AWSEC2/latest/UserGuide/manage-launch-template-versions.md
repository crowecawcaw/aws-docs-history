

# Modify a launch template (manage launch template versions)
<a name="manage-launch-template-versions"></a>

Launch templates are immutable; after you create a launch template, you can't modify it. Instead, you can create a new version of the launch template that includes any changes you require.

You can create different versions of a launch template, set the default version, describe a launch template version, and [delete versions](delete-launch-template.md#delete-launch-template-version) you no longer need.

**Topics**
+ [Create a launch template version](#create-launch-template-version)
+ [Set the default launch template version](#set-default-launch-template-version)
+ [Describe a launch template version](#describe-launch-template-version)

## Create a launch template version
<a name="create-launch-template-version"></a>

When you create a launch template version, you can specify new launch parameters or use an existing version as the base for the new version. For a description of each parameter, see [Reference for Amazon EC2 instance configuration parameters](ec2-instance-launch-parameters.md).

------
#### [ Console ]

**To create a launch template version**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Launch Templates**.

1. Choose a launch template, and then choose **Actions**, **Modify template (Create new version)**.

1. For **Template version description**, enter a description for this version of the launch template.

1. (Optional) Expand **Source template** and select a version of the launch template to use as a base for the new launch template version. The new launch template version inherits the launch parameters from this launch template version.

1. Modify the launch parameters as required.

1. Choose **Create launch template**.

------
#### [ AWS CLI ]

**To create a launch template version**  
Use the [create-launch-template-version](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-launch-template-version.html) command. You can specify a source version on which to base the new version. The new version inherits the launch parameters from this version, and you can override parameters using `--launch-template-data`. The following example creates a new version based on version 1 of the launch template and specifies a different AMI ID.

```
aws ec2 create-launch-template-version \
    --launch-template-id {{lt-0abcd290751193123}} \
    --version-description {{WebVersion2}} \
    --source-version {{1}} \
    --launch-template-data "ImageId={{ami-0abcdef1234567890}}"
```

------
#### [ PowerShell ]

**To create a launch template version**  
Use the [New-EC2LaunchTemplateVersion](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2LaunchTemplateVersion.html) Cmdlet. You can specify a source version on which to base the new version. The new version inherits the launch parameters from this version, and you can override parameters using `LaunchTemplateData`. The following example creates a new version based on version 1 of the launch template and specifies a different AMI ID.

```
New-EC2LaunchTemplateVersion `
    -LaunchTemplateId {{lt-0abcd290751193123}} `
    -VersionDescription {{WebVersion2}} `
    -SourceVersion {{1}} `
    -LaunchTemplateData (
        New-Object `
            -TypeName Amazon.EC2.Model.RequestLaunchTemplateData `
            -Property @{ImageId = '{{ami-0abcdef1234567890}}'}
    )
```

------

## Set the default launch template version
<a name="set-default-launch-template-version"></a>

You can set the default version for the launch template. When you launch an instance from a launch template and do not specify a version, the instance is launched using the parameters of the default version.

------
#### [ Console ]

**To set the default launch template version**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Launch Templates**.

1. Choose the launch template and choose **Actions**, **Set default version**.

1. For **Template version**, select the version number to set as the default version and choose **Set as default version**.

------
#### [ AWS CLI ]

**To set the default launch template version**  
Use the [modify-launch-template](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-launch-template.html) command.

```
aws ec2 modify-launch-template \
    --launch-template-id {{lt-0abcd290751193123}} \
    --default-version {{2}}
```

------
#### [ PowerShell ]

**To set the default launch template version**  
Use the [Edit-EC2LaunchTemplate](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2LaunchTemplate.html) cmdlet.

```
Edit-EC2LaunchTemplate `
    -LaunchTemplateId {{lt-0abcd290751193123}} `
    -DefaultVersion {{2}}
```

------

## Describe a launch template version
<a name="describe-launch-template-version"></a>

Using the console, you can view all the versions of the selected launch template, or get a list of the launch templates whose latest or default version matches a specific version number. Using the AWS CLI, you can describe all versions, individual versions, or a range of versions of a specified launch template. You can also describe all the latest versions or all the default versions of all the launch templates in your account.

------
#### [ Console ]

**To describe a launch template version**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Launch Templates**.

1. You can view a version of a specific launch template, or get a list of the launch templates whose latest or default version matches a specific version number.
   + To view a version of a launch template: Choose the launch template. On the **Versions** tab, from **Version**, choose a version to view its details.
   + To get a list of all the launch templates whose latest version matches a specific version number: From the search bar, choose **Latest version**, and then choose a version number.
   + To get a list of all the launch templates whose default version matches a specific version number: From the search bar, choose **Default version**, and then choose a version number.

------
#### [ AWS CLI ]

**To describe a launch template version**  
Use the [describe-launch-template-versions](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-launch-template-versions.html) command and specify the version numbers. In the following example, versions `{{1}}` and {{`3`}} are specified.

```
aws ec2 describe-launch-template-versions \
    --launch-template-id {{lt-0abcd290751193123}} \
    --versions {{1 3}}
```

**To describe the latest and default launch template versions in your account**  
Use the [describe-launch-template-versions](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-launch-template-versions.html) command and specify `$Latest`, `$Default`, or both. You must omit the launch template ID and name in the call. You can't specify version numbers.

```
aws ec2 describe-launch-template-versions \
    --versions "{{$Latest}},{{$Default}}"
```

------
#### [ PowerShell ]

**To describe a launch template version**  
Use the [Get-EC2TemplateVersion](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2TemplateVersion.html) Cmdlet and specify the version numbers. In the following example, versions `{{1}}` and {{`3`}} are specified.

```
Get-EC2TemplateVersion `
    -LaunchTemplateId {{lt-0abcd290751193123}} `
    -Version {{1,3}}
```

**To describe the latest and default launch template versions in your account**  
Use the [Get-EC2TemplateVersion](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2TemplateVersion.html) Cmdlet and specify `$Latest`, `$Default`, or both. You must omit the launch template ID and name in the call. You can't specify version numbers.

```
Get-EC2TemplateVersion `
    -Version '{{$Latest}}','{{$Default}}'
```



------