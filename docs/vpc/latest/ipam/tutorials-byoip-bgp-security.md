

# Tutorial: Set up delegated RPKI for BYOIP prefixes
<a name="tutorials-byoip-bgp-security"></a>

This tutorial walks through all BGP route protection capabilities end to end. You can stop after any step and use what you've set up so far. Steps 1 and 2 require no RIR interaction. Steps 3 and later require a one-time setup with your RIR. For background on BGP route protection concepts, tier requirements, and supported RIRs, see [Monitor BGP route protection](monitor-bgp-route-security.md).

## Prerequisites
<a name="tutorials-byoip-bgp-security-prereqs"></a>
+ An IPAM created in the Advanced Tier.
+ One or more BYOIP prefixes provisioned to IPAM pools.
+ Access to your Regional Internet Registry account (ARIN, RIPE, APNIC, or LACNIC).

## Step 1: View your BGP routes
<a name="tutorials-byoip-bgp-security-step1"></a>

Once you have BYOIP prefixes provisioned to IPAM, view all advertised routes in the centralized dashboard.

------
#### [ AWS Management Console ]

**To view your BGP routes**

1. Open the IPAM console at [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/). 

1. In the navigation pane, choose **IPAM**, and then choose your IPAM.

1. Under **Monitoring**, choose **Route monitoring**.

The dashboard displays all BYOIP routes with prefix, locale, advertisement status, ASN, RPKI validity, ROA strength, and route overlaps.

------
#### [ Command line ]

Use [get-ipam-discovered-routes](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-ipam-discovered-routes.html) to view discovered routes. This command is available to both Free Tier and Advanced Tier customers.

```
aws ec2 get-ipam-discovered-routes \
    --ipam-resource-discovery-id ipam-res-disco-0365d2977fc1672fe \
    --resource-region us-west-2
```

The following is example output.

```
{
    "IpamDiscoveredRoutes": [
        {
            "IpamResourceDiscoveryId": "ipam-res-disco-0365d2977fc1672fe",
            "ResourceRegion": "us-west-2",
            "ResourceOwnerId": "123456789012",
            "Cidr": "203.0.113.0/24",
            "Asn": "64512",
            "State": "advertised",
            "AdvertisementType": "regional",
            "NetworkBorderGroup": "us-west-2",
            "PoolId": "ipv4pool-ec2-0a1b2c3d4e5f6g7h8",
            "IpamPoolId": "ipam-pool-0da89c821626f1e4b",
            "SampleTime": "2026-03-10T15:30:00+00:00"
        }
    ]
}
```

------

## Step 2: Review route protection findings
<a name="tutorials-byoip-bgp-security-step2"></a>

For Advanced Tier customers, IPAM evaluates routes against published ROA data and surfaces findings with [get-ipam-route-protection-findings](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-ipam-route-protection-findings.html).

**Note**  
get-ipam-route-protection-findings requires the Advanced Tier. Free Tier customers receive an `UnsupportedOperation` error.

1. List all findings.

   ```
   aws ec2 get-ipam-route-protection-findings \
       --ipam-id ipam-0a1b2c3d4e5f6g7h8
   ```

1. Filter for invalid or missing ROAs.

   ```
   aws ec2 get-ipam-route-protection-findings \
       --ipam-id ipam-0a1b2c3d4e5f6g7h8 \
       --filters "Name=rpki-status,Values=invalid,unknown"
   ```

1. Filter by status in a specific Region.

   ```
   aws ec2 get-ipam-route-protection-findings \
       --ipam-id ipam-0a1b2c3d4e5f6g7h8 \
       --filters "Name=rpki-status,Values=invalid" "Name=resource-region,Values=us-west-2"
   ```

The following is example output.

```
{
    "IpamId": "ipam-0a1b2c3d4e5f6g7h8",
    "RouteProtectionFindings": [
        {
            "ResourceOwnerId": "123456789012",
            "ResourceRegion": "us-west-2",
            "IpamPoolId": "ipam-pool-0da89c821626f1e4b",
            "Cidr": "203.0.113.0/24",
            "State": "advertised",
            "AdvertisementType": "regional",
            "NetworkBorderGroup": "us-west-2",
            "PoolId": "ipv4pool-ec2-0a1b2c3d4e5f6g7h8",
            "Asn": "64512",
            "RpkiStatus": "valid",
            "RpkiStrength": "strict",
            "Roas": [
                {
                    "Asn": "64512",
                    "Prefix": "203.0.113.0/24",
                    "MaxLength": 24,
                    "Match": true,
                    "Expiration": "2027-06-15T00:00:00Z"
                }
            ],
            "RouteOverlaps": [
                {
                    "Prefix": "203.0.113.128/25",
                    "Asn": "64513",
                    "DetectedAt": "2026-03-10T15:45:00+00:00"
                }
            ],
            "SampleTime": "2026-03-10T15:30:00+00:00",
            "RoaSampleTime": "2026-03-10T16:00:00+00:00"
        }
    ]
}
```

Valid filter names are `cidr`, `account-id`, `resource-region`, `byoip-cidr-state`, `advertisement-type`, `network-border-group`, `ipam-pool-id`, `rpki-status`, and `asn`. These EC2-style filter names don't always match the returned fields. For example, you filter on `account-id` but the response returns `ResourceOwnerId`, and you filter on `byoip-cidr-state` but the field is `State`. ROA strength is not filterable.

## Step 3: Set up delegated RPKI
<a name="tutorials-byoip-bgp-security-step3"></a>

Delegated RPKI lets you authorize AWS to manage ROAs on your behalf.

1. **Create the Internet Registry Association.**

   ```
   aws ec2 create-ipam-internet-registry-association --region us-east-1 \
       --ipam-id ipam-0de83dba6694560a9 \
       --rir ARIN --org-handle my-arin-org
   ```

   The following is example output.

   ```
   {
       "IpamInternetRegistryAssociation": {
           "IpamInternetRegistryAssociationId": "ipam-internet-registry-assoc-036486dfa6af58ee0",
           "State": "create-in-progress"
       }
   }
   ```

   Run the following command until the state reaches `pending-enable`.

   ```
   aws ec2 describe-ipam-internet-registry-associations --region us-east-1 \
       --ipam-internet-registry-association-ids ipam-internet-registry-assoc-036486dfa6af58ee0
   ```

   Once the state is `pending-enable`, the ChildRequestXml is ready to submit to your RIR. IPAM stages ROAs based on public VRP (Validated ROA Payload) data. They're pending and will be activated once the Internet Registry Association is enabled.

1. **Review the staged ROAs.**

   ```
   aws ec2 get-ipam-route-origin-authorizations --region us-east-1 \
       --ipam-internet-registry-association-id ipam-internet-registry-assoc-036486dfa6af58ee0
   ```

   The following is example output.

   ```
   {
       "Roas": [
           {
               "prefix": "18.96.0.0/14",
               "asn": "77221",
               "maxLength": "24",
               "state": "pending-activate"
           }
       ]
   }
   ```

1. **Enable the Internet Registry Association.**

   Take the ChildRequestXml to your RIR portal and submit the delegation request. The RIR returns a parent response XML. Extract the following fields from that response: RpkiVersion, ServiceUri, ChildHandle, ParentHandle, and ParentBpkiTa. Then call the following command.

   ```
   aws ec2 enable-ipam-internet-registry-association --region us-east-1 \
       --ipam-internet-registry-association-id ipam-internet-registry-assoc-036486dfa6af58ee0 \
       --rpki-version "..." \
       --service-uri "..." \
       --child-handle "..." \
       --parent-handle "..." \
       --parent-bpki-ta "..."
   ```

   The following is example output.

   ```
   {
       "IpamInternetRegistryAssociation": {
           "IpamInternetRegistryAssociationId": "ipam-internet-registry-assoc-036486dfa6af58ee0",
           "State": "enable-in-progress"
       }
   }
   ```

   Run the following command until the state reaches `enable-complete`.

   ```
   aws ec2 describe-ipam-internet-registry-associations --region us-east-1 \
       --ipam-internet-registry-association-ids ipam-internet-registry-assoc-036486dfa6af58ee0
   ```

   Once the state is `enable-complete`, staged ROAs transition to `create-complete`. AWS now manages the ROA lifecycle for all CIDRs under this association.

1. **View associated CIDRs.**

   ```
   aws ec2 get-ipam-internet-registry-association-cidrs --region us-east-1 \
       --ipam-internet-registry-association-id ipam-internet-registry-assoc-036486dfa6af58ee0
   ```

   The following is example output.

   ```
   {
       "IpamInternetRegistryAssociationCidrs": [
           {
               "Cidr": "18.96.0.0/14",
               "LastObservedAt": "2026-07-30T18:00:00.000Z"
           }
       ]
   }
   ```

1. **View associated ASNs.**

   ```
   aws ec2 get-ipam-internet-registry-association-asns --region us-east-1 \
       --ipam-internet-registry-association-id ipam-internet-registry-assoc-036486dfa6af58ee0
   ```

   The following is example output.

   ```
   {
       "IpamInternetRegistryAssociationAsns": [
           {
               "Asn": "77221",
               "LastObservedAt": "2026-07-30T18:00:00.000Z"
           }
       ]
   }
   ```

## Step 4: Provision BYOIP with automated ROA creation
<a name="tutorials-byoip-bgp-security-step4"></a>

With delegated RPKI active, provisioning is simplified.


| Before (without delegated RPKI) | After (with delegated RPKI) | 
| --- | --- | 
| Must provide --cidr-authorization-context | Still pass --cidr-authorization-context, but with Message="CoveredByInternetRegistryAssociation",Signature="" — no signed message is required | 
| Must validate via WHOIS or DNS TXT record | Not required — IPAM verifies against association CIDRs | 
| Must manually create ROAs at RIR before advertising | ROAs auto-created on provisioning | 
| Must manually renew ROAs before expiration | AWS auto-renews — no action needed | 

```
aws ec2 provision-ipam-pool-cidr \
    --cidr 18.97.16.0/24 \
    --ipam-pool-id ipam-pool-0da89c821626f1e4b \
    --cidr-authorization-context Message="CoveredByInternetRegistryAssociation",Signature="" \
    --region us-east-1
```

IPAM validates ownership through the Internet Registry Association and creates strict ROAs matching the pool's locale and ASN. There is no manual ROA step.

## Step 5: Manage ROAs for on-premises prefixes
<a name="tutorials-byoip-bgp-security-step5"></a>

For IP space that is not brought to AWS, use routing policy registrations (RPRs).

1. **Create an RPR.**

   ```
   aws ec2 create-ipam-routing-policy-registration --region us-east-1 \
       --ipam-id ipam-0de83dba6694560a9 \
       --ipam-internet-registry-association-id ipam-internet-registry-assoc-036486dfa6af58ee0 \
       --cidr 18.96.0.0/14 --asns 77221,13446 \
       --permit-more-specific-announcements
   ```

   The following is example output.

   ```
   {
       "deltaId": "0130c368-1f8c-4283-8f16-66e67e633086",
       "state": "PENDING"
   }
   ```

1. **Check delta status.** If the change would invalidate existing routes, it fails with an error. Use `--force` to override.

   ```
   aws ec2 get-ipam-routing-policy-registration-deltas --region us-east-1 \
       --ipam-id ipam-0de83dba6694560a9 \
       --ipam-internet-registry-association-id ipam-internet-registry-assoc-036486dfa6af58ee0 \
       --delta-id 0130c368-1f8c-4283-8f16-66e67e633086
   ```

1. **Batch update (atomic).** Batch updates succeed or fail atomically. There is no partial application.

   ```
   aws ec2 batch-modify-ipam-routing-policy-registrations --region us-east-1 \
       --ipam-id ipam-0de83dba6694560a9 \
       --ipam-internet-registry-association-id ipam-internet-registry-assoc-036486dfa6af58ee0 \
       --delta-json file://delta.json
   ```

   Where `delta.json` contains the following.

   ```
   {
       "Add": [
           {
               "prefix": "18.96.0.0/14",
               "asns": ["77221", "13446"],
               "permit-more-specific-announcements": "false"
           }
       ],
       "Delete": [
           {
               "prefix": "18.97.16.0/24",
               "asns": ["77221", "13446"],
               "permit-more-specific-announcements": "false"
           }
       ]
   }
   ```

1. **View all registrations for an association.**

   ```
   aws ec2 get-ipam-routing-policy-registrations --region us-east-1 \
       --ipam-internet-registry-association-id ipam-internet-registry-assoc-036486dfa6af58ee0
   ```

   The following is example output.

   ```
   {
       "IpamRoutingPolicyRegistrations": [
           {
               "Cidr": "18.96.0.0/14",
               "Asns": ["77221", "13446"],
               "PermitMoreSpecificAnnouncements": false,
               "MaxLength": 14,
               "LatestDeltaId": "0130c368-1f8c-4283-8f16-66e67e633086",
               "State": "create-complete"
           },
           {
               "Cidr": "18.97.16.0/24",
               "Asns": ["77221", "13446"],
               "PermitMoreSpecificAnnouncements": false,
               "MaxLength": 24,
               "LatestDeltaId": "0130c368-1f8c-4283-8f16-66e67e633086",
               "State": "create-complete"
           }
       ]
   }
   ```

1. **Filter to a specific prefix.**

   ```
   aws ec2 get-ipam-routing-policy-registrations --region us-east-1 \
       --ipam-internet-registry-association-id ipam-internet-registry-assoc-036486dfa6af58ee0 \
       --cidr 18.96.0.0/14
   ```

## Step 6: Set up CloudWatch alarms for route anomalies
<a name="tutorials-byoip-bgp-security-step6"></a>

IPAM publishes CloudWatch metrics for each BYOIP route to the global IPAM account. The `RoaExpiration` metric is published to the `AWS/IPAM` namespace with the dimensions `Cidr`, `RoaPrefix`, `Asn`, and `MaxLength`.


| Type | Name | Description | 
| --- | --- | --- | 
| Metric | RoaExpiration | Number of days until the ROA expires | 
| Dimension | Asn | ASN for the prefix | 
| Dimension | Cidr | CIDR brought via BYOIP | 
| Dimension | MaxLength | MaxLength from the ROA | 
| Dimension | RoaPrefix | Prefix from the ROA | 

Because `RoaExpiration` reports the number of days remaining until the ROA expires, alarm when the value drops to or below your threshold. Specify all four dimensions to target a single ROA. Create the alarm in the same account and Region where the metrics are published.

```
aws cloudwatch put-metric-alarm --region us-east-1 \
    --alarm-name "IPAM-RoaExpiration-203.0.113.0-24" \
    --alarm-description "Alert when the ROA for 203.0.113.0/24 is within 30 days of expiration" \
    --namespace "AWS/IPAM" \
    --metric-name RoaExpiration \
    --dimensions Name=Cidr,Value=203.0.113.0/24 Name=RoaPrefix,Value=203.0.113.0/24 Name=Asn,Value=64512 Name=MaxLength,Value=24 \
    --statistic Minimum \
    --period 86400 \
    --evaluation-periods 1 \
    --threshold 30 \
    --comparison-operator LessThanOrEqualToThreshold \
    --treat-missing-data notBreaching \
    --alarm-actions arn:aws:sns:us-east-1:123456789012:roa-expiry-notifications
```

## Cleanup
<a name="tutorials-byoip-bgp-security-cleanup"></a>

To remove delegated RPKI resources:

1. Delete all routing policy registrations.

1. Disassociate the Internet Registry Association.

1. (Optional) Remove the authorization at your RIR portal.

**Important**  
Deleting an Internet Registry Association removes all AWS-managed ROAs for that association. Make sure your routes have alternative ROA coverage before you disassociate.

## Related resources
<a name="tutorials-byoip-bgp-security-related"></a>
+ [Monitor BGP route protection](monitor-bgp-route-security.md)
+ [Tutorial: Bring your IP addresses to IPAM](tutorials-byoip-ipam.md)
+ [Tutorial: Bring your ASN to IPAM](tutorials-byoasn.md)
+ [Monitor IPAM with Amazon CloudWatch](cloudwatch-ipam.md)