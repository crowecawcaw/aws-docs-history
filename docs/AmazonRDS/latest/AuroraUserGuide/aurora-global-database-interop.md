# Using Amazon Aurora global databases with other AWS services

You can use your Aurora global databases with other AWS services, such as Amazon S3 and AWS Lambda. Doing so requires that
all Aurora DB clusters in your global database have the same privileges, external functions, and so on in the
respective AWS Regions. Because a read-only Aurora secondary DB cluster in an Aurora global database can be promoted
to the role of primary, we recommend that you set up write privileges ahead of time, on all Aurora DB clusters for any services
you plan to use with your Aurora global database.

The following procedures summarize the actions to take for each AWS service.

###### To invoke AWS Lambda functions from an Aurora global database

1. For all the Aurora clusters that make up the Aurora global database, perform the
   procedures in [Invoking a Lambda function from an Amazon Aurora MySQL DB cluster](AuroraMySQL.Integrating.Lambda.md "AuroraMySQL.Integrating.Lambda.md").
2. For each cluster in the Aurora global database, set the
   (ARN) of the new IAM (IAM) role.
3. To permit database users in an Aurora global database to invoke Lambda functions,
   associate the role that you created in [Creating an IAM role to allow Amazon Aurora to access AWS services](AuroraMySQL.Integrating.Authorizing.IAM.CreateRole.md "AuroraMySQL.Integrating.Authorizing.IAM.CreateRole.md") with each cluster
   in the Aurora global database.
4. Configure each cluster in the Aurora global database to allow outbound connections
   to Lambda. For instructions, see [Enabling network communication from Amazon Aurora to other AWS services](AuroraMySQL.Integrating.Authorizing.Network.md "AuroraMySQL.Integrating.Authorizing.Network.md").

###### To load data from Amazon S3

1. For all the Aurora clusters that make up the Aurora global database, perform the
   procedures in [Loading data into an Amazon Aurora MySQL DB cluster from text files in an Amazon S3 bucket](AuroraMySQL.Integrating.LoadFromS3.md "AuroraMySQL.Integrating.LoadFromS3.md").
2. For each Aurora cluster in the global database, set either the
   `aurora_load_from_s3_role` or `aws_default_s3_role` DB cluster
   parameter to the Amazon Resource Name (ARN) of the new IAM role. If an IAM role
   isn't specified for `aurora_load_from_s3_role`, Aurora uses the IAM role
   specified in `aws_default_s3_role`.
3. To permit database users in an Aurora global database to access S3, associate
   the role that you created in [Creating an IAM role to allow Amazon Aurora to access AWS services](AuroraMySQL.Integrating.Authorizing.IAM.CreateRole.md "AuroraMySQL.Integrating.Authorizing.IAM.CreateRole.md") with each Aurora
   cluster in the global database.
4. Configure each Aurora cluster in the global database to allow outbound connections to S3.
   For instructions, see
   [Enabling network communication from Amazon Aurora to other AWS services](AuroraMySQL.Integrating.Authorizing.Network.md "AuroraMySQL.Integrating.Authorizing.Network.md").

###### To save queried data to Amazon S3

1. For all the Aurora clusters that make up the Aurora global database, perform the
   procedures in
   [Saving data from an Amazon Aurora MySQL DB cluster into text files in an Amazon S3 bucket](AuroraMySQL.Integrating.SaveIntoS3.md "AuroraMySQL.Integrating.SaveIntoS3.md")
   or [Exporting data from an Aurora PostgreSQL DB cluster to Amazon S3](postgresql-s3-export.md "postgresql-s3-export.md").
2. For each Aurora cluster in the global database, set either the
   `aurora_select_into_s3_role` or `aws_default_s3_role` DB cluster
   parameter to the Amazon Resource Name (ARN) of the new IAM role. If an IAM role
   isn't specified for `aurora_select_into_s3_role`, Aurora uses the IAM
   role specified in `aws_default_s3_role`.
3. To permit database users in an Aurora global database to access S3, associate the
   role that you created in
   [Creating an IAM role to allow Amazon Aurora to access AWS services](AuroraMySQL.Integrating.Authorizing.IAM.CreateRole.md "AuroraMySQL.Integrating.Authorizing.IAM.CreateRole.md")
   with each Aurora cluster in the global database.
4. Configure each Aurora cluster in the global database to allow outbound connections
   to S3. For instructions, see [Enabling network communication from Amazon Aurora to other AWS services](AuroraMySQL.Integrating.Authorizing.Network.md "AuroraMySQL.Integrating.Authorizing.Network.md").

## Using Amazon Application Recovery Controller (ARC) with Aurora Global Database

When planning your business continuity and disaster recovery strategy, you need to
orchestrate recovery across application stacks and their dependencies. [Amazon
Application Recovery Controller (ARC)](../../../r53recovery/latest/dg/region-switch.md "../../../r53recovery/latest/dg/region-switch.md") integrates with Aurora Global Database to
automate this process through ARC Region Switch, a centralized solution for automated
multi-Region application recovery. Region Switch orchestrates failover steps across AWS
accounts and Regions, provides real-time recovery dashboards, and generates compliance
reports by aggregating data across resources and accounts. Learn more about [using
Region Switch for Aurora Global Database](../../../r53recovery/latest/dg/aurora-global-database-block.md "../../../r53recovery/latest/dg/aurora-global-database-block.md").
