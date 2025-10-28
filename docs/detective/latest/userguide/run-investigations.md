# Running a Detective Investigation

Use **Run investigation** to analyze resources such as IAM users
and IAM roles and to generate an investigation report. The generated report details
anomalous behavior that indicates potential compromise.

ConsoleFollow these steps to run a Detective Investigation from the
**Investigations page** using the Amazon Detective
console.

1.  Sign in to the AWS Management Console. Then open the Detective console at
    [https://console.aws.amazon.com/detective/](https://console.aws.amazon.com/detective/ "https://console.aws.amazon.com/detective/").
2.  In the navigation pane, choose **Investigations**.
3.  In the **Investigations** page, choose **Run investigation** in the top right corner.
4.  In the **Select resource** section, you have three ways to run an investigation. You can choose
    to run the investigation for a resource recommended by Detective. You can
    run the investigation for a specific resource. You can also investigate a resource from the Detective Search page.
    1. `Choose a recommended resource` – Detective recommends resources based on its activity in findings and
       finding groups. To run the investigation for a resource recommended by Detective, in the **Recommended resources** table, select a resource to
       investigate.

    The Recommended resources table provides the following details:

        * **Resource ARN** – The Amazon Resource Name
         (ARN) of the AWS resource.
        * **Reason to investigate** – Displays the key
         reason(s) to investigate the resource. The reasons for which Detective recommends to investigate a resource are as follows:




        	+ If a resource was involved in a High Severity finding in the last 24 hours.
        	+ If a resource was involved in a finding group observed in the last 7 days. Detective finding groups let you examine multiple activities as they relate to a potential security event. For more details, see [Analyzing finding groups](groups-about.md "groups-about.md").
        	+ If a resource was involved in a finding in the last 7 days.
        * **Latest finding** – Latest findings are
         prioritized on top of the list.
        * **Resource type** – Identifies the type of
         resource. For example, an AWS user or AWS role.

    2. `Specify an AWS role or user with an ARN` – You can select an AWS role or AWS user and run an investigation for the specific resource.

    Follow these steps to investigate a specific resource type.

        1. From the **Select resource type** drop-down list, choose AWS role or AWS user.
        2. Enter the **Resource ARN** of the IAM resource. For more details about Resource ARNs, see [Amazon Resource Names (ARNs)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md") in the IAM User Guide.

    3. `Find a resource to investigate from the Search page` – You can search all of your IAM resources from the Detective
       **Search** page.

    Follow these steps to investigate a resource from the Search page.

        1. In the navigation pane, choose **Search**.
        2. In the Search page, search for an IAM resource.
        3. Navigate to the profile page of the resource and run investigation from there.

5.  In the **Investigation scope time** section, choose the
    **Scope time** for the investigation to assess the selected
    resource's activity. You can select a **Start date** and
    **Start time**; and **End date** and
    **End time** in UTC format. The selected scope time window
    can be between at a minimum of 3 hours and a maximum of 30 days.
6.  Choose **Run investigation**.

APITo run an investigation programmatically, use the [StartInvestigation](../APIReference/API_StartInvestigation.md "../APIReference/API_StartInvestigation.md") operation of the Detective API. To run an investigation using the AWS Command Line Interface (AWS CLI) run the [start-investigation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/start-investigation.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/start-investigation.html") command.

In your request, use these parameters to run an investigation in Detective:

- `GraphArn` – Specify the Amazon Resource Name (ARN) of the behavior graph.
- `EntityArn` – Specify the unique Amazon Resource Name (ARN) of the IAM user and IAM role.
- `ScopeStartTime` – Optionally, specify the data
  and time from which the investigation should begin. The value is an
  UTC ISO8601 formatted string. For example,`2021-08-18T16:35:56.284Z`.
- `ScopeEndTime` – Optionally, specify the data
  and time when the investigation should end. The value is an
  UTC ISO8601 formatted string. For example,`2021-08-18T16:35:56.284Z`.

This example is formatted for
Linux, macOS, or Unix, and it uses the backslash (\) line-continuation
character to improve readability.

```
aws detective start-investigation \
--graph-arn ``arn:aws:detective:us-east-1:123456789123:graph:fdac8011456e4e6182facb26dfceade0`` --entity-arn ``arn:aws:iam::123456789123:role/rolename`` --scope-start-time ``2023-09-27T20:00:00.00Z``
--scope-end-time ``2023-09-28T22:00:00.00Z``
```

You can also run an investigation from the following pages in Detective:

- An IAM user or IAM role profile page in Detective.
- Graph visualization pane of a finding group.
- Actions column of an involved resource.
- IAM user or IAM role on a finding page.
  After Detective runs the investigation for a resource, an investigation report is generated.
  To access the report, go to **Investigations** from the navigation
  pane.
