

# Route requests to endpoints in other AWS accounts

With an inference router, you can send requests to an endpoint or inference component that another AWS account owns. Both accounts must allow it:

1. The *endpoint owner* attaches an endpoint policy (a resource-based policy) that allows the router's account to invoke the endpoint through that router.

1. The *router owner* allows its callers to invoke the router and the destination, and adds the destination to a routing target.

The caller's identity needs permission in both accounts. For the reason, see [How the router authorizes requests to destinations](inference-router-security.md#inference-router-security-confused-deputy).

## Example endpoint policy
<a name="inference-router-endpoint-policy-example"></a>

The endpoint owner (account {{444455556666}}) runs the following command in the endpoint's AWS Region. The first statement lets account {{111122223333}} invoke the endpoint only through {{my-router}}. The second lets that account describe the endpoint, so SageMaker AI can show its `RoutingStatus` and check its mode.

```bash
aws sagemaker put-endpoint-policy \
    --region {{eu-west-1}} \
    --endpoint-name {{shared-endpoint}} \
    --resource-policy '{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "InvokeThroughRouter",
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::{{111122223333}}:root" },
      "Action": "sagemaker:InvokeEndpoint",
      "Resource": "arn:aws:sagemaker:{{eu-west-1}}:{{444455556666}}:endpoint/{{shared-endpoint}}",
      "Condition": {
        "ArnEquals": {
          "sagemaker:SourceInferenceRouterArn": "arn:aws:sagemaker:{{us-west-2}}:{{111122223333}}:inference-router/{{my-router}}"
        }
      }
    },
    {
      "Sid": "DescribeForRouterAccount",
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::{{111122223333}}:root" },
      "Action": "sagemaker:DescribeEndpoint",
      "Resource": "arn:aws:sagemaker:{{eu-west-1}}:{{444455556666}}:endpoint/{{shared-endpoint}}"
    }
  ]
}'
```

In the command, replace the following values:
+ {{444455556666}} – the account ID of the endpoint owner.
+ {{111122223333}} – the account ID of the router owner.
+ {{shared-endpoint}} – the name of your endpoint.
+ {{my-router}} – the name of the inference router.
+ {{eu-west-1}} – the endpoint's Region.
+ {{us-west-2}} – the router's Region.

To share an inference component, add the inference component ARN to the `Resource` of both statements, together with the endpoint ARN, and add `sagemaker:DescribeInferenceComponent` to the second statement.

For an asynchronous endpoint, allow `sagemaker:InvokeEndpointAsync` in the first statement instead of `sagemaker:InvokeEndpoint`.

## Allow callers in the router account
<a name="inference-router-cross-account-router-side"></a>

As the router owner (account {{111122223333}}), attach a policy like the following to the IAM identities that invoke the router. It allows the caller to invoke {{my-router}}, and to invoke and describe the shared endpoint in account {{444455556666}}.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "InvokeRouter",
      "Effect": "Allow",
      "Action": "sagemaker:InvokeInferenceRouter",
      "Resource": "arn:aws:sagemaker:us-west-2:{{111122223333}}:inference-router/{{my-router}}"
    },
    {
      "Sid": "InvokeAndDescribeSharedEndpoint",
      "Effect": "Allow",
      "Action": [
        "sagemaker:InvokeEndpoint",
        "sagemaker:DescribeEndpoint"
      ],
      "Resource": "arn:aws:sagemaker:eu-west-1:{{444455556666}}:endpoint/{{shared-endpoint}}"
    }
  ]
}
```

For an asynchronous routing target, allow `sagemaker:InvokeInferenceRouterAsync` and `sagemaker:InvokeEndpointAsync` instead of `sagemaker:InvokeInferenceRouter` and `sagemaker:InvokeEndpoint`, and add the permissions in [Permissions for asynchronous requests](inference-router-async.md#inference-router-async-permissions).

Then add the shared endpoint's ARN as a destination in a routing target with `CreateInferenceRouter` or `UpdateInferenceRouter`, as shown in [Get started with inference routers](inference-router-get-started.md). The following example shows the destination entry to add to the routing target.

```json
{ "ResourceArn": "arn:aws:sagemaker:eu-west-1:{{444455556666}}:endpoint/{{shared-endpoint}}" }
```

## Endpoint policy rules
<a name="inference-router-endpoint-policy-rules"></a>

SageMaker AI rejects an endpoint policy that doesn't follow these rules.
+ `Version` must be `2012-10-17`. The policy must contain only ASCII characters and must be within the size quota in [Quotas and limits](inference-router.md#inference-router-quotas).
+ `Effect` must be `Allow`. `NotPrincipal`, `NotAction`, and `NotResource` aren't supported.
+ `Principal` must name each AWS account (account ID or `root` ARN) or IAM role explicitly in the `AWS` form. Wildcard (`*`), service, federated, and IAM group principals aren't supported. Principals must exist when you put the policy.
+ `Action` can be `sagemaker:InvokeEndpoint`, `sagemaker:InvokeEndpointAsync`, `sagemaker:InvokeEndpointWithResponseStream`, `sagemaker:DescribeEndpoint`, and `sagemaker:DescribeInferenceComponent`. Wildcards aren't supported. Allowing `sagemaker:InvokeEndpointWithResponseStream` has no effect for inference routers.
+ `Resource` must be the endpoint's ARN or the ARNs of inference components in the same account and Region.
+ `Condition` operators can be `ArnEquals`, `ArnLike`, `StringEquals`, and `StringLike`. Condition keys can be `sagemaker:SourceInferenceRouterArn`, `sagemaker:TargetModel`, and `sagemaker:TargetContainerHostname`.
+ `Condition` must include a `sagemaker:SourceInferenceRouterArn` key that names an inference router in every statement that allows another account to invoke the endpoint. We recommend `ArnEquals` with the full router ARN.
+ The `sagemaker:SourceInferenceRouterArn` value must be an inference router ARN in the endpoint's partition, with a 12-digit account ID. Wildcards (`*` or `?`) aren't allowed in the partition, service, or account ID. With `ArnLike` or `StringLike`, you can use wildcards in the Region and the router name. With `ArnEquals` or `StringEquals`, wildcards aren't allowed.
+ A statement that allows `sagemaker:DescribeEndpoint` or `sagemaker:DescribeInferenceComponent` can't have a `Condition`. Grant these actions in their own statement, as in the example above.

You can't put an endpoint policy on an endpoint that is being deleted or that has failed (status `Deleting` or `Failed`).

To manage the policy, use `PutEndpointPolicy`, `GetEndpointPolicy`, and `DeleteEndpointPolicy`. `PutEndpointPolicy` replaces the whole policy. To change one statement, get the current policy, edit it, and put it back. `GetEndpointPolicy` returns a `ValidationException` if the endpoint has no policy.

## Revoke access
<a name="inference-router-endpoint-policy-revoke"></a>

To revoke one account, put the policy again without that account's statements. To revoke every account, run `delete-endpoint-policy`. Changes typically take effect within 30 seconds, and can take up to 5 minutes.

After access is revoked, the destination denies requests from the router, and your callers can get `ServiceUnavailableException` (503). If `sagemaker:DescribeEndpoint` is also removed, the destination's `RoutingStatus` becomes `Unknown`. Neither account is notified. If you own the router, remove the destination with `UpdateInferenceRouter`. If you own the endpoint, tell the router owner that you revoked access.

If you delete an endpoint and create a new one with the same name, the new endpoint has no policy. As the endpoint owner, put the policy again on the new endpoint.

## Set up cross-account access with AWS CloudFormation
<a name="inference-router-cloudformation"></a>

You can create inference routers and endpoint policies with the AWS CloudFormation resource types `AWS::SageMaker::InferenceRouter` and `AWS::SageMaker::EndpointPolicy`. For `AWS::SageMaker::EndpointPolicy`, the endpoint must be in the same AWS account and AWS Region as the stack, so a router and an endpoint policy in different accounts need a stack in each account. For the properties of each type, see [AWS::SageMaker::InferenceRouter](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-inferencerouter.html) and [AWS::SageMaker::EndpointPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-endpointpolicy.html) in the *CloudFormation Template Reference*.

The endpoint owner (account {{444455556666}}) deploys the following template in {{eu-west-1}} first. It allows account {{111122223333}} to invoke the endpoint only through {{my-router}}.

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  SharedEndpointPolicy:
    Type: AWS::SageMaker::EndpointPolicy
    Properties:
      EndpointArn: arn:aws:sagemaker:{{eu-west-1}}:{{444455556666}}:endpoint/{{shared-endpoint}}
      PolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Sid: InvokeThroughRouter
            Effect: Allow
            Principal:
              AWS: arn:aws:iam::{{111122223333}}:root
            Action: sagemaker:InvokeEndpoint
            Resource: arn:aws:sagemaker:{{eu-west-1}}:{{444455556666}}:endpoint/{{shared-endpoint}}
            Condition:
              ArnEquals:
                sagemaker:SourceInferenceRouterArn: arn:aws:sagemaker:{{us-west-2}}:{{111122223333}}:inference-router/{{my-router}}
          - Sid: DescribeForRouterAccount
            Effect: Allow
            Principal:
              AWS: arn:aws:iam::{{111122223333}}:root
            Action: sagemaker:DescribeEndpoint
            Resource: arn:aws:sagemaker:{{eu-west-1}}:{{444455556666}}:endpoint/{{shared-endpoint}}
```

To avoid drift, specify principals as full ARNs, as in this example. For the policy rules, see [Endpoint policy rules](#inference-router-endpoint-policy-rules).

The router owner (account {{111122223333}}) then deploys the following template in {{us-west-2}}. It creates a router with one routing target and two destinations: an endpoint in the router owner's account and the shared endpoint.

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  MyRouter:
    Type: AWS::SageMaker::InferenceRouter
    Properties:
      InferenceRouterName: {{my-router}}
      RoutingTargets:
        - Name: {{my-model}}
          Destinations:
            - ResourceArn: arn:aws:sagemaker:{{us-west-2}}:{{111122223333}}:endpoint/{{my-endpoint-usw2}}
            - ResourceArn: arn:aws:sagemaker:{{eu-west-1}}:{{444455556666}}:endpoint/{{shared-endpoint}}
```

In the templates, replace the following values:
+ {{444455556666}} – the account ID of the endpoint owner.
+ {{111122223333}} – the account ID of the router owner.
+ {{shared-endpoint}} and {{my-endpoint-usw2}} – the names of your endpoints.
+ {{my-router}} – the name of the inference router. Specify a name, so that the endpoint policy can refer to the router's ARN.
+ {{my-model}} – the name of the routing target that callers pass on each request.
+ {{eu-west-1}} – the endpoint's Region.
+ {{us-west-2}} – the router's Region.

Changing `InferenceRouterName` replaces the router and changes its ARN, so also update the endpoint policies and IAM policies that refer to it.