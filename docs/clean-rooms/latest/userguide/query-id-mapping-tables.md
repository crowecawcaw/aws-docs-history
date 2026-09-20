

# Querying ID mapping tables using the SQL code editor
<a name="query-id-mapping-tables"></a>

The following procedure describes how to run a multi-table join query on the ID mapping table to join the `sourceId` with the `targetId`.

Before you query the ID mapping table, the ID mapping table must be successfully populated.

**To query ID mapping tables using the SQL code editor**

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home).

1. In the left navigation pane, choose **Collaborations**.

1. Choose the collaboration that has **Your member abilities** status of **Run queries**.

1. On the **Analysis** tab, go to the **Analysis** section.
**Note**  
The **Analysis** section only displays if the member who can receive results and the member who is responsible to pay for query compute costs have joined the collaboration as an active member.

1. On the **Analysis** tab, under **Tables**, view the list of ID mapping tables (under **Managed by AWS Clean Rooms**) and their associated analysis rule type (**ID mapping table analysis rule**).
**Note**  
If you don’t see the ID mapping tables that you expect in the list, it might be because the ID mapping tables haven't been successfully populated. For more information, see [Populating an existing ID mapping table](populate-id-mapping-table.md).

1. Build the query by typing the query into the SQL code editor.


<table>
<thead>
  <tr><th>(Optional) If you want to use an example query </th><th>(Optional) If you want to insert a table name</th></tr>
</thead>
<tbody>
  <tr><td> <ol><li> Select the three vertical dots next to the table. </li><li> Under <b>Insert in editor</b>, choose <b>Example JOIN statement</b>.  Inserting an <b>Example JOIN statements</b> appends the query already in the editor.  <br />The example JOIN statement appears.  </li><li> Edit the placeholder values in the query. </li></ol> </td><td> <ol><li> Select the three vertical dots next to a column. </li><li> Under <b>Insert in editor</b>, choose <b>Table name</b>. </li><li> Edit the placeholder values in the query. </li></ol> </td></tr>
</tbody>
</table>


1. Specify the supported **Worker type** and the **Number of workers**. 

   Use the following table to determine the worker type and number of workers you need for your use case.


<table>
<thead>
  <tr><th>Worker type</th><th>vCPU</th><th>Memory (GB)</th><th>Storage (GB)</th><th>Number of workers</th><th>Total Clean Rooms Processing Units (CRPU)</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2"><b>CR.1X</b> (default)</td><td rowspan="2">4</td><td rowspan="2">30</td><td rowspan="2">500</td><td>2</td><td>4</td></tr>
  <tr><td>128</td><td>256</td></tr>
  <tr><td rowspan="2"><b>CR.4X</b></td><td rowspan="2">16</td><td rowspan="2">120</td><td rowspan="2">2000</td><td>2</td><td>16</td></tr>
  <tr><td>32</td><td>256</td></tr>
  <tr><td rowspan="2"><b>CR.8X</b></td><td rowspan="2">32</td><td rowspan="2">244</td><td rowspan="2">2000</td><td>2</td><td>32</td></tr>
  <tr><td>16</td><td>256</td></tr>
</tbody>
</table>

**Note**  
Different worker types and number of workers have associated costs. To learn more about the pricing, see [AWS Clean Rooms pricing](https://aws.amazon.com/clean-rooms/pricing/).

1. Choose **Run**.
**Note**  
You can't run the query if the member who can receive results hasn’t configured the query results settings.

1. View the **Results**.

   For more information, see [Receiving and using analysis results](receive-query-results.md).

1. Continue to adjust parameters and run your query again, or choose the **\+** button to start a new query in a new tab.

**Note**  
AWS Clean Rooms aims to provide clear error messaging. If an error message doesn't have enough details to help you troubleshoot, contact the account team. Provide them with a description of how the error occurred and the error message (including any identifiers). For more information, see [Troubleshooting AWS Clean Rooms](troubleshooting.md).