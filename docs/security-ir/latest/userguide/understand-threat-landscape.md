# Understand the threat landscape

## Develop threat models

By developing threat models, organizations can identify threats and mitigations
before an unauthorized user can. There are a number of strategies and approaches to threat
modeling; refer to the [How to
approach threat modeling](https://aws.amazon.com/blogs/security/how-to-approach-threat-modeling/ "https://aws.amazon.com/blogs/security/how-to-approach-threat-modeling/") blog post. For incident response, a threat model can
help identify the attack vectors a threat actor might have used during an incident.
Understanding what you’re defending against will be crucial in order to respond in a
timely manner. You can also use an AWS Partner for threat modeling. To search for an AWS
partner, use the [AWS Partner Network](https://partners.amazonaws.com/ "https://partners.amazonaws.com/").

## Integrate and use cyber

threat intelligence

Cyber threat intelligence is the data and analysis of a threat actor’s intent,
opportunity, and capability. Obtaining and using threat intelligence is helpful to detect
an incident early and to better understand threat actor behavior. Cyber threat
intelligence includes static indicators like IP addresses or file hashes of malware. It
also includes high-level information, like behavioral patterns and intent. You can collect
threat intelligence from a number of cyber security vendors and from open-source
repositories.

To integrate and maximize threat intelligence for your AWS environment, you can use
some out-of-the-box capabilities and integrate your own threat intelligence lists.
Amazon GuardDuty uses AWS internal and third-party threat intelligence sources. Other AWS
services, such as a DNS firewall and AWS WAF rules, also take inputs from AWS' advanced
threat intelligence group. Some GuardDuty findings are mapped to the [MITRE ATT&CK Framework](https://attack.mitre.org/ "https://attack.mitre.org/"), which provides
information on real-world observations on adversary tactics and techniques.
