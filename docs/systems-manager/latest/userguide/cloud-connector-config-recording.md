

# AWS Config recording for Cloud Connectors
<a name="cloud-connector-config-recording"></a>

When you create a Cloud Connector, you choose whether AWS Config records the connector's resources in your cloud provider. Recording is on by default. You can't turn it on or off after you create the connector.

Record with AWS Config  
The Cloud Connector is linked to an AWS Config connector, and AWS Config records the connector's resources. The setup also creates the resources that AWS Config uses to receive resource change events from your cloud provider. When a new VM is created, Systems Manager can onboard it as soon as the change event arrives.

Don't record  
The Cloud Connector has no AWS Config connector, and AWS Config doesn't record the connector's resources. The setup creates only the resources that Systems Manager needs. If you enable VM onboarding, new VMs get SSM Agent at the next scheduled run of the onboarding association.

To check a connector's setting in the AWS Management Console, see the **AWS Config recording** field on the connector details page or the **AWS Config recording** column on the **Cloud connectors** tab. In the AWS CLI, the `get-cloud-connector` output includes a `ConfigConnectorArn` only for a connector that records with AWS Config. To create a connector without AWS Config recording in the AWS CLI, omit `--config-connector-arn` from `create-cloud-connector`.

If you change the **Recording** setting after you run the console's setup script, the resources that the earlier run created for AWS Config stay in your cloud provider. The setup topic for your cloud provider lists them.

For information about how to set up a Cloud Connector, see the following topics:
+ [Set up a Cloud Connector for Microsoft Azure in Systems Manager](systems-manager-cloud-connector.md)
+ [Set up a Cloud Connector for Google Cloud Platform in Systems Manager](systems-manager-cloud-connector-gcp.md)