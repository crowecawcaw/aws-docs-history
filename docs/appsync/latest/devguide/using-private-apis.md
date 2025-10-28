# Using AWS AppSync Private APIs

If you use Amazon Virtual Private Cloud (Amazon VPC), you can create AWS AppSync Private APIs, which are APIs that can only be accessed from
a VPC. With a Private API, you can restrict API access to your internal applications and connect to your GraphQL and
Realtime endpoints without exposing data publicly.

To establish a private connection between your VPC and the AWS AppSync service, you must create
interface VPC endpoints. Interface endpoints are powered by [AWS PrivateLink](http://aws.amazon.com/privatelink "http://aws.amazon.com/privatelink"), which enables you to privately
access AWS AppSync APIs without an internet gateway, NAT device, VPN connection, or AWS Direct Connect
connection. Instances in your VPC don't need public IP addresses to communicate with AWS AppSync
APIs. Traffic between your VPC and AWS AppSync doesn't leave the AWS network.

AWS AppSync supports AWS PrivateLink for both data plane and control plane operations:

- **Data plane endpoint** (`com.amazonaws.{region}.appsync-api`):
  Provides private access to your GraphQL and Real-time APIs for querying, mutations, and subscriptions.
- **Control plane endpoint** (`com.amazonaws.{region}.appsync`):
  Provides private access to AWS AppSync management operations such as creating APIs, updating schemas,
  and configuring data sources.

![AWS Cloud architecture showing VPC with public and private subnets connecting to AWS AppSync via PrivateLink.](images/private-api-architecture.png)
There are some additional factors to consider before enabling Private API features:

- Setting up VPC interface endpoints for AWS AppSync with Private DNS features enabled will prevent resources in
  the VPC from being able to invoke other AWS AppSync public APIs using the AWS AppSync generated API URL. This is due to
  the request to the public API being routed via the interface endpoint, which is not allowed for public APIs. To
  invoke public APIs in this scenario, it is recommended to configure custom domain names on public APIs, which
  can then be used by resources in the VPC to invoke the public API.
- Your AWS AppSync Private APIs will only be available from your VPC. The AWS AppSync console Query
  editor will only be able to reach your API if your browser's network configuration can route
  traffic to your VPC (e.g., connection via VPN or over AWS Direct Connect).
- With a VPC interface endpoint for AWS AppSync, you can access any Private API in the same AWS account and
  Region. To further restrict access to Private APIs, you can consider the following options:
  - Ensuring only the required administrators can create VPC endpoint interfaces for AWS AppSync.
  - Using VPC endpoint custom policies to restrict which APIs can be invoked from resources in the VPC.
  - For resources in the VPC, we recommend that you use IAM authorization to invoke AWS AppSync APIs by
    ensuring that the resources are given scoped-down roles to the APIs.

- When creating or using policies that restrict IAM principals, you must set the
  `authorizationType` of the method to `AWS_IAM` or `NONE`.

## Creating AWS AppSync Private APIs

The following steps below show you how to create Private APIs in the AWS AppSync service.

###### Warning

You can enable Private API features only during the creation of the API. This setting cannot be modified on
an AWS AppSync API or an AWS AppSync Private API after it has been created.

1. Sign in to the AWS Management Console and open the [AppSync console](https://console.aws.amazon.com/appsync/ "https://console.aws.amazon.com/appsync/").
   1. In the **Dashboard**, choose **Create
      API**.

2. Choose **Design an API from scratch**, then choose **Next**.
3. In the **Private API** section, choose **Use Private API features**.
4. Configure the rest of the options, review your API's data, then choose **Create**.

Before you can use your AWS AppSync Private API, you must configure interface endpoints for
AWS AppSync in your VPC. Note that both the Private API and VPC must be in the same AWS account
and Region.

## Creating interface endpoints for AWS AppSync

You can create interface endpoints for AWS AppSync using either the Amazon VPC console or the
AWS Command Line Interface (AWS CLI). Depending on your use case, you may need to create one or both endpoint types:

- **Data plane endpoint**: Required for accessing Private APIs from your VPC
- **Control plane endpoint**: Required for managing AWS AppSync resources from your VPC using the AWS CLI or SDKs

For more information, see [Creating an interface endpoint](../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint") in the _Amazon VPC User
Guide_.

###### Note

Make sure you select the right VPC endpoint service; there are two for AppSync:
`com.amazonaws.{region}.appsync-api` is the one required for private APIs while
`com.amazonaws.{region}.appsync` is used for API management.

Console

1.  Sign in to the AWS Management Console and open the [Endpoints](https://console.aws.amazon.com/vpc/home?#Endpoints "https://console.aws.amazon.com/vpc/home?#Endpoints") page of the Amazon VPC
    console.
2.  Choose **Create endpoint**.
    1.  In the **Service category** field, verify that **AWS services** is selected.
    2.  In the **Services** table, choose one of the following services:

            * For data plane access: `com.amazonaws.{region}.appsync-api`
            * For control plane access: `com.amazonaws.{region}.appsync`

        Verify that the **Type** column value is `Interface`.

    3.  In the **VPC** field, choose a VPC and its subnets.
    4.  To enable private DNS features for the interface endpoint, tick the **Enable
        DNS Name** check box.
    5.  In the **Security group** field, choose one or more security
        groups.

3.  Choose **Create endpoint**.
4.  Repeat the process to create the second endpoint type if needed.

CLI
Use the `create-vpc-endpoint` command and specify the VPC ID, VPC endpoint type (interface),
service name, subnets that will use the endpoint, and security groups to associate with the endpoint's
network interfaces.

**Create data plane endpoint:**

```
$ aws ec2 create-vpc-endpoint —vpc-id vpc-ec43eb89 \
  —vpc-endpoint-type Interface \
  —service-name com.amazonaws.{region}.appsync-api \
  —subnet-id subnet-abababab —security-group-id sg-1a2b3c4d
```

**Create control plane endpoint:**

```
$ aws ec2 create-vpc-endpoint —vpc-id vpc-ec43eb89 \
  —vpc-endpoint-type Interface \
  —service-name com.amazonaws.{region}.appsync \
  —subnet-id subnet-abababab —security-group-id sg-1a2b3c4d
```

To use the private DNS option, you must set the `enableDnsHostnames` and
`enableDnsSupportattributes` values of your VPC. For more information, see [Viewing
and updating DNS support for your VPC](../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-updating "../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-updating") in the _Amazon VPC User
Guide_. If you enable private DNS features for the interface endpoint, you can
make requests to your AWS AppSync API GraphQL and Real-time endpoint using its default public DNS
endpoints using the format below:

```
https://{api_url_identifier}.appsync-api.{region}.amazonaws.com/graphql
```

For control plane operations, you can use the standard AWS AppSync service endpoint:

```
https://appsync.{region}.amazonaws.com
```

For more information on service endpoints, see [Service endpoints and
quotas](../../../general/latest/gr/aws-service-information.md "../../../general/latest/gr/aws-service-information.md") in the _AWS General Reference_.

For more information on service interactions with interface endpoints, see [Accessing a service through an interface endpoint](../../../vpc/latest/privatelink/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/privatelink/vpce-interface.md#access-service-though-endpoint") in the _Amazon VPC User Guide_.

For information about creating and configuring an endpoint using AWS CloudFormation, see the [AWS::EC2::VPCEndpoint](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.md") resource in the _AWS CloudFormation User
Guide_.

## Advanced examples

If you enable private DNS features for the interface endpoint, you can make requests to your AWS AppSync API
GraphQL and Real-time endpoint using its default public DNS endpoints using the format below:

```
https://{api_url_identifier}.appsync-api.{region}.amazonaws.com/graphql
```

Using the interface VPC endpoint public DNS hostnames, the base URL to invoke the API will be in the following
format:

```
https://{vpc_endpoint_id}-{endpoint_dns_identifier}.appsync-api.{region}.vpce.amazonaws.com/graphql
```

You can also use the AZ-specific DNS hostname if you have deployed an endpoint in the AZ:

```
https://{vpc_endpoint_id}-{endpoint_dns_identifier}-{az_id}.appsync-api.{region}.vpce.amazonaws.com/graphql.
```

Using the VPC endpoint public DNS name will require the AWS AppSync API endpoint hostname to be passed as
`Host` or as a `x-appsync-domain` header to the request. These examples use a
`TodoAPI` that was created in the [Launch a sample
schema](quickstart-launch-a-sample-schema.md "quickstart-launch-a-sample-schema.md") guide:

```
curl https://{vpc_endpoint_id}-{endpoint_dns_identifier}.appsync-api.{region}.vpce.amazonaws.com/graphql \
-H "Content-Type:application/graphql" \
-H "x-api-key:da2-{xxxxxxxxxxxxxxxxxxxxxxxxxx}" \
-H "Host:{api_url_identifier}.appsync-api.{region}.amazonaws.com" \
-d '{"query":"mutation add($createtodoinput: CreateTodoInput!) {\n createTodo(input: $createtodoinput) {\n id\n name\n where\n when\n description\n }\n}","variables":{"createtodoinput":{"name":"My first GraphQL task","when":"Friday Night","where":"Day 1","description":"Learn more about GraphQL"}}}'
```

In the following examples, we will use the _Todo_ app that is generated in
the [Launch
a sample schema](quickstart-launch-a-sample-schema.md "quickstart-launch-a-sample-schema.md") guide. To test out the sample Todo API, we will be using the Private DNS to invoke the
API. You can use any command line tool of your choice; this example uses [curl](https://curl.se/ "https://curl.se/") to send queries and mutations and [wscat](https://www.npmjs.com/package/wscat "https://www.npmjs.com/package/wscat")
to set up subscriptions. To emulate our example, replace the values in brackets `{ }` in the commands
below with the corresponding values from your AWS account.

**Testing Mutation Operation – `createTodo` Request**

```
curl https://{api_url_identifier}.appsync-api.{region}.amazonaws.com/graphql \
-H "Content-Type:application/graphql" \
-H "x-api-key:da2-{xxxxxxxxxxxxxxxxxxxxxxxxxx}" \
-d '{"query":"mutation add($createtodoinput: CreateTodoInput!) {\n createTodo(input: $createtodoinput) {\n id\n name\n where\n when\n description\n }\n}","variables":{"createtodoinput":{"name":"My first GraphQL task","when":"Friday Night","where":"Day 1","description":"Learn more about GraphQL"}}}'
```

**Testing Mutation Operation – `createTodo` Response**

```
{
    "data": {
        "createTodo": {
            "id": "<todo-id>",
            "name": "My first GraphQL task",
            "where": "Day 1",
            "when": "Friday Night",
            "description": "Learn more about GraphQL"
        }
    }
}
```

**Testing Query Operation – `listTodos` Request**

```
curl https://{api_url_identifier}.appsync-api.{region}.amazonaws.com/graphql \
-H "Content-Type:application/graphql" \
-H "x-api-key:da2-{xxxxxxxxxxxxxxxxxxxxxxxxxx}" \
-d '{"query":"query ListTodos {\n listTodos {\n items {\n description\n id\n name\n when\n where\n }\n }\n}\n","variables":{"createtodoinput":{"name":"My first GraphQL task","when":"Friday Night","where":"Day 1","description":"Learn more about GraphQL"}}}'
```

**Testing Query Operation – `listTodos` Request**

```
{
  "data": {
    "listTodos": {
      "items": [
        {
          "description": "Learn more about GraphQL",
          "id": "<todo-id>",
          "name": "My first GraphQL task",
          "when": "Friday night",
          "where": "Day 1"
        }
      ]
    }
  }
}
```

**Testing Subscription Operation – Subscribing to `createTodo`
mutation**

To set up GraphQL subscriptions in AWS AppSync, see [Building a real-time
WebSocket client.](real-time-websocket-client.md "real-time-websocket-client.md") From an Amazon EC2 instance in a VPC, you can test your AWS AppSync Private API subscription
endpoint using [wscat](https://github.com/websockets/wscat "https://github.com/websockets/wscat"). The example below uses an `API
 KEY` for authorization.

```
$ header=`echo '{"host":"{api_url_identifier}.appsync-api.{region}.amazonaws.com","x-api-key":"da2-{xxxxxxxxxxxxxxxxxxxxxxxxxx}"}' | base64 | tr -d '\n'`
$ wscat -p 13 -s graphql-ws -c  "wss://{api_url_identifier}.appsync-realtime-api.us-west-2.amazonaws.com/graphql?header=$header&payload=e30="
Connected (press CTRL+C to quit)
> {"type": "connection_init"}
< {"type":"connection_ack","payload":{"connectionTimeoutMs":300000}}
< {"type":"ka"}
> {"id":"f7a49717","payload":{"data":"{\"query\":\"subscription onCreateTodo {onCreateTodo {description id name where when}}\",\"variables\":{}}","extensions":{"authorization":{"x-api-key":"da2-{xxxxxxxxxxxxxxxxxxxxxxxxxx}","host":"{api_url_identifier}.appsync-api.{region}.amazonaws.com"}}},"type":"start"}
< {"id":"f7a49717","type":"start_ack"}
```

Alternatively, use the VPC endpoint domain name while making sure to specify the **Host** header in the `wscat` command to establish the websocket:

```
$ header=`echo '{"host":"{api_url_identifier}.appsync-api.{region}.amazonaws.com","x-api-key":"da2-{xxxxxxxxxxxxxxxxxxxxxxxxxx}"}' | base64 | tr -d '\n'`
$ wscat -p 13 -s graphql-ws -c  "wss://{vpc_endpoint_id}-{endpoint_dns_identifier}.appsync-api.{region}.vpce.amazonaws.com/graphql?header=$header&payload=e30=" --header Host:{api_url_identifier}.appsync-realtime-api.us-west-2.amazonaws.com
Connected (press CTRL+C to quit)
> {"type": "connection_init"}
< {"type":"connection_ack","payload":{"connectionTimeoutMs":300000}}
< {"type":"ka"}
> {"id":"f7a49717","payload":{"data":"{\"query\":\"subscription onCreateTodo {onCreateTodo {description id priority title}}\",\"variables\":{}}","extensions":{"authorization":{"x-api-key":"da2-{xxxxxxxxxxxxxxxxxxxxxxxxxx}","host":"{api_url_identifier}.appsync-api.{region}.amazonaws.com"}}},"type":"start"}
< {"id":"f7a49717","type":"start_ack"}
```

Run the mutation code below:

```
curl https://{api_url_identifier}.appsync-api.{region}.amazonaws.com/graphql \
-H "Content-Type:application/graphql" \
-H "x-api-key:da2-{xxxxxxxxxxxxxxxxxxxxxxxxxx}" \
-d '{"query":"mutation add($createtodoinput: CreateTodoInput!) {\n createTodo(input: $createtodoinput) {\n id\n name\n where\n when\n description\n }\n}","variables":{"createtodoinput":{"name":"My first GraphQL task","when":"Friday Night","where":"Day 1","description":"Learn more about GraphQL"}}}'
```

Afterwards, a subscription is trigged, and the message notification appears as shown below:

```
< {"id":"f7a49717","type":"data","payload":{"data":{"onCreateTodo":{"description":"Go to the shops","id":"169ce516-b7e8-4a6a-88c1-ab840184359f","priority":5,"title":"Go to the shops"}}}}
```

## Control plane examples

With the control plane VPC endpoint configured, you can manage AWS AppSync resources from within your VPC using the AWS CLI or SDKs. Here are examples of common control plane operations:

**Creating an API using the AWS CLI**

```
aws appsync create-graphql-api \
  --name "MyPrivateAPI" \
  --authentication-type API_KEY \
  --visibility PRIVATE
```

**Updating a schema**

```
aws appsync start-schema-creation \
  --api-id {api-id} \
  --definition file://schema.graphql
```

**Creating a data source**

```
aws appsync create-data-source \
  --api-id {api-id} \
  --name "MyDataSource" \
  --type AWS_LAMBDA \
  --lambda-config lambdaFunctionArn=arn:aws:lambda:{region}:{account}:function:MyFunction
```

When using the control plane endpoint with private DNS enabled, these commands will automatically route through your VPC endpoint. If private DNS is not enabled, you can specify the endpoint URL:

```
aws appsync create-graphql-api \
  --endpoint-url https://{vpc_endpoint_id}-{endpoint_dns_identifier}.appsync.{region}.vpce.amazonaws.com \
  --name "MyPrivateAPI" \
  --authentication-type API_KEY \
  --visibility PRIVATE
```

## Using IAM policies to limit public API creation

AWS AppSync supports IAM [`Condition` statements](../../../service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.md "../../../service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.md") for use with Private APIs. The `visibility` field can be
included with IAM policy statements for the `appsync:CreateGraphqlApi` operation to control which
IAM roles and users can create private and public APIs. This gives an IAM administrator the ability to define
an IAM policy that will only allow a user to create a Private GraphQL API. A user attempting to create a public
API will receive an unauthorized message.

For example, an IAM administrator could create the following IAM policy statement to allow for the
creation of Private APIs:

```
{
    "Sid": "AllowPrivateAppSyncApis",
    "Effect": "Allow",
    "Action": "appsync:CreateGraphqlApi",
    "Resource": "*",
    "Condition": {
        "ForAnyValue:StringEquals": {
            "appsync:Visibility": "PRIVATE"
        }
    }
}
```

An IAM administrator could also add the following [service control policy](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") to block all users in an AWS organization from creating
AWS AppSync APIs other than Private APIs:

```
{
    "Sid": "BlockNonPrivateAppSyncApis",
    "Effect": "Deny",
    "Action": "appsync:CreateGraphqlApi",
    "Resource": "*",
    "Condition": {
        "ForAnyValue:StringNotEquals": {
            "appsync:Visibility": "PRIVATE"
        }
    }
}
```

## VPC PrivateLink support

VPC Privatelink support is available in AWS AppSync. PrivateLink allows you to use and interact
with an AWS Service without any traffic leaving the AWS network.

AWS AppSync supports AWS PrivateLink for both data plane and control plane operations.

- **VPCE endpoint**
  (`appsync.<region>.vpce.amazonaws.com`): Provides VPC access to data plane
  and control plane operations as follows:
  - **appsync** for control plane operations
  - **appsync-api** for data plane operations
