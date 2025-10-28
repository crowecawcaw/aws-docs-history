# Create a flow using the AWS console

There are several ways to gets started with creating your first flow by using the AWS console
user interface, AWS CLI commands, APIs, or by specifying CloudFormation resources. The console
enables you to input basic information for your flow and connect as a user of the associated SaaS
application.

###### To create a flow using the console

The following procedure provides the steps to create and configure a flow using the
Amazon AppFlow console user interface.

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. Choose **Create flow**.
3. For **Flow details**, enter a name and description for the flow. A valid
   flow name is a combination of alphanumeric characters and the following special characters:
   !@#.-\_.
4. (Optional) To use a customer managed CMK instead of the default AWS managed CMK, choose
   **Data encryption**, **Customize encryption settings** and
   then select an existing CMK or create a new one.
5. (Optional) To add a tag, choose **Tags**, **Add tag** and
   then enter the key name and value. The following basic restrictions apply to tags:
   - Maximum number of tags per resource – 50
   - For each resource, each tag key must be unique, and each tag key can have only one value.
   - Maximum key length – 128
   - Unicode characters in UTF-8
   - Use letters, numbers, and spaces representable in UTF-8, and the following characters: +
   * = . \_ : / @.
   - Tag keys and values are case-sensitive.
   - The `aws:` prefix is reserved for AWS use. If a tag has a tag key with this
     prefix, then you can't edit or delete the tag's key or value. Tags with the `aws:`
     prefix do not count against your tags per resource limit.

6. Choose **Next**.

###### To configure the flow

1. For **Source details**, select the source and provide the requested
   information. For example, provide connection information and select objects or events. For more
   information, look up your source application on the [Supported source and destination applications](app-specific.md "app-specific.md") page where you can find application-specific connection
   instructions.

###### Note

To successfully configure a connection for a flow, the user or role you use to create the
flow must have permission to use the `UseConnectorProfile` permission-only action
for the connection (connectorprofile) that you choose for the flow. This permission is included
in the AmazonAppFlowFullAccess managed policy. If you are using a custom policy, you must add
the permission to the policy and specify the connectorprofile resource in the policy. 2. For **Destination details**, select the destination and provide the
requested information about the location. For more information, look up your destination
application on the [Supported source and destination applications](app-specific.md "app-specific.md") page where you
can find application-specific connection instructions. 3. For **Flow trigger**, choose how to trigger the flow. The following are
the flow trigger options:

    * **Run on demand** - Run the flow manually.
    * **Run on event** - Run the flow based on the specified change event.




    	+ This option is available only for SaaS applications that provide change events. You
    	 must choose the event when you choose the source.
    * **Run on schedule** - Run the flow on the specified schedule and
     transfer the specified data.




    	+ You can choose either full or incremental transfer for schedule-triggered flows.
    	+ When you select full transfer, Amazon AppFlow transfers a snapshot of all records at the
    	 time of the flow run from the source to the destination.
    	+ When you select incremental transfer, Amazon AppFlow transfers only the records that have
    	 been added or changed since the last successful flow run. You can also select a timestamp
    	 field to specify how Amazon AppFlow identifies new or changed records. For example, if you have
    	 a **Created Date** timestamp field, choose this to instruct Amazon AppFlow to
    	 transfer only newly-created records (and not changed records) since the last successful flow
    	 run. The first flow in a schedule-triggered flow will pull 30 days of past records at the
    	 time of the first flow run.
    	+ The scheduling frequency depends on the frequency supported by the source application.

4. Choose **Next**.

###### Tip

Attempting a connection with an expired user login can return a 'status code 400' error. If
you encounter this error, we recommend creating a new connection and deleting the old one, or
using an existing connection with valid credentials. For more information on setting up a
connection, look up your source application on the [Supported source and destination applications](app-specific.md "app-specific.md") page.

###### To map data fields

1. For **Mapping method**, choose how to map the fields and complete the
   field mapping. The following are the field mapping options:
   - **Manually map fields** - Use the Amazon AppFlow user interface to specify
     the field mapping. To map all fields, choose **Source field name**,
     **Bulk actions**, **Map all fields directly**. Otherwise,
     select one or more fields from **Source field name**, **Source
     fields**, and then choose **Map fields directly**.
   - **Upload a .csv file with mapped fields** - Use a comma-separated values
     (CSV) file to specify the field mappings. Each line in the CSV file contains the source field
     name, followed by a comma, which is followed by the destination field name. For more
     information on how to create the CSV file for upload, see the note that follows this
     procedure.

2. (Optional) To add a formula that concatenates fields, select two fields from
   **Mapped fields** and then choose **Add formula**.
3. (Optional) To mask or truncate field values, select one or more fields from
   **Mapped fields** and then choose **Modify values**.
4. (Optional) For **Validations**, add validations to check whether a field
   has bad data. For each field, choose the condition that indicates bad data and what action
   Amazon AppFlow should take when a field in a record is bad.
5. Choose **Next**.

###### Tip

When manually mapping between a source and destination, you must select compatible fields
and be sure not to exceed the number of records supported by the destination. For more
information on supported record quotas, see [Quotas for Amazon AppFlow](service-quotas.md "service-quotas.md") in the
_Amazon AppFlow User Guide_.

###### Note

When creating a CSV file to upload to Amazon AppFlow, you must specify each source field and
destination field pair in a single line separated by a comma. For example, if you want to map
source fields SF1, SF2, and SF3 to destination fields DFa, DFb, and DFc respectively, the CSV
file should contain three lines as follows:

SF1, DFa

SF2, DFb

SF3, DFc

Save your file with a .csv extension and then upload this file to import the mapping into
Amazon AppFlow.

###### To add filters

Specify a filter to determine which records to transfer. Amazon AppFlow enables you to filter
data fields by adding multiple filters and by adding criteria to a filter.

###### Note

When you select field names with string values, OR logic allows you to combine two or more
criteria into a broader condition. When you add multiple filters, AND logic allows you to
combine your filters into a narrower condition.

1. To add a filter, choose **Add filter**, select the field name, select a
   condition, and then specify the criteria.
2. (Optional) To add further criteria to your filter, choose **Add
   criteria**. Depending on the field and the condition, you can add up to 10 criteria per
   filter.
3. (Optional) To add another filter, choose **Add filter** again. You can
   create up to 10 filters to specify which data fields you want to use in your flow. Amazon AppFlow
   will implement each filter in the order in which you specify them, and transfer only the records
   that meet all filter criteria.
4. To remove a filter, choose **Remove** next to the filter.
5. When you are finished adding filters, choose **Next**.

Review the information for your flow. To change the information for a step, choose
**Edit**. When you are finished, choose **Create
flow**.

###### Tip

If the flow creation fails, review the error message and confirm that all required fields
have been entered, and that the user or role you are using has permission to the
`UseConnectorProfile` action for the connection selected for the flow.
