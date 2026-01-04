# TELSEC03-BP02 Deploy signaling firewall on the roaming and

interconnecting interfaces with other telco networks

The Global System for Mobile Communications Association (GSMA) recommends deploying
signaling firewalls on the roaming and interconnecting interfaces with other telco networks.
This best practice is aimed at protecting the telco network from potential signaling-based
attacks and maintaining the overall security and integrity of the network.

The signaling firewall acts as a gatekeeper, monitoring and filtering the signaling
traffic exchanged between the telco network and its roaming partners or interconnected
networks. By implementing a signaling firewall, organizations can effectively mitigate the
risk of unauthorized access, signaling storms, and other signaling-related security threats,
thereby enhancing the resilience and reliability of the network.

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance

Catalog and understand the network topology and signaling traffic across each
identified interface. Deploy a signaling firewall solution capable of deep packet
inspection, protocol validation, and anomaly detection, aligned with the organization's
security policies. Integrate the signaling firewall with comprehensive logging,
monitoring, and centralized security analysis capabilities. Configure the firewall to
inspect and filter signaling traffic, implementing protocol-specific rules to detect and
block unauthorized or malicious activities. Establish robust monitoring and incident
response procedures, integrating the firewall logs with advanced security analytics
tools. Regularly review and update the signaling firewall's configuration, rulesets, and
software versions to maintain effectiveness against evolving threats, leveraging
automated maintenance and validation processes.

### Implementation steps

- Identify roaming and interconnection interfaces:
  - Catalog the roaming and interconnection interfaces within the
    telco network, including the protocols and signaling traffic
    exchanged.
  - Understand the network topology and the flow of signaling traffic
    across the identified interfaces.

- Deploy signaling firewall solution:
  - Select a signaling firewall solution that is compatible with the
    identified protocols and interfaces within the telco network.
  - Configure the signaling firewall to align with the organization's
    security policies and best practices.

- Integrate signaling firewall with AWS services:
  - Integrate the signaling firewall with Amazon CloudWatch for comprehensive
    logging and monitoring of signaling traffic and security events.
  - Utilize AWS Security Hub CSPM to centralize the security findings from the
    signaling firewall and other security services, enabling holistic
    security analysis and incident response.

- Signaling traffic inspection and filtering:
  - Configure the signaling firewall to inspect incoming and outgoing
    signaling traffic, validating the integrity and authenticity of the
    signaling messages.
  - Implement signaling protocol-specific rules and policies to
    detect and block unauthorized or malicious signaling activities,
    such as signaling storms, fraud attempts, and network element
    impersonation.
  - Regularly update the signaling firewall's rulesets and signatures
    to address evolving signaling-based threats and vulnerabilities.

- Signaling firewall monitoring and incident response:
  - Establish robust monitoring and alerting mechanisms to detect and
    respond to anomalies or security incidents related to the signaling
    traffic.
  - Integrate the signaling firewall logs with Amazon CloudWatch and Amazon OpenSearch Service
    for advanced security analysis and threat hunting.
  - Develop and test incident response procedures to mitigate the
    impact of signaling-based attacks or network disruptions.

- Signaling firewall maintenance and updates:
  - Regularly review and update the signaling firewall's
    configuration, rulesets, and software versions to verify it remains
    effective against the latest security threats.
  - Leverage AWS Systems Manager for automated patching and updates of the
    signaling firewall infrastructure.
  - Conduct periodic testing and validation of the signaling
    firewall's functionality and security posture.
