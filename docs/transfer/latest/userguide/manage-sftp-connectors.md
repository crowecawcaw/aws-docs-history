# Managing SFTP connectors

This topic describes how to view and update SFTP connectors.

###### Note

Each connector is automatically assigned static IP addresses that remain unchanged
over the lifetime of the connector. This allows you to connect with remote SFTP servers
that only accept inbound connections from known IP addresses. Your connectors are
assigned a set of static IP addresses that are shared by all connectors using the same
protocol (SFTP or AS2) in your AWS account.

For VPC_LATTICE-enabled connectors, the remote SFTP server will see IP addresses from your VPC CIDR range instead of AWS Transfer Family service-managed IP addresses.

## Update SFTP connectors

To change the existing parameter values for your connectors, you can run the
`update-connector` command. The following command updates the secret for
the connector `connector-id`, in the Region
`region-id` to
`secret-ARN`. To use this example command,
replace the `user input placeholders` with your
own information.

```
aws transfer update-connector --sftp-config '{"UserSecretId":"`secret-ARN`"}' \
   --connector-id `connector-id` --region `region-id`
```

### Updating VPC connectivity settings

You can update VPC connectivity settings for existing connectors, including switching between service-managed and VPC egress types or changing the Resource Configuration ARN.

To switch a connector from service-managed to VPC egress:

```
aws transfer update-connector \
   --connector-id `connector-id` \
   --egress-type VPC \
   --egress-config ResourceConfigurationArn=`resource-configuration-arn`
```

To update the Resource Configuration ARN for a VPC_LATTICE-enabled connector:

```
aws transfer update-connector \
   --connector-id `connector-id` \
   --egress-config ResourceConfigurationArn=`new-resource-configuration-arn`
```

###### Note

When updating VPC connectivity settings, the connector status will change to `PENDING` during the reconfiguration process. Monitor the connector status using the `describe-connector` command.

## View SFTP connector details

You can find a list of details and properties for an SFTP connector in the AWS Transfer Family
console.

###### To view connector details

1. Open the AWS Transfer Family console at [https://console.aws.amazon.com/transfer/](https://console.aws.amazon.com/transfer/ "https://console.aws.amazon.com/transfer/").
2. In the left navigation pane, choose **Connectors**.
3. Choose the identifier in the **Connector ID** column to see
   the details page for the selected connector.

You can change the properties for the SFTP connector by choosing
**Edit** on the connector details page.

### Monitoring VPC connector status

VPC_LATTICE-enabled connectors include additional status information to help you monitor the provisioning process:

- **Status**: Shows `PENDING`, `ACTIVE`, or `ERRORED`
- **EgressType**: Shows `VPC` or `SERVICE_MANAGED`
- **EgressConfig**: Contains the Resource Configuration ARN for VPC connectors
- **Error**: Provides detailed error information if the connector is in `ERRORED` state

For VPC connectors, the `ServiceManagedEgressIpAddresses` field will be null since traffic uses your VPC IP addresses instead.

###### Note

You can get much of this information, albeit in a different format, by running the
following AWS Command Line Interface (AWS CLI) command. To use this example command, replace the
`user input placeholders` with your
own information.

```
aws transfer describe-connector --connector-id `your-connector-id`
```

For more information, see [DescribeConnector](../APIReference/API_DescribeConnector.md "../APIReference/API_DescribeConnector.md") in the API reference.
