

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# AWS Config Linked Resources
<a name="jsd-config-linked-resources"></a>

The **AWS Config Linked Resources** field should be set to the JSON string representation of a list of objects (maps) corresponding to the linked resources, each with the following keys:
+  *resourceId*: the ID of the resource in AWS Config 
+  *resourceType*: the type of the resource in AWS Config 
+  *accountName*: the name or alias of the AWS account configured in Jira that should be used to access this resource
+  *region*: the Region where AWS Config should be accessed to get information on this resource

For example, the following value would show information on the S3 bucket `my-bucket` in `eu-central-1`, using the account and end user credentials specified in Jira for the AWS account identified in Jira as `MyAccount1`:

```
                    [ { "resourceId": "my-bucket", 
        "resourceType": "AWS::S3::Bucket", 
        "accountName": "MyAccount1", 
        "region": "eu-central-1" } ]
```