

# Adding AWS context
<a name="cv-adding-context"></a>

AWS Continuum uses context about your code, infrastructure, and application business to calibrate the severity of the vulnerabilities that it detects. AWS Continuum uses this context to answer questions such as the following:
+ Is this vulnerability reachable over the network?
+ Is this vulnerability deployed?
+ Where is this code running?
+ What could an attacker reach if this node was compromised?
+ Is a credential escalation possible?

**Note**  
AWS Continuum determines network reachability by reasoning over your AWS configuration constructs, such as security groups, routing, and load balancer and API configuration. It does not perform a formal network reachability proof, so treat reachability as a prioritization signal rather than a guarantee that a path does or does not exist.

## Adding infrastructure context
<a name="cv-adding-context-infrastructure"></a>

To collect AWS context, you create an AWS Continuum Collector in the account and AWS Region where your code runs. The collector gathers context such as AWS Config resources, AWS Lambda APIs, and Amazon EKS context. You then authorize an AWS Continuum environment to use that inventory.

To integrate AWS infrastructure context, do the following.

1. Open the AWS Continuum console at [https://console.aws.amazon.com/continuum/](https://console.aws.amazon.com/continuum/) and sign in to the AWS account that contains the infrastructure that you want AWS Continuum to collect context from.

1. In the AWS Region where the code runs, create an AWS Continuum Collector.

   1. In the navigation pane, choose **Collectors**.

   1. Select the AWS collector.

   1. Choose **Enable**.

   1. In the confirmation dialog box, choose **Enable**.

   1. Wait for the collector status to change to **Active**.

1. Sign in to the account that owns the environment. Create or select an IAM role that AWS Continuum can assume to authorize access to collector data. For more information, see [Authorizing an environment to use collector data](#cv-adding-context-cross-account).

1. Sign in to the account that owns the collector and add a resource policy on the collector that grants the environment account access. Skip this step for same-account access. If `AssociateCollector` returns `AccessDeniedException`, check the caller's association and role-passing permissions. Verify that the collector data-access role can access the collector. For instructions on resolving authorization errors, see [Troubleshooting collector authorization](#cv-adding-context-cross-account-troubleshooting).

1. Sign in to the account that owns the environment. Associate the collector with the environment and provide the role's Amazon Resource Name (ARN). You must provide the role for both same-account and cross-account collectors. For instructions on authorizing collector data, see [Authorizing an environment to use collector data](#cv-adding-context-cross-account).

The collector gathers the following information from an AWS account:
+ AWS Config resources. The collector includes the following resource types:
  + Amazon API Gateway: REST API methods, REST APIs, and stages; and Amazon API Gateway Version 2 (HTTP and WebSocket) APIs, integrations, and stages
  + Amazon Elastic Compute Cloud (Amazon EC2): instances, internet gateways, NAT gateways, network ACLs, network interfaces, route tables, security groups, subnets, transit gateways, transit gateway attachments, VPCs, and VPC endpoints
  + AWS Identity and Access Management (IAM): groups, instance profiles, OpenID Connect (OIDC) identity providers, policies, roles, and users
  + Amazon Elastic Container Service (Amazon ECS): clusters, services, and task definitions
  + Amazon Elastic Kubernetes Service (Amazon EKS): clusters, Fargate profiles, and node groups
  + Amazon Elastic Container Registry (Amazon ECR): repositories and public repositories
  + Elastic Load Balancing: Classic Load Balancers; and Elastic Load Balancing Version 2 listeners, listener rules, Application Load Balancers and Network Load Balancers, and target groups
  + Amazon Relational Database Service (Amazon RDS): DB clusters and DB instances
  + Amazon Redshift: clusters
  + Amazon DynamoDB: tables
  + Amazon Keyspaces (for Apache Cassandra): keyspaces
  + Amazon QLDB: ledgers
  + AWS Lambda: functions
  + Amazon Simple Storage Service (Amazon S3): buckets
  + Amazon Elastic File System (Amazon EFS): file systems
  + CloudFormation: stacks
  + Amazon CloudFront: distributions
  + AWS CodeBuild: projects
  + AWS CodePipeline: pipelines
  + Amazon Kinesis Data Streams: streams
  + Amazon Data Firehose: delivery streams
  + Amazon Managed Streaming for Apache Kafka (Amazon MSK): clusters
  + Amazon Simple Notification Service (Amazon SNS): topics
  + Amazon Simple Queue Service (Amazon SQS): queues
  + Amazon OpenSearch Service: domains
  + Amazon OpenSearch Service (legacy Elasticsearch): Elasticsearch domains
  + Amazon Route 53: hosted zones
  + AWS Key Management Service (AWS KMS): KMS keys
  + AWS Secrets Manager: secrets
  + Amazon GuardDuty: detectors
  + AWS WAF: web ACLs (WAFV2)

The collector also gathers the following:
+ AWS Lambda function data collected through API polling
+ Amazon EKS Kubernetes objects: pods, deployments, nodes, and replicas
+ Amazon ECR container images

After you complete these steps, AWS Continuum can use the authorized collector inventory when it generates context for the environment. Repeat these steps for each account from which you want to collect AWS context. For information about collector quotas, see [Quotas for AWS Continuum](quotas.md).

## Authorizing an environment to use collector data
<a name="cv-adding-context-cross-account"></a>

An environment can use inventory from a collector in the same AWS account or in another account. For either configuration, the environment owner associates the collector and supplies a customer-managed role that AWS Continuum assumes before it requests access to the inventory. For cross-account access, the collector owner must also add a resource-policy grant.

The following controls work together:
+ The association identifies the collector that the environment wants to use.
+ The collector data-access role represents the environment when AWS Continuum requests authorization.
+ For cross-account access, the collector resource policy represents the collector owner's consent.

The following table lists the responsibilities for each account.


| Account | Responsibilities | 
| --- | --- | 
| Collector account | Create the collector. For cross-account access, grant the environment account access in the collector resource policy and manage the policy with GetResourcePolicy and PutResourcePolicy. | 
| Environment account | Create the environment and collector data-access role. Associate the collector with the environment and pass the role to AWS Continuum. | 

If the collector and environment are in the same account, that account performs both sets of responsibilities. You don't need to add an `Allow` statement to the collector resource policy for same-account access.

The examples use the AWS Continuum public API namespace, `continuum`.

In the following examples, replace {{collector-account}} with the ID of the account that owns the collector, and {{environment-account}} with the ID of the account that owns the environment. Replace {{environment-id}}, {{collector-id}}, and {{region}} with your resource values.

1. Open the [IAM console](https://console.aws.amazon.com/iam/) in the account that owns the environment.

   Create an IAM role for collector data access. The role trust policy must allow the AWS Continuum service principal, `continuum.amazonaws.com`, to assume it. The following trust policy limits role assumption to the specified environment:

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "AllowContinuumRuntime",
         "Effect": "Allow",
         "Principal": {
           "Service": "continuum.amazonaws.com"
         },
         "Action": "sts:AssumeRole",
         "Condition": {
           "StringEquals": {
             "aws:SourceAccount": "{{environment-account}}"
           },
           "ArnLike": {
             "aws:SourceArn": "arn:aws:continuum:{{region}}:{{environment-account}}:environments/{{environment-id}}"
           }
         }
       }
     ]
   }
   ```

   Attach an identity policy that permits the role to request authorization for every collector that can contribute data to the environment:

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "AuthorizeCollectorData",
         "Effect": "Allow",
         "Action": "continuum:GetCollectorDataAccessAuthorization",
         "Resource": "arn:aws:continuum:{{region}}:{{collector-account}}:collectors/{{collector-id}}"
       }
     ]
   }
   ```

1. For cross-account access, sign in to the account that owns the collector. Skip this step for same-account access. Add a resource policy that grants the environment account permission to call `continuum:GetCollectorDataAccessAuthorization`.

   Use an account principal so the identity policies in the environment account can authorize the collector data-access role that AWS Continuum assumes for the environment.

   The IAM principal that manages the resource policy must belong to the collector account and have the following permissions for the collector:

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "ManageCollectorResourcePolicy",
         "Effect": "Allow",
         "Action": [
           "continuum:GetResourcePolicy",
           "continuum:PutResourcePolicy"
         ],
         "Resource": "arn:aws:continuum:{{region}}:{{collector-account}}:collectors/{{collector-id}}"
       }
     ]
   }
   ```

   Use the following collector resource policy:

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "AllowEnvironmentAccount",
         "Effect": "Allow",
         "Principal": {
           "AWS": "arn:aws:iam::{{environment-account}}:root"
         },
         "Action": "continuum:GetCollectorDataAccessAuthorization",
         "Resource": "arn:aws:continuum:{{region}}:{{collector-account}}:collectors/{{collector-id}}"
       }
     ]
   }
   ```

   Call `GetResourcePolicy` with the full collector ARN in the `arn` input:

   ```
   {
     "arn": "arn:aws:continuum:{{region}}:{{collector-account}}:collectors/{{collector-id}}"
   }
   ```

   Copy the `revisionId` from the response. Read the `policy`. Add the `AllowEnvironmentAccount` statement and retain all existing statements. Serialize the complete policy as a JSON string. Call `PutResourcePolicy` with the following input:

   ```
   {
     "arn": "arn:aws:continuum:{{region}}:{{collector-account}}:collectors/{{collector-id}}",
     "policy": "{{JSON-serialized-policy-document}}",
     "expectedRevisionId": "{{resource-policy-revision}}"
   }
   ```

   If the policy changed after you read it, AWS Continuum returns `ConflictException`. Read the latest policy and `revisionId` with `GetResourcePolicy`. Reapply your change to that policy, retaining its current statements. Retry `PutResourcePolicy` with the updated policy and the latest revision in `expectedRevisionId`.
**Important**  
`PutResourcePolicy` replaces the entire policy. Include every statement that you want to keep. If you omit `policy`, or supply a policy with an empty `Statement` array, AWS Continuum removes all cross-account grants. Same-account authorization remains subject to applicable identity policies. An applicable explicit `Deny` in the collector resource policy still overrides an `Allow`. There is no separate delete operation for a collector resource policy.

1. To associate the collector with the environment, call `AssociateCollector` in the account that owns the environment. The caller must have `continuum:AssociateCollector` permission for the environment and `iam:PassRole` permission for the exact collector data-access role. AWS Continuum assumes that role and checks its access to the collector before creating the association.

   The following example grants the caller these permissions:

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "AssociateCollector",
         "Effect": "Allow",
         "Action": "continuum:AssociateCollector",
         "Resource": "arn:aws:continuum:{{region}}:{{environment-account}}:environments/{{environment-id}}"
       },
       {
         "Sid": "PassCollectorDataAccessRole",
         "Effect": "Allow",
         "Action": "iam:PassRole",
         "Resource": "arn:aws:iam::{{environment-account}}:role/ContinuumCollectorDataAccess"
       }
     ]
   }
   ```

   Then call `AssociateCollector` with the following input:

   ```
   {
     "environmentId": "{{environment-id}}",
     "collectorArn": "arn:aws:continuum:{{region}}:{{collector-account}}:collectors/{{collector-id}}",
     "collectorDataAccessRoleArn": "arn:aws:iam::{{environment-account}}:role/ContinuumCollectorDataAccess"
   }
   ```

   The role must belong to the environment account. This request stores the role on the environment, replacing the previously configured collector data-access role. If the environment has other associated collectors, make sure that the replacement role also permits access to those collectors.

   Verify that the response contains the expected `environmentId` and `environmentArn`. Check that the `associatedCollector` object contains the requested `collectorArn` and its `collectorId`.

1. To confirm the stored association, call `ListAssociatedCollectors` in the environment account with the following input. The caller needs `continuum:ListAssociatedCollectors` permission for the environment.

   ```
   {
     "environmentId": "{{environment-id}}"
   }
   ```

   Verify that `associatedCollectors` contains the expected collector ARN. If the response includes `nextToken`, pass it in the next request to read the remaining results. Continue through empty pages while the response includes a token.

The collector data-access role doesn't need permission to access the collector's inventory storage. This role is separate from a role that AWS Continuum uses to read a customer-managed Amazon S3 source.

AWS Continuum assumes the collector data-access role when it generates context for the environment. AWS Continuum uses the resulting role session to request authorization for each associated collector. AWS Continuum returns an empty response when authorization succeeds. AWS Continuum uses inventory only when authorization succeeds.

For same-account access, configure the association, role trust policy, and role identity permission. For cross-account access, also add the collector resource-policy grant. You can revoke access independently from either account by removing the association, the role permission, or the cross-account resource-policy grant.

### Troubleshooting collector authorization
<a name="cv-adding-context-cross-account-troubleshooting"></a>

If `AssociateCollector` returns `AccessDeniedException`, verify the following:
+ The caller has `continuum:AssociateCollector` permission for the environment and `iam:PassRole` permission for the collector data-access role.
+ The collector data-access role permits `continuum:GetCollectorDataAccessAuthorization` for the collector. Its trust policy allows AWS Continuum to assume it for this environment.
+ For cross-account access, the collector resource policy grants the environment account `continuum:GetCollectorDataAccessAuthorization` permission for the exact collector ARN.
+ The collector and environment are in the same AWS Region, and the collector ARN contains the correct partition, Region, account ID, and `collectors/{{collector-id}}` resource path.
+ No identity policy, collector resource policy, permissions boundary, or AWS Organizations service control policy (SCP) contains an applicable explicit `Deny`.

If the association succeeds but the environment doesn't use the collector inventory, verify the following:
+ The role trust policy allows `continuum.amazonaws.com` and uses the environment account ID for `aws:SourceAccount` and the exact environment ARN for `aws:SourceArn`.
+ The role identity policy allows `continuum:GetCollectorDataAccessAuthorization` for every associated collector that can contribute data to the environment.
+ The most recent `AssociateCollector` request supplied the intended role. Supplying a different role for another collector replaces the role stored on the environment.
+ For cross-account access, the current collector resource policy still grants the environment account access. Call `GetResourcePolicy` to inspect the stored policy and revision.

You can also review CloudTrail events for the failed operation to confirm the caller and resource ARN that AWS Continuum evaluated.

## Adding continuous integration context
<a name="cv-adding-context-cicd"></a>

When you connect a GitHub integration, AWS Continuum also collects continuous integration (CI) context from the repository. AWS Continuum uses this context to determine how your code is built and deployed, which helps it establish whether a vulnerability reaches a running workload.

AWS Continuum collects the following CI context from a connected GitHub repository:
+ Workflows
+ Actions
+ Environment variables that are defined for the workflows and actions