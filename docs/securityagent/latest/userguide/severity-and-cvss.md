# Severity ratings and CVSS metrics

AWS Security Agent assigns each finding a severity rating, and penetration test findings also include a CVSS (Common Vulnerability Scoring System) metrics breakdown. Use this reference to interpret those values when you review findings.

## Severity levels

Each finding includes a color-coded severity badge that shows its risk level:

- **Critical** (red) – Requires immediate action; exploitation could lead to system compromise
- **High** (red) – Requires prompt attention; exploitation could result in significant security impact
- **Medium** (orange) – Should be addressed in a reasonable timeframe; contributes to overall security risk
- **Low** (yellow) – Can be addressed as part of regular maintenance; minimal immediate risk
- **Informational** (blue) – For informational purposes; minimal to no immediate risk

## CVSS metrics

Penetration test findings include a CVSS metrics breakdown in the finding’s **Risk Reasoning** section. These metrics explain how AWS Security Agent calculated the severity and help you assess the true risk:

- **Attack Vector** (Network, Adjacent, Local, or Physical) – How remotely the attack can be executed
- **Attack Complexity** (Low or High) – Whether specialized conditions are required to exploit the vulnerability
- **Privileges Required** (None, Low, or High) – The access level an attacker needs
- **User Interaction** (None or Required) – Whether the exploit needs user involvement
- **Scope** – Whether the vulnerability affects components beyond the vulnerable one
- **Confidentiality, Integrity, and Availability impact** (None, Low, or High) – The impact on your system’s security

###### Important

Findings with a Network attack vector, Low attack complexity, and High confidentiality or integrity impact represent the most dangerous vulnerabilities and require immediate attention.
