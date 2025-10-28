# Automated IAM deployments using CFN ingest or stack update CTs in AMS

You can use these AMS change types to deploy IAM roles (the `AWS::IAM::Role` resource) in both multi-account landing zone (MALZ) and single-account landing zone (SALZ):

- Deployment | Ingestion | Stack from CloudFormation Template | Create (ct-36cn2avfrrj9v)
- Management | Custom Stack | Stack From CloudFormation Template | Update (ct-361tlo1k7339x)
- Management | Custom Stack | Stack From CloudFormation Template | Approve and Update (ct-1404e21baa2ox)
  **Validations performed on the IAM roles in your CFN template:**

- **ManagedPolicyArns**: The attribute **ManagedPolicyArns** must not exist in `AWS::IAM::Role`.
  The validation disallows attaching managed policies to the role being provisioned. Instead, the permissions for the role can be managed
  using the inline policy through the property Policies.
- **PermissionsBoundary**: The policy used to set the permissions boundary for the role can only be the
  AMS vended managed policy: `AWSManagedServices_IAM_PermissionsBoundary`. This policy acts as a guard rail that protects the AMS
  infrastructure resources from being modified using the role being provisioned. With this default permissions boundary, the security benefits
  that AMS provides are preserved.

The `AWSManagedServices_IAM_PermissionsBoundary` (the default) is required, without it, the request is rejected.

- **MaxSessionDuration**: The maximum session duration that can be set for the IAM role is 1 to 4 hours.
  AMS technical standard require a customer risk acceptance for session duration beyond 4 hours.
- **RoleName**: The following namespaces are preserved by AMS and cannot be used as IAM role name prefixes:

```
AmazonSSMRole,
AMS,
Ams,
ams,
AWSManagedServices,
customer_developer_role,
customer-mc-,
Managed_Services,
MC,
Mc,
mc,
SENTINEL,
Sentinel,
sentinel,
StackSet-AMS,
StackSet-Ams,
StackSet-ams,
StackSet-AWS,
StackSet-MC,
StackSet-Mc,
StackSet-mc
```

- **Policies**: The inline policy embedded in the IAM role can only include a set of IAM actions that are pre-approved by AMS.
  This is the upper bound of all IAM actions allowed to create an IAM role with (control policy). The control policy consists of:
  - All actions in the AWS managed policy ReadOnlyAccess that provides read-only access to all AWS services and resources
  - The following actions, with the restriction on cross-account S3 actions i.e. allowed S3 actions can only be performed on resources
    present in the same account as the role being created:

  ```
  amscm:*,
  amsskms:*,
  lambda:InvokeFunction,
  logs:CreateLogStream,
  logs:PutLogEvents,
  s3:AbortMultipartUpload,
  s3:DeleteObject,
  s3:DeleteObjectVersion,
  s3:ObjectOwnerOverrideToBucketOwner,
  s3:PutObject,
  s3:ReplicateTags,
  secretsmanager:GetRandomPassword,
  sns:Publish
  ```

  Any IAM role created or updated through CFN ingest can allow actions listed on this control policy, or actions that are scoped down
  from (less permissive than) the actions listed on the control policy. Currently we allow these safe IAM actions that can be categorized
  as readonly actions, plus the above mentioned non-readonly actions that can't be accomplished through CTs
  and are pre-approved per AMS technical standard.

- **AssumeRolePolicyDocument**: The following entities are pre-approved and can be included in the trust policy to
  assume the role being created:

      + Any IAM entity (role, user, root user, STS assumed-role session) in the same account can assume the role.
      + The following AWS services can assume the role:



      ```
      apigateway.amazonaws.com,
      autoscaling.amazonaws.com,
      cloudformation.amazonaws.com,
      codebuild.amazonaws.com,
      codedeploy.amazonaws.com,
      codepipeline.amazonaws.com,
      datapipeline.amazonaws.com,
      datasync.amazonaws.com,
      dax.amazonaws.com,
      dms.amazonaws.com,
      ec2.amazonaws.com,
      ecs-tasks.amazonaws.com,
      ecs.application-autoscaling.amazonaws.com,
      elasticmapreduce.amazonaws.com,
      es.amazonaws.com,
      events.amazonaws.com,
      firehose.amazonaws.com,
      glue.amazonaws.com,
      lambda.amazonaws.com,
      monitoring.rds.amazonaws.com,
      pinpoint.amazonaws.com,
      rds.amazonaws.com,
      redshift.amazonaws.com,
      s3.amazonaws.com,
      sagemaker.amazonaws.com,
      servicecatalog.amazonaws.com,
      sns.amazonaws.com,
      ssm.amazonaws.com,
      states.amazonaws.com,
      storagegateway.amazonaws.com,
      transfer.amazonaws.com,
      vmie.amazonaws.com
      ```
      + The SAML provider in the same account can assume the role. Currently, the only supported SAML provider name is
       `customer-saml`.

  If one or more of the validations fail, the RFC is rejected. A sample RFC rejection reason look like this:

```
{"errorMessage":"[ 'LambdaRole: The maximum session duration (in seconds) should be a numeric value in the range 3600 to 14400 (i.e. 1 to 4 hours).', 'lambda-policy: Policy document is too permissive.']","errorType":"ClientError"}

```

If you need assistance with a failed RFC validation or execution, use the RFC correspondence to reach out to AMS.
For instructions, see [RFC correspondence and attachment (console)](../ctref/ex-rfc-correspondence.md "../ctref/ex-rfc-correspondence.md").
For any other questions, submit a service request. For a how-to, see
[Creating a Service Request](../userguide/gui-ex-create-service-request.md "../userguide/gui-ex-create-service-request.md").

###### Note

We do not currently enforce any IAM best practices as part of our IAM validations. For IAM best practices, see
[Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md").

**Creating IAM roles with more permissive actions or enforcing IAM best practices**

Create your IAM entities with the following manual change types:

- Deployment | Advanced stack components | Identity and Access Management (IAM) | Create entity or policy (ct-3dpd8mdd9jn1r)
- Management | Advanced stack components | Identity and Access Management (IAM) | Update entity or policy (ct-27tuth19k52b4)
  We recommend that you read and understand our technical standards before filing these manual RFCs. For access, see
  [How to access technical standards](../ctref/rfc-security.md#rfc-sec-tech-standards-access "../ctref/rfc-security.md#rfc-sec-tech-standards-access").

###### Note

Each IAM role directly created with these manual change types belongs to its own individual stack and does not reside in the same
stack where the other infrastructure resources are created through CFN Ingest CT.

**Updating IAM Roles created with CFN ingest through manual change types when updates cannot be done through automated change types**

Use the Management | Advanced stack components | Identity and Access Management (IAM) | Update entity or policy (ct-27tuth19k52b4) change type.

###### Important

Updates on IAM roles through the manual CT are not reflected in the CFN stack templates and cause stack drift.
Once the role has been updated through a manual request to a state that doesn’t pass our validations, the role cannot be
further updated using the Stack Update CT (ct-361tlo1k7339x) again as long as it continues to be non-compliant with our validations.
The update CT can be used only if the CFN stack template is compliant with our validations. However, the stack can still be
updated via the Stack Update CT (ct-361tlo1k7339x), as long as the IAM resource that’s non-compliant with our validations is not being updated
and the CFN template passes our validations.

**Deleting your IAM roles created through AWS CloudFormation ingest**

If you want to delete the whole stack, use the following automated Delete Stack change type. For instructions, see
[Delete Stack](../ctref/ex-stack-delete-col.md "../ctref/ex-stack-delete-col.md"):

- Change Type ID: ct-0q0bic0ywqk6c
- Classification: Management | Standard stacks | Stack | Delete and Management | Advanced stack components | Stack | Delete
  If you want to delete an IAM role without deleting the whole stack, you can remove the IAM role from the CloudFormation template and use the updated template
  as an input to the automated Stack Update change type:

- Change Type ID: ct-361tlo1k7339x
- Classification: Management | Custom stack | Stack from CloudFormation template | Update
  For instructions, see
  [Update AWS CloudFormation ingest stack](ex-cfn-ingest-update-col.md "ex-cfn-ingest-update-col.md").
