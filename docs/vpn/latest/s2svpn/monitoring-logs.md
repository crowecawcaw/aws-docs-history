# AWS Site-to-Site VPN logs

AWS Site-to-Site VPN logs provide you with deeper visibility into your Site-to-Site VPN deployments. With
this feature, you have access to Site-to-Site VPN connection logs that provide details on IP
Security (IPsec) tunnel establishment, Internet Key Exchange (IKE)
negotiations, and dead peer detection (DPD) protocol messages.

Site-to-Site VPN logs can be published to Amazon CloudWatch Logs. This feature provides customers with a
single consistent way to access and analyze detailed logs for all of their Site-to-Site VPN
connections.

###### Topics

- [Benefits of Site-to-Site VPN logs](#log-benefits "#log-benefits")
- [Amazon CloudWatch Logs resource policy size restrictions](#cwl-policy-size "#cwl-policy-size")
- [Site-to-Site VPN log contents](#log-contents "#log-contents")
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
  provide tunnel activity logs for all of the different ways that
  Site-to-Site VPN is connected: Virtual Gateway, Transit Gateway, and CloudHub, using
  both internet and AWS Direct Connect as transport. This feature provides customers
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
| VpnLogCreationTimestamp (`event_timestamp`)        | Log creation timestamp in human readable format.             |
| TunnelDPDEnabled (`dpd_enabled`)                   | Dead Peer Detection Protocol Enabled Status<br>(True/False). |
| TunnelCGWNATTDetectionStatus<br>(`nat_t_detected`) | NAT-T detected on customer gateway device (True/False).      |
| TunnelIKEPhase1State (`ike_phase1_state`)          | IKE Phase 1 Protocol State<br>(Established                   | Rekeying | Negotiating | Down). |
| TunnelIKEPhase2State (`ike_phase2_state`)          | IKE Phase 2 Protocol State<br>(Established                   | Rekeying | Negotiating | Down). |
| VpnLogDetail (`details`)                           | Verbose messages for IPsec, IKE and DPD protocols.           |

###### Contents

- [IKEv1 Error Messages](#sample-log-ikev1 "#sample-log-ikev1")
- [IKEv2 Error Messages](#sample-log-ikev2 "#sample-log-ikev2")
- [IKEv2 Negotiation Messages](#sample-log-ikev2-negotiation "#sample-log-ikev2-negotiation")

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
