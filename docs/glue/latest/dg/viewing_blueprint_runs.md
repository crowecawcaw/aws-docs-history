# Viewing blueprint runs in AWS Glue

View a blueprint run to see the following information:

- Name of the workflow that was created.
- blueprint parameter values that were used to create the workflow.
- Status of the workflow creation operation.
  You can view a blueprint run by using the AWS Glue console, AWS Glue API, or AWS Command Line Interface
  (AWS CLI).

###### To view a blueprint run (console)

1. Open the AWS Glue console at
   [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").
2. In the navigation pane, choose **blueprints**.
3. On the **blueprints** page, select a blueprint. Then on the
   **Actions** menu, choose **View**.
4. At the bottom of the **Blueprint Details** page, select a blueprint run,
   and on the **Actions** menu, choose **View**.

###### To view a blueprint run (AWS CLI)

- Enter the following command. Replace `<blueprint-name>` with
  the name of the blueprint. Replace `<blueprint-run-id>` with the
  blueprint run ID.

```
aws glue get-blueprint-run --blueprint-name `<blueprint-name>` --run-id `<blueprint-run-id>`

```

###### See also:

- [Overview of blueprints in AWS Glue](blueprints-overview.md "blueprints-overview.md")
