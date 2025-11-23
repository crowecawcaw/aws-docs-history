# AWS Site-to-Site VPN logs

AWS Site-to-Site VPN logs provide you with deeper visibility into your Site-to-Site VPN deployments. With
this feature, you have access to Site-to-Site VPN connection logs that provide details on IP
Security (IPsec) tunnel establishment, Internet Key Exchange (IKE)
negotiations, dead peer detection (DPD) protocol messages, Border Gateway protocol (BGP)
status and routing updates.

Site-to-Site VPN logs can be published to Amazon CloudWatch Logs. This feature provides customers with a
single consistent way to access and analyze detailed logs for all of their Site-to-Site VPN
connections.

###### Topics

- [Benefits of Site-to-Site VPN logs](#log-benefits "#log-benefits")
- [Amazon CloudWatch Logs resource policy size restrictions](#cwl-policy-size "#cwl-policy-size")
- [Site-to-Site VPN log contents](#log-contents "#log-contents")
- [Example log format for Tunnel BGP logs](#example-bgp-logs "#example-bgp-logs")
- [IAM requirements to publish to CloudWatch Logs](#publish-cw-logs "#publish-cw-logs")
- [View Site-to-Site VPN logs configuration](status-logs.md "status-logs.md")
- [Enable Site-to-Site VPN logs](enable-logs.md "enable-logs.md")
- [Disable Site-to-Site VPN logs](disable-logs.md "disable-logs.md")

## Benefits of Site-to-Site VPN logs

- **Simplified VPN troubleshooting:** Site-to-Site VPN logs help
  you to pinpoint configuration mismatches between AWS and your customer
  gateway device, and address initial VPN connectivity issues. VPN connections
  can intermittently flap over time due to misconfigured settings (such as
  poorly tuned timeouts), there can be issues in the underlying transport
  networks (like internet weather), or routing changes or path failures can
  cause disruption of connectivity over VPN. This feature allows you to
  accurately diagnose the cause of intermittent connection failures and
  fine-tune low-level tunnel configuration for reliable operation.
- **Centralized AWS Site-to-Site VPN visibility:** Site-to-Site VPN logs can
  provide tunnel activity and BGP routing logs across all Site-to-Site VPN
  connection types. This feature provides customers
  with a single consistent way to access and analyze detailed logs for all of
  their Site-to-Site VPN connections.
- **Security and compliance:** Site-to-Site VPN logs can
  be sent to Amazon CloudWatch Logs for retrospective analysis of VPN
  connection status and activity over time. This can help you meet compliance
  and regulatory requirements.

## Amazon CloudWatch Logs resource policy size restrictions

CloudWatch Logs resource policies are limited to 5120 characters. When CloudWatch Logs detects that a policy approaches this size limit, it automatically enables log groups that start with `/aws/vendedlogs/`. When you enable logging, Site-to-Site VPN must update your CloudWatch Logs resource policy with the log group you specify. To avoid reaching the CloudWatch Logs resource policy size limit, prefix your log group names with `/aws/vendedlogs/`.

## Site-to-Site VPN log contents

The following information is included in the Site-to-Site VPN tunnel activity log. The log
stream file name uses VpnConnectionID and TunnelOutsideIPAddress.

| Field                                              | Description                                                  |
| -------------------------------------------------- | ------------------------------------------------------------ | -------- | ----------- | ------ |
| VpnLogCreationTimestamp (`event_timestamp`)        | Log creation timestamp in epoch time format.                 |
| VpnLogCreationTimestampReadable (`timestamp`)      | Log creation timestamp in human readable time format.        |
| TunnelDPDEnabled (`dpd_enabled`)                   | Dead Peer Detection Protocol Enabled Status<br>(True/False). |
| TunnelCGWNATTDetectionStatus<br>(`nat_t_detected`) | NAT-T detected on customer gateway device (True/False).      |
| TunnelIKEPhase1State (`ike_phase1_state`)          | IKE Phase 1 Protocol State<br>(Established                   | Rekeying | Negotiating | Down). |
| TunnelIKEPhase2State (`ike_phase2_state`)          | IKE Phase 2 Protocol State<br>(Established                   | Rekeying | Negotiating | Down). |
| VpnLogDetail (`details`)                           | Verbose messages for IPsec, IKE and DPD protocols.           |

The following information is included in the Site-to-Site VPN tunnel BGP log. The log
stream file name uses VpnConnectionID and TunnelOutsideIPAddress.

| Field           | Description                                                                                                                                                                                  |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | ----------------------------------------------------- | -------------------------------------------------- |
| resource_id     | A unique ID to identify the tunnel and the VPN connection the log is associated with.                                                                                                        |
| event_timestamp | Log creation timestamp in epoch time format.                                                                                                                                                 |
| timestamp       | Log creation timestamp in human readable time format.                                                                                                                                        |
| type            | Type of BGP Log Event (BGPStatus                                                                                                                                                             | RouteStatus).                                                        |
| status          | status update for a specific type of log event<br>(BGPStatus: UP                                                                                                                             | DOWN)<br>(RouteStatus: ADVERTISED {route was advertised by the peer} | <br>UPDATED: {existing route was updated by the peer} | <br>WITHDRAWN: {route was withdrawn by peer})<br>. |
| message         | Provides additional details on the log even and status. This field will<br>help you understand why the BGPStatus is down what route attributes were exchanged<br>in the RouteStatus message. |

###### Contents

- [IKEv1 Error Messages](#sample-log-ikev1 "#sample-log-ikev1")
- [IKEv2 Error Messages](#sample-log-ikev2 "#sample-log-ikev2")
- [IKEv2 Negotiation Messages](#sample-log-ikev2-negotiation "#sample-log-ikev2-negotiation")
- [BGP Status Messages](#sample-bgp-status-messages "#sample-bgp-status-messages")
- [Route Status Messages](#sample-route-status-messages "#sample-route-status-messages")

### IKEv1 Error Messages

| Message                                                                      | Explanation                                                                                                                                        |
| ---------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Peer is not responsive<br>• Declaring peer dead                              | Peer has not responded to DPD Messages, enforcing DPD time-out action.                                                                             |
| AWS tunnel payload decryption was unsuccessful due to invalid Pre-shared Key | Same Pre-Shared key needs to be configured on both IKE Peers.                                                                                      |
| No Proposal Match Found by AWS                                               | Proposed Attributes for Phase 1 (Encryption, Hashing and<br>DH Group) are not supported by AWS VPN Endpoint— for<br>example, `3DES`.               |
| No Proposal Match Found. Notifying with "No proposal chosen"                 | No Proposal Chosen error message is exchanged between Peers to inform that correct Proposals/Policies must be configured for phase 2 on IKE Peers. |
| AWS tunnel received DELETE for Phase 2 SA with SPI: xxxx                     | CGW has sent the Delete_SA message for Phase 2.                                                                                                    |
| AWS tunnel received DELETE for IKE_SA from CGW                               | CGW has sent the Delete_SA message for Phase 1.                                                                                                    |

### IKEv2 Error Messages

| Message                                                                       | Explanation                                                                                                                                     |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS tunnel DPD timed out after {retry_count}<br>retransmits                   | Peer has not responded to DPD Messages, enforcing DPD<br>time-out action.                                                                       |
| AWS tunnel received DELETE for IKE_SA from CGW                                | Peer has sent the Delete_SA message for<br>Parent/IKE_SA.                                                                                       |
| AWS tunnel received DELETE for Phase 2 SA with SPI:<br>xxxx                   | Peer has sent the Delete_SA message for CHILD_SA.                                                                                               |
| AWS tunnel detected a (CHILD_REKEY) collision as CHILD_DELETE                 | CGW has sent the Delete_SA message for the Active SA, which is being rekeyed.                                                                   |
| AWS tunnel (CHILD_SA) redundant SA is being deleted due to detected collision | Due to Collision, If redundant SAs are generated, Peers will close redundant SA after matching<br>the nonce values as per RFC.                  |
| AWS tunnel Phase 2 was unable to establish while keeping Phase 1              | Peer was unable to establish CHILD_SA due to negotiation error — for example, incorrect<br>proposal.                                            |
| AWS: Traffic Selector: TS_UNACCEPTABLE: received from responder               | Peer has proposed Incorrect Traffic Selectors/Encryption Domain. Peers should be configured with identical and correct CIDRs.                   |
| AWS tunnel is sending AUTHENTICATION_FAILED as the response                   | Peer is unable to Authenticate the Peer by verifying IKE_AUTH message's contents                                                                |
| AWS tunnel detected a pre-shared key mismatch with cgw: xxxx                  | Same Pre-Shared key needs to be configured on both IKE Peers.                                                                                   |
| AWS tunnel Timeout: deleting un-established Phase 1 IKE_SA with cgw: xxxx     | Deleting the half-opened IKE_SA as peer has not proceeded with negotiations                                                                     |
| No Proposal Match Found. Notifying with "No proposal chosen"                  | No Proposal Chosen error message is exchanged between Peers to inform that correct Proposals must be configured on IKE Peers.                   |
| No Proposal Match Found by AWS                                                | Proposed Attributes for Phase 1 or Phase 2 (Encryption, Hashing and DH Group) are not<br>supported by AWS VPN Endpoint— for example,<br>`3DES`. |

### IKEv2 Negotiation Messages

| Message                                                     | Explanation                                               |
| ----------------------------------------------------------- | --------------------------------------------------------- |
| AWS tunnel processed request (id=xxx) for CREATE_CHILD_SA   | AWS has received the CREATE_CHILD_SA request from<br>CGW. |
| AWS tunnel is sending response (id=xxx) for CREATE_CHILD_SA | AWS is sending CREATE_CHILD_SA response to CGW.           |
| AWS tunnel is sending request (id=xxx) for CREATE_CHILD_SA  | AWS is sending CREATE_CHILD_SA request to CGW.            |
| AWS tunnel processed response (id=xxx) for CREATE_CHILD_SA  | AWS has received CREATE_CHILD_SA response form<br>CGW.    |

### BGP Status Messages

BGP Status messages contain information related to BGP Session state transitions, prefix limit
warnings, limit violations, BGP session notifications, BGP OPEN messages, and attribute updates
for a BGP neighbor for a given BGP session.

| Message                                                                                                                                                              | BGP Status | Explanation                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| AWS-side peer BGP session state has changed from Idle to Connect with neighbor {ip: xxx}                                                                             | DOWN       | BGP Connection state on the AWS side has been updated to Connect.                                                                                                        |
| AWS-side peer BGP session state has changed from Connect to OpenSent with neighbor {ip: xxx}                                                                         | DOWN       | BGP Connection state on the AWS side has been updated to OpenSent.                                                                                                       |
| AWS-side peer BGP session state has changed from OpenSent to OpenConfirm with neighbor {ip: xxx}                                                                     | DOWN       | BGP Connection state on the AWS side has been updated to OpenConfirm.                                                                                                    |
| AWS-side peer BGP session state has changed from OpenConfirm to Established with neighbor {ip: xxx}                                                                  | UP         | BGP Connection state on the AWS side has been updated to Established.                                                                                                    |
| AWS-side peer BGP session state has changed from Established to Idle with neighbor {ip: xxx}                                                                         | DOWN       | BGP Connection state on the AWS side has been updated to Idle.                                                                                                           |
| AWS-side peer BGP session state has changed from Connect to Active with neighbor {ip: xxx}                                                                           | DOWN       | BGP Connection state on the AWS side transitioned from Connect to Active. Check TCP port 179 availability on CGW if BGP session is stuck in Connect state.               |
| AWS-side peer is reporting a maximum prefix limit warning<br>• received {prefixes (count): xxx} prefixes from neighbor {ip: xxx}, limit is {limit (numeric): xxx}    | UP         | The AWS side periodically generates a log message when the number of prefixes received from the CGW nears the allowed limit.                                             |
| AWS-side peer detected the maximum prefix limit was exceeded<br>• received {prefixes (count): xxx} prefixes from neighbor {ip: xxx}, limit is {limit (numeric): xxx} | DOWN       | The AWS side generates a log message when the number of prefixes received from the CGW exceeded the allowed limit.                                                       |
| AWS-side peer sent a notification 6/1 (Cease/Maximum Number of Prefixes Reached) to neighbor {ip: xxx}                                                               | DOWN       | The AWS side sent a notification to the CGW BGP peer to indicate that the BGP session was terminated due to a prefix limit violation.                                    |
| AWS-side peer received notification 6/1 (Cease/Maximum Number of Prefixes Reached) from neighbor {ip: xxx}                                                           | DOWN       | The AWS side received a notification from the CGW peer to indicate that the BGP session was terminated due to a prefix limit violation.                                  |
| AWS-side peer sent a notification 6/2 (Cease/Administrative Shutdown) to neighbor {ip: xxx}                                                                          | DOWN       | The AWS side sent a notification to the CGW BGP peer to indicate that the BGP session was terminated.                                                                    |
| AWS-side peer received notification 6/2 (Cease/Administrative Shutdown) from neighbor {ip: xxx}                                                                      | DOWN       | The AWS side received a notification from the CGW peer to indicate that the BGP session was terminated.                                                                  |
| AWS-side peer sent a notification 6/3 (Cease/Peer Unconfigured) to neighbor {ip: xxx}                                                                                | DOWN       | The AWS side sent a notification to the CGW peer to indicate that the peer is not configured or has been removed from configuration.                                     |
| AWS-side peer received notification 6/3 (Cease/Peer Unconfigured) from neighbor {ip: xxx}                                                                            | DOWN       | The AWS side received a notification from the CGW peer to indicate that the peer is not configured or has been removed from configuration.                               |
| AWS-side peer sent a notification 6/4 (Cease/Administrative Reset) to neighbor {ip: xxx}                                                                             | DOWN       | The AWS side sent a notification to the CGW BGP peer to indicate that the BGP session was reset.                                                                         |
| AWS-side peer received notification 6/4 (Cease/Administrative Reset) from neighbor {ip: xxx}                                                                         | DOWN       | The AWS side received a notification from the CGW peer to indicate that the BGP session was reset.                                                                       |
| AWS-side peer sent a notification 6/5 (Cease/Connection Rejected) to neighbor {ip: xxx}                                                                              | DOWN       | The AWS side sent a notification to the CGW BGP peer to indicate that the BGP session was rejected.                                                                      |
| AWS-side peer received notification 6/5 (Cease/Connection Rejected) from neighbor {ip: xxx}                                                                          | DOWN       | The AWS side received a notification from the CGW peer to indicate that the BGP session was rejected.                                                                    |
| AWS-side peer sent a notification 6/6 (Cease/Other Configuration Change) to neighbor {ip: xxx}                                                                       | DOWN       | The AWS side sent a notification to the CGW BGP peer to indicate that a BGP session configuration change took place.                                                     |
| AWS-side peer received notification 6/6 (Cease/Other Configuration Change) from neighbor {ip: xxx}                                                                   | DOWN       | The AWS side received a notification from the CGW peer which indicates that a BGP session configuration change took place.                                               |
| AWS-side peer sent a notification 6/7 (Cease/Connection Collision Resolution) to neighbor {ip: xxx}                                                                  | DOWN       | The AWS side sent a notification to the CGW peer to resolve a connection collision when both peers attempt to establish a connection simultaneously.                     |
| AWS-side peer received notification 6/7 (Cease/Connection Collision Resolution) from neighbor {ip: xxx}                                                              | DOWN       | The AWS side received a notification from the CGW peer indicating resolution of a connection collision when both peers attempt to establish a connection simultaneously. |
| AWS-side peer sent a Hold Timer Expired notification to neighbor {ip: xxx}                                                                                           | DOWN       | The BGP hold timer expired and a notification was sent by the AWS side to the CGW.                                                                                       |
| AWS-side peer detected a bad OPEN message from neighbor {ip: xxx}<br>• remote AS is {asn: xxx}, expected {asn: xxx}                                                  | DOWN       | The AWS side detected a bad OPEN message was received from the CGW peer which is indicative of a configuration mismatch.                                                 |
| AWS-side peer received an OPEN message from neighbor {ip: xxx}<br>• version 4, AS {asn: xxx}, holdtime {holdtime (seconds): xxx}, router-id {id: xxx}}               | DOWN       | The AWS side received a BGP open message to initiate a BGP session with the CGW peer.                                                                                    |
| AWS-side peer sent an OPEN message to neighbor {ip: xxx}<br>• version 4, AS {asn: xxx}, holdtime {holdtime (seconds): xxx}, router-id {id: xxx}                      | DOWN       | The CGW peer sent a BGP open message to initiate a BGP session with the AWS side BGP peer.                                                                               |
| AWS-side peer is initiating a connection (via Connect) to neighbor {ip: xxx}                                                                                         | DOWN       | The AWS side is attempting to connect with the CGW BGP neighbor.                                                                                                         |
| AWS-side peer sent an End-of-RIB message to neighbor {ip: xxx}                                                                                                       | UP         | The AWS side has finished transmitting routes to the CGW after BGP session establishment.                                                                                |
| AWS-side peer received update with attributes from neighbor {ip: xxx}<br>• AS path: {aspath (list): xxx xxx xxx}                                                     | UP         | The AWS side received a BGP session attribute update from the neighbor.                                                                                                  |

### Route Status Messages

Unlike BGP Status Messages, Route Status Messages contain data about BGP attributes of a given
prefix such as AS path, local preference, Multi-Exit Discriminator (MED), next hop IP address,
and weight. A Route Status message will only contain a details field when there is an error with a route that was
ADVERTISED, UPDATED, or WITHDRAWN. Examples of which are as follows

| Message                                    | Explanation                                                                                                                                                           |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DENIED due to: as-path contains our own AS | BGP update messages for a new prefix from CGW was denied by AWS due to the route containing the AWS-side peers own AS.                                                |
| DENIED due to: non-connected next-hop      | AWS rejected a BGP route advertisement for the prefix from the CGW due to a non-connected next-hop validation failure. Ensure the route is reachable on the CGW side. |

## Example log format for Tunnel BGP logs

```

{
    "resource_id": "vpn-1234abcd_1.2.3.4",
    "event_timestamp": 1762580429641,
    "timestamp": "2025-11-08 05:40:29.641Z",
    "type": "BGPStatus",
    "status": "UP",
    "message": {
        "details": "AWS-side peer BGP session state has changed from OpenConfirm to Established with neighbor 169.254.50.85"
    }
}

{
    "resource_id": "vpn-1234abcd_1.2.3.4",
    "event_timestamp": 1762579573243,
    "timestamp": "2025-11-08 05:26:13.243Z",
    "type": "RouteStatus",
    "status": "UPDATED",
    "message": {
        "prefix": "172.31.0.0/16",
        "asPath": "64512",
        "localPref": 100,
        "med": 100,
        "nextHopIp": "169.254.50.85",
        "weight": 32768,
        "details": "DENIED due to: as-path contains our own AS"
    }
}

```

## IAM requirements to publish to CloudWatch Logs

For the logging feature to work properly, the IAM policy attached to the IAM
principal being used to configure the feature, must include the following
permissions at minimum. More details can also be found in the [Enabling logging from certain AWS services](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md") section of the _Amazon CloudWatch Logs User Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "logs:CreateLogDelivery",
 "logs:GetLogDelivery",
 "logs:UpdateLogDelivery",
 "logs:DeleteLogDelivery",
 "logs:ListLogDeliveries"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow",
 "Sid": "S2SVPNLogging"
 },
 {
 "Sid": "S2SVPNLoggingCWL",
 "Action": [
 "logs:PutResourcePolicy",
 "logs:DescribeResourcePolicies",
 "logs:DescribeLogGroups"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow"
 }
 ]
}`

```
