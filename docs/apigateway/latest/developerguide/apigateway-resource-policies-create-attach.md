# Create and attach an API Gateway

resource policy to an API

To allow a user to access your API by calling the API execution service, you must create an API Gateway resource
policy and attach the policy to the API. When you attach a policy to your API, it applies
the permissions in the policy to the methods in the API. If you update the resource policy, you'll need to deploy
the API.

###### Topics

- [Prerequisites](#apigateway-resource-policies-prerequisites "#apigateway-resource-policies-prerequisites")
- [Attach a resource policy to an API Gateway
  API](#apigateway-resource-policies-create-attach-procedure "#apigateway-resource-policies-create-attach-procedure")
- [Troubleshoot your resource policy](#apigateway-resource-policies-troubleshoot "#apigateway-resource-policies-troubleshoot")

## Prerequisites

To update an API Gateway resource policy, you'll need the `apigateway:UpdateRestApiPolicy`
permission and the `apigateway:PATCH` permission.

For an edge-optimized or Regional API, you can attach your resource policy to your API as you create
it, or after it has been deployed. For a private API, you can't deploy your API without a resource policy. For
more information, see [Private REST APIs in API Gateway](apigateway-private-apis.md "apigateway-private-apis.md").

## Attach a resource policy to an API Gateway

API

The following procedure shows you how to attach a resource policy to an API Gateway API.

AWS Management Console

###### To attach a resource policy to an API Gateway API

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway "https://console.aws.amazon.com/apigateway").
2. Choose a REST API.
3. In the main navigation pane, choose **Resource policy**.
4. Choose **Create policy**.
5. (Optional) Choose **Select a template** to generate an example policy.

In the
example policies, placeholders are enclosed in double curly braces
(`"{{`placeholder`}}"`). Replace
each of the placeholders, including the curly braces, with the necessary
information. 6. If you don't use one of the template examples, enter your
resource policy. 7. Choose **Save changes**.

If the API has been deployed previously in the API Gateway console, you'll need to
redeploy it for the resource policy to take effect.

AWS CLI
To use the AWS CLI to create a new API and attach a resource policy to it, use the following
[create-rest-api](../../../cli/latest/reference/apigateway/create-rest-api.md "../../../cli/latest/reference/apigateway/create-rest-api.md") command:

```
aws apigateway create-rest-api \
    --name "`api-name`" \
    --policy "{\"`jsonEscapedPolicyDocument`\"}"
```

To use the AWS CLI to attach a resource policy to an existing API, use the following [update-rest-api](../../../cli/latest/reference/apigateway/update-rest-api.md "../../../cli/latest/reference/apigateway/update-rest-api.md") command:

```
aws apigateway update-rest-api \
    --rest-api-id `api-id` \
    --patch-operations op=replace,path=/policy,value='"{\"`jsonEscapedPolicyDocument`\"}"'
```

You can also attach your resource policy as a separate `policy.json` file and including it
in your [create-rest-api](../../../cli/latest/reference/apigateway/create-rest-api.md "../../../cli/latest/reference/apigateway/create-rest-api.md") command. The
following [create-rest-api](../../../cli/latest/reference/apigateway/create-rest-api.md "../../../cli/latest/reference/apigateway/create-rest-api.md") command
creates a new API with a resource policy:

```
aws apigateway create-rest-api \
    --name "`api-name`" \
    --policy file://policy.json
```

`policy.json` is an API Gateway resource policy, such as
[Example:
Deny API traffic based on source IP address or range](apigateway-resource-policies-examples.md#apigateway-resource-policies-source-ip-address-example "apigateway-resource-policies-examples.md#apigateway-resource-policies-source-ip-address-example").

AWS CloudFormation
You can use AWS CloudFormation to create an API with a resource policy. The following example creates a REST API
with the example resource policy, [Example:
Deny API traffic based on source IP address or range](apigateway-resource-policies-examples.md#apigateway-resource-policies-source-ip-address-example "apigateway-resource-policies-examples.md#apigateway-resource-policies-source-ip-address-example").

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  Api:
    Type: 'AWS::ApiGateway::RestApi'
    Properties:
      Name: testapi
      Policy:
        Statement:
          - Action: 'execute-api:Invoke'
            Effect: Allow
            Principal: '*'
            Resource: 'execute-api:/*'
          - Action: 'execute-api:Invoke'
            Effect: Deny
            Principal: '*'
            Resource: 'execute-api:/*'
            Condition:
              IpAddress:
                'aws:SourceIp': ["192.0.2.0/24", "198.51.100.0/24" ]
        Version: 2012-10-17
  Resource:
    Type: 'AWS::ApiGateway::Resource'
    Properties:
      RestApiId: !Ref Api
      ParentId: !GetAtt Api.RootResourceId
      PathPart: 'helloworld'
  MethodGet:
    Type: 'AWS::ApiGateway::Method'
    Properties:
      RestApiId: !Ref Api
      ResourceId: !Ref Resource
      HttpMethod: GET
      ApiKeyRequired: false
      AuthorizationType: NONE
      Integration:
        Type: MOCK
        RequestTemplates:
          application/json: '{"statusCode": 200}'
        IntegrationResponses:
          - StatusCode: 200
            ResponseTemplates:
              application/json: '{}'
      MethodResponses:
        - StatusCode: 200
          ResponseModels:
            application/json: 'Empty'
  ApiDeployment:
    Type: 'AWS::ApiGateway::Deployment'
    DependsOn:
      - MethodGet
    Properties:
      RestApiId: !Ref Api
      StageName: test
```

## Troubleshoot your resource policy

The following troubleshooting guidance might help resolve issues with your resource policy.

### My API returns {"Message":"User: anonymous is

not authorized to perform: execute-api:Invoke on resource:
arn:aws:execute-api:us-east-1:\*\*\*\*\*\*\*\*/\*\*\*\*/\*\*\*\*/"}

In your resource policy, if you set the Principal to an AWS principal, such as the following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::111111111111:role/developer",
 "arn:aws:iam::111111111111:role/Admin"
 ]
 },
 "Action": "execute-api:Invoke",
 "Resource": [
 "execute-api:/stage/GET/pets"
 ]
 }
 ]
}`

```

You must use `AWS_IAM` authorization for every method in your API, or else your API returns the
previous error message. For more instructions on how to turn on `AWS_IAM` authorization for a
method, see [Methods for REST APIs in API Gateway](how-to-method-settings.md "how-to-method-settings.md").

### My resource policy is not updating

If you update the resource policy after the API is created, you'll need to deploy the API to propagate
the changes after you've attached the updated policy. Updating or saving the policy alone won't change the
runtime behavior of the API. For more information about deploying your API, see [Deploy REST APIs in API Gateway](how-to-deploy-api.md "how-to-deploy-api.md").

### My resource policy returns the following error: Invalid policy document. Please

check the policy syntax and ensure that Principals are valid.

To troubleshoot this error, we first recommend that you check the policy syntax. For more information, see
[Access policy
language overview for Amazon API Gateway](apigateway-control-access-policy-language-overview.md "apigateway-control-access-policy-language-overview.md"). We also recommend that you check
that all the principals specified are valid and haven’t been deleted.

In addition, if your API is in an [opt-in
Region](../../../glossary/latest/reference/glos-chap.md#optinregion "../../../glossary/latest/reference/glos-chap.md#optinregion"), verify that all accounts in the resource policy have the Region enabled.
