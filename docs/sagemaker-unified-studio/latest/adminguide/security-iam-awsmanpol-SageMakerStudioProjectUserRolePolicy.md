

# AWS policy: SageMakerStudioProjectUserRolePolicy
<a name="security-iam-awsmanpol-SageMakerStudioProjectUserRolePolicy"></a>

Amazon SageMaker Unified Studio creates IAM roles for projects users to perform data analytics, artificial intelligence, and machine learning actions, and uses this policy when creating these roles to define the permissions.

This is the main policy for the SageMakerUnifiedStudioProjectRole role. The SageMakerStudioProjectUserRolePolicy policy is created as part of the Tooling environment blueprint. This policy grants read and write access for Amazon SageMaker Unified Studio users to services such as Amazon SageMaker, AWS Glue, Amazon S3, AWS Lake Formation, Amazon Redshift, Amazon Athena, Amazon Q, Amazon EMR. The policy also gives read and write permissions to some infrastructure resources that are required to use these services such as network interfaces, AWS KMS keys, AWS CodeCommit, and AWS Secrets Manager. 

An administrator can control certain permissions in this policy by tagging the role to which the policy is attached. The following tags control permission scoping:
+ EnableGlueWorkloadsPermissions — When set to "true" (default), grants permissions for AWS Glue workloads including creating and managing Glue Sessions, Blueprints, Jobs, Data Quality Rulesets, and Workflows. When not set to "true", these Glue workload permissions are not granted. Glue Data Catalog permissions (such as GetCatalogs, GetDatabases, GetTables) are not affected by this tag and remain available regardless of this setting.
+ EnableAmazonBedrockPermissions — When set to "true" (default), grants permissions for Amazon Bedrock including foundation model access and Bedrock agent operations. When not set to "true", these Bedrock permissions are not granted.

**Note**  
You can't create new projects with AWS CodeCommit. Existing projects that were created using CodeCommit will continue to work.
+ Amazon SageMaker permissions are required for users to use the Amazon SageMaker Domain and Spaces provisioned by default by the Tooling blueprint.
+ AWS Glue permissions are required for users to use the default AWS Glue Connection and create AWS Glue Sessions.
+ Amazon S3 permissions are required for users to access the project's Amazon S3 bucket.
+ AWS Lake Formation permissions are required for users to access underlying data in Amazon S3.
+ Amazon Redshift permissions are required for users to perform SQL queries against Amazon Redshift, and to allow access to the project's Amazon Redshift clusters.
+ Amazon Athena permissions are required for users to use the provisioned Amazon Athena workgroup and to perform SQL queries.
+ Amazon Q permissions are required for users to interact with Amazon Q within Amazon SageMaker Unified Studio.
+ Amazon EMR permissions are required for users to create and access Amazon EMR clusters.
+ AWS CodeCommit permissions are required for users to use the default Git repository, and perform operations such as committing changes.
+ AWS Secrets Manager permissions are required for accessing the secret for various services, such as Amazon Redshift, AWS Glue federated data connections, and Amazon Bedrock.
+ Amazon Bedrock permissions are required to allow users access to Amazon Bedrock IDE, a development experience in Amazon SageMaker Unified Studio that lets you easily discover Amazon Bedrock models and build generative AI apps that use Amazon Bedrock models and features.
+ AWS KMS permissions are required to support customer managed keys. Resources provisioned by Amazon SageMaker Unified Studio can be encrypted with your customer managed key.

To view the permissions for this policy, see [SageMakerStudioProjectUserRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/SageMakerStudioProjectUserRolePolicy.html) in the *AWS Managed Policy Reference*.

**Note**  
Amazon SageMaker Unified Studio creates IAM roles for project users to perform data analytics, AI, and ML actions. You can attach the SageMakerStudioProjectUserRolePolicy managed policy as your user role policy or you can create and attach your own user role policy. Using your own policy provides more granular control over permissions but requires knowledge of IAM policy configuration. The IAM policy must include all necessary permissions required for the service to function properly.

## Role assumption permissions in this policy
<a name="security-iam-awsmanpol-SageMakerStudioProjectUserRolePolicy-assume-role"></a>

This policy lets the project user role assume other IAM roles. Amazon SageMaker Unified Studio projects can use compute resources that you provide, such as an Amazon EMR on EC2 cluster, through an access role. Because you define the access role name, the policy can't predict it in advance. For this reason, the AllowAssumeAccessRole statement grants `sts:AssumeRole` on `Resource: "*"`, so the project user role can assume the access role at runtime. The policy also includes a SetSourceIdentityForAssumeAccessRole statement that requires `sts:SetSourceIdentity` on every assume-role call the project user role makes. For more information about roles and trust policies, see [Roles terms and concepts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html) in the *IAM User Guide*.

Because of these two statements, the project user role can assume another IAM role in the account *only if* that target role's trust policy explicitly allows both `sts:AssumeRole` and `sts:SetSourceIdentity`. A role whose trust policy allows only `sts:AssumeRole` can't be assumed by the project user role. For example, a role that trusts the account root but doesn't grant `sts:SetSourceIdentity` fails the assume-role call with an `AccessDenied` error.

**Audit trust policies for broad role assumption**  
If you administer an account that hosts Amazon SageMaker Unified Studio projects, audit the trust policies of privileged IAM roles in the account. This helps you avoid unintended role assumption from a project identity. Confirm that no privileged role grants `sts:SetSourceIdentity` to a broad principal, such as the account root, using an unrestricted or wildcard source-identity condition (for example, `"Condition": {"StringLike": {"sts:SourceIdentity": "*"}}`). An exception applies only if the role is intended to be assumable by Amazon SageMaker Unified Studio project roles.  
When you register an access or compute role for a project, scope the role's trust policy to the specific project user role. Where possible, use an `sts:ExternalId` condition that matches the project ID, instead of trusting the account root broadly.