

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Add tags to Amazon Pinpoint resources programmatically
<a name="tags-add"></a>

The following examples show how to add a tag to an Amazon Pinpoint resource by using the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/) and the [Amazon Pinpoint REST API](https://docs.aws.amazon.com/pinpoint/latest/apireference/). You can also use any supported AWS SDK to add a tag to a resource.

To add a tag to multiple Amazon Pinpoint resources in a single operation, use the resource groups tagging operations of the AWS CLI or the [AWS Resource Groups Tagging API](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/Welcome.html).

## Add tags by using the API
<a name="tags-add-api"></a>

To create a new resource and add a tag to it by using the Amazon Pinpoint REST API, send a POST request to the appropriate resource URI. Include the `tags` parameter and values in the body of the request. The following example shows how to specify a tag when you create a new project.

```
POST /v1/apps HTTP/1.1
Host: pinpoint.us-east-1.amazonaws.com
Content-Type: application/x-www-form-urlencoded
Accept: application/json
Cache-Control: no-cache

{
   "Name":"MyProject",
   "tags":{
      "key1":"value1"
   }
}
```

To add a tag to an existing resource, send a POST request to the [Tags](https://docs.aws.amazon.com/pinpoint/latest/apireference/tags-resource-arn.html) URI. Include the Amazon Resource Name (ARN) of the resource in the URI. The ARN should be URL encoded. In the body of the request, include the `tags` parameter and values, as shown in the following example.

```
POST /v1/tags/{{resource-arn}} HTTP/1.1
Host: pinpoint.us-east-1.amazonaws.com
Content-Type: application/json
Accept: application/json
Cache-Control: no-cache

{
   "tags":{
      "key1":"value1"
   }
}
```



## Add tags by using the AWS CLI
<a name="add-tags-cli"></a>

To create a new resource and add a tag to it by using the AWS CLI, use the appropriate `create` command for the resource. Include the `tags` parameter and values. The following example shows how to specify tags when you create a new project.

------
#### [ Linux, macOS, or Unix ]

```
$ aws pinpoint create-app \
  --create-application-request '{
    "Name":"{{MyProject}}",
    "tags": {
      "{{key1}}":"{{value1}}",
      "{{key2}}":"{{value2}}"
    } 
  }'
```

------
#### [ Windows Command prompt ]

```
C:\> aws pinpoint create-app ^
     --create-application-request Name={{MyProject}},tags={{{key1}}={{value1}},{{key2}}={{value2}}}
```

------

In the preceding example, do the following:
+ Replace {{MyProject}} with the name that you want to give the project.
+ Replace {{key1}} and {{key2}} with the keys of the tags that you want to add to the resource.
+ Replace {{value1}} and {{value2}} with the values of the tags that you want to add for the respective keys.

For information about the commands that you can use to create an Amazon Pinpoint resource, see the [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/).

To add a tag to an existing resource, use the `tag-resource` command and specify the appropriate values for the required parameters:

------
#### [ Linux, macOS, or Unix ]

```
$ aws pinpoint tag-resource \
  --resource-arn {{resource-arn}} \
  --tags-model '{
    "tags": {
      "{{key1}}":"{{value1}}",
      "{{key2}}":"{{value2}}"
    }
  }'
```

------
#### [ Windows Command Prompt ]

```
C:\> aws pinpoint tag-resource ^
     --resource-arn {{resource-arn}} ^
     --tags-model tags={{{key1}}={{value1}},{{key2}}={{value2}}}
```

------

In the preceding example, do the following:
+ Replace {{resource-arn}} with the Amazon Resource Name (ARN) of the resource that you want to add a tag to.
+ Replace {{key1}} and {{key2}} with the keys of the tags that you want to add to the resource.
+ Replace {{value1}} and {{value2}} with the values of the tags that you want to add for the respective keys.