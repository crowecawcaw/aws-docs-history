# Installing third-party plugins in Amazon OpenSearch Service

Amazon OpenSearch Service supports third-party plugins from selected partners. These plugins can enhance
your OpenSearch setup with additional features such as custom analyzers, tokenizers, or
encryption capabilities. Follow the specific installation and configuration instructions
provided by the third-party developers to ensure proper integration with your OpenSearch Service
domain.

###### Note

You must obtain and maintain valid licenses directly from the third-party developers.
Some providers might not enable their plugins in all AWS Regions, so check with the plugin
provider for availability.

The following third-party plugins are available for use with OpenSearch Service:

- **Portal26 encryption plugin (Titanium-lockbox)**
  – Uses NIST FIPS 140-2 certified encryption to encrypt data as it’s indexed. It
  includes Bring Your Own Key (BYOK) support, which lets you manage your encryption keys for
  enhanced security. The plugin is provided by [Portal26](https://portal26.ai/ "https://portal26.ai/") and requires OpenSearch version 2.15 or higher.
- **Name Match (RNI)** – Matches names,
  organizations, addresses, and dates in over 24 languages, which improves security and
  compliance. The plugin is provided by [Babel
  Street](https://www.babelstreet.com/ "https://www.babelstreet.com/") and requires OpenSearch version 2.15 or higher.

###### Topics

- [Prerequisites](#prerequisites-partner-plugins "#prerequisites-partner-plugins")
- [Installing third-party plugins](#third-party-partner-plugins-install "#third-party-partner-plugins-install")
- [Next steps](#third-party-partner-plugins-next "#third-party-partner-plugins-next")

## Prerequisites

Before you install a third-party plugin, perform the following steps:

- Obtained the plugin configuration and license files and uploaded them to an Amazon S3
  bucket. The bucket must be in the same AWS Region as domain.
- A third-party plugin is a type of custom plugin. Make sure that the domain meets the
  [prerequisites](custom-plugins.md#custom-plugin-prerequisites "custom-plugins.md#custom-plugin-prerequisites") for custom
  plugins.

## Installing third-party plugins

To associate a third-party plugin with an OpenSearch Service domain, you must first upload three
separate packages: the _license_ package, the
_configuration_ package, and the _plugin_
package.

- The **license** package includes the licensing
  information or metadata associated with the plugin, in .json or .xml format.
- The **configuration** package contains the plugin
  configuration files and supporting assets and settings. These files define how the
  plugin behaves or integrates with OpenSearch.
- The **plugin** package contains the compiled plugin
  binary, which is the executable code that OpenSearch runs. This is the core of the plugin
  functionality.

After you upload both packages, you can associate the plugin and license with a
compatible domain.

To associate a third-party plugin to a domain, first import the plugin license and
configuration as packages.

###### To install a third-party plugin

1. Sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home "https://console.aws.amazon.com/aos/home").
2. In the left navigation pane, choose **Packages**.
3. First, import the license package. Choose **Import
   package**.
4. For **Package type**, choose
   **License**.
5. For **Package source**, enter the path to the license JSON or
   XML file in Amazon S3.
6. Choose **Import**. The package appears on the
   **Licenses** tab of the **Packages** page.
7. Now, import the plugin configuration. Choose **Import package**
   again.
8. For **Package type**, choose
   **Configuration**.
9. For **Package source**, enter the path to the plugin
   configuration ZIP file in Amazon S3.
10. Choose **Import**.
11. Lastly, import the plugin itself. Choose **Import
    package**.
12. For **Package type**, choose
    **Plugin**.
13. For **Package source**, enter the path to the plugin ZIP file
    in Amazon S3.
14. Select the OpenSearch engine version that the plugin supports.
15. Choose **Import**.

###### To associate a third-party plugin to a domain

1. Now, associate the plugin license and configuration with the domain. In the left
   navigation pane, choose **Domains**.
2. Choose the name of the domain to open its cluster configuration.
3. Navigate to the **Plugins** tab.
4. Choose **Associate packages** and select the plugin, license,
   and configuration packages that you just imported.
5. Choose **Select**.
6. Choose **Next**. Review the packages to associate and choose
   **Associate**.
   First, use the [create-package](../../../cli/latest/reference/opensearch/create-package.md "../../../cli/latest/reference/opensearch/create-package.md")
   command to create a new package that contains the plugin license. The `S3Key`
   must point to a .json or .xml file in Amazon S3 that includes the license text or
   metadata.

```
aws opensearch create-package \
  --package-name `plugin-license-package` \
  --package-type PACKAGE-LICENSE \
  --package-source S3BucketName=`my-bucket`,S3Key=`licenses/my-plugin-license.json`
```

Use the [create-package](../../../cli/latest/reference/opensearch/create-package.md "../../../cli/latest/reference/opensearch/create-package.md")
command again to create a package that contains the plugin configuration. The
`S3Key` must point to a .zip file in Amazon S3 that adheres to the directory
structure expected by the plugin.

```
aws opensearch create-package \
  --package-name `plugin-config-package` \
  --package-type PACKAGE-CONFIG \
  --package-source S3BucketName=`my-bucket`,S3Key=`path/to/package.zip`
```

Use the [create-package](../../../cli/latest/reference/opensearch/create-package.md "../../../cli/latest/reference/opensearch/create-package.md")
command again to create a package that contains the plugin itself. The
`S3Key` must point to the plugin .zip file in Amazon S3.

```
aws opensearch create-package \
  --package-name `plugin-package` \
  --package-type ZIP-PLUGIN \
  --package-source S3BucketName=`my-bucket`,S3Key=`path/to/package.zip`
```

Finally, use the [associate-package](../../../cli/latest/reference/opensearch/associate-package.md "../../../cli/latest/reference/opensearch/associate-package.md")
command to link the partner plugin, license, and configuration to a compatible domain by
specifying the package IDs for each. Specify the plugin ID as a prerequisite for the
other packages, which means that it must be associated with the domain before the other
packages.

```
aws opensearch associate-packages \
  --domain-name `my-domain` \
  --package-list '[{"PackageID": "`plugin-package-id`"},{"PackageID": "`license-package-id`","PrerequisitePackageIDList":["`plugin-package-id`"]},{"PackageID":"`config-package-id`","PrerequisitePackageIDList":["`plugin-package-id`"]}]'
```

## Next steps

When the association completes, you can enable the plugin on specific indexes or
configure it as needed based on your requirements. To apply third-party plugin functionality
to specific indexes, modify the index settings during index creation or update existing
indexes. For example, if your third-party plugin includes a [custom
analyzer](https://opensearch.org/docs/latest/analyzers/custom-analyzer/ "https://opensearch.org/docs/latest/analyzers/custom-analyzer/"), reference it in the index settings.

To apply the plugin features consistently across multiple indexes, use [index
templates](https://opensearch.org/docs/latest/im-plugin/index-templates/ "https://opensearch.org/docs/latest/im-plugin/index-templates/") that include the plugin configurations. Always consult the plugin
documentation to understand how to configure its features for your OpenSearch setup.
