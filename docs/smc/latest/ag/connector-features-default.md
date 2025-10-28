# Connector features

enabled by default

###### To configure the default Connector features for specific AWS

services

For a new installation of Connector, we enable the default
project configuration for all Connector features (AWS Service Catalog, AWS Config,
AWS Systems Manager Automation, AWS Systems Manager OpsCenter, and AWS Security Hub). If you
are upgrading an existing installation, for security reasons, we do
not intially enable new features.

###### Note

If you are using the AWS Security Hub integration, we recommend you
also turn on AWS Config.

If you use the AWS Config integration with JSM, this might add more
resource details in JSM issues created for AWS Security Hub Findings. For
example, if the original Finding has limited resource details, the
Config resource enrichment provides fuller information.

Also, if the resource no longer exists, the Config enrichment
provides information about the resource status. If the resource
details changed since the creation of the Finding, the Config
enrichment provides the latest details, but it does not overwrite
the original details.

1. In the left navigation menu, under **AWS Service
   Management**, select **Connector
   settings.**
2. At the top, under **Connector features enabled by
   default**, select each feature depending whether you
   want projects using the default configuration to be able to use
   them or not.
3. Choose **Save**.
