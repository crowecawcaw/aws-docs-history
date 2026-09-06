

# RadiusSettings
<a name="API_RadiusSettings"></a>

Contains information about a Remote Authentication Dial In User Service (RADIUS) server.

## Contents
<a name="API_RadiusSettings_Contents"></a>

 ** AuthenticationProtocol **   <a name="DirectoryService-Type-RadiusSettings-AuthenticationProtocol"></a>
The protocol specified for your RADIUS endpoints.  
Type: String  
Valid Values: `PAP | CHAP | MS-CHAPv1 | MS-CHAPv2`   
Required: No

 ** DisplayLabel **   <a name="DirectoryService-Type-RadiusSettings-DisplayLabel"></a>
Not currently used.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: No

 ** RadiusPort **   <a name="DirectoryService-Type-RadiusSettings-RadiusPort"></a>
The port that your RADIUS server is using for communications. Your self-managed network must allow inbound traffic over this port from the AWS Directory Service servers.  
Type: Integer  
Valid Range: Minimum value of 1025. Maximum value of 65535.  
Required: No

 ** RadiusRetries **   <a name="DirectoryService-Type-RadiusSettings-RadiusRetries"></a>
The maximum number of times that communication with the RADIUS server is retried after the initial attempt.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 10.  
Required: No

 ** RadiusServers **   <a name="DirectoryService-Type-RadiusSettings-RadiusServers"></a>
The fully qualified domain name (FQDN) or IP addresses of the RADIUS server endpoints, or the FQDN or IP addresses of your RADIUS server load balancer.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: No

 ** RadiusServersIpv6 **   <a name="DirectoryService-Type-RadiusSettings-RadiusServersIpv6"></a>
The IPv6 addresses of the RADIUS server endpoints or RADIUS server load balancer.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: No

 ** RadiusTimeout **   <a name="DirectoryService-Type-RadiusSettings-RadiusTimeout"></a>
The amount of time, in seconds, to wait for the RADIUS server to respond.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 50.  
Required: No

 ** SharedSecret **   <a name="DirectoryService-Type-RadiusSettings-SharedSecret"></a>
Required for enabling RADIUS on the directory.  
Type: String  
Length Constraints: Minimum length of 8. Maximum length of 512.  
Pattern: `^(\p{LD}|\p{Punct}| )+$`   
Required: No

 ** UseSameUsername **   <a name="DirectoryService-Type-RadiusSettings-UseSameUsername"></a>
Not currently used.  
Type: Boolean  
Required: No

## See Also
<a name="API_RadiusSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/RadiusSettings) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/RadiusSettings) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/RadiusSettings) 