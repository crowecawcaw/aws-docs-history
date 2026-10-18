

# List and view distribution configuration detail
<a name="distribution-settings-detail"></a>

This section describes the various ways that you can find information and view details for your EC2 Image Builder distribution configuration.

**Topics**
+ [List distribution configurations](#list-distribution-config)
+ [Get distribution configuration details](#get-distribution-config-detail)
+ [Delete a distribution configuration](#delete-distribution-config)

## List distribution configurations
<a name="list-distribution-config"></a>

List the distribution configurations that are created under your account from the AWS Management Console, the AWS CLI, or AWS Tools for PowerShell.

------
#### [ AWS Management Console ]

To see a list of the distribution configurations created under your account in the Image Builder console, follow these steps:

1. Open the EC2 Image Builder console at [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/).

1. Choose **Distribution settings** from the navigation pane. This shows a list of the distribution configurations that are created under your account.

------
#### [ AWS CLI ]

The following example shows how to use the [list-distribution-configurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-distribution-configurations.html) command in the AWS CLI to list all of your distribution configurations.

```
aws imagebuilder list-distribution-configurations
```

You can filter the list by distribution configuration `name`, which is the only supported filter. To page through results, use the `--page-size`, `--max-items`, and `--starting-token` options. The `--page-size` value can't exceed 25.

```
aws imagebuilder list-distribution-configurations --filters name=name,values={{MyExampleDistribution}}
```

------
#### [ PowerShell ]

The following example shows how to use the [Get-EC2IBDistributionConfigurationList](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2IBDistributionConfigurationList.html) cmdlet to list all of your distribution configurations:

```
Get-EC2IBDistributionConfigurationList
```

------

## Get distribution configuration details
<a name="get-distribution-config-detail"></a>

View the details for a specific distribution configuration from the AWS Management Console, the AWS CLI, or AWS Tools for PowerShell.

------
#### [ AWS Management Console ]

To view details for a specific distribution configuration in the Image Builder console, follow these steps:

1. Open the EC2 Image Builder console at [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/).

1. Choose **Distribution settings** from the navigation pane. This shows a list of the distribution configurations that are created under your account.

1. To open the detail view, choose the **Configuration name** link.
**Note**  
You can also select the check box next to the **Configuration name**, then choose **View details**.

On the distribution detail page, you can also **Edit** the distribution details, or **Delete** the distribution configuration.

------
#### [ AWS CLI ]

The following example shows how to use the [get-distribution-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-distribution-configuration.html) command in the AWS CLI to get the details of a distribution configuration by specifying its ARN.

```
aws imagebuilder get-distribution-configuration --distribution-configuration-arn arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:distribution-configuration/{{my-example-distribution-configuration}}
```

------
#### [ PowerShell ]

The following example shows how to use the [Get-EC2IBDistributionConfiguration](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2IBDistributionConfiguration.html) cmdlet to get the details of a distribution configuration by specifying its ARN:

```
Get-EC2IBDistributionConfiguration -DistributionConfigurationArn arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:distribution-configuration/{{my-example-distribution-configuration}}
```

------

## Delete a distribution configuration
<a name="delete-distribution-config"></a>

Delete a distribution configuration from the AWS Management Console or the AWS CLI.

**Note**  
You can't delete a distribution configuration that an image pipeline still references. Update or delete the pipeline first. For more information about deleting resources in Image Builder, see [Delete outdated or unused Image Builder resources](delete-resources.md).

------
#### [ AWS Management Console ]

To delete a distribution configuration in the Image Builder console, follow these steps:

1. Open the EC2 Image Builder console at [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/).

1. Choose **Distribution settings** from the navigation pane. This shows a list of the distribution configurations that are created under your account.

1. Choose the **Configuration name** link to open the detail view for the distribution configuration that you want to delete.

1. Choose **Delete**, and then confirm the deletion.

------
#### [ AWS CLI ]

The following example shows how to use the [delete-distribution-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/delete-distribution-configuration.html) command to delete a distribution configuration by specifying its ARN.

```
aws imagebuilder delete-distribution-configuration --distribution-configuration-arn arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:distribution-configuration/{{my-example-distribution-configuration}}
```

------