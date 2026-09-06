

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Find resources by ARN in AMS
<a name="find-resource-by-arn"></a>

Amazon Resource Names (ARNs) uniquely identify AWS resources. To learn about ARNs and ARN formats, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) and [ARN Formats](https://docs.aws.amazon.com/quicksight/latest/APIReference/qs-arn-format.html).

**Note**  
In order to obtain details about a resource from its ARN, *you must have access to the account that created the resource*.

There is no direct path in AWS to look up all resource details from the resource ARN, because services have multiple resource types with various related information. If you have the ARN for a resource, you can determine:
+ The related AWS service (the third ARN segment) tells you what AWS console to look at to find the resource
+ The resource ID (the sixth or seventh ARN segment) confirms that you've found the right resource

Or you can look for the AWS CLI commands available for that service in the [*AWS CLI Command Reference*](https://docs.aws.amazon.com/cli/latest/index.html) for information about obtaining details about the resource.

For example, from the following ARN, you can determine that the service is `lambda`, the account is `123456789012`, the resource type is `function`, and the name of the function is `TestFunction`.

```
arn:aws:lambda:us-east-1:123456789012:function:TestFunction
```

From this, you can review the [AWS CLI documentation for the Lambda service](https://docs.aws.amazon.com/cli/latest/reference/lambda/index.html) to learn how more details can be retrieved with various commands, such as `get-function` and `get-function-configuration`.

For example, you can use the following commands to get more information about a Lambda function if you have its name or ARN:

```
aws lambda get-function-configuration --function-name TestFunction
```

```
aws lambda get-function-configuration --function-name arn:aws:lambda:us-east-1:123456789012:function:TestFunction
```