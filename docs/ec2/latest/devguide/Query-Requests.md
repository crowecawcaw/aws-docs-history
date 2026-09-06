

# Query requests for Amazon EC2
<a name="Query-Requests"></a>

Query requests are HTTP or HTTPS requests that use the HTTP verb GET or POST and a Query parameter named `Action`. For each Amazon EC2 API action, you can choose whether to use GET or POST. Regardless of which verb you choose, the same data is sent and received. For a list of Amazon EC2 API actions, see [Actions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/query-apis.html).

**Topics**
+ [Structure of a GET request](#structure-of-a-get-request)
+ [Query parameters](#query-parameters)
+ [Query API authentication](#query-authentication)
+ [Query response structures](#api-responses)
+ [Pagination](#api-pagination)
+ [Preventing requests over HTTP](#prevent-http-requests)

## Structure of a GET request
<a name="structure-of-a-get-request"></a>

The Amazon EC2 documentation presents the GET requests as URLs, which can be used directly in a browser.

**Note**  
Because the GET requests are URLs, you must URL encode the parameter values. In the Amazon EC2 documentation, we leave the example GET requests unencoded to make them easier to read.

The request consists of the following:
+ **Endpoint**: The URL that serves as the entry point for the web service. For more information, see [Amazon EC2 service endpoints](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-endpoints.html).
+ **Action**: The action that you want to perform; for example, use `RunInstances` to launch an instance.
+ **Parameters**: Any parameters for the action; each parameter is separated by an ampersand (&).
+ **Version**: The API version to use. For the Amazon EC2 API, the version is 2016-11-15.
+ **Authorization parameters**: The authorization parameters that AWS uses to ensure the validity and authenticity of the request. Amazon EC2 supports Signature Version 2 and Signature Version 4. We recommend that you use Signature Version 4. For more information, see [Signing AWS API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html) in the *IAM User Guide*.

The following optional parameters can be included in your request:
+ **DryRun**: Checks whether you have the required permissions for the action, without actually making the request. If you have the required permissions, the request returns `DryRunOperation`; otherwise, it returns `UnauthorizedOperation`.
+ **SecurityToken**: The temporary security token obtained through a call to AWS Security Token Service.

For more information about common parameters for API requests, see [Common query parameters](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/CommonParameters.html).

The following is an example request that launches instances:

```
https://ec2.amazonaws.com/?Action=RunInstances&ImageId=ami-2bb65342&MaxCount=3&MinCount=1&Placement.AvailabilityZone=us-east-1a&Monitoring.Enabled=true&Version=2016-11-15&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIDEXAMPLE%2F20130813%2Fus-east-1%2Fec2%2Faws4_request&X-Amz-Date=20130813T150206Z&X-Amz-SignedHeaders=content-type%3Bhost%3Bx-amz-date&X-Amz-Signature=525d1a96c69b5549dd78dbbec8efe264102288b83ba87b7d58d4b76b71f59fd2
Content-type: application/json
host:ec2.amazonaws.com
```

To make these example requests even easier to read, AWS documentation may present them in the following format:

```
https://ec2.amazonaws.com/?Action=RunInstances
&ImageId=ami-2bb65342
&MaxCount=3
&MinCount=1
&Placement.AvailabilityZone=us-east-1a
&Monitoring.Enabled=true
&Version=2016-11-15
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLEus-east-1%2Fec2%2Faws4_request
&X-Amz-Date=20130813T150206Z
&X-Amz-SignedHeaders=content-type%3Bhost%3Bx-amz-date
&X-Amz-Signature=ced6826de92d2bdeed8f846f0bf508e8559e98e4b0194b84example54174deb456c
Content-type: application/json
host:ec2.amazonaws.com
```

The first line specifies the endpoint of the request. After the endpoint is a question mark (?), which separates the endpoint from the parameters. For more information about Amazon EC2 endpoints, see [Amazon EC2 service endpoints](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-endpoints.html). 

The `Action` parameter indicates the action to perform. For a complete list of actions, see [Actions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/query-apis.html). The remaining lines specify additional parameters for the request.

In the example Query requests we present in the Amazon EC2 API documentation, we omit the headers, [common required parameters](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/CommonParameters.html), and authentication parameters to make it easier for you to focus on the parameters for the action. We replace them with the `&AUTHPARAMS` literal string to remind you that you must include these parameters in your request; for example:

```
https://ec2.amazonaws.com/?Action=RunInstances
&ImageId=ami-2bb65342
&MaxCount=3
&MinCount=1
&Placement.AvailabilityZone=us-east-1a
&Monitoring.Enabled=true
&AUTHPARAMS
```

**Important**  
Before you specify your access key ID for the `AWSAccessKeyId` or `Credential` parameter, review and follow the guidance in [AWS security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html).

## Query parameters
<a name="query-parameters"></a>

Each Query request must include required common parameters to handle authentication and selection of an action. Query parameters are case sensitive.

Some operations take lists of parameters. These lists are specified using the *param.n* notation, where *n* is an integer starting from 1. 

The following example adds multiple devices to a block device mapping using a list of `BlockDeviceMapping` parameters.

```
http://ec2.amazonaws.com/?Action=RunInstances
&ImageId.1=ami-72aa081b
...
&BlockDeviceMapping.1.DeviceName=/dev/sdj
&BlockDeviceMapping.1.Ebs.NoDevice=true
&BlockDeviceMapping.2.DeviceName=/dev/sdh
&BlockDeviceMapping.2.Ebs.VolumeSize=300
&BlockDeviceMapping.3.DeviceName=/dev/sdc
&BlockDeviceMapping.3.VirtualName=ephemeral1
&AUTHPARAMS
```

## Query API authentication
<a name="query-authentication"></a>

You can send Query requests over either the HTTP or HTTPS protocol.

Regardless of which protocol you use, you must include a signature in every Query request. Amazon EC2 supports Signature Version 2 and Signature Version 4. We recommend that you use Signature Version 4. For more information, see [Signing AWS API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html) in the *IAM User Guide*.

Signature Version 4 requests allow you to specify all the authorization parameters in a single header, for example:

```
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Amz-Date: 20130813T150211Z
Host: ec2.amazonaws.com
Authorization: AWS4-HMAC-SHA256 Credential=AKIDEXAMPLE/202230813/us-east-1/ec2/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature=ced6826de92d2bdeed8f846f0bf508e8559e98e4b0194b84example54174deb456c

http://ec2.amazonaws.com/?Action=RunInstances
ImageId=ami-2bb65342
&MaxCount=3
&MinCount=1
&Monitoring.Enabled=true
&Placement.AvailabilityZone=us-east-1a
&Version=2016-11-15
```

## Query response structures
<a name="api-responses"></a>

In response to a Query request, the service returns an XML data structure that conforms to an XML schema defined for Amazon EC2. The structure of an XML response is specific to the associated request. In general, the response data types are named according to the operation performed and whether the data type is a container (can have children). Examples of containers include `groupSet` for security groups and `keySet` for key pairs (see the example that follows). Item elements are children of containers, and their contents vary according to the container's role.

Every successful response includes a request ID in a `requestId` element, and every unsuccessful response includes a request ID in a `RequestID` element. The value is a unique string that AWS assigns. If you ever have issues with a particular request, AWS will ask for the request ID to help troubleshoot the issue. The following shows an example response.

```
<DescribeKeyPairsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
  <keySet>
    <item>
      <keyName>gsg-keypair</keyName>
      <keyFingerprint>
         00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00
      </keyFingerprint>
    </item>
  </keySet>
</DescribeKeyPairsResponse>
```

**Considerations**
+ As of July 31 2024, for any new Amazon EC2 API actions or newly supported AWS Regions, the XML data structures in the responses won't include new lines and indentations. If you use a custom client, ensure that it does not rely on the responses including new lines and indentations.
+ As of July 31 2025, the XML data structures in the responses will no longer include new lines and indentations. This change will reduce the size of the responses. If you use a custom client, ensure that it does not rely on the responses including new lines and indentations.
+ The order of the elements in the response, including those within nested structures, might vary. Applications should not assume that the elements appear in a particular order.

## Pagination
<a name="api-pagination"></a>

For actions that can return a long list of items, the Amazon EC2 API includes parameters to support pagination: `MaxResults`, `NextToken` (input), and `nextToken` (output). With pagination, you specify a size for `MaxResults` and then each call returns 0 to `MaxResults` items and sets `nextToken`. If there are additional items to iterate, `nextToken` is non-null and you can specify its value in the `NextToken` parameter of a subsequent call to get the next set of items. With pagination, you continue to call the action until `nextToken` is null, even if you receive less than `MaxResults` items, including zero items.

If you call a describe API action with both a list of IDs and `MaxResults`, the request fails with the error `InvalidParameterCombination`.

We recommend that you use pagination when using describe actions that can potentially return a large number of results, such as `DescribeInstances`. Using pagination bounds the number of items returned and the time it takes for these calls to return.

For more information, see [Pagination](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-pagination.html) in the *Amazon EC2 Developer Guide*.

## Preventing requests over HTTP
<a name="prevent-http-requests"></a>

If your workload does not require you to use HTTP, we recommend that you avoid using it to prevent transmitting and receiving unencrypted data, and to use HTTPS instead. You can use the [`aws:SecureTransport`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-securetransport) global IAM condition key in your IAM policies to prevent users from sending requests over HTTP.

The following example policy prevents users from sending requests over HTTP.

```
{
    "Statement": [
        {
            "Sid": "AllowAllEC2HttpsRequests",
            "Effect": "Allow",
            "Action": "ec2:*",
            "Resource": "*",
            "Condition": {
                "StringEqualsIgnoreCase": {
                    "aws:SecureTransport": "true"
                }
            }
        }
    ]
}
```