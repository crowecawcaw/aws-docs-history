# Review IAM Access Analyzer findings

After you enable IAM Access Analyzer, the next step is to review any findings to determine
whether the access identified in the finding is intentional or unintentional. You can also
review findings to determine similar findings for access that is intended, and then [create an archive rule](access-analyzer-archive-rules.md "access-analyzer-archive-rules.md") to automatically
archive those findings. You can also review archived and resolved findings.

You should review all of the findings in your account to determine whether the external,
internal, or unused access is expected and approved. If the access identified in the finding
is expected, you can archive the finding. When you archive a finding, the status is changed
to **Archived**, and the finding is removed from the active findings list.
The finding is not deleted. You can view your archived findings at any time. Work through
all of the findings in your account until you have zero active findings. After you get to
zero findings, you know that any new **Active** findings that are generated
are from a recent change in your environment.

###### To review active findings for all types of access analyzers

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Access analyzer**. The findings dashboard is displayed.
3. Choose **Select analyzers**.
4. In the **Select analyzers** window, choose a maximum of one
   external access analyzer and a maximum of one internal access analyzer from the
   **Resource access analyzers** dropdown. Choose an unused access
   analyzer from the **Unused access analyzers** dropdown.
5. Choose **Update summary**. A summary of the active findings for
   the selected access analyzers is displayed on the dashboard. Choose a finding type
   in the **Resource access findings** or **Unused access
   findings** sections to view all active findings of the selected
   type.

For more information on viewing the findings dashboard, see [View the IAM Access Analyzer findings
dashboard](access-analyzer-dashboard.md "access-analyzer-dashboard.md").

###### Note

Findings are displayed only if you have permission to view findings for the
analyzer.

## External and internal access

findings

###### Note

IAM Access Analyzer charges for internal access analysis based on the number of
resources monitored per Region per month. For more details about pricing, see [IAM Access Analyzer
pricing](https://aws.amazon.com/iam/access-analyzer/pricing "https://aws.amazon.com/iam/access-analyzer/pricing").

1. Under **Access Analyzer**, choose **Resource
   analysis**.
2. Choose **Select analyzers**.
3. In the **Select analyzers** window, choose a maximum of one
   external access analyzer and a maximum of one internal access analyzer from the
   **Resource access analyzers** dropdown.
4. Choose **Update summary**.

The **Resource analysis** page displays the following details
about the resources with active findings for the selected access
analyzers:

**Name**

The name of the resource with active findings.

**Type**

The type of the resource.

**Owner account**

This column is displayed only if you are using an organization as the zone
of trust for one or more of the selected analyzers. The account in the
organization that owns the resource reported in the finding.

**Active findings**

A visual representation of the number and type of active findings for the
resource. Hover over the field to display more information about the
findings for the resource.

**Public access**

Indicates whether any of the findings for the resource allow public
access.

## Unused access findings

###### Note

IAM Access Analyzer charges for unused access analysis based on the number of IAM
roles and users analyzed per month. For more details about pricing, see [IAM Access Analyzer
pricing](https://aws.amazon.com/iam/access-analyzer/pricing "https://aws.amazon.com/iam/access-analyzer/pricing").

1. Under **Access Analyzer**, choose **Unused
   access**.
2. Choose **Select analyzers**.
3. In the **Select analyzers** window, choose an unused access
   analyzer from the **Unused access analyzers** dropdown.
4. Choose **Update summary**.

The **Unused access** page displays the following details
about the IAM entities that generated the findings for the selected access
analyzer:

**Finding ID**

The unique ID assigned to the finding. Choose the finding ID to display
additional details about the IAM entity that generated the finding.

**Finding type**

The type of unused access finding: **Unused access key**,
**Unused password**, **Unused
permission**, or **Unused role**.

**IAM entity**

The IAM entity reported in the finding. This can be an IAM user or
role.

**AWS account ID**

This column is displayed only if you set up the analyzer for all
AWS accounts in the organization. The AWS account in the organization
that owns the IAM entity reported in the finding.

**Last updated**

The last time that the IAM entity reported in the finding was updated,
or when the entity was created if no updates have been made.

**Status**

The status of the finding (**Active**,
**Archived**, or **Resolved**).
