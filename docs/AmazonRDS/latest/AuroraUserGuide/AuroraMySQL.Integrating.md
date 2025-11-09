# Giving Aurora access to Lambda

Before you can invoke Lambda functions from an Aurora MySQL DB cluster, make sure to first give your cluster
permission to access Lambda.

###### To give Aurora MySQL access to Lambda

1. Create an AWS Identity and Access Management (IAM) policy that provides the permissions that allow
   your Aurora MySQL DB cluster to invoke Lambda functions. For instructions, see
   [Creating an IAM policy to access AWS Lambda resources](AuroraMySQL.Integrating.Authorizing.IAM.md "AuroraMySQL.Integrating.Authorizing.IAM.md").
2. Create an IAM role, and attach the IAM policy you created in [Creating an IAM policy to access AWS Lambda resources](AuroraMySQL.Integrating.Authorizing.IAM.md "AuroraMySQL.Integrating.Authorizing.IAM.md") to the new IAM role.
   For instructions, see [Creating an
   IAM role to allow Amazon Aurora to access AWS services](AuroraMySQL.Integrating.Authorizing.IAM.md "AuroraMySQL.Integrating.Authorizing.IAM.md").
3. Set the `aws_default_lambda_role` DB cluster parameter to the Amazon Resource
   Name (ARN) of the new IAM role.

If the cluster is part of an Aurora global database, apply the same setting for each Aurora cluster in the global
database.

For more information about DB cluster parameters, see [Amazon Aurora DB cluster and DB instance
parameters](USER_WorkingWithDBClusterParamGroups.md#Aurora.Managing.ParameterGroups "USER_WorkingWithDBClusterParamGroups.md#Aurora.Managing.ParameterGroups"). 4. To permit database users in an Aurora MySQL DB cluster to invoke Lambda functions, associate the role that you
created in [Creating an
IAM role to allow Amazon Aurora to access AWS services](AuroraMySQL.Integrating.Authorizing.IAM.md "AuroraMySQL.Integrating.Authorizing.IAM.md") with the DB cluster.
For information about associating an IAM role with a DB cluster, see
[Associating an IAM role with an
Amazon Aurora MySQL DB cluster](AuroraMySQL.Integrating.Authorizing.IAM.md "AuroraMySQL.Integrating.Authorizing.IAM.md").

If the cluster is part of an Aurora global database, associate the role with each Aurora cluster in the
global database. 5. Configure your Aurora MySQL DB cluster to allow outbound connections to Lambda. For instructions, see
[Enabling network
communication from Amazon Aurora to other AWS services](AuroraMySQL.Integrating.Authorizing.md "AuroraMySQL.Integrating.Authorizing.md").

If the cluster is part of an Aurora global database, enable outbound connections for each Aurora cluster
in the global database.
