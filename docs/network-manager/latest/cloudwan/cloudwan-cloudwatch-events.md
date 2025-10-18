# Monitor with Amazon CloudWatch Events

You can monitor your core network using Amazon EventBridge, which delivers a near-real-time stream
 of system events that describe changes in your resources. You set up simple rules, which
 then can match events and route them to one or more target functions or streams. For more
 information, see the [Amazon EventBridge User Guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/ "https://docs.aws.amazon.com/eventbridge/latest/userguide/").

The following events can be sent to EventBridge:


* [Topology changes](#cloudwan-events-topology "#cloudwan-events-topology")
* [Route changes](#cloudwan-events-routes "#cloudwan-events-routes")
* [Status updates](#cloudwan-events-status "#cloudwan-events-status")
* [Policy updates](#cloudwan-events-policy "#cloudwan-events-policy")
* [Segment update events](#cloudwan-events-segments "#cloudwan-events-segments")
* [Network function group update events](#cloudwan-events-nfg "#cloudwan-events-nfg")

## Topology changes


Topology change events occur when there are changes to your core network resources.
 These changes include the following:



* An Edge location has been added to the Core Network.
* An edge location has been deleted from the Core Network.
* A Site-to-Site VPN attachment has been created for a Core Network.
* A Site-to-Site VPN attachment has been deleted for a Core Network.
* A VPC attachment has been created for a Core Network.
* A VPC attachment has been deleted for a Core Network.
* A Site-to-Site VPN attachment has been created for a Core Network.
* A Site-to-Site VPN attachment has been deleted for a Core Network.
* A Connect attachment has been created for a Core Network.
* A Connect attachment has been deleted for a Core Network.
* A Connect peer attachment has been created for a Core Network.
* A Connect peer attachment has been deleted for a Core Network.
* A Direct Connect Gateway attachment has been created for a Core Network.
* A Direct Connect Gateway attachment has been deleted for a Core Network.
* A Direct Connect Gateway attachment has been updated for a Core
 Network.

 The following example shows a topology update event where a core network VPC
 attachment has been deleted.



```
{ 
  "version": "0", 
  "id": "13143a7e-806e-a904-300b-ef874c56eaac", 
  "detail-type": "Network Manager Topology Change", 
  "source": "aws.networkmanager", 
  "account": "111122223333", 
  "time": "2021-09-02T12:00:38Z", 
  "region": "us-west-2", 
  "resources": [ 
    "arn:aws:networkmanager::111122223333:global-network/global-network-021345abcdef6789", 
    "arn:aws:networkmanager::111122223333:core-network/core-network-abcdef01234567890"   
  ], 
  "detail": { 
    "changeType": "VPC-ATTACHMENT-DELETED", 
    "changeDescription": "A VPC attachment has been deleted from a Core Network.", 
    "edgeLocation": "us-east-2", 
    "attachmentArn": "arn:aws:networkmanager::111122223333:attachment/attachment-1234567890abcdef0",
    "vpcArn": "arn:aws:ec2:us-east-2:212869205455:vpc/vpc-049a3a24f48fcc47d", 
    "coreNetworkArn": "arn:aws:networkmanager::111122223333:core-network/core-network-abcdef01234567890"   
  } 
}
```

## Route changes


Routing events occur when there are changes to your core network routes. These changes
 include the following:



* Routes in one or more segments have been installed.
* Routes in one or more segments have been uninstalled.

 The following example shows a routing update event where a route was installed in one
 or more segments.



```
{ 
   "version": "0", 
   "id": "13143a7e-806e-a904-300b-ef874c56eaac", 
   "detail-type": "Network Manager Routing Update", 
   "source": "aws.networkmanager", 
   "account": "111122223333", 
   "time": "2021-09-02T12:00:38Z", 
   "region": "us-west-2", 
   "resources": [ 
     "arn:aws:networkmanager::111122223333:global-network/global-network-021345abcdef6789", 
     "arn:aws:networkmanager::111122223333:core-network/core-network-abcdef01234567890" 
   ], 
   "detail": { 
     "changeType": "SEGMENT-ROUTES-INSTALLED", 
     "changeDescription": "Routes in one or more Segments have been installed.", 
     "region": "us-east-2", 
     "segments": [ 
       "development" 
     ], 
     "sequenceNumber": 1630585228195, 
     "routes": [ 
       { 
         "destinationCidrBlock": "169.254.137.220/30", 
         "attachments": [ 
           { 
             "attachmentId": "attachment1234567890abcdef0", 
             "attachmentType": "vpn", 
             "vpnOutsideIpAddress": "3.138.83.40" 
           } 
         ],
         "routeType": "route_propagated", 
         "routeState": "active", 
         "propagatedRouteFamily": "bgp", 
         "bgpAttributes": { 
           "med": "0", 
           "asPath": [ "AS_SEQ: [65001]" ] 
         } 
       } 
     ], 
     "coreNetworkArn": "arn:aws:networkmanager::111122223333:core-network/core-network-abcdef01234567890"
   } 
 }
}
```

## Status updates


Routing events occur when there are changes to your core network status. These changes
 include the following:



* IPsec for a VPN connection has gone down.
* IPsec for a VPN connection has come back up.
* BGP for a VPN connection has gone down.
* BGP for a VPN connection has come back up.
* BGP for a Connect peer connection has gone down.
* BGP for a Connect peer connection has come back up.

 The following example shows a status update event where IPsec for a VPN connection
 has come up.



```
{ 
   "version": "0", 
   "id": "13143a7e-806e-a904-300b-ef874c56eaac", 
   "detail-type": "Network Manager Status Update", 
   "source": "aws.networkmanager", 
   "account": "111122223333", 
   "time": "2021-09-02T12:00:38Z", 
   "region": "us-west-2", 
   "resources": [ 
     "arn:aws:networkmanager::111122223333:global-network/global-network-021345abcdef6789", 
     "arn:aws:networkmanager::111122223333:core-network/core-network-abcdef01234567890" 
   ], 
   "detail": { 
     "changeType": "VPN-CONNECTION-IPSEC-UP", 
     "changeDescription": "IPsec for a VPN connection has come up.", 
     "region": "us-west-2", 
     "attachmentArn": "arn:aws:networkmanager::111122223333:attachment/attachment-1234567890abcdef0", 
     "outsideIpAddress": "35.161.41.136", 
     "coreNetworkArn": "arn:aws:networkmanager::111122223333:core-network/core-network-abcdef01234567890" 
   } 
 }
```

## Policy updates


Routing events occur when there are changes to your core network policies. These
 changes include the following:



* A change set is ready to run for a core network policy.
* A change set was run successfully for a core network policy.

 The following example shows a policy update event where a change set was run
 successfully.



```
{ 
   "version": "0", 
   "id": "13143a7e-806e-a904-300b-ef874c56eaac", 
   "detail-type": "Network Manager Policy Update", 
   "source": "aws.networkmanager", 
   "account": "111122223333", 
   "time": "2021-09-02T12:00:38Z", 
   "region": "us-west-2", 
   "resources": [ 
     "arn:aws:networkmanager::111122223333:global-network/global-network-1234567890abcdef0", 
     "arn:aws:networkmanager::111122223333:core-network/core-network-abcdef01234567890" 
   ], 
   "detail": { 
     "changeType": "CHANGE-SET-EXECUTED", 
     "changeDescription": "A change-set has been sucessfully executed for a Core Network policy.", 
     "policyVersionId":"1",
     "coreNetworkArn": "arn:aws:networkmanager::111122223333:core-network/core-network-abcdef01234567890"
   } 
 }
```

## Segment update events


Routing events occur when there are changes to your core network segments. These
 changes include the following:



* An attachment was associated with a segment.
* An attachment was mapped to a different segment.
* An attachment was disassociated from a segment.

 The following example shows a segment update event where an attachment was mapped to
 a different segment.



```
{ 
   "version": "0", 
   "id": "13143a7e-806e-a904-300b-ef874c56eaac", 
   "detail-type": "Network Manager Segment Update", 
   "source": "aws.networkmanager", 
   "account": "111122223333", 
   "time": "2021-09-02T12:00:38Z", 
   "region": "us-west-2", 
   "resources": [ 
     "arn:aws:networkmanager::111122223333:global-network/global-network-021345abcdef6789", 
     "arn:aws:networkmanager::111122223333:core-network/core-network-abcdef01234567890" 
   ], 
   "detail": { 
     "changeType": "ATTACHMENT-ASSOCIATION-MODIFIED", 
     "changeDescription": "An attachment has been mapped to a different Segment.", 
     "attachmentArn": "arn:aws:networkmanager::111122223333:attachment/attachment-1234567890abcdef0",
     "previousSegmentName": "development",
     "segmentName": "production",
     "edgeLocation": "us-west-2",
     "coreNetworkArn": "arn:aws:networkmanager::111122223333:core-network/core-network-abcdef01234567890"
   } 
 }
```

## Network function group update events


A network function group event occurs when any of the following changes occur:



* An attachment was associated with a different network function group.
* An attachment was mapped to a different network function group
* An attachment was disassociated from a network function group.

 The following example shows a network function group update event where an attachment
 is associated with a different network function group.



```
{ 
   "version": "0", 
   "id": "13143a7e-806e-a904-300b-ef874c56eaac", 
   "detail-type": "Network Function Group Update", 
   "source": "aws.networkmanager", 
   "account": "111122223333", 
   "time": "2024-06-12T12:00:00Z", 
   "region": "us-west-2", 
   "resources": [ 
     "arn:aws:networkmanager::111122223333:global-network/global-network-021345abcdef6789", 
     "arn:aws:networkmanager::111122223333:core-network/core-network-abcdef01234567890",
     "arn:aws:networkmanager::111122223333:attachment/attachment-1234567890abcdef0"
   ], 
   "detail": { 
     "changeType": "ATTACHMENT_MODIFIED", 
     "changeDescription": "An attachment is disassociated from network function group and associated with a new function group.", 
     "attachmentArn": "arn:aws:networkmanager::111122223333:attachment/attachment-1234567890abcdef0",
     "previousNetworkFunctionGroupName": "development",
     "newNetworkFunctionGroupName": "production",
     "edgeLocation": "us-west-2",
     "coreNetworkArn": "arn:aws:networkmanager::111122223333:core-network/core-network-abcdef01234567890"
   } 
 }
```
