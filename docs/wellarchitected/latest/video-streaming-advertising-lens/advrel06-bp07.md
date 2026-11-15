

# ADVREL06-BP07 Implement capability detection and fallback creative mapping for all innovative format campaigns
<a name="advrel06-bp07"></a>

 Not all player environments support innovative ad formats. A squeeze-back instruction sent to an incompatible player results in no ad display and zero revenue. Every innovative format campaign must have a fallback creative that is served automatically to incompatible players. 

 **Desired outcome:** 
+  Every innovative format ad request is preceded by capability detection, incompatible players automatically receive a standard fallback creative. 
+  Every innovative format campaign has a mandatory fallback creative mapped at trafficking time, campaign setup is rejected if no fallback is provided. 
+  Fallback activation rates are monitored to identify the fraction of inventory that doesn't support each format type. 

 **Common anti-patterns:** 
+  Serving innovative format instructions to players without verifying capability support 
+  No fallback creative mapped to innovative format campaigns, format failure results in empty ad slot 
+  Client-side rendering failures that go unreported, silent revenue loss 
+  No systematic testing of fallback paths across device/player combinations 

 **Benefits of establishing this best practice:** 
+  Capability detection with mandatory fallback supports 100% ad slot utilization regardless of format support. 
+  Publisher revenue is protected even when innovative formats fail, as the system automatically falls back to standard creatives that generate baseline CPMs. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 *Player fragmentation* means that format support varies across devices, player versions, and operating systems, so a squeeze-back that renders on one player produces nothing on another. 

 A capability flag is a claim about what a player can render, and it is only useful if every player version reports the flag identically. SDK owners decide what a capability flag means, and ad decisioning owners decide how to act on it. When those definitions drift apart, the ADS acts on ambiguous signals. 

 Choose serving scope based on device compatibility and the amount of addressable inventory each format provides. When device compatibility varies, narrow serving on confirmed devices reduces the risk of serving an incompatible format. 

 A player can receive an unsupported instruction, render nothing, and return no error to the ADS, so revenue for that slot vanishes without a signal. A fallback creative delivers a standard ad when an innovative format fails to render. Untested fallback paths can fail on the device even when their mapping is correct at trafficking. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Implement player capability detection in the SDK:** Extend the player's ad request parameters to include a capability flags field. Populate flags based on runtime detection: overlay support, squeeze-back/resize support, IAB SIMID support, pause event handling, commerce integration capability. Document the flag schema and confirm all player versions report consistently. 

1.  **Enforce fallback creative requirement at campaign trafficking:** Configure your campaign management system to require a standard fallback creative for all innovative format campaigns. Reject campaign trafficking attempts that lack a mapped fallback. Validate that fallback creatives are pre-approved and meet brand safety standards. 

1.  **Implement ADS capability-routing logic:** When the ADS receives a bid request with capability flags, route to the appropriate creative: innovative format if flags indicate support, standard fallback if not. Log the routing decision per request for compatibility matrix analysis. 

1.  **Test fallback paths quarterly across device/player combinations:** Maintain a compatibility test matrix covering your top device types and player versions. Run quarterly tests that verify: capability detection correctly identifies support/non-support, fallback routing delivers the correct creative to incompatible devices, fallback fill rate is 100% across all device/format combinations. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL04-BP02 Architect defensively against failures](advrel04-bp02.md) 
+  [ADVREL04-BP04 Design your workloads to withstand failures of individual components](advrel04-bp04.md) 

 **Related documents:** 
+  [IAB SIMID specification](https://iabtechlab.com/standards/simid/) 

 **Related services:** 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 