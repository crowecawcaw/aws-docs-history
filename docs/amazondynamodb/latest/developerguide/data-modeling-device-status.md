

# Monitoring device status updates in DynamoDB
<a name="data-modeling-device-status"></a>

This use case talks about using DynamoDB to monitor device status updates (or changes in device state) in DynamoDB.

## Use case
<a name="data-modeling-schema-device-status-use-case"></a>

In IoT use-cases (a smart factory for instance) many devices need to be monitored by operators and they periodically send their status or logs to a monitoring system. When there is a problem with a device, the status for the device changes from *normal* to *warning*. There are different log levels or statuses depending on the severity and type of abnormal behavior in the device. The system then assigns an operator to check on the device and they may escalate the problem to their supervisor if needed.

Some typical access patterns for this system include:
+ Create log entry for a device
+ Get all logs for a specific device state showing the most recent logs first
+ Get all logs for a given operator between two dates
+ Get all escalated logs for a given supervisor
+ Get all escalated logs with a specific device state for a given supervisor
+ Get all escalated logs with a specific device state for a given supervisor for a specific date

## Entity relationship diagram
<a name="data-modeling-schema-device-status-erd"></a>

This is the entity relationship diagram (ERD) we'll be using for monitoring device status updates.

![ERD of device status updates. It shows the entities: Device and Operator.](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/images/DataModeling/DeviceStatus-1-ERD.jpg)


## Access patterns
<a name="data-modeling-schema-device-status-access-patterns"></a>

These are the access patterns we'll be considering for monitoring device status updates.

1. `createLogEntryForSpecificDevice`

1. `getLogsForSpecificDevice`

1. `getWarningLogsForSpecificDevice`

1. `getLogsForOperatorBetweenTwoDates`

1. `getEscalatedLogsForSupervisor`

1. `getEscalatedLogsWithSpecificStatusForSupervisor`

1. `getEscalatedLogsWithSpecificStatusForSupervisorForDate`

## Schema design evolution
<a name="data-modeling-schema-device-status-design-evolution"></a>

**Step 1: Address access patterns 1 (`createLogEntryForSpecificDevice`) and 2 (`getLogsForSpecificDevice`)**

The unit of scaling for a device tracking system would be individual devices. In this system, a `deviceID` uniquely identifies a device. This makes `deviceID` a good candidate for the partition key. Each device sends information to the tracking system periodically (say, every five minutes or so). This ordering makes date a logical sorting criterion and therefore, the sort key. The sample data in this case would look something like this:

![Table to store status of multiple devices. DeviceID is the primary key and status update Date is the sort key.](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/images/DataModeling/DeviceStatus-2-Step1.png)


To fetch log entries for a specific device, we can perform a [query](Query.md) operation with partition key `DeviceID="d#12345"`.

**Step 2: Address access pattern 3 (`getWarningLogsForSpecificDevice`)**

Since `State` is a non-key attribute, addressing access pattern 3 with the current schema would require a [filter expression](Query.FilterExpression.md). In DynamoDB, filter expressions are applied after data is read using key condition expressions. For example, if we were to fetch warning logs for `d#12345`, the query operation with partition key `DeviceID="d#12345"` will read four items from the above table and then filter out the one item without the *warning* status. This approach is not efficient at scale. A filter expression can be a good way to exclude items that are queried if the ratio of excluded items is low or the query is performed infrequently. However, for cases where many items are retrieved from a table and the majority of the items are filtered out, we can continue evolving our table design so it runs more efficiently.

Let's change how to handle this access pattern by using [composite sort keys](data-modeling-blocks.md#data-modeling-blocks-composite). You can import sample data from [DeviceStateLog\_3.json](https://github.com/aws-samples/amazon-dynamodb-design-patterns/blob/master/examples/device-state-log/json/DeviceStateLog_3.json) where the sort key is changed to `State#Date`. This sort key is the composition of the attributes `State`, `#`, and `Date`. In this example, `#` is used as a delimiter. The data now looks something like this: 

![Status update data for the device, d#12345, fetched using the composite sort key State#Date.](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/images/DataModeling/DeviceStatus-3-Step2.png)


To fetch only warning logs for a device, the query becomes more targeted with this schema. The key condition for the query uses partition key `DeviceID="d#12345"` and sort key `State#Date begins_with “WARNING”`. This query will only read the relevant three items with the *warning* state.

**Step 3: Address access pattern 4 (`getLogsForOperatorBetweenTwoDates`)**

You can import [DeviceStateLog\_4.json](https://github.com/aws-samples/amazon-dynamodb-design-patterns/blob/master/examples/device-state-log/json/DeviceStateLog_4.json)D where the `Operator` attribute was added to the `DeviceStateLog` table with example data.

![DeviceStateLog table design with Operator attribute to get an operator's logs between specific dates.](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/images/DataModeling/DeviceStatus-4-Step3.png)


Since `Operator` is not currently a partition key, there is no way to perform a direct key-value lookup on this table based on `OperatorID`. We’ll need to create a new [item collection](WorkingWithItemCollections.md) with a global secondary index on `OperatorID`. The access pattern requires a lookup based on dates so Date is the sort key attribute for the [global secondary index (GSI)](GSI.md). This is what the GSI now looks like:

![GSI design with OperatorID and Date as partition key and sort key to get logs for a specific operator.](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/images/DataModeling/DeviceStatus-5-Step3.png)


For access pattern 4 (`getLogsForOperatorBetweenTwoDates`), you can query this GSI with partition key `OperatorID=Liz` and sort key `Date` between `2020-04-11T05:58:00` and `2020-04-24T14:50:00`.

![Querying on GSI using OperatorID and Date to get logs for an operator between two dates.](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/images/DataModeling/DeviceStatus-6-GSI1_1.png)


**Step 4: Address access patterns 5 (`getEscalatedLogsForSupervisor`) 6 (`getEscalatedLogsWithSpecificStatusForSupervisor`), and 7 (`getEscalatedLogsWithSpecificStatusForSupervisorForDate`)**

We’ll be using a [sparse index](data-modeling-blocks.md#data-modeling-blocks-sparse-index) to address these access patterns.

Global secondary indexes are sparse by default, so only items in the base table that contain primary key attributes of the index will actually appear in the index. This is another way of excluding items that are not relevant for the access pattern being modeled.

You can import [DeviceStateLog\_6.json](https://github.com/aws-samples/amazon-dynamodb-design-patterns/blob/master/examples/device-state-log/json/DeviceStateLog_6.json) where the `EscalatedTo` attribute was added to the `DeviceStateLog` table with example data. As mentioned earlier, not all of the logs gets escalated to a supervisor.

![GSI design with the EscalatedTo attribute to get all the escalated logs for a supervisor.](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/images/DataModeling/DeviceStatus-7-Step4.png)


You can now create a new GSI where `EscalatedTo` is the partition key and `State#Date` is the sort key. Notice that only items that have both `EscalatedTo` and `State#Date` attributes appear in the index.

![GSI design to get all the items with the EscalatedTo and State#Date attributes.](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/images/DataModeling/DeviceStatus-8-Step4.png)


The rest of the access patterns are summarized as follows:

    For access pattern 5 (getEscalatedLogsForSupervisor), you can perform a query on the escalations GSI with partition key EscalatedTo="Sara"   For access pattern 6 (getEscalatedLogsWithSpecificStatusForSupervisor), you can perform a query on the escalations GSI with partition key EscalatedTo="Sara" and sort key State\#Date begins\_with “WARNING”    For access pattern 7 (getEscalatedLogsWithSpecificStatusForSupervisorForDate), you can perform a query on the escalations GSI with partition key EscalatedTo="Sara" and sort key State\#Date begins\_with “WARNING4\#2020-04-27”    

All access patterns and how the schema design addresses them are summarized in the table below:


| Access pattern | Base table/GSI/LSI | Operation | Partition key value | Sort key value | Other conditions/filters | 
| --- | --- | --- | --- | --- | --- | 
| createLogEntryForSpecificDevice | Base table | PutItem | DeviceID=deviceId | State\#Date=state\#date |  | 
| getLogsForSpecificDevice | Base table | Query | DeviceID=deviceId | State\#Date begins\_with "state1\#" | ScanIndexForward = False | 
| getWarningLogsForSpecificDevice | Base table | Query | DeviceID=deviceId | State\#Date begins\_with "WARNING" |  | 
| getLogsForOperatorBetweenTwoDates | GSI-1 | Query | Operator=operatorName | Date between date1 and date2 |  | 
| getEscalatedLogsForSupervisor | GSI-2 | Query | EscalatedTo=supervisorName |  |  | 
| getEscalatedLogsWithSpecificStatusForSupervisor | GSI-2 | Query | EscalatedTo=supervisorName | State\#Date begins\_with "state1\#" |  | 
| getEscalatedLogsWithSpecificStatusForSupervisorForDate | GSI-2 | Query | EscalatedTo=supervisorName | State\#Date begins\_with "state1\#date1" |  | 

## Final schema
<a name="data-modeling-schema-device-status-final-schema"></a>

Here are the final schema designs. To download this schema design as a JSON file, see [DynamoDB Examples](https://github.com/aws-samples/aws-dynamodb-examples/tree/master/schema_design/SchemaExamples) on GitHub.

**Base table**

![Base table design with device status metadata, such as Device ID, State, and Date.](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/images/DataModeling/DeviceStatus-9-Table.png)


**GSI-1**

![GSI-1 design. It shows the primary key and attributes: DeviceID, State#Date, and State.](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/images/DataModeling/DeviceStatus-10-GSI1.png)


**GSI-2**

![GSI-2 design. It shows the primary key and attributes: DeviceID, Operator, Date, and State.](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/images/DataModeling/DeviceStatus-11-GSI2.png)


## Using NoSQL Workbench with this schema design
<a name="data-modeling-schema-device-status-nosql"></a>

You can import this final schema into [NoSQL Workbench](workbench.md), a visual tool that provides data modeling, data visualization, and query development features for DynamoDB, to further explore and edit your new project. Follow these steps to get started:

1. Download NoSQL Workbench. For more information, see [Download NoSQL Workbench for DynamoDB](workbench.settingup.md).

1. Download the JSON schema file listed above, which is already in the NoSQL Workbench model format.

1. Import the JSON schema file into NoSQL Workbench. For more information, see [Importing an existing data model](workbench.Modeler.ImportExisting.md). 

1. Once you've imported into NOSQL Workbench, you can edit the data model. For more information, see [Editing an existing data model](workbench.Modeler.Edit.md).