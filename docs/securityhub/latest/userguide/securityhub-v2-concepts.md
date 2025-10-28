# Security Hub concepts

###### Note

Security Hub is in preview release and is subject to change.

In Security Hub, we build on common AWS concepts and terminology and use these additional terms.

**Account**

The standard AWS account containing your AWS resources.
Sign in to AWS with your AWS account to enable Security Hub.

If your account is enrolled in AWS Organizations, your organization designates a Security Hub administrator account.
This account can enable other organization accounts as member accounts.

An organization can only have one administrator account.
An account cannot be an administrator account and a member account simultaneously.

Security Hub supports the following accounts:

- Organization management account — an AWS account that administers an AWS organization.
- Delegated administrator account — an AWS account that manages the use of an AWS service for an AWS organization.
- Member account — an AWS account that is a member of an AWS organization.
- Standalone account — an AWS account without AWS Organizations enabled

**Administrator account**

This type of AWS account can view findings for associated member accounts.

This type of AWS account becomes an administrator account when the account is designated by an organization management account as the Security Hub administrator account.
The Security Hub administrator account can enable any organization account as a member account and can also invite other accounts to be member accounts.

An organization can only have one administrator account.
An account cannot be an administrator account and a member account simultaneously.

**Aggregation Region**

An aggregation Region allows you to view security findings from multiple AWS Regions in a single pane of glass.

The aggregation Region is the AWS Region where you view and manage findings.
Findings are aggregated in the aggregation Region from linked Regions.
Updated findings are replicated across Regions.

In the aggregation Region, the dashboard and inventory pages include data from all linked Regions.
The automations page can only be used to define automation rules in the aggregation region.
Third-party ticketing integrations can only be configured in the aggregation region.

**Archived finding**

A finding with a status of `ARCHIVED`.
These findings indicate the finding provider or customer investigating the finding believes the finding is no longer relevant.

Finding providers can archive findings they create.

In the Security Hub console, default filter settings exclude archived findings from finding lists and tables.
You can update the filters to include archived findings.
If you retrieve findings by using the [GetFindingsV2](../../1.0/APIReference/API_GetFindingsV2.md "../../1.0/APIReference/API_GetFindingsV2.md") operation, the operation retrieves both archived and active findings.
The following example shows how to exclude archived findings in the results.

```
{
    "StringFilters":
    [
        {
            "FieldName": "status",
            "Filter":
            {
                "Value": "Archived",
                "Comparison": "EQUALS"
            }
        }
    ]
}
```

**Cross-Region aggregation**

The aggregation of findings and resources from linked Regions to an aggregation Region.
You can view all of your data from the aggregation Region and update findings from the aggregation Region.

**Delegated administrator account**

In AWS Organizations, the delegated administrator account for a service is able to
manage the use of a service for the organization.

In Security Hub, the Security Hub administrator account is also the delegated administrator
account for Security Hub. When the organization management account first designates the
Security Hub administrator account, Security Hub calls Organizations to make that account the delegated
administrator account.

The organization management account must then choose the delegated
administrator account as the Security Hub administrator account in all Regions.

**Exposure**

A potential security scenario in your account that may be due to vulnerabilities, exploitable resources, or misconfigurations.

**Exposure finding**

A type of finding that describes an exposure present in your environment.
An exposure finding includes traits and signals.
A signal can include one or more types of exposure traits.
Security Hub generates an exposure finding when signals from Security Hub CSPM control findings or other AWS services, such as Amazon Inspector, indicate the presence of an exposure.
A resource can have at most one exposure finding.
Security Hub generates an exposure finding when a resource is exposed.
If a resource doesn't have any exposure traits or has insufficient traits, Security Hub doesn't generate an exposure finding for that resource.

**Finding**

The observable record of a security check or security-related detection. Security Hub
generates and updates findings through the correlation of other security findings.
These are called _exposure findings_. Findings
can also come from integrations with other AWS services and third-party
products.

**Finding ingestion**

The import of findings into Security Hub .
Finding ingestion events include both new findings and updates to existing
findings.

**Linked Region**

When you enable cross-Region aggregation, a linked Region is a region that aggregates findings and resource inventory to the aggregation Region.

In a linked Region, the dashboard and inventory pages only contain findings for that AWS Region.

**Open cybersecurity schema framework (OCSF)**

The [Open Cybersecurity Schema Framework (OCSF)](https://schema.ocsf.io/ "https://schema.ocsf.io/") is a collaborative, open-source effort by AWS and leading partners in the cybersecurity industry.
OCSF provides a standard schema for common security events, defines versioning criteria to facilitate schema evolution, and includes a self-governance process for security log producers and consumers.
For more information, see [OCSF findings in Security Hub](ocsf-findings.md "ocsf-findings.md").

**Member account**

An AWS account that granted permission to an administrator account to view and take action on their findings.
This kind of AWS account becomes a member account when the Security Hub administrator account enables it as a member account.

**Signal**

A finding that contributes to an exposure finding.
A signal can be referred to as a _contributing finding_.
A signal can originate in Security Hub CSPM, AWS Config, or other AWS services, such as Amazon Inspector.

**Trait**

A security deviation that results in an exposure finding.
Trait types include **Assumability**, **Misconfiguration**, **Reachability**, **Sensitive Data**, and **Vulnerability**.
A trait is associated with one signal, and a signal can contain multiple traits.
For example, a Security Hub CSPM control indicates a customer-managed policy allows administrative access control.
This signal contains a misconfiguration trait.
