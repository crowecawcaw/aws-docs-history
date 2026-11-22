

# ADVOPS03-BP01 Mitigate deployment risks for publisher workload changes

 Controlled deployment mechanisms help publishers reduce the risk of deploying changes to Prebid adapter configurations, SGAI manifest generation logic, FAST channel schedules, and ad format rendering code. These mechanisms limit the scope of impact of bad deployments and enable rapid rollback. 

 **Desired outcome:** 
+  All publisher workload changes are deployed through controlled mechanisms (canary, blue/green, staged rollout) that limit the scope of impact and enable rapid rollback. 
+  Automated rollback triggers activate when composite alarm thresholds are breached during deployment. 
+  Rollback procedures are validated through periodic dry-run exercises, confirming that traffic reverts to the previous configuration within defined time targets. 

 **Common anti-patterns:** 
+  Deploying Prebid adapter updates directly to all auction traffic without canary testing. 
+  Modifying SGAI manifest generation logic without blue/green deployment. Manifest errors propagate through CDN caching layers and affect all viewers until the cache expires. 
+  Lacking automated rollback triggers for publisher workload changes, requiring manual detection and intervention that extends the duration of the impact. 

 **Benefits of establishing this best practice:** 
+  Reduced scope of impact for faulty deployments. 
+  Faster recovery from undesired changes. 
+  Maintained revenue continuity during updates through pre-validated rollback procedures. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Publisher ad tech infrastructure is a critical part of advertising revenue. A faulty Prebid adapter update that misconfigures timeout parameters can immediately reduce bid density by 30–50%, which degrades CPM and fill rate within minutes. A manifest generation change that introduces a SCTE-35 marker formatting error can break ad break detection for every FAST channel viewer at once. 

 How a change propagates decides which deployment strategy fits it. Some changes affect only the requests that pass through them. Exposure is proportional to the traffic fraction routed to them, and a small fraction means a small risk. Others are cached downstream, which breaks that proportionality. Once a bad artifact reaches downstream caches, every viewer holding it is affected regardless of how little traffic produced it. Exposure persists until the cache expires, not until you stop the rollout. Others are scheduled, so the effect happens at a future moment. What matters is whether you have time to correct the change before that moment arrives. 

 Detectability matters as much as exposure. You can only roll out a change incrementally if its failure becomes visible within the validation window at the traffic fraction you use. Yield metrics are noisy at small fractions. A canary can be too small to distinguish a real regression from normal variance, which produces a confident pass on a broken change. Statistical noise imposes minimums on both the canary fraction and the validation window. 

 Rollback speed determines whether incremental deployment helps. Reversing a routing decision is close to instantaneous. Reversing something already distributed to caches is slower and only partly within your control. A CDN invalidation clears edge caches but does nothing to copies already held by viewer browsers or corporate proxies, which expire on their own schedule. Publishing under a new path avoids the problem, because a different URL cannot return a stale object. The slowest cache in the chain bounds mean time to recovery, not the deployment tool. Scheduled changes are the extreme case. Once the moment passes, there is nothing left to roll back to. Which case a change falls into determines whether pre-activation validation is optional or your only control. 

 Automated rollback is worth more than a human watching a dashboard, but it has its own risks. A trigger tied to a single noisy signal fires on normal variation and rolls back healthy deployments. After a few false rollbacks, the team turns it off. To keep the trigger credible enough to leave armed, require corroboration between a business symptom and a technical cause. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define deployment strategies per workload type:** Document the deployment strategy for each publisher workload change category: canary (1–5% initial traffic, 30-minute validation) for Prebid adapter configuration changes, blue/green with pre-distribution SCTE-35 validation for SGAI manifest generation logic, staged rollout with 60-minute pre-validation for FAST channel schedule changes, and standard canary for innovative ad format rendering code. 

1.  **Establish baseline metrics and rollback trigger thresholds:** For each workload type, define the metrics and thresholds that trigger automated rollback: Prebid (per-adapter bid response rate drops >20% from baseline, or p99 latency exceeds 90% of configured timeout), SGAI (SCTE-35 validation failure rate exceeds 1%, or ad break completion rate drops >10% from baseline), FAST channel (content gap detection triggers, or ad pod fill rate drops >15%). 

1.  **Configure composite alarms as automated rollback triggers:** Create CloudWatch Composite Alarms that combine multiple health indicators into a single rollback trigger. A composite alarm that fires when (SGAI manifest error rate alarm) AND (CDN cache hit rate decline alarm) fire simultaneously provides higher-confidence rollback signal than either alarm alone. Configure these composite alarms as rollback triggers in AWS CodeDeploy deployment configurations. 

1.  **Implement automated rollback procedures in AWS CodeDeploy:** Configure CodeDeploy deployment configurations to activate rollback automatically when composite alarm thresholds are breached. For SGAI deployments, include an automated CDN cache purge in the rollback procedure to remove cached manifests generated by the faulty version. Test the complete rollback procedure in staging before enabling it for production. 

1.  **Validate rollback procedures through periodic dry-run exercises:** Schedule quarterly rollback dry-run exercises where the on-call team executes a simulated rollback for each publisher workload type. Measure the time from rollback trigger to traffic fully reverted. Set a target of under 5 minutes for Prebid adapter rollbacks and under 10 minutes for SGAI blue/green rollbacks. Document the results and update rollback procedures when targets are not met. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVOPS03-BP02 Establish operational readiness reviews for publisher launches](advops03-bp02.md) 
+  [ADVOPS04-BP02 Automate runbooks to gain operational efficiency](advops04-bp02.md) 

 **Related documents:** 
+  [AWS CodeDeploy deployment configurations documentation](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html) 
+  [Amazon CloudWatch composite alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Composite_Alarm.html) 
+  [Invalidate files to remove content from a CloudFront edge cache](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html) 

 **Related services:** 
+  [AWS CodeDeploy](https://aws.amazon.com/codedeploy/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 