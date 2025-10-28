# List and view distribution configuration detail

This section describes the various ways that you can find information and
view details for your EC2 Image Builder distribution configuration.

###### Distribution configuration detail

- [List distribution configurations from the console](#list-distribution-config-console "#list-distribution-config-console")
- [View distribution configuration details from the console](#view-distribution-config-details-console "#view-distribution-config-details-console")
- [List distributions from the AWS CLI](#cli-list-distributions "#cli-list-distributions")
- [Get
  distribution configuration detail from the AWS CLI](#cli-get-distribution-configuration "#cli-get-distribution-configuration")

## List distribution configurations from the console

To see a list of the distribution configurations created under your account
in the Image Builder console, follow these steps:

1. Open the EC2 Image Builder console at
   [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/ "https://console.aws.amazon.com/imagebuilder/").
2. Choose **Distribution settings**
   from the navigation pane. This shows a list of the
   distribution configurations that are created under your account.
3. To view details or create new distribution configuration, choose
   the **Configuration name** link. This opens the
   detail view for the distribution settings.

###### Note

You can also select the check box next to the
**Configuration name**, then choose
**View details**.

## View distribution configuration details from the console

To view details for a specific distribution configuration
using the Image Builder console, select the configuration to review, using the steps
described in [List distribution configurations from the console](#list-distribution-config-console "#list-distribution-config-console").

On the distribution detail page, you can:

- **Delete** the distribution configuration. For more information
  about deleting resources in Image Builder, see [Delete outdated or unused Image Builder resources](delete-resources.md "delete-resources.md").
- **Edit** distribution details.

## List distributions from the AWS CLI

The following example shows how to use the **[list-distribution-configurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-distribution-configurations.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-distribution-configurations.html")**
command in the AWS CLI to list all of your distributions.

```
aws imagebuilder list-distribution-configurations
```

## Get

distribution configuration detail from the AWS CLI

The following example shows how to use the **[get-distribution-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-distribution-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-distribution-configuration.html")**
command in the AWS CLI to get the details of a distribution configuration by specifying
its Amazon Resource Name (ARN).

```
aws imagebuilder get-distribution-configuration --distribution-configuration-arn arn:aws:imagebuilder:us-west-`2:123456789012`:distribution-configuration/`my-example-distribution-configuration`
```
