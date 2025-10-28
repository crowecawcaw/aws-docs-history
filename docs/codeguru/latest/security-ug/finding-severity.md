On November 20, 2025, AWS will discontinue support for Amazon CodeGuru Security. After
November 20, 2025, you will no longer be able to access the /codeguru/security console, service
resources, or documentation. For more information, see [End of support for CodeGuru Security](end-of-support.md "end-of-support.md").

# Finding severity

CodeGuru Security defines the severity of the findings detected in your code resources so
you can prioritize what vulnerabilities to remediate and track the security posture of your
application. The following sections explain what methods are used to determine the severity of
findings and what each level of severity means.

## How severity is calculated

The severity of a security vulnerability is determined by the detector that generated the
finding. Detectors in the Amazon CodeGuru Detector Library are each assigned a severity using the
Common Vulnerability Scoring System ([CVSS](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator "https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator")). The CVSS considers
how the finding can be exploited in its context (for example, can it be done over internet, or
is physical access required) and what level of access can be obtained.

The following table outlines how severity is determined based on the level of access and
level of effort required for a bad actor to successfully attack a system.

|                                      | Level of Effort |
| ------------------------------------ | --------------- | ------------------------- | ---------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                      | Not exploitable | Requires access to system | Internet with high LoE | Over internet |
| **Level of access**                  |                 |                           |                        |               |
| Full control of system or its output | N/A             | High                      | Critical               | Critical      |
| Access to sensitive information      | N/A             | Medium                    | High                   | High          |
| Can crash or slow down the system    | Low             | Low                       | Medium                 | Medium        |
| Provides additional security         | Info            | Info                      | Low                    | Low           |
| Best practice                        | Info            | N/A                       | N/A                    | N/A           | ## Severity definitions The severity levels are defined as follows. **Critical – The security vulnerability should be remediated immediately to avoid it escalating.** Critical findings suggest that an attacker can gain control of the system or modify its behavior with moderate effort. CodeGuru Security recommends that you treat critical findings with the utmost urgency. You also should consider the criticality of the resource. **High – The security vulnerability must be addressed as a near-term priority.** High severity findings suggest that an attacker can gain control of the system or modify its behavior with high effort. CodeGuru Security recommends that you treat a high severity finding as a near-term priority and that you take immediate remediation steps. You also should consider the criticality of the resource. **Medium – The security vulnerability should be addressed as a midterm priority.** Medium severity findings can lead to crash, unresponsiveness, or unavailability of the system. CodeGuru Security recommends that you investigate the implicated code at your earliest convenience. You also should consider the criticality of the resource. **Low – The security vulnerability does not require action on its own.** Low severity findings suggest programming errors or anti-patterns. You do not need to take immediate action on low severity findings, but they can provide context when you correlate them with other issues. **Informational – No recommended action.** Informational findings include suggestions for quality or readability improvements, or alternative API operations. No immediate action is necessary. |
