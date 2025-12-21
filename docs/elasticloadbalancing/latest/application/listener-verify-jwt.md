# Verify JWTs using an Application Load Balancer

You can configure an Application Load Balancer (ALB) to verify JSON Web Tokens (JWT) provided
by clients for secure service-to-service (S2S) or machine-to-machine
(M2M) communications. The load balancer can verify a JWT no matter
how it was issued and without human interaction.

ALB will validate the token signature and requires two mandatory claims: 'iss' (issuer) and 'exp' (expiration). Additionally, if present in the token, ALB will also validate 'nbf' (not before) and 'iat' (issued at time) claims.
You can configure up to 10 additional claims for validation. These claims support three formats:

- Single-string: A single text value
- Space-separated values: Multiple values separated by spaces (maximum 10 values)
- String-array: An array of text values (maximum 10 values)
  If the token is valid, the load balancer forwards the request with token as is to the target. Otherwise, it rejects the request.

## Prepare to use JWT verification

Complete the following tasks:

1. Register your service with an IdP, which issues a client ID and
   a client secret.
2. Make a separate call to the IdP to request access to a service.
   The IdP responds with an access token. This token is typically a
   JWT signed by the IdP.
3. Set up a JSON Web Key Sets (JWKS) endpoint. The load balancer acquires the
   public key published by the IdP in a well-known location that you configure.
4. Include the JWT in a request header, and forward it to the
   Application Load Balancer in every request.

# To configure JWT verification using console

1. Open the Amazon EC2 console console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**, choose **Load Balancers**.
3. Select your Application Load Balancer and choose the **Listeners** tab.
4. Select an HTTPS listener and choose **Manage rules**.
5. Choose **Add rule**.
6. (Optional) To specify a name for your rule, expand **Name and tags**, and enter the name. To add additional tags, choose **Add additional tags** and enter the tag key and tag value.
7. Under **Conditions**, define 1-5 condition values
8. (Optional) To add a transform, choose **Add transform**, choose the transform type, and enter a regular expression to match and a replacement string.
9. For **Actions, Pre-routing** action, choose **Validate token.**
   1. For **JWKS endpoint**, enter the URL of your JSON Web Key Set endpoint. This endpoint must be publicly accessible and return the public keys used to verify JWT signatures.
   2. For **Issuer**, enter the expected value of the iss claim in your JWT tokens.
   3. (Optional) To validate additional claims, choose **Additional claim.**
      1. For **Claim name**, enter the name of the claim to validate.
      2. For **Format**, choose how the claim values should be interpreted:
         1. **Single string**: The claim must match exactly one specified value.
         2. **String array**: The claim must match one of the values in an array.
         3. **Space separated values**: The claim contains space-separated values that must include the specified values.

      3. For **Values**, enter the expected values for the claim.
      4. Repeat for additional claims (maximum 10 claims).

10. For **Actions, Routing action**, select the primary action **(Forward to, Redirect to, or Return fixed response)** that should be performed after successful token validation.
11. Configure the primary action as needed
12. Choose **Save.**

## To configure JWT verification using CLI

Use the following [create-rule](../../../cli/latest/reference/elbv2/create-rule.md "../../../cli/latest/reference/elbv2/create-rule.md") command to configure JWT verification .

Create a listener rule with an action to verify JWTs. The listener must
be an HTTPS listener.

```
aws elbv2 create-rule \
    --listener-arn `listener-arn` \
    --priority `10` \
    --conditions Field=path-pattern,Values="`/login`" \
    --actions file://actions.json
```

The following is an example of the `actions.json` file that
specifies a `jwt-validation` action and a `forward`
action. Please follow documentation provided by
your identity provider to determine the fields that are supported

```
--actions '[
    {
        "Type":"jwt-validation",
        "JwtValidationConfig":{
            "JwksEndpoint":"`https://issuer.example.com/.well-known/jwks.json`",
            "Issuer":"`https://issuer.com`"
        },
        "Order":1
    },
    {
        "Type":"forward",
        "TargetGroupArn":"`target-group-arn`",
        "Order":2
    }
]'
```

The following example specifies an additional claim to validate.

```
--actions '[
    {
        "Type":"jwt-validation",
        "JwtValidationConfig":{
            "JwksEndpoint":"`https://issuer.example.com/.well-known/jwks.json`",
            "Issuer":"`https://issuer.com`",
            "AdditionalClaims":[
              {
                  "Format":"`string-array`",
                  "Name":"`claim_name`",
                  "Values":["`value1`","`value2`"]
              }
            ],
        },
        "Order":1
    },
    {
        "Type":"forward",
        "TargetGroupArn":"`target-group-arn`",
        "Order":2
    }
]'
```

For more information, see [Listener rules for your Application Load Balancer](listener-rules.md "listener-rules.md").
