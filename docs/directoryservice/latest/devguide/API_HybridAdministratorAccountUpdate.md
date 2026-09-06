

# HybridAdministratorAccountUpdate
<a name="API_HybridAdministratorAccountUpdate"></a>

 Use to recover to the hybrid directory administrator account credentials.

## Contents
<a name="API_HybridAdministratorAccountUpdate_Contents"></a>

 ** SecretArn **   <a name="DirectoryService-Type-HybridAdministratorAccountUpdate-SecretArn"></a>
The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that contains the credentials for the AD administrator user, and enables hybrid domain controllers to join the managed AD domain. For example:  
 ` {"customerAdAdminDomainUsername":"carlos_salazar","customerAdAdminDomainPassword":"ExamplePassword123!"}. `   
Type: String  
Pattern: `^arn:aws:secretsmanager:[a-z0-9-]+:\d{12}:secret:[a-zA-Z0-9/_+=.@-]+-[a-zA-Z0-9]{6}$`   
Required: Yes

## See Also
<a name="API_HybridAdministratorAccountUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/HybridAdministratorAccountUpdate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/HybridAdministratorAccountUpdate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/HybridAdministratorAccountUpdate) 