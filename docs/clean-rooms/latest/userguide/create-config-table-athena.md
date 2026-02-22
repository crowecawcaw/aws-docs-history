# Creating a configured table –

Amazon Athena data source

The Amazon Athena data source option allows you to query data stored in Amazon S3, cataloged in
the AWS Glue data catalog or federated catalogs, and access controlled via AWS Lake Formation. Both tables and AWS Glue Data Catalog
Views are supported. Lake Formation resource links can be used to share tables and views across
AWS accounts and across AWS Regions to the AWS Clean Rooms member account that joins them to
an AWS Clean Rooms collaboration.

###### Note

Only Amazon S3-based datasets can be queried via the Athena data source
integration.

In this procedure, the [member](glossary.md#glossary-member "glossary.md#glossary-member") does the following tasks:

- Configures an existing table or view in the AWS Glue Data Catalog for use the
  AWS Clean Rooms
- Names the [configured table](glossary.md#glossary-configured-table "glossary.md#glossary-configured-table") and
  chooses which columns to use in the collaboration.
  The following procedure assumes that:

- The collaboration member has already created the AWS Glue Data Catalog database and
  table or GDC view.

###### To create a configured table – Athena data source

1.  Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home").
2.  In the left navigation pane, choose **Tables**.
3.  In the upper right corner, choose **Configure new
    table**.
4.  For **Data source**, under **AWS data
    sources**, choose **Amazon Athena**.
5.  Under **Amazon Athena table**:
    1. Select the **Region** where the Amazon Athena table is
       hosted.

    By default, the current Region (such as N. Virginia
    us-east-1) is selected.

    ###### Warning

    When your Amazon Athena data source is in a different Region than your
    processing location, data processing may occur temporarily outside
    the source Region. Before proceeding, verify that cross-Region data
    movement complies with your data sovereignty requirements,
    regulatory compliance policies, and data governance standards.

    For more information about Regions, see [Regions and Endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") in the
    _AWS General Reference_. 2. Choose the **Catalog** from the dropdown list.

    By default, **AWS Glue Data Catalog** is selected.

        * **AWS Glue Data Catalog** – The default catalog for tables in AWS Glue.
        * **Federated catalog** – Available if you've configured AWS Glue Catalog Federation to connect to remote Apache Iceberg REST catalogs. For more information, see [Catalog federation](../../../lake-formation/latest/dg/catalog-federation.md "../../../lake-formation/latest/dg/catalog-federation.md") in the *AWS Lake Formation Developer Guide*.

    3. Choose the **Database** from the dropdown
       list.
    4. Choose the **Table** that you want to configure from
       the dropdown list.###### Note

To verify that this is the correct table, do either one of the
following:

    * Choose **View in AWS Glue** or **View in AWS Lake Formation** (depending on your catalog type).
    * Turn on **View schema from AWS Glue** to view the
     schema.

6. For **Amazon Athena configurations**,
   1. Choose a **Workgroup** from the dropdown list.
   2. For **S3 output location**, choose a recommended
      action, based on one of the following scenarios.

   | Scenario                                                                 | Recommended action                                                                  |
   | ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------- |
   | Your \*_Workgroup_<br>• doesn’t have a<br>default output location.       | Enter the **S3 output location**<br>or choose **Browse S3**.                        |
   | Your \*_Workgroup_<br>• enforces your<br>default output location.        | The \*_S3 output location_<br>• is<br>automatically chosen and you can't change it. |
   | Your \*_Workgroup_<br>• doesn’t enforce<br>your default output location. | Enter the **S3 output location**<br>or choose **Browse S3**.                        |

7. For **Columns allowed in collaborations**, choose an option
   based on your goal.

| Your goal                                                                            | Recommended option |
| ------------------------------------------------------------------------------------ | ------------------ |
| Allow all columns for use in AWS Clean Rooms (subject to analysis<br>rules)          | **All columns**    |
| Allow one or more columns from the \*_Specify allowed<br>columns_<br>• dropdown list | **Custom list**    |

8. For **Configured table details**,
   1. Enter a **Name** for the configured table.

   You can use the default name or rename this table. 2. Enter a **Description** of the table.

   The description helps differentiate between other configured tables
   with similar names. 3. If you want to enable **Tags** for the configured
   table resource, choose **Add new tag** and then enter
   the **Key** and **Value** pair.

9. Choose **Configure new table**.
   Now that you have created a configured table, you are ready to:

- [Add an analysis rule to the configured
  table](add-analysis-rule.md "add-analysis-rule.md")
- [Associate the configured table to a
  collaboration](associate-configured-table.md "associate-configured-table.md")
