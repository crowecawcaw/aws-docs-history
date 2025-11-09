# Configuring AWS tags for provisioned

products

The AWS Service Management Connector enables ServiceNow administrators to add
tags (metadata) to provisioned products globally across the scoped app or granularly
at the portfolio level. These tags are not visible to end users.

Three tag types are available in this release:

- Generic tags in which the administrator can enter the key and
  value.
- ServiceNow Request Item tags in which the admin can enter the syntax for
  Key and Value in the table below.
- ServiceNow table(s) values that end users can select as tags for
  provisioned AWS resources. This release now enables administrators to
  identify any ServiceNow tables, such as Cost center or Department, and makes
  values from that table selectable for end users.

###### Note

Generic tags (from administrators) and ServiceNow Request Item tags
are not viewable by end users.

| Key                   | Value             |
| --------------------- | ----------------- |
| Requested Item Number | ${REQUEST_NUMBER} |
| User                  | ${USERNAME}       |
| Requested for         | ${REQUESTED_FOR}  |
| Opened by             | ${OPENED_BY}      |

###### To add generic AWS tags to Service Catalog provisioned products in ServiceNow

1. In the AWS Service Management scoped app, choose **Setup**, then the **Automated
   Tags** module.
2. Choose **New**.
3. For Global tags, enter the Key and Value entries and choose
   **Submit**.
4. For Portfolio tags, deselect **Global check**. The
   **Portfolio** field appears.

Choose the Service Catalog portfolio, enter the Key and Value entries, and choose
**Submit**.

###### To add in-scope ServiceNow request item AWS tags to Service Catalog provisioned

products derived from ServiceNow

1. In the AWS Service Management scoped app, choose **Setup**, then the **Automated
   Tags** module.
2. Choose **New**.
3. For Global tags, enter the specific Key and Value entries for either User
   or Request Item Number, and choose **Submit**.
4. For Portfolio tags, deselect **Global
   check**. The Portfolio field appears. Select the AWS Service Catalog
   portfolio, enter the Key and Value entries, and choose **Submit**.

###### To add tags to AWS provisioned products from ServiceNow tables and fields

that are selectable by end users

1. In the AWS Service Management scoped app, choose **Setup**, then the **Automated
   Tags** module.
2. Choose **New**.
3. Choose **Selectable by End User**.
4. Choose a table from the dropdown list: **Table
   Name**.
5. Choose a field from the dropdown list: **Table
   Field**.
6. [Optional] Add a filter for the table selected using the **Table Filter** field.
7. For Global tags, enter the Key and Value entries and choose **Submit**.
8. For Portfolio tags, deselect **Global
   check**. The **Portfolio** field
   appears.

Select the AWS Service Catalog portfolio, enter the Key and Value entries, and choose
**Submit**.

The ServiceNow table and field value appear on the AWS Product
(ServiceNow catalog item). It is a required value prior to ordering. After
product provisioning, you can see in the AWS console that these tags
associate with the resource.
