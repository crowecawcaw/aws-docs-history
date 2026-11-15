

# ADVREL01-BP05 Through your CI/CD pipeline, implement regression, performance, and canary tests
<a name="advrel01-bp05"></a>

 Integrate holistic regression, performance, and canary tests into your CI/CD pipeline for advertising workloads. Monitor 5xx errors and latency in RTB systems, and roll back quickly when they breach thresholds. 

 **Desired outcome:** 
+  All production changes pass automated regression, performance, and canary tests before reaching production. 
+  Performance tests compare against established SLO baselines so latency regressions are caught before production deployment. 
+  Automated rollback is triggered when error rates or latency metrics breach thresholds during deployment. 

 **Common anti-patterns:** 
+  Deploying changes straight to 100% of bid traffic without a canary phase to catch regressions. 
+  Running functional tests only, with no performance test comparing bid latency against an SLO baseline. 
+  Relying on manual rollback decisions instead of automated triggers on 5xx error rate or latency breach. 
+  No bid response schema/regression validation, so malformed OpenRTB responses reach production undetected. 

 **Benefits of establishing this best practice:** 
+  Regressions in latency or bid response correctness are caught before reaching full auction volume. 
+  Canary deployments limit the exposure of a flawed change to a small traffic slice. 
+  Automated rollback minimizes the duration of any deployment-induced impact on monetization. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 For RTB availability, the primary reliability metrics are 5xx internal errors and elevated latency. When either breaches its threshold, fail fast and revert the change immediately, then diagnose the root cause afterward. 

 Auction-path failures often produce no 5xx error. A defect in bid construction or price logic can make the system stop winning auctions it should have won. The loss appears as a revenue trend hours later, with no alarm to signal it. Cover bid response semantics (such as schema, pricing bounds, and creative references) in your regression tests. Verify each deployment against more than error rates. No staging environment reproduces the production mix of partners, deal types, and traffic composition that determines bid behavior. Pre-production load tests confirm throughput. Only live traffic confirms bid correctness, so promote new versions through a canary. 

 Size the canary slice large enough that tail-latency and error-rate samples separate a regression from auction noise, and small enough that a bad change stays bounded. Automate rollback authority so that at auction timescales, the deployment system must revert on breached thresholds without waiting for a human decision. Infrastructure signals respond fastest. Business signals such as fill rate and win rate lag and carry noise. Pair infrastructure and business signals in your rollback criteria. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Add bid latency performance tests to CI/CD:** Create a performance test stage in your pipeline that runs a simulated RTB auction load test (5,000 bid requests/second for 10 minutes) against a staging environment. Compare measured p99 bid response latency against the production baseline. Fail the pipeline if latency exceeds baseline by more than 5%. 

1.  **Configure canary deployments for auction services:** Use AWS CodeDeploy with a canary deployment configuration that routes 5% of production bid traffic to the new version for 10 minutes before expanding. Configure automatic rollback to trigger when CloudWatch alarm BidResponseP99Latency exceeds threshold or 5xxErrorRate exceeds 0.1% during the canary phase. 

1.  **Implement regression tests for bid response format validation:** Add automated tests that validate bid response schema compliance (OpenRTB format), required field presence, price validation (no negative or unreasonably high bids), and creative asset URL validity. Run these tests against every build to catch regressions in bid response construction logic. 

1.  **Use FIS to test deployment resilience:** Create FIS experiments that inject failures during deployments (CPU stress on new instances, network latency injection) to validate that the deployment process remains stable under stress. Run these experiments in staging during every major release cycle. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL01-BP06 Deploy new code or resources in staggered phases, separated by sufficient time, to verify that the changes are successful](advrel01-bp06.md) 
+  [ADVREL01-BP04 Implement chaos engineering practices](advrel01-bp04.md) 

 **Related documents:** 
+  [Canary deployments](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html) 
+  [Use CloudWatch Synthetics to Monitor Sites, API Endpoints, Web Workflows, and More](https://aws.amazon.com/blogs/aws/new-use-cloudwatch-synthetics-to-monitor-sites-api-endpoints-web-workflows-and-more/) 

 **Related services:** 
+  [AWS CodePipeline](https://aws.amazon.com/codepipeline/) 
+  [AWS CodeDeploy](https://aws.amazon.com/codedeploy/) 
+  [AWS Fault Injection Service](https://aws.amazon.com/fis/) 