On November 20, 2025, AWS will discontinue support for Amazon CodeGuru Security. After
November 20, 2025, you will no longer be able to access the /codeguru/security console, service
resources, or documentation. For more information, see [End of support for CodeGuru Security](end-of-support.md "end-of-support.md").

# Terminology and metrics

This section provides an overview of the key terminology and metrics in
Amazon CodeGuru Security.

**Age**

The amount of time a finding is open, starting at initial detection.

**Analysis type**

The type of analysis performed in a scan. You can create scans that only detect security
vulnerabilities, or scan for both security and quality defects in your code. For more
information, see [Types of code scans](scan-types.md "scan-types.md").

**Average time to close**

The average amount of time that a finding is open, from initial detection to being
closed, during a particular date range.

**Closed findings**

Previously detected findings that CodeGuru Security no longer identifies as security
vulnerabilities during a subsequent scan because the security vulnerabilities were
remediated.

**Closure rate**

The percentage of findings that were closed during a particular date range. This number
is determined by dividing the number of open findings during the date range by the number of
closed findings for the same period. For example, if 8 out of 10 open findings were closed
during a date range, then the closure rate is 80%.

**Detector**

A defined rule that CodeGuru Security uses to check your code for security vulnerabilities based
on industry standards and AWS best practices. Detectors identify a type security
vulnerability and are used to group findings based on these categorizations of
vulnerabilities. To learn more, see the [Amazon CodeGuru Detector
Library](../../detector-library/index.md "../../detector-library/index.md").

**Finding**

A security vulnerability that CodeGuru Security detects during a scan.

**Finding ID**

A unique identifier for a finding.

**Finding summary**

The number of findings of each severity level that are open across all scans in an
account.

**Finding status**

Indicates whether a finding is open or closed.

**Open findings**

Detected security vulnerabilities that have not been remediated and are still open. This
number could include new findings from a current scan or findings that are still open from a
previous scan.

**Relevant CWE**

The Common Weakness Enumeration, or set of software vulnerabilities with identification,
mitigation, and prevention descriptions that applies to a particular detector. For more
information, see [Common Weakness
Enumeration](https://cwe.mitre.org/ "https://cwe.mitre.org/").

**Rule ID**

An identifier for the rule that generated the finding.

**Scan**

An analysis of a code resource by CodeGuru Security for potential security policy violations and vulnerabilities.

**Scan name**

The unique name that CodeGuru Security uses to track scans across multiple revisions of the same
code resource. When you create a unique scan name and use it to re-run scans on updated
resources, CodeGuru Security is able to provide accurate metrics for your findings.

**Scan status**

Indicates whether a scan is in progress, complete, or failed.

**Severity**

The gravity of findings that CodeGuru Security identifies, divided into critical, high, medium,
low, and informational. For more information, see [Severity definitions](finding-severity.md#severity-definitions "finding-severity.md#severity-definitions").

**Vulnerability tags**

Categorizations of findings by type, programming language, or other classification such
as maintainability or consistency.

**Vulnerability name**

The categorization of a vulnerability based on the detector that generated the
finding.
