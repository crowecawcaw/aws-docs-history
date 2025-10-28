AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Automation runs in AWS Migration Hub

###### Note

The AWS Migration Hub Automation feature is in preview release. It is available in
US East (N. Virginia). To use this feature, you must set your AWS Region to US East (N. Virginia).
You must also set the AWS Migration Hub home Region to US East (N. Virginia). For instructions on how to
set the AWS Migration Hub home Region, see [.](home-region.md "home-region.md")

This is pre-release documentation. Both the AWS Migration Hub Automation feature and the
documentation are subject to change.

An automation run is an execution of a managed or custom automation unit. You can run the
same automation unit more than once. You can manually specify the same input values or different
input values for the different runs of an automation unit. You can also create duplicate runs. A
duplicate run uses the same input values that you specified for the run from which you created
the duplicate.

###### To start an automation run

1. Sign in to the AWS Management Console and open
   the Migration Hub console at
   [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/ "https://console.aws.amazon.com/migrationhub/").
2. In the left navigation pane, under **Automate**, choose
   **Automation units**.
3. Choose the name of the automation unit that you want to run.
4. On the details page of the automation unit, in the **Service role**
   section, choose **Attach role**.
5. At the top of the page, choose **Run automation**.

###### To view automation runs

1. Sign in to the AWS Management Console and open
   the Migration Hub console at
   [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/ "https://console.aws.amazon.com/migrationhub/").
2. In the left navigation pane, under **Automate**, choose
   **Automation runs**.
3. To see the details of an automation run, choose the name of the run in the table that
   lists all runs.

###### To create a duplicate run

1. Sign in to the AWS Management Console and open
   the Migration Hub console at
   [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/ "https://console.aws.amazon.com/migrationhub/").
2. In the left navigation pane, under **Automate**, choose
   **Automation runs**.
3. Choose the name of the run in the table that lists all runs.
4. On the automation run's details page, choose **Create duplicate
   run**.
