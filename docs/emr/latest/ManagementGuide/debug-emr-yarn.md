# Debugging EMR steps Using YARN application IDs

One effective way to debug steps that launch YARN-based applications (such as Spark steps) is to leverage the Yarn Application ID
information available in the Amazon EMR console.

## YARN application ID

For steps that run Spark or other YARN-based jobs, The EMR console shows the most recently executed YARN Application ID in the step details. If a step launches
multiple YARN applications, only the last executed Application ID is displayed.

Why use Yarn application IDs for debugging?

- _You can directly correlate EMR steps to Yarn applications_: Identify exactly which Yarn application corresponds to a
  problematic or interesting step.
- _You can access live monitoring tools_: Use the application ID to open the YARN ResourceManager Live UI or the Spark History Server UI to inspect
  running or finished applications.
- _You can retrieve logs for detailed troubleshooting_: Use the application ID to find container logs stored in S3, associated with that application,
  that help you dig deeper into failures or performance issues.
  You can use this information in various ways:

1.  Navigate to the **Steps** tab of your EMR cluster.
2.  Click on the step you want to debug.
3.  Locate the **Yarn Application ID** section in the step details panel.
4.  Copy the application ID provided.
5.  Use the ID to:

        * Open the YARN ResourceManager Live UI. The URI appears like the following: **http://`resourcemanager-host`:8088/cluster/app/`application_id`**
        * Open the Spark History Server UI to review application execution details.
        * Access container logs in your S3 bucket under paths tagged by the application ID.

    By using Yarn application ID, you can streamline your debugging process and connect high-level EMR step failures to the underlying Yarn
    application executions.
