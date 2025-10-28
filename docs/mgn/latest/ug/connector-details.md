NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Review details about your MGN connectors

There are several ways you can access the **MGN connector details** view.

Click the **MGN connector name** of any MGN connector to open its details page.

The page includes the following details:

- Overview – View all the information related to the specific MGN connector including state and when it last communicated with AWS Application Migration Service.
- Source servers – This section features all the source servers managed by the MGN connector.
  Each row in the "servers" table provides details about a single source server, including:

- **Hostname** – The source server's hostname.
- **Account** - The source server account id.
- **Prerequisites** – The status of prerequisites verification, with the following options: **Verified**, **Not verified**, **In progress**, or **Invalid**.
- **Agent installed** – Indicates whether the AWS MGN Agent is installed on the server.
- **Credential secret** – The secret of the specific source server.
- **Next step** – What is the new action in the connector installation workflow. Options include:
  - **Initiate test** – Test your source server before migration.
  - **Mark as tested** – Mark that the source server is ready for migration.
  - **Check prerequisites** – Ensure that the source server meets the required prerequisites.
  - **Wait for check to complete** – This indicates that the prerequisites are being verified. If this step is completed successfully, the next step will be **Install agent**. If not, the next step will be **Resolve cause of invalidity**.
  - **Resolve cause of invalidity** – This indicates that the prerequisite verification process failed and that a specific issue needs to be resolved.

- Tags - This section features the tags associated with your connector.
