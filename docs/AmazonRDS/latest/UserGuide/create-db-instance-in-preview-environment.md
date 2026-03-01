# Creating a new DB instance in the Database Preview environment

Use the following procedure to create a DB instance in the preview
environment.

###### To create a DB instance in the Database Preview environment

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Choose **Dashboard** from the navigation pane.
3. In the Dashboard page, locate the **Database Preview
   Environment** section on the Dashboard page, as shown in the
   following image.

![Preview environment section with link displayed in RDS Console, Dashboard](images/preview-environment-dashboard.png)

You can navigate directly to the [Database Preview environment](https://us-east-2.console.aws.amazon.com/rds-preview/home?region=us-east-2# "https://us-east-2.console.aws.amazon.com/rds-preview/home?region=us-east-2#"). Before you can proceed, you must
acknowledge and accept the limitations.

![Preview environment limitations dialog](images/preview-environment-console.png) 4. To create the RDS for PostgreSQL DB instance, follow the same process as that
for creating any Amazon RDS DB instance. For more information, see the [Console](USER_CreateDBInstance.md#USER_CreateDBInstance.CON "USER_CreateDBInstance.md#USER_CreateDBInstance.CON") procedure in [Creating a DB instance](USER_CreateDBInstance.md#USER_CreateDBInstance.Creating "USER_CreateDBInstance.md#USER_CreateDBInstance.Creating").
To create an instance in the Database Preview Environment using the RDS API or the
AWS CLI, use the following endpoint.

```
rds-preview.us-east-2.amazonaws.com
```
