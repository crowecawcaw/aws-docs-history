

# Using IAM policy conditions for fine-grained access control
<a name="specifying-conditions-route53"></a>

In Route 53, you can specify conditions when granting permissions using an IAM policy (see [Access control](security-iam.md#access-control)). For example, you can:
+ Grant permissions to allow access to a single resource record set.
+ Grant permissions to allow users access to all resource record sets of a specific DNS record type in a hosted zone, for example A and AAAA records.
+ Grant permissions to allow users access to a resource record set where its name contains a specific string.
+ Grant permissions to allow users to perform only a subset of the `CREATE | UPSERT | DELETE` actions on the Route 53 console, or when using the [ChangeResourceRecordSets](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeResourceRecordSets.html) API.
+ Grant permissions to allow users to associate or dissociate private hosted zones from a particular VPC.
+ Grant permissions to allow users to list hosted zones associated to a particular VPC.
+ Grant permissions to allow users access to create a new private hosted zone and associate it to a particular VPC.
+ Grant permissions to allow users to create or delete a VPC association authorization.
+ Grant permissions to allow users to manage (associate/disassociate/update) only specific resource types with a Route 53 Profile.
+ Grant permissions to allow users to manage (associate/disassociate/update) only specific resource ARNs with a Route 53 Profile.
+ Grant permissions to allow users to manage (associate/disassociate/update) only specific hosted zone domains with a Route 53 Profile.
+ Grant permissions to allow users to manage (associate/disassociate/update) only specific Resolver Rule domains with a Route 53 Profile.
+ Grant permissions to allow users to manage (associate/disassociate/update) Firewall Rule Groups with a specific priority range in a Route 53 Profile.
+ Grant permissions to allow users to manage (associate/disassociate) a Route 53 Profile with specific VPCs.

You can also create permissions that combine any of the granular permissions.

## Normalizing the Route 53 condition key values
<a name="route53_rrset_conditionkeys_normalization"></a>

The values you enter for the policy conditions must be formatted, or normalized, as follows:

**For `route53:ChangeResourceRecordSetsNormalizedRecordNames`:**
+ All letters must be lowercase.
+ The DNS name must be without the trailing dot.
+ Characters other than a–z, 0–9, - (hyphen), \_ (underscore), and . (period, as a delimiter between labels) must use escape codes in the format \\three-digit octal code. For example, `\052 `is the octal code for character \*.

**For `route53:ChangeResourceRecordSetsActions`, the value can be any of the following and must be uppercase:**
+ CREATE
+ UPSERT
+ DELETE

**For `route53:ChangeResourceRecordSetsRecordTypes`**:
+ The value must be in uppercase, and can be any of the Route 53 supported DNS record types. For more information, see [Supported DNS record types](ResourceRecordTypes.md).

**For `route53:VPCs`:**
+ The value must be in the format of `VPCId=<vpc-id>,VPCRegion=<region>`.
+ The value of `<vpc-id>` and `<region>`must be in lowercase, such as `VPCId=vpc-123abc` and `VPCRegion=us-east-1`.
+ The context keys and values are case sensitive.

**Important**  
For your permissions to allow or restrict actions as you intend, you must follow these conventions. Only `VPCId` and `VPCRegion` elements are accepted by this condition key, any other AWS resources, such as AWS account, are not supported.

**For `route53profiles:ResourceTypes`, the value can be any of the following and is case sensitive:**
+ HostedZone
+ FirewallRuleGroup
+ ResolverQueryLoggingConfig
+ ResolverRule
+ VPCEndpoint

**For `route53profiles:ResourceArns`:**
+ The value must be a valid AWS resource ARN, such as `arn:aws:route53:::hostedzone/Z12345`.
+ Use the `ArnEquals` or `ArnLike` condition operator when comparing ARN values.

**For `route53profiles:HostedZoneDomains`:**
+ The value must be a valid domain name, such as `example.com`.
+ The domain name must be without the trailing dot.
+ The values are case sensitive.

**For `route53profiles:ResolverRuleDomains`:**
+ The value must be a valid domain name, such as `example.com`.
+ The domain name must be without the trailing dot.
+ The values are case sensitive.

**For `route53profiles:FirewallRuleGroupPriority`:**
+ The value must be a numeric value representing the priority of the Firewall Rule Group.
+ Use numeric condition operators such as `NumericEquals`, `NumericGreaterThanEquals`, or `NumericLessThanEquals` to compare priority values or define a priority range.

**For `route53profiles:ResourceIds`:**
+ The value must be a valid VPC ID, such as `vpc-1a2b3c4d5e6f`.
+ The values are case sensitive.

You can use the [Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) or [Policy Simulator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-reference-policy-checks.html) in the *IAM User Guide* to validate that your policy grants or restricts the permissions as expected. You can also validate the permissions by applying an IAM policy to a test user or role to carry out Route 53 operations. 

## Specifying conditions: using condition keys
<a name="route53_rrsetConditionKeys"></a>

AWS provides a set of predefined condition keys (AWS-wide condition keys) for all AWS services that support IAM for access control. For example, you can use the `aws:SourceIp` condition key to check the requester's IP address before allowing an action to be performed. For more information and a list of the AWS-wide keys, see [Available Keys for Conditions](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#AvailableKeys) in the *IAM User Guide*.

**Note**  
Route 53 doesn't support tag-based condition keys.

The following table shows the Route 53 service-specific condition keys that apply to Route 53.



| Route 53 Condition Key | API operations | Value type | Description | 
| --- | --- | --- | --- | 
| route53:ChangeResourceRecordSetsNormalizedRecordNames | [ChangeResourceRecordSets](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeResourceRecordSets.html) | Multi-valued | Represents a list of DNS record names in the request of ChangeResourceRecordSets. To get the expected behavior, DNS names in the IAM policy must be normalized as follows: +  All letters must be lowercase. <br />+  The DNS name must be without the trailing dot. <br />+  Characters other than a to z, 0 to 9, - (hyphen), \_ (underscore), and . (period, as a delimiter between labels) must use escape codes in the format \\three-digit octal code.  | 
| route53:ChangeResourceRecordSetsRecordTypes | [ChangeResourceRecordSets](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeResourceRecordSets.html) | Multi-valued | Represents a list of DNS record types in the request of `ChangeResourceRecordSets`.<br />`ChangeResourceRecordSetsRecordTypes` can be any of the Route 53 supported DNS record types. For more information, see [Supported DNS record types](ResourceRecordTypes.md). All must be entered in uppercase in the policy. | 
| route53:ChangeResourceRecordSetsActions | [ChangeResourceRecordSets](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeResourceRecordSets.html) | Multi-valued | Represents a list of actions in the request of `ChangeResourceRecordSets`. <br />`ChangeResourceRecordSetsActions` can be any of the following values (must be uppercase):+  CREATE <br />+  UPSERT <br />+  DELETE  | 
| route53:VPCs | [AssociateVPCWithHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_AssociateVPCWithHostedZone.html)<br />[DisassociateVPCFromHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DisassociateVPCFromHostedZone.html)<br />[ListHostedZonesByVPC](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListHostedZonesByVPC.html)<br />[CreateHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateHostedZone.html)<br />[CreateVPCAssociationAuthorization](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateVPCAssociationAuthorization.html)<br />[DeleteVPCAssociationAuthorization](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteVPCAssociationAuthorization.html) | Multi-valued | Represents a list of VPCs in the request of AssociateVPCWithHostedZone, DisassociateVPCFromHostedZone, ListHostedZonesByVPC, CreateHostedZone, CreateVPCAssociationAuthorization, and DeleteVPCAssociationAuthorization, in the format of "VPCId=<vpc-id>,VPCRegion=<region> | 
| route53profiles:ResourceTypes | [AssociateResourceToProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_AssociateResourceToProfile.html)<br />[DisassociateResourceFromProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_DisassociateResourceFromProfile.html)<br />[UpdateProfileResourceAssociation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_UpdateProfileResourceAssociation.html) | String | Filters access by specific resource type.<br />`route53profiles:ResourceTypes` can be any of the following values (case sensitive):+  HostedZone <br />+  FirewallRuleGroup <br />+  ResolverQueryLoggingConfig <br />+  ResolverRule <br />+  VPCEndpoint  | 
| route53profiles:ResourceArns | [AssociateResourceToProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_AssociateResourceToProfile.html)<br />[DisassociateResourceFromProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_DisassociateResourceFromProfile.html) | ARN | Filters access by specific resource ARNs. | 
| route53profiles:HostedZoneDomains | [AssociateResourceToProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_AssociateResourceToProfile.html)<br />[DisassociateResourceFromProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_DisassociateResourceFromProfile.html)<br />[UpdateProfileResourceAssociation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_UpdateProfileResourceAssociation.html) | String | Filters access by Hosted Zone domains. To get the expected behavior, domain names in the IAM policy must be normalized as follows:+  The domain name must be without the trailing dot. <br />+  The values are case sensitive.  | 
| route53profiles:ResolverRuleDomains | [AssociateResourceToProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_AssociateResourceToProfile.html)<br />[DisassociateResourceFromProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_DisassociateResourceFromProfile.html)<br />[UpdateProfileResourceAssociation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_UpdateProfileResourceAssociation.html) | String | Filters access by Resolver Rule domains. To get the expected behavior, domain names in the IAM policy must be normalized as follows:+  The domain name must be without the trailing dot. <br />+  The values are case sensitive.  | 
| route53profiles:FirewallRuleGroupPriority | [AssociateResourceToProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_AssociateResourceToProfile.html)<br />[DisassociateResourceFromProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_DisassociateResourceFromProfile.html)<br />[UpdateProfileResourceAssociation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_UpdateProfileResourceAssociation.html) | Numeric | Filters access by priority range of a Firewall Rule Group. | 
| route53profiles:ResourceIds | [AssociateProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_AssociateProfile.html)<br />[DisassociateProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_DisassociateProfile.html) | String | Filters access by given VPCs. | 

## Example policies: Using conditions for fine-grained access
<a name="route53_rrset_conditionkeys-examples"></a>

Each of the examples in this section sets the Effect clause to Allow and specifies only the actions, resources, and parameters that are allowed. Access is permitted only to what is explicitly listed in the IAM policy.

In some cases, it is possible to rewrite these policies so that they are deny-based (that is, setting the Effect clause to Deny and inverting all of the logic in the policy). However, we recommend that you avoid using deny-based policies because they are difficult to write correctly, compared to allow-based policies. This is especially true for Route 53 due to text normalization that is required. 

**Grant permissions that limit access to DNS records with specific names**  
The following permissions policy grants permissions that allow `ChangeResourceRecordSets` actions on the Hosted Zone Z12345 for example.com and marketing.example.com. It uses the `route53:ChangeResourceRecordSetsNormalizedRecordNames` condition key to limit user actions only on the records that match the specified names. 

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "route53:ChangeResourceRecordSets",
            "Resource": "arn:aws:route53:::hostedzone/Z11111112222222333333",
            "Condition": {
                "ForAllValues:StringEquals":{
                    "route53:ChangeResourceRecordSetsNormalizedRecordNames": ["example.com", "marketing.example.com"]
                }
            }
          }
        ]
}
```

------

`ForAllValues:StringEquals` is an IAM condition operator that applies to multi-valued keys. The condition in the policy above will allow the operation only when all changes in `ChangeResourceRecordSets` have the DNS name of example.com. For more information, see [IAM condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html) and [IAM condition with multiple keys or values](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_multi-value-conditions.html) in the IAM User Guide.

To implement the permission that matches names with certain suffixes, you can use the IAM wildcard (\*) in the policy with condition operator `StringLike` or `StringNotLike`. The following policy will allow the operation when all changes in the `ChangeResourceRecordSets` operation have DNS names that end with “-beta.example.com”.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "route53:ChangeResourceRecordSets",
            "Resource": "arn:aws:route53:::hostedzone/Z11111112222222333333",
            "Condition": {
                "ForAllValues:StringLike":{
                     "route53:ChangeResourceRecordSetsNormalizedRecordNames": ["*-beta.example.com"]
                }
            }
          }
        ]
}
```

------

**Note**  
The IAM wildcard isn't the same as the domain name wildcard. See the following example for how to use the wildcard with a domain name.

**Grant permissions that limit access to DNS records that match a domain name containing a wildcard**  
The following permissions policy grants permissions that allow `ChangeResourceRecordSets` actions on the Hosted Zone Z12345 for example.com. It uses the `route53:ChangeResourceRecordSetsNormalizedRecordNames` condition key to limit user actions only to the records that match \*.example.com.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "route53:ChangeResourceRecordSets",
            "Resource": "arn:aws:route53:::hostedzone/Z11111112222222333333",
            "Condition": {
                "ForAllValues:StringEquals":{
                     "route53:ChangeResourceRecordSetsNormalizedRecordNames": ["\\052.example.com"]
                }
            }
          }
        ]
}
```

------

`\052 `is the octal code for character \* in the DNS name, and `\` in `\052` is escaped to be `\\` to follow JSON syntax.

**Grant permissions that limit access to specific DNS records**  
The following permissions policy grants permissions that allow `ChangeResourceRecordSets` actions on the Hosted Zone Z12345 for example.com. It uses the combination of three condition keys to limit user actions to allow only creating or editing DNS records with certain DNS name and type.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "route53:ChangeResourceRecordSets",
            "Resource": "arn:aws:route53:::hostedzone/Z11111112222222333333",
            "Condition": {
                "ForAllValues:StringEquals":{
                     "route53:ChangeResourceRecordSetsNormalizedRecordNames": ["example.com"],
                     "route53:ChangeResourceRecordSetsRecordTypes": ["MX"],
                     "route53:ChangeResourceRecordSetsActions": ["CREATE", "UPSERT"]
                }
            }
          }
        ]
}
```

------

**Grant permissions that limit access to creating and editing only the specified types of DNS records**  
The following permissions policy grants permissions that allow `ChangeResourceRecordSets` actions on the Hosted Zone Z12345 for example.com. It uses the `route53:ChangeResourceRecordSetsRecordTypes` condition key to limit user actions only on the records which match the specified types (A and AAAA). 

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "route53:ChangeResourceRecordSets",
            "Resource": "arn:aws:route53:::hostedzone/Z11111112222222333333",
            "Condition": {
                "ForAllValues:StringEquals":{
                     "route53:ChangeResourceRecordSetsRecordTypes": ["A", "AAAA"]
                }
            }
          }
        ]
}
```

------

**Grant permissions that specifies the VPC that the IAM principal can operate in**  
The following permissions policy grants permissions that allow `AssociateVPCWithHostedZone` , `DisassociateVPCFromHostedZone`, `ListHostedZonesByVPC`, `CreateHostedZone`, `CreateVPCAssociationAuthorization`, and `DeleteVPCAssociationAuthorization` actions on the VPC specified by the vpc-id.

**Important**  
The condition value must be in the format of `VPCId=<vpc-id>,VPCRegion=<region>`. If you specify a VPC ARN in the condition value, the condition key will not take effect.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Action": [
                "route53:*"
            ],
            "Resource": [
                "*"
            ],
            "Condition": {
                "StringLike": {
                    "route53:VPCs": [
                        "VPCId=<vpc-id>,VPCRegion=<region>"
                    ]
                }
            }
        },
        {
            "Sid": "Statement2",
            "Effect": "Allow",
            "Action": "ec2:DescribeVpcs",
            "Resource": "*"
        }
    ]
}
```

------

**Important**  
The `route53profiles` condition keys are available in all AWS Regions where Route 53 Route53Profiles is available, except for me-central-1 and me-south-1.

**Grant permissions that limit resource association to specific resource types in Route 53 Profiles**  
The following permissions policy grants permissions that allow `AssociateResourceToProfile` and `DisassociateResourceFromProfile` actions only when the resource type is a hosted zone. It uses the `route53profiles:ResourceTypes` condition key to restrict the resource types that can be associated with a profile.

```
{
    "Effect": "Allow",
    "Action": [
        "route53profiles:AssociateResourceToProfile",
        "route53profiles:DisassociateResourceFromProfile"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "route53profiles:ResourceTypes": "HostedZone"
        }
    }
}
```

**Grant permissions that limit resource association to specific resource ARNs in Route 53 Profiles**  
The following permissions policy grants permissions that allow `AssociateResourceToProfile` and `DisassociateResourceFromProfile` actions only for the specified resource ARN. It uses the `route53profiles:ResourceArns` condition key to restrict which resources can be associated with a profile.

```
{
    "Effect": "Allow",
    "Action": [
        "route53profiles:AssociateResourceToProfile",
        "route53profiles:DisassociateResourceFromProfile"
    ],
    "Resource": "*",
    "Condition": {
        "ArnEquals": {
            "route53profiles:ResourceArns": "arn:aws:route53:::hostedzone/Z12345"
        }
    }
}
```

**Grant permissions that limit resource association to specific hosted zone domains in Route 53 Profiles**  
The following permissions policy grants permissions that allow `AssociateResourceToProfile`, `DisassociateResourceFromProfile`, and `UpdateProfileResourceAssociation` actions only when the hosted zone domain matches the specified value. It uses the `route53profiles:HostedZoneDomains` condition key to restrict which hosted zone domains can be associated with a profile.

```
{
    "Effect": "Allow",
    "Action": [
        "route53profiles:AssociateResourceToProfile",
        "route53profiles:DisassociateResourceFromProfile",
        "route53profiles:UpdateProfileResourceAssociation"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "route53profiles:HostedZoneDomains": "example.com"
        }
    }
}
```

**Grant permissions that limit resource association to specific Resolver Rule domains in Route 53 Profiles**  
The following permissions policy grants permissions that allow `AssociateResourceToProfile`, `DisassociateResourceFromProfile`, and `UpdateProfileResourceAssociation` actions only when the Resolver Rule domain matches the specified value. It uses the `route53profiles:ResolverRuleDomains` condition key to restrict which Resolver Rule domains can be associated with a profile.

```
{
    "Effect": "Allow",
    "Action": [
        "route53profiles:AssociateResourceToProfile",
        "route53profiles:DisassociateResourceFromProfile",
        "route53profiles:UpdateProfileResourceAssociation"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "route53profiles:ResolverRuleDomains": "example.com"
        }
    }
}
```

**Grant permissions that limit Firewall Rule Group association to a specific priority range in Route 53 Profiles**  
The following permissions policy grants permissions that allow `AssociateResourceToProfile`, `DisassociateResourceFromProfile`, and `UpdateProfileResourceAssociation` actions only when the Firewall Rule Group priority is within the specified range. It uses the `route53profiles:FirewallRuleGroupPriority` condition key to restrict the priority values that can be used.

```
{
    "Effect": "Allow",
    "Action": [
        "route53profiles:AssociateResourceToProfile",
        "route53profiles:DisassociateResourceFromProfile",
        "route53profiles:UpdateProfileResourceAssociation"
    ],
    "Resource": "*",
    "Condition": {
        "NumericGreaterThanEquals": {
            "route53profiles:FirewallRuleGroupPriority": "100"
        }
    }
}
```

**Grant permissions that limit profile association to specific VPCs in Route 53 Profiles**  
The following permissions policy grants permissions that allow `AssociateProfile` and `DisassociateProfile` actions only for the specified VPC. It uses the `route53profiles:ResourceIds` condition key to restrict which VPCs a profile can be associated with.

```
{
    "Effect": "Allow",
    "Action": [
        "route53profiles:AssociateProfile",
        "route53profiles:DisassociateProfile"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "route53profiles:ResourceIds": "vpc-1a2b3c4d5e6f"
        }
    }
}
```