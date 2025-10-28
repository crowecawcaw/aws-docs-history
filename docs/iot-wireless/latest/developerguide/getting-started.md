# Getting started with AWS IoT Wireless

You can get started with AWS IoT Wireless by signing up for an AWS account and following
the steps to create an IAM user. After you've signed up, you can then use the AWS Management Console, the
AWS IoT Wireless API, or the AWS CLI to onboard your Sidewalk and LoRaWAN devices and
gateways. When onboarding your devices, consider how to describe and tag your resources to help
you identify them more easily.

The following sections show how to get started with AWS IoT Wireless.

###### Topics

- [Setting up AWS IoT Wireless](#setting-up-iotwireless "#setting-up-iotwireless")
- [Describing your AWS IoT Wireless
  resources](#iotwireless-describe-resources "#iotwireless-describe-resources")

## Setting up AWS IoT Wireless

When you sign up for AWS, your AWS account is automatically signed up for all services in
AWS, including AWS IoT Wireless. You are charged only for the services that you use.

To set up AWS IoT Wireless, perform the steps in the following section:

###### Topics

- [Set up your AWS account and the AWS CLI](#iotwireless-setup-account "#iotwireless-setup-account")
- [Installing Python and Python3-pip](#wireless-onboard-prereq "#wireless-onboard-prereq")
- [Installing boto3 (AWS SDK for Python)](#wireless-prereq-cli "#wireless-prereq-cli")

### Set up your AWS account and the AWS CLI

Before you use AWS IoT Core for LoRaWAN or AWS IoT Core for Amazon Sidewalk for the first time, you must set up your
AWS account and AWS CLI. For detailed steps, see [Setting up your AWS
environment](https://aws.amazon.com/getting-started/guides/setup-environment/ "https://aws.amazon.com/getting-started/guides/setup-environment/").

### Installing Python and Python3-pip

Before you connect your LoRaWAN or Sidewalk end device, you must set up and install
Python.

###### Note

To use the AWS CLI and boto3 as described in the next section, you must use a Python version
3.6 or later. If you want to onboard your end devices using the AWS IoT console, you can skip this
section.

To check whether you’ve already installed Python and Python3-pip, run the following
commands. If running these commands return the version, it means that Python and Python3-pip have
been installed correctly.

```
python3 -V
pip3 --version
```

If this command returns an error, it might be because Python is not installed, or your
operating system calls the Python v3.x executable as Python3. In that case, replace all instances
of `python` with `python3` when you run the commands. If it still produces
an error, either download and run the [Python
installer](https://www.python.org/downloads/ "https://www.python.org/downloads/"), or install Python depending on your operating system as described below.

Windows
On your Windows machine, download Python from the [Python website](https://www.python.org/downloads/windows/ "https://www.python.org/downloads/windows/") and then run the
installer to install Python on your machine.

Linux
On your Ubuntu machine, run the following `sudo` command to install
Python.

```
sudo apt install python3
sudo apt install python3-pip
```

macOS
On your Mac machine, use Homebrew to install Python. Homebrew also installs pip, which
then points to the installed Python3 version.

```
$ brew install python
```

### Installing boto3 (AWS SDK for Python)

The following steps show you how to configure boto3 (AWS SDK for Python). Before you
follow these steps, you must sign up for an AWS account and create an administrative user. For
instructions, see [Setting up AWS IoT Wireless](#setting-up-iotwireless "#setting-up-iotwireless").

1. ###### Install boto3 (AWS SDK for Python)

The following commands show you how to install boto3 (AWS SDK for Python) and the AWS CLI.
You'll also install botocore, which is required to run boto3. For detailed instructions, see
[Installing Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation") in the _Boto3 Documentation
Guide_.

###### Note

`awscli` version `1.26.6` requires PyYAML version that's 3.10 or
later, but not later than 5.5.

```
python3 -m pip install botocore-`version`-py3-none-any.whl
python3 -m pip install boto3-`version`-py3-none-any.whl
```

2. ###### Configure your credentials and default Region

Configure your credentials and default Region in the `~/.aws/credentials` and
`~/.aws/config` files. The boto3 library uses these credentials to identify your
AWS account and authorize API calls. For configuration instructions, see:

    * [Configuration](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration") in the *Boto3 Documentation
     Guide*
    * [Configuration and credentials file settings](../../../cli/latest/userguide/cli-configure-files.md "../../../cli/latest/userguide/cli-configure-files.md") in the *AWS CLI
     Documentation Guide*

## Describing your AWS IoT Wireless

resources

Before you get started with onboarding your LoRaWAN or Sidewalk devices, consider
the naming convention of your devices, gateways, and destination. AWS IoT Wireless provides
several options to help you identify the resources you create. While AWS IoT Wireless resources
are given a unique ID when they're created, this ID is not descriptive nor can it be changed
after the resource is created. To make it more convenient to select, identify, and manage your
resources, you can assign a name, add a description, and attach tags and tag values to most
AWS IoT Wireless resources.

- ###### [Resource names and description](#wireless-describe-resource-names "#wireless-describe-resource-names")

For devices, gateways, and profiles, the resource name is an optional field that you can
change after the resource is created. The name appears in the lists displayed on the resource
hub pages. For destinations, you provide a name that is unique in your AWS account and
AWS Region. You can't change the destination name after you create the destination
resource.

###### Note

While a name can have up to 256 characters, the display space in the resource hub is
limited. Make sure that the distinguishing part of the name appears in the first 20 to 30
characters, if possible.

- ###### [Resource tags](#wireless-describe-resource-tags "#wireless-describe-resource-tags")

Tags are key-value pairs of metadata that can be attached to AWS resources. You choose
both tag keys and their corresponding values. Gateways, destinations, and profiles can have up
to 50 tags attached to them. Devices don't support tags.

### Resource names and description

| AWS IoT Wireless resource support for name | Resource                                                    | Name field support                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------ | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- | --------------- |
| Destination                                | Name is unique ID of resource and can't be changed.         |
| Wireless device                            | Name is optional descriptor of resource and can be changed. |
| LoRaWAN gateway                            | Name is optional descriptor of resource and can be changed. |
| Profile                                    | Name is optional descriptor of resource and can be changed. | The name field appears in resource hub lists of resources; however, the space is limited and so only the first 15-30 characters of the name might be visible. When selecting names for your resources, consider how you want them to identify the resources and how they'll be displayed in the console. ###### Description Destination, device, and gateway resources also support a description field, which can accept up to 2,048 characters. The description field appears only in the individual resource's detail page. While the description field can hold a lot of information, because it only appears in the resource's detail page, it isn't convenient for scanning in the context of multiple resources. ### Resource tags AWS IoT Wireless resource support for AWS tags                                                                                                                                             | Resource | AWS tag support |
| ---                                        | ---                                                         |
| Destination                                | Up to 50 AWS tags can be added to the resource.             |
| Wireless device                            | This resource doesn't support AWS tags.                     |
| LoRaWAN gateway                            | Up to 50 AWS tags can be added to the resource.             |
| Profile                                    | Up to 50 AWS tags can be added to the resource.             | Tags are words or phrases that act as metadata that you can use to identify and organize your AWS resources. You can think of the tag key as a category of information and the tag value as a specific value in that category. For example, you might have a tag value of _color_ and then give some resources a value of _blue_ for that tag and others a value of _red_. With that, you could use the [Tag editor](../../../ARG/latest/userguide/tag-editor.md "../../../ARG/latest/userguide/tag-editor.md") in the AWS console to find the resources with a _color_ tag value of _blue_. For more information about tagging in AWS IoT Wireless, see [Tagging your AWS IoT Wireless resources](tagging-iotwireless.md "tagging-iotwireless.md"). For more information about tagging and tagging strategies, see [Tag editor](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md"). |
