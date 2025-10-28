# Using tags to identify resources in your DevOps Guru

applications

You can use tags to identify the AWS resources that Amazon DevOps Guru analyzes and to specify which resources are grouped for monitoring with the selected tag key and tag values.
You can edit these configurations when you set up DevOps Guru or when you choose **Edit analyzed resources** from the **Analyzed resources** page.
After you select **Tags**, you choose a specific tag key that you want Amazon DevOps Guru to monitor.
To analyze all resources in the account and use tag values to group the resources, select **All Account Resources**. To use tag values to specify the resources for DevOps Guru to analyze, select **Choose specific tag values**.

###### Note

When **All Account Resources** is selected and no tag value exists, resources without the tag key are grouped and analyzed separately.

You use a tag's
_key_ to identify the resources, then use _values_ with that _key_ to group
resources into your applications. For example, you can tag your resources with the _key_
`devops-guru-applications`, then use that _key_ with a different
_value_ for each of your applications. You might use the tag _key_-_value_ pairs
`devops-guru-applications/database`,
`devops-guru-applications/cicd`, and
`devops-guru-applications/monitoring` to identify three applications in your
account. Each application is made up of related resources that contain the same tag
_key_-_value_ pair. You add tags to your resources using the AWS service to which
they belong. For more information, see [Adding AWS tags to AWS resources](#add-tags-to-aws-resources "#add-tags-to-aws-resources").

After you add a tag to the resources in your application, you can filter your insights by
the tags on resources that generated them. For more information about how to filter your
insights using a tag, see [Viewing DevOps Guru insights](working-with-insights.md#view-insights "working-with-insights.md#view-insights").

For more
information about the supported services and resources, see
[Amazon DevOps Guru pricing](https://aws.amazon.com/devops-guru/pricing/ "https://aws.amazon.com/devops-guru/pricing/").

###### Topics

- [What is an AWS tag?](#what-is-a-tag "#what-is-a-tag")
- [Defining a DevOps Guru
  application using a tag](#define-a-devops-guru-application-using-a-tag "#define-a-devops-guru-application-using-a-tag")
- [Using tags with DevOps Guru](#choose-tags "#choose-tags")
- [Adding AWS tags to AWS resources](#add-tags-to-aws-resources "#add-tags-to-aws-resources")

## What is an AWS tag?

Tags help you identify and organize your AWS resources. Many AWS services support
tagging, so you can assign the same tag to resources from different services to indicate
that the resources are related. For example, you can assign the same tag to an Amazon DynamoDB
table resource that you assign to an AWS Lambda function. For more information about
using tags, see the [Tagging
best practices](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf "https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf") whitepaper.

Each AWS tag has two parts.

- A tag _key_ (for example, `CostCenter`,
  `Environment`, `Project`, or `Secret`). Tag
  _keys_ are case-sensitive.
- An optional field known as a tag _value_ (for example,
  `111122223333`, `Production`, or a team
  name). Omitting the tag _value_ is the same as using an empty string. Like
  tag _keys_, tag _values_ are case-sensitive.

Together these are known as _key_-_value_ pairs.

## Defining a DevOps Guru

application using a tag

To define your Amazon DevOps Guru application using a tag, add that tag to the AWS resources
in your account that make up your application. Your tag contains a _key_ and a
_value_. We recommend that you add a tag to each of your AWS resources analyzed by
DevOps Guru that has the same _key_. Use a different _value_ in the tag to group
resources into your applications. For example, you might assign tags with the _key_
`devops-guru-analysis-boundary` to all the AWS resources in your
coverage boundary. Use different _values_ with that _key_ to identify
applications in your account. You might use the _values_ `containers`,
`database`, and `monitoring` for three applications. For more
information, see [Updating your AWS analysis coverage in DevOps Guru](update-settings.md#update-coverage "update-settings.md#update-coverage").

If you use AWS tags to specify which resources to analyze, you can use tags with
only one _key_. You can pair your tags' _key_ paired with any _value_. Use
the _value_ to group the resources that contain your _key_ into your operational
applications.

###### Important

When you create a _key_, the case of characters in the _key_ can be whatever you choose. After you create a _key_, it is case-sensitive.
For example, DevOps Guru works with a
_key_ named `devops-guru-rds` and a _key_ named
`DevOps-Guru-RDS`, and these act as two different _keys_. Possible _key_/_value_ pairs in your
application might be `Devops-Guru-production-application/RDS` or
`Devops-Guru-production-application/containers`.

## Using tags with DevOps Guru

Specify the AWS tags that identify the AWS resources that you want Amazon DevOps Guru to
analyze, or specify tag values that identify which resources will be grouped. These resources are your resource coverage boundary. You can choose one
_key_ and zero or more _values_.

###### To choose your tags

1. Open the Amazon DevOps Guru console at [https://console.aws.amazon.com/devops-guru/](https://console.aws.amazon.com/devops-guru/ "https://console.aws.amazon.com/devops-guru/").
2. Open the navigation pane, then expand **Settings**.
3. In **Analyzed resources**, choose
   **Edit**.
4. Choose **Tags** if you want DevOps Guru to analyze all
   resources that contain the tags you choose. Choose a _key_, then
   choose one of the following options.
   - **All account resources** – Analyze all AWS resources in the current Region and account.
     Resources with the selected tag key are grouped by tag value, if any exist.
     Resources without this tag key are grouped and analyzed separately.
   - **Choose specific tag values** – All resources that
     contain a tag with the _key_ you chose are analyzed. DevOps Guru groups your
     resources into applications by your tag's _values_.

5. Choose **Save**.

## Adding AWS tags to AWS resources

When you specify the AWS tags that identify the AWS resources that you want DevOps Guru to analyze, choose tags that have resources
associated with them. You can add tags to your resources using the AWS service to which each resource
belongs, or using the AWS Tag Editor.

- To manage tags using your resources' service, use the console, AWS Command Line Interface, or
  SDK of the service to which a resource belongs. For example, you can tag an
  Amazon Kinesis stream resource or an Amazon CloudFront distribution resource. These are two
  examples of services with resources that can be tagged. Most resources that
  DevOps Guru can analyze support tags. For more information, see [Tagging your
  streams](../../../streams/latest/dev/tagging.md "../../../streams/latest/dev/tagging.md") in the _Amazon Kinesis Developer Guide_ and
  [Tagging a
  distribution](../../../AmazonCloudFront/latest/DeveloperGuide/tagging.md "../../../AmazonCloudFront/latest/DeveloperGuide/tagging.md") in the _Amazon CloudFront Developer Guide_.
  To learn how to add tags to other types of resources, see the user guide or
  developer guide for the AWS service to which they belong.

###### Note

When you tag Amazon RDS resources, you must tag the database instance and not the cluster.

- You can use the AWS Tag Editor to manage tags by resources in your Region
  and by resources in specific AWS services. For more information, see [Tag
  editor](../../../ARG/latest/userguide/tag-editor.md "../../../ARG/latest/userguide/tag-editor.md") in the _AWS Resource Group and Tags User
  Guide_.

When you add a tag to a resource, you can add the _key_ only, or the _key_ and
a _value_. For example, you can create a tag with the _key_ `devops-guru-`
for all the resources that are part of your DevOps application. You can also add a tag
with the _key_ `devops-guru-` and the _value_ `RDS`, then add
that _key_-_value_ pair to only the Amazon RDS resources in your application. This is
useful if you want to view insights in the console that are generated from only the
Amazon RDS resources in your application.
