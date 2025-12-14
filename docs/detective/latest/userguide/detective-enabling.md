# Enabling Detective

You can enable Detective from the Detective console, the Detective API, or the AWS Command Line Interface.

You can only enable Detective once in each Region. If you already are the administrator
account for a behavior graph in the Region, then you cannot enable Detective again in that
Region.

Console

###### To enable Detective (console)

1. Sign in to the AWS Management Console. Then open the Detective console at [https://console.aws.amazon.com/detective/](https://console.aws.amazon.com/detective/ "https://console.aws.amazon.com/detective/").
2. Choose **Get started**.
3. On the **Enable Amazon Detective** page, **Align administrator
   accounts (recommended)** explains the recommendation to align the
   administrator accounts between Detective and Amazon GuardDuty and AWS Security Hub CSPM. See [Recommended alignment with GuardDuty and
   AWS Security Hub CSPM](detective-recommendations.md#recommended-service-alignment "detective-recommendations.md#recommended-service-alignment").
4. The **Attach IAM policy** button takes you directly to the IAM
   console and opens up the recommended policy, You have the option to attach the
   recommended policy to the principal you use for Detective. If you do not have permissions to
   operate in the IAM console, within the **Required permissions** you
   can copy the policy Amazon Resource Name (ARN) to provide it to your IAM
   administrator. They can attach the policy on your behalf.

Confirm that the required IAM policy is in place. 5. The **Add tags** section allows you to add tags to the behavior
graph.

To add a tag, do the following:

    1. Choose **Add new tag**.
    2. For **Key**, enter the name of the tag.
    3. For **Value**, enter the value of the tag.To remove a tag, choose the **Remove** option for that tag.

6. Choose **Enable Amazon Detective**.
7. After you enable Detective, you can invite member accounts to your behavior
   graph.

To navigate to the **Account management** page, choose
**Add members now**. For information about inviting member accounts,
see [Managing invited member accounts in Detective](accounts-invited-members.md "accounts-invited-members.md").

Detective API, AWS CLI
You can enable Amazon Detective from the Detective API or the AWS Command Line Interface.

###### To enable Detective (Detective API, AWS CLI)

- **Detective API:** Use the [`CreateGraph`](../APIReference/API_CreateGraph.md "../APIReference/API_CreateGraph.md")
  operation.
- **AWS CLI:** At the command line, run the [`create-graph`](../../../cli/latest/reference/detective/create-graph.md "../../../cli/latest/reference/detective/create-graph.md") command.

```
aws detective create-graph --tags '{"`tagName`": "`tagValue`"}'
```

The following command enables Detective and sets the value of the
`Department` tag to `Security`.

```
aws detective create-graph --tags '{"Department": "Security"}'
```

Python script on GitHub
You can enable Detective across Regions usin the Detective Python script on
GitHub.Detective provides an open-source script in GitHub that does the following:

- Enables Detective for an administrator account in a specified list of Regions
- Adds a provided list of member accounts to each of the resulting behavior
  graphs
- Sends invitation emails to the member accounts
- Automatically accepts the invitations for the member accounts

For information about how to configure and use the GitHub scripts, see [Using Detective Python scripts to manage accounts](detective-github-scripts.md "detective-github-scripts.md").

## Checking that Detective is ingesting data from your AWS account

After you enable Detective, it begins to ingest and extract data from your AWS account
into your behavior graph.

For the initial extraction, data usually becomes available in the behavior graph within
2 hours.

One way to check that Detective is extracting data is to look for example values on the
Detective **Search** page.

###### To check for example values on the Search page

1. Open the Amazon Detective console at [https://console.aws.amazon.com/detective/](https://console.aws.amazon.com/detective/ "https://console.aws.amazon.com/detective/").
2. In the navigation pane, choose **Search**.
3. From the **Select type** menu, choose a type of item.

**Examples from your data** contains a sample set of identifiers of
the selected type that are in your behavior graph data.

If you can see example values, then you know that data is being ingested and
extracted into your behavior graph.
