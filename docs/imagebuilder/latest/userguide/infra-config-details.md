# List and view infrastructure configuration details

This section describes the various ways that you can
find information and view details for your EC2 Image Builder
infrastructure configurations.

###### Infrastructure configuration details

- [List infrastructure configurations](#list-infrastructure-configurations "#list-infrastructure-configurations")
- [Get infrastructure configuration details](#get-infrastructure-configuration-details "#get-infrastructure-configuration-details")

## List infrastructure configurations

Console
To see a list of the infrastructure configurations created
under your account in the Image Builder console, follow these
steps:

1. Open the EC2 Image Builder console at
   [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/ "https://console.aws.amazon.com/imagebuilder/").
2. Choose **Infrastructure
   configuration** from the navigation pane.
   This shows a list of the infrastructure configurations
   that are created under your account.

AWS CLI
The following example shows how to list all of your
infrastructure configurations, using the **[list-infrastructure-configurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-infrastructure-configurations.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-infrastructure-configurations.html")**
command in the AWS CLI.

```
aws imagebuilder list-infrastructure-configurations
```

To narrow the results, use the `--filters` option. You can filter
by `name`. The following example returns infrastructure
configurations whose name matches the value that you specify.

```
aws imagebuilder list-infrastructure-configurations --filters name=name,values=`my-example-infrastructure-configuration`
```

If you have many infrastructure configurations, Image Builder returns results one page
at a time. Use `--max-results` to control the page size. If the
response includes a `nextToken` value, pass it with
`--next-token` to retrieve the next page.

```
aws imagebuilder list-infrastructure-configurations --max-results 10
```

## Get infrastructure configuration details

Console
To view the details for a specific infrastructure
configuration in the Image Builder console, follow these steps:

1. Open the EC2 Image Builder console at
   [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/ "https://console.aws.amazon.com/imagebuilder/").
2. Choose **Infrastructure
   configuration** from the navigation
   pane.
3. Choose the **Configuration name**
   link for the infrastructure configuration that you
   want to view. This opens the detail page, where you
   can review its settings.

AWS CLI
The following example shows how to use the **[get-infrastructure-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-infrastructure-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-infrastructure-configuration.html")**
command in the AWS CLI to get the details of an infrastructure configuration by specifying its Amazon Resource
Name (ARN).

```
aws imagebuilder get-infrastructure-configuration --infrastructure-configuration-arn arn:aws:imagebuilder:`us-west-2`:`123456789012`:infrastructure-configuration/`my-example-infrastructure-configuration`
```
