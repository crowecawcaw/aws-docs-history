# Disabling Amazon Detective

The administrator account for a behavior graph can disable Amazon Detective from the Detective console,
the Detective API, or AWS Command Line Interface. When you disable Detective, the behavior graph and its associated Detective
data are deleted.

Once a behavior graph is deleted, it cannot be restored.

###### Contents

- [Disabling Detective (Console)](#disable-from-console "#disable-from-console")
- [Disabling Detective (Detective API, AWS CLI)](#disable-from-api "#disable-from-api")
- [Disabling Detective across Regions (Python script on
  GitHub)](#disable-from-github-script "#disable-from-github-script")

## Disabling Detective (Console)

You can disable Amazon Detective from the AWS Management Console.

###### To disable Amazon Detective (console)

1. Open the Amazon Detective console at [https://console.aws.amazon.com/detective/](https://console.aws.amazon.com/detective/ "https://console.aws.amazon.com/detective/").
2. In the Detective navigation pane, under **Settings**, choose
   **General**.
3. On the **General** page, under **Disable Amazon Detective**,
   choose **Disable Amazon Detective**.
4. When prompted to confirm, type `disable`.
5. Choose **Disable Amazon Detective**.

## Disabling Detective (Detective API, AWS CLI)

You can disable Amazon Detective from the Detective API or the AWS Command Line Interface. To get the ARN of your
behavior graph to use in the request, use the [`ListGraphs`](../APIReference/API_ListGraphs.md "../APIReference/API_ListGraphs.md")
operation.

###### To disable Detective (Detective API, AWS CLI)

- **Detective API:** Use the [`DeleteGraph`](../APIReference/API_DeleteGraph.md "../APIReference/API_DeleteGraph.md") operation. You must
  provide the graph ARN.
- **AWS CLI:** At the command line, run the [`delete-graph`](../../../cli/latest/reference/detective/delete-graph.md "../../../cli/latest/reference/detective/delete-graph.md") command.

```
aws detective delete-graph --graph-arn `<graph ARN>`
```

Example:

```
aws detective delete-graph --graph-arn arn:aws:detective:us-east-1:111122223333:graph:123412341234
```

## Disabling Detective across Regions (Python script on

GitHub)

Detective provides an open-source script in GitHub that allows you to disable Detective for an administrator
account across a specified list of Regions.

For information on how to configure and use the GitHub scripts, see [Using Detective Python scripts to manage accounts](detective-github-scripts.md "detective-github-scripts.md").
