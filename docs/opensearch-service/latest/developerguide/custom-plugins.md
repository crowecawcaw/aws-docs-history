# Managing custom plugins in Amazon OpenSearch Service

Using custom plugins for OpenSearch Service, you can extend OpenSearch functionality in areas like
language analysis, custom filtering, ranking and more, making it possible for you to craft
personalized search experiences. Custom plugins for OpenSearch can be developed by extending
the `org.opensearch.plugins.Plugin` class and then packaging it in a
`.zip` file.

The following plugin extensions are currently supported by Amazon OpenSearch Service:

- **AnalysisPlugin** – Extends analysis
  functionality by adding, for example, custom analyzers, character tokenizers, or filters
  for text processing.
- **SearchPlugin** – Enhances search capabilities
  with custom query types, similarity algorithms, suggestion options, and
  aggregations.
- **MapperPlugin** – Allows you to create custom field
  types and their mapping configurations in OpenSearch, enabling you to define how
  different types of data should be stored and indexed.
- **ScriptPlugin** – Allows you to add custom scripting
  capabilities to OpenSearch, for example, custom scripts for operations like scoring,
  sorting, and field value transformations during search or indexing.
  You can use the OpenSearch Service console or existing API commands for custom packages to upload and
  associate the plugin with the Amazon OpenSearch Service cluster. You can also use the [DescribePackages](../APIReference/API_DescribePackages.md "../APIReference/API_DescribePackages.md") command to describe all the packages in your account and to view
  details such as OpenSearch version and error details. OpenSearch Service validates plugin package for
  version compatibility, security vulnerabilities, and permitted plugin operations. For more
  information about custom packages, see [Importing and managing packages in Amazon OpenSearch Service](custom-packages.md "custom-packages.md").

###### OpenSearch version and AWS Region support

Custom plugins are supported on OpenSearch Service domains that are running OpenSearch version 2.15
in the following AWS Regions:

- US East (Ohio) (us-east-2)
- US East (N. Virginia) (us-east-1)
- US West (Oregon) (us-west-2)
- Asia Pacific (Mumbai) (ap-south-1)
- Asia Pacific (Seoul) (ap-northeast-2)
- Asia Pacific (Singapore) (ap-southeast-1)
- Asia Pacific (Sydney) (ap-southeast-2)
- Asia Pacific (Tokyo) (ap-northeast-1)
- Canada (Central) (ca-central-1)
- Europe (Frankfurt) (eu-central-1)
- Europe (Ireland) (eu-west-1)
- Europe (London) (eu-west-2)
- Europe (Paris) (eu-west-3)
- South America (São Paulo) (sa-east-1)

###### Note

Custom plugins contain user-developed code. Any issues, including SLA breaches, caused
by user developed code aren't eligible for SLA credits. For more information, see [Amazon OpenSearch Service - Service Level
Agreement](https://aws.amazon.com/opensearch-service/sla/ "https://aws.amazon.com/opensearch-service/sla/").

###### Topics

- [Plugin quotas](#plugin-limits "#plugin-limits")
- [Prerequisites](#custom-plugin-prerequisites "#custom-plugin-prerequisites")
- [Troubleshooting](#custom-plugin-troubleshooting "#custom-plugin-troubleshooting")
- [Installing a custom plugin using the
  console](#custom-plugin-install-console "#custom-plugin-install-console")
- [Managing custom plugins using the
  AWS CLI](#managing-custom-plugins-cli "#managing-custom-plugins-cli")
- [Amazon OpenSearch Service custom package AWS KMS
  integration](custom-package-kms-integration.md "custom-package-kms-integration.md")

## Plugin quotas

- You can create up to 25 custom plugins per account per Region.
- The maximum uncompressed size for a plugin is 1 GB.
- The maximum number of plugins that can be associated with a single domain is 20.
  This quota applies to all plugin types combined: optional, third-party, and
  custom.
- Custom plugins are supported on domains running OpenSearch version 2.15 or
  later.
- The `descriptor.properties` file for your plugin must support an engine
  version similar to 2.15.0 or any 2.x.x version, where the patch version is set to
  zero.

## Prerequisites

Before you install a custom plugin and associate it to a domain, make sure you meet the
following requirements:

- The supported engine version for the plugin in the
  `descriptor.properties` file should be similar to
  `2.15.0` or `2.*x*.0`. That is,
  the patch version must be zero.
- The following features must be enabled on your domain:
  - [Node-to-node encryption](ntn.md "ntn.md")
  - [Encryption at rest](encryption-at-rest.md "encryption-at-rest.md")
  - [EnforceHTTPS is set to
    'true'](createupdatedomains.md "createupdatedomains.md")

  See also [opensearch-https-required](../../../config/latest/developerguide/opensearch-https-required.md "../../../config/latest/developerguide/opensearch-https-required.md") in the
  _AWS Config Developer Guide_.
  - Clients must support **Policy-Min-TLS-1-2-PFS-2023-10**. You can specify this support using the
    following command. Replace the `placeholder value` with
    your own information:

  ```
  aws opensearch update-domain-config \
      --domain-name `domain-name` \
      --domain-endpoint-options '{"TLSSecurityPolicy":"Policy-Min-TLS-1-2-PFS-2023-10" }'
  ```

  For more information, see [DomainEndpointOptions](../APIReference/API_DomainEndpointOptions.md "../APIReference/API_DomainEndpointOptions.md") in the _Amazon OpenSearch Service API
  Reference_.

## Troubleshooting

If the system returns the error `PluginValidationFailureReason : The provided
 plugin could not be loaded`, see [Custom plugin installation fails due to
version compatibility](handling-errors.md#troubleshooting-custom-plugins "handling-errors.md#troubleshooting-custom-plugins")
for troubleshooting information.

## Installing a custom plugin using the

console

To associate a third-party plugin to a domain, first import the plugin license and
configuration as packages.

###### To install a custom plugin

1. Sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home "https://console.aws.amazon.com/aos/home").
2. In the left navigation pane, choose **Packages**.
3. Choose **Import package**.
4. For **Name**, enter a unique, easily identifiable name for the
   plugin.
5. (Optional) For **Description**, provide any useful details about
   the package or its purpose.
6. For **Package type**, choose **Plugin**.
7. For **Package source**, enter the path or browse to the plugin ZIP
   file in Amazon S3.
8. For **OpenSearch engine version**, choose the version of
   OpenSearch that the plugin supports.
9. For **Package encryption**, choose whether to customize the
   encryption key for the package. By default, OpenSearch Service encrypts the plugin package with an
   AWS owned key. You can use a customer managed key instead.
10. Choose **Import**.

After you import the plugin package, associate it with a domain. For instructions, see
[Import and associate a package to a domain](custom-packages.md#associate-console "custom-packages.md#associate-console").

## Managing custom plugins using the

AWS CLI

You can use the AWS CLI to manage a number of custom plugin tasks.

###### Tasks

- [Installing a custom plugin using the
  AWS CLI](#custom-plugin-install-cli "#custom-plugin-install-cli")
- [Updating a custom plugin using the
  AWS CLI](#custom-plugin-update-cli "#custom-plugin-update-cli")
- [Create or update a custom plugin with
  an AWS KMS key security](#custom-plugin-kms-key-security-cli "#custom-plugin-kms-key-security-cli")
- [Upgrading an OpenSearch Service domain with custom
  plugins to a later version of OpenSearch using the AWS CLI](#custom-plugin-domain-upgrade-cli "#custom-plugin-domain-upgrade-cli")
- [Uninstalling and viewing the dissociation
  status of a custom plugin](#custom-plugin-uninstall-cli "#custom-plugin-uninstall-cli")

### Installing a custom plugin using the

AWS CLI

###### Before you begin

Before you can associate a custom plugin with your domain, you must upload it to an
Amazon Simple Storage Service (Amazon S3) bucket. The bucket must be located in the same AWS Region where you
intend to use the plugin. For information about adding an object to an S3 bucket, see
[Uploading objects](../../../AmazonS3/latest/userguide/upload-objects.md "../../../AmazonS3/latest/userguide/upload-objects.md") in the _Amazon Simple Storage Service User Guide_.

If your plugin contains sensitive information, specify server-side encryption with
S3-managed keys when you upload it. After you upload the file, make note of its S3 path.
The path format is
`s3://`amzn-s3-demo-bucket`/`file-path`/file-name`.

###### Note

You can optionally secure a custom plugin when you create the plugin by specifying
an AWS Key Management Service (AWS KMS) key. For information, see [Create or update a custom plugin with
an AWS KMS key security](#custom-plugin-kms-key-security-cli "#custom-plugin-kms-key-security-cli").

###### To install a custom plugin using the AWS CLI

1.  Create a new package for your custom plugin by running the following [create-package](../../../cli/latest/reference/opensearch/create-package.md "../../../cli/latest/reference/opensearch/create-package.md") command, ensuring that the following requirements are
    met:

        * The bucket and key location must point to the plugin `.zip`
         file in an S3 bucket in the account in which your are running the commands.
        * The S3 bucket must be in the same Region where the package is being created.
        * Only `.zip` files are supported for `ZIP-PLUGIN`
         packages.
        * The contents of the `.zip` file must follow directory
         structure as expected by the plugin.
        * The value for `--engine-version` must be in the format
         `OpenSearch_`{MAJOR}`.`{MINOR}``.
         For example: `OpenSearch_2.17`.

    Replace the `placeholder values` with your own
    information:

```
aws opensearch create-package \
    --package-name `package-name` \
    --region `region` \
    --package-type ZIP-PLUGIN \
    --package-source S3BucketName=`amzn-s3-demo-bucket`,S3Key=`s3-key` \
    --engine-version `opensearch-version`
```

2. (Optional) View the status of the `create-package` operation, including
   any validation and security vulnerability findings, by using the [describe-packages](../../../cli/latest/reference/es/describe-packages.md "../../../cli/latest/reference/es/describe-packages.md") command. Replace the `placeholder
values` with your own information:

```
aws opensearch describe-packages \
    --region `region`  \
    --filters '[{"Name": "PackageType","Value": ["ZIP-PLUGIN"]}, {"Name": "PackageName","Value": ["`package-name`"]}]'
```

The command returns information similar to the following:

```
{
    "PackageDetailsList": [{
        "PackageID": "pkg-identifier",
        "PackageName": "package-name",
        "PackageType": "ZIP-PLUGIN",
        "PackageStatus": "VALIDATION_FAILED",
        "CreatedAt": "2024-11-11T13:07:18.297000-08:00",
        "LastUpdatedAt": "2024-11-11T13:10:13.843000-08:00",
        "ErrorDetails": {
            "ErrorType": "",
            "ErrorMessage": "PluginValidationFailureReason : Dependency Scan reported 3 vulnerabilities for the plugin: CVE-2022-23307, CVE-2019-17571, CVE-2022-23305"
        },
        "EngineVersion": "OpenSearch_2.15",
        "AllowListedUserList": [],
        "PackageOwner": "OWNER-XXXX"
    }]
}
```

###### Note

During the `create-package` operation, Amazon OpenSearch Service checks the
`ZIP-PLUGIN` value for version compatibility, supported plugin
extensions, and security vulnerabilities. The security vulnerabilities are scanned
using the [Amazon Inspector](https://aws.amazon.com/inspector/getting-started/ "https://aws.amazon.com/inspector/getting-started/")
service. The results of these checks are shown in `ErrorDetails`
field in the API response. 3. Use the [associate-package](../../../cli/latest/reference/opensearch/associate-package.md "../../../cli/latest/reference/opensearch/associate-package.md") command to associate the plugin with the OpenSearch Service domain of
your choice using the package ID of the package created in the previous step.

###### Tip

If you have multiple plugins, you can instead use the [associate-packages](../../../cli/latest/reference/opensearch/associate-packages.md "../../../cli/latest/reference/opensearch/associate-packages.md") command to associate multiple packages to a domain in
single operation.

Replace the `placeholder values` with your own
information:

```
aws opensearch associate-package \
    --domain-name `domain-name` \
    --region `region` \
    --package-id `package-id`
```

###### Note

The plugin is installed and uninstalled using a [blue/green deployment
process](managedomains-configuration-changes.md "managedomains-configuration-changes.md"). 4. (Optional) Use the [list-packages-for-domain](../../../cli/latest/reference/opensearch/list-packages-for-domain.md "../../../cli/latest/reference/opensearch/list-packages-for-domain.md") command to view the status of the association. The
association status changes as the workflow progresses from `ASSOCIATING` to
`ACTIVE`. The association status changes to ACTIVE after the plugin
installation completes and the plugin is ready for use.

Replace the `placeholder values` with your own
information.

```
aws opensearch list-packages-for-domain \
    --region `region` \
    --domain-name `domain-name`
```

### Updating a custom plugin using the

AWS CLI

Use the [update-package](../../../cli/latest/reference/opensearch/update-package.md "../../../cli/latest/reference/opensearch/update-package.md") command
to make changes to a plugin.

###### Note

You can optionally secure a custom plugin when you update the plugin by specifying
an AWS Key Management Service (AWS KMS) key. For information, see [Create or update a custom plugin with
an AWS KMS key security](#custom-plugin-kms-key-security-cli "#custom-plugin-kms-key-security-cli").

###### To update a custom plugin using the AWS CLI

- Run the following command. Replace the `placeholder
values` with your own information.

```
aws opensearch update-package \
    --region `region` \
    --package-id `package-id` \
    --package-source S3BucketName=`amzn-s3-demo-bucket`,S3Key=`s3-key` \
    --package-description `description`
```

After updating a package, you can use the [associate-package](../../../cli/latest/reference/opensearch/associate-package.md "../../../cli/latest/reference/opensearch/associate-package.md")
or [associate-packages](../../../cli/latest/reference/opensearch/associate-packages.md "../../../cli/latest/reference/opensearch/associate-packages.md")
command to apply package updates to a domain.

###### Note

You can audit, create, update, associate, and disassociate operations on the plugin
using AWS CloudTrail. For more information, see [Monitoring Amazon OpenSearch Service API calls with
AWS CloudTrail](managedomains-cloudtrailauditing.md "managedomains-cloudtrailauditing.md").

### Create or update a custom plugin with

an AWS KMS key security

You can secure a custom plugin when you create or update the plugin by specifying an
AWS KMS key. To accomplish this, set `PackageEncryptionOptions` to
`true` and specify the Amazon Resource Name (ARN) of the key, as shown in the
following examples.

**Example: Create a custom plugin with AWS KMS key
security**

```
aws opensearch create-package \
    --region us-east-2  --package-name my-custom-package \
    --package-type ZIP-PLUGIN \
    --package-source S3BucketName=amzn-s3-demo-bucket,S3Key=my-s3-key
    --engine-version OpenSearch_2.15
"PackageConfigOptions": {
     ...
  }
  "PackageEncryptionOptions": {
    "Enabled": true,
    "KmsKeyId":"arn:aws:kms:us-east-2:111222333444:key/2ba228d5-1d09-456c-ash9-daf42EXAMPLE"
  }
```

**Example: Update a custom plugin with AWS KMS key
security**

```
aws opensearch update-package \
    --region us-east-2  --package-name my-custom-package \
    --package-type ZIP-PLUGIN \
    --package-source S3BucketName=amzn-s3-demo-bucket,S3Key=my-s3-key
    --engine-version OpenSearch_2.15
"PackageConfigOptions": {
     ...
  }
  "PackageEncryptionOptions": {
    "Enabled": true,
    "KmsKeyId":"arn:aws:kms:us-east-2:111222333444:key/2ba228d5-1d09-456c-ash9-daf42EXAMPLE"
  }
```

###### Important

If the AWS KMS key you specify is disabled or deleted, it can leave the associated
cluster inoperational.

For more information about AWS KMS integration with custom packages, [Amazon OpenSearch Service custom package AWS KMS
integration](custom-package-kms-integration.md "custom-package-kms-integration.md").

### Upgrading an OpenSearch Service domain with custom

plugins to a later version of OpenSearch using the AWS CLI

When you need to upgrade an OpenSearch Service domain that uses custom plugins to a later version of
OpenSearch, complete the following processes.

###### To upgrade an OpenSearch Service domain with custom plugins to a later version of OpenSearch

using the AWS CLI

1. Use the create-package command to create a new package for your plugin specifying
   the new OpenSearch version.

Ensure that package name is the same for the plugin for all engine versions.
Changing the package name causes the domain upgrade process to fail during the
blue/green deployment. 2. Upgrade your domain to the higher version by following the steps in [Upgrading Amazon OpenSearch Service domains](version-migration.md "version-migration.md").

During this process, Amazon OpenSearch Service disassociates the previous version of the plugin
package and installs the new version using a blue/green deployment.

### Uninstalling and viewing the dissociation

status of a custom plugin

To uninstall the plugin from any domain, you can use the [dissociate-package](../../../cli/latest/reference/es/dissociate-package.md "../../../cli/latest/reference/es/dissociate-package.md")
command. Running this command also removes any related configuration or license packages.
You can then use the [list-packages-for-domain](../../../cli/latest/reference/es/list-packages-for-domain.md "../../../cli/latest/reference/es/list-packages-for-domain.md") command to view the status of the dissociation.

###### Tip

You can also use [dissociate-packages](../../../cli/latest/reference/opensearch/dissociate-packages.md "../../../cli/latest/reference/opensearch/dissociate-packages.md") command to uninstall multiple plugins from a domain in a
single operation.

###### To uninstall and view the dissociation status of a custom plugin

1. Disable the plugin in every index. This must be done before you dissociate the
   plugin package.

If you try to uninstall a plugin before disabling it from every index, the
blue/green deployment process remains stuck in the `Processing`
state. 2. Run the following command to uninstall the plugin. Replace the
`placeholder values` with your own information.

```
aws opensearch dissociate-package \
    --region `region` \
    --package-id `plugin-package-id` \
    --domain-name `domain name`

```

3. (Optional) Run the [list-packages-for-domain](../../../cli/latest/reference/opensearch/list-packages-for-domain.md "../../../cli/latest/reference/opensearch/list-packages-for-domain.md") command to view the status of the
   dissociation.
