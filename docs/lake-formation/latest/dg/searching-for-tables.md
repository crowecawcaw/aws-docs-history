

# Searching for tables
<a name="searching-for-tables"></a>

You can use the AWS Lake Formation console to search for Data Catalog tables by name, location, containing database, and more. The search results show only the tables that you have Lake Formation permissions on.

**To search for tables (console)**

1. Sign in to the AWS Management Console and open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/).

1. In the navigation pane, choose **Tables**.

1. Position the cursor in the search field. The field has the placeholder text *Find table by properties*.

   The **Properties** menu appears, showing the various table properties to search by.  
![The properties menu is dropped down from the search field and contains these entries: Name, Classification, Database, Location, Catalog ID](http://docs.aws.amazon.com/lake-formation/latest/dg/images/search-for-tables.png)

1. Do one of the following:
   + Search by containing database.

     1. Choose **Database** from the **Properties** menu, and then either choose a database from the **Databases** menu that appears or type a database name and press **Enter**.

        The tables that you have permissions on in the database are listed.

     1. (Optional) To narrow down the list to a single table in the database, position the cursor in the search field again, choose **Name** from the **Properties** menu, and either choose a table name from the **Tables** menu that appears or type a table name and press **Enter**.

        The single table is listed, and both the database name and table name appear as tiles under the search field.  
![Beneath the search field are two tiles: one labeled Database, which includes the selected database name, and one labeled Table, which includes the selected table name. To the right of the tiles is a Clear filter button.](http://docs.aws.amazon.com/lake-formation/latest/dg/images/search-for-tables-with-filter.png)

        To adjust the filter, close either of the tiles or choose **Clear filter**.
   + Search by other properties.

     1. Choose a search property from the **Properties** menu.

        To search by AWS account ID, choose **Catalog ID** from the **Properties** menu, enter a valid AWS account ID (for example, 111122223333), and press **Enter**.

        To search by location, choose **Location** from the **Properties** menu, and select a location from the **Locations** menu that appears. All tables in the root location of the selected location (for example, Amazon S3) are returned.

**Searching tables using AWS CLI**
+ The following example shows how to run a partial serach. The `--search-text` parameter allows you to search for tables that contain the specified text in their metadata. In this case, it returns all tables that have "customer" in their name, description, or other metadata fields.

  ```
  aws glue search-tables 
        --search-text "{{customer}}" 
        --region {{AWS Region}}
        --max-results {{10}}
        --sort-criteria "FieldName=Name,Sort=ASC"
  ```