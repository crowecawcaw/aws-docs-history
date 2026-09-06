

# Loading data into Aurora PostgreSQL Limitless Database
<a name="limitless-load"></a>

You can load data into Aurora PostgreSQL Limitless Database tables by using the `COPY` command or by using the data loading utility.

**Note**  
You can load data into standard, sharded, and reference tables.

**Contents**
+ [Using the COPY command with Aurora PostgreSQL Limitless Database](limitless-load.copy.md)
  + [Using the COPY command to load data into Aurora PostgreSQL Limitless Database](limitless-load.copy.md#limitless-load.copy-to)
    + [Splitting data into multiple files](limitless-load.copy.md#limitless-load.copy-split)
  + [Using the COPY command to copy Limitless Database data to a file](limitless-load.copy.md#limitless-load.copy-from)
+ [Using the Aurora PostgreSQL Limitless Database data loading utility](limitless-load.utility.md)
  + [Limitations](limitless-load.utility.md#limitless-load.limitations)
  + [Prerequisites](limitless-load.utility.md#limitless-load.prereqs)
  + [Preparing the source database](limitless-load.utility.md#limitless-load.source)
  + [Preparing the destination database](limitless-load.utility.md#limitless-load.destination)
  + [Creating database credentials](limitless-load.utility.md#limitless-load.users)
    + [Create the source database credentials](limitless-load.utility.md#limitless-load.users.source)
    + [Create the destination database credentials](limitless-load.utility.md#limitless-load.users.destination)
  + [Setting up database authentication and resource access using a script](limitless-load.script.md)
    + [Setup script for the data loading utility](limitless-load.script.md#limitless-load.script.file)
    + [Output from the data loading utility setup script](limitless-load.script.md#limitless-load.script.output)
    + [Cleaning up failed resources](limitless-load.script.md#limitless-load.script.cleanup)
  + [Setting up database authentication and resource access manually](limitless-load.manual.md)
    + [Creating the customer-managed AWS KMS key](limitless-load.manual.md#limitless-load.auth.create-kms)
    + [Creating the database secrets](limitless-load.manual.md#limitless-load.auth.secrets)
    + [Creating the IAM role](limitless-load.manual.md#limitless-load.auth.iam-role)
    + [Updating the customer-managed AWS KMS key](limitless-load.manual.md#limitless-load.auth.update-kms)
    + [Adding the IAM role permission policies](limitless-load.manual.md#limitless-load.auth.iam-policy)
  + [Loading data from an Aurora PostgreSQL DB cluster or RDS for PostgreSQL DB instance](limitless-load.data.md)
  + [Monitoring data loading](limitless-load.monitor.md)
    + [Listing data loading jobs](limitless-load.monitor.md#limitless-load.monitor-list)
    + [Viewing details of data loading jobs using the job ID](limitless-load.monitor.md#limitless-load.monitor-describe)
    + [Monitoring the Amazon CloudWatch log group](limitless-load.monitor.md#limitless-load.monitor-cwl)
    + [Monitoring RDS events](limitless-load.monitor.md#limitless-load.monitor-events)
  + [Canceling data loading](limitless-load.cancel.md)