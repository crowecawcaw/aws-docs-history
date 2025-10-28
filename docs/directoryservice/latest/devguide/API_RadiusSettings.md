# RadiusSettings

Contains information about a Remote Authentication Dial In User Service (RADIUS)
server.

## Contents

**AuthenticationProtocol**

The protocol specified for your RADIUS endpoints.

Type: String

Valid Values: `PAP | CHAP | MS-CHAPv1 | MS-CHAPv2`

Required: No

**DisplayLabel**

Not currently used.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Required: No

**RadiusPort**

The port that your RADIUS server is using for communications. Your self-managed network
must allow inbound traffic over this port from the AWS Directory Service servers.

Type: Integer

Valid Range: Minimum value of 1025. Maximum value of 65535.

Required: No

**RadiusRetries**

The maximum number of times that communication with the RADIUS server is retried after
the initial attempt.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 10.

Required: No

**RadiusServers**

The fully qualified domain name (FQDN) or IP addresses of the RADIUS server endpoints,
or the FQDN or IP addresses of your RADIUS server load balancer.

Type: Array of strings

Length Constraints: Minimum length of 1. Maximum length of 256.

Required: No

**RadiusServersIpv6**

The IPv6 addresses of the RADIUS server endpoints or RADIUS server
load balancer.

Type: Array of strings

Length Constraints: Minimum length of 1. Maximum length of 256.

Required: No

**RadiusTimeout**

The amount of time, in seconds, to wait for the RADIUS server to respond.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 50.

Required: No

**SharedSecret**

Required for enabling RADIUS on the directory.

Type: String

Length Constraints: Minimum length of 8. Maximum length of 512.

Pattern: `^(\p{LD}|\p{Punct}| )+$`

Required: No

**UseSameUsername**

Not currently used.

Type: Boolean

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/RadiusSettings.md "../../../goto/SdkForCpp/ds-2015-04-16/RadiusSettings.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/RadiusSettings.md "../../../goto/SdkForJavaV2/ds-2015-04-16/RadiusSettings.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/RadiusSettings.md "../../../goto/SdkForRubyV3/ds-2015-04-16/RadiusSettings.md")
