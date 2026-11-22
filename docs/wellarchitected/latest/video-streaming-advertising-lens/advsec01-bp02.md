

# ADVSEC01-BP02 Restrict DSP access to allow only authorized SSPs

 In programmatic advertising, DSPs receive bid requests from dozens to hundreds of SSP partners. Without ingress controls that validate each SSP connection, unauthorized parties can submit fraudulent bid requests, access bidding signals, or send invalid traffic. That traffic consumes compute resources without generating revenue. 

 **Desired outcome:** 
+  You have validated every inbound SSP connection against an approved partner list before bid requests reach your bidding logic. 
+  You have ingress controls that operate within the allocated bid-request latency budget. 
+  You have automated updates for SSP allow lists as partnerships change, without infrastructure redeployment. 

 **Common anti-patterns:** 
+  Accepting bid requests from any source without verifying the SSP's identity against sellers.json or an approved partner registry. 
+  Relying exclusively on application-layer validation for SSP authorization, which consumes compute on invalid requests before rejection. 
+  Maintaining static IP allowlists that become stale as SSP infrastructure changes and either over-permit or break partner connections. 

 **Benefits of establishing this best practice:** 
+  Blocks unauthorized bid requests at the network edge before they consume bidding compute resources. 
+  Reduces exposure to bid request injection attacks that attempt to harvest bidding algorithms or audience signals. 
+  Enables supply-path optimization by restricting inbound traffic to verified, high-quality SSP partners. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Ingress protection for bid endpoints uses a defense-in-depth model with three filtering layers, and each layer catches threats the others miss. Network-edge filtering (IP allowlisting) is the fastest and cheapest to run, and also the most brittle. SSPs rotate infrastructure, use CDN-fronted endpoints, and scale across cloud regions, so static IP sets go stale within weeks without automated maintenance. Protocol-layer inspection (OpenRTB field validation) catches semantically invalid bid requests that pass IP checks, but it adds processing latency. Application-layer validation (sellers.json cross-referencing) is the most authoritative check and also the slowest, because it requires external lookups against cached declaration files. 

 The layers compensate for each other's failure modes. When an SSP changes IP ranges without notice, protocol-layer validation still catches unauthorized requests. When a threat actor crafts valid-looking OpenRTB payloads from an authorized IP, sellers.json validation detects the identity mismatch. No single layer provides complete protection. 

 Each filter reads certain OpenRTB fields and assumes they arrive in a certain form. The same field can arrive as a single value on one supply path and as an array on another. It can also arrive empty, absent, or truncated. Each variation needs a representative test, because a filter that treats an unreadable field as acceptable will admit the request. Testing against your own corpus still leaves the forms you have not seen, so stage enforcement. Annotate traffic first, then enforce on a fraction of it. This exposes field behavior across live supply paths, and an unexpected form costs observation rather than lost bids. 

 Tight allowlists improve security but create friction when you onboard new SSPs (days of lead time) or when existing partners scale during high-traffic events. Supply-path optimization through IAB Tech Lab transparency initiatives (sellers.json, ads.txt, and the SupplyChain object) improves both security and bid economics. Reducing authorized supply paths shrinks the attack surface and removes low-quality intermediaries. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Configure AWS WAF IP sets for authorized SSP partners:** Create IP sets containing the known egress IP ranges for each approved SSP. Associate WAF web ACLs with your bid endpoint ALB or CloudFront distribution. Update IP sets dynamically as SSP infrastructure changes using AWS WAF APIs. 

1.  **Configure the module and define each filter criterion:** Configure the [OpenRTB Attribute Module](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/modules.html) (openRtbAttributeModule) on an active link. For each criterion, record the field path, the data type you expect, how a match is evaluated when the field is scalar and when it is an array, and the outcome you expect. Combine criteria with AND logic inside a filter, and combine filters with OR logic. Select the documented INCLUDE or EXCLUDE filter type and the noBid or headerTag action for the intended policy. 

1.  **Validate criteria and promote enforcement in stages:** Build a test set covering a passing request, an unlisted value, a malformed field, a missing field, and an array field where one element is unlisted. Start with the annotating action and a holdback that limits enforcement to a small share of eligible traffic. Record the holdback stages, the promotion threshold each stage must meet, the module version and OpenRTB revision you tested, the accountable owner, the approval date, and the next review date. Promote to the next stage only when the current one meets its threshold. 

1.  **Implement sellers.json validation for SSP verification:** Build a validation layer (Lambda or inline in bid processing) that cross-references the SSP's claimed identity against their published sellers.json. Cache sellers.json lookups to avoid per-request latency. Alert on SSPs whose bid requests don't match their published seller declarations. 

1.  **Establish private connectivity for high-volume SSP partners:** Configure AWS PrivateLink for SSP partners operating on AWS to remove public internet transit for bid traffic. For non-AWS SSPs, use VPC security groups to restrict inbound traffic to documented SSP IP ranges. 

1.  **Enable AWS WAF Bot Control:** Deploy the [AWS WAF Bot Control managed rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-bot.html) on bid endpoints to detect automated invalid traffic. Test labels and actions against expected SSP traffic before blocking requests. 

1.  **Configure rate-based rules:** Add [AWS WAF rate-based rules](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based.html) for each SSP traffic boundary. Alert on unexpected increases, and throttle request floods that exceed the approved traffic profile. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSEC01-BP01 Implement user authentication and access control to protect bidding process and content](advsec01-bp01.md) 
+  [ADVSEC01-BP03 Restrict DSP outbound traffic to authorized SSPs only](advsec01-bp03.md) 
+  [ADVSEC04-BP03 Implement supply chain transparency controls to block ad fraud](advsec04-bp03.md) 

 **Related documents:** 
+  [AWS WAF IP set rules for IPv4 and IPv6](https://repost.aws/knowledge-center/waf-allow-my-ip-block-other-ip) 
+  [AWS PrivateLink documentation](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) 
+  [Network Load Balancer security groups](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-security-groups.html) 
+  [IAB Tech Lab sellers.json specification](https://iabtechlab.com/sellers-json/) 

 **Related services:** 
+  [AWS WAF](https://aws.amazon.com/waf/) 
+  [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) 
+  [AWS PrivateLink](https://aws.amazon.com/privatelink/) 
+  [Amazon CloudFront](https://aws.amazon.com/cloudfront/) 
+  [Amazon API Gateway](https://aws.amazon.com/api-gateway/) 