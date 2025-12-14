# Understanding the finding groups page

The finding groups page lists all the finding groups collected by Amazon Detective from your
behavior graph. Take note of the following attributes of finding groups:

**Severity of a group**
Each finding group is assigned a severity based on the AWS Security Finding Format (ASFF)
severity of the associated findings. ASFF finding severity values are
**Critical**, **High**,
**Medium**, **Low**, or
**Informational** from most to least severe. The severity of a
grouping is equal to the highest severity finding among the findings in that
grouping.

Groups that consist of **Critical** or **High** severity
findings that impact a large number of entities should be prioritized for
investigations, as they are more likely to represent high-impact security
issues.

**Group title**
In the **Title** column, each group has a unique ID and a non-unique title.
These are based on the ASFF type namespace for the group and the number of
findings within that namespace in the cluster. For example, if a grouping
has the title: Group with: **TTP (2), Effect (1), and Unusual
behavior (2)** it includes five total findings consisting of
two findings in the **TTP** namespace, one finding in the
**Effect** namespace, and two findings in the
**Unusual Behavior** namespace. For a complete list of
namespaces, see [Types taxonomy for ASFF](../../../securityhub/latest/userguide/securityhub-findings-format-type-taxonomy.md "../../../securityhub/latest/userguide/securityhub-findings-format-type-taxonomy.md").

**Tactics in a group**
The **Tactics** column in a group details which tactics category the activity
falls into. The tactics, techniques, and procedures categories in the
following list align to the [MITRE ATT&CK
matrix](https://attack.mitre.org/matrices/enterprise/ "https://attack.mitre.org/matrices/enterprise/").

You can select a tactic on the chain to see a description of the tactic. Following the chain is a
list of the tactics detected within the group. These categories and the
activities they typically represent are as follows:

- **Initial Access** – An adversary is trying to get into someone else’s
  network.
- **Execution** – An adversary is trying to get into someone else’s
  network.
- **Persistence** – An adversary is trying to maintain their
  foothold.
- **Privilege Escalation** – An adversary is trying to gain higher-level
  permissions.
- **Defense Evasion** – An adversary is trying to avoid being
  detected.
- **Credential Access** – An adversary is trying to steal account names
  and passwords.
- **Discovery** – An adversary is trying to understand and learn about
  an environment.
- **Lateral Movement** – An adversary is trying to move through an
  environment.
- **Collection** – An adversary is trying to gather data of interest to
  their goal.
- **Command and Control** – An adversary is trying to get into someone
  else’s network.
- **Exfiltration** – An adversary is trying to steal data.
- **Impact** – An adversary is trying to manipulate, interrupt, or
  destroy your systems and data.
- **Other** – Indicates activity from a finding that does not align with
  tactics listed in the matrix.

**Entities within a group**
The **Entities** column contains details on the specific entities detected
within this grouping. Select this value for a breakdown of entities based on
the categories: **Identity**, **Network**,
**Storage**, and **Compute**. Examples
of entities in each category are:

- **Identity** – IAM principals and AWS accounts, such as user and
  role
- **Network** – IP address or other networking and VPC entities
- **Storage** – Amazon S3 buckets or
  DDBs
- **Compute** Amazon EC2 instances or
  Kubernetes
  containers

**Accounts within a group**
The **Accounts** column tells you what AWS accounts own entities involved
with the findings in the group. The AWS Accounts are listed by name and
AWS ID so you can prioritize investigations of activity involving critical
accounts.

**Findings within a group**
The **Findings** column has a lists the entities within a group by severity.
The findings include Amazon GuardDuty findings, Amazon Inspector findings, AWS security
findings, and evidence from Detective. You can select the graph to see an exact
count of findings by severity.

GuardDuty findings are part of the Detective core package and are ingested by default. All
other AWS security findings that are aggregated by Security Hub CSPM are ingested as
an optional data source. See [Source data used in a behavior graph](detective-source-data-about.md "detective-source-data-about.md") for more details.
