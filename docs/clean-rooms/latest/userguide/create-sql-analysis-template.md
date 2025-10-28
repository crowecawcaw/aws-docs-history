# Creating a SQL analysis template

**Prerequisites**

Before you create a SQL analysis template, you must have:

- An active AWS Clean Rooms collaboration
- Access to at least one configured table in the collaboration

For information about configuring tables in AWS Clean Rooms, see [Creating a configured table in
AWS Clean Rooms](create-configured-table.md "create-configured-table.md").

- Permissions to create analysis templates
- Basic knowledge of SQL query syntax
  The following procedure describes the process of creating a SQL analysis template using
  the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home").

For information about how to create a SQL analysis template using the AWS SDKs, see
the [AWS Clean Rooms
API Reference](../apireference/Welcome.md "../apireference/Welcome.md").

###### To create a SQL analysis template

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home") with the AWS account that will function as the
   collaboration creator.
2. In the left navigation pane, choose **Collaborations**.
3. Choose the collaboration.
4. On the **Templates** tab, go to the **Analysis templates
   created by you** section.
5. Choose **Create analysis template**.
6. On the **Create analysis template** page, for
   **Details**,
   1. Enter a **Name** for the analysis template.
   2. (Optional) Enter a **Description**.
   3. For **Format**, leave the **SQL** option
      selected.

7. For **Tables**, view the configured tables associated with the
   collaboration.
8. For **Definition**,
   1. Enter the definition for the analysis template.
   2. Choose **Import from** to import a definition.
   3. (_Optional_) Specify a parameter in the SQL
      editor by entering a colon (`:`) in front of the parameter name.

   For example:

   `WHERE table1.date + :date_period > table1.date`

9. If you added parameters previously, under **Parameters –
   optional**, for each **Parameter name**, choose the
   **Type** and **Default value** (optional).
10. If you want to enable **Tags** for the conﬁgured table resource,
    choose **Add new tag** and then enter the **Key** and
    **Value** pair.
11. Choose **Create**.
12. You are now ready to inform your collaboration member that they can [Review an analysis template](review-analysis-template.md "review-analysis-template.md"). (Optional if
    you want to query your own data.)
