

# DSSEC04-BP01 Enhance threat detection through targeted intelligence
<a name="dssec04-bp01"></a>

 By using region- and domain-specific threat intelligence, organizations can enhance their detection capabilities. With this targeted approach, security teams can contextualize threats within their specific regulatory and infrastructure environment. 

 **Desired outcome:** 
+  Security teams detect threats using jurisdiction-specific and domain-relevant threat intelligence that maps to the organizational risk profile. 

 **Common anti-patterns:** 
+  Relying solely on internally derived threat assessments. 
+  Lack of clear strategy for selecting, using, and governing cyber threat intelligence (CTI) information. This leads to under-performing threat detection capabilities. 
+  Failing to prioritize threat intelligence sources that focus on adversaries and attack patterns specific to a jurisdiction or regulatory environment. 
+  Implementing generic threat indicators without mapping them to your specific infrastructure, data classification levels, or compliance requirements. 

 **Benefits of establishing this best practice:** 
+  Improved detection capabilities by shifting from reactive to proactive threat detection. 
+  Improved early warning capabilities by focusing on specific Indicators of Compromise (IoCs) and configuration of defenses against prioritized tactics, techniques, and procedures (TTPs). 
+  Provides security analysts with contextual information about adversary behaviors and campaign patterns, enabling more targeted investigations. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 [Cyber threat intelligence (CTI)](https://docs.aws.amazon.com/prescriptive-guidance/latest/cyber-threat-intelligence-sharing/introduction.html) is evidence-based, actionable data about a threat actor's intent, opportunity, and capability. What makes it useful for a sovereign workload is relevance. The adversaries and campaigns that matter differ by sector and jurisdiction, and a broad global feed can under-represent them. Review the threat intelligence expectations in the standards and frameworks that apply to you, then prioritize sources that reflect the jurisdictions you operate in. National cybersecurity authorities (such as [NCSC](https://www.ncsc.gov.uk/), [ACSC](https://www.cyber.gov.au/), [ANSSI](https://cyber.gouv.fr/), and [CISA](https://www.cisa.gov/)) and sector-specific Information Sharing and Analysis Centers (ISACs) publish intelligence that carries locally authoritative context. 

 CTI runs as a lifecycle from collection through analysis, automation, and sharing. Two points matter most for a sovereign workload. First, sharing has a jurisdictional dimension. Standards such as the [Trusted Automated Exchange of Intelligence Information (TAXII)](https://oasis-open.github.io/cti-documentation/taxii/intro.html) and the [Malware Information Sharing Platform (MISP)](https://www.misp-project.org/) structure the exchange, but confirm what your organization is permitted to share, and with whom, before joining a trust community. Second, relevance and freshness determine value. Unvetted or stale indicators create false positives that bury real detections, so treat source selection as an ongoing decision rather than a one-time subscription. The steps below cover selecting sources, using AWS detection services, and measuring each source's accuracy and efficacy. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Select CTI sources and services**: Organizations have access to a diverse range of CTI services. Carefully evaluate which services match your requirements and risk profile. Threat intelligence provides information about potential cybersecurity threats from adversaries, enabling proactive defense strategies. Organizations typically share this intelligence in the following formats: 
   +  Indicators of compromise (IoCs) 
   +  Tactics, techniques, and procedures (TTPs) 
   +  High-level contextual information about potential threats. This includes targeted organizations, adversary motivations, geographic origins, and threat actor affiliations. Security leaders often share this type of information within trusted, sector-specific communities. 

    CTI services are available through both commercial vendors offering premium features and open source solutions providing free access to threat data. Assess your needs, budget constraints, and capabilities when selecting CTI services. 

    Validate open source threat intelligence sources before integration. Unvetted sources can contain false positives, outdated indicators, or even malicious data designed to trigger false alerts. Prefer AWS services (GuardDuty) and established commercial vendors with service-level agreements (SLAs). 

1.  **Consider AWS services for threat detection**: [Amazon GuardDuty](https://aws.amazon.com/guardduty/features/) is a threat detection service that protects AWS workloads. The service actively monitors your AWS account activities and alerts you to potential security threats. You can enable GuardDuty with no additional infrastructure or setup. 

    AWS has extensive visibility into internet-wide threat patterns. This extensive reach enables AWS to detect, analyze, and block sophisticated attack techniques from various threat actors. For a detailed example of the AWS threat detection capabilities in action, see [How AWS disrupts watering hole campaign by APT29](https://aws.amazon.com/blogs/security/amazon-disrupts-watering-hole-campaign-by-russias-apt29/). 

1.  **Integrate national cybersecurity authority threat intelligence**: Supplement commercial CTI with jurisdiction-specific intelligence from national authorities and, for regulated industries, from sector-specific ISACs. Many authorities and ISACs distribute machine-readable feeds using STIX over TAXII or MISP. For example, CISA [Automated Indicator Sharing (AIS)](https://www.cisa.gov/how-automated-indicator-sharing-ais-works) exchanges indicators as STIX over a TAXII server. Confirm the membership or subscription requirements for each source, then ingest the feeds through the path described in step 4. 

1.  **Integrate and operationalize**: To deploy your own CTI solution, refer to this [AWS Prescriptive Guidance](https://docs.aws.amazon.com/pdfs/prescriptive-guidance/latest/cyber-threat-intelligence-sharing/cyber-threat-intelligence-sharing.pdf). The guide covers solution deployment, architecture patterns, and intelligence sharing best practices. Operationalize CTI capabilities across the organization, encompassing the following key components: 
   +  **Intelligence management:** Define standardized protocols for collecting, analyzing, and disseminating threat intelligence data. Establish clear roles, responsibilities, and authorization levels for security operations personnel. 
   +  **Technology integration:** Integrate automated CTI feeds into existing security infrastructure, including protective and detective controls. For example, integrate threat intelligence with security information and event management (SIEM) solutions for real-time IoC detection. 
   +  **Quality assurance and governance**: Establish a governance framework to evaluate threat intelligence source accuracy, timeliness, and relevance. Implement regular reviews to assess CTI effectiveness and adjust sources accordingly. 

    An example integration approach: 
   +  Subscribe to threat feeds from relevant national authorities 
   +  Ingest feeds into Amazon Security Lake or SIEM solution 
   +  Correlate national threat intelligence with Amazon GuardDuty findings 
   +  Prioritize threats based on jurisdiction-specific risk profile 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC01-BP04 Stay up to date with security threats and recommendations](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_securely_operate_updated_threats.html) 
+  [SEC01-BP07 Identify threats and prioritize mitigations using a threat model](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_securely_operate_threat_model.html) 
+  [SEC05-BP03 Implement inspection-based protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_network_protection_inspection.html) 
+  [SEC04-BP03 Correlate and enrich security alerts](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_security_alerts.html) 
+  [OPS01-BP04 Evaluate compliance requirements](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_priorities_compliance_reqs.html) 
+  [OPS01-BP05 Evaluate threat landscape](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_priorities_eval_threat_landscape.html) 

 **Related documents:** 
+  [AWS Prescriptive Guidance, Cyber Threat Intelligence Sharing on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/cyber-threat-intelligence-sharing/introduction.html) 
+  [Improve your security posture using Amazon threat intelligence on AWS Network Firewall](https://aws.amazon.com/blogs/security/improve-your-security-posture-using-amazon-threat-intelligence-on-aws-network-firewall/) 
+  [How AWS tracks the cloud's biggest security threats and helps shut them down](https://aws.amazon.com/blogs/security/how-aws-tracks-the-clouds-biggest-security-threats-and-helps-shut-them-down/#:~:text=Organizations%20around%20the%20world%20trust,%2C%20partners%2C%20and%20other%20organizations.) 
+  [Meet MadPot, a threat intelligence tool Amazon uses to protect customers from cybercrime](https://www.aboutamazon.com/news/aws/amazon-madpot-stops-cybersecurity-crime) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Protecting Your Infrastructure with Amazon Threat Intelligence (SEC311)](https://www.youtube.com/watch?v=pbFLIYPsjqY) 

 **Related services:** 
+  [Amazon GuardDuty](https://aws.amazon.com/guardduty/) 
+  [Amazon Security Lake](https://aws.amazon.com/security-lake/) 
+  [AWS Network Firewall](https://aws.amazon.com/network-firewall/) 
+  [AWS WAF](https://aws.amazon.com/waf/) 