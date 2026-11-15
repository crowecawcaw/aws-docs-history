

# ADVOPS03-BP04 Establish third-party DSP integration operations for Prebid Server
<a name="advops03-bp04"></a>

 Third-party DSP integrations require dedicated operational management beyond standard adapter onboarding. Each DSP can support different identity frameworks (UID2, LiveRamp, and ID5) with varying signal fidelity. The operational health of these integrations affects bid response rates and publisher yield in a multi-identity-provider environment. 

 **Desired outcome:** 
+  Third-party DSP integrations are operationally validated with standardized identity-signal pass-through monitoring across identity frameworks (UID2, LiveRamp, and ID5). 
+  Per-DSP monitoring tracks bids per auction, win rate, and identity-signal match rate as primary health indicators. 
+  Automated alerting triggers when a DSP's bid response rate drops below historical baselines, enabling rapid detection of identity-signal pass-through failures or integration degradation. 

 **Common anti-patterns:** 
+  Treating DSP integrations as one-time technical setups rather than ongoing operational assets requiring health monitoring and lifecycle management. 
+  Not monitoring identity-signal match rates per DSP. 
+  Lacking DSP-specific runbooks for common integration failure modes, which requires troubleshooting for recurring issues. 

 **Benefits of establishing this best practice:** 
+  Proactive detection of DSP integration failures that reduce bids per auction and eCPM without triggering an alarm. 
+  Faster root cause identification for bid density drops through per-DSP identity-signal visibility. 
+  Structured lifecycle management limiting the accumulation of unmaintained, underperforming DSP integrations. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Identity pass-through for each DSP determines how accurately that DSP can evaluate audience targeting in its bid decisions. A DSP receiving well-formed UID2 tokens bids with more precision and higher CPMs than the same DSP receiving requests with no identity signal. 

 An integration that passes onboarding doesn't stay validated. The DSP evolves its bidding models, endpoint infrastructure, and identity handling on its own release schedule, and few partners announce every change to every publisher they buy from. The production traffic the integration serves keeps shifting as creative formats change, device mixes change, and the identity-signal composition of requests moves with consent rates and identity framework adoption. An adapter that behaved correctly against the traffic it was certified with can misbehave against the traffic it receives six months later, with no deployment on either side to point to. 

 Once live, per-DSP monitoring tracks the operational health metrics most likely to degrade without an obvious signal, such as: 
+  Bids per auction (the primary indicator of demand competition, a drop here reduces eCPM even if fill rate remains stable) 
+  Win rate (declining win rate indicates either budget exhaustion or reduced targeting precision) 
+  Identity-signal match rate (the fraction of bid requests where the DSP's identity resolution succeeds and enriches the bid decision) 

 These integrations are operationally distinct because they degrade without producing an incident. A broken DSP integration removes one bidder from the auction. The auction still clears, fill rate holds, and the loss appears only as softer competition and a lower eCPM that is misread as seasonality or marketplace softness. No alarm fires for revenue that failed to materialize, so these degradations persist for weeks. Recovery depends on people outside your company. The engineers who can fix a partner-side regression work for the DSP and answer to the DSP's priorities. Agree escalation contacts, expected response times, and change-notification expectations across the company boundary before the first incident, not during it. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Create a DSP integration onboarding checklist:** Define required validations for each new DSP integration: identity-signal compatibility testing (send bid requests with UID2, LiveRamp, and ID5 tokens and verify the DSP's bid response demonstrates enriched targeting), bid response format conformance testing (parse all bid responses for required fields and valid formats), and latency threshold verification (confirm p99 response time is within 80% of the configured adapter timeout). Document the test results in the adapter onboarding record. 

1.  **Configure per-DSP monitoring dashboards:** Build CloudWatch dashboards for each DSP integration tracking bids per auction, win rate, eCPM contribution, and identity-signal match rate per identity framework (UID2, LiveRamp, ID5, and no-ID). Use CloudWatch Contributor Insights to visualize per-DSP performance trends over time. Configure daily metric summaries delivered through Quick for ad operations review. 

1.  **Establish automated alerting on historical baselines:** After 2 weeks of production data, configure per-DSP alarms based on individual baselines. Alert when a DSP's bid response rate drops more than 30% below its baseline, when identity-signal match rate drops more than 20% below baseline, or when p99 response latency exceeds 90% of the configured adapter timeout. Use CloudWatch Anomaly Detection for eCPM contribution to detect demand partner degradation that doesn't manifest in binary metrics. 

1.  **Implement quarterly DSP integration health reviews:** Schedule quarterly cross-functional reviews where engineering and ad operations jointly analyze per-DSP performance data. Evaluate: DSPs with declining bid density and the likely causes, identity-signal match rate trends and whether they correlate with industry-wide identity framework adoption patterns, and whether any underperforming DSP integrations should be reconfigured or decommissioned. 

1.  **Document DSP-specific runbooks for common failure modes:** Create runbooks for the three most common DSP integration failure modes: timeout escalation (when to escalate to the DSP's technical support and what information to provide), identity-signal degradation (how to diagnose whether the issue is in the adapter configuration, the DSP's integration, or the identity provider), and bid format validation errors (how to capture malformed bid responses and report them to the DSP's integration team). Store runbooks in the same version-controlled repository as adapter configurations. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVOPS02-BP08 Monitor server-side auction health and demand partner yield across your header bidding infrastructure](advops02-bp08.md) 

 **Related documents:** 
+  [Prebid Server deployment guidance on AWS](https://aws.amazon.com/solutions/implementations/prebid-server-deployment-on-aws/) 
+  [UID2, LiveRamp, and ID5 integration specifications](https://unifiedid.com/docs/intro) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Quick](https://aws.amazon.com/quicksight/) 