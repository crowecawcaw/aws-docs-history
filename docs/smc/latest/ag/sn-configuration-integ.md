

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Configuring system properties, aggregators, and custom resources
<a name="sn-configuration-integ"></a>

This version of the AWS Service Management Connector enables ServiceNow administrators to configure system properties, Config Aggregators, and AWS Config custom resources from select ServiceNow tables.

**To configure the new AWS Config integration System properties**

1. In the navigator, enter **AWS Service Management**.

1. Choose **System Properties**, and then choose **AWS Config**. 

1. Review the available settings and recommendations in the table below.


<table>
<thead>
  <tr><th>Available settings </th><th>Description </th></tr>
</thead>
<tbody>
  <tr><td>The name of the S3 bucket from where to get the resource provider ZIP files</td><td>The S3 bucket for custom resources from ServiceNow that populates AWS Config. <br />Default and hard coded value: <code>cmdb-resource-providers</code> Service Management Connector recommends that you do not change this setting.  </td></tr>
  <tr><td>Name of the Discovery source for synchronization with AWS Config</td><td>The setting that correlates the Discovery source in ServiceNow. <br />Default and hard coded value: AWS Service Management Connector Service Management Connector recommends you do not change this setting.  </td></tr>
  <tr><td>What field to use for correlation ID </td><td>Administrators use this setting to specify which column contains the correlation ID for each AWS Config.<br />The correlation ID disambiguates AWS Config item that might have the same resource ID (such as SQS queues). It consists of the comma separated string of: <ul><li> Source account number  </li><li> Source Region  </li><li> Resource type, such as AWS::EC2::Instance </li><li> Resource ID  </li></ul><br />Default: <code>correlation_id</code> </td></tr>
  <tr><td>What field to use for AWS capture time </td><td>Administrators use this setting to specify which column contains the capture time (such as capture time from AWS Config) for each AWS Config item. <br />Default: <code>last_discovered</code> </td></tr>
  <tr><td>What field to use for last sync time </td><td>Administrators use this setting to specify which column contains the last sync time (such as the last time AWS Config integration performed a synchronization for a given item) for each AWS Config item. <br />Default: <code>checked_in</code> </td></tr>
  <tr><td>Enable the creation of a relationship for state sync </td><td>Administrators use this setting to enable the creation of a relationship to a special <i>state sync</i> configuration item. <br />When enabled, each synchronized item links to a particular state sync, or execution. By enabling this feature, it allows the SMC to identify stale items. <br /><b>Warning</b>: This action creates an additional relationship per synchronized item. Depending on the number of items, it might have a performance impact.<br />Default: No</td></tr>
  <tr><td>Enable the deletion of the previous relationship for state sync </td><td>Administrators use this setting to enable the deletion of previous relationships to a special <i>state sync </i>configuration item. <br />When enabled, a successful synchronization to a given AWS Config time deletes the previous relationships to state sync configuration item.<br /><b>Warning:</b> This action performs <code>GlideAggregate</code> queries for each group of synchronized accounts, Regions, or Aggregators. Depending on the number of items, it might have a performance impact. <br />Default: No </td></tr>
  <tr><td>What <i>Install status</i> to put stale config item into </td><td>Administrators use this setting to automatically change the <i>install_status</i> of configuration items identified as stale. <br />This action ensures that the status of stale resources correctly updates when using an Aggregator. Be aware this feature works only if you set <i>What field to use for last sync time</i> and enable <i>Enable the creation of a relationship for state sync</i>. <br />Allowed values:<ul><li> Installed  </li><li> Retired  </li><li> Absent  </li><li> Do nothing  </li></ul><br />Default: Do nothing </td></tr>
  <tr><td>Interval in minutes between the execution of full Config synchronization</td><td>Administrators use this setting to control the time between full syncs of Config data. The default is 720 minutes or 12 hours.</td></tr>
  <tr><td>Use MTM for managing stale status</td><td>This setting ensures the use of separate tables for handing relationships for sync status instead of using the <code>cmdb_rel_ci</code> table. AWS Service Management Connector recommends using the default setting.<br />Default: Yes</td></tr>
</tbody>
</table>
