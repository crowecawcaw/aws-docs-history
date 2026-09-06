

# How Elastic Load Balancing works with IAM
<a name="security_iam_service-with-iam"></a>

Before you use IAM to manage access to Elastic Load Balancing, learn what IAM features are available to use with Elastic Load Balancing.


**IAM features you can use with Elastic Load Balancing**  

| IAM feature | Elastic Load Balancing support | 
| --- | --- | 
| [Identity-based policies](#security_iam_service-with-iam-id-based-policies) |  Yes | 
| [Resource-based policies](#security_iam_service-with-iam-resource-based-policies) |  No  | 
| [Policy actions](#security_iam_service-with-iam-id-based-policies-actions) |  Yes | 
| [Policy resources](#security_iam_service-with-iam-id-based-policies-resources) |  Yes | 
| [Policy condition keys (service-specific)](#security_iam_service-with-iam-id-based-policies-conditionkeys) |  Yes | 
| [ACLs](#security_iam_service-with-iam-acls) |  No  | 
| [ABAC (tags in policies)](#security_iam_service-with-iam-tags) |  Yes | 
| [Temporary credentials](#security_iam_service-with-iam-roles-tempcreds) |  Yes | 
| [Principal permissions](#security_iam_service-with-iam-principal-permissions) |  Yes | 
| [Service roles](#security_iam_service-with-iam-roles-service) |  No  | 
| [Service-linked roles](#security_iam_service-with-iam-roles-service-linked) |  Yes | 

## Identity-based policies for Elastic Load Balancing
<a name="security_iam_service-with-iam-id-based-policies"></a>

**Supports identity-based policies:** Yes

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. To learn about all of the elements that you can use in a JSON policy, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

## Resource-based policies within Elastic Load Balancing
<a name="security_iam_service-with-iam-resource-based-policies"></a>

**Supports resource-based policies:** No 

Resource-based policies are JSON policy documents that you attach to a resource. Examples of resource-based policies are IAM *role trust policies* and Amazon S3 *bucket policies*. In services that support resource-based policies, service administrators can use them to control access to a specific resource. For the resource where the policy is attached, the policy defines what actions a specified principal can perform on that resource and under what conditions. You must [specify a principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html) in a resource-based policy. Principals can include accounts, users, roles, federated users, or AWS services.

To enable cross-account access, you can specify an entire account or IAM entities in another account as the principal in a resource-based policy. For more information, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the *IAM User Guide*.

## Policy actions for Elastic Load Balancing
<a name="security_iam_service-with-iam-id-based-policies-actions"></a>

**Supports policy actions:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

To see a list of Elastic Load Balancing actions, see [Actions defined by Elastic Load Balancing V2](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselasticloadbalancingv2.html#awselasticloadbalancingv2-actions-as-permissions) and [Actions defined by Elastic Load Balancing V1](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselasticloadbalancing.html#awselasticloadbalancing-actions-as-permissions) in the *Service Authorization Reference*.

Policy actions in Elastic Load Balancing use the following prefix before the action:

```
elasticloadbalancing
```

To specify multiple actions in a single statement, separate them with commas.

```
"Action": [
    "elasticloadbalancing:{{action1}}",
    "elasticloadbalancing:{{action2}}"
]
```

You can specify multiple actions using wildcards (\*). For example, to specify all actions that begin with the word `Describe`, include the following action:

```
"Action": "elasticloadbalancing:Describe*"
```

For the complete list of the API actions for Elastic Load Balancing, see the following documentation:
+ Application Load Balancers, Network Load Balancers, and Gateway Load Balancers — [API Reference version 2015-12-01](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/)
+ Classic Load Balancers — [API Reference version 2012-06-01](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/)

## Policy resources for Elastic Load Balancing
<a name="security_iam_service-with-iam-id-based-policies-resources"></a>

**Supports policy resources:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

Some Elastic Load Balancing API actions support multiple resources. To specify multiple resources in a single statement, separate the ARNs with commas.

```
"Resource": [
    "{{resource1}}",
    "{{resource2}}"
]
```

To see a list of Elastic Load Balancing resource types and their ARNs, see [Resources defined by Elastic Load Balancing V2](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselasticloadbalancingv2.html#awselasticloadbalancingv2-resources-for-iam-policies) and [Resources defined by Elastic Load Balancing V1](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselasticloadbalancing.html#awselasticloadbalancing-resources-for-iam-policies) in the *Service Authorization Reference*. To learn with which actions you can specify the ARN of each resource, see [Actions defined by Elastic Load Balancing V2](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselasticloadbalancingv2.html#awselasticloadbalancingv2-actions-as-permissions) and [Actions defined by Elastic Load Balancing V1](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselasticloadbalancing.html#awselasticloadbalancing-actions-as-permissions).

## Policy condition keys for Elastic Load Balancing
<a name="security_iam_service-with-iam-id-based-policies-conditionkeys"></a>

**Supports service-specific policy condition keys:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

To see a list of Elastic Load Balancing condition keys, see [Condition keys for Elastic Load Balancing V2](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselasticloadbalancingv2.html#awselasticloadbalancingv2-policy-keys) and [Condition keys for Elastic Load Balancing V1](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselasticloadbalancing.html#awselasticloadbalancing-policy-keys) in the *Service Authorization Reference*. To learn with which actions and resources you can use a condition key, see [Actions defined by Elastic Load Balancing V2](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselasticloadbalancingv2.html#awselasticloadbalancingv2-actions-as-permissions) and [Actions defined by Elastic Load Balancing V1](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselasticloadbalancing.html#awselasticloadbalancing-actions-as-permissions).

**Topics**
+ [elasticloadbalancing:ListenerProtocol](#listenerprotocol-condition)
+ [elasticloadbalancing:SecurityPolicy](#securitypolicy-condition)
+ [elasticloadbalancing:Scheme](#scheme-condition)
+ [elasticloadbalancing:SecurityGroup](#securitygroup-condition)
+ [elasticloadbalancing:Subnet](#subnet-condition)
+ [elasticloadbalancing:ResourceTag](#resourcetag-condition)

### elasticloadbalancing:ListenerProtocol condition key
<a name="listenerprotocol-condition"></a>

The `elasticloadbalancing:ListenerProtocol` condition key can be used for conditions that define the types of listeners that can be created and used. The policy is available for Application Load Balancers, Network Load Balancers, and Classic Load Balancers. The following actions support this condition key:

**API version 2015-12-01**
+ `CreateListener`
+ `ModifyListener`

**API version 2012-06-01**
+ `CreateLoadBalancer`
+ `CreateLoadBalancerListeners`

The following example policy requires users to select the HTTPS protocol for the listeners for their Application Load Balancers and the TLS protocol for the listeners for their Network Load Balancers.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": {
        "Effect": "Allow",
        "Action": [
            "elasticloadbalancing:CreateListener",
            "elasticloadbalancing:ModifyListener"
        ],
        "Resource": "*",
        "Condition": {
            "ForAnyValue:StringEquals": {
                "elasticloadbalancing:ListenerProtocol": [
                    "HTTPS",
                    "TLS"
                ]
            }
        }
    }
}
```

------

With a Classic Load Balancer, you can specify multiple listeners in a single call. Therefore, your policy must use a [multi-value context key](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition_examples-multi-valued-context-keys.html), as shown in the following example.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "elasticloadbalancing:CreateLoadBalancer",
                "elasticloadbalancing:CreateLoadBalancerListeners"
            ],
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "elasticloadbalancing:ListenerProtocol": [
                        "TCP",
                        "HTTP",
                        "HTTPS"
                    ]
                }
            }
        }
    ]
}
```

------

### elasticloadbalancing:SecurityPolicy condition key
<a name="securitypolicy-condition"></a>

The `elasticloadbalancing:SecurityPolicy` condition key can be used for conditions that define and enforce specific security policies on the load balancers. The policy is available for Application Load Balancers, Network Load Balancers and Classic Load Balancers. The following actions support this condition key:

**API version 2015-12-01**
+ `CreateListener`
+ `ModifyListener`

**API version 2012-06-01**
+ `CreateLoadBalancerPolicy`
+ `SetLoadBalancerPoliciesOfListener`

The following example policy requires users to select one of the specified security policies for their Application Load Balancers and Network Load Balancers.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": {
        "Effect": "Allow",
        "Action": [
            "elasticloadbalancing:CreateListener",
            "elasticloadbalancing:ModifyListener"
        ],
        "Resource": "*",
        "Condition": {
            "ForAnyValue:StringEquals": {
                "elasticloadbalancing:SecurityPolicy": [
                    "ELBSecurityPolicy-TLS13-1-2-2021-06",
                    "ELBSecurityPolicy-TLS13-1-2-Res-2021-06",
                    "ELBSEcurityPolicy-TLS13-1-1-2021-06"
                ]
            }
        }
    }
}
```

------

### elasticloadbalancing:Scheme condition key
<a name="scheme-condition"></a>

The `elasticloadbalancing:Scheme` condition key can be used for conditions that define which scheme can be selected during load balancer creation. The policy is available for Application Load Balancers, Network Load Balancers, and Classic Load Balancers. The following actions support this condition key:

**API version 2015-12-01**
+ `CreateLoadBalancer`

**API version 2012-06-01**
+ `CreateLoadBalancer`

The following example policy requires users to select the specified scheme for their load balancers.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": {
        "Effect": "Allow",
        "Action": "elasticloadbalancing:CreateLoadBalancer",
        "Resource": "*",
        "Condition": {
            "StringEquals": {
                "elasticloadbalancing:Scheme": "internal"
            }
        }
    }
}
```

------

### `elasticloadbalancing:SecurityGroup` condition key
<a name="securitygroup-condition"></a>

**Important**  
Elastic Load Balancing accepts all capitalizations of security group IDs. However, make sure to use the appropriate case insensitive condition operators, for example `StringEqualsIgnoreCase`.

The `elasticloadbalancing:SecurityGroup` condition key can be used for conditions that define which security groups can be applied to the load balancers. The policy is available for Application Load Balancers, Network Load Balancers and Classic Load Balancers. The following actions support this condition key:

**API version 2015-12-01**
+ `CreateLoadBalancer`
+ `SetSecurityGroups`

**API version 2012-06-01**
+ `CreateLoadBalancer`
+ `ApplySecurityGroupsToLoadBalancer`

The following example policy requires users to select one of the specified security groups for their load balancers.

```
    "Version": "2012-10-17",		 	 	 
    "Statement": {
        "Effect": "Allow",
        "Action": [
            "elasticloadbalancing:CreateLoadBalancer",
            "elasticloadbalancing:SetSecurityGroup"
        ],
        "Resource": "*",
        "Condition": {
            "ForAnyValue:StringEqualsIgnoreCase":{ 
                "elasticloadbalancing:SecurityGroup": [
                    "sg-51530134",
                    "sg-51530144",
                    "sg-51530139"
                ]
            },
        }
    }
}
```

### elasticloadbalancing:Subnet condition key
<a name="subnet-condition"></a>

**Important**  
Elastic Load Balancing accepts all capitalizations of subnet IDs. However, make sure to use the appropriate case insensitive condition operators, for example `StringEqualsIgnoreCase`.

The `elasticloadbalancing:Subnet` condition key can be used for conditions that define which subnets can be created and attached to load balancers. The policy is available for Application Load Balancers, Network Load Balancers, Gateway Load Balancers and Classic Load Balancers. The following actions support this condition key:

**API version 2015-12-01**
+ `CreateLoadBalancer`
+ `SetSubnets`

**API version 2012-06-01**
+ `CreateLoadBalancer`
+ `AttachLoadBalancerToSubnets`

The following example policy requires users to select one of the specified subnets for their load balancers.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": {
        "Effect": "Allow",
        "Action": [
            "elasticloadbalancing:CreateLoadBalancer",
            "elasticloadbalancing:SetSubnets"
        ],
        "Resource": "*",
        "Condition": {
            "ForAnyValue:StringEqualsIgnoreCase": {
                "elasticloadbalancing:Subnet": [
                    "subnet-01234567890abcdef",
                    "subnet-01234567890abcdeg "
                ]
            }
        }
    }
}
```

------

### elasticloadbalancing:ResourceTag condition key
<a name="resourcetag-condition"></a>

The `elasticloadbalancing:ResourceTag`/{{key}} condition key is specific to Elastic Load Balancing. All mutating actions support this condition key.

## ACLs in Elastic Load Balancing
<a name="security_iam_service-with-iam-acls"></a>

**Supports ACLs:** No 

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are similar to resource-based policies, although they do not use the JSON policy document format.

## ABAC with Elastic Load Balancing
<a name="security_iam_service-with-iam-tags"></a>

**Supports ABAC (tags in policies):** Yes

Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `aws:ResourceTag/{{key-name}}`, `aws:RequestTag/{{key-name}}`, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*. To view a tutorial with steps for setting up ABAC, see [Use attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) in the *IAM User Guide*.

## Using temporary credentials with Elastic Load Balancing
<a name="security_iam_service-with-iam-roles-tempcreds"></a>

**Supports temporary credentials:** Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you dynamically generate temporary credentials instead of using long-term access keys. For more information, see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) and [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

## Cross-service principal permissions for Elastic Load Balancing
<a name="security_iam_service-with-iam-principal-permissions"></a>

**Supports forward access sessions (FAS):** Yes

 Forward access sessions (FAS) use the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services. For policy details when making FAS requests, see [Forward access sessions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_forward_access_sessions.html). 

## Service roles for Elastic Load Balancing
<a name="security_iam_service-with-iam-roles-service"></a>

**Supports service roles:** No 

 A service role is an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that a service assumes to perform actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For more information, see [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*. 

## Service-linked roles for Elastic Load Balancing
<a name="security_iam_service-with-iam-roles-service-linked"></a>

**Supports service-linked roles:** Yes

 A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf. Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view, but not edit the permissions for service-linked roles. 

For details about creating or managing Elastic Load Balancing service-linked roles, see [Elastic Load Balancing service-linked role](elb-service-linked-roles.md).