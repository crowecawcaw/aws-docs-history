# PutLifecycleConfiguration

Use this action to manage storage for your file system. A
`LifecycleConfiguration` consists of one or more `LifecyclePolicy`
objects that define the following:

- **`TransitionToIA`** –
  When to move files in the file system from primary storage (Standard storage class) into the Infrequent Access
  (IA) storage.
- **`TransitionToArchive`** –
  When to move files in the file system from their current storage class (either IA or Standard storage) into the
  Archive storage.

File systems cannot transition into Archive storage before transitioning into IA storage. Therefore,
TransitionToArchive must either not be set or must be later than TransitionToIA.

###### Note

The Archive storage class is available only for file systems that use the Elastic throughput mode
and the General Purpose performance mode.

- **`TransitionToPrimaryStorageClass`** –
  Whether to move files in the file system back to primary storage (Standard storage class) after they are accessed in IA
  or Archive storage.
  For more information, see [Managing file system
  storage](lifecycle-management-efs.md "lifecycle-management-efs.md").

Each Amazon EFS file system supports one lifecycle configuration, which applies to
all files in the file system. If a `LifecycleConfiguration` object already exists
for the specified file system, a `PutLifecycleConfiguration` call modifies the
existing configuration. A `PutLifecycleConfiguration` call with an empty
`LifecyclePolicies` array in the request body deletes any existing
`LifecycleConfiguration`. In the request, specify the following:

- The ID for the file system for which you are enabling, disabling, or modifying
  lifecycle management.
- A `LifecyclePolicies` array of `LifecyclePolicy` objects that
  define when to move files to IA storage, to Archive storage,
  and back to primary storage.

###### Note

Amazon EFS requires that each `LifecyclePolicy`
object have only have a single transition, so the `LifecyclePolicies` array needs to be structured with separate
`LifecyclePolicy` objects. See the example requests in the following section for more information.
This operation requires permissions for the `elasticfilesystem:PutLifecycleConfiguration` operation.

To apply a `LifecycleConfiguration` object to an encrypted file system, you
need the same AWS Key Management Service permissions as when you created the encrypted file system.

## Request Syntax

```
PUT /2015-02-01/file-systems/`FileSystemId`/lifecycle-configuration HTTP/1.1
Content-type: application/json

{
   "LifecyclePolicies": [
      {
         "TransitionToArchive": "`string`",
         "TransitionToIA": "`string`",
         "TransitionToPrimaryStorageClass": "`string`"
      }
   ]
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[FileSystemId](#API_PutLifecycleConfiguration_RequestSyntax "#API_PutLifecycleConfiguration_RequestSyntax")**

The ID of the file system for which you are creating the
`LifecycleConfiguration` object (String).

Length Constraints: Maximum length of 128.

Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[LifecyclePolicies](#API_PutLifecycleConfiguration_RequestSyntax "#API_PutLifecycleConfiguration_RequestSyntax")**

An array of `LifecyclePolicy` objects that define the file system's
`LifecycleConfiguration` object. A `LifecycleConfiguration` object
informs lifecycle management of the following:

- **`TransitionToIA`** –
  When to move files in the file system from primary storage (Standard storage class) into the Infrequent Access
  (IA) storage.
- **`TransitionToArchive`** –
  When to move files in the file system from their current storage class (either IA or Standard storage) into the
  Archive storage.

File systems cannot transition into Archive storage before transitioning into IA storage. Therefore,
TransitionToArchive must either not be set or must be later than TransitionToIA.

###### Note

The Archive storage class is available only for file systems that use the Elastic throughput mode
and the General Purpose performance mode.

- **`TransitionToPrimaryStorageClass`** – Whether to move files in the file system back to primary storage (Standard storage class) after they are accessed in IA
  or Archive storage.

###### Note

When using the `put-lifecycle-configuration` CLI command or the
`PutLifecycleConfiguration` API action, Amazon EFS requires that each
`LifecyclePolicy` object have only a single transition. This means that in a
request body, `LifecyclePolicies` must be structured as an array of
`LifecyclePolicy` objects, one object for each storage transition. See the example
requests in the following section for more information.

Type: Array of [LifecyclePolicy](API_LifecyclePolicy.md "API_LifecyclePolicy.md") objects

Array Members: Maximum number of 3 items.

Required: Yes

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "LifecyclePolicies": [
      {
         "TransitionToArchive": "***string***",
         "TransitionToIA": "***string***",
         "TransitionToPrimaryStorageClass": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[LifecyclePolicies](#API_PutLifecycleConfiguration_ResponseSyntax "#API_PutLifecycleConfiguration_ResponseSyntax")**

An array of lifecycle management policies. EFS supports a maximum of one
policy per file system.

Type: Array of [LifecyclePolicy](API_LifecyclePolicy.md "API_LifecyclePolicy.md") objects

Array Members: Maximum number of 3 items.

## Errors

**BadRequest**

Returned if the request is malformed or contains an error such as an invalid
parameter value or a missing required parameter.

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 400

**FileSystemNotFound**

Returned if the specified `FileSystemId` value doesn't exist in the
requester's AWS account.

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 404

**IncorrectFileSystemLifeCycleState**

Returned if the file system's lifecycle state is not "available".

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 409

**InternalServerError**

Returned if an error occurred on the server side.

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 500

## Examples

### Create a lifecycle configuration

The following example creates a `LifecyclePolicy` object using the
`PutLifecycleConfiguration` action. This example creates a lifecycle policy
that instructs EFS to do the following:

- Move all files in the file system that haven't been accessed in Standard
  storage within the last 30 days to IA storage.
- Move all files in the file system that haven't been accessed in
  Standard storage within the last 90 days to Archive
  storage.
- Move files back to Standard storage after they are accessed in IA
  or Archive storage. The Archive storage class is available only for file systems that use the Elastic throughput mode
  and the General Purpose performance mode.

For more information, see [EFS storage classes](storage-classes.md "storage-classes.md") and [Managing file
system storage](lifecycle-management-efs.md "lifecycle-management-efs.md").

#### Sample Request

```

PUT /2015-02-01/file-systems/fs-0123456789abcdefb/lifecycle-configuration HTTP/1.1
Host: elasticfilesystem.us-west-2.amazonaws.com
x-amz-date: 20181122T232908Z
Authorization: <...>
Content-type: application/json
Content-Length: 86

{
   "LifecyclePolicies": [
      {
         "TransitionToArchive": "AFTER_90_DAYS"
      },
      {
         "TransitionToIA": "AFTER_30_DAYS"
      },
      {
         "TransitionToPrimaryStorage": "AFTER_1_ACCESS"
      }
   ]
}
```

#### Sample Response

```
HTTP/1.1 200 OK
x-amzn-RequestId: 01234567-89ab-cdef-0123-456789abcdef
Content-type: application/json
Content-Length: 86

{
    "LifecyclePolicies": [
      {
         "TransitionToArchive": "AFTER_90_DAYS"
      },
      {
         "TransitionToIA": "AFTER_30_DAYS"
      },
      {
         "TransitionToPrimaryStorage": "AFTER_1_ACCESS"
      }
    ]
}
```

### Example put-lifecycle-configuration CLI request

This example illustrates one usage of PutLifecycleConfiguration.

#### Sample Request

```
aws efs put-lifecycle-configuration \
   --file-system-id fs-0123456789abcdefb \
   --lifecycle-policies "[{"TransitionToArchive":"AFTER_90_DAYS"},
     {"TransitionToIA":"AFTER_30_DAYS"},
     {"TransitionToPrimaryStorageClass":"AFTER_1_ACCESS"}]
   --region us-west-2 \
   --profile adminuser

```

#### Sample Response

```
{
   "LifecyclePolicies": [
       {
           "TransitionToArchive": "AFTER_90_DAYS"
       },
       {
           "TransitionToIA": "AFTER_30_DAYS"
       },
       {
           "TransitionToPrimaryStorageClass": "AFTER_1_ACCESS"
       }
   ]
}
```

### Disable lifecycle management

The following example disables lifecycle management for the specified
file system.

#### Sample Request

```

PUT /2015-02-01/file-systems/fs-01234567/lifecycle-configuration HTTP/1.1
Host: elasticfilesystem.us-west-2.amazonaws.com
x-amz-date: 20181122T232908Z
Authorization: <...>
Content-type: application/json
Content-Length: 86

{
   "LifecyclePolicies": [ ]
}


```

#### Sample Response

```

HTTP/1.1 200 OK
x-amzn-RequestId: 01234567-89ab-cdef-0123-456789abcdef
Content-type: application/json
Content-Length: 86

{
   "LifecyclePolicies": [ ]
}

```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/elasticfilesystem-2015-02-01/PutLifecycleConfiguration.md "../../../goto/cli2/elasticfilesystem-2015-02-01/PutLifecycleConfiguration.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/elasticfilesystem-2015-02-01/PutLifecycleConfiguration.md "../../../goto/DotNetSDKV4/elasticfilesystem-2015-02-01/PutLifecycleConfiguration.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/PutLifecycleConfiguration.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/PutLifecycleConfiguration.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/PutLifecycleConfiguration.md "../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/PutLifecycleConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/PutLifecycleConfiguration.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/PutLifecycleConfiguration.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/PutLifecycleConfiguration.md "../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/PutLifecycleConfiguration.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/PutLifecycleConfiguration.md "../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/PutLifecycleConfiguration.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/PutLifecycleConfiguration.md "../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/PutLifecycleConfiguration.md")
- [AWS SDK for Python](../../../goto/boto3/elasticfilesystem-2015-02-01/PutLifecycleConfiguration.md "../../../goto/boto3/elasticfilesystem-2015-02-01/PutLifecycleConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/PutLifecycleConfiguration.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/PutLifecycleConfiguration.md")
