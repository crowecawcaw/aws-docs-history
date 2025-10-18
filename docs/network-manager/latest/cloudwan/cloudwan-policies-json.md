#  Core network policy version parameters in
 AWS Cloud WAN

The following sections describe the parameters that you use to create a core network
 policy version using JSON. Your JSON file contains two sections that describe the policy
 network settings and segments. You can then add optional sections for defining network
 function groups and segment actions. 

For example JSON policies, see [AWS Cloud WAN core network policy examples](cloudwan-policy-examples.md "cloudwan-policy-examples.md"). 

###### Topics

* [core-network-configuration](#cloudwan-network-config-json "#cloudwan-network-config-json")
* [segments](#cloudwan-segments-json-about "#cloudwan-segments-json-about")
* [network-function-groups](#cloudwan-network-functions-json "#cloudwan-network-functions-json")
* [segment-actions](#cloudwan-segment-actions-json "#cloudwan-segment-actions-json")
* [attachment-policies](#cloudwan-attach-policies-json "#cloudwan-attach-policies-json")

## `core-network-configuration`


The core network configuration section defines the Regions where a core network should
 operate. 


For AWS Regions that are defined in the policy, the core network creates a Core
 Network Edge where you can connect attachments. After it's created, each Core Network
 Edge is peered with every other defined Region and is configured with
 consistent segment and routing across all Regions. Regions can't be
 removed until the associated attachments are deleted.
 `core-network-configuration` is required.


### Parameters


 The following parameters are used in
 `core-network-configuration`:



* General settings allow you to create the foundation of a core network,
 including whether VPN ECMP, DNS, and security group referencing are
 supported. 




	+ `vpn-ecmp-support` — (Optional) Indicates whether the core network forwards traffic over multiple equal-cost routes using VPN. The value can be either `true` or `false`. When set to `true`, traffic can be distributed across multiple VPN tunnels for better throughput and redundancy. The default is `true`.
	+ `dns-support` — (Optional) Indicates whether DNS
	 resolution is enabled for the core network. The value can be either
	 `true` or `false`. When set to
	 `true`, DNS resolution is enabled for VPCs attached
	 to the core network, allowing resources in different VPCs to resolve
	 each other's domain names. The default is `true`. For
	 more information, see [DNS support](cloudwan-vpc-attachment.md#cloudwan-dns-support "cloudwan-vpc-attachment.md#cloudwan-dns-support").
	+ `security-group-referencing-support` — (Optional)
	 Indicates whether security group referencing is enabled for the core
	 network. The value can be either `true` or
	 `false`. When set to `true`, security
	 groups in one VPC can reference security groups in another VPC
	 attached to the core network, enabling more flexible security
	 configurations across your network. The default is
	 `false`. For more information about security group referencing,
	 see [Security group referencing](cloudwan-vpc-attachment.md#cloudwan-sg-referencing "cloudwan-vpc-attachment.md#cloudwan-sg-referencing").


* `asn-ranges` — The Autonomous System Numbers (ASNs) to assign
 to core network edges. By default, the core network automatically assigns an
 ASN for each core network edge, but you can optionally define the ASN in the
 `edge-locations` for each Region. The ASN
 uses an array of integer ranges only from `64512` to
 `65534` and `4200000000` to
 `4294967294`. No other ASN ranges can be used.
* `inside-cidr-blocks` — (Optional) The Classless Inter-Domain
 Routing (CIDR) block range used to create tunnels for AWS Transit Gateway Connect.
 The format is standard AWS CIDR range (for example,
 `10.0.1.0/24`). You can optionally define the inside CIDR in
 the core network edges section per Region. The minimum is a `/24`
 for IPv4 or `/64` for IPv6. You can provide multiple
 `/24` subnets or a larger CIDR range. If you define a larger
 CIDR range, new core network edges will be automatically assigned
 `/24` and `/64` subnets from the larger CIDR. an
 Inside CIDR block is required for attaching Connect attachments to a Core
 Network Edge.
* `vpn-ecmp-support` — (Optional) Indicate whether the core
 network forwards traffic over multiple equal-cost routes using VPN. The
 value can either be `true` or `false`. The default is
 `true`.
* `edge-locations` — An array of AWS Region locations where you're
 creating core network edges. The array is composed of the following
 parameters:




	+ `location` — An AWS Region code, such as
	 `us-east-1`.
	+ `asn` — (Optional) The ASN of the core network edge in an
	 AWS Region. By default, the ASN will be a single integer
	 automatically assigned from `asn-ranges`. 
	
	
	###### Note
	
	You can't change the ASN of a core network edge. Any transit gateway with the same ASN can't be peered to that core network edge. For example, if you have a core network edge with an ASN of `64512`, you can't peer any transit gateway that also has an ASN of `64512`.
	+ `inside-cidr-blocks` — (Optional) The local CIDR blocks for
	 this core network edge for AWS Transit Gateway Connect attachments. By
	 default, this CIDR block will be one or more optional IPv4 and IPv6
	 CIDR prefixes auto-assigned from `inside-cidr-blocks`. 
	
	
	###### Note
	
	You can't delete the inside CIDR block once it's assigned to a
	 core network edge.

For example, you might have the following core network configuration. This
 core network configuration establishes a Cloud WAN core network with VPN ECMP and
 DNS support enabled, while disabling security group referencing across VPCs. It
 allocates two internal CIDR blocks (`10.0.0.0/16` and
 `10.1.0.0/16`) for network connectivity, defines an ASN range of
 `65000-65100`, and deploys a single edge location in
 `us-east-1`, providing the foundation for a managed wide area
 network. 



```
{
 "version": "2021.12",
 "core-network-configuration": {
    "vpn-ecmp-support": true,
    "dns-support": true,
    "security-group-referencing-support": false,
    "inside-cidr-blocks": [
        "10.0.0.0/16",
        "10.1.0.0/16"
    ],
    "asn-ranges": [
        "65000-65100"
    ],
    "edge-locations": [
        {
        "location": "us-east-1"        
        }
    ]
 }
 ...
}
```

## `segments`


The segments section defines the different segments in the network. Here you can
 provide descriptions, change defaults, and provide explicit regional, operational, and
 route filters. The names defined for each segment are used in the segment-actions and
 attachment-policies section. Each segment is created and operates as a completely
 separate routing domain. By default, attachments can only communicate with other
 attachments in the same segment. `segments` is a required section.


### Parameters


The following parameters are used in `segments`:



* `segments` — At least one segment must be defined and composed of
 the following parameters:




	+ `name` — The name of the segment. The `name`
	 is a string used in other parts of the policy document, as well as
	 in the console for metrics and other reference points. Valid
	 characters are a–z, A–Z, and 0–9.
	
	
	###### Note
	
	There is no ARN or ID for a segment.
	+ `description` — (Optional) A user-defined string describing
	 the segment.
	+ `edge-locations` — (Optional) Allows you to define a more
	 restrictive set of Regions for a segment. The edge
	 location must be a subset of the locations that are defined for
	 `edge-locations` in the core-network-configuration.
	 These locations use the AWS Region code. For example, you might
	 want to use `us-east-1` as an edge
	 location.
	+ `isolate-attachments`  — (Optional) This Boolean setting
	 determines whether attachments on the same segment can communicate
	 with each other. The default value is `false`. When set
	 to `true`, the only routes available will either be
	 shared routes through the share actions, which are attachments in
	 other segments, or static routes. For example, you might have a
	 segment dedicated to `development` that should never
	 allow VPCs to talk to each other, even if they’re on the same
	 segment. In this example, you would set the parameter to
	 `true`.
	
	
	###### Note
	
	Routes coming from a route table attachment are not affected
	 by the `isolate-attachments` parameter. You are
	 responsible for managing routes propagating from their attached
	 route tables. Routes flowing into the route table attachment
	 from other attachments within the segment follow the standard
	 `isolate-attachments` behavior
	+ `require-attachment-acceptance` — (Optional) This Boolean
	 setting determines whether attachment requests are automatically
	 approved or require acceptance. The default is `true`,
	 indicating that attachment requests require acceptance. For example,
	 you might use this setting to allow a `sandbox` segment
	 to allow any attachment request so that a core network or attachment
	 administrator does not need to review and approve attachment
	 requests. In this example,
	 `require-attachment-acceptance` is set to
	 `false`.
	
	
	###### Note
	
	If `require-attachment-acceptance` is
	 `false` for a segment, it's still possible for
	 attachments to be added to or removed from a segment
	 automatically when their tags change. If this behavior is not
	 desired, set `require-attachment-acceptance` to
	 `true`.
	+ `deny-filter` — (Optional) An array of segments that
	 disallows routes from the segments listed in the array. It is
	 applied only after routes have been shared in
	 `segment-actions`. If a segment is listed in the
	 `deny-filter`, attachments between the two segments
	 will never have routes shared across them. For example, you might
	 have a financial `payment` segment that should
	 never share routes with a `development` segment,
	 regardless of how many other share statements are created. Adding
	 the `payments` segment to the
	 `deny-filter` parameter prevents any shared routes
	 from being created with other segments.
	+ `allow-filter` (optional) — An array of segments that
	 explicitly allows only routes from the segments that are listed in
	 the array. Use the `allow-filter` setting if a segment has a well-defined group of
	 other segments that connectivity should be restricted to. It is
	 applied after routes have been shared in
	 `segment-actions`. If a segment is listed in
	 `allow-filter`, attachments between the two segments
	 will have routes if they are also shared in the
	 `segment-actions` area. For example, you might have a
	 segment named `video-producer` that should only
	 ever share routes with a `video-distributor` segment, no
	 matter how many other share statements are created.
	
	
	###### Note
	
	 You can use either `allow-filter` or `deny-filter`, but you can't use
	 both of them simultaneously. These are optional fields used to more
	 explicitly control segment sharing. These parameters are not
	 required in order to receive or send routes between segments.

## `network-function-groups`


`network-function-groups` defines the container for the service insertion
 actions you want to include. This will include any attachment policies.



* `name` — Required. This identifies the network function group
 container.
* `description` — Optional description of the network function
 group.
* `require-attachment-acceptance` — This will be either
 `true`, that attachment acceptance is required, or
 `false`, that it is not required.

## `segment-actions`


`segment-actions` define how routing works between segments. By default,
 attachments can only communicate with other attachments in the same segment. You can use
 `segment-actions` to:



* `share` attachments across segments. Use the `share`
 action so that attachments from two different segments can reach each other. For
 example, if you’ve set a segment to `isolate-attachments`, the
 segment can't reach anything unless it has a `share` relationship
 with other segments. The `share` statement creates routes between
 attachments in the provided segments. If you're creating a share between one
 segment and an array of segments, the segment to share allows attachments from
 the segments in the array. However, sharing does not occur between the segments
 within the array. For example, if a segment named `shared-service` is
 defined as a segment with a `share-with` array of segments named
 `prod` and `prod2`, the network policy will allow the
 attachments in both `prod` and `prod2` to reach
 `shared-service`. But the network policy will not allow sharing
 of attachments between `prod` and `prod2`.
* `create-route` to define a static route in a segment.

###### Note

Sharing routes occurs between segments. All attachments connected to the same
 segment will share a similar routing behavior globally. If some attachments differ
 from other attachments in the same segment, those attachments should be within their
 own segments. This is intentional to prevent a proliferation of segments where one
 segment equals one attachment. 


`segment-actions` is an optional section.


### Parameters


The following parameters are used in `segment-actions`:



* `action` — The action to take for the chosen segment. The
 `action` can be any of the following: 




	+ `share` for a shared route
	+ `create-route` for a route
	+ `send-via` for service insertion, indicating that
	 traffic is sent from one Cloud WAN attachment to another
	 (east-west).
	+ `send-to` for service insertion, indicating that
	 traffic is sent out from the cloud and doesn't re-enter
	 (north-south).
The following parameters are described for these
 actions.
* `share` parameters. If the action to take is share, the following
 parameters are required. `share` is the default action
 behavior.




	+ `segment` — The name of the segment created in the
	 `segments` section to share.
	+ `mode` — `attachment-route` is the only
	 supported value. This mode places the attachment and return routes
	 in each of the `share-with` segments. For example, if
	 there are static routes or routes shared from other segments, those
	 will not be shared through the `attachment-route`
	`mode`.
	+ `share-with` — An array of segments that will have
	 reachability with the segment defined. The core network will create
	 mutual advertisements between these `share-with` segments
	 and the defined segment attachments.
	
	
	For example, if you create a `share` between a segment
	 named `shared-services` and share-with “A” and “B”,
	 this allows the attachments from “A” and “B” to reach “Shared
	 services”. “A” and “B” cannot reach each other, and any static
	 routes or routes propagated from other segments are not shared among
	 these segments.
	
	
	Use "`*`" as a wild card to reference all segments instead
	 of explicitly calling out segments individually.
	+ `except` — Explicitly exclude segments, encapsulated within
	 a `share-with` block. For example,
	
	
	
	```
	{
	      "action": "share",
	      "mode": "attachment-route",
	      "segment": "segment",
	      "share-with": {
	        "except": [
	          "dev",
	          "prod"
	        ]
	      }
	    }
	```
* `create-route` parameters. If the action is
 `create-route`, the following are the required and optional
 parameters.




	+ `segment` — The name of the segment created in the
	 `segments` section, which must be a static route. If
	 you need to duplicate the static route in multiple segments, use
	 multiple `create-route` statements.
	+ `destination-cidr-blocks` — The static route to create. A
	 segment should have the same routing behavior for a certain
	 destination. This means if one Region has a route to
	 a destination, other Regions should also have that
	 route, but with potentially different paths. You can define the IPv4
	 and IPv6 CIDR notation for each AWS Region. For example,
	 `10.1.0.0/16` or `2001:db8::/56`. This is
	 an array of CIDR notation strings.
	+ `destinations` — Defines the list of attachments to send
	 the traffic to, with up to one `attachment-id` per
	 Region. Because a segment is a global object, you
	 should design your routing so that every AWS Region has an
	 attachment in the destinations list. Regions that do
	 not have attachments in this list will receive a propagated version
	 of this route through cross-Region peering
	 connections, and will use the static route of another
	 Region. This is the same case for multiple
	 attachments that are defined across multiple remote
	 Regions. Instead of an array of attachments, you can
	 also provide a `blackhole`, which drops all traffic to
	 the `destination-cidr-blocks`. 
	
	
	###### Note
	
	
	
		- AWS Cloud WAN does not propagate blackhole routes.
	+ `description` — (Optional) A user-defined description to
	 help further identify this route.


* `send-via` and `send-to` parameters. If the network
 function group segment `action` is either `send-via`
 or `send-to`. Use `send-via` if you want to send
 east-west traffic between VPCs. Use `send-to` for north-south
 traffic; that is, traffic that first must come into your security appliance
 and then out to either the Internet or an on-premises location. 


The following are the required and optional parameters:




	+ `segment` — Required. The name of an existing segment
	 that can be used for the `send-via` or
	 `send-to` action.
	+ `mode` — This only applies when the `action`
	 is `send-via`, and indicates the mode used for packets.
	 This will be either `single-hop` or
	 `dual-hop`. `send-to` does not rely on
	 `mode` for traffic.
	+ `when-sent-to` parameters are used to list the
	 destination segments for the `send-via` or
	 `send-to` action. 
	
	
	
	
		- `segments` — The list of segments that the
		 `send-via` action uses. `segments`
		 is not used for the `send-to` action.
	+ `via` parameters describe the network function groups
	 and any edge overrides associated with the
	
	
	
	
		- `network-function-groups` — The network
		 function group to use for the service insertion
		 action.
		- `with-edge-overrides` parameters describe any
		 edge overrides and the preferred edge to use.
		
		
		
		
			* `edge-sets` — The list of edges
			 associated with the network function group.
			* `use-edge` — The preferred edge to
			 use.
The following example shows an example of the `send-via`
 action:




	+ Traffic is sent via a segment named
	 `development`.
	+ the `via` parameter, which contains the details of the
	 edge locations and overrides. It uses a network function group named
	 `inspection-vpc` and has two defined
	 `edge-sets`, `corenetwork1`and
	 `corenetwork2`. `corenetwork2` is set as
	 the preferred core network edge (`use-edge`).

```
{
        "segment": "SendToInspectionVPC", 
        "action": "send-via",
        "mode": "single-hop",
        "when-sent-to": { 
            "segments ": [ 
                "development" 
            ]
        }, 
        "via": { 
            "network-function-groups": [
                "inspection-vpc"
            ], 
            "with-edge-overrides ": [ 
                { 
                    "edge-sets ": [ 
                        ["corenetwork1", "corenetwork2"] 
                    ], 
                    "use-edge": "corenetwork2" 
                } 
            ] 
        } 
    }
```

The following example shows an example of the `send-to` action. In this
 example, traffic is sent to a segment named `development` through a
 network function group named `inspection-vpc`.



```
{
      “action”: “send-to”,
      “segment”: “development”,
      “via”: {
        “network-function-groups”: [
          “inspetion-vpc”
        ]
      }
    }
]
```

## `attachment-policies`


In a core network, all attachments use the `attachment-policies` section to
 map an attachment to a segment. Instead of manually associating a segment to each
 attachment, attachments use tags. The tags are then used to associate the attachment to
 the specified segment or network function group. A core network supports the following
 types of attachments:



* Transit Gateway Connect — `connect`
* Direct Connect gateway — `direct-connect-gateway`
* VPC — `vpc`
* VPN — `site-to-site-vpn`
* Transit Gateway route table — `transit-gateway-route-table`

For example, to attach a VPC to a core network, either the VPC owner or the core
 network owner would create a core network attachment in the core network using either
 the AWS Cloud WAN console or the Network Manager `create-attachment` command line or API. The
 attachment itself will have tags analyzed by the attachment policy, and not the tags
 associated with the VPC resource. A tag on the attachment such as `“environment” :
 “development”`  would then map to a `development` segment.
 Attachment policy rules can also use available metadata from within the conditions, such
 as `account ID`, `type` of attachment, the `resource
 ID` (for example, `vpc-id`), or the AWS Region.


Rules are assigned numbers for processing, and are processed in order by number, from
 lowest to highest. When a match is made, the action is taken and no further rules are
 processed. A single attachment can only be associated to a single segment. If no rules
 are matched (for example, there might be a misspelled tag value), the attachment won't
 be associated to a segment. 


When an attachment matches a rule, the attachment attaches to the segment defined
 `segment`. Each attachment can either be associated without acceptance or
 require a separate action to approve the attachment association. By default, every
 segment requires all attachments to be accepted. The acceptance requirement can be
 turned off with `“require-attachment-acceptance” : false` in the
 `segment` definition. When `require-acceptance` is
 `false`, any attachment that maps to the segment is automatically added.
 For example, a developer `sandbox` segment might want to allow any attachment
 with the correct tag to be added to the network. With the
 `attachment-policies`, you can add additional controls on a per-rule
 basis. For example, if attachments from the `us-east-2`
 Region require acceptance but other Regions do not, you
 can set the `“require-acceptance” : true` setting on a rule that is specific
 to `us-east-2` .


You can apply multiple conditions using either `and` or `or`
 logic to create a single rule. For example, you can state that if the account is
 `111122223333` and includes the tag `“stage” :
 “development”` it should map to a specified segment. If you don't want to use
 tags to map attachments, you could use the `resource-id` to manually map each
 incoming connection to a segment. However, this approach requires changing the policy
 document every time new attachments are added and can reduce the operability of your
 current LIVE policy.


If you're creating an attachment policy that includes a network functions group for
 service insertion, an attachment is required. If you attempt to create a service
 insertion policy that doesn't include an attachment, policy generation will fail.


`attachment-policies` is an optional section.


### Parameters


The following parameters are used in `attachment-policies`:



* `rule-number` — An integer from `1` to
 `65535` indicating the rule's order number. Rules are
 processed in order from the lowest numbered rule to the highest. Rules stop
 processing when a rule is matched. It's important to make sure that you
 number your rules in the exact order that you want them processed.
* `description` — (Optional) A user-defined description that
 further helps identify the rule.
* `condition-logic` — Evaluates a condition on either
 `and` or `or`. This is a mandatory parameter only
 if you have more than one condition. The conditions themselves are
 unordered, so the `condition-logic` applies to all of the
 conditions for a rule, which also means nested conditions of
 `and` or `or` are not supported. Use
 `and` if you want to the rule to match on all of the
 conditions, or use `or` if you want the rule to match on one of
 the conditions. 


If you're creating a JSON policy for a network function group
 `and` and `or` are the only supported
 `condition-logic` options.
* `conditions` — An array composed of one of the four following
 types: 




	1. `type` where the `value` is `any` —
	 This matches any request. For example, you could use any if you're
	 only using one segment that everything should map to. Or, you could
	 use this as a fallback segment if you want all attachments that
	 don't match a rule to map to a known segment.
	2. `type` where 
	
	
	
	
		+ `value` = `resource-id` |
		 `account-id` | `region` |
		 `attachment-type`
		+ `operator` = `equals` |
		 `not-equals` | `contains` |
		 `begins-with`
	This type is the `value` compared against the
	 `operator`. For example, you might use the
	 `condition`
	`type` in the following way:
	
	
	
	
		+ where the `resource-id` uses the resource
		 associated with the attachment (for example,
		 `vpc-1234567890123456`)
		+ where the `account-id` uses the account ID of
		 the requesting attachment (for example,
		 `111122223333`)
		+ where the `Region` uses the
		 Region code for the requesting attachment
		 (for example, `us-east-1`), and
		+ where the `attachment-type` uses
		 `vpc`, `site-to-site-vpn`,
		 `connect`, or
		 `transit-gateway-route-table` strings
	3. `type` where the `value` is
	 `tag-exists` — A string that matches against any of
	 the keys defined on the attachment. Use this type when the value of
	 the tag is not important, or if there is only a key without a
	 value.
	
	
	A network function group attachment policy requires that you use
	 the `tag-exists` type and then either `tag-name` or `tag-value`.
	4. `type` where the `value` is
	 `tag-value` — Evaluates the following key value
	 parameters:
	
	
	
	
		+ `key` — A string that matches against any of
		 the keys defined on the attachment. It must be an exact
		 match of the key.
		+ `operator` — The operation to perform against
		 the key value. Must be one of `equals` |
		 `not-equals` | `contains` |
		 `begins-with`.
		
		
		`operator` is not supported for tag-name in a
		 network function group policy version.
		+ `value` — The value of the key to be evaluated
		 for the operator.
	In this example, 
	
	
	`“type” : “tag-value”,`
	
	
	`“key” : “project”,`
	
	
	`“operator” : “begins-with”,`
	
	
	`“value” : “sta”`
	
	
	Any condition where the value of `project` begins with
	 `sta` is matched against the condition. This would
	 return `staging`, `stage`, etc.
* `description` — A user-defined description to help further
 identify the attachment policy.
* `action` — The action to take when a condition is true.




	+ `association-method` — Defines how a segment is mapped.
	 Values can be `constant` or `tag`.
	 `constant` statically defines the segment to
	 associate the attachment to. `tag` uses the value of a
	 tag to dynamically try to map to a segment.
	+ `segment` — The name of the segment to share as defined
	 in the `segments` section. This is used only when the
	 `association-method` is constant.
	+ `tag-value-of-key` — Maps the attachment to the value
	 of a known key. This is used with the `association-method`  is `tag`. For example a tag of `“stage” :
	 “test”,` will map to a segment named `test`.
	 The value must exactly match the name of a segment. This allows you
	 to have many segments, but use only a single rule without having to
	 define multiple nearly identical conditions. This prevents creating
	 many similar conditions that all use the same keys to map to
	 segments.
	+ `require-acceptance` — Determines if this mapping
	 should override the segment value for
	 `require-attachment-acceptance`. You can only set
	 this to `true`, indicating that this setting applies only
	 to segments that have `require-attachment-acceptance` set
	 to `false`. If the segment already has the default
	 `require-attachment-acceptance`, you can set this to
	 inherit segment’s acceptance value.
	+ `add-to-network-function-group` — The name of the
	 network function group to attach to the attachment policy. The
	 network function group must use `and` for the
	 `condition-logic` and have an associated
	 `Conditions` tag. 
	
	
	The following shows an example policy adding a network function
	 group named `SendToInspectionVPC`. The rule-number for
	 the service insertion policy `125`. It uses the and
	 condition-logic with a `tag` type of
	 `tag-exists` type and a `key` value of
	 `Location`.
	
	
	
	```
	"attachment-policies": [
	    {
	      "rule-number": 125,
	      "description": "Sends to Inspection VPC",
	      "condition-logic": "and",
	      "conditions": [
	        {
	          "type": "tag-exists",
	          "key": "Location"
	        }
	      ],
	      "action": {
	        "add-to-network-function-group": "SendToInspectionVPC"
	      }
	    }
	  ]
	}
	```
