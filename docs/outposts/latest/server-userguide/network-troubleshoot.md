# Outposts server network troubleshooting

Use this checklist to help troubleshoot a service link that has a status of
`DOWN`.

## Initial assessment

Verify the status of the service link through Amazon CloudWatch metrics:

1. Monitor the **ConnectedStatus** metric in the AWS Outposts
   namespace.
2. If the average value is less than 1, this confirms that the service link is
   impaired.
3. If the service link is impaired, complete the steps in the following
   sections to resolve and reestablish the connection.

## Step 1. Check physical

connectivity

1. Verify you are using the provided QSFP breakout cable. If issues persist, test with a different QSFP breakout cable if
   available.
2. Verify that the QSFP breakout cable in the Outposts server is firmly
   seated.
3. Verify that **cable 1** (LNI) is firmly seated in
   the switch.
4. Verify that **cable 2** (service link) is firmly seated in
   the switch.
5. Complete a general switch-sanity check such as, checking link lights.

## Step 2. Test the Outposts server connection to

AWS

[Create a serial connection](../install-server/authorize-2.md "../install-server/authorize-2.md") to the Outposts server and perform the following
tests:

1. [Test the
   links](../install-server/authorize-3.md#w8aac17c15b7 "../install-server/authorize-3.md#w8aac17c15b7").
   1. If successful, proceed with the next test.
   2. If it fails, [Verify network configuration](#verify-network-configuration "#verify-network-configuration").

2. [Test for
   DNS resolution](../install-server/authorize-3.md#w8aac17c15b9 "../install-server/authorize-3.md#w8aac17c15b9").
   1. If successful, proceed with the next test.
   2. If it fails, [Check firewall rules](#check-firewall-rules "#check-firewall-rules").

3. [Test for
   access to the AWS Region](../install-server/authorize-3.md#w8aac17c15c11 "../install-server/authorize-3.md#w8aac17c15c11").
   1. If successful, proceed to reestablish the connection.
   2. If it fails, [Verify MTU](#verify-mtu "#verify-mtu").

### Verify network configuration

Ensure that your switch meets the following specifications:

- Basic configuration — The service
  link port must be an untagged access port to a VLAN with a gateway and a
  route to AWS endpoints.
- Link speed — The switch port must
  have link speed set to 10 Gb and auto-negotiation must be turned off.

### Verify MTU

The network must support 1500-bytes MTU between the Outpost and the service link
endpoints in the parent AWS Region. For more information about the service link,
see [AWS Outposts
connectivity to AWS Regions](region-connectivity.md "region-connectivity.md").

### Check firewall rules

If you use a firewall to limit the connectivity from the service link VLAN, you
can block all inbound connections. You must allow outbound connections back to the
Outpost from the AWS Region as per the following table. If the firewall is stateful,
outbound connections from the Outpost that are allowed, meaning that they were
initiated from the Outpost, should be allowed back inbound.

| Protocol | Source Port     | Source Address  | Destination Port | Destination Address                 |
| -------- | --------------- | --------------- | ---------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| UDP      | 1024-65535      | Service Link IP | 53               | DNS server                          |
| UDP      | 443, 1024-65535 | Service Link IP | 443              | AWS Outposts Service Link endpoints |
| TCP      | 1024-65535      | Service Link IP | 443              | AWS Outposts Registration endpoints | ## Step 3. Reestablish connectivity If the previous checks pass but the service link remains `DOWN` (**ConnectedStatus** is less than 1 in CloudWatch), then follow the steps in [Authorize the Outposts server using the Outpost Configuration Tool](../install-server/authorize-4.md "../install-server/authorize-4.md") to reestablish the connection. ###### Note If the service link remains down, create a case at the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/"). |
