

# Restrict direct access to Memory
<a name="memory-gateway-restrict-access"></a>

The fine-grained access control policies on your gateway govern requests that arrive *through the gateway*. They do not stop a principal that has IAM permissions on the Memory resource from calling the Memory data plane directly and bypassing the gateway. To ensure Memory can only be reached through your gateway, attach a resource-based policy to the Memory resource that allows access only when the request was forwarded by that gateway. This is a JSON resource-based policy on Memory, not a Cedar policy, and it complements the Cedar policies on your gateway.

The gateway stamps the `aws:SourceArn` condition key with its gateway ARN on every request it forwards, in both outbound credential modes. The following resource-based policy allows Memory access only when `aws:SourceArn` matches your gateway ARN. Replace the example account, Region, resource ids, and caller principal with your own.

```
{
"Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AllowOnlyThroughGateway",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:role/CallerRole"
      },
      "Action": "bedrock-agentcore:*",
      "Resource": "arn:aws:bedrock-agentcore:us-east-1:123456789012:memory/<memory-id>",
      "Condition": {
        "ArnEquals": {
          "aws:SourceArn": "arn:aws:bedrock-agentcore:us-east-1:123456789012:gateway/<gateway-id>"
        }
      }
    }
  ]
}
```

**Note**  
The gateway stamps `aws:SourceArn` in both outbound credential modes, so this policy works regardless of the mode you use. The `Principal` you specify differs by mode, because it must match the identity Memory authorizes: with `CALLER_IAM_CREDENTIALS`, that is the caller’s IAM identity; with `GATEWAY_IAM_ROLE`, it is the gateway execution role. For more information, see [How the outbound credential mode affects Memory access control](memory-gateway-connector.md#memory-gateway-connector-credential-modes) and [Resource-based policies for Amazon Bedrock AgentCore](resource-based-policies.md).