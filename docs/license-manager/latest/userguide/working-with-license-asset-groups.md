# Working with license asset groups

This section describes how to create, update, delete, and manage license asset groups in AWS License Manager. License asset groups help track and manage licenses across your AWS resources.

## Creating license asset groups

License asset groups track and manage licenses across your AWS resources. You can create multiple asset groups to organize different software products and modify their settings at any time to adapt to your licensing needs.

###### Note

You can use a one-click template to quickly create a license asset group, or follow the steps below to manually create a license asset group by adding various license rule sets based on your specific needs.

###### To create license asset groups using the console

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. In the navigation pane, choose **License asset discovery and ruleset**.
3. In the **License asset discovery** section, ensure **Region discovery** is populated with regions.
4. In the **License asset ruleset** section, select either **AWS-managed rulesets** (preset rules configured for specific AWS-managed products) or **custom rulesets**. See .
5. Choose **Create license asset group with ruleset**.
6. For **License asset group name**, enter a friendly name to remember how you are grouping the assets.
7. (Optional) For **License asset group description**, enter a detailed description about how you are grouping the assets.
8. For **Usage Dimension**, choose one of the following options: vCPU, Sockets, Instance, or Core. This field determines the usage calculation for the assets.
9. Select one or more **License asset ruleset**, either **Create new** ruleset or **Add** from existing AWS managed or custom ruleset. See .
10. (Optional) For **Tags**, add one or more tags.
11. Choose **Create license asset group**.

###### Note

Once a license asset group is created, discovery begins automatically and typically completes within 24 hours. During this time, License Manager scans your configured regions and accounts to identify all instances matching your ruleset criteria.

###### To create license asset groups using the CLI

- Use the `create-license-asset-group` command. For more information, see the [AWS CLI Command Reference](../../../cli/latest/reference/license-manager/create-license-asset-group.md "../../../cli/latest/reference/license-manager/create-license-asset-group.md").

```

aws license-manager create-license-asset-group \
    --name "Windows Server Group" \
    --description "License asset group for Windows Server instances" \
    --license-asset-group-configurations UsageDimension=vCPU \
    --associated-license-asset-ruleset-arns arn:aws:license-manager:region:account:ruleset/ruleset-id \
    --client-token unique-token

```

## Updating license asset groups

You can update license asset groups to modify their configuration, add or remove rulesets, and update tags.

###### To update license asset groups using the console

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. In the navigation pane, choose **Licenses**.
3. In the **License asset group** section, ensure one or more license asset groups are available.
4. To select a license asset group for editing, select the check box and choose **Actions**, **Edit**. Alternatively, choose the item itself.
5. Choose the **Edit** button on the license asset group's page. From here, you can:
   - Edit the license asset group name
   - Edit the license asset group description
   - Add or remove license asset rulesets
   - Add or remove license asset group tags

6. Choose **Save changes** when your changes are complete.

###### To update license asset groups using the CLI

- Use the `update-license-asset-group` command. For more information, see the [AWS CLI Command Reference](../../../cli/latest/reference/license-manager/update-license-asset-group.md "../../../cli/latest/reference/license-manager/update-license-asset-group.md").

```

aws license-manager update-license-asset-group \
    --license-asset-group-arn arn:aws:license-manager:region:account:license-asset-group/group-id \
    --name "Updated Windows Server Group" \
    --description "Updated description for Windows Server instances"

```

## Deleting license asset groups

You can delete license asset groups that are no longer needed. Note that this action cannot be undone, and rulesets associated with the license asset group will not be deleted.

###### To delete license asset groups using the console

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. In the navigation pane, choose **Licenses**.
3. In the **License asset group** section, ensure one or more license asset groups are available.
4. To select a license asset group for deletion, select the check box and choose **Actions**, **Delete**. Alternatively, choose the item itself, then choose the **Delete** button from the license asset group's page.
5. To permanently delete the license asset group, type `confirm` in the text box, then choose **Delete**.

###### Important

This action cannot be undone. Rulesets associated with this license asset group will not be deleted.

###### To delete license asset groups using the CLI

- Use the `delete-license-asset-group` command. For more information, see the [AWS CLI Command Reference](../../../cli/latest/reference/license-manager/delete-license-asset-group.md "../../../cli/latest/reference/license-manager/delete-license-asset-group.md").

```

aws license-manager delete-license-asset-group \
    --license-asset-group-arn arn:aws:license-manager:region:account:license-asset-group/group-id

```

## Viewing license asset group details

You can view detailed information about your license asset groups, including associated rulesets, instances, and licenses.

###### To view license asset group details using the console

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. In the navigation pane, choose **Licenses**.
3. In the **License asset group** section, ensure one or more license asset groups are available.
4. To view details for a license asset group, select the check box and choose **Actions**, **View details**. Alternatively, choose the item itself.

###### To view license asset groups using the CLI

- Use the `get-license-asset-group` command. For more information, see the [AWS CLI Command Reference](../../../cli/latest/reference/license-manager/get-license-asset-group.md "../../../cli/latest/reference/license-manager/get-license-asset-group.md").

```

aws license-manager get-license-asset-group \
    --license-asset-group-arn arn:aws:license-manager:region:account:license-asset-group/group-id

```

## List license asset groups

You can list all license asset groups in your account to view their status and configuration.

###### To list license asset groups using the console

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. In the left navigation pane, choose **License asset groups**.
3. View the list of license asset groups with their names, status, and associated rulesets.

###### To list license asset groups using the CLI

- Use the `list-license-asset-groups` command. For more information, see the [AWS CLI Command Reference](../../../cli/latest/reference/license-manager/list-license-asset-groups.md "../../../cli/latest/reference/license-manager/list-license-asset-groups.md").

```

aws license-manager list-license-asset-groups \
    --max-results 50 \
    --next-token token-from-previous-call

```

## Listing discovered assets for a license asset group

It takes up to 24 hours to view all instances, granted licenses, and self-managed licenses associated within a license asset group. Any changes to your instances, granted licenses, and self-managed licenses are reflected in 24 hours.

###### To list assets for a license asset group using the console

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. In the navigation pane, choose **Licenses**.
3. View details for a license asset group by selecting the check box and choosing **Actions**, **View details**. Alternatively, choose the item itself.
4. From the license asset group's page, you can view all instances, granted licenses, and self-managed licenses associated with the license asset group.

###### To list assets for license asset groups using the CLI

- Use the `list-assets-for-license-asset-group` command. For more information, see the [AWS CLI Command Reference](../../../cli/latest/reference/license-manager/list-assets-for-license-asset-group.md "../../../cli/latest/reference/license-manager/list-assets-for-license-asset-group.md").

```

aws license-manager list-assets-for-license-asset-group \
    --license-asset-group-arn arn:aws:license-manager:region:account:license-asset-group/group-id

```
