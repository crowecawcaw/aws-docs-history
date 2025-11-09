# Connect to a Salesforce data

source

###### Note

This data source is for Grafana Enterprise only. For more information,
see [Manage access to Enterprise plugins](upgrade-to-enterprise-plugins.md "upgrade-to-enterprise-plugins.md").

Additionally, in workspaces that support version 9 or newer, this data source might
require you to install the appropriate plugin. For more information, see [Extend your workspace with plugins](grafana-plugins.md "grafana-plugins.md").

The Salesforce data source allows you to visualize data from Salesforce within
Amazon Managed Grafana.

To use this data source, you must have a [Salesforce](https://www.salesforce.com/ "https://www.salesforce.com/") account and a [Salesforce Connected App](https://help.salesforce.com/articleView?id=sf.connected_app_overview.htm&type=5 "https://help.salesforce.com/articleView?id=sf.connected_app_overview.htm&type=5").

## Known limitations

- Ad-hoc filters are not supported yet.
- Only SOQL queries, and data that is accessible via SOQL are currently
  supported. SOSL and SAQL query formats are not yet supported.

## Required settings

The following settings are required.

###### Note

The plugin currently uses the OAuth 2.0 Username-Password Flow. The
required callback URL in the Connected App is not used. Thus, you can set it
to any valid URL.

| Name                                           | Description                                                |
| ---------------------------------------------- | ---------------------------------------------------------- |
| `Enable OAuth settings`                        | You must check this to enable OAuth.                       |
| `Callback URL`                                 | Not used in this plugin, so you can specify any valid URL. |
| `Selected OAuth Scopes (minimum requirements)` | Access and Manage your data (api).                         |
| `Require Secret for Refresh Token Flow`        | You can either enable or disable this.                     |

## Adding the data

source

1. Open the Grafana console in the Amazon Managed Grafana workspace and make sure you
   are logged in.
2. In the side menu under **Configuration** (the gear
   icon), choose **Data Sources**.
3. Choose **Add data source**.

###### Note

If you don't see the **Data Sources** link in
your side menu, it means that your current user does not have the
`Admin` role. 4. Select **Salesforce** from the list of data sources. 5. Enter the following information:

    * For **User Name**, enter the username for the
     Salesforce account that you want to use to connect and query
     Salesforce.
    * For **Password**, enter the password for that
     user.
    * For **Security Token**, enter the security
     token for that user.
    * For **Consumer Key**, enter A Consumer key to
     connect to Salesforce. You can obtain this from your Salesforce
     Connected App.
    * For **Consumer Secret**, enter A Consumer
     secrete to connect to Salesforce. You can obtain this from your
     Salesforce Connected App.
    * For **Use Sandbox**, select this if you want
     to use a Salesforce sandbox.

## Query the Salesforce data source

The query editor supports the modes Query Builder and SOQL Editor. SOQL stands
for [Salesforce Object Query Language](https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql.htm "https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql.htm").

### Query Builder (SOQL

Builder)

Query Builder is a user friendly interface for building SOQL queries. If
you are not familiar with writing SOQL queries, you can use this mode to
build the SOQL to query Salesforce objects. The **FROM**
field in the query builder refers to the entity or entities in Salesforce.
You need to select the **FROM** field before any other
operation in the query builder. After you choose the
**FROM** field, you need to choose the builder mode.
SOQL Builder currently supports the following modes.

- `List`— List the items with their fields from
  the selected table/salesforce. Use this mode to get results such as,
  "Show me list of opportunities created in this fiscal quarter along
  with their name, value, and stage."
- `Aggregate`— Aggregate the items in an entity.
  Use this mode to get results such as,"Count the opportunities
  created in last month." or "What is the total value of the
  opportunities grouped by their stage name?"
- `Trend`— Display the aggregated results over
  time. Use this mode to get results such as, "Count the number of
  opportunities by CreatedDate." or "What is the total sum of value
  grouped by opportunities' closing dates."

After you choose the `Entity/FROM` and the
**mode** in the query editor, build your query using
the following options.

| **Fields** | **Appplicable to** | **Descriptions**                                                                                                                         |
| ---------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| SELECT     | ALL                | Select the list of fields that you want to see. For the<br>aggregate or trend view, also select how you want to<br>aggregate the values. |
| WHERE      | ALL                | (Optional) Specify the filter conditions. The results<br>are filtered based on the conditions that you<br>select.                        |
| ORDER BY   | LIST, AGGREGATE    | (Optional) Select the field name and the sort order that<br>you want for the results.                                                    |
| LIMIT      | LIST, AGGREGATE    | (Optional) Limit the number fo results returned. The<br>default is 100.                                                                  |
| GROUP BY   | AGGREGATE          | (Optional) Select the field if you want to split the<br>aggregated value by any specific field.                                          |
| TIME FIELD | TREND              | Specify the date field by which you want to group your<br>results. Results are filtered based on Grafana's time picker<br>range.         |

s you configure the preceding fields in the query editor, you will also
see a preview of generated SOQL below the query editor. If you are blocked
with any limitations in the query builder, you can safely switch to SOQL
Editor, where you can customize the generated SOQL query.

### SOQL editor

The raw SOQL editor provides the option to query Salesforce objects via
raw a SOQL query. The SOQL editor provides autocomplete suggestions, such as
available entities per tables and corresponding fields. Use Ctrl+Space after
SELECT or WHERE to see the available entities per tables. You can see the
available fields, if you enter a dot after the entity name.

**Shortcuts**

Use CTRL + SPACE to show code completion, which shows available contextual
options.

CMD + S runs the query.

**Query as time series**

Make a time series query by aliasing a date field to time, and a metric
field to metric, then grouping by the metric and date. The following is an
example:

```
SELECT sum(Amount) amount, CloseDate time, Type metric from Opportunity
group by Type, CloseDate
```

**Macros**

To filter by the dashboard time range, you can use Macros in your SOQL
queries:

- `$__timeFrom`— Will be replaced by the start of
  the currently active time selection converted to the
  `time` data type.
- `$__timeTo`— Will be replaced by the end of the
  currently active time selection converted to the `time`
  data type.
- `$__quarterStart`— The start of the fiscal
  quarter (derived from SalesForce Fiscal Year Settings).
- `$__quarterEnd`— The end of the fiscal quarter
  (derived from SalesForce Fiscal Year Settings).

```
SELECT UserId, LoginTime from LoginHistory where LoginTime > $__timeFrom
```

## Templates and variables

To add a new Salesforce query variable, see [Adding a query variable](variables-types.md#add-a-query-variable "variables-types.md#add-a-query-variable"). Use
your Salesforce data source as your data source. You can use any SOQL query
here.

If you want to use name/value pairs, for example a user id and user name,
return two fields from your SOQL query. The first field will be used as the ID.
Do this when you want to filter by key (ID, etc) in your query editor
SOQL.

Use the variable in your SOQL queries by using Variable syntax. For more
information, see [Variable syntax](templates-and-variables.md#variable-syntax "templates-and-variables.md#variable-syntax").
