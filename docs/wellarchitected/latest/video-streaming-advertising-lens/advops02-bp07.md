

# ADVOPS02-BP07 Implement observability for bot and agent traffic in AI content licensing
<a name="advops02-bp07"></a>

 AI search agents are reducing direct traffic to publisher sites and cutting ad revenue, while AI-powered bots can generate false impressions that constitute ad tech fraud. You need real-time visibility into bot and agent traffic volumes, classification accuracy, and revenue impact. Automated detection identifies anomalous bot behavior patterns that may indicate ad fraud or unauthorized content crawling. 

 **Desired outcome:** 
+  Publishers have real-time visibility into bot and agent traffic volumes, classification accuracy, and revenue impact. 
+  Bot traffic is classified between legitimate AI agents (licensed crawlers, authorized assistants) and fraudulent bots (impression generators, unauthorized scrapers). 
+  Automated alerting detects anomalous bot traffic patterns within minutes, triggering revenue-protection responses. 

 **Common anti-patterns:** 
+  Not distinguishing between legitimate AI agent traffic and fraudulent bot activity. 
+  Treating bot detection as a binary decision to allow or deny without visibility into the spectrum of bot types and their individual revenue impacts. 
+  Monitoring bot traffic volumes without correlating to ad revenue metrics. 

 **Benefits of establishing this best practice:** 
+  Publishers can distinguish legitimate AI agent traffic from fraudulent bot activity, which protects revenue while maintaining appropriate access for licensed content partners. 
+  Automated detection limits the duration and magnitude of bot-driven revenue impact. 
+  Revenue impact quantification enables data-driven decisions about traffic management policies. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Unlike traditional malicious bot traffic, AI agent traffic runs on a spectrum from legitimate licensed crawlers and authorized AI assistants to fraudulent impression-generating bots and unauthorized content scrapers. 

 At the infrastructure level, AWS Bot Control (a managed rule set within AWS WAF) identifies and manages automated traffic at the network edge using machine learning models trained on bot behavior signatures. It provides classification without requiring application-level changes. For Amazon CloudFront-delivered content, AWS WAF Bot Control on the distribution's web ACL can identify and mitigate unauthorized AI crawling activity, including blocking unverified AI agents and, on CloudFront-attached web ACLs, monetizing AI bot traffic. 

 For ad-tech-specific classification at the impression level (not the request level), use Invalid Traffic (IVT) detection solutions such as Integral Ad Science (IAS), DoubleVerify, or HUMAN. These solutions operate at the ad server or SDK level and use proprietary detection models trained on advertising-specific fraud patterns like click injection, impression stacking, and device emulation. 

 Quantify what fraction of impressions are IVT, the revenue impact of those impressions (both direct CPM loss and potential advertiser trust erosion), and whether the IVT rate is increasing over time. Use Amazon CloudWatch dashboards to correlate bot-to-human traffic ratios with eCPM trends over time. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Deploy AWS Bot Control on advertising-facing endpoints:** Configure AWS WAF with the Bot Control managed rule group on CloudFront distributions and Application Load Balancers serving ad tags, bid endpoints, and content pages. Enable Bot Control in "Count" mode initially to assess traffic composition without blocking, then transition to "Block" mode for bot categories that are definitively fraudulent. Monitor bot traffic metrics in the AWS/WAFV2 CloudWatch namespace. 

1.  **Integrate industry-standard IVT detection at the ad serving layer:** Integrate IAS, DoubleVerify, or HUMAN IVT detection through their respective SDK or API integration patterns at the ad server or publisher ad tag level. Configure IVT classification to categorize traffic as General Invalid Traffic (GIVT) or Sophisticated Invalid Traffic (SIVT) per IAB/MRC standards. Publish IVT rate metrics to CloudWatch as custom metrics with content type and ad format dimensions. 

1.  **Define bot traffic classification taxonomy:** Document the classification hierarchy: Tier 1 (definitively legitimate: licensed AI content partners with verified tokens), Tier 2 (likely legitimate: known search engine crawlers, verified bots from public IP lists), Tier 3 (ambiguous: unknown automated traffic requiring further analysis), Tier 4 (definitively fraudulent: known IVT signatures, bot farm IP ranges). Configure routing rules at each tier level. 

1.  **Build bot traffic observability dashboards correlating traffic with revenue impact:** Create CloudWatch dashboards showing bot-to-human traffic ratio, IVT rate by classification tier, estimated revenue impact of IVT impressions (IVT impression count × average CPM), and trend lines over 30/60/90-day windows. Publish these dashboards to both engineering and ad operations teams. Include bot traffic KPIs in the weekly yield review meeting agenda. 

1.  **Configure automated alerting for anomalous bot volume and new signatures:** Set CloudWatch alarms on bot traffic volume anomalies (using Anomaly Detection to account for natural variation) and on detection of new unclassified bot signatures (a spike in Tier 3 ambiguous traffic). Route alerts to the ad fraud response workflow. Configure monthly traffic policy reviews where engineering and ad operations jointly evaluate bot traffic patterns and update classification rules. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [AWS Bot Control documentation](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-bot.html) 
+  [Amazon CloudFront security features](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/security.html) 

 **Related services:** 
+  [AWS WAF](https://aws.amazon.com/waf/) 
+  [Amazon CloudFront](https://aws.amazon.com/cloudfront/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 