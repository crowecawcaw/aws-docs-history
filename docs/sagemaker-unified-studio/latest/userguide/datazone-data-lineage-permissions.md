# Permissions required for data

lineage

## Read permissions to

view lineage

Permissions on following actions are needed to view lineage graph:

- `datazone:GetLineageNode`
- `datazone:ListLineageNodeHistory`

Both these are included in the `AmazonSageMakerDomainExecution`
managed policy and therefore every user in an Amazon SageMaker Unified Studio
domain can invoke these to view the data lineage graph in Amazon SageMaker
Unified Studio.

Permissions on following actions are needed to view lineage events:

- `datazone:ListLineageEvents`
- `datazone:GetLineageEvent`

User must have an IAM role with a policy that includes "Allow" action on
these APIs to view lineage events posted to Amazon SageMaker Unified
Studio.

## Write permissions to

publish lineage

### Lineage for

AWS Glue crawler

The project user role is used to fetch required data from AWS Glue. The
project user role should contain the following permissions on Glue
operations:

- `glue:listCrawls`
- `glue:getConnection`

###### Note

`SageMakerStudioProjectUserRolePolicy` already contains above
permissions.

### Lineage for

Amazon Redshift

The project user role is used to execute queries on the cluster/workgroup
defined in the connection. The project user role should contain the following
permissions:

- `redshift-data:BatchExecuteStatement`
- `redshift-data:ExecuteStatement`
- `redshift-data:DescribeStatement`
- `redshift-data:GetStatementResult`

###### Note

`SageMakerStudioProjectUserRolePolicy` already contains above
permissions.

In addition, the credentials provided for Amazon Redshift connection in Amazon
SageMaker Unified Studio should contain following permissions:

- `sys:operator` role to access the data from system
  tables for all user queries performed on the
  cluster/workgroup
- Has "SELECT" grant on all the tables

### Lineage for

AWS Glue, EMR jobs

The IAM role used to execute the job should contain following permissions
to publish lineage events to Amazon SageMaker Unified Studio:

- ALLOW action on `datazone:PostLineageEvent`
- If your Amazon SageMaker Unified Studio domain is encrypted with
  KMS CMK (customer managed key), the job role should have permissions
  to encrypt and decrypt as well
- If the spark job is in an account different from Amazon SageMaker
  Unified Studio domain account, associate the account with domain
  prior to running the job. Follow [https://docs.aws.amazon.com/datazone/latest/userguide/working-with-associated-accounts.html](../../../datazone/latest/userguide/working-with-associated-accounts.md "../../../datazone/latest/userguide/working-with-associated-accounts.md")
  to set up account association

### Publish Lineage using API

IAM role with a policy to allow `datazone:PostLineageEvent` action
is needed to post lineage events programmatically
