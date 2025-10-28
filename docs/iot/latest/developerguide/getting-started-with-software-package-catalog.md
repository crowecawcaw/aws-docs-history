# Getting started with Software Package Catalog

You can build and maintain the AWS IoT Device Management Software Package Catalog through the AWS Management Console,
AWS IoT Core API operations, and AWS Command Line Interface (AWS CLI).

###### Note

Enabling AWS IoT fleet indexing is a requirement to use Software Package Catalog. Basic operations
such as creating a software package version in the AWS Management Console and using the
`CreatePackage` API command will fail without AWS IoT fleet indexing
enabled.

For more information on using AWS IoT fleet indexing with Software Package Catalog, see [Preparing fleet indexing](preparing-fleet-indexing.md "preparing-fleet-indexing.md").

**Using the console**

To use the AWS Management Console, sign into your AWS account and navigate to
[AWS IoT Core](https://console.aws.amazon.com/iot/home "https://console.aws.amazon.com/iot/home").
In the navigation pane, choose **Software packages**.
You can then create and manage packages and their versions from this section.

**Using API or CLI operations**

You can use the AWS IoT Core API operations to create and manage Software Package Catalog features.
For more information, see [AWS IoT API Reference](../apireference.md "../apireference.md") and
[AWS SDKs and Toolkits](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/").
The AWS CLI commands also manage your catalog. For more information, see the
[AWS IoT CLI Command Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/index.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/index.html").

###### This chapter contains the following sections:

- [Creating a software package and package version](creating-package-and-version.md "creating-package-and-version.md")
- [Deploying a package version through AWS IoT jobs](deploying-package-version.md "deploying-package-version.md")
- [Associating a package version to an AWS IoT thing](associating-package-version.md "associating-package-version.md")
