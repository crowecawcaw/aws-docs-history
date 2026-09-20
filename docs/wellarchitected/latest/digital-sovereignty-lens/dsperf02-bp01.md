

# DSPERF02-BP01 Validate third-party software components for sovereignty compliance
<a name="dsperf02-bp01"></a>

 Third-party software components (open source libraries, commercial SDKs, and proprietary middleware) can introduce sovereignty risks that standard security scanning doesn't detect. Licensing restrictions, supply chain provenance, runtime behavior, and jurisdiction-specific certification requirements each affect whether a component is suitable for use in a regulated environment. 

 **Desired outcome:** 
+  You have sovereignty-specific validation criteria defined for third-party software components, covering licensing compatibility, supply chain provenance, data handling behavior, and jurisdiction-specific certifications. 
+  Your validation process is layered on top of existing security scanning, not a replacement for it. 
+  You have documented compensating controls for components that can't meet certification requirements. 
+  Your critical third-party dependencies have contingency plans for abandonment, licensing changes, or vendor disruption. 

 **Common anti-patterns:** 
+  Validating third-party components only for security vulnerabilities without assessing licensing obligations or supply chain provenance. 
+  Depending on software maintained or sold by a single vendor in a single jurisdiction without assessing continuity risk. 
+  Overlooking licensing terms that might be incompatible with sovereignty mandates, such as copyleft disclosure requirements or restrictive commercial EULAs. 

 **Benefits of establishing this best practice:** 
+  Reduced risk of operational disruption from licensing changes, vendor acquisitions, or trade restrictions affecting critical software dependencies. 
+  Demonstrated due diligence through documented sovereignty-specific validation of all third-party software, not only open source. 
+  Greater confidence in the continuity of critical dependencies through provenance assessment and contingency planning. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Standard vulnerability scanning and dependency auditing (for example, with [Amazon Inspector](https://aws.amazon.com/inspector/)) assess whether a component contains known exploitable flaws. Sovereignty validation assesses whether a component can be used in a regulated environment given the jurisdiction's licensing restrictions, certification mandates, and data handling rules. 

 Match the depth of sovereignty assessment to the component's exposure and criticality. A permissive-licensed logging library with broad maintainer diversity carries minimal continuity risk. A proprietary cryptographic SDK from a vendor subject to foreign export controls, or an open source library maintained by a small group in a single jurisdiction, each carry substantially greater continuity risks. Components that handle regulated data, make network calls, or sit in the critical path of a sovereign workload warrant full assessment. Lower-exposure components might need only a lightweight licensing and provenance check. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Validate licensing compatibility with sovereignty mandates:** Review the license terms of each third-party component for potential incompatibilities with sovereignty requirements. For open source, assess copyleft provisions (for example, AGPL) that could create unintended disclosure obligations. For proprietary software, assess EULA clauses that restrict usage in specific jurisdictions or impose export controls. Document the license of each component and assess compatibility with your regulatory obligations. For commercial components, use [AWS License Manager](https://aws.amazon.com/license-manager/) to track entitlements and enforce license usage rules. 

1.  **Assess supply chain provenance and concentration risk:** For each critical dependency, document where the software is developed and maintained, who the primary contributors or vendor entities are, and whether there is concentration risk in a single jurisdiction. For open source, prefer components backed by foundations with established governance structures (for example, Apache Software Foundation, Cloud Native Computing Foundation). 

1.  **Verify jurisdiction-specific certification requirements:** Some jurisdictions require software components used in critical infrastructure to hold specific certifications. Verify whether each component (open source or proprietary) can meet these requirements. 

1.  **Validate data handling and telemetry behavior:** Review whether third-party components send telemetry, connect to external services, or make outbound network calls. For open source, inspect the source code and test in an isolated environment. For proprietary components where source is unavailable, review vendor documentation, contractual data processing addendums, and use network monitoring to observe actual behavior. Consider using [AWS Network Firewall](https://aws.amazon.com/network-firewall/) to monitor outbound traffic from workloads that include third-party components. 

1.  **Plan for continuity of critical dependencies:** For third-party components critical to sovereign workloads, develop contingency plans for project abandonment (open source), vendor acquisition, licensing disputes, or trade restrictions. Evaluate whether alternative components exist that could be substituted. Document the estimated effort and timeline to switch. Integrate this assessment with the vendor concentration risk evaluation in [DSREL04-BP01 Plan for disruptions beyond technical failures](dsrel04-bp01.html). 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC06-BP01 Perform vulnerability management](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_compute_vulnerability_management.html) 
+  [DSREL03-BP01 Design workloads for greater interoperability and portability](dsrel03-bp01.html) 
+  [DSREL04-BP01 Plan for disruptions beyond technical failures](dsrel04-bp01.html) 

 **Related documents:** 
+  [[QA.ST.6] Validate third-party components using software composition analysis](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.st.6-validate-third-party-components-using-software-composition-analysis.html) 
+  [US Bureau of Industry and Security - Export Administration Regulations](https://www.bis.gov/regulations/ear) 

 **Related videos:** 
+  [AWS re:Inforce 2023 - Security in the Open: OSS and AWS (SEC201-L)](https://www.youtube.com/watch?v=kMY8gGmWfAI) 

 **Related services:** 
+  [AWS License Manager](https://aws.amazon.com/license-manager/) 
+  [Amazon Inspector](https://aws.amazon.com/inspector/) 
+  [AWS Network Firewall](https://aws.amazon.com/network-firewall/) 