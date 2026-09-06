

# IAM Roles Anywhere and interface VPC endpoints (AWS PrivateLink)
<a name="vpc-interface-endpoints"></a>

You can establish a private connection between your VPC and AWS Identity and Access Management Roles Anywhere by creating an *interface VPC endpoint*. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink), a technology that enables you to privately access IAM Roles Anywhere APIs without an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. Instances in your VPC don't need public IP addresses to communicate with IAM Roles Anywhere APIs. Traffic between your VPC and IAM Roles Anywhere does not leave the Amazon network. 

Each interface endpoint is represented by one or more [Elastic Network Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in your subnets. 

For more information, see [Interface VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *Amazon VPC User Guide*. 

## Considerations for IAM Roles Anywhere VPC endpoints
<a name="vpc-endpoint-considerations"></a>

Before you set up an interface VPC endpoint for IAM Roles Anywhere, ensure that you review [Interface endpoint properties and limitations](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#vpce-interface-limitations) in the *Amazon VPC User Guide*. 

IAM Roles Anywhere supports making calls to all of its API actions from your VPC. 

VPC endpoint policies are supported for all IAM Roles Anywhere API methods, including `CreateSession`. Full access to IAM Roles Anywhere is allowed through the endpoint by default. For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) in the *Amazon VPC User Guide*.

## Creating an interface VPC endpoint for IAM Roles Anywhere
<a name="vpc-endpoint-create"></a>

You can create a VPC endpoint for the IAM Roles Anywhere service using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *Amazon VPC User Guide*.

Create a VPC endpoint for IAM Roles Anywhere using the following service name: 
+ com.amazonaws.{{region}}.rolesanywhere 

If you enable private DNS for the endpoint, you can make API requests to IAM Roles Anywhere using its default DNS name for the Region, for example, `rolesanywhere.us-east-1.amazonaws.com`. 

For more information, see [Accessing a service through an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#access-service-though-endpoint) in the *Amazon VPC User Guide*.

## Creating a VPC endpoint policy for IAM Roles Anywhere
<a name="vpc-endpoint-policy"></a>

You can attach an endpoint policy to your VPC endpoint that controls access to IAM Roles Anywhere. The policy specifies the following information:
+ The principal that can perform actions.
+ The actions that can be performed.
+ The resources on which actions can be performed.

For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *Amazon VPC User Guide*. 

**Example: VPC endpoint policy for IAM Roles Anywhere actions**  
The following is an example of an endpoint policy for IAM Roles Anywhere. When attached to an endpoint, this policy grants access to the listed IAM Roles Anywhere actions for all principals on all resources.

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":[
            "rolesanywhere:CreateTrustAnchor",
            "rolesanywhere:CreateProfile",
            "rolesanywhere:UpdateProfile"
         ],
         "Resource":"*"
      }
   ]
}
```

### VPC endpoint policy for CreateSession
<a name="vpc-endpoint-policy-createsession"></a>

When creating a VPC endpoint policy for the `CreateSession` action, you must specify `*` as the principal, as the policy is evaluated before the certificate-based authentication is complete. As a result, consider specifying trust anchor ARNs in the `Resource` element. Additionally, condition keys are available, extracted from the X.509 certificate. These keys follow the same format as the principal tags referenced in [The IAM Roles Anywhere trust model](trust-model.md), but using `rolesanywhere:` as a prefix instead of `aws:PrincipalTag/`.

Trust anchor resources use the following ARN format:

```
arn:aws:rolesanywhere:{{region}}:{{account-id}}:trust-anchor/{{trust-anchor-id}}
```

You can use wildcards to allow access to multiple trust anchors, or specify individual trust anchor ARNs for more restrictive access control.

**VPC endpoint policy for CreateSession with a specific trust anchor**  
The following is an example of an endpoint policy for `CreateSession` that restricts access to a specific trust anchor. When attached to an endpoint, this policy grants access to the `CreateSession` action only for the specified trust anchor.

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":"rolesanywhere:CreateSession",
         "Resource":"arn:aws:rolesanywhere:us-west-2:111122223333:trust-anchor/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"
      }
   ]
}
```

This policy allows `CreateSession` operations only for the specified trust anchor. Replace the example ARN with your actual trust anchor ARN. This configuration provides the most restrictive access control, limiting session creation to a specific trust anchor.

**VPC endpoint policy for CreateSession with wildcard trust anchors**  
The following is an example of an endpoint policy for `CreateSession` that allows access to all trust anchors in a specific region and account. When attached to an endpoint, this policy grants access to the `CreateSession` action for any trust anchor in the specified region and account.

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":"rolesanywhere:CreateSession",
         "Resource":"arn:aws:rolesanywhere:us-west-2:111122223333:trust-anchor/*"
      }
   ]
}
```

This policy allows `CreateSession` operations for all trust anchors in the specified region and account. This is useful when you want to control access at the VPC level without restricting specific trust anchors. Replace the region and account ID with your values.

**VPC endpoint policy for CreateSession with certificate attribute conditions**  
The following is an example of an endpoint policy for `CreateSession` that uses condition keys based on X.509 certificate attributes. When attached to an endpoint, this policy grants access to the `CreateSession` action only when the authenticating certificate's Common Name matches the specified value.

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":"rolesanywhere:CreateSession",
         "Resource":"arn:aws:rolesanywhere:us-west-2:111122223333:trust-anchor/*",
         "Condition":{
            "StringEquals":{
               "rolesanywhere:x509Subject/CN":"Bob"
            }
         }
      }
   ]
}
```

This policy allows `CreateSession` operations for all trust anchors but only when the X.509 certificate's Common Name (CN) matches `Bob`. IAM Roles Anywhere extracts attributes from the authenticating certificate and makes them available as condition keys. You can use these keys in condition statements to further restrict access based on certificate properties. Replace `Bob` with your required CN value.

Other X.509 certificate attributes are also available as condition keys, including:
+ `rolesanywhere:x509Subject/CN` - Subject Common Name
+ `rolesanywhere:x509Subject/O` - Subject Organization
+ `rolesanywhere:x509Issuer/CN` - Issuer Common Name

You can use any X.509 subject or issuer attribute as a condition key to create fine-grained access control policies based on certificate properties.

**VPC endpoint policy combining CreateSession and management operations**  
Because the Principal required for `CreateSession` is `*`, consider adding two separate statements to the policy. The following is an example of an endpoint policy that combines multiple statements to control different types of access. This policy allows any principal to call `CreateSession` with trust anchor conditions, while restricting management operations to a specific IAM principal.

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":"rolesanywhere:CreateSession",
         "Resource":"arn:aws:rolesanywhere:us-west-2:111122223333:trust-anchor/*",
         "Condition":{
            "StringEquals":{
               "rolesanywhere:x509Subject/OU":"Development"
            }
         }
      },
      {
         "Principal":{
            "AWS":"arn:aws:iam::111122223333:role/RolesAnywhereAdmin"
         },
         "Effect":"Allow",
         "Action":[
            "rolesanywhere:CreateTrustAnchor",
            "rolesanywhere:UpdateTrustAnchor",
            "rolesanywhere:CreateProfile",
            "rolesanywhere:UpdateProfile"
         ],
         "Resource":"*"
      }
   ]
}
```

This policy demonstrates a common pattern for separating session creation from administrative operations. The first statement allows any workload with a certificate from `ExampleCorp` to create sessions through the VPC endpoint, while the second statement restricts trust anchor and profile management to a specific IAM role. This approach provides broad access for authentication while maintaining tight control over configuration changes. Replace the organization name, region, account ID, and IAM role ARN with your values.