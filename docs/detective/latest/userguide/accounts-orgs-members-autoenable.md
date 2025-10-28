# Enabling new organization accounts as Detective member

accounts

The Detective administrator account can configure Detective to automatically enable new organization
accounts as member accounts in the organization behavior graph.

When new accounts are added to your organization, they are added to the list on the
**Account management** page. For organization accounts,
**Type** is **By organization**.

By default, new organization accounts are not enabled as member accounts. Their status is
**Not a member**.

When you choose to enable organization accounts automatically, then Detective begins to enable
new accounts as member accounts as they are added to the organization. Detective does not enable
existing organization accounts that are not yet enabled.

Detective can enable organization accounts as member accounts only if the maximum number of
member accounts for a behavior graph is 1,200. If your behavior graph already contains 1,200
member accounts, then new accounts cannot be enabled.

ConsoleOn the **Account management** page, the **Automatically enable new
organization accounts** setting determines whether to automatically enable accounts as
they are added to an organization.

###### To automatically enable new organization accounts as member accounts

1. Open the Amazon Detective console at [https://console.aws.amazon.com/detective/](https://console.aws.amazon.com/detective/ "https://console.aws.amazon.com/detective/").
2. In the Detective navigation pane, choose **Account management**.
3. Toggle **Automatically enable new organization accounts** to the on
   position.

DetectiveAPI/AWS CLITo determine whether to automatically enable new organization accounts as Detective member accounts,
the administrator account can use the Detective API or the AWS Command Line Interface.

To view and manage the configuration, you must provide the behavior graph ARN. To obtain
the ARN, use the [`ListGraphs`](../APIReference/API_ListGraphs.md "../APIReference/API_ListGraphs.md")
operation.

###### To view the current configuration for automatically enabling organization

accounts

- **Detective API:** Use the [`DescribeOrganizationConfiguration`](../APIReference/API_DescribeOrganizationConfiguration.md "../APIReference/API_DescribeOrganizationConfiguration.md") operation.

In the response, if new organization accounts are enabled automatically, then
`AutoEnable` is `true`.

- **AWS CLI:** At the command line, run the [`describe-organization-configuration`](../../../cli/latest/reference/detective/describe-organization-configuration.md "../../../cli/latest/reference/detective/describe-organization-configuration.md") command.

```
aws detective describe-organization-configuration --graph-arn `<behavior graph ARN>`
```

**Example**

```
aws detective describe-organization-configuration --graph-arn arn:aws:detective:us-east-1:111122223333:graph:123412341234
```

###### To automatically enable new organization accounts

- **Detective API:** Use the [`UpdateOrganizationConfiguration`](../APIReference/API_UpdateOrganizationConfiguration.md "../APIReference/API_UpdateOrganizationConfiguration.md") operation. To automatically enable new
  organization accounts, set `AutoEnable` to `true`.
- **AWS CLI:** At the command line, run the [`update-organization-configuration`](../../../cli/latest/reference/detective/update-organization-configuration.md "../../../cli/latest/reference/detective/update-organization-configuration.md") command.

```
aws detective update-organization-configuration --graph-arn `<behavior graph ARN>` --auto-enable | --no-auto-enable
```

Example

```
aws detective update-organization-configuration --graph-arn arn:aws:detective:us-east-1:111122223333:graph:123412341234 --auto-enable
```
