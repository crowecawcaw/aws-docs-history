

# Flow versioning and aliasing in Connect Customer
<a name="flows-versions-aliases"></a>

To improve maintenance efficiency and reduce deployment risks, Connect Customer supports versioning and aliasing for flows. This lets you track changes over time, roll back to a known-good state, and control which content is live without editing the flows that reference it.

Flow version  
A version is an immutable, point-in-time snapshot of the flow. You can continue to edit the flow and create new versions as needed. Connect Customer assigns each version a sequential number automatically.

Flow alias  
An alias is a reference to a specific version of the flow. Aliases let you switch between flow versions without updating each Connect Customer resource. Resources such as queues, quick connects, and phone numbers can reference a flow alias instead of a specific version. When you publish a new version, you point the alias to it, and every Connect Customer resource that uses the alias picks up the new version automatically. Each alias is assigned a unique alias ID when it's created, and you can also assign it an alias name.

Following are the benefits of using flow versioning and aliasing:
+ **Immutable versions**. Each published version is a point-in-time snapshot of the flow's content that remains unchanged, which provides consistency and reliability for rollback and audit.
+ **Safer deployments**. Aliases let you point live traffic at a specific version and switch versions with a single update, without republishing or relinking every reference.
+ **Easier change tracking**. Sequential version numbers (starting from 1) and human-readable version descriptions make it straightforward to see what changed and when.

**Topics**
+ [Reference a version or alias of a flow](#flow-version-alias-reference)
+ [Create a version of a flow](#flow-version-create)
+ [Create an alias for a flow](#flow-alias-create)
+ [View a specific version or alias of a flow](#flow-version-alias-view)
+ [Use flow versions and aliases](#flow-version-alias-use)
+ [Audit history](#flow-version-alias-audit-history)
+ [Metrics](#flow-version-alias-metrics)
+ [Reference aliases or versions in other resources](#flow-version-alias-reference-other-resources)

## Reference a version or alias of a flow
<a name="flow-version-alias-reference"></a>

You can reference a specific version or alias of a flow by using the qualified ARN or ID:
+ `flow-arn-or-id:VersionNumber` references a specific version.
+ `flow-arn-or-id:AliasId` references an alias.

## Create a version of a flow
<a name="flow-version-create"></a>

When you publish a flow, select the **Create new version** check box to create a new version of the flow.

![The Publish dialog box with the Create new version check box selected.](https://docs.aws.amazon.com/connect/latest/adminguide/images/fva-publish-create-version.png)


If a flow is already published, the **Versions** tab is enabled. You can also choose **Create version** to create a new version of the flow.

![The Create version dialog box.](https://docs.aws.amazon.com/connect/latest/adminguide/images/fva-create-version-dialog.png)


## Create an alias for a flow
<a name="flow-alias-create"></a>

To create an alias, you must first create a version for the flow. After the version is created, navigate to the **Aliases** tab and choose **Create alias** to create a new alias for the flow. When you create the alias, you must associate it with a version.

![The Create alias dialog box, where you associate the alias with a version.](https://docs.aws.amazon.com/connect/latest/adminguide/images/fva-create-alias-dialog.png)


## View a specific version or alias of a flow
<a name="flow-version-alias-view"></a>

To view a specific flow alias or version, choose the version or alias link on the **Versions** or **Aliases** list page.

![The Versions list page.](https://docs.aws.amazon.com/connect/latest/adminguide/images/fva-versions-list.png)


![The Aliases list page.](https://docs.aws.amazon.com/connect/latest/adminguide/images/fva-aliases-list.png)


When you choose the link, the designer opens in read-only mode.

![A flow version open in the designer in read-only mode.](https://docs.aws.amazon.com/connect/latest/adminguide/images/fva-read-only-designer.png)


## Use flow versions and aliases
<a name="flow-version-alias-use"></a>

When you reference a flow, you can optionally use either an alias or a version. If you don't select an alias or version, the latest published content of the flow will be referenced.

![Referencing a flow alias from the Transfer to flow block.](https://docs.aws.amazon.com/connect/latest/adminguide/images/fva-transfer-alias.png)


![Referencing a flow version from the Transfer to flow block.](https://docs.aws.amazon.com/connect/latest/adminguide/images/fva-transfer-version.png)


## Audit history
<a name="flow-version-alias-audit-history"></a>

On the designer page, you can view and switch between different versions and aliases of the flow by using the **Audit history** dropdown list.

![The Audit history dropdown list on the designer page.](https://docs.aws.amazon.com/connect/latest/adminguide/images/fva-audit-history-dropdown.png)


You can also track all the changes made to the different aliases and versions of the flow on the flow historical changes page.

![The flow historical changes page, showing recent changes to the flow.](https://docs.aws.amazon.com/connect/latest/adminguide/images/fva-historical-changes.png)


## Metrics
<a name="flow-version-alias-metrics"></a>

To view the metrics associated with a flow version or flow alias, you can:

1. Open the flow version or alias in read-only mode, and then choose **Show Metrics**.  
![Metrics displayed for a flow version open in read-only mode.](https://docs.aws.amazon.com/connect/latest/adminguide/images/fva-metrics-read-only.png)

1. Use the **Audit history** dropdown list to switch to the alias or version, and then choose **Show Metrics**.  
![Using the Audit history dropdown list to switch to a version before showing metrics.](https://docs.aws.amazon.com/connect/latest/adminguide/images/fva-metrics-audit-history.png)  
![Metrics displayed on the flow designer for a specific version.](https://docs.aws.amazon.com/connect/latest/adminguide/images/fva-metrics-displayed.png)

## Reference aliases or versions in other resources
<a name="flow-version-alias-reference-other-resources"></a>

You can optionally reference an alias or version when you configure any of the following pages that require you to reference a flow:
+ Queues
+ Quick connects
+ Phone numbers
+ Test chat
+ Test management
+ Task template
+ Email
+ Outbound campaigns
+ Views
+ Rules