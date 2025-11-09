# Understand codes for Amazon VPC in billing and usage reports

When you use Amazon VPC, we include related codes in your AWS billing and usage reports. Reviewing these
codes helps you understand your costs and usage patterns for Amazon VPC. Tracking and managing your
expenses is essential for optimizing your costs.

The following tables describe the codes for Amazon VPC that appear in your billing and usage reports.
For a list of the Region codes used in the billing and usage reports, see [AWS Region billing codes](../../../global-infrastructure/latest/regions/aws-region-billing-codes.md "../../../global-infrastructure/latest/regions/aws-region-billing-codes.md").

###### Billing codes for:

- [IP address management](#ip-billing-usage-reports "#ip-billing-usage-reports")
- [VPC endpoints](#vpce-billing-usage-reports "#vpce-billing-usage-reports")
- [Transit gateways](#tgw-billing-usage-reports "#tgw-billing-usage-reports")
- [Network analysis](#analysis-billing-usage-reports "#analysis-billing-usage-reports")
- [Traffic mirroring](#mirroring-billing-usage-reports "#mirroring-billing-usage-reports")
- [VPC Lattice](#lattice-billing-usage-reports "#lattice-billing-usage-reports")
- [Cross-account/Region resources](#cross-billing-usage-reports "#cross-billing-usage-reports")

###### Related resources

- [Amazon VPC pricing](https://aws.amazon.com/vpc/pricing/ "https://aws.amazon.com/vpc/pricing/")
- [AWS PrivateLink pricing](https://aws.amazon.com/privatelink/pricing/ "https://aws.amazon.com/privatelink/pricing/")
- [AWS Transit Gateway pricing](https://aws.amazon.com/transit-gateway/pricing/ "https://aws.amazon.com/transit-gateway/pricing/")
- [Amazon VPC Lattice pricing](https://aws.amazon.com/vpc/lattice/pricing/ "https://aws.amazon.com/vpc/lattice/pricing/")

## IP address management

| Code                                  | Description                                                                   | Units | Granularity |
| ------------------------------------- | ----------------------------------------------------------------------------- | ----- | ----------- |
| ``region`-PublicIPv4:InUseAddress`    | The time that public IPv4 addresses are in use by a resource.                 | Hours | Per-second  |
| ``region`-PublicIPv4:IdleAddress`     | The time that public IPv4 addresses are not in use by a resource.             | Hours | Per-second  |
| ``region`-PublicIPv4:ContiguousBlock` | The use of public IPv4 addresses in an Amazon-provided contiguous IPv4 block. | Hours | Hourly      |
| ``region`-IPAddressManager-IP-Hours`  | The time that IP addresses are managed by IPAM Advanced Tier.                 | Hours | Hourly      |

## VPC endpoints

| Code                               | Description                                                    | Units | Granularity |
| ---------------------------------- | -------------------------------------------------------------- | ----- | ----------- |
| ``region`-VpcEndpoint-Hours`       | The time that interface VPC endpoints are provisioned.         | Hours | Hourly      |
| ``region`-VpcEndpoint-Bytes`       | The data processed by interface VPC endpoints.                 | GB    | Hourly      |
| ``region`-VpcEndpoint-GWLBE-Hours` | The time that Gateway Load Balancer endpoints are provisioned. | Hours | Hourly      |
| ``region`-VpcEndpoint-GWLBE-Bytes` | The data processed by Gateway Load Balancer endpoints.         | GB    | Hourly      |

## Transit gateways

| Code                                    | Description                                         | Units | Granularity |
| --------------------------------------- | --------------------------------------------------- | ----- | ----------- |
| ``region`-TransitGateway-Hours`         | The use of transit gateway attachments.             | Hours | Hourly      |
| ``region`-TransitGateway-Bytes`         | The data processed by transit gateways.             | GB    | Hourly      |
| ``region`-TGW-Multicast-Consumer-Bytes` | The data processed by multicast receiver instances. | GB    | Hourly      |

## Network analysis

| Code                                   | Description                                                           | Units | Granularity    |
| -------------------------------------- | --------------------------------------------------------------------- | ----- | -------------- |
| ``region`-Analysis-Runs`               | The number of network paths analyzed by Reachability Analyzer.        | Count | Per analysis   |
| ``region`-NetworkInterface-Assessment` | The number of network interfaces analyzed by Network Access Analyzer. | Count | Per assessment |

## Traffic mirroring

| Code                  | Description                                                            | Units | Granularity |
| --------------------- | ---------------------------------------------------------------------- | ----- | ----------- |
| ``region`-ENI-Mirror` | The time that a network interface is configured for traffic mirroring. | Hours | Hourly      |

## VPC Lattice

| Code                                                 | Description                                        | Units | Granularity |
| ---------------------------------------------------- | -------------------------------------------------- | ----- | ----------- |
| ``region`-VPCLattice-Service-Hourly`                 | The running time for VPC Lattice services.         | Hours | Hourly      |
| ``region`-VPCLattice-DataProcessing-Bytes`           | The data processed by VPC Lattice services.        | GB    | Hourly      |
| ``region`-VPCLattice-RequestCount-Free`              | The free HTTP requests and TCP connections.        | Count | Hourly      |
| ``region`-VpcLattice-Service-Network-Resource-Hours` | The running time for VPC Lattice service networks. | Hours | Hourly      |

## Cross-account/Region resources

| Code                                  | Description                                                              | Units | Granularity |
| ------------------------------------- | ------------------------------------------------------------------------ | ----- | ----------- |
| ``region`-VpcResource-Provider-Bytes` | The data transferred from provider resources across accounts or Regions. | GB    | Hourly      |
| ``region`-VpcResource-Consumer-Bytes` | The data transferred by consumer resources across accounts or Regions.   | GB    | Hourly      |
