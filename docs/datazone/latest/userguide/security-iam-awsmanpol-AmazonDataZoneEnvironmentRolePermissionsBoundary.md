

# AWS managed policy: AmazonDataZoneEnvironmentRolePermissionsBoundary
<a name="security-iam-awsmanpol-AmazonDataZoneEnvironmentRolePermissionsBoundary"></a>

**Note**  
This policy is a *permissions boundary*. A permissions boundary sets the maximum permissions that an identity-based policy can grant to an IAM entity. You should not use and attach Amazon DataZone permissions boundary policies on your own. Amazon DataZone permissions boundary policies should only be attached to Amazon DataZone managed roles. For more information on permissions boundaries, see [Permissions boundaries for IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) in the IAM User Guide.

When you create an environment via the Amazon DataZone data portal, Amazon DataZone applies this permissions boundary to the [IAM roles that are produced during environment creation](https://docs.aws.amazon.com/datazone/latest/userguide/roles-for-projects.html). The permissions boundary limits the scope of the roles that Amazon DataZone creates and any roles that you add. 

Amazon DataZone uses the `AmazonDataZoneEnvironmentRolePermissionsBoundary` managed policy to limit the provisioned IAM principal to which it is attached. The principals might take the form of the [user roles](https://docs.aws.amazon.com/datazone/latest/userguide/Identitybasedroles.html) that Amazon DataZone can assume on behalf of interactive enterprise users or analytic services (AWS Glue, for example), and then conduct actions to process data such as reading and writing from Amazon S3 or running AWS Glue crawler.

The `AmazonDataZoneEnvironmentRolePermissionsBoundary` policy grants read and write access for Amazon DataZone to services such as AWS Glue, Amazon S3, AWS Lake Formation, Amazon Redshift, and Amazon Athena. The policy also gives read and write permissions to some infrastructure resources that are required to use these services such as network interfaces and AWS KMS keys.

Amazon DataZone applies the `AmazonDataZoneEnvironmentRolePermissionsBoundary` AWS managed policy as a permissions boundary for all Amazon DataZone environment roles (owner and contributor). This permissions boundary restricts these roles to only allow access to the required resources and actions necessary for an environment.

To view the permissions for this policy, see [AmazonDataZoneEnvironmentRolePermissionsBoundary](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonDataZoneEnvironmentRolePermissionsBoundary.html) in the *AWS Managed Policy Reference*.