Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Upgrade Studio Runtime

This section contains information about how to upgrade your Studio notebook Runtime. We
recommend that you always upgrade to the latest supported Studio Runtime.

## Upgrade your notebook to a new Studio Runtime

Depending on how you use Studio, the steps to upgrade your Runtime differ. Select
the option that fits your use case.

If you are using SQL or Python without any external dependencies, use the
following Runtime upgrade process. We recommend that you upgrade to the
latest Runtime version. The upgrade process is the same, reardless of the
Runtime version you are upgrading from.

1. Create a new Studio notebook using the latest Runtime.
2. Copy and paste the code of every note from the old notebook to the
   new notebook.
3. In the new notebook, adjust the code to make it compatible with
   any Apache Flink feature that has changed from the previous
   version.
   - Run the new notebook. Open the notebook and run it note by
     note, in sequence, and test if it works.
   - Make any required changes to the code.
   - Stop the new notebook.

4. If you had deployed the old notebook as application:
   - Deploy the new notebook as a separate, new
     application.
   - Stop the old application.
   - Run the new application without snapshot.

5. Stop the old notebook if it's running. Start the new notebook, as
   required, for interactive use.
   **Process flow for upgrading without external
   dependencies**

![The following diagram represents the recommended workflow to upgrade your notebook without external dependencies.](images/MSF-Studio-upgrade-without-dependencies.png)

Follow this process if you are using SQL or Python and using external dependencies such as connectors or custom artifacts, like user-defined functions implemented in Python or Java.
We recommend that you upgrade to the latest Runtime. The process is the same, regardless of the Runtime version that you are upgrading from.

1. Create a new Studio notebook using the latest Runtime.
2. Copy and paste the code of every note from the old notebook to the
   new notebook.
3. Update the external dependencies and custom artifacts.
   - Look for new connectors compatible with the Apache Flink
     version of the new Runtime. Refer to [Table & SQL Connectors](https://nightlies.apache.org/flink/flink-docs-release-1.15/docs/connectors/table/overview/ "https://nightlies.apache.org/flink/flink-docs-release-1.15/docs/connectors/table/overview/") in the Apache Flink
     documentation to find the correct connectors for the Flink
     version.
   - Update the code of user-defined functions to match changes
     in the Apache Flink API, and any Python or JAR dependencies
     used by the user-defined functions. Re-package your updated
     custom artifact.
   - Add these new connectors and artifacts to the new
     notebook.

4. In the new notebook, adjust the code to make it compatible with
   any Apache Flink feature that has changed from the previous
   version.
   - Run the new notebook. Open the notebook and run it note by
     note, in sequence, and test if it works.
   - Make any required changes to the code.
   - Stop the new notebook.

5. If you had deployed the old notebook as application:
   - Deploy the new notebook as a separate, new
     application.
   - Stop the old application.
   - Run the new application without snapshot.

6. Stop the old notebook if it's running. Start the new notebook, as
   required, for interactive use.
   **Process flow for upgrading with external
   dependencies**

![The following diagram represents the recommended workflow to upgrade your notebook with external dependencies..](images/MSF-Studio-upgrade-with-dependencies.png)
