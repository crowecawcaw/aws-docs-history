# DSSEC04-BP01 Enhance threat detection through targeted

intelligence

By using region and domain-specific threat intelligence,
organizations can enhance their detection capabilities. This
targeted approach allows security teams to contextualize threats
within their specific regulatory and infrastructure environment.

**Desired outcome:** Achieve enhanced
threat detection through contextually relevant threat intelligence
that aligns with organizational risk profile and regulatory
requirements.

**Common anti-patterns:**

- Relying solely on internally derived threat assessments.
- Lack of clear strategy for selecting, using, and governing cyber
  threat intelligence (CTI) information. This leads to
  under-performing threat detection capabilities.
- Failing to prioritize threat intelligence sources that focus on
  adversaries and attack patterns specific to a geographic region
  or regulatory environment.
- Implementing generic threat indicators without mapping them to
  your specific infrastructure, data classification levels, or
  compliance requirements.
- Failing to consider data residency and sovereignty requirements
  when sharing threat intelligence information. This leads to
  inadvertently transferring sensitive security data outside
  approved jurisdictions.

**Benefits of establishing this best
practice:**

- Improved detection capabilities by shifting from reactive to
  proactive threat detection.
- Improved early warning capabilities by focusing on specific
  Indicator of Compromise (IoC) and configuration of defenses
  against prioritized tactics, techniques, and procedures (TTPs).
- Provides security analysts with contextual information about
  adversary behaviors and campaign patterns, enabling more
  targeted investigations.
- Facilitates information sharing with industry peers, government
  agencies, and security communities, creating collective defense
  benefits while maintaining regulatory adherence.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Review the guidelines around threat intelligence included in the
applicable standards and compliance frameworks that are relevant
to the organization. Evaluate available resources from cloud
service providers, local cybersecurity authorities (such as
[NCSC](https://www.ncsc.gov.uk/ "https://www.ncsc.gov.uk/"),
[ACSC](https://www.cyber.gov.au/ "https://www.cyber.gov.au/"),
[ANSSI](https://cyber.gouv.fr/ "https://cyber.gouv.fr/"), and
[CISA](https://www.cisa.gov/ "https://www.cisa.gov/")), and third
parties through the AWS Marketplace.

Develop supporting processes and capabilities to make sure CTI
effectively improves threat detection and incident response
performance. Implement monitoring and review of CTI impact on
threat detection capabilities. Verify CTI provides relevant
information with good accuracy and efficacy.

### Implementation steps

1. **Select CTI sources and
   services**: Organizations have access to a diverse
   range of CTI services. You must carefully evaluate which
   services align with your requirements and risk profile.
   Threat intelligence provides information about potential
   cybersecurity threats from adversaries, enabling proactive
   defense strategies. Organizations typically share this
   intelligence in the following formats:
   - Indicator of compromise (IoCs)
   - Tactics, techniques, and procedures (TTPs)
   - High-level contextual information about potential
     threats. This includes targeted organizations, adversary
     motivations, geographic origins, and threat actor
     affiliations. Security leaders often share this type of
     information within trusted, sector-specific communities.

CTI services are available through both commercial vendors
offering premium features and open-source solutions
providing free access to threat data. Assess your needs,
budget constraints, and capabilities when selecting CTI
services.

Consider a cloud-based service such as Amazon GuardDuty.
GuardDuty is a threat detection service that protects AWS
workloads. It uses AWS's proprietary and external threat
intelligence sources to safeguard your infrastructure. The
service actively monitors your AWS account activities and
alerts you to potential security threats. You can enable
GuardDuty with no additional infrastructure or setup.

AWS has extensive visibility into internet-wide threat
patterns. This extensive reach enables AWS to detect,
analyze, and block sophisticated attack techniques from
various threat actors. For a detailed example of AWS's
threat detection capabilities in action, see
[How
AWS disrupts watering hole campaign by APT29](https://aws.amazon.com/blogs/security/amazon-disrupts-watering-hole-campaign-by-russias-apt29/ "https://aws.amazon.com/blogs/security/amazon-disrupts-watering-hole-campaign-by-russias-apt29/"). 2. **Integrate and
operationalize**: To deploy your own CTI solution,
refer to this
[AWS Prescriptive Guidance](../../../pdfs/prescriptive-guidance/latest/cyber-threat-intelligence-sharing/cyber-threat-intelligence-sharing.md "../../../pdfs/prescriptive-guidance/latest/cyber-threat-intelligence-sharing/cyber-threat-intelligence-sharing.md"). The guide covers solution
deployment, architecture patterns, and intelligence sharing
best practices. Operationalize CTI capabilities across the
organization, encompassing the following key components:

    * **Intelligence
     management:** Define standardized protocols for
     collecting, analyzing, and disseminating threat
     intelligence data. Establish clear roles,
     responsibilities, and authorization levels for security
     operations personnel.
    * **Technology
     integration:** Integrate automated CTI feeds
     into existing security infrastructure, including
     protective and detective controls. For example,
     integrate threat intelligence with SIEM solutions for
     real-time IoC detection.
    * **Quality assurance and
     governance**: Establish a governance framework
     to evaluate threat intelligence source accuracy,
     timeliness, and relevance. Implement regular reviews to
     assess CTI effectiveness and adjust sources accordingly.

## Resources

**Related best practices:**

- [SEC01-BP04
  Stay up to date with security threats and
  recommendations](../security-pillar/sec_securely_operate_updated_threats.md "../security-pillar/sec_securely_operate_updated_threats.md")
- [SEC05-BP03
  Implement inspection-based protection](../security-pillar/sec_network_protection_inspection.md "../security-pillar/sec_network_protection_inspection.md")
- [OPS01-BP04
  Evaluate compliance requirements](../operational-excellence-pillar/ops_priorities_compliance_reqs.md "../operational-excellence-pillar/ops_priorities_compliance_reqs.md")
- [SEC04-BP03
  Correlate and enrich security alerts](../../../en_us/wellarchitected/latest/security-pillar/sec_detect_investigate_events_security_alerts.md "../../../en_us/wellarchitected/latest/security-pillar/sec_detect_investigate_events_security_alerts.md")

**Related documents:**

- [AWS Prescriptive Guidance, Cyber Threat Intelligence Sharing on
  AWS](../../../prescriptive-guidance/latest/cyber-threat-intelligence-sharing/introduction.md "../../../prescriptive-guidance/latest/cyber-threat-intelligence-sharing/introduction.md")
- [Improve
  your security posture using Amazon threat intelligence on AWS Network Firewall](https://aws.amazon.com/blogs/security/improve-your-security-posture-using-amazon-threat-intelligence-on-aws-network-firewall/ "https://aws.amazon.com/blogs/security/improve-your-security-posture-using-amazon-threat-intelligence-on-aws-network-firewall/")
- [How
  AWS tracks the cloud's biggest security threats and helps shut
  them down](https://aws.amazon.com/blogs/security/how-aws-tracks-the-clouds-biggest-security-threats-and-helps-shut-them-down/#:~:text=Organizations%20around%20the%20world%20trust,%2C%20partners%2C%20and%20other%20organizations. "https://aws.amazon.com/blogs/security/how-aws-tracks-the-clouds-biggest-security-threats-and-helps-shut-them-down/#:~:text=Organizations%20around%20the%20world%20trust,%2C%20partners%2C%20and%20other%20organizations.")
- [Meet
  MadPot, a threat intelligence tool Amazon uses to protect
  customers from cybercrime](https://www.aboutamazon.com/news/aws/amazon-madpot-stops-cybersecurity-crime "https://www.aboutamazon.com/news/aws/amazon-madpot-stops-cybersecurity-crime")

**Related videos:**

- [AWS re:Invent 2025 - Protecting Your Infrastructure with Amazon
  Threat Intelligence (SEC311)](https://www.youtube.com/watch?v=pbFLIYPsjqY "https://www.youtube.com/watch?v=pbFLIYPsjqY")
