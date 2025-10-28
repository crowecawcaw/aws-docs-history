# Creating and associating a new ID namespace

Each member of the collaboration must create and associate either an ID namespace
**Source** or an ID namespace **Target** before creating
an ID mapping table to query identity data.

If you have already created an ID namespace in AWS Entity Resolution, skip to [Associating an existing ID namespace](associate-existing-id-namespace.md "associate-existing-id-namespace.md").

###### To create and associate a new ID namespace

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms/](https://console.aws.amazon.com/cleanrooms/ "https://console.aws.amazon.com/cleanrooms/").
2. In the left navigation pane, choose **Collaborations**.
3. Choose the collaboration.
4. On the **Entity resolution** tab, choose **Associate ID
   namespace**.
5. On the **Associate ID namespace** page, for **Entity
   resolution data**, choose **Create ID namespace**.

The AWS Entity Resolution console appears in a new tab. 6. Follow the prompts on the **Create ID namespace** page in the AWS Entity Resolution
console.

    1. For **Details**, enter the **ID namespace
     name**, **Description**, and select the **ID
     namespace type** (either **Source** or
     **Target**).
    2. For the **ID namespace method**, choose either the
     **Rule-based** method for rule-based matching or **Provider
     services** for third-party transcoding.
    3. Specify the **Data input type**, depending on the ID namespace
     method you've chosen.
    4. Choose **Create ID namespace**.

7. Go back to the AWS Clean Rooms console.
8. On the **Associate ID namespace** page, for **Entity
   resolution data**, choose the **AWS Entity Resolution ID namespace** source or
   target that you want to associate with the collaboration from the dropdown list.
9. For **Association details**, take the following steps.
   1. Enter a **Name** for the associated ID namespace.

   You can use the default name or rename this ID namespace. 2. (Optional) Enter a **Description** of the ID namespace.

   The description helps with writing queries.

10. Specify the **AWS Clean Rooms access** permissions by selecting an option and
    then taking the recommended action.

| Option                                                                                                                                                                 | Recommended action                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Allow AWS Clean Rooms to add and manage permission policy**                                                                                                          | AWS Clean Rooms creates a service role with the required policy for this association.                                                                                                                                                                                                                                                                                                       |
| **Add and manage permissions manually**                                                                                                                                | Do one of the following: <br>• Review the **Resource policy** and add necessary permissions to the policy. <br>• Use an existing policy by choosing **Add policy statement**.You must have permissions to modify roles and create policies.NoteIf you can’t modify the role policy, you receive an error message stating that AWS Clean Rooms couldn't ﬁnd the policy for the service role. | 11. (Optional) For **Advanced ID mapping table configurations**, modify the default protections for the column that comes from the ID namepsace. The ID mapping table is configured by default to only allow an `INNER JOIN` on both the `sourceID` column and the `targetID` column. You can modify this configuration so that the column that comes from this ID namespace (either `sourceID` or `targetID`) can be allowed anywhere in the query.                                                                                                                         |
| Your goal                                                                                                                                                              | Recommended option                                                                                                                                                                                                                                                                                                                                                                          |
| ---                                                                                                                                                                    | ---                                                                                                                                                                                                                                                                                                                                                                                         |
| Categorize the column as a "join column" and only allow it in an `INNER JOIN` clause                                                                                   | **Yes**                                                                                                                                                                                                                                                                                                                                                                                     |
| Categorize the column as a "dimension column" and allow it anywhere in the query, including a `JOIN` clause, `SELECT`, `WHERE` and `GROUP BY` statements of the query. | **No, allow anywhere in the query**                                                                                                                                                                                                                                                                                                                                                         | 12. (Optional) If you want to enable **Tags** for the ID namepsace resource, choose **Add new tag** and then enter the **Key** and **Value** pair. 13. Choose **Associate**. 14. On the **Entity resolution** tab, under the **Associated ID namespaces** table, view the associated ID namespace and verify that the ID namespace type is correct (**Source** or **Target**). After all members in the collaboration have associated their ID namespaces, you can [create an ID mapping table](create-id-mapping-table.md "create-id-mapping-table.md") and query the data. |
