

# Regional Scope for Policy Updates
<a name="cloudwan-policy-regional-scope"></a>

When making changes to your core network, some policy changes require making edits to multiple regions during the change set execution workflow. When making changes to things like routing policies or service insertion it may not always be immediately obvious that those changes can impact all of the core networks edge locations. Below we have listed the various sections of a core network policy and the regions that would require updates if the change is made. This can help determine whether making changes to your core network policy could require doing work in any particular region which could be dangerous if that region is experiencing issues. 

**Topics**
+ [`version`](#regional-cloudwan-version-json)
+ [`core-network-configuration`](#regional-cloudwan-network-config-json)
+ [`segments`](#regional-cloudwan-segments-json)
+ [`network-function-groups`](#regional-cloudwan-network-functions-json)
+ [`segment-actions`](#regional-cloudwan-segment-actions-json)
+ [`attachment-policies`](#regional-cloudwan-attachment-policies-json)
+ [`attachment-routing-policy-rules`](#regional-cloudwan-attachment-routing-policy-rules-json)
+ [`routing-policies`](#regional-cloudwan-routing-policies-json)

## `version`
<a name="regional-cloudwan-version-json"></a>
+ Changing the `version` will trigger an update in all of your core network edge locations

## `core-network-configuration`
<a name="regional-cloudwan-network-config-json"></a>
+ Changing the following settings on the core network will trigger an update in all of your core network edge locations
  + `vpn-ecmp-support`
  + `dns-support`
  + `security-group-referencing-support`
+ `asn-ranges` and `inside-cidr-blocks` changes will not affect any region by themselves
+ `edge-locations` changes (adding/removing) will trigger work in all edge locations since the connections between all other edge locations needs to be established or torn down for the added/removed edge locations

## `segments`
<a name="regional-cloudwan-segments-json"></a>
+ Adding/removing entries from `segments` will trigger an update in all of your core network edge locations unless the edge-locations field is specified in which case it will use those regions instead
+ The following will also trigger an update in all applicable edge locations (based on the information from the previous line)
  + `isolate-attachments`
  + `deny-filter`
  + `allow-filter`
+ The following will not trigger an update in any edge location
  + `description`
  + `require-attachment-acceptance`

## `network-function-groups`
<a name="regional-cloudwan-network-functions-json"></a>
+ Adding/removing entries from `network-function-groups` will trigger an update in all of your core network edge locations

## `segment-actions`
<a name="regional-cloudwan-segment-actions-json"></a>
+ `share`
  +  Adding/removing segment shares will trigger an update in all segment edge locations (the segment with more edge-locations dictates which edge locations are affected)
+ `create-route`
  +  Adding/removing create-route entries will trigger an update in all edge locations the attachments listed in destinations are located in (or all segment edge locations if blackhole is specified instead)
+ `send-via`
  +  Adding/removing entries in send via will trigger an update in all segment edge locations (the segment with more edge-locations dictates which edge locations are affected)
+ `send-to`
  +  Adding/removing entries in send to will trigger an update in all segment edge locations
+ `associate-routing-policy`
  +  Adding/removing entries in associate-routing-policy will trigger an update in the 2 edge locations that are specified in the edge-location and peer-edge-location parameters

## `attachment-policies`
<a name="regional-cloudwan-attachment-policies-json"></a>
+ Adding/removing/modifying entries here can trigger an update in any region where an attachment is being associated/disassociated from a segment or network function group (for most attachments this will be the region the attachment resource such as the VPC or Site-to-Site VPN exist in, for Direct Connect it will be across all regions the Direct Connect Core Network attachment exists in)

## `attachment-routing-policy-rules`
<a name="regional-cloudwan-attachment-routing-policy-rules-json"></a>
+ Adding/removing/modifying entries here can trigger an update in any region where an attachment is now associated to or being disassociated from a set of routing policies (for most attachments this will be the region the attachment resource such as the VPC or Site-to-Site VPN exist in, for Direct Connect it will be across all regions the Direct Connect Gateway Core Network attachment exists in)

## `routing-policies`
<a name="regional-cloudwan-routing-policies-json"></a>
+ Adding/removing/modifying entries here will affect any resource that the routing policy is connected to this can be an attachment (see Attachment Policies), a segment sharing (See Segment Actions/Share), or between two edge locations (See Segment Actions/AssociateRoutingPolicy).