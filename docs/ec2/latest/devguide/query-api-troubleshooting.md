

# Troubleshooting API request errors
<a name="query-api-troubleshooting"></a>

In the Amazon EC2 Query API, errors codes are indicated as being either client or server. Client errors usually occur because there is a problem with the structure, content, or validity of the request. Server errors usually indicate a server-side issue. 

For more information about API error codes, see [Error Codes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/api-error-codes.html).

**Topics**
+ [Query API request rate](#api-request-rate)
+ [Eventual consistency](#api-eventual-consistency)
+ [Unauthorized operation](#unauthorized-operation)

## Query API request rate
<a name="api-request-rate"></a>

We throttle Amazon EC2 API requests for each AWS account on a per-Region basis to help the performance of the service. We ensure that all calls to the Amazon EC2 API (whether they originate from an application, calls to a command line interface, or the Amazon EC2 console) don't exceed the maximum allowed API request rate. The maximum API request rate may vary across Regions. Note that API requests made by users are attributed to the underlying AWS account.

For more information, see [Request throttling](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-throttling.html) in the *Amazon EC2 Developer Guide*.

## Eventual consistency
<a name="api-eventual-consistency"></a>

The Amazon EC2 API follows an eventual consistency model, due to the distributed nature of the system supporting the API. This means that the result of an API command you run that affects your Amazon EC2 resources might not be immediately visible to all subsequent commands you run. You should keep this in mind when you carry out an API command that immediately follows a previous API command.

For more information, see [Eventual consistency](https://docs.aws.amazon.com/ec2/latest/devguide/eventual-consistency.html) in the *Amazon EC2 Developer Guide*.

## Unauthorized operation
<a name="unauthorized-operation"></a>

By default, users, groups, and roles don't have permission to create or modify Amazon EC2 resources, or perform tasks using the Amazon EC2 API. You must explicitly grant permission through IAM policies. If a user attempts to perform an action for which permission has not been granted, the request returns the following error: `Client.UnauthorizedOperation`.

This error may occur when a policy is unintentionally restrictive. For example, to allow a user to launch instances into a specific subnet, you need to grant permissions for the following resources by specifying their ARNs in your IAM policy: instances, volumes, AMIs, the specific subnet, network interfaces, key pairs, and security groups. If you omit the permission for volumes, for example, the user is only able to launch an instance from an instance store-backed AMI, as they do not have permission to create the root EBS volume for an EBS-backed instance.

For more information about creating IAM policies for Amazon EC2, see [IAM policies for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html) in the *Amazon EC2 User Guide*.

For more information about which ARNs you can use with which Amazon EC2 API actions, see [Actions, resources, and condition keys for Amazon EC2](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html) in the *Service Authorization Reference*.