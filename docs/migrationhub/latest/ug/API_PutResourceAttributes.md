AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# PutResourceAttributes

Provides identifying details of the resource being migrated so that it can be associated
in the Application Discovery Service repository. This association occurs asynchronously
after `PutResourceAttributes` returns.

###### Important

- Keep in mind that subsequent calls to PutResourceAttributes will override
  previously stored attributes. For example, if it is first called with a MAC
  address, but later, it is desired to _add_ an IP address, it
  will then be required to call it with _both_ the IP and MAC
  addresses to prevent overriding the MAC address.
- Note the instructions regarding the special use case of the [`ResourceAttributeList`](API_PutResourceAttributes.md#migrationhub-PutResourceAttributes-request-ResourceAttributeList "API_PutResourceAttributes.md#migrationhub-PutResourceAttributes-request-ResourceAttributeList") parameter when specifying any
  "VM" related value.

###### Note

Because this is an asynchronous call, it will always return 200, whether an
association occurs or not. To confirm if an association was found based on the provided
details, call `ListDiscoveredResources`.

## Request Syntax

```
{
   "DryRun": `boolean`,
   "MigrationTaskName": "`string`",
   "ProgressUpdateStream": "`string`",
   "ResourceAttributeList": [
      {
         "Type": "`string`",
         "Value": "`string`"
      }
   ]
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DryRun](#API_PutResourceAttributes_RequestSyntax "#API_PutResourceAttributes_RequestSyntax")**

Optional boolean flag to indicate whether any effect should take place. Used to test if
the caller has permission to make the call.

Type: Boolean

Required: No

**[MigrationTaskName](#API_PutResourceAttributes_RequestSyntax "#API_PutResourceAttributes_RequestSyntax")**

Unique identifier that references the migration task. _Do not store personal
data in this field._

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[^:|]+`

Required: Yes

**[ProgressUpdateStream](#API_PutResourceAttributes_RequestSyntax "#API_PutResourceAttributes_RequestSyntax")**

The name of the ProgressUpdateStream.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Pattern: `[^/:|\000-\037]+`

Required: Yes

**[ResourceAttributeList](#API_PutResourceAttributes_RequestSyntax "#API_PutResourceAttributes_RequestSyntax")**

Information about the resource that is being migrated. This data will be used to map the
task to a resource in the Application Discovery Service repository.

###### Note

Takes the object array of `ResourceAttribute` where the `Type`
field is reserved for the following values: `IPV4_ADDRESS | IPV6_ADDRESS |
 MAC_ADDRESS | FQDN | VM_MANAGER_ID | VM_MANAGED_OBJECT_REFERENCE | VM_NAME | VM_PATH
| BIOS_ID | MOTHERBOARD_SERIAL_NUMBER` where the identifying value can be a string up to 256 characters. ###### Important <br>• If any "VM" related value is set for a `ResourceAttribute` object, it is required that `VM_MANAGER_ID`, as a minimum, is always set. If `VM_MANAGER_ID` is not set, then all "VM" fields will be discarded and "VM" fields will not be used for matching the migration task to a server in Application Discovery Service repository. See the [Example](API_PutResourceAttributes.md#API_PutResourceAttributes_Examples "API_PutResourceAttributes.md#API_PutResourceAttributes_Examples") section below for a use case of specifying "VM" related values. <br>• If a server you are trying to match has multiple IP or MAC addresses, you should provide as many as you know in separate type/value pairs passed to the `ResourceAttributeList` parameter to maximize the chances of matching. Type: Array of [ResourceAttribute](API_ResourceAttribute.md "API_ResourceAttribute.md") objects Array Members: Minimum number of 1 item. Maximum number of 100 items. Required: Yes ## Response Elements If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body. ## Errors **AccessDeniedException** You do not have sufficient access to perform this action. HTTP Status Code: 400 **DryRunOperation** Exception raised to indicate a successfully authorized action when the `DryRun` flag is set to "true". HTTP Status Code: 400 **HomeRegionNotSetException** The home region is not set. Set the home region to continue. HTTP Status Code: 400 **InternalServerError** Exception raised when an internal, configuration, or dependency error is encountered. HTTP Status Code: 500 **InvalidInputException** Exception raised when the provided input violates a policy constraint or is entered in the wrong format or data type. HTTP Status Code: 400 **ResourceNotFoundException** Exception raised when the request references a resource (Application Discovery Service configuration, update stream, migration task, etc.) that does not exist in Application Discovery Service (Application Discovery Service) or in Migration Hub's repository. HTTP Status Code: 400 **ServiceUnavailableException** Exception raised when there is an internal, configuration, or dependency error encountered. HTTP Status Code: 500 **ThrottlingException** The request was denied due to request throttling. **Message** A message that provides information about the exception. **RetryAfterSeconds** The number of seconds the caller should wait before retrying. HTTP Status Code: 400 **UnauthorizedOperation** Exception raised to indicate a request was not authorized when the `DryRun` flag is set to "true". HTTP Status Code: 400 ## Examples ### Put migration resource attributes to associate with resource in repository The following example sends identifying details of the resource being migrated so that it can be associated with a resource in the Application Discovery Service's repository using the values passed to the required parameters `MigrationTaskName` and `ProgressUpdateStream` to tag the correct target and its migration tool. The `ResourceAttributeList` parameter is also required to define the resource type and its identifying value. Its `Type` field is reserved for the following values: `IPV4_ADDRESS | IPV6_ADDRESS | MAC_ADDRESS | FQDN | VM_MANAGER_ID | VM_MANAGED_OBJECT_REFERENCE | VM_NAME | VM_PATH | BIOS_ID | MOTHERBOARD_SERIAL_NUMBER` where the identifying value can be a string up to 256 characters. In this particular example, the user wants to define the resource type by `VM_NAME`, but also has to set the `VM_MANAGER_ID` field as it is always required when setting any other "VM" related fields. #### Sample Request `{ "MigrationTaskName":"canary-4c208ae8-9876-5432-1098-b748dd9179d3", "ProgressUpdateStream":"canary-017563f9-1234-5678-9de4-cf9d3378d18d", "ResourceAttributeList": [ { "Type":"VM_NAME", "Value":"v1.1.1.0-cloudfront" }, { "Type":"VM_MANAGER_ID", "Value":"a7b4c06d-e12f-1234-9gh7-i5j26k1lm2no" } ] }` ## See Also For more information about using this API in one of the language-specific AWS SDKs, see the following: <br>• [AWS Command Line Interface V2](../../../goto/cli2/AWSMigrationHub-2017-05-31/PutResourceAttributes.md "../../../goto/cli2/AWSMigrationHub-2017-05-31/PutResourceAttributes.md") <br>• [AWS SDK for .NET](../../../goto/DotNetSDKV3/AWSMigrationHub-2017-05-31/PutResourceAttributes.md "../../../goto/DotNetSDKV3/AWSMigrationHub-2017-05-31/PutResourceAttributes.md") <br>• [AWS SDK for C++](../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/PutResourceAttributes.md "../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/PutResourceAttributes.md") <br>• [AWS SDK for Go v2](../../../goto/SdkForGoV2/AWSMigrationHub-2017-05-31/PutResourceAttributes.md "../../../goto/SdkForGoV2/AWSMigrationHub-2017-05-31/PutResourceAttributes.md") <br>• [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/PutResourceAttributes.md "../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/PutResourceAttributes.md") <br>• [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/AWSMigrationHub-2017-05-31/PutResourceAttributes.md "../../../goto/SdkForJavaScriptV3/AWSMigrationHub-2017-05-31/PutResourceAttributes.md") <br>• [AWS SDK for Kotlin](../../../goto/SdkForKotlin/AWSMigrationHub-2017-05-31/PutResourceAttributes.md "../../../goto/SdkForKotlin/AWSMigrationHub-2017-05-31/PutResourceAttributes.md") <br>• [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/AWSMigrationHub-2017-05-31/PutResourceAttributes.md "../../../goto/SdkForPHPV3/AWSMigrationHub-2017-05-31/PutResourceAttributes.md") <br>• [AWS SDK for Python](../../../goto/boto3/AWSMigrationHub-2017-05-31/PutResourceAttributes.md "../../../goto/boto3/AWSMigrationHub-2017-05-31/PutResourceAttributes.md") <br>• [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/PutResourceAttributes.md "../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/PutResourceAttributes.md")
