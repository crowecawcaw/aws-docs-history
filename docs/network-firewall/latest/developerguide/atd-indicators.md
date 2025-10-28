# Understanding active threat defense managed rule group indicators

A threat indicator is a unique identifier of potentially malicious infrastructure or threat
activity. active threat defense managed rule groups match traffic for IP address, domain name, and URL indicators that are
associated with known threats.

###### Tip

If you use Amazon GuardDuty, you can strengthen your security by using active threat defense managed rule group to automatically
block the threats that Amazon GuardDuty detects. For information, see [Working with active threat defense indicators in Amazon GuardDuty](nwfw-atd-guardduty-use-case.md "nwfw-atd-guardduty-use-case.md").

AWS groups threat indicators into categories based on observed attack patterns.
The following table describes each indicator group available in the active threat defense managed rule group:

| Indicator group and description                                                                                                                                                          | Traffic direction | Indicator types |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | --------------- |
| **Command and control** Infrastructure that malicious actors use to remotely control compromised systems.                                                                                | Egress            | IPs, domains    |
| **Malware staging** Infrastructure that facilitates the distribution of malware and attack tooling.                                                                                      | Ingress/Egress    | URLs            |
| **Sinkholes** Previously abused infrastructure used for malicious purposes.                                                                                                              | Egress            | Domains         |
| **Out-of-band application security testing** A technique where injected payloads make an outbound connection to external infrastructure that validates the existence of a vulnerability. | Egress            | IPs, domains    |
| **Crypto-mining pool** Infrastructure used by crypto-miners.                                                                                                                             | Egress            | IPs, domains    |
