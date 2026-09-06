

# Delete a launch template or a launch template version
<a name="delete-launch-template"></a>

If you no longer require a launch template, you can delete it. Deleting a launch template deletes all of its versions. If you only want to delete a specific version of a launch template, you can do so while retaining the other versions of the launch template.

Deleting a launch template or launch template version doesn't affect any instances that you've launched from the launch template. 

## Delete a launch template and all of its versions
<a name="delete-launch-template-including-versions"></a>

If you no longer require a launch template, including all of its versions, you can delete the launch template. Deleting a launch template deletes all of its versions.

------
#### [ Console ]

**To delete a launch template and all its versions**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Launch Templates**.

1. Choose the launch template and choose **Actions**, **Delete template**.

1. Enter **Delete** to confirm deletion, and then choose **Delete**.

------
#### [ AWS CLI ]

**To delete a launch template and all its versions**  
Use the [delete-launch-template](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-launch-template.html) command and specify the launch template.

```
aws ec2 delete-launch-template --launch-template-id {{lt-01238c059e3466abc}}
```

------
#### [ PowerShell ]

**To delete a launch template and all its versions**  
Use the [Remove-EC2LaunchTemplate](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-EC2LaunchTemplate.html) (AWS Tools for PowerShell) command and specify the launch template. If `-Force` is omitted, PowerShell prompts for a confirmation.

```
Remove-EC2LaunchTemplate -LaunchTemplateId {{lt-0123456789example}} -Force
```

------

## Delete a launch template version
<a name="delete-launch-template-version"></a>

If you no longer require a launch template version, you can delete it.

**Considerations**
+ You can't replace the version number after you delete it.
+ You can't delete the default version of the launch template; you must first assign a different version as the default. If the default version is the only version for the launch template, you must [delete the entire launch template](#delete-launch-template).
+ When using the console, you can delete one launch template version at a time. When using the AWS CLI, you can delete up to 200 launch template versions in a single request. To delete more than 200 versions in a single request, you can [delete the launch template](#delete-launch-template), which also deletes all of its versions.

------
#### [ Console ]

**To delete a launch template version**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Launch Templates**.

1. Choose the launch template and choose **Actions**, **Delete template version**.

1. Choose the version to delete and choose **Delete**.

------
#### [ AWS CLI ]

**To delete a launch template version**  
Use the [delete-launch-template-versions](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-launch-template-versions.html) command and specify the version numbers to delete. You can specify up to 200 launch template versions to delete in a single request.

```
aws ec2 delete-launch-template-versions \
    --launch-template-id {{lt-0abcd290751193123}} \
    --versions {{1}}
```

------
#### [ PowerShell ]

**To delete a launch template version**  
Use the [Remove-EC2TemplateVersion](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-EC2TemplateVersion.html) cmdlet and specify the version numbers to delete. You can specify up to 200 launch template versions to delete in a single request.

```
Remove-EC2TemplateVersion `
    -LaunchTemplateId {{lt-0abcd290751193123}} `
    -Version {{1}}
```

------