

# Access Connect Customer data lake
<a name="access-datalake"></a>

To access the data lake, you can use the AWS console, the [AWS Command Line Interface](https://aws.amazon.com/cli/) or [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html). AWS CloudShell is a browser-based, pre-authenticated shell that you can launch directly from the AWS Management Console. 

There are two ways to access the analytics data lake and configure data to be shared: 
+ [Option 1: Use the Connect Customer console](#option1-configure-data-to-be-shared)
+ [Option 2: Use CLI or CloudShell](#option2-configure-data-to-be-shared)

If you are unable to access the scheduling tables by using Option 1, try using Option 2.

## Option 1: Use the Connect Customer console
<a name="option1-configure-data-to-be-shared"></a>

1. Open the Connect Customer console at [https://console.aws.amazon.com/connect/](https://console.aws.amazon.com/connect/).

1. On the instances page, choose the instance alias. The instance alias is also your instance name, which appears in your Connect Customer URL. The following image shows the Connect Customer virtual contact center instances page, with a box around the instance alias.  
![The Connect Customer virtual contact center instances page.](http://docs.aws.amazon.com/connect/latest/adminguide/images/access-datalake-configure-data-option1-1.png)

1. On the left navigation menu, choose **Analytics Tools** and then choose **Add data share**.  
![The Connect Customer analytics tools page.](http://docs.aws.amazon.com/connect/latest/adminguide/images/access-datalake-configure-data-option1-2.png)

1. For the **Target AWS account ID** specify the AWS account ID of the account from which you wish to access data (consumer). This can be the same AWS account as hosts your Connect Customer instance or a different AWS account. Select one or multiple data types you wish to access from the consumer account and select **Confirm**.  
![The Connect Customer analytics tools Add data share page.](http://docs.aws.amazon.com/connect/latest/adminguide/images/access-datalake-configure-data-option1-3.png)

## Option 2: Use CLI or CloudShell
<a name="option2-configure-data-to-be-shared"></a>

1. Generate the `generate Association api` request file by running the `aws connect batch-associate-analytics-data-set --generate-cli-skeleton input > input_batch_association.json` command.

1. Open the JSON file in a text editor and enter the following:
   + **Instance ID** – Your Connect Customer instance ID.
   + **DataSetID** – Enter the required tables. For more information about required tables, see [Associate tables for the Connect Customer analytics data lake](datalake-tables.md).
   + **TargetAccountId** – Account ID to share data.

   Each value in `DataSetIds` is a data lake table name, such as `contact_record`. The following JSON file shows a subset of tables as an example. For more information about table names that you can use as `DataSetIds`, see [Data type definitions for the Connect Customer data lake](data-type-definitions.md).

   ```
   {
   "InstanceId": your_instance_id,
   "DataSetIds": [
     "contact_record",
     "contact_flow_events",
     "contact_statistic_record",
     "contact_lens_conversational_analytics",
     "agent_queue_statistic_record",
     "agent_statistic_record",
     "contact_evaluation_record"
   ],
   "TargetAccountId": your_account_ID
   }
   ```

1. Associate the data lake to a single account by running the `aws connect batch-associate-analytics-data-set --cli-input-json file:///path/to/request/file` command (where this path is based on the location of the JSON file).