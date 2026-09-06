

# Creating an intermediate table
<a name="create-intermediate-table"></a>

You can create an intermediate table to cache analysis results for reuse in subsequent queries within a collaboration.

**To create an intermediate table**

1. Open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms/](https://console.aws.amazon.com/cleanrooms/).

1. In the left navigation pane, choose **Collaborations**.

1. Choose the collaboration.

1. Choose the **Tables** tab.

1. From the **Add** dropdown, choose **Create intermediate table**.

1. In **Details**, enter a **Name** for the intermediate table and an optional **Description**.
**Note**  
The name must be unique across all tables, intermediate tables, and ID mapping tables in the collaboration. The name can be up to 100 characters and cannot contain SQL reserved words. The description can be up to 255 characters.

1. In **Details**, choose a **Retention (in days)**. The default retention period is 30 days. This period applies to any active intermediate table version. After a version expires, all stored data is deleted from AWS Clean Rooms. To use the table again, you must repopulate it.

1. In **Dataset**, choose a method to define your intermediate table:
   + **SQL query** – Use the Tables panel to reference available tables, and write a query in the SQL editor.
   + **Analysis template** – Provide the ARN of a PySpark analysis template.

1. In **Encryption**, optionally select **Encrypt secret with a custom KMS key** and provide the KMS key ARN. For more information about the required key policy, see [Encryption for intermediate tables](data-protection.md#encrypt-intermediate-tables).

1. (Optional) Add **Tags** to organize and identify your intermediate table.

1. In **Populate**, optionally select **Populate the intermediate table after creation**.

   If you select this option, configure the following:
   + **Query compute payer** – If your collaboration has multiple query compute payers, select the one that pays for query compute costs for the populate operation.
   + **Worker type** – The instance type for the populate job (default: CR.1X).
   + **Number of workers** – The number of instances to use (2–128, default: 16).
   + (Optional) **Spark properties** – Custom Spark runtime configuration.

1. Choose **Create intermediate table**.

**Note**  
The service creates the intermediate table in CREATED status. The table contains no materialized data until you populate it. If you didn't select the option to populate after creation, you can populate the table later. For more information, see [Populating an intermediate table](populate-intermediate-table.md).