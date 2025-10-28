# Data lineage

authorization

**Write permissions** - to publish lineage events
into Amazon SageMaker Unified Studio, you must have an IAM role with a policy that includes an ALLOW
action on the PostLineageEvent API. To publish lineage data into Amazon SageMaker Unified Studio, you must
have an IAM role with a permissions policy that includes an ALLOW action on the
PostLineageEvent API. This IAM authorization happens at API Gateway layer.

**Read permissions to view lineage** - GetLineageNode
and ListLineageNodeHistory are included in the AmazonSageMakerDomainExecution
managed policy and therefore every user in an Amazon SageMaker unified domain can
invoke these to view the data lineage graph in Amazon SageMaker Unified Studio.

**Read permissions to get lineage events:** you must
have an IAM role with a policy that includes ALLOW action on ListLineageEvents and
GetLineageEvent APIs to view lineage events posted to Amazon SageMaker Unified Studio.
