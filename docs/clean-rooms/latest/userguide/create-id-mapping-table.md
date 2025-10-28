# Creating and populating a new ID mapping

table

**Prerequisites**

Before creating an ID mapping table, ensure you have:

- An associated ID namespace source and target
- The ID namespaces configured for either rule-based ID mapping or provider services
  ID mapping
  You can create two types of ID mapping tables:

- Rule-based – Uses matching rules to translate first-party data
- Provider services – Uses LiveRamp to translate RampIDs
  After you create an ID mapping table, you can either populate it immediately by running
  an ID mapping workflow, or you can wait to populate the table later.

After the ID mapping table is successfully populated, you can then run a multi-table join
query on the ID mapping table to join the `sourceId` with the
`targetId` and analyze the data.

###### Topics

- [Create an ID mapping table
  (rule-based)](#create-id-mapping-table-rule-based "#create-id-mapping-table-rule-based")
- [Create an ID mapping table
  (provider services)](#create-id-mapping-table-provider-services "#create-id-mapping-table-provider-services")

## Create an ID mapping table

(rule-based)

This topic describes the process of creating an ID mapping table that uses matching
rules to translate first-party data from a source to a target.

When you create a rule-based ID mapping table, you can choose to process only new,
updated, or deleted records in the workflow by turning on incremental processing.

###### To create and populate a new ID mapping table using the rule-based method

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms/](https://console.aws.amazon.com/cleanrooms/ "https://console.aws.amazon.com/cleanrooms/").
2. In the navigation pane, choose **Collaborations**.
3. Choose the collaboration, and then choose the **Entity
   resolution** tab.
4. Choose **Create ID mapping table**.
5. Under **ID mapping settings**, do one of the
   following:
   - To create a new workflow, keep **Create a new ID mapping
     workflow** selected.
   - To use an existing workflow, clear the checkbox and select a workflow
     from the dropdown list, then skip to step 9.

6. Under **Identity data**, view or configure the source and
   target.
   - For a single ID namespace pair: Review the pre-selected
     **Source** and **Target**.
   - For multiple ID namespaces: Select the **Source** and
     **Target** from the dropdown lists.

7. (Optional) Select **Turn on incremental processing** to
   process only new, updated, or deleted records in the workflow.

AWS Entity Resolution processes only new, updated, or deleted records in either the Source or
Target ID namespace, rather than recreating the entire ID mapping table.

If you leave this option unselected, AWS Entity Resolution runs the default batch processing ID
mapping workflow on the ID mapping table. 8. Under **Rule parameters**, configure the following:

    * **Rule controls** – Choose whether the
     **Target** or **Source** provides
     matching rules.


    You can view the rules by turning on **Show
     rules**.


    Rule controls must be compatible between the source and the target ID
     namespace to be used in an ID mapping workflow. For example, if a source
     ID namespace limits rules to the target but the target ID namespace
     limits rules to the source, this results in an error.
    * **Comparison type** is automatically set to
     **Multiple input fields.**


    This is because both participants had selected this option previously.
    * **Record matching**




    	+ **One source to one target** – Stores
    	 one matching record per target
    	+ **Many sources to one target** –
    	 Stores all matching records per target


    	###### Note

    	The limitations specified for the source and target ID
    	 namespaces must be compatible.

9. For **ID mapping details**, configure the following:
   1. Enter an **ID mapping table name** or keep the
      default name.
   2. (Optional) Enter a **Description** of the ID mapping
      table.

   The description helps with writing queries.

10. For **AWS Clean Rooms access**, choose one:
    - **Allow AWS Clean Rooms to add and manage permission policy**
      – Creates a service role automatically.
    - **Add and manage permissions manually** –
      Either review and modify the resource policy or choose **Add
      policy statement**.

    ###### Note

    If you can’t modify the role policy, you receive an error message
    stating that AWS Clean Rooms couldn't find the policy for the service
    role.

11. For **AWS Entity Resolution access**, choose one:

This section is only visible if you're creating a new ID mapping table.

    * **Create and use a new service role**




    	+ The default Service role name is
    	 `entityresolution-id-mapping-workflow-<timestamp>`
    	+ (Optional) For encrypted data, select **This data is
    	 encrypted by a KMS key** and enter the
    	 **AWS KMS key**.
    * **Use an existing service role**




    	+ Choose an **Existing service role name** from
    	 the dropdown list or enter a role ARN.


    	The list of roles are displayed if you have permissions to
    	 list roles.


    	View the service role by choosing the **View in
    	 IAM** external link.


    	If there are no existing service roles, the option to
    	 **Use an existing service role** is
    	 unavailable.


    	By default, AWS Clean Rooms doesn't attempt to update the existing
    	 role policy to add necessary permissions.
    	+ (Optional) Select **Add a pre-conﬁgured policy with
    	 necessary permissions to this role** to attach
    	 necessary permissions to the role.


    	You must have permissions to modify roles and create
    	 policies.

12. (Optional) Under **Additional settings**, configure:
    1.  **ID mapping table settings**
        - To enable custom encryption, choose **Customize
          encryption settings** and enter an AWS KMS
          key.

        ###### Note

        This KMS key needs to grant the required permissions to
        use within AWS Entity Resolution to `cleanrooms.amazonaws.com`
        using a KMS key policy. For more details about the
        required permissions for working with encryptions with an ID
        mapping workflow, see [Create a workflow job role for AWS Entity Resolution](../../../entityresolution/latest/userguide/create-workflow-job-role.md "../../../entityresolution/latest/userguide/create-workflow-job-role.md") in the
        _AWS Entity Resolution User
        Guide_.
        - To add tags, choose **Add new tag** and enter
          key-value pairs

    2.  **ID mapping workflow settings** (new workflows
        only):
        - To use different names, clear **Keep the same ID
          mapping table name and description** and enter new
          values.
        - To add tags, choose **Add new tag** and enter
          key-value pairs

13. Choose one of the following:

        * **Create ID mapping table** – Creates an empty
         table you can populate later ([Populating an existing ID mapping table](populate-id-mapping-table.md "populate-id-mapping-table.md"))
        * **Create and populate ID mapping table** –
         Creates and immediately populates the table (may take several
         hours)

    The ID mapping workflow process begins. During this process, the ID mapping
    table is populated with translated IDs. The ID mapping workflow might take a few
    hours to process.

After the ID mapping table is successfully populated, you can [query the ID mapping table](query-id-mapping-tables.md "query-id-mapping-tables.md") to join the `sourceId` with
the `targetId` and analyze the data.

## Create an ID mapping table

(provider services)

This topic describes the process of creating an ID mapping table that uses a provider
service (LiveRamp). The LiveRamp provider services translates a set of source RampIDs to
another using either maintained or derived RampIDs.

###### To create a new ID mapping table using the provider services method

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms/](https://console.aws.amazon.com/cleanrooms/ "https://console.aws.amazon.com/cleanrooms/").
2. In the navigation pane, choose **Collaborations**.
3. Choose the collaboration, and then choose the **Entity
   resolution** tab.
4. Choose **Create ID mapping table**.
5. Under **ID mapping settings**, do one of the
   following:
   - To create a new workflow, keep **Create a new ID mapping
     workflow** selected.
   - To use an existing workflow, clear the checkbox and select a workflow
     from the dropdown list, then skip to step 9.

6. Under **Identity data**, view or configure the source and
   target.
   - For a single ID namespace pair: Review the pre-selected
     **Source** and **Target**.
   - For multiple ID namespaces: Select the **Source** and
     **Target** from the dropdown lists.

7. Under **Method**, verify that the selected ID mapping
   workflow method is **LiveRamp transcoding**.
8. For **LiveRamp conﬁgurations**, do one of the
   following:
   - Enter the **LiveRamp ID manager ARN** and
     **LiveRamp secret manager ARN**.
   - Choose **Import from existing workflow**.

9. For **ID mapping details**, configure the following:
   1. Enter an **ID mapping table name** or keep the
      default name.
   2. (Optional) Enter a **Description** of the ID mapping
      table.

   The description helps with writing queries.

10. For **AWS Clean Rooms access**, choose one:
    - **Allow AWS Clean Rooms to add and manage permission policy**
      – Creates a service role automatically.
    - **Add and manage permissions manually** –
      Either review and modify the resource policy or choose **Add
      policy statement**.

    ###### Note

    If you can’t modify the role policy, you receive an error message
    stating that AWS Clean Rooms couldn't find the policy for the service
    role.

11. For **AWS Entity Resolution access** choose one:

This section is only visible if you're creating a new ID mapping table.

    * **Create and use a new service role**




    	+ The default Service role name is
    	 `entityresolution-id-mapping-workflow-<timestamp>`
    	+ (Optional) For encrypted data, select **This data is
    	 encrypted by a KMS key** and enter the
    	 **AWS KMS key**.
    * **Use an existing service role**




    	+ Choose an **Existing service role name** from
    	 the dropdown list or enter a role ARN.


    	The list of roles are displayed if you have permissions to
    	 list roles.


    	View the service role by choosing the **View in
    	 IAM** external link.


    	If there are no existing service roles, the option to
    	 **Use an existing service role** is
    	 unavailable.


    	By default, AWS Clean Rooms doesn't attempt to update the existing
    	 role policy to add necessary permissions.
    	+ (Optional) Select **Add a pre-conﬁgured policy with
    	 necessary permissions to this role** to attach
    	 necessary permissions to the role.


    	You must have permissions to modify roles and create
    	 policies.

12. (Optional) Under **Additional settings** configure:
    1.  **ID mapping table settings**
        - To enable custom encryption, choose **Customize
          encryption settings** and enter an AWS KMS
          key.

        ###### Note

        This KMS key needs to grant the required permissions to
        use within AWS Entity Resolution to `cleanrooms.amazonaws.com`
        using a KMS key policy. For more details about the
        required permissions for working with encryptions with an ID
        mapping workflow, see [Create a workflow job role for AWS Entity Resolution](../../../entityresolution/latest/userguide/create-workflow-job-role.md "../../../entityresolution/latest/userguide/create-workflow-job-role.md") in the
        _AWS Entity Resolution User
        Guide_.
        - To add tags, choose **Add new tag** and enter
          key-value pairs.

    2.  **ID mapping workflow settings** (new workflows
        only):
        - To use different names, clear **Keep the same ID
          mapping table name and description** and enter new
          values.
        - To add tags, choose **Add new tag** and enter
          key-value pairs.

13. Choose one of the following:

        * **Create ID mapping table** – Creates an empty
         table you can populate later ([Populating an existing ID mapping table](populate-id-mapping-table.md "populate-id-mapping-table.md"))
        * **Create and populate ID mapping table** –
         Creates and immediately populates the table (may take several
         hours)

    The ID mapping workflow process begins. During this process, the ID mapping
    table is populated with translated IDs. The ID mapping workflow might take a few
    hours to process.

After the ID mapping table is successfully populated, you can [query the ID mapping table](query-id-mapping-tables.md "query-id-mapping-tables.md") to join the `sourceId` with
the `targetId` and analyze the data.
