

# Actions, resources, and condition keys for Amazon CloudFront
<a name="list_cloudfront"></a>

Amazon CloudFront (service prefix: `cloudfront`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/cloudfront/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/auth-and-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/cloudfront/cloudfront.json) for this service.

**Topics**
+ [API operations defined by Amazon CloudFront](#list_cloudfront-operations)
+ [Actions defined by Amazon CloudFront](#list_cloudfront-actions-as-permissions)
+ [Permission-only actions for Amazon CloudFront](#list_cloudfront-permission-only-actions)
+ [Resource types defined by Amazon CloudFront](#list_cloudfront-resources-for-iam-policies)
+ [Condition keys for Amazon CloudFront](#list_cloudfront-policy-keys)

## API operations defined by Amazon CloudFront
<a name="list_cloudfront-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_cloudfront-actions-as-permissions).




- **   AssociateAlias  **
  - **IAM action:**  [cloudfront:AssociateAlias](#list_cloudfront-action-AssociateAlias)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudfront:UpdateDistribution](#list_cloudfront-action-UpdateDistribution)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   AssociateDistributionTenantWebACL  **
  - **IAM action:**  [cloudfront:AssociateDistributionTenantWebACL](#list_cloudfront-action-AssociateDistributionTenantWebACL) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateDistributionWebACL  **
  - **IAM action:**  [cloudfront:AssociateDistributionWebACL](#list_cloudfront-action-AssociateDistributionWebACL)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudfront:GetVpcOrigin](#list_cloudfront-action-GetVpcOrigin)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   CopyDistribution  **
  - **IAM action:**  [cloudfront:CopyDistribution](#list_cloudfront-action-CopyDistribution)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudfront:CreateDistribution](#list_cloudfront-action-CreateDistribution)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudfront:GetDistribution](#list_cloudfront-action-GetDistribution)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [cloudfront:GetVpcOrigin](#list_cloudfront-action-GetVpcOrigin)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   CreateAnycastIpList  **
  - **IAM action:**  [cloudfront:CreateAnycastIpList](#list_cloudfront-action-CreateAnycastIpList)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudfront:TagResource](#list_cloudfront-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCachePolicy  **
  - **IAM action:**  [cloudfront:CreateCachePolicy](#list_cloudfront-action-CreateCachePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateCloudFrontOriginAccessIdentity  **
  - **IAM action:**  [cloudfront:CreateCloudFrontOriginAccessIdentity](#list_cloudfront-action-CreateCloudFrontOriginAccessIdentity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateConnectionFunction  **
  - **IAM action:**  [cloudfront:CreateConnectionFunction](#list_cloudfront-action-CreateConnectionFunction)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudfront:TagResource](#list_cloudfront-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateConnectionGroup  **
  - **IAM action:**  [cloudfront:CreateConnectionGroup](#list_cloudfront-action-CreateConnectionGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudfront:TagResource](#list_cloudfront-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateContinuousDeploymentPolicy  **
  - **IAM action:**  [cloudfront:CreateContinuousDeploymentPolicy](#list_cloudfront-action-CreateContinuousDeploymentPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDistribution  **
  - **IAM action:**  [cloudfront:CreateConnectionGroup](#list_cloudfront-action-CreateConnectionGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudfront:CreateDistribution](#list_cloudfront-action-CreateDistribution)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudfront:GetVpcOrigin](#list_cloudfront-action-GetVpcOrigin)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   CreateDistributionTenant  **
  - **IAM action:**  [cloudfront:CreateDistributionTenant](#list_cloudfront-action-CreateDistributionTenant)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudfront:GetVpcOrigin](#list_cloudfront-action-GetVpcOrigin)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [cloudfront:TagResource](#list_cloudfront-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDistributionWithTags  **
  - **IAM action:**  [cloudfront:CreateConnectionGroup](#list_cloudfront-action-CreateConnectionGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudfront:CreateDistribution](#list_cloudfront-action-CreateDistribution)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudfront:GetVpcOrigin](#list_cloudfront-action-GetVpcOrigin)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [cloudfront:TagResource](#list_cloudfront-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateFieldLevelEncryptionConfig  **
  - **IAM action:**  [cloudfront:CreateFieldLevelEncryptionConfig](#list_cloudfront-action-CreateFieldLevelEncryptionConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateFieldLevelEncryptionProfile  **
  - **IAM action:**  [cloudfront:CreateFieldLevelEncryptionProfile](#list_cloudfront-action-CreateFieldLevelEncryptionProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateFunction  **
  - **IAM action:**  [cloudfront:CreateFunction](#list_cloudfront-action-CreateFunction)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudfront:TagResource](#list_cloudfront-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateInvalidation  **
  - **IAM action:**  [cloudfront:CreateInvalidation](#list_cloudfront-action-CreateInvalidation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateInvalidationForDistributionTenant  **
  - **IAM action:**  [cloudfront:CreateInvalidationForDistributionTenant](#list_cloudfront-action-CreateInvalidationForDistributionTenant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateKeyGroup  **
  - **IAM action:**  [cloudfront:CreateKeyGroup](#list_cloudfront-action-CreateKeyGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateKeyValueStore  **
  - **IAM action:**  [cloudfront:CreateKeyValueStore](#list_cloudfront-action-CreateKeyValueStore)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudfront:TagResource](#list_cloudfront-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateMonitoringSubscription  **
  - **IAM action:**  [cloudfront:CreateMonitoringSubscription](#list_cloudfront-action-CreateMonitoringSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateOriginAccessControl  **
  - **IAM action:**  [cloudfront:CreateOriginAccessControl](#list_cloudfront-action-CreateOriginAccessControl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateOriginRequestPolicy  **
  - **IAM action:**  [cloudfront:CreateOriginRequestPolicy](#list_cloudfront-action-CreateOriginRequestPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreatePublicKey  **
  - **IAM action:**  [cloudfront:CreatePublicKey](#list_cloudfront-action-CreatePublicKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateRealtimeLogConfig  **
  - **IAM action:**  [cloudfront:CreateRealtimeLogConfig](#list_cloudfront-action-CreateRealtimeLogConfig)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudfront.amazonaws.com / **Access level:** Write

- **   CreateResponseHeadersPolicy  **
  - **IAM action:**  [cloudfront:CreateResponseHeadersPolicy](#list_cloudfront-action-CreateResponseHeadersPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateTrustStore  **
  - **IAM action:**  [cloudfront:CreateTrustStore](#list_cloudfront-action-CreateTrustStore)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudfront:TagResource](#list_cloudfront-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateVpcOrigin  **
  - **IAM action:**  [cloudfront:CreateVpcOrigin](#list_cloudfront-action-CreateVpcOrigin)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudfront:TagResource](#list_cloudfront-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteAnycastIpList  **
  - **IAM action:**  [cloudfront:DeleteAnycastIpList](#list_cloudfront-action-DeleteAnycastIpList) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCachePolicy  **
  - **IAM action:**  [cloudfront:DeleteCachePolicy](#list_cloudfront-action-DeleteCachePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCloudFrontOriginAccessIdentity  **
  - **IAM action:**  [cloudfront:DeleteCloudFrontOriginAccessIdentity](#list_cloudfront-action-DeleteCloudFrontOriginAccessIdentity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConnectionFunction  **
  - **IAM action:**  [cloudfront:DeleteConnectionFunction](#list_cloudfront-action-DeleteConnectionFunction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConnectionGroup  **
  - **IAM action:**  [cloudfront:DeleteConnectionGroup](#list_cloudfront-action-DeleteConnectionGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteContinuousDeploymentPolicy  **
  - **IAM action:**  [cloudfront:DeleteContinuousDeploymentPolicy](#list_cloudfront-action-DeleteContinuousDeploymentPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDistribution  **
  - **IAM action:**  [cloudfront:DeleteDistribution](#list_cloudfront-action-DeleteDistribution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDistributionTenant  **
  - **IAM action:**  [cloudfront:DeleteDistributionTenant](#list_cloudfront-action-DeleteDistributionTenant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFieldLevelEncryptionConfig  **
  - **IAM action:**  [cloudfront:DeleteFieldLevelEncryptionConfig](#list_cloudfront-action-DeleteFieldLevelEncryptionConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFieldLevelEncryptionProfile  **
  - **IAM action:**  [cloudfront:DeleteFieldLevelEncryptionProfile](#list_cloudfront-action-DeleteFieldLevelEncryptionProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFunction  **
  - **IAM action:**  [cloudfront:DeleteFunction](#list_cloudfront-action-DeleteFunction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteKeyGroup  **
  - **IAM action:**  [cloudfront:DeleteKeyGroup](#list_cloudfront-action-DeleteKeyGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteKeyValueStore  **
  - **IAM action:**  [cloudfront:DeleteKeyValueStore](#list_cloudfront-action-DeleteKeyValueStore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMonitoringSubscription  **
  - **IAM action:**  [cloudfront:DeleteMonitoringSubscription](#list_cloudfront-action-DeleteMonitoringSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteOriginAccessControl  **
  - **IAM action:**  [cloudfront:DeleteOriginAccessControl](#list_cloudfront-action-DeleteOriginAccessControl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteOriginRequestPolicy  **
  - **IAM action:**  [cloudfront:DeleteOriginRequestPolicy](#list_cloudfront-action-DeleteOriginRequestPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePublicKey  **
  - **IAM action:**  [cloudfront:DeletePublicKey](#list_cloudfront-action-DeletePublicKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRealtimeLogConfig  **
  - **IAM action:**  [cloudfront:DeleteRealtimeLogConfig](#list_cloudfront-action-DeleteRealtimeLogConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourcePolicy  **
  - **IAM action:**  [cloudfront:DeleteResourcePolicy](#list_cloudfront-action-DeleteResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResponseHeadersPolicy  **
  - **IAM action:**  [cloudfront:DeleteResponseHeadersPolicy](#list_cloudfront-action-DeleteResponseHeadersPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteStreamingDistribution  **
  - **IAM action:**  [cloudfront:DeleteStreamingDistribution](#list_cloudfront-action-DeleteStreamingDistribution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTrustStore  **
  - **IAM action:**  [cloudfront:DeleteTrustStore](#list_cloudfront-action-DeleteTrustStore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteVpcOrigin  **
  - **IAM action:**  [cloudfront:DeleteVpcOrigin](#list_cloudfront-action-DeleteVpcOrigin) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeConnectionFunction  **
  - **IAM action:**  [cloudfront:DescribeConnectionFunction](#list_cloudfront-action-DescribeConnectionFunction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFunction  **
  - **IAM action:**  [cloudfront:DescribeFunction](#list_cloudfront-action-DescribeFunction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeKeyValueStore  **
  - **IAM action:**  [cloudfront:DescribeKeyValueStore](#list_cloudfront-action-DescribeKeyValueStore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisassociateDistributionTenantWebACL  **
  - **IAM action:**  [cloudfront:DisassociateDistributionTenantWebACL](#list_cloudfront-action-DisassociateDistributionTenantWebACL) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateDistributionWebACL  **
  - **IAM action:**  [cloudfront:DisassociateDistributionWebACL](#list_cloudfront-action-DisassociateDistributionWebACL) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAnycastIpList  **
  - **IAM action:**  [cloudfront:GetAnycastIpList](#list_cloudfront-action-GetAnycastIpList) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCachePolicy  **
  - **IAM action:**  [cloudfront:GetCachePolicy](#list_cloudfront-action-GetCachePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCachePolicyConfig  **
  - **IAM action:**  [cloudfront:GetCachePolicyConfig](#list_cloudfront-action-GetCachePolicyConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCloudFrontOriginAccessIdentity  **
  - **IAM action:**  [cloudfront:GetCloudFrontOriginAccessIdentity](#list_cloudfront-action-GetCloudFrontOriginAccessIdentity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCloudFrontOriginAccessIdentityConfig  **
  - **IAM action:**  [cloudfront:GetCloudFrontOriginAccessIdentityConfig](#list_cloudfront-action-GetCloudFrontOriginAccessIdentityConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConnectionFunction  **
  - **IAM action:**  [cloudfront:GetConnectionFunction](#list_cloudfront-action-GetConnectionFunction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConnectionGroup  **
  - **IAM action:**  [cloudfront:GetConnectionGroup](#list_cloudfront-action-GetConnectionGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConnectionGroupByRoutingEndpoint  **
  - **IAM action:**  [cloudfront:GetConnectionGroupByRoutingEndpoint](#list_cloudfront-action-GetConnectionGroupByRoutingEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetContinuousDeploymentPolicy  **
  - **IAM action:**  [cloudfront:GetContinuousDeploymentPolicy](#list_cloudfront-action-GetContinuousDeploymentPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetContinuousDeploymentPolicyConfig  **
  - **IAM action:**  [cloudfront:GetContinuousDeploymentPolicyConfig](#list_cloudfront-action-GetContinuousDeploymentPolicyConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDistribution  **
  - **IAM action:**  [cloudfront:GetDistribution](#list_cloudfront-action-GetDistribution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDistributionConfig  **
  - **IAM action:**  [cloudfront:GetDistributionConfig](#list_cloudfront-action-GetDistributionConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDistributionTenant  **
  - **IAM action:**  [cloudfront:GetDistributionTenant](#list_cloudfront-action-GetDistributionTenant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDistributionTenantByDomain  **
  - **IAM action:**  [cloudfront:GetDistributionTenantByDomain](#list_cloudfront-action-GetDistributionTenantByDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFieldLevelEncryption  **
  - **IAM action:**  [cloudfront:GetFieldLevelEncryption](#list_cloudfront-action-GetFieldLevelEncryption) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFieldLevelEncryptionConfig  **
  - **IAM action:**  [cloudfront:GetFieldLevelEncryptionConfig](#list_cloudfront-action-GetFieldLevelEncryptionConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFieldLevelEncryptionProfile  **
  - **IAM action:**  [cloudfront:GetFieldLevelEncryptionProfile](#list_cloudfront-action-GetFieldLevelEncryptionProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFieldLevelEncryptionProfileConfig  **
  - **IAM action:**  [cloudfront:GetFieldLevelEncryptionProfileConfig](#list_cloudfront-action-GetFieldLevelEncryptionProfileConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFunction  **
  - **IAM action:**  [cloudfront:GetFunction](#list_cloudfront-action-GetFunction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInvalidation  **
  - **IAM action:**  [cloudfront:GetInvalidation](#list_cloudfront-action-GetInvalidation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInvalidationForDistributionTenant  **
  - **IAM action:**  [cloudfront:GetInvalidationForDistributionTenant](#list_cloudfront-action-GetInvalidationForDistributionTenant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetKeyGroup  **
  - **IAM action:**  [cloudfront:GetKeyGroup](#list_cloudfront-action-GetKeyGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetKeyGroupConfig  **
  - **IAM action:**  [cloudfront:GetKeyGroupConfig](#list_cloudfront-action-GetKeyGroupConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetManagedCertificateDetails  **
  - **IAM action:**  [cloudfront:GetManagedCertificateDetails](#list_cloudfront-action-GetManagedCertificateDetails) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMonitoringSubscription  **
  - **IAM action:**  [cloudfront:GetMonitoringSubscription](#list_cloudfront-action-GetMonitoringSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOriginAccessControl  **
  - **IAM action:**  [cloudfront:GetOriginAccessControl](#list_cloudfront-action-GetOriginAccessControl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOriginAccessControlConfig  **
  - **IAM action:**  [cloudfront:GetOriginAccessControlConfig](#list_cloudfront-action-GetOriginAccessControlConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOriginRequestPolicy  **
  - **IAM action:**  [cloudfront:GetOriginRequestPolicy](#list_cloudfront-action-GetOriginRequestPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOriginRequestPolicyConfig  **
  - **IAM action:**  [cloudfront:GetOriginRequestPolicyConfig](#list_cloudfront-action-GetOriginRequestPolicyConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPublicKey  **
  - **IAM action:**  [cloudfront:GetPublicKey](#list_cloudfront-action-GetPublicKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPublicKeyConfig  **
  - **IAM action:**  [cloudfront:GetPublicKeyConfig](#list_cloudfront-action-GetPublicKeyConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRealtimeLogConfig  **
  - **IAM action:**  [cloudfront:GetRealtimeLogConfig](#list_cloudfront-action-GetRealtimeLogConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcePolicy  **
  - **IAM action:**  [cloudfront:GetResourcePolicy](#list_cloudfront-action-GetResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResponseHeadersPolicy  **
  - **IAM action:**  [cloudfront:GetResponseHeadersPolicy](#list_cloudfront-action-GetResponseHeadersPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResponseHeadersPolicyConfig  **
  - **IAM action:**  [cloudfront:GetResponseHeadersPolicyConfig](#list_cloudfront-action-GetResponseHeadersPolicyConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetStreamingDistribution  **
  - **IAM action:**  [cloudfront:GetStreamingDistribution](#list_cloudfront-action-GetStreamingDistribution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetStreamingDistributionConfig  **
  - **IAM action:**  [cloudfront:GetStreamingDistributionConfig](#list_cloudfront-action-GetStreamingDistributionConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTrustStore  **
  - **IAM action:**  [cloudfront:GetTrustStore](#list_cloudfront-action-GetTrustStore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetVpcOrigin  **
  - **IAM action:**  [cloudfront:GetVpcOrigin](#list_cloudfront-action-GetVpcOrigin) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAnycastIpLists  **
  - **IAM action:**  [cloudfront:ListAnycastIpLists](#list_cloudfront-action-ListAnycastIpLists) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCachePolicies  **
  - **IAM action:**  [cloudfront:ListCachePolicies](#list_cloudfront-action-ListCachePolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCloudFrontOriginAccessIdentities  **
  - **IAM action:**  [cloudfront:ListCloudFrontOriginAccessIdentities](#list_cloudfront-action-ListCloudFrontOriginAccessIdentities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConflictingAliases  **
  - **IAM action:**  [cloudfront:GetDistribution](#list_cloudfront-action-GetDistribution)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [cloudfront:ListConflictingAliases](#list_cloudfront-action-ListConflictingAliases)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListConnectionFunctions  **
  - **IAM action:**  [cloudfront:ListConnectionFunctions](#list_cloudfront-action-ListConnectionFunctions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConnectionGroups  **
  - **IAM action:**  [cloudfront:ListConnectionGroups](#list_cloudfront-action-ListConnectionGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListContinuousDeploymentPolicies  **
  - **IAM action:**  [cloudfront:ListContinuousDeploymentPolicies](#list_cloudfront-action-ListContinuousDeploymentPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDistributionTenants  **
  - **IAM action:**  [cloudfront:ListDistributionTenants](#list_cloudfront-action-ListDistributionTenants) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDistributionTenantsByCustomization  **
  - **IAM action:**  [cloudfront:ListDistributionTenantsByCustomization](#list_cloudfront-action-ListDistributionTenantsByCustomization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDistributions  **
  - **IAM action:**  [cloudfront:ListDistributions](#list_cloudfront-action-ListDistributions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDistributionsByAnycastIpListId  **
  - **IAM action:**  [cloudfront:ListDistributionsByAnycastIpListId](#list_cloudfront-action-ListDistributionsByAnycastIpListId) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDistributionsByCachePolicyId  **
  - **IAM action:**  [cloudfront:ListDistributionsByCachePolicyId](#list_cloudfront-action-ListDistributionsByCachePolicyId) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDistributionsByConnectionFunction  **
  - **IAM action:**  [cloudfront:ListDistributionsByConnectionFunction](#list_cloudfront-action-ListDistributionsByConnectionFunction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDistributionsByConnectionMode  **
  - **IAM action:**  [cloudfront:ListDistributionsByConnectionMode](#list_cloudfront-action-ListDistributionsByConnectionMode) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDistributionsByKeyGroup  **
  - **IAM action:**  [cloudfront:ListDistributionsByKeyGroup](#list_cloudfront-action-ListDistributionsByKeyGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDistributionsByOriginRequestPolicyId  **
  - **IAM action:**  [cloudfront:ListDistributionsByOriginRequestPolicyId](#list_cloudfront-action-ListDistributionsByOriginRequestPolicyId) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDistributionsByRealtimeLogConfig  **
  - **IAM action:**  [cloudfront:ListDistributionsByRealtimeLogConfig](#list_cloudfront-action-ListDistributionsByRealtimeLogConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDistributionsByResponseHeadersPolicyId  **
  - **IAM action:**  [cloudfront:ListDistributionsByResponseHeadersPolicyId](#list_cloudfront-action-ListDistributionsByResponseHeadersPolicyId) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDistributionsByTrustStore  **
  - **IAM action:**  [cloudfront:ListDistributionsByTrustStore](#list_cloudfront-action-ListDistributionsByTrustStore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDistributionsByVpcOriginId  **
  - **IAM action:**  [cloudfront:ListDistributionsByVpcOriginId](#list_cloudfront-action-ListDistributionsByVpcOriginId) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDistributionsByWebACLId  **
  - **IAM action:**  [cloudfront:ListDistributionsByWebACLId](#list_cloudfront-action-ListDistributionsByWebACLId) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDomainConflicts  **
  - **IAM action:**  [cloudfront:GetDistribution](#list_cloudfront-action-GetDistribution)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [cloudfront:GetDistributionTenant](#list_cloudfront-action-GetDistributionTenant)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [cloudfront:ListDomainConflicts](#list_cloudfront-action-ListDomainConflicts)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListFieldLevelEncryptionConfigs  **
  - **IAM action:**  [cloudfront:ListFieldLevelEncryptionConfigs](#list_cloudfront-action-ListFieldLevelEncryptionConfigs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFieldLevelEncryptionProfiles  **
  - **IAM action:**  [cloudfront:ListFieldLevelEncryptionProfiles](#list_cloudfront-action-ListFieldLevelEncryptionProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFunctions  **
  - **IAM action:**  [cloudfront:ListFunctions](#list_cloudfront-action-ListFunctions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInvalidations  **
  - **IAM action:**  [cloudfront:ListInvalidations](#list_cloudfront-action-ListInvalidations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInvalidationsForDistributionTenant  **
  - **IAM action:**  [cloudfront:ListInvalidationsForDistributionTenant](#list_cloudfront-action-ListInvalidationsForDistributionTenant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListKeyGroups  **
  - **IAM action:**  [cloudfront:ListKeyGroups](#list_cloudfront-action-ListKeyGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListKeyValueStores  **
  - **IAM action:**  [cloudfront:ListKeyValueStores](#list_cloudfront-action-ListKeyValueStores) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOriginAccessControls  **
  - **IAM action:**  [cloudfront:ListOriginAccessControls](#list_cloudfront-action-ListOriginAccessControls) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOriginRequestPolicies  **
  - **IAM action:**  [cloudfront:ListOriginRequestPolicies](#list_cloudfront-action-ListOriginRequestPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPublicKeys  **
  - **IAM action:**  [cloudfront:ListPublicKeys](#list_cloudfront-action-ListPublicKeys) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRealtimeLogConfigs  **
  - **IAM action:**  [cloudfront:ListRealtimeLogConfigs](#list_cloudfront-action-ListRealtimeLogConfigs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResponseHeadersPolicies  **
  - **IAM action:**  [cloudfront:ListResponseHeadersPolicies](#list_cloudfront-action-ListResponseHeadersPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStreamingDistributions  **
  - **IAM action:**  [cloudfront:ListStreamingDistributions](#list_cloudfront-action-ListStreamingDistributions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [cloudfront:ListTagsForResource](#list_cloudfront-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTrustStores  **
  - **IAM action:**  [cloudfront:ListTrustStores](#list_cloudfront-action-ListTrustStores) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListVpcOrigins  **
  - **IAM action:**  [cloudfront:ListVpcOrigins](#list_cloudfront-action-ListVpcOrigins) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PublishConnectionFunction  **
  - **IAM action:**  [cloudfront:PublishConnectionFunction](#list_cloudfront-action-PublishConnectionFunction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PublishFunction  **
  - **IAM action:**  [cloudfront:PublishFunction](#list_cloudfront-action-PublishFunction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutResourcePolicy  **
  - **IAM action:**  [cloudfront:PutResourcePolicy](#list_cloudfront-action-PutResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [cloudfront:TagResource](#list_cloudfront-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TestConnectionFunction  **
  - **IAM action:**  [cloudfront:TestConnectionFunction](#list_cloudfront-action-TestConnectionFunction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TestFunction  **
  - **IAM action:**  [cloudfront:TestFunction](#list_cloudfront-action-TestFunction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UntagResource  **
  - **IAM action:**  [cloudfront:UntagResource](#list_cloudfront-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAnycastIpList  **
  - **IAM action:**  [cloudfront:UpdateAnycastIpList](#list_cloudfront-action-UpdateAnycastIpList) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCachePolicy  **
  - **IAM action:**  [cloudfront:UpdateCachePolicy](#list_cloudfront-action-UpdateCachePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCloudFrontOriginAccessIdentity  **
  - **IAM action:**  [cloudfront:UpdateCloudFrontOriginAccessIdentity](#list_cloudfront-action-UpdateCloudFrontOriginAccessIdentity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateConnectionFunction  **
  - **IAM action:**  [cloudfront:UpdateConnectionFunction](#list_cloudfront-action-UpdateConnectionFunction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateConnectionGroup  **
  - **IAM action:**  [cloudfront:UpdateConnectionGroup](#list_cloudfront-action-UpdateConnectionGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateContinuousDeploymentPolicy  **
  - **IAM action:**  [cloudfront:UpdateContinuousDeploymentPolicy](#list_cloudfront-action-UpdateContinuousDeploymentPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDistribution  **
  - **IAM action:**  [cloudfront:GetVpcOrigin](#list_cloudfront-action-GetVpcOrigin)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [cloudfront:UpdateDistribution](#list_cloudfront-action-UpdateDistribution)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateDistributionTenant  **
  - **IAM action:**  [cloudfront:GetVpcOrigin](#list_cloudfront-action-GetVpcOrigin)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [cloudfront:UpdateDistributionTenant](#list_cloudfront-action-UpdateDistributionTenant)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateDistributionWithStagingConfig  **
  - **IAM action:**  [cloudfront:GetDistribution](#list_cloudfront-action-GetDistribution)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [cloudfront:GetVpcOrigin](#list_cloudfront-action-GetVpcOrigin)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [cloudfront:UpdateDistribution](#list_cloudfront-action-UpdateDistribution)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateDomainAssociation  **
  - **IAM action:**  [cloudfront:UpdateDistribution](#list_cloudfront-action-UpdateDistribution)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudfront:UpdateDistributionTenant](#list_cloudfront-action-UpdateDistributionTenant)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudfront:UpdateDomainAssociation](#list_cloudfront-action-UpdateDomainAssociation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateFieldLevelEncryptionConfig  **
  - **IAM action:**  [cloudfront:UpdateFieldLevelEncryptionConfig](#list_cloudfront-action-UpdateFieldLevelEncryptionConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFieldLevelEncryptionProfile  **
  - **IAM action:**  [cloudfront:UpdateFieldLevelEncryptionProfile](#list_cloudfront-action-UpdateFieldLevelEncryptionProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFunction  **
  - **IAM action:**  [cloudfront:UpdateFunction](#list_cloudfront-action-UpdateFunction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateKeyGroup  **
  - **IAM action:**  [cloudfront:UpdateKeyGroup](#list_cloudfront-action-UpdateKeyGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateKeyValueStore  **
  - **IAM action:**  [cloudfront:UpdateKeyValueStore](#list_cloudfront-action-UpdateKeyValueStore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateOriginAccessControl  **
  - **IAM action:**  [cloudfront:UpdateOriginAccessControl](#list_cloudfront-action-UpdateOriginAccessControl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateOriginRequestPolicy  **
  - **IAM action:**  [cloudfront:UpdateOriginRequestPolicy](#list_cloudfront-action-UpdateOriginRequestPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePublicKey  **
  - **IAM action:**  [cloudfront:UpdatePublicKey](#list_cloudfront-action-UpdatePublicKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRealtimeLogConfig  **
  - **IAM action:**  [cloudfront:UpdateRealtimeLogConfig](#list_cloudfront-action-UpdateRealtimeLogConfig)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudfront.amazonaws.com / **Access level:** Write

- **   UpdateResponseHeadersPolicy  **
  - **IAM action:**  [cloudfront:UpdateResponseHeadersPolicy](#list_cloudfront-action-UpdateResponseHeadersPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTrustStore  **
  - **IAM action:**  [cloudfront:UpdateTrustStore](#list_cloudfront-action-UpdateTrustStore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateVpcOrigin  **
  - **IAM action:**  [cloudfront:UpdateVpcOrigin](#list_cloudfront-action-UpdateVpcOrigin) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   VerifyDnsConfiguration  **
  - **IAM action:**  [cloudfront:VerifyDnsConfiguration](#list_cloudfront-action-VerifyDnsConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read



## Actions defined by Amazon CloudFront
<a name="list_cloudfront-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateAlias](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_AssociateAlias.html)  **
  - **Description:** Grants permission to associate an alias to a CloudFront distribution
  - **Resource types (\*required):** [distribution\*](#list_cloudfront-resource-distribution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateDistributionTenantWebACL](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_AssociateDistributionTenantWebACL.html)  **
  - **Description:** Grants permission to associate a distribution tenant with an AWS WAF web ACL
  - **Resource types (\*required):** [distribution-tenant\*](#list_cloudfront-resource-distribution-tenant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateDistributionWebACL](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_AssociateDistributionWebACL.html)  **
  - **Description:** Grants permission to associate a distribution with an AWS WAF web ACL
  - **Resource types (\*required):** [distribution\*](#list_cloudfront-resource-distribution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CopyDistribution](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CopyDistribution.html)  **
  - **Description:** Grants permission to copy an existing distribution and create a new web distribution
  - **Resource types (\*required):** [distribution\*](#list_cloudfront-resource-distribution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAnycastIpList](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateAnycastIpList.html)  **
  - **Description:** Grants permission to create an Anycast static IP list
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudfront-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cloudfront-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCachePolicy](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateCachePolicy.html)  **
  - **Description:** Grants permission to add a new cache policy to CloudFront
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateCloudFrontOriginAccessIdentity](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateCloudFrontOriginAccessIdentity.html)  **
  - **Description:** Grants permission to create a new CloudFront origin access identity
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateConnectionFunction](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateConnectionFunction.html)  **
  - **Description:** Grants permission to create a connection function
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudfront-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cloudfront-aws_TagKeys)
  - **Access level:** Write

- **   [CreateConnectionGroup](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateConnectionGroup.html)  **
  - **Description:** Grants permission to create a connection group
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudfront-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cloudfront-aws_TagKeys)
  - **Access level:** Write

- **   [CreateContinuousDeploymentPolicy](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateContinuousDeploymentPolicy.html)  **
  - **Description:** Grants permission to add a new continuous-deployment policy to CloudFront
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateDistribution](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateDistribution.html)  **
  - **Description:** Grants permission to create a new web distribution
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudfront-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cloudfront-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDistributionTenant](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateDistributionTenant.html)  **
  - **Description:** Grants permission to create a distribution tenant
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudfront-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cloudfront-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFieldLevelEncryptionConfig](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateFieldLevelEncryptionConfig.html)  **
  - **Description:** Grants permission to create a new field-level encryption configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateFieldLevelEncryptionProfile](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateFieldLevelEncryptionProfile.html)  **
  - **Description:** Grants permission to create a field-level encryption profile
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateFunction](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateFunction.html)  **
  - **Description:** Grants permission to create a CloudFront function
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudfront-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cloudfront-aws_TagKeys)
  - **Access level:** Write

- **   [CreateInvalidation](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateInvalidation.html)  **
  - **Description:** Grants permission to create a new invalidation batch request
  - **Resource types (\*required):** [distribution\*](#list_cloudfront-resource-distribution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateInvalidationForDistributionTenant](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateInvalidationForDistributionTenant.html)  **
  - **Description:** Grants permission to create an invalidation for a distribution tenant
  - **Resource types (\*required):** [distribution-tenant\*](#list_cloudfront-resource-distribution-tenant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateKeyGroup](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateKeyGroup.html)  **
  - **Description:** Grants permission to add a new key group to CloudFront
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateKeyValueStore](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateKeyValueStore.html)  **
  - **Description:** Grants permission to create a CloudFront KeyValueStore
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudfront-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cloudfront-aws_TagKeys)
  - **Access level:** Write

- **   [CreateMonitoringSubscription](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateMonitoringSubscription.html)  **
  - **Description:** Grants permission to enable additional CloudWatch metrics for the specified CloudFront distribution. The additional metrics incur an additional cost
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateOriginAccessControl](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateOriginAccessControl.html)  **
  - **Description:** Grants permission to create a new origin access control
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateOriginRequestPolicy](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateOriginRequestPolicy.html)  **
  - **Description:** Grants permission to add a new origin request policy to CloudFront
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreatePublicKey](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreatePublicKey.html)  **
  - **Description:** Grants permission to add a new public key to CloudFront
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateRealtimeLogConfig](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateRealtimeLogConfig.html)  **
  - **Description:** Grants permission to create a real-time log configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateResponseHeadersPolicy](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateResponseHeadersPolicy.html)  **
  - **Description:** Grants permission to add a new response headers policy to CloudFront
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateStreamingDistribution](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateStreamingDistribution.html)  **
  - **Description:** Grants permission to create a new RTMP distribution
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateStreamingDistributionWithTags](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateStreamingDistributionWithTags.html)  **
  - **Description:** Grants permission to create a new RTMP distribution with tags
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudfront-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cloudfront-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTrustStore](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateTrustStore.html)  **
  - **Description:** Grants permission to create a trust store
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudfront-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cloudfront-aws_TagKeys)
  - **Access level:** Write

- **   [CreateVpcOrigin](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateVpcOrigin.html)  **
  - **Description:** Grants permission to create a VPC origin
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudfront-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cloudfront-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAnycastIpList](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DeleteAnycastIpList.html)  **
  - **Description:** Grants permission to delete an Anycast static IP list
  - **Resource types (\*required):** [anycast-ip-list\*](#list_cloudfront-resource-anycast-ip-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCachePolicy](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DeleteCachePolicy.html)  **
  - **Description:** Grants permission to delete a cache policy
  - **Resource types (\*required):** [cache-policy\*](#list_cloudfront-resource-cache-policy)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteCloudFrontOriginAccessIdentity](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DeleteCloudFrontOriginAccessIdentity.html)  **
  - **Description:** Grants permission to delete a CloudFront origin access identity
  - **Resource types (\*required):** [origin-access-identity\*](#list_cloudfront-resource-origin-access-identity)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteConnectionFunction](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DeleteConnectionFunction.html)  **
  - **Description:** Grants permission to delete a connection function
  - **Resource types (\*required):** [connection-function\*](#list_cloudfront-resource-connection-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConnectionGroup](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DeleteConnectionGroup.html)  **
  - **Description:** Grants permission to delete a connection group
  - **Resource types (\*required):** [connection-group\*](#list_cloudfront-resource-connection-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteContinuousDeploymentPolicy](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DeleteContinuousDeploymentPolicy.html)  **
  - **Description:** Grants permission to delete a continuous-deployment policy
  - **Resource types (\*required):** [continuous-deployment-policy\*](#list_cloudfront-resource-continuous-deployment-policy)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteDistribution](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DeleteDistribution.html)  **
  - **Description:** Grants permission to delete a web distribution
  - **Resource types (\*required):** [distribution\*](#list_cloudfront-resource-distribution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDistributionTenant](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DeleteDistributionTenant.html)  **
  - **Description:** Grants permission to delete a distribution tenant
  - **Resource types (\*required):** [distribution-tenant\*](#list_cloudfront-resource-distribution-tenant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFieldLevelEncryptionConfig](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DeleteFieldLevelEncryptionConfig.html)  **
  - **Description:** Grants permission to delete a field-level encryption configuration
  - **Resource types (\*required):** [field-level-encryption-config\*](#list_cloudfront-resource-field-level-encryption-config)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteFieldLevelEncryptionProfile](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DeleteFieldLevelEncryptionProfile.html)  **
  - **Description:** Grants permission to delete a field-level encryption profile
  - **Resource types (\*required):** [field-level-encryption-profile\*](#list_cloudfront-resource-field-level-encryption-profile)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteFunction](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DeleteFunction.html)  **
  - **Description:** Grants permission to delete a CloudFront function
  - **Resource types (\*required):** [function\*](#list_cloudfront-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteKeyGroup](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DeleteKeyGroup.html)  **
  - **Description:** Grants permission to delete a key group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteKeyValueStore](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DeleteKeyValueStore.html)  **
  - **Description:** Grants permission to delete a CloudFront KeyValueStore
  - **Resource types (\*required):** [key-value-store\*](#list_cloudfront-resource-key-value-store)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMonitoringSubscription](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DeleteMonitoringSubscription.html)  **
  - **Description:** Grants permission to disable additional CloudWatch metrics for the specified CloudFront distribution
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteOriginAccessControl](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DeleteOriginAccessControl.html)  **
  - **Description:** Grants permission to delete an origin access control
  - **Resource types (\*required):** [origin-access-control\*](#list_cloudfront-resource-origin-access-control)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteOriginRequestPolicy](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DeleteOriginRequestPolicy.html)  **
  - **Description:** Grants permission to delete an origin request policy
  - **Resource types (\*required):** [origin-request-policy\*](#list_cloudfront-resource-origin-request-policy)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeletePublicKey](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DeletePublicKey.html)  **
  - **Description:** Grants permission to delete a public key from CloudFront
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteRealtimeLogConfig](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DeleteRealtimeLogConfig.html)  **
  - **Description:** Grants permission to delete a real-time log configuration
  - **Resource types (\*required):** [realtime-log-config\*](#list_cloudfront-resource-realtime-log-config)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DeleteResourcePolicy.html)  **
  - **Description:** Grants permission to delete a resource's policy document
  - **Resource types (\*required):** [vpcorigin](#list_cloudfront-resource-vpcorigin)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteResponseHeadersPolicy](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DeleteResponseHeadersPolicy.html)  **
  - **Description:** Grants permission to delete a response headers policy
  - **Resource types (\*required):** [response-headers-policy\*](#list_cloudfront-resource-response-headers-policy)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteStreamingDistribution](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DeleteStreamingDistribution.html)  **
  - **Description:** Grants permission to delete an RTMP distribution
  - **Resource types (\*required):** [streaming-distribution\*](#list_cloudfront-resource-streaming-distribution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTrustStore](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DeleteTrustStore.html)  **
  - **Description:** Grants permission to delete a trust store
  - **Resource types (\*required):** [trust-store\*](#list_cloudfront-resource-trust-store)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteVpcOrigin](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DeleteVpcOrigin.html)  **
  - **Description:** Grants permission to delete a VPC origin
  - **Resource types (\*required):** [vpcorigin\*](#list_cloudfront-resource-vpcorigin)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeConnectionFunction](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DescribeConnectionFunction.html)  **
  - **Description:** Grants permission to get a connection function summary
  - **Resource types (\*required):** [connection-function\*](#list_cloudfront-resource-connection-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFunction](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DescribeFunction.html)  **
  - **Description:** Grants permission to get a CloudFront function summary
  - **Resource types (\*required):** [function\*](#list_cloudfront-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeKeyValueStore](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DescribeKeyValueStore.html)  **
  - **Description:** Grants permission to get a CloudFront KeyValueStore summary
  - **Resource types (\*required):** [key-value-store\*](#list_cloudfront-resource-key-value-store)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DisassociateDistributionTenantWebACL](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DisassociateDistributionTenantWebACL.html)  **
  - **Description:** Grants permission to disassociate a distribution tenant from an AWS WAF web ACL
  - **Resource types (\*required):** [distribution-tenant\*](#list_cloudfront-resource-distribution-tenant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateDistributionWebACL](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DisassociateDistributionWebACL.html)  **
  - **Description:** Grants permission to disassociate a distribution from an AWS WAF web ACL
  - **Resource types (\*required):** [distribution\*](#list_cloudfront-resource-distribution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAnycastIpList](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetAnycastIpList.html)  **
  - **Description:** Grants permission to get an Anycast static IP list
  - **Resource types (\*required):** [anycast-ip-list\*](#list_cloudfront-resource-anycast-ip-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCachePolicy](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetCachePolicy.html)  **
  - **Description:** Grants permission to get the cache policy
  - **Resource types (\*required):** [cache-policy\*](#list_cloudfront-resource-cache-policy)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCachePolicyConfig](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetCachePolicyConfig.html)  **
  - **Description:** Grants permission to get the cache policy configuration
  - **Resource types (\*required):** [cache-policy\*](#list_cloudfront-resource-cache-policy)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCloudFrontOriginAccessIdentity](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetCloudFrontOriginAccessIdentity.html)  **
  - **Description:** Grants permission to get the information about a CloudFront origin access identity
  - **Resource types (\*required):** [origin-access-identity\*](#list_cloudfront-resource-origin-access-identity)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCloudFrontOriginAccessIdentityConfig](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetCloudFrontOriginAccessIdentityConfig.html)  **
  - **Description:** Grants permission to get the configuration information about a Cloudfront origin access identity
  - **Resource types (\*required):** [origin-access-identity\*](#list_cloudfront-resource-origin-access-identity)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetConnectionFunction](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetConnectionFunction.html)  **
  - **Description:** Grants permission to get a connection function's code
  - **Resource types (\*required):** [connection-function\*](#list_cloudfront-resource-connection-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetConnectionGroup](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetConnectionGroup.html)  **
  - **Description:** Grants permission to get information about a connection group
  - **Resource types (\*required):** [connection-group\*](#list_cloudfront-resource-connection-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetConnectionGroupByRoutingEndpoint](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetConnectionGroupByRoutingEndpoint.html)  **
  - **Description:** Grants permission to get information about a connection group by the specified routing endpoint
  - **Resource types (\*required):** [connection-group\*](#list_cloudfront-resource-connection-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetContinuousDeploymentPolicy](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetContinuousDeploymentPolicy.html)  **
  - **Description:** Grants permission to get the continuous-deployment policy
  - **Resource types (\*required):** [continuous-deployment-policy\*](#list_cloudfront-resource-continuous-deployment-policy)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetContinuousDeploymentPolicyConfig](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetContinuousDeploymentPolicyConfig.html)  **
  - **Description:** Grants permission to get the continuous-deployment policy configuration
  - **Resource types (\*required):** [continuous-deployment-policy\*](#list_cloudfront-resource-continuous-deployment-policy)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDistribution](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetDistribution.html)  **
  - **Description:** Grants permission to get the information about a web distribution
  - **Resource types (\*required):** [distribution\*](#list_cloudfront-resource-distribution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDistributionConfig](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetDistributionConfig.html)  **
  - **Description:** Grants permission to get the configuration information about a distribution
  - **Resource types (\*required):** [distribution\*](#list_cloudfront-resource-distribution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDistributionTenant](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetDistributionTenant.html)  **
  - **Description:** Grants permission to get information about a distribution tenant
  - **Resource types (\*required):** [distribution-tenant\*](#list_cloudfront-resource-distribution-tenant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDistributionTenantByDomain](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetDistributionTenantByDomain.html)  **
  - **Description:** Grants permission to get information about a distribution tenant by the associated domain
  - **Resource types (\*required):** [distribution-tenant\*](#list_cloudfront-resource-distribution-tenant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFieldLevelEncryption](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetFieldLevelEncryption.html)  **
  - **Description:** Grants permission to get the field-level encryption configuration information
  - **Resource types (\*required):** [field-level-encryption-config\*](#list_cloudfront-resource-field-level-encryption-config)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetFieldLevelEncryptionConfig](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetFieldLevelEncryptionConfig.html)  **
  - **Description:** Grants permission to get the field-level encryption configuration information
  - **Resource types (\*required):** [field-level-encryption-config\*](#list_cloudfront-resource-field-level-encryption-config)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetFieldLevelEncryptionProfile](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetFieldLevelEncryptionProfile.html)  **
  - **Description:** Grants permission to get the field-level encryption configuration information
  - **Resource types (\*required):** [field-level-encryption-profile\*](#list_cloudfront-resource-field-level-encryption-profile)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetFieldLevelEncryptionProfileConfig](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetFieldLevelEncryptionProfileConfig.html)  **
  - **Description:** Grants permission to get the field-level encryption profile configuration information
  - **Resource types (\*required):** [field-level-encryption-profile\*](#list_cloudfront-resource-field-level-encryption-profile)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetFunction](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetFunction.html)  **
  - **Description:** Grants permission to get a CloudFront function's code
  - **Resource types (\*required):** [function\*](#list_cloudfront-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetInvalidation](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetInvalidation.html)  **
  - **Description:** Grants permission to get the information about an invalidation
  - **Resource types (\*required):** [distribution\*](#list_cloudfront-resource-distribution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetInvalidationForDistributionTenant](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetInvalidationForDistributionTenant.html)  **
  - **Description:** Grants permission to get information about an invalidation for a distribution tenant
  - **Resource types (\*required):** [distribution-tenant\*](#list_cloudfront-resource-distribution-tenant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetKeyGroup](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetKeyGroup.html)  **
  - **Description:** Grants permission to get a key group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetKeyGroupConfig](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetKeyGroupConfig.html)  **
  - **Description:** Grants permission to get a key group configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetManagedCertificateDetails](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetManagedCertificateDetails.html)  **
  - **Description:** Grants permission to get details about a CloudFront managed certificate
  - **Resource types (\*required):** [distribution-tenant\*](#list_cloudfront-resource-distribution-tenant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMonitoringSubscription](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetMonitoringSubscription.html)  **
  - **Description:** Grants permission to get information about whether additional CloudWatch metrics are enabled for the specified CloudFront distribution
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetOriginAccessControl](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetOriginAccessControl.html)  **
  - **Description:** Grants permission to get the origin access control
  - **Resource types (\*required):** [origin-access-control\*](#list_cloudfront-resource-origin-access-control)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetOriginAccessControlConfig](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetOriginAccessControlConfig.html)  **
  - **Description:** Grants permission to get the origin access control configuration
  - **Resource types (\*required):** [origin-access-control\*](#list_cloudfront-resource-origin-access-control)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetOriginRequestPolicy](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetOriginRequestPolicy.html)  **
  - **Description:** Grants permission to get the origin request policy
  - **Resource types (\*required):** [origin-request-policy\*](#list_cloudfront-resource-origin-request-policy)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetOriginRequestPolicyConfig](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetOriginRequestPolicyConfig.html)  **
  - **Description:** Grants permission to get the origin request policy configuration
  - **Resource types (\*required):** [origin-request-policy\*](#list_cloudfront-resource-origin-request-policy)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetPublicKey](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetPublicKey.html)  **
  - **Description:** Grants permission to get the public key information
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetPublicKeyConfig](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetPublicKeyConfig.html)  **
  - **Description:** Grants permission to get the public key configuration information
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetRealtimeLogConfig](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetRealtimeLogConfig.html)  **
  - **Description:** Grants permission to get a real-time log configuration
  - **Resource types (\*required):** [realtime-log-config\*](#list_cloudfront-resource-realtime-log-config)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetResourcePolicy](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetResourcePolicy.html)  **
  - **Description:** Grants permission to get the information about a resource's policy document
  - **Resource types (\*required):** [vpcorigin](#list_cloudfront-resource-vpcorigin)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetResponseHeadersPolicy](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetResponseHeadersPolicy.html)  **
  - **Description:** Grants permission to get the response headers policy
  - **Resource types (\*required):** [response-headers-policy\*](#list_cloudfront-resource-response-headers-policy)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetResponseHeadersPolicyConfig](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetResponseHeadersPolicyConfig.html)  **
  - **Description:** Grants permission to get the response headers policy configuration
  - **Resource types (\*required):** [response-headers-policy\*](#list_cloudfront-resource-response-headers-policy)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetStreamingDistribution](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetStreamingDistribution.html)  **
  - **Description:** Grants permission to get the information about an RTMP distribution
  - **Resource types (\*required):** [streaming-distribution\*](#list_cloudfront-resource-streaming-distribution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetStreamingDistributionConfig](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetStreamingDistributionConfig.html)  **
  - **Description:** Grants permission to get the configuration information about a streaming distribution
  - **Resource types (\*required):** [streaming-distribution\*](#list_cloudfront-resource-streaming-distribution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTrustStore](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetTrustStore.html)  **
  - **Description:** Grants permission to get information about a trust store
  - **Resource types (\*required):** [trust-store\*](#list_cloudfront-resource-trust-store)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetVpcOrigin](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetVpcOrigin.html)  **
  - **Description:** Grants permission to get the information about a VPC origin
  - **Resource types (\*required):** [vpcorigin\*](#list_cloudfront-resource-vpcorigin)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAnycastIpLists](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListAnycastIpLists.html)  **
  - **Description:** Grants permission to list your Anycast static IP lists
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCachePolicies](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListCachePolicies.html)  **
  - **Description:** Grants permission to list all cache policies that have been created in CloudFront for this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCloudFrontOriginAccessIdentities](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListCloudFrontOriginAccessIdentities.html)  **
  - **Description:** Grants permission to list your CloudFront origin access identities
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListConflictingAliases](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListConflictingAliases.html)  **
  - **Description:** Grants permission to list all aliases that conflict with the given alias in CloudFront
  - **Resource types (\*required):** [distribution\*](#list_cloudfront-resource-distribution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListConnectionFunctions](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListConnectionFunctions.html)  **
  - **Description:** Grants permission to list the connection functions in your AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListConnectionGroups](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListConnectionGroups.html)  **
  - **Description:** Grants permission to list the connection groups in your AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListContinuousDeploymentPolicies](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListContinuousDeploymentPolicies.html)  **
  - **Description:** Grants permission to list all continuous-deployment policies in the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDistributionTenants](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListDistributionTenants.html)  **
  - **Description:** Grants permission to list the distribution tenants in your AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDistributionTenantsByCustomization](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListDistributionTenantsByCustomization.html)  **
  - **Description:** Grants permission to list the distribution tenants by the customization that you specify
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDistributions](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListDistributions.html)  **
  - **Description:** Grants permission to list the distributions associated with your AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDistributionsByAnycastIpListId](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListDistributionsByAnycastIpListId.html)  **
  - **Description:** Grants permission to list the distributions in your account that are associated with the specified AnycastIpListId
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDistributionsByCachePolicyId](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListDistributionsByCachePolicyId.html)  **
  - **Description:** Grants permission to list distribution IDs for distributions that have a cache behavior that's associated with the specified cache policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDistributionsByConnectionFunction](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListDistributionsByConnectionFunction.html)  **
  - **Description:** Grants permission to list summaries for distributions associated with the specified connection function
  - **Resource types (\*required):** [connection-function\*](#list_cloudfront-resource-connection-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDistributionsByConnectionMode](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListDistributionsByConnectionMode.html)  **
  - **Description:** Grants permission to list the distributions by the specified connection mode
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDistributionsByKeyGroup](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListDistributionsByKeyGroup.html)  **
  - **Description:** Grants permission to list distribution IDs for distributions that have a cache behavior that's associated with the specified key group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDistributionsByOriginRequestPolicyId](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListDistributionsByOriginRequestPolicyId.html)  **
  - **Description:** Grants permission to list distribution IDs for distributions that have a cache behavior that's associated with the specified origin request policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDistributionsByRealtimeLogConfig](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListDistributionsByRealtimeLogConfig.html)  **
  - **Description:** Grants permission to get a list of distributions that have a cache behavior that's associated with the specified real-time log configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDistributionsByResponseHeadersPolicyId](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListDistributionsByResponseHeadersPolicyId.html)  **
  - **Description:** Grants permission to list distribution IDs for distributions that have a cache behavior that's associated with the specified response headers policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDistributionsByTrustStore](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListDistributionsByTrustStore.html)  **
  - **Description:** Grants permission to list summaries for distributions associated with the specified trust store
  - **Resource types (\*required):** [trust-store\*](#list_cloudfront-resource-trust-store)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDistributionsByVpcOriginId](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListDistributionsByVpcOriginId.html)  **
  - **Description:** Grants permission to list IDs for distributions associated with the specified VPC origin
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDistributionsByWebACLId](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListDistributionsByWebACLId.html)  **
  - **Description:** Grants permission to list the distributions associated with your AWS account with given AWS WAF web ACL
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDomainConflicts](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListDomainConflicts.html)  **
  - **Description:** Grants permission to list domain conflicts for a specified domain
  - **Resource types (\*required):** [distribution](#list_cloudfront-resource-distribution) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [distribution-tenant](#list_cloudfront-resource-distribution-tenant) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListFieldLevelEncryptionConfigs](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListFieldLevelEncryptionConfigs.html)  **
  - **Description:** Grants permission to list all field-level encryption configurations that have been created in CloudFront for this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFieldLevelEncryptionProfiles](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListFieldLevelEncryptionProfiles.html)  **
  - **Description:** Grants permission to list all field-level encryption profiles that have been created in CloudFront for this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFunctions](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListFunctions.html)  **
  - **Description:** Grants permission to get a list of CloudFront functions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListInvalidations](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListInvalidations.html)  **
  - **Description:** Grants permission to list your invalidation batches
  - **Resource types (\*required):** [distribution\*](#list_cloudfront-resource-distribution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListInvalidationsForDistributionTenant](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListInvalidationsForDistributionTenant.html)  **
  - **Description:** Grants permission to list the invalidations for a distribution tenant
  - **Resource types (\*required):** [distribution-tenant\*](#list_cloudfront-resource-distribution-tenant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListKeyGroups](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListKeyGroups.html)  **
  - **Description:** Grants permission to list all key groups that have been created in CloudFront for this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListKeyValueStores](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListKeyValueStores.html)  **
  - **Description:** Grants permission to get a list of CloudFront KeyValueStores
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListOriginAccessControls](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListOriginAccessControls.html)  **
  - **Description:** Grants permission to list all origin access controls in the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListOriginRequestPolicies](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListOriginRequestPolicies.html)  **
  - **Description:** Grants permission to list all origin request policies that have been created in CloudFront for this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPublicKeys](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListPublicKeys.html)  **
  - **Description:** Grants permission to list all public keys that have been added to CloudFront for this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRealtimeLogConfigs](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListRealtimeLogConfigs.html)  **
  - **Description:** Grants permission to get a list of real-time log configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListResponseHeadersPolicies](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListResponseHeadersPolicies.html)  **
  - **Description:** Grants permission to list all response headers policies that have been created in CloudFront for this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListStreamingDistributions](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListStreamingDistributions.html)  **
  - **Description:** Grants permission to list your RTMP distributions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a CloudFront resource
  - **Resource types (\*required):** [anycast-ip-list](#list_cloudfront-resource-anycast-ip-list) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [connection-function](#list_cloudfront-resource-connection-function) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [connection-group](#list_cloudfront-resource-connection-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [distribution](#list_cloudfront-resource-distribution) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [distribution-tenant](#list_cloudfront-resource-distribution-tenant) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [function](#list_cloudfront-resource-function) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [key-value-store](#list_cloudfront-resource-key-value-store) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [trust-store](#list_cloudfront-resource-trust-store) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [vpcorigin](#list_cloudfront-resource-vpcorigin) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTrustStores](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListTrustStores.html)  **
  - **Description:** Grants permission to list the trust stores in your AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListVpcOrigins](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListVpcOrigins.html)  **
  - **Description:** Grants permission to list VPC origins
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PublishConnectionFunction](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_PublishConnectionFunction.html)  **
  - **Description:** Grants permission to publish a connection function
  - **Resource types (\*required):** [connection-function\*](#list_cloudfront-resource-connection-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PublishFunction](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_PublishFunction.html)  **
  - **Description:** Grants permission to publish a CloudFront function
  - **Resource types (\*required):** [function\*](#list_cloudfront-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutResourcePolicy](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_PutResourcePolicy.html)  **
  - **Description:** Grants permission to update or create a resource's policy document
  - **Resource types (\*required):** [vpcorigin](#list_cloudfront-resource-vpcorigin)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to a CloudFront resource
  - **Resource types (\*required):** [anycast-ip-list](#list_cloudfront-resource-anycast-ip-list) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudfront-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudfront-aws_TagKeys)
  - **Resource types (\*required):** [connection-function](#list_cloudfront-resource-connection-function) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudfront-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudfront-aws_TagKeys)
  - **Resource types (\*required):** [connection-group](#list_cloudfront-resource-connection-group) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudfront-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudfront-aws_TagKeys)
  - **Resource types (\*required):** [distribution](#list_cloudfront-resource-distribution) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudfront-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudfront-aws_TagKeys)
  - **Resource types (\*required):** [distribution-tenant](#list_cloudfront-resource-distribution-tenant) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudfront-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudfront-aws_TagKeys)
  - **Resource types (\*required):** [function](#list_cloudfront-resource-function) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudfront-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudfront-aws_TagKeys)
  - **Resource types (\*required):** [key-value-store](#list_cloudfront-resource-key-value-store) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudfront-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudfront-aws_TagKeys)
  - **Resource types (\*required):** [streaming-distribution](#list_cloudfront-resource-streaming-distribution) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudfront-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudfront-aws_TagKeys)
  - **Resource types (\*required):** [trust-store](#list_cloudfront-resource-trust-store) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudfront-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudfront-aws_TagKeys)
  - **Resource types (\*required):** [vpcorigin](#list_cloudfront-resource-vpcorigin) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudfront-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudfront-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TestConnectionFunction](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_TestConnectionFunction.html)  **
  - **Description:** Grants permission to test a connection function
  - **Resource types (\*required):** [connection-function\*](#list_cloudfront-resource-connection-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TestFunction](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_TestFunction.html)  **
  - **Description:** Grants permission to test a CloudFront function
  - **Resource types (\*required):** [function\*](#list_cloudfront-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a CloudFront resource
  - **Resource types (\*required):** [anycast-ip-list](#list_cloudfront-resource-anycast-ip-list) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudfront-aws_TagKeys)
  - **Resource types (\*required):** [connection-function](#list_cloudfront-resource-connection-function) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudfront-aws_TagKeys)
  - **Resource types (\*required):** [connection-group](#list_cloudfront-resource-connection-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudfront-aws_TagKeys)
  - **Resource types (\*required):** [distribution](#list_cloudfront-resource-distribution) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudfront-aws_TagKeys)
  - **Resource types (\*required):** [distribution-tenant](#list_cloudfront-resource-distribution-tenant) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudfront-aws_TagKeys)
  - **Resource types (\*required):** [function](#list_cloudfront-resource-function) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudfront-aws_TagKeys)
  - **Resource types (\*required):** [key-value-store](#list_cloudfront-resource-key-value-store) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudfront-aws_TagKeys)
  - **Resource types (\*required):** [streaming-distribution](#list_cloudfront-resource-streaming-distribution) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudfront-aws_TagKeys)
  - **Resource types (\*required):** [trust-store](#list_cloudfront-resource-trust-store) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudfront-aws_TagKeys)
  - **Resource types (\*required):** [vpcorigin](#list_cloudfront-resource-vpcorigin) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudfront-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAnycastIpList](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateAnycastIpList.html)  **
  - **Description:** Grants permission to update an Anycast static IP list
  - **Resource types (\*required):** [anycast-ip-list\*](#list_cloudfront-resource-anycast-ip-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCachePolicy](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateCachePolicy.html)  **
  - **Description:** Grants permission to update a cache policy
  - **Resource types (\*required):** [cache-policy\*](#list_cloudfront-resource-cache-policy)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateCloudFrontOriginAccessIdentity](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateCloudFrontOriginAccessIdentity.html)  **
  - **Description:** Grants permission to set the configuration for a CloudFront origin access identity
  - **Resource types (\*required):** [origin-access-identity\*](#list_cloudfront-resource-origin-access-identity)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateConnectionFunction](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateConnectionFunction.html)  **
  - **Description:** Grants permission to update a connection function
  - **Resource types (\*required):** [connection-function\*](#list_cloudfront-resource-connection-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateConnectionGroup](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateConnectionGroup.html)  **
  - **Description:** Grants permission to update a connection group
  - **Resource types (\*required):** [connection-group\*](#list_cloudfront-resource-connection-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateContinuousDeploymentPolicy](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateContinuousDeploymentPolicy.html)  **
  - **Description:** Grants permission to update a continuous-deployment policy
  - **Resource types (\*required):** [continuous-deployment-policy\*](#list_cloudfront-resource-continuous-deployment-policy)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateDistribution](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateDistribution.html)  **
  - **Description:** Grants permission to update the configuration for a web distribution
  - **Resource types (\*required):** [distribution\*](#list_cloudfront-resource-distribution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDistributionTenant](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateDistributionTenant.html)  **
  - **Description:** Grants permission to update a distribution tenant
  - **Resource types (\*required):** [distribution-tenant\*](#list_cloudfront-resource-distribution-tenant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDistributionWithStagingConfig](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateDistributionWithStagingConfig.html)  **
  - **Description:** Grants permission to copy the configuration from a staging web distribution to its corresponding primary web distribution
  - **Resource types (\*required):** [distribution\*](#list_cloudfront-resource-distribution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDomainAssociation](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateDomainAssociation.html)  **
  - **Description:** Grants permission to update a domain association
  - **Resource types (\*required):** [distribution](#list_cloudfront-resource-distribution) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [distribution-tenant](#list_cloudfront-resource-distribution-tenant) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFieldLevelEncryptionConfig](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateFieldLevelEncryptionConfig.html)  **
  - **Description:** Grants permission to update a field-level encryption configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateFieldLevelEncryptionProfile](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateFieldLevelEncryptionProfile.html)  **
  - **Description:** Grants permission to update a field-level encryption profile
  - **Resource types (\*required):** [field-level-encryption-profile\*](#list_cloudfront-resource-field-level-encryption-profile)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateFunction](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateFunction.html)  **
  - **Description:** Grants permission to update a CloudFront function
  - **Resource types (\*required):** [function\*](#list_cloudfront-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateKeyGroup](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateKeyGroup.html)  **
  - **Description:** Grants permission to update a key group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateKeyValueStore](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateKeyValueStore.html)  **
  - **Description:** Grants permission to update a CloudFront KeyValueStore
  - **Resource types (\*required):** [key-value-store\*](#list_cloudfront-resource-key-value-store)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateOriginAccessControl](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateOriginAccessControl.html)  **
  - **Description:** Grants permission to update an origin access control
  - **Resource types (\*required):** [origin-access-control\*](#list_cloudfront-resource-origin-access-control)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateOriginRequestPolicy](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateOriginRequestPolicy.html)  **
  - **Description:** Grants permission to update an origin request policy
  - **Resource types (\*required):** [origin-request-policy\*](#list_cloudfront-resource-origin-request-policy)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdatePublicKey](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdatePublicKey.html)  **
  - **Description:** Grants permission to update public key information
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateRealtimeLogConfig](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateRealtimeLogConfig.html)  **
  - **Description:** Grants permission to update a real-time log configuration
  - **Resource types (\*required):** [realtime-log-config\*](#list_cloudfront-resource-realtime-log-config)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateResponseHeadersPolicy](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateResponseHeadersPolicy.html)  **
  - **Description:** Grants permission to update a response headers policy
  - **Resource types (\*required):** [response-headers-policy\*](#list_cloudfront-resource-response-headers-policy)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateStreamingDistribution](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateStreamingDistribution.html)  **
  - **Description:** Grants permission to update the configuration for an RTMP distribution
  - **Resource types (\*required):** [streaming-distribution\*](#list_cloudfront-resource-streaming-distribution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTrustStore](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateTrustStore.html)  **
  - **Description:** Grants permission to update a trust store
  - **Resource types (\*required):** [trust-store\*](#list_cloudfront-resource-trust-store)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateVpcOrigin](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateVpcOrigin.html)  **
  - **Description:** Grants permission to update a VPC origin
  - **Resource types (\*required):** [vpcorigin\*](#list_cloudfront-resource-vpcorigin)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [VerifyDnsConfiguration](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_VerifyDnsConfiguration.html)  **
  - **Description:** Grants permission to verify the DNS configuration for a specified domain
  - **Resource types (\*required):** [distribution-tenant](#list_cloudfront-resource-distribution-tenant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Read



## Permission-only actions for Amazon CloudFront
<a name="list_cloudfront-permission-only-actions"></a>

The following actions are defined by Amazon CloudFront but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AllowVendedLogDeliveryForResource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html#AWS-logs-infrastructure-V2-service-specific)  **
  - **Description:** Grants permission to configure vended log delivery for a distribution
  - **Resource types (\*required):** [distribution](#list_cloudfront-resource-distribution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [CreateSavingsPlan](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cf-api-permissions-ref.html)  **
  - **Description:** Grants permission to create a new savings plan
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetSavingsPlan](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cf-api-permissions-ref.html)  **
  - **Description:** Grants permission to get a savings plan
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListDistributionsByLambdaFunction](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cf-api-permissions-ref.html)  **
  - **Description:** Grants permission to list the distributions associated a Lambda function
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRateCards](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cf-api-permissions-ref.html)  **
  - **Description:** Grants permission to list CloudFront rate cards for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSavingsPlans](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cf-api-permissions-ref.html)  **
  - **Description:** Grants permission to list savings plans in the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListUsages](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cf-api-permissions-ref.html)  **
  - **Description:** Grants permission to list CloudFront usage
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [UpdateSavingsPlan](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cf-api-permissions-ref.html)  **
  - **Description:** Grants permission to update a savings plan
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by Amazon CloudFront
<a name="list_cloudfront-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [anycast-ip-list](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/request-static-ips.html)  | arn:${Partition}:cloudfront::${Account}:anycast-ip-list/${Id} | [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_) | 
|  [cache-policy](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cache-key-create-cache-policy.html)  | arn:${Partition}:cloudfront::${Account}:cache-policy/${Id} |   | 
|  [connection-function](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/connection-functions.html)  | arn:${Partition}:cloudfront::${Account}:connection-function/${Id} | [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_) | 
|  [connection-group](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/custom-connection-group.html)  | arn:${Partition}:cloudfront::${Account}:connection-group/${Id} | [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_) | 
|  [continuous-deployment-policy](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/working-with-staging-distribution-continuous-deployment-policy.html)  | arn:${Partition}:cloudfront::${Account}:continuous-deployment-policy/${Id} |   | 
|  [distribution](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-working-with.html)  | arn:${Partition}:cloudfront::${Account}:distribution/${DistributionId} | [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_) | 
|  [distribution-tenant](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-creating-console.html)  | arn:${Partition}:cloudfront::${Account}:distribution-tenant/${Id} | [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_) | 
|  [field-level-encryption-config](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html)  | arn:${Partition}:cloudfront::${Account}:field-level-encryption-config/${Id} |   | 
|  [field-level-encryption-profile](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html)  | arn:${Partition}:cloudfront::${Account}:field-level-encryption-profile/${Id} |   | 
|  [function](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-functions.html)  | arn:${Partition}:cloudfront::${Account}:function/${Name} | [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_) | 
|  [key-value-store](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/kvs-with-functions.html)  | arn:${Partition}:cloudfront::${Account}:key-value-store/${Name} | [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_) | 
|  [origin-access-control](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-origin.html)  | arn:${Partition}:cloudfront::${Account}:origin-access-control/${Id} |   | 
|  [origin-access-identity](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html#private-content-restricting-access-to-s3-overview)  | arn:${Partition}:cloudfront::${Account}:origin-access-identity/${Id} |   | 
|  [origin-request-policy](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html)  | arn:${Partition}:cloudfront::${Account}:origin-request-policy/${Id} |   | 
|  [realtime-log-config](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html)  | arn:${Partition}:cloudfront::${Account}:realtime-log-config/${Name} |   | 
|  [response-headers-policy](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/modifying-response-headers.html)  | arn:${Partition}:cloudfront::${Account}:response-headers-policy/${Id} |   | 
|  [streaming-distribution](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-working-with.html)  | arn:${Partition}:cloudfront::${Account}:streaming-distribution/${DistributionId} | [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_) | 
|  [trust-store](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/trust-stores-certificate-management.html)  | arn:${Partition}:cloudfront::${Account}:trust-store/${Id} | [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_) | 
|  [vpcorigin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-vpc-origins.html)  | arn:${Partition}:cloudfront::${Account}:vpcorigin/${Id} | [aws:ResourceTag/${TagKey}](#list_cloudfront-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon CloudFront
<a name="list_cloudfront-policy-keys"></a>

Amazon CloudFront defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 