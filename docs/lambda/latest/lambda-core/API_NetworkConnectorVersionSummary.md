

# NetworkConnectorVersionSummary
<a name="API_NetworkConnectorVersionSummary"></a>

Summary information about a single version of a network connector returned by `ListNetworkConnectorVersions`. Each configuration update creates a new immutable version; this shape describes one such version. To retrieve the full configuration of a version, call `GetNetworkConnector` with a version-qualified identifier.

## Contents
<a name="API_NetworkConnectorVersionSummary_Contents"></a>

 ** Arn **   <a name="lambdacore-Type-NetworkConnectorVersionSummary-Arn"></a>
The unqualified ARN of the network connector that this version belongs to.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 140.  
Pattern: `(arn:aws[a-zA-Z-]*:lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:network-connector:[a-zA-Z0-9-_]+(:[1-9][0-9]*)?)`   
Required: Yes

 ** Id **   <a name="lambdacore-Type-NetworkConnectorVersionSummary-Id"></a>
The unique identifier of the network connector.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 140.  
Required: Yes

 ** Name **   <a name="lambdacore-Type-NetworkConnectorVersionSummary-Name"></a>
The name of the network connector.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 140.  
Pattern: `(arn:aws[a-zA-Z-]*:lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:network-connector:[a-zA-Z0-9-_]+(:[1-9][0-9]*)?)|[a-zA-Z0-9_-]{1,64}`   
Required: Yes

 ** State **   <a name="lambdacore-Type-NetworkConnectorVersionSummary-State"></a>
The current state of this connector version.  
Type: String  
Valid Values: `PENDING | ACTIVE | INACTIVE | FAILED | DELETING | DELETE_FAILED`   
Required: Yes

 ** Version **   <a name="lambdacore-Type-NetworkConnectorVersionSummary-Version"></a>
The version number of this connector version.  
Type: Long  
Valid Range: Minimum value of 1.  
Required: Yes

 ** VersionArn **   <a name="lambdacore-Type-NetworkConnectorVersionSummary-VersionArn"></a>
The qualified ARN of this connector version, including the immutable version suffix.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 140.  
Pattern: `(arn:aws[a-zA-Z-]*:lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:network-connector:[a-zA-Z0-9-_]+(:[1-9][0-9]*)?)`   
Required: Yes

 ** LastModified **   <a name="lambdacore-Type-NetworkConnectorVersionSummary-LastModified"></a>
The date and time when this connector version was last modified.  
Type: Timestamp  
Required: No

 ** StateReason **   <a name="lambdacore-Type-NetworkConnectorVersionSummary-StateReason"></a>
A human-readable explanation of the current state, populated when the state is `FAILED`.  
Type: String  
Required: No

 ** StateReasonCode **   <a name="lambdacore-Type-NetworkConnectorVersionSummary-StateReasonCode"></a>
A machine-readable code indicating the reason for the current state. Use this for programmatic error handling.  
Type: String  
Valid Values: `DisallowedByVpcEncryptionControl | Ec2RequestLimitExceeded | InsufficientRolePermissions | InternalError | InvalidSecurityGroup | InvalidSubnet | SecurityGroupsPerInterfaceLimitExceeded | SubnetOutOfIPAddresses`   
Required: No

## See Also
<a name="API_NetworkConnectorVersionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-core-2026-04-30/NetworkConnectorVersionSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-core-2026-04-30/NetworkConnectorVersionSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-core-2026-04-30/NetworkConnectorVersionSummary) 