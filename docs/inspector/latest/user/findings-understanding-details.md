# Viewing details for your Amazon Inspector findings

The procedure in this section describes how to view details for Amazon Inspector findings.

###### To view the details for a finding

1. Sign in using your credentials, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home")
2. Select the Region to view findings in.
3. In the navigation pane, choose **Findings** to display the
   findings list
4. (Optional) Use the filter bar to select a specific finding. For more
   information, see [Filtering your Amazon Inspector findings](findings-managing-filtering.md "findings-managing-filtering.md").
5. Choose a finding to view its details panel.
   The **Finding details** panel contains the basic identifying features
   of the finding. This includes the title of the finding as well as a basic description of
   the vulnerability identified, remediation suggestions, and a severity score. For
   information about scoring, see [Understanding severity levels for your Amazon Inspector findings](findings-understanding-severity.md "findings-understanding-severity.md").

The details available for a finding varies depending on finding type and the
**Resource affected**.

All findings contain the AWS account ID number the finding was identified for, a
severity, a finding **Type**, the date the finding was created at, and
a **Resource affected** section with details about that
resource.

The finding **Type** determines the remediation and vulnerability
intelligence information available for the finding. Depending on the finding type, different finding details are available.

**Package Vulnerability**

Package vulnerability findings are available for EC2 instances, ECR
container images, and Lambda functions. See [Package vulnerability](findings-types.md#findings-types-package "findings-types.md#findings-types-package") for more info.

Package vulnerability findings also include [Viewing the Amazon Inspector score and understanding vulnerability intelligence details](findings-understanding-score.md "findings-understanding-score.md").

This finding type has the following details:

- **Fix available** – Indicates if the
  vulnerability is fixed in a newer version of the affected packages.
  Has one of the following values:
  - `YES`, which means all the affected packages
    have a fixed version.
  - `NO`, which means no affected packages have a
    fixed version.
  - `PARTIAL`, which means one or more (but not
    all) of the affected packages have a fixed version.

- **Exploit available** – Indicates the
  vulnerability has a known exploit.
  - `YES`, which means the vulnerability discovered
    in your environment has a known exploit. Amazon Inspector doesn't have
    visibility into the use of exploits in an environment.
  - `NO`, which means this vulnerability doesn't
    have a known exploit.

- **Affected packages** – Lists
  each package identified as vulnerable in the finding, and the
  details of each package:
- **Filepath** – The EBS volume
  ID and partition number associated with a finding. This field is
  present in findings for EC2 instances scanned using [Agentless scanning](scanning-ec2.md#agentless "scanning-ec2.md#agentless").
- **Installed version / Fixed version**
  – The version number of the currently installed package that
  a vulnerability was detected for. Compare the installed version
  number with the value after the slash (**/**). The second value is the version number of the
  package that fixes the detected vulnerability as provided by the
  Common Vulnerabilities and Exposures (CVEs) or advisory associated
  with the finding. If the vulnerability has been fixed in multiple
  versions, this field lists the most recent version that includes the
  fix. If a fix isn't available, this value is `None
available`.

###### Note

If a finding was detected before Amazon Inspector began including this
field in findings, the value for this field is empty. However, a
fix may be available.

- **Package manager** – The
  package manager used to configure this package.
- **Remediation** – If a fix is available
  through an updated package or programming library, this section
  includes the commands that you can run to make the update. You can
  copy the provided command and run it in your environment.

###### Note

Remediation commands are provided from vendor data feeds and
may vary depending on your system configuration. Review finding
references or operating system documentation for more specific
guidance.

- **Vulnerability details** –
  provides a link to the Amazon Inspector preferred source for the CVE identified
  in the finding, such as National Vulnerability Database (NVD),
  REDHAT, or another OS vendor. Additionally, you will find the
  severity scores for the finding. For more information about severity
  scoring such as, see [Understanding severity levels for your Amazon Inspector findings](findings-understanding-severity.md "findings-understanding-severity.md"). The following
  scores are included, including the scoring vectors for each:
  - [Exploit Prediction Scoring System (EPSS) score](https://www.first.org/epss/ "https://www.first.org/epss/")
  - Inspector score
  - CVSS 3.1 from Amazon CVE
  - CVSS 3.1 from NVD
  - CVSS 2.0 from NVD (where applicable, for older
    CVEs)

- **Related vulnerabilities** –
  Specifies other vulnerabilities related to the finding. Typically
  these are other CVEs that impact the same package version, or other
  CVEs within the same group as the finding CVE, as determined by the
  vendor.
- **Resources affected** – Includes information about the registry, repository, resource type, image ID, and image operating system.
  It also includes information, such as when an image was last pushed, how many Amazon ECS tasks and Amazon EKS pods are deployed, and when the image was last used in the past 24 hours.
  If you have any deployed Amazon ECS tasks and Amazon EKS pods, you can view details by choosing the value for the field.
  This directs you to a screen where you can view information, such as the cluster ARN, when the resource was last used in the past 24 hours, the running and stopped count for the resource, and the workload name and type.

**Code vulnerability**

Code vulnerability findings are available for Lambda functions only. See
[Code vulnerability](findings-types.md#findings-types-code "findings-types.md#findings-types-code") for more info. This finding type has the following details:

- **Fix available** – For code
  vulnerabilities this value is always `YES`.
- **Detector name** – The name of the
  Amazon Q detector used to detect the code vulnerability.
  For a list of possible detections, see the [Q Detector Library](../../../amazonq/detector-library.md "../../../amazonq/detector-library.md").
- **Detector tags** – The Amazon Q
  tags associated with the detector, Amazon Q uses tags to
  categorize detections.
- **Relevant CWE** – IDs of the Common
  Weakness Enumeration (CWE)s associated with the code
  vulnerability.
- **File path** – The file location of the
  code vulnerability.
- **Vulnerability location** – For
  Lambda code scanning code vulnerabilities, this field shows the exact lines
  of code where Amazon Inspector found the vulnerability.
- **Suggested remediation** – This suggests
  how the code can be edited to remediate the finding.

**Network reachability**

Network reachability findings are only available for EC2 instances. See
[Network reachability](findings-types.md#findings-types-network "findings-types.md#findings-types-network") for more info. This finding
type has the following details:

- **Open port range** – The port range
  through which the EC2 instance could be accessed.
- **Open network paths** – Shows the open
  access path to the EC2 instance. Select an item on the path for more
  information.
- **Remediation** – Recommends a method for
  closing the open network path.
