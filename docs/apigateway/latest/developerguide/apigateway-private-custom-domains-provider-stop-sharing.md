# API provider: Stop sharing a private custom domain name using AWS RAM

To stop sharing your private custom domain name, first you stop the API consumer from creating more domain
name access associations by dissociating the resource share. Then, you reject the domain name access
association and remove the API consumer's VPC endpoint from your `policy` for the
`execute-api` service. The API consumer can then delete their
domain name access association.

## Stop sharing your private custom domain name

First, you stop the resource share using AWS RAM.

AWS Management ConsoleTo use the AWS Management Console, see [Update a resource share in AWS RAM](../../../ram/latest/userguide/working-with-sharing-update.md "../../../ram/latest/userguide/working-with-sharing-update.md").

AWS CLI
The following [disassociate-resource-share](../../../cli/latest/reference/ram/disassociate-resource-share.md "../../../cli/latest/reference/ram/disassociate-resource-share.md") disassociates a resource share for your private custom domain
name.

```
aws ram disassociate-resource-share \
    --region us-west-2 \
    --resource-arns arn:aws:apigateway:us-west-2:111122223333:/domainnames/private.example.com+abcd1234 \
    --principals 222222222222
```

## Reject the domain name access association

After you stop sharing your resource using AWS RAM, you reject the domain name access association between a VPC endpoint in another account and
your private custom domain name.

###### Note

You can't reject a domain name access association in your own account. To
stop resource sharing, delete the domain name access association. For more information, see [Delete a domain name access association](apigateway-private-custom-domains-tutorial.md#apigateway-private-custom-domains-cleanup "apigateway-private-custom-domains-tutorial.md#apigateway-private-custom-domains-cleanup").

When you reject a domain name access association with
a VPC endpoint, if an API consumer tries to call your private custom domain name, API Gateway rejects the call and
returns a `403` status code.

AWS Management Console

###### To reject a domain name access association

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway "https://console.aws.amazon.com/apigateway").
2. In the main navigation pane, choose **Custom domain names**.
3. Choose the private custom domain name that you shared with other AWS accounts.
4. On the **Resource sharing**, choose the domain name access association you want
   to reject.
5. Choose **Reject association**.
6. Confirm your choice, and then choose **Reject**.

AWS CLIThe following `reject-domain-name-access-association` command rejects the domain name access association between the VPC
endpoint and your private custom domain name:

```
aws apigateway reject-domain-name-access-association \
    --domain-name-access-association-arn arn:aws:apigateway:us-west-2:444455556666:/domainnameaccessassociations/domainname/private.example.com+abcd1234/vpcesource/vpce-abcd1234efg \
    --domain-name-arn arn:aws:apigateway:us-west-2:111122223333:/domainnames/private.example.com+abcd1234
```

## Deny the API provider access to invoke your private custom domain name

After you reject the domain name access association, you remove the API consumer's VPC endpoint from your `policy` for the
`execute-api` service.

AWS Management Console

###### To remove the API consumer's VPC endpoint from your resource policy

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway "https://console.aws.amazon.com/apigateway").
2. In the main navigation pane, choose **Custom domain names**.
3. Choose the private custom domain name that you shared with other AWS accounts.
4. On the **Resource policy** tab, choose **Edit**.
5. Remove the VPC endpoint from the policy.
6. Choose **Save changes**.

AWS CLI
The following [update-domain-name](../../../cli/latest/reference/apigateway/update-domain-name.md "../../../cli/latest/reference/apigateway/update-domain-name.md") command uses a patch operation to update the `policy` for
the `execute-api` service for a private custom domain name. This new
`policy` removes an additional VPC endpoint ID added in
[Allow other accounts to invoke your private custom domain name](apigateway-private-custom-domains-provider-share.md#apigateway-private-custom-domains-provider-policy-update "apigateway-private-custom-domains-provider-share.md#apigateway-private-custom-domains-provider-policy-update"):

```
aws apigateway update-domain-name
    --domain-name private.example.com \
    --domain-name-id abcd1234 \
    --patch-operations op=replace,path=/policy,value='"{\"Version\": \"2012-10-17\",		 	 	 \"Statement\": [{\"Effect\": \"Allow\",\"Principal\": \"*\",\"Action\": \"execute-api:Invoke\",\"Resource\":[\"execute-api:/*\"]},{\"Effect\": \"Deny\",\"Principal\": \"*\",\"Action\": \"execute-api:Invoke\",\"Resource\":[\"execute-api:/*\"],\"Condition\":{\"StringNotEquals\":{\"aws:SourceVpce\": \"vpce-abcd1234efg\"}}}]}"
```

The API consumer should then delete the domain name access association. You can't delete it for them. For
more information, see [API consumer: Delete your domain name access association with a private custom domain name](apigateway-private-custom-domains-consumer-delete-domain-name-access-association.md "apigateway-private-custom-domains-consumer-delete-domain-name-access-association.md").
