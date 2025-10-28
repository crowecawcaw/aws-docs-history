# Configure AMI distribution with

an EC2 launch template

To help ensure a consistent launch experience for your Image Builder AMI in target accounts
and Regions, you can specify an Amazon EC2 launch template in your distribution settings,
using `launchTemplateConfigurations`. When `launchTemplateConfigurations`
are present during the distribution process, Image Builder creates a new version of the launch template that
includes all of the original settings from the template, and the new AMI ID from the build.
For more information about launching an EC2 instance using a launch template, see one of
the following links, depending on your target operating system.

- [Launch a Linux instance
  from a launch template](../../../AWSEC2/latest/UserGuide/ec2-launch-templates.md "../../../AWSEC2/latest/UserGuide/ec2-launch-templates.md")
- [Launch a Windows instance
  from a launch template](../../../AWSEC2/latest/UserGuide/ec2-launch-templates.md "../../../AWSEC2/latest/UserGuide/ec2-launch-templates.md")

###### Note

When you include a launch template to enable Windows Fast Launch in your image, the launch
template must include the following tag so that Image Builder can enable Windows Fast Launch on your behalf.

`CreatedBy: EC2 Image Builder`

## Add an EC2 launch template to AMI

distribution settings from the console

To provide a launch template with your output AMI, follow these steps in the console:

1. Open the EC2 Image Builder console at
   [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/ "https://console.aws.amazon.com/imagebuilder/").
2. Choose **Distribution settings**
   from the navigation pane. This shows a list of the
   distribution settings that are created under your account.
3. At the top of the **Distribution settings** page, choose
   **Create distribution settings**. This opens the
   **Create distribution settings** page.
4. In the **Image type** section, choose the
   **Amazon Machine Image (AMI)** **Output
   type**. This is the default setting.
5. In the **General** section, enter the **Name** of the
   distribution settings resource that you want to create
   (_required_).
6. In the **Region settings** section, select the name of an EC2 launch
   template from the list. If there are no launch templates in your account,
   choose **Create new launch template**, which opens the
   **Launch Templates** in the **EC2
   Dashboard**.

Select the **Set the default version** check
box to update the launch template default version to the new
version that Image Builder creates with your output AMI.

To add another launch template to the selected Region, choose
**Add launch template configuration**.

To remove a launch template, choose **Remove**. 7. Continue specifying any additional settings that you require, and choose
**Create settings** to create your new distribution
settings resource.

## Add an EC2 launch template to

AMI distribution settings from the AWS CLI

This section describes how to configure a distribution settings file with a
launch template, and use the **create-image** command in the AWS CLI
to build and distribute an Image Builder AMI and a new version of the launch template
that uses it.

1. ###### Configure a distribution settings file

Before you can create an Image Builder AMI with a launch template, using the AWS CLI,
you must create a distribution configuration JSON structure that specifies
the `launchTemplateConfigurations` settings. You must specify at least
one `launchTemplateConfigurations` entry in the source Region.

The following sample file, named
`create-distribution-config-launch-template.json`,
shows a few possible scenarios for launch template configuration in the
source Region.

```
{
    "name": "NewDistributionConfiguration",
    "description": "This is just a test",
    "distributions": [
        {
            "region": "us-west-2",
            "amiDistributionConfiguration": {
                "name": "test-{{imagebuilder:buildDate}}-{{imagebuilder:buildVersion}}",
                "description": "description"
            },
            "launchTemplateConfigurations": [
                {
                    "launchTemplateId": "lt-0a1bcde2fgh34567",
                    "accountId": "935302948087",
                    "setDefaultVersion": true
                },
                {
                    "launchTemplateId": "lt-0aaa1bcde2ff3456"
                },
                {
                    "launchTemplateId": "lt-12345678901234567",
                    "accountId": "123456789012"
                }
            ]
        }
    ],
    "clientToken": "clientToken1"
}
```

2. ###### Create the distribution settings

To create an Image Builder distribution settings resource using the
[create-distribution-configuration](../../../cli/latest/reference/imagebuilder/create-distribution-configuration.md "../../../cli/latest/reference/imagebuilder/create-distribution-configuration.md")
command in the AWS CLI, provide the following parameters in the command:

    * Enter the name of the distribution in the `--name` parameter.
    * Attach the distribution configuration JSON file you created in the
     `--cli-input-json` parameter.

```
`aws imagebuilder create-distribution-configuration --name `my distribution name`--cli-input-json file://`create-distribution-config-launch-template.json``
```

###### Note

    * You must include the `file://` notation
     at the beginning of the JSON file path.
    * The path for the JSON file should follow the appropriate
     convention for the base operating system where you are running
     the command. For example, Windows uses the backslash (\) to
     refer to the directory path, while Linux and macOS use the forward slash (/).

_You can also provide JSON directly in the command, using the
`--distributions` parameter._
