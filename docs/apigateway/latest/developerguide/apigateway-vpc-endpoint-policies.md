

# Use VPC endpoint policies for private APIs in API Gateway
<a name="apigateway-vpc-endpoint-policies"></a>

To improve the security of your private API, you can create a VPC endpoint policy. A VPC endpoint policy is an IAM resource policy that you attach to a VPC endpoint. For more information, see [Controlling Access to Services with VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html).

You might want to create a VPC endpoint policy to do the following tasks.
+ Allow only certain organizations or resources to access your VPC endpoint and invoke your API.
+ Use a single policy and avoid session-based or role-based policies to control traffic to your API.
+ Tighten the security perimeter of your application while migrating from on premises to AWS.

## VPC endpoint policy considerations
<a name="apigateway-vpc-endpoint-policies-considerations"></a>

The following are considerations for your VPC endpoint policy:
+ The identity of the invoker is evaluated based on the `Authorization` header value. The VPC endpoint policy is evaluated first, and then API Gateway evaluates the request, based on the type of authorization configured on the method request. The following table shows how the VPC endpoint policy is evaluated based on the content of the `Authorization` header value.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-vpc-endpoint-policies.html)
+ If your access control depends on using a bearer token, such as a Lambda or Amazon Cognito authorizer, you can control your security perimeter by using [properties of the resource](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resource-properties).
+  If your authorization controls use IAM authorization, you can control your security perimeter by using [properties of the resource](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resource-properties) and [ properties of the principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resource-principal).
+ VPC endpoint policies can be used together with API Gateway resource policies. The API Gateway resource policy specifies which principals can access the API. The endpoint policy specifies who can access the VPC and which APIs can be called from the VPC endpoint. Your private API needs a resource policy but you don't need to create a custom VPC endpoint policy.

## VPC endpoint policy examples
<a name="apigateway-vpc-endpoint-policies-examples"></a>

You can create policies for Amazon Virtual Private Cloud endpoints for Amazon API Gateway in which you can specify the following.
+ The principal that can perform actions.
+ The actions that can be performed.
+ The resources that can have actions performed on them.

This might depend on the contents of your authorization header. For more information, see [VPC endpoint policy considerations](#apigateway-vpc-endpoint-policies-considerations). For additional example policies, see [Data perimeter policy examples](https://github.com/aws-samples/data-perimeter-policy-examples) on the GitHub website.

To attach the policy to the VPC endpoint, you'll need to use the VPC console. For more information, see [Controlling Access to Services with VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html). 

## Example 1: VPC endpoint policy granting access to two APIs
<a name="apigateway-vpc-endpoint-policies-example-1"></a>

The following example policy grants access to only two specific APIs via the VPC endpoint that the policy is attached to.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Principal": "*",
            "Action": [
                "execute-api:Invoke"
            ],
            "Effect": "Allow",
            "Resource": [
                "arn:aws:execute-api:us-east-1:123412341234:a1b2c3d4e5/*",
                "arn:aws:execute-api:us-east-1:123412341234:aaaaa11111/*"
            ]
        }
    ]
}
```

------

## Example 2: VPC endpoint policy granting access to GET methods
<a name="apigateway-vpc-endpoint-policies-example-2"></a>

The following example policy grants users access to `GET` methods for a specific API via the VPC endpoint that the policy is attached to.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Principal": "*",
            "Action": [
                "execute-api:Invoke"
            ],
            "Effect": "Allow",
            "Resource": [
                "arn:aws:execute-api:us-east-1:123412341234:a1b2c3d4e5/stageName/GET/*"
            ]
        }
    ]
}
```

------

## Example 3: VPC endpoint policy granting a specific user access to a specific API
<a name="apigateway-vpc-endpoint-policies-example-3"></a>

The following example policy grants a specific user access to a specific API via the VPC endpoint that the policy is attached to.

In this case, because the policy restricts access to specific IAM principals, you must set the `authorizationType` of the method to `AWS_IAM` or `NONE`.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Principal": {
                "AWS": [
                    "arn:aws:iam::123412341234:user/MyUser"
                ]
            },
            "Action": [
                "execute-api:Invoke"
            ],
            "Effect": "Allow",
            "Resource": [
                "arn:aws:execute-api:us-east-1:123412341234:a1b2c3d4e5/*"
            ]
        }
    ]
}
```

------

## Example 4: VPC endpoint policy granting users access to a specific custom domain name and every API mapped to the domain
<a name="apigateway-vpc-endpoint-policies-example-4"></a>

The following example policy grants users access to a specific custom domain name for private APIs via the VPC endpoint that the policy is attached to. With this policy, as long as a user has created a domain name access association between the VPC endpoint and the custom domain name and is granted access to invoke the custom domain name and any private API's mapped to the custom domain name, the user can invoke any APIs mapped to this custom domain name. For more information, see [Custom domain names for private APIs in API Gateway](apigateway-private-custom-domains.md).

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "*"
      },
      "Action": "execute-api:Invoke",
      "Resource": [
        "*"
      ],
       "Condition": {
        "ArnEquals": {
          "execute-api:viaDomainArn": "arn:aws:execute-api:us-west-2:111122223333:/domainnames/private.test.com+f4g5h6"
        }
      }
    }
  ]
}
```

------

## Example 5: VPC endpoint policy granting or denying access to specific APIs and domain resources
<a name="apigateway-vpc-endpoint-policies-example-5"></a>

The following example policy grants users access to specific APIs and domain resources. With this policy, as long as a user has created a domain name access association between the VPC endpoint and the custom domain name and is granted access to invoke the custom domain name and any private API's mapped to the custom domain name, the user can invoke allowed private APIs and domain resources. For more information, see [Custom domain names for private APIs in API Gateway](apigateway-private-custom-domains.md).

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "*"
      },
      "Action": "execute-api:Invoke",
      "Resource": [
        "arn:aws:execute-api:us-west-2:111122223333:/domainnames/private.test.com+f4g5h6",
        "arn:aws:execute-api:us-west-2:111122223333:a1b2c3d4e5/*"
      ]
    },
    {
      "Effect": "Deny",
      "Principal": {
        "AWS": "*"
      },
      "Action": "execute-api:Invoke",
      "Resource": [
        "arn:aws:execute-api:us-west-2:111122223333:a1b2c3d4e5/admin/*",
        "arn:aws:execute-api:us-west-2:111122223333:bcd123455/*"
      ]
    }
  ]
}
```

------

## Example 6: VPC endpoint policy granting or denying access by principals and resources belonging to an organization
<a name="apigateway-vpc-endpoint-policies-example-6"></a>

The following example policy grants access to principals and resources that belong to an organization.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Condition": {
                "StringEquals": {
                    "aws:ResourceOrgID": "o-abcd1234",
                    "aws:PrincipalOrgID": "o-abcd1234"
                }
            },
            "Action": "*",
            "Resource": "*",
            "Effect": "Allow",
            "Principal": {
                "AWS": "*"
            },
            "Sid": "AllowRequestsByOrgsIdentitiesToOrgsResources"
        }
    ]
}
```

------