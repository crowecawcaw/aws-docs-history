# Viewing the Amazon Inspector score and understanding vulnerability intelligence details

Amazon Inspector creates a score for Amazon Elastic Compute Cloud (Amazon EC2) instance findings.
You can view the Amazon Inspector score and vulnerability intelligence details in the Amazon Inspector console.
The Amazon Inspector score provides you with details that you can compare with metrics in the [Common Vulnerability Scoring System](https://www.first.org/cvss/v3.1/specification-document "https://www.first.org/cvss/v3.1/specification-document").
These details are only available for [package vulnerability](findings-types.md#findings-types-package "findings-types.md#findings-types-package") findings.
This section describes how to interpret the Amazon Inspector score and understand vulnerability intelligence details.

## Amazon Inspector score

Amazon Inspector creates a score for each Amazon EC2 finding.
Amazon Inspector determines the score by correlating CVSS base score information with information from your compute environment, such as network reachability data and exploitability data.
Amazon Inspector supports Amazon, Debian, and RHEL vendors.
Each vendor provides a CVSS v3.1 base score.
For other vendors, Amazon Inspector uses a CVSS base score provided by the [National Vulnerability Database (NVD)](https://nvd.nist.gov/vuln "https://nvd.nist.gov/vuln").

Due to FedRAMP requirements, Amazon Inspector uses the CVSS v3.1 base score as the default score.
However, a [CVSS 4.0](https://www.first.org/cvss/v4-0/specification-document "https://www.first.org/cvss/v4-0/specification-document") base score will be included in your vulnerability metadata when one is available.
The CVSS 4.0 base score provides additional metrics to improve vulnerability assessment.
You can find the source and version of a CVSS base score in the vulnerability details for a finding and in exported findings.

###### Note

The Amazon Inspector score is not available for Linux instances running Ubuntu.
Ubuntu uses a custom severity rating system that differs from CVSS scores.

### Amazon Inspector score

details

When you open the details page of a finding you can select the
**Inspector score and vulnerability intelligence** Tab.
This panel shows the difference between the base score and the
**Inspector score**. This section explains how Amazon Inspector
assigned the severity rating based on a combination of the Amazon Inspector score and the
vendor score for the software package. If the scores differ this panel shows an
explanation of why.

In the **CVSS score metrics** section you can see a table
with comparisons between the CVSS base score metrics and the **Inspector
score**. The metrics compared are the base metrics defined in the
[CVSS
specification document](https://www.first.org/cvss/specification-document "https://www.first.org/cvss/specification-document") maintained by first.org. The
following is a summary of the base metrics:

**Attack Vector**

The context by which a vulnerability can be exploited. For Amazon Inspector
findings this can be Network, **Adjacent**
**Network**, or **Local**.

**Attack Complexity**

This describes the level of difficulty an attacker will face when
exploiting the vulnerability. A **Low** score means
that the attacker will need to meet little or no additional
conditions to exploit the vulnerability. A **High**
score means that an attacker will need invest a considerable amount
of effort in order carry out a successful attack with this
vulnerability.

**Privilege Required**

This describes the level of privilege an attacker will need to
exploit a vulnerability.

**User Interaction**

This metric states if a successful attack using this vulnerability
requires a human user, other than the attacker.

**Scope**

This states whether a vulnerability in one vulnerable component
impacts resources in components beyond the vulnerable component’s
security scope. If this value is **Unchanged** the
affected resource and the impacted resource are the same. If this
value is **Changed** then the vulnerable component
can be exploited to impact resources managed by different security
authorities.

**Confidentiality**

This measures the level of impact to the confidentiality of data
within a resource when the vulnerability is exploited. This ranges
from **None**, where no confidentiality is lost, to
**High** where all information within a
resource is divulged or confidential information such as passwords
or encryption keys can be divulged.

**Integrity**

This measures the level of impact to the integrity of data within
the impacted resource if the vulnerability is exploited. Integrity
is at risk when the attacker to modify files within impacted
resources. The score ranges from **None**, where
the exploit does not allow an attacker to modify any information, to
**High**, where if exploited, the vulnerability
would allow an attacker to modify any or all files, or the files
that could be modified have serious consequences.

**Availability**

This measures the level of impact to the availability of the
impacted resource when the vulnerability is exploited. The score
ranges from **None**, when the vulnerability does
not impact availability at all, to **High**, where
if exploited, the attacker can completely deny availability to the
resource, or cause a service to become unavailable.

## Vulnerability Intelligence

This section summarizes available intelligence about the CVE from Amazon as well
as industry standard security intelligence sources such as Recorded Future, and
Cybersecurity and Infrastructure Security Agency (CISA).

###### Note

Intel from CISA, Amazon, or Recorded Future won't be available for all
CVEs.

You can view vulnerability intelligence details in the console or by using the
[BatchGetFindingDetails](../../v2/APIReference/API_BatchGetFindingDetails.md "../../v2/APIReference/API_BatchGetFindingDetails.md") API. The following details
are available in the console:

**ATT&CK**

This section shows the MITRE tactics, techniques, and procedures
(TTPs) associated with the CVE. The associated TTPs are shown, if there
are more than two applicable TTPs you can select the link to see a
complete list. Selecting a tactic or technique opens information about
it on the MITRE website.

**CISA**

This section covers relevant dates associated with the vulnerability.
The date Cybersecurity and Infrastructure Security Agency (CISA) added
the vulnerability to Known Exploited Vulnerabilities Catalog, based on
evidence of active exploitation, and the Due date CISA expects systems
to be patched by. This information is sourced from CISA.

**Known malware**

This section lists known exploit kits and tools that exploit this
vulnerability.

**Evidence**

This section summarizes the most critical security events involving
this vulnerability. If more than 3 events have the same criticality
level the top three most recent events are displayed.

**Last time reported**

This section shows the Last known public exploit date for this
vulnerability.
