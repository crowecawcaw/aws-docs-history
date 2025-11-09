# Editing ID namespace associations

As a collaboration member, you can edit the ID namespace associations that you have
created.

###### To edit an ID namespace association

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms/](https://console.aws.amazon.com/cleanrooms/ "https://console.aws.amazon.com/cleanrooms/").
2. In the left navigation pane, choose **Collaborations**.
3. Choose the collaboration.
4. Choose the **Entity resolution** tab.
5. For **Associated ID namespaces**, choose an ID namespace.
6. On the ID namespace details page, scroll down to view the **ID namespace
   association details**.
7. Choose **Edit**.
8. On the **Edit ID namespace associations** page, edit any of the
   following:
   1. For **Association details**, update the **Name** or
      the **Description**.
   2. (Optional) For **Advanced ID mapping table configurations**, modify the
      default protections for the column that comes from the ID namepsace.

   The ID mapping table is configured by default to only allow an `INNER JOIN`
   on both the `sourceID` column and the `targetID` column. You can modify
   this configuration so that the column that comes from this ID namespace (either
   `sourceID` or `targetID`) can be allowed anywhere in the query.

   | Your goal                                                                                                                                                                    | Recommended option                  |
   | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
   | Categorize the column as a "join column" and only allow it in an `INNER<br>JOIN` clause                                                                                      | **Yes**                             |
   | Categorize the column as a "dimension column" and allow it anywhere in the query,<br>including a `JOIN` clause, `SELECT`, `WHERE` and<br>`GROUP BY` statements of the query. | **No, allow anywhere in the query** |

9. Choose **Save changes**.
