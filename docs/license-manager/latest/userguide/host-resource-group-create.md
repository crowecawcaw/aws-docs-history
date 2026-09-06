

# Create a host resource group in License Manager
<a name="host-resource-group-create"></a>

Configure a host resource group to enable License Manager to manage your Dedicated Hosts. You can create a host resource group with or without license tracking. To track license usage, associate one or more core- or socket-based self-managed licenses with your host resource group. To manage Dedicated Hosts without license tracking (for example, for Mac workloads), choose the option that does not require license configurations.

------
#### [ Console ]

**To create a host resource group**

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/).

1. In the left navigation pane, choose **Host resource groups**.

1. Choose **Create host resource group**.

1. For **Host resource group details**, specify a name and description for the host resource group.

1. For **EC2 Dedicated Host management settings**, enable or disable the following settings as needed:
   + **Allocate hosts automatically**
   + **Release hosts automatically**
   + **Recover hosts automatically**

1. For **Instance launch option**, choose one of the following:
   + **License configuration required** (default) – Instances must have license configurations to launch. Choose this for BYOL workloads.
   + **License configuration not required** – Instances can launch with any AMI and do not require you to set up a license configuration. This option is better suited for workloads that do not require license tracking, such as Mac workloads.

   If you chose **License configuration required**, for **Self-managed licenses**, select one or more core- or socket-based self-managed licenses.

1. (Optional) For **Additional settings**, select the instance families that you can launch in the host resource group.

1. (Optional) For **Tags**, add one or more tags.

1. Choose **Create**.

------
#### [ AWS CLI ]

To create a host resource group from the AWS CLI, use the [create-group](https://docs.aws.amazon.com/cli/latest/reference/resource-groups/create-group.html) command in AWS Resource Groups. Specify the host resource group settings in the `--configuration` parameter.

**Example: Create a host resource group that requires license configurations**  
The following example creates a host resource group that allows only the specified license configuration, has auto-allocate, auto-release, and auto-recovery enabled, and is restricted to the `c5` instance family.

```
aws resource-groups create-group \
    --name {{MyLicensedHostGroup}} \
    --description "{{HRG for BYOL workloads}}" \
    --configuration '[
        {
            "Type": "AWS::EC2::HostManagement",
            "Parameters": [
                {"Name": "allowed-host-based-license-configurations",
                 "Values": ["{{arn:aws:license-manager:us-east-1:123456789012:license-configuration:lic-abc123}}"]},
                {"Name": "allowed-host-families", "Values": ["{{c5}}"]},
                {"Name": "auto-allocate-host", "Values": ["true"]},
                {"Name": "auto-release-host", "Values": ["true"]},
                {"Name": "auto-host-recovery", "Values": ["true"]}
            ]
        },
        {
            "Type": "AWS::ResourceGroups::Generic",
            "Parameters": [
                {"Name": "allowed-resource-types", "Values": ["AWS::EC2::Host"]},
                {"Name": "deletion-protection", "Values": ["UNLESS_EMPTY"]}
            ]
        }
    ]'
```

**Example: Create a host resource group that does not require license configurations**  
The following example creates a host resource group that does not require license configurations. Instances can launch with any AMI. Auto-allocate, auto-release, and auto-recovery are enabled.

```
aws resource-groups create-group \
    --name {{MyMacHostGroup}} \
    --description "{{HRG for Mac workloads}}" \
    --configuration '[
        {
            "Type": "AWS::EC2::HostManagement",
            "Parameters": [
                {"Name": "instance-launch-option", "Values": ["LICENSE_CONFIGURATION_NOT_REQUIRED"]},
                {"Name": "auto-allocate-host", "Values": ["true"]},
                {"Name": "auto-release-host", "Values": ["true"]},
                {"Name": "auto-host-recovery", "Values": ["true"]}
            ]
        },
        {
            "Type": "AWS::ResourceGroups::Generic",
            "Parameters": [
                {"Name": "allowed-resource-types", "Values": ["AWS::EC2::Host"]},
                {"Name": "deletion-protection", "Values": ["UNLESS_EMPTY"]}
            ]
        }
    ]'
```

------