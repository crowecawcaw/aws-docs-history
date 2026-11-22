

# Using service-linked roles for AWS Network Security Manager

AWS Network Security Manager uses IAM [service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to AWS Network Security Manager. Service-linked roles are predefined by AWS Network Security Manager and include all the permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes setting up AWS Network Security Manager easier because you don't have to manually add the necessary permissions. AWS Network Security Manager defines the permissions of its service-linked roles. Unless defined otherwise, only AWS Network Security Manager can assume its roles. The defined permissions include the trust policy and the permissions policy. You can't attach that permissions policy to any other IAM entity.

You can delete a service-linked role only after you first delete the related resources. This protects your AWS Network Security Manager resources because you can't inadvertently remove permission to access the resources.

For information about other services that support service-linked roles, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) and look for the services that include **Yes** in the **Service-linked role** column. Choose the **Yes** link to view the service-linked role documentation for that service.

## Service-linked role permissions for AWS Network Security Manager
<a name="slr-permissions"></a>

AWS Network Security Manager uses the service-linked role named `AWSServiceRoleForNetworkSecurityManager`. This service-linked role trusts the `network-security-manager.amazonaws.com` service principal to assume the role.

The role permissions policy named `NetworkSecurityManagerServiceRolePolicy` is an AWS managed policy that allows AWS Network Security Manager to complete actions on the specified resources.

The following trust policy allows the `network-security-manager.amazonaws.com` service principal to assume the role.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "network-security-manager.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

**Note**  
You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

### Permissions details
<a name="slr-permissions-details"></a>

AWS Network Security Manager requires each group of permissions to protect and discover resources across your account and organization. The `NetworkSecurityManagerServiceRolePolicy` managed policy grants the following permissions, grouped by service:
+ `wafv2` – Create, read, update, and delete web ACLs and Firewall Manager rule groups. Associate and disassociate web ACLs with protected resources. Manage web ACL logging configurations and rule group permission policies. Tag and untag resources. Check web ACL capacity. Validate AWS Network Security Manager web ACL and rule configurations.
+ `network-firewall` – Create, read, update, and delete Network Firewall firewalls and firewall policies, including V2. Associate and disassociate firewall policies, subnets, and Availability Zones. Manage TLS inspection configurations, rule groups, logging configurations, and resource policies. Set firewall and policy change and delete protection. Tag and untag resources.
+ `shield` – Create, describe, list, and delete AWS Shield Advanced protections. Create and describe the AWS Shield Advanced subscription.
+ `elasticloadbalancing` – Describe Application Load Balancers, tags, and web ACL associations. Get the load balancer web ACL. Create, delete, and set web ACL associations on Application Load Balancers.
+ `cloudfront` – Get and list Amazon CloudFront distributions, configurations, and tags. Associate and disassociate distribution web ACLs. Read VPC origins.
+ `apigateway` – Read Amazon API Gateway REST APIs, stages, and tags. Set the web ACL on an API stage.
+ `ec2` – Describe VPCs, subnets, route tables, Availability Zones, internet gateways, VPC endpoints, Elastic IP addresses, and tags. Create, delete, associate, and disassociate route tables and subnets, and replace route table associations, to deploy Network Firewall. Create tags. Read Amazon EC2 Verified Access instance web ACLs and associations.
+ `ram` – Create, update, delete, and associate AWS Resource Access Manager (AWS RAM) resource shares, read resource shares and their associations, and tag resources so AWS Network Security Manager can share Network Firewall resources across your organization.
+ `cognito-idp`, `apprunner`, `appsync`, `amplify`, and `bedrock-agentcore` – Read web ACL associations for Amazon Cognito user pools, AWS App Runner services, AWS AppSync GraphQL APIs, AWS Amplify apps, and Amazon Bedrock AgentCore gateways so AWS Network Security Manager can discover protected resources.
+ `config` – Select resource configurations and manage the service-linked AWS Config configuration recorder that AWS Network Security Manager uses to discover in-scope resources.
+ `organizations` – Read your organization, accounts, roots, parents, children, organizational units, delegated administrators, and enabled service access so AWS Network Security Manager can operate across your organization.
+ `logs` – Create, read, update, delete, and list log deliveries for web ACL logging.
+ `s3` – Get and put bucket policies on Amazon S3 buckets whose names begin with `aws-waf-logs-` so web ACL logs can be delivered.
+ `servicequotas` – Read AWS WAF and Shield service quotas.
+ `payments` – Read the AWS Payments connected account for AWS Network Security Manager-managed resources.
+ `iam` – Get roles and create the service-linked roles that AWS Shield Advanced, AWS Config, AWS WAF, and Network Firewall require, scoped by the `iam:AWSServiceName` condition key.

The following JSON shows the complete `NetworkSecurityManagerServiceRolePolicy` permissions policy.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "LogsGeneral",
      "Effect": "Allow",
      "Action": [
        "logs:ListLogDeliveries",
        "logs:CreateLogDelivery",
        "logs:GetLogDelivery",
        "logs:UpdateLogDelivery",
        "logs:DeleteLogDelivery"
      ],
      "Resource": "*"
    },
    {
      "Sid": "S3LogBucketGeneral",
      "Effect": "Allow",
      "Action": [
        "s3:GetBucketPolicy",
        "s3:PutBucketPolicy"
      ],
      "Resource": "arn:aws:s3:::aws-waf-logs-*"
    },
    {
      "Sid": "CloudfrontVpcOriginAccess",
      "Effect": "Allow",
      "Action": [
        "cloudfront:GetVpcOrigin"
      ],
      "Resource": "arn:aws:cloudfront::*:vpcorigin/*"
    },
    {
      "Sid": "ConfigUnscoped",
      "Effect": "Allow",
      "Action": [
        "config:SelectResourceConfig"
      ],
      "Resource": "*"
    },
    {
      "Sid": "DescribeOrganizationUnScoped",
      "Effect": "Allow",
      "Action": [
        "organizations:DescribeOrganization",
        "organizations:ListAccounts",
        "organizations:ListChildren",
        "organizations:ListRoots",
        "organizations:ListParents",
        "organizations:ListOrganizationalUnitsForParent",
        "organizations:ListAWSServiceAccessForOrganization"
      ],
      "Resource": "*"
    },
    {
      "Sid": "DescribeAccountScoped",
      "Effect": "Allow",
      "Action": "organizations:DescribeAccount",
      "Resource": "arn:aws:organizations::*:account/o-*/*"
    },
    {
      "Sid": "DescribeOrganizationUnitScoped",
      "Effect": "Allow",
      "Action": "organizations:DescribeOrganizationalUnit",
      "Resource": "arn:aws:organizations::*:ou/o-*/ou-*"
    },
    {
      "Sid": "ListDelegatedAdministratorsScoped",
      "Effect": "Allow",
      "Action": "organizations:ListDelegatedAdministrators",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "organizations:ServicePrincipal": [
            "network-security-manager.amazonaws.com"
          ]
        }
      }
    },
    {
      "Sid": "LoadBalancerNonMutationApiAccess",
      "Effect": "Allow",
      "Action": [
        "elasticloadbalancing:DescribeLoadBalancers",
        "elasticloadbalancing:DescribeTags",
        "elasticloadbalancing:DescribeWebACLAssociation"
      ],
      "Resource": "*"
    },
    {
      "Sid": "LoadBalancerGetWebACLScoped",
      "Effect": "Allow",
      "Action": "elasticloadbalancing:GetLoadBalancerWebACL",
      "Resource": "arn:aws:elasticloadbalancing:*:*:loadbalancer/app/*/*"
    },
    {
      "Sid": "CloudFrontDistributionNonMutationApiAccess",
      "Effect": "Allow",
      "Action": [
        "cloudfront:GetDistribution",
        "cloudfront:GetDistributionConfig",
        "cloudfront:ListTagsForResource"
      ],
      "Resource": "arn:aws:cloudfront::*:distribution/*"
    },
    {
      "Sid": "ApiGatewayStageNonMutationApiAccess",
      "Effect": "Allow",
      "Action": "apigateway:GET",
      "Resource": [
        "arn:aws:apigateway:*::/restapis",
        "arn:aws:apigateway:*::/restapis/*/stages",
        "arn:aws:apigateway:*::/restapis/*/stages/*",
        "arn:aws:apigateway:*::/tags/*"
      ]
    },
    {
      "Sid": "Wafv2General",
      "Effect": "Allow",
      "Action": [
        "wafv2:TagResource",
        "wafv2:ListResourcesForWebACL",
        "wafv2:AssociateWebACL",
        "wafv2:ListTagsForResource",
        "wafv2:UntagResource",
        "wafv2:GetWebACL",
        "wafv2:DisassociateFirewallManager",
        "wafv2:DeleteWebACL",
        "wafv2:DisassociateWebACL",
        "wafv2:ValidateNetworkSecurityManagerWebACLConfiguration",
        "wafv2:ValidateNetworkSecurityManagerRuleConfiguration"
      ],
      "Resource": "arn:aws:wafv2:*:*:*/webacl/*"
    },
    {
      "Sid": "Wafv2WebAclAndRuleGroupMutation",
      "Effect": "Allow",
      "Action": [
        "wafv2:UpdateWebACL",
        "wafv2:CreateWebACL",
        "wafv2:DeleteFirewallManagerRuleGroups",
        "wafv2:PutFirewallManagerRuleGroups"
      ],
      "Resource": [
        "arn:aws:wafv2:*:*:*/webacl/*",
        "arn:aws:wafv2:*:*:global/rulegroup/*",
        "arn:aws:wafv2:*:*:regional/rulegroup/*",
        "arn:aws:wafv2:*:*:global/managedruleset/*",
        "arn:aws:wafv2:*:*:regional/managedruleset/*",
        "arn:aws:wafv2:*:*:global/ipset/*",
        "arn:aws:wafv2:*:*:regional/ipset/*",
        "arn:aws:wafv2:*:*:global/regexpatternset/*",
        "arn:aws:wafv2:*:*:regional/regexpatternset/*"
      ]
    },
    {
      "Sid": "Wafv2Logging",
      "Effect": "Allow",
      "Action": [
        "wafv2:PutLoggingConfiguration",
        "wafv2:GetLoggingConfiguration",
        "wafv2:DeleteLoggingConfiguration"
      ],
      "Resource": "arn:aws:wafv2:*:*:*/webacl/*"
    },
    {
      "Sid": "Wafv2ListLogging",
      "Effect": "Allow",
      "Action": "wafv2:ListLoggingConfigurations",
      "Resource": "*"
    },
    {
      "Sid": "Wafv2ListWebACLs",
      "Effect": "Allow",
      "Action": "wafv2:ListWebACLs",
      "Resource": "*"
    },
    {
      "Sid": "Wafv2PermissionPolicy",
      "Effect": "Allow",
      "Action": [
        "wafv2:PutPermissionPolicy",
        "wafv2:GetPermissionPolicy",
        "wafv2:DeletePermissionPolicy"
      ],
      "Resource": [
        "arn:aws:wafv2:*:*:global/rulegroup/*",
        "arn:aws:wafv2:*:*:regional/rulegroup/*"
      ]
    },
    {
      "Sid": "Wafv2WebaclDescribe",
      "Effect": "Allow",
      "Action": "wafv2:GetWebACLForResource",
      "Resource": "arn:aws:wafv2:*:*:*/webacl/*"
    },
    {
      "Sid": "Wafv2GetConnectedAccount",
      "Effect": "Allow",
      "Action": [
        "payments:GetConnectedAccount"
      ],
      "Resource": "arn:aws:payments:*:*:connectedaccount/*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid": "CloudFrontListDistributions",
      "Effect": "Allow",
      "Action": [
        "cloudfront:ListDistributionsByWebACLId",
        "cloudfront:ListDistributions"
      ],
      "Resource": "*"
    },
    {
      "Sid": "CloudFrontDistributionMutation",
      "Effect": "Allow",
      "Action": [
        "cloudfront:AssociateDistributionWebACL",
        "cloudfront:DisassociateDistributionWebACL"
      ],
      "Resource": "arn:aws:cloudfront::*:distribution/*"
    },
    {
      "Sid": "ElbWebAclRemediationScoped",
      "Effect": "Allow",
      "Action": [
        "elasticloadbalancing:CreateWebACLAssociation",
        "elasticloadbalancing:DeleteWebACLAssociation"
      ],
      "Resource": "arn:aws:elasticloadbalancing:*:*:loadbalancer/app/*/*"
    },
    {
      "Sid": "ElbSetWebAcl",
      "Effect": "Allow",
      "Action": "elasticloadbalancing:SetWebACL",
      "Resource": "*"
    },
    {
      "Sid": "ApiGatewayWebAclRemediation",
      "Effect": "Allow",
      "Action": "apigateway:SetWebACL",
      "Resource": "arn:aws:apigateway:*::/restapis/*/stages/*"
    },
    {
      "Sid": "CognitoWebAclIntegration",
      "Effect": "Allow",
      "Action": [
        "cognito-idp:GetWebACLForResource",
        "cognito-idp:ListResourcesForWebACL"
      ],
      "Resource": "*"
    },
    {
      "Sid": "AppRunnerWebAclIntegration",
      "Effect": "Allow",
      "Action": [
        "apprunner:DescribeWebAclForService",
        "apprunner:ListAssociatedServicesForWebAcl"
      ],
      "Resource": "*"
    },
    {
      "Sid": "VerifiedAccessWebAclIntegration",
      "Effect": "Allow",
      "Action": [
        "ec2:GetVerifiedAccessInstanceWebAcl",
        "ec2:DescribeVerifiedAccessInstanceWebAclAssociations"
      ],
      "Resource": "*"
    },
    {
      "Sid": "AppSyncWebAclIntegration",
      "Effect": "Allow",
      "Action": [
        "appsync:GetWebACLForResource",
        "appsync:ListResourcesForWebACL"
      ],
      "Resource": "*"
    },
    {
      "Sid": "AmplifyWebAclIntegration",
      "Effect": "Allow",
      "Action": [
        "amplify:GetWebACLForResource",
        "amplify:ListResourcesForWebACL"
      ],
      "Resource": "*"
    },
    {
      "Sid": "ShieldGeneral",
      "Effect": "Allow",
      "Action": [
        "shield:CreateProtection",
        "shield:DeleteProtection",
        "shield:DescribeProtection",
        "shield:ListProtections",
        "shield:CreateSubscription",
        "shield:DescribeSubscription",
        "shield:GetSubscriptionState",
        "ec2:DescribeAddresses",
        "elasticloadbalancing:DescribeLoadBalancers",
        "elasticloadbalancing:DescribeTags"
      ],
      "Resource": "*"
    },
    {
      "Sid": "ShieldSlrCreation",
      "Effect": "Allow",
      "Action": "iam:CreateServiceLinkedRole",
      "Resource": "arn:aws:iam::*:role/aws-service-role/shield.amazonaws.com/*",
      "Condition": {
        "StringEquals": {
          "iam:AWSServiceName": "shield.amazonaws.com"
        }
      }
    },
    {
      "Sid": "AllowConfigRecorderList",
      "Effect": "Allow",
      "Action": "config:ListConfigurationRecorders",
      "Resource": "*"
    },
    {
      "Sid": "AllowPutServiceLinkedConfigRecorder",
      "Effect": "Allow",
      "Action": "config:PutServiceLinkedConfigurationRecorder",
      "Resource": "*"
    },
    {
      "Sid": "AllowConfigRecorderScopedAccess",
      "Effect": "Allow",
      "Action": [
        "config:DescribeConfigurationRecorders",
        "config:DescribeConfigurationRecorderStatus",
        "config:DeleteServiceLinkedConfigurationRecorder",
        "config:AssociateResourceTypes",
        "config:DisassociateResourceTypes"
      ],
      "Resource": "arn:aws:config:*:*:configuration-recorder/*"
    },
    {
      "Sid": "AllowCreateConfigServiceLinkedRole",
      "Effect": "Allow",
      "Action": "iam:CreateServiceLinkedRole",
      "Resource": "arn:aws:iam::*:role/aws-service-role/config.amazonaws.com/*",
      "Condition": {
        "StringEquals": {
          "iam:AWSServiceName": "config.amazonaws.com"
        }
      }
    },
    {
      "Sid": "AllowListActionsForAgentCoreGateway",
      "Effect": "Allow",
      "Action": [
        "bedrock-agentcore:GatewayListResourcesForWebACL"
      ],
      "Resource": "*"
    },
    {
      "Sid": "AllowGetActionForAgentCoreGateway",
      "Effect": "Allow",
      "Action": [
        "bedrock-agentcore:GatewayGetWebACLForResource"
      ],
      "Resource": "arn:aws:bedrock-agentcore:*:*:gateway/*"
    },
    {
      "Sid": "WafV2LoggingSlrCreation",
      "Effect": "Allow",
      "Action": "iam:CreateServiceLinkedRole",
      "Resource": "arn:aws:iam::*:role/aws-service-role/wafv2.amazonaws.com/*",
      "Condition": {
        "StringEquals": {
          "iam:AWSServiceName": "wafv2.amazonaws.com"
        }
      }
    },
    {
      "Sid": "SlrCreation",
      "Effect": "Allow",
      "Action": "iam:CreateServiceLinkedRole",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "iam:AWSServiceName": [
            "network-firewall.amazonaws.com",
            "igw-firewall.network-firewall.amazonaws.com"
          ]
        }
      }
    },
    {
      "Sid": "IamDescribe",
      "Effect": "Allow",
      "Action": "iam:GetRole",
      "Resource": "arn:*:iam::*:role/aws-service-role/ram.amazonaws.com/*"
    },
    {
      "Sid": "NetworkFirewallCreateScoped",
      "Effect": "Allow",
      "Action": [
        "network-firewall:CreateFirewall"
      ],
      "Resource": [
        "arn:*:network-firewall:*:*:firewall/*",
        "arn:*:network-firewall:*:*:igw-firewall/*"
      ],
      "Condition": {
        "ForAllValues:StringEquals": {
          "aws:TagKeys": [
            "Name",
            "NSMManaged"
          ]
        },
        "StringEquals": {
          "aws:RequestTag/NSMManaged": [
            "true"
          ]
        }
      }
    },
    {
      "Sid": "NetworkFirewallCreateScopedFirewallPolicy",
      "Effect": "Allow",
      "Action": [
        "network-firewall:CreateFirewall"
      ],
      "Resource": [
        "arn:*:network-firewall:*:*:firewall-policy/*",
        "arn:*:network-firewall:*:*:firewall-policy-v2/*"
      ],
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/NSMManaged": "true"
        }
      }
    },
    {
      "Sid": "NetworkFirewallTagManagement",
      "Effect": "Allow",
      "Action": "network-firewall:TagResource",
      "Resource": [
        "arn:*:network-firewall:*:*:firewall/*",
        "arn:*:network-firewall:*:*:igw-firewall/*",
        "arn:*:network-firewall:*:*:firewall-policy/*",
        "arn:*:network-firewall:*:*:firewall-policy-v2/*"
      ],
      "Condition": {
        "ForAllValues:StringEquals": {
          "aws:TagKeys": [
            "Name",
            "NSMManaged"
          ]
        },
        "StringEquals": {
          "aws:RequestTag/NSMManaged": [
            "true"
          ],
          "aws:ResourceTag/NSMManaged": [
            "true"
          ]
        }
      }
    },
    {
      "Sid": "NetworkFirewallUnTag",
      "Effect": "Allow",
      "Action": "network-firewall:UntagResource",
      "Resource": [
        "arn:*:network-firewall:*:*:firewall/*",
        "arn:*:network-firewall:*:*:igw-firewall/*",
        "arn:*:network-firewall:*:*:firewall-policy/*",
        "arn:*:network-firewall:*:*:firewall-policy-v2/*"
      ],
      "Condition": {
        "ForAllValues:StringEquals": {
          "aws:TagKeys": [
            "Name",
            "NSMManaged"
          ]
        },
        "StringEquals": {
          "aws:ResourceTag/NSMManaged": [
            "true"
          ]
        }
      }
    },
    {
      "Sid": "NetworkFirewallRead",
      "Effect": "Allow",
      "Action": [
        "network-firewall:DescribeFirewall",
        "network-firewall:DescribeFirewallPolicy",
        "network-firewall:DescribeFirewallPolicyV2",
        "network-firewall:DescribeRuleGroup",
        "network-firewall:ListFirewallPolicies",
        "network-firewall:ListFirewallPoliciesV2",
        "network-firewall:ListFirewalls",
        "network-firewall:ListRuleGroups",
        "network-firewall:DescribeResourcePolicy",
        "network-firewall:DescribeLoggingConfiguration",
        "network-firewall:DescribeTLSInspectionConfiguration",
        "network-firewall:ListTLSInspectionConfigurations"
      ],
      "Resource": "*"
    },
    {
      "Sid": "NetworkFirewallUpdateScoped",
      "Effect": "Allow",
      "Action": [
        "network-firewall:AssociateSubnets",
        "network-firewall:AssociateAvailabilityZones",
        "network-firewall:DisassociateSubnets",
        "network-firewall:DisassociateAvailabilityZones",
        "network-firewall:UpdateFirewallDeleteProtection",
        "network-firewall:UpdateFirewallPolicyChangeProtection",
        "network-firewall:UpdateSubnetChangeProtection",
        "network-firewall:UpdateLoggingConfiguration"
      ],
      "Resource": [
        "arn:*:network-firewall:*:*:firewall/*",
        "arn:*:network-firewall:*:*:igw-firewall/*"
      ],
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/NSMManaged": "true"
        }
      }
    },
    {
      "Sid": "NetworkFirewallCreateFirewallPolicyResource",
      "Effect": "Allow",
      "Action": [
        "network-firewall:CreateFirewallPolicy",
        "network-firewall:CreateFirewallPolicyV2"
      ],
      "Resource": [
        "arn:*:network-firewall:*:*:firewall-policy/*",
        "arn:*:network-firewall:*:*:firewall-policy-v2/*"
      ],
      "Condition": {
        "ForAllValues:StringEquals": {
          "aws:TagKeys": [
            "Name",
            "NSMManaged"
          ]
        },
        "StringEquals": {
          "aws:RequestTag/NSMManaged": [
            "true"
          ]
        }
      }
    },
    {
      "Sid": "NetworkFirewallPolicyDependentResource",
      "Effect": "Allow",
      "Action": [
        "network-firewall:CreateFirewallPolicy",
        "network-firewall:CreateFirewallPolicyV2",
        "network-firewall:UpdateFirewallPolicy",
        "network-firewall:UpdateFirewallPolicyV2"
      ],
      "Resource": [
        "arn:*:network-firewall:*:*:stateful-rulegroup/*",
        "arn:*:network-firewall:*:*:stateless-rulegroup/*",
        "arn:*:network-firewall:*:*:tls-configuration/*",
        "arn:*:network-firewall:*:*:firewall-rulegroup/*",
        "arn:*:network-firewall:*:*:ips-rulegroup/*"
      ]
    },
    {
      "Sid": "NetworkFirewallPolicyUpdateScoped",
      "Effect": "Allow",
      "Action": [
        "network-firewall:UpdateFirewallPolicy",
        "network-firewall:UpdateFirewallPolicyV2"
      ],
      "Resource": [
        "arn:*:network-firewall:*:*:firewall-policy/*",
        "arn:*:network-firewall:*:*:firewall-policy-v2/*"
      ],
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/NSMManaged": "true"
        }
      }
    },
    {
      "Sid": "NetworkFirewallAssociateFirewallPolicy",
      "Effect": "Allow",
      "Action": [
        "network-firewall:AssociateFirewallPolicy"
      ],
      "Resource": [
        "arn:*:network-firewall:*:*:firewall-policy/*",
        "arn:*:network-firewall:*:*:firewall-policy-v2/*",
        "arn:*:network-firewall:*:*:firewall/*",
        "arn:*:network-firewall:*:*:igw-firewall/*"
      ],
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/NSMManaged": "true"
        }
      }
    },
    {
      "Sid": "NetworkFirewallResourcePolicyRulegroups",
      "Effect": "Allow",
      "Action": [
        "network-firewall:PutResourcePolicy",
        "network-firewall:DeleteResourcePolicy"
      ],
      "Resource": [
        "arn:*:network-firewall:*:*:stateful-rulegroup/*",
        "arn:*:network-firewall:*:*:stateless-rulegroup/*",
        "arn:*:network-firewall:*:*:firewall-rulegroup/*",
        "arn:*:network-firewall:*:*:ips-rulegroup/*"
      ]
    },
    {
      "Sid": "NetworkFirewallResourcePolicyScoped",
      "Effect": "Allow",
      "Action": [
        "network-firewall:PutResourcePolicy",
        "network-firewall:DeleteResourcePolicy"
      ],
      "Resource": [
        "arn:*:network-firewall:*:*:firewall-policy/*",
        "arn:*:network-firewall:*:*:firewall-policy-v2/*",
        "arn:*:network-firewall:*:*:firewall/*",
        "arn:*:network-firewall:*:*:igw-firewall/*"
      ],
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/NSMManaged": "true"
        }
      }
    },
    {
      "Sid": "NetworkFirewallCleanup",
      "Effect": "Allow",
      "Action": [
        "network-firewall:DeleteFirewallPolicy",
        "network-firewall:DeleteFirewallPolicyV2",
        "network-firewall:DeleteFirewall"
      ],
      "Resource": [
        "arn:*:network-firewall:*:*:firewall-policy/*",
        "arn:*:network-firewall:*:*:firewall-policy-v2/*",
        "arn:*:network-firewall:*:*:firewall/*",
        "arn:*:network-firewall:*:*:igw-firewall/*"
      ],
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/NSMManaged": "true"
        }
      }
    },
    {
      "Sid": "RamTagManagement",
      "Effect": "Allow",
      "Action": [
        "ram:TagResource"
      ],
      "Resource": [
        "arn:*:ram:*:*:resource-share/*"
      ],
      "Condition": {
        "ForAllValues:StringEquals": {
          "aws:TagKeys": [
            "Name",
            "NSMManaged"
          ]
        },
        "StringEquals": {
          "aws:RequestTag/NSMManaged": [
            "true"
          ],
          "aws:ResourceTag/NSMManaged": [
            "true"
          ]
        }
      }
    },
    {
      "Sid": "RamMutation",
      "Effect": "Allow",
      "Action": [
        "ram:AssociateResourceShare",
        "ram:UpdateResourceShare",
        "ram:DeleteResourceShare"
      ],
      "Resource": "arn:*:ram:*:*:resource-share/*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/NSMManaged": "true"
        }
      }
    },
    {
      "Sid": "RamCreation",
      "Effect": "Allow",
      "Action": "ram:CreateResourceShare",
      "Resource": "arn:*:ram:*:*:resource-share/*",
      "Condition": {
        "ForAllValues:StringEquals": {
          "aws:TagKeys": [
            "Name",
            "NSMManaged"
          ]
        },
        "StringEquals": {
          "aws:RequestTag/NSMManaged": "true"
        }
      }
    },
    {
      "Sid": "RamDescribe",
      "Effect": "Allow",
      "Action": [
        "ram:GetResourceShareAssociations",
        "ram:GetResourceShares"
      ],
      "Resource": "*"
    },
    {
      "Sid": "Ec2DescribeUnscoped",
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeInternetGateways",
        "ec2:DescribeRouteTables",
        "ec2:DescribeSubnets",
        "ec2:DescribeTags",
        "ec2:DescribeVpcEndpoints",
        "ec2:DescribeAvailabilityZones",
        "ec2:DescribeVpcs"
      ],
      "Resource": "*"
    },
    {
      "Sid": "Ec2RouteTableScoped",
      "Effect": "Allow",
      "Action": [
        "ec2:AssociateRouteTable",
        "ec2:ReplaceRouteTableAssociation",
        "ec2:DisassociateRouteTable"
      ],
      "Resource": [
        "arn:*:ec2:*:*:route-table/*",
        "arn:*:ec2:*:*:subnet/*"
      ],
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/NSMManaged": "true"
        }
      }
    },
    {
      "Sid": "Ec2RouteTableCreate",
      "Effect": "Allow",
      "Action": [
        "ec2:CreateRouteTable"
      ],
      "Resource": [
        "arn:*:ec2:*:*:route-table/*"
      ],
      "Condition": {
        "ForAllValues:StringEquals": {
          "aws:TagKeys": [
            "Name",
            "NSMManaged"
          ]
        },
        "StringEquals": {
          "aws:RequestTag/NSMManaged": [
            "true"
          ]
        }
      }
    },
    {
      "Sid": "RouteTableCleanup",
      "Effect": "Allow",
      "Action": "ec2:DeleteRouteTable",
      "Resource": "arn:*:ec2:*:*:route-table/*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/NSMManaged": "true"
        }
      }
    },
    {
      "Sid": "Ec2TagManagement",
      "Effect": "Allow",
      "Action": "ec2:CreateTags",
      "Resource": [
        "arn:*:ec2:*:*:route-table/*",
        "arn:*:ec2:*:*:subnet/*"
      ],
      "Condition": {
        "ForAllValues:StringEquals": {
          "aws:TagKeys": [
            "Name",
            "NSMManaged"
          ]
        },
        "StringEquals": {
          "aws:RequestTag/NSMManaged": "true",
          "ec2:CreateAction": [
            "CreateRouteTable",
            "CreateSubnet"
          ]
        }
      }
    },
    {
      "Sid": "Ec2SubnetCreate",
      "Effect": "Allow",
      "Action": [
        "ec2:CreateSubnet"
      ],
      "Resource": [
        "arn:*:ec2:*:*:subnet/*"
      ],
      "Condition": {
        "ForAllValues:StringEquals": {
          "aws:TagKeys": [
            "Name",
            "NSMManaged"
          ]
        },
        "StringEquals": {
          "aws:RequestTag/NSMManaged": [
            "true"
          ]
        }
      }
    },
    {
      "Sid": "Ec2SubnetCleanup",
      "Effect": "Allow",
      "Action": [
        "ec2:DeleteSubnet"
      ],
      "Resource": [
        "arn:*:ec2:*:*:subnet/*"
      ],
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/NSMManaged": "true"
        }
      }
    },
    {
      "Sid": "DependencyQuotaRead",
      "Effect": "Allow",
      "Action": "servicequotas:GetServiceQuota",
      "Resource": [
        "arn:*:servicequotas:*:*:wafv2/*",
        "arn:*:servicequotas:*:*:shield/*"
      ]
    },
    {
      "Sid": "Wafv2CheckCapacity",
      "Effect": "Allow",
      "Action": "wafv2:CheckCapacity",
      "Resource": "*"
    }
  ]
}
```

## Creating a service-linked role for AWS Network Security Manager
<a name="slr-create"></a>

You don't need to manually create a service-linked role. When you enable AWS Network Security Manager, AWS Network Security Manager creates the service-linked role for you. There is no manual step to perform.

If you delete this service-linked role and then need to create it again, AWS Network Security Manager recreates the role the next time you use the service. You don't have to take any action.

For more information, see [Creating a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#create-service-linked-role) in the *IAM User Guide*.

## Editing a service-linked role for AWS Network Security Manager
<a name="slr-edit"></a>

You can't change the permissions of the `AWSServiceRoleForNetworkSecurityManager` service-linked role. After you create a service-linked role, you can't change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM.

For more information, see [Editing a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

## Deleting a service-linked role for AWS Network Security Manager
<a name="slr-delete"></a>

If you no longer need to use AWS Network Security Manager, we recommend that you delete the `AWSServiceRoleForNetworkSecurityManager` service-linked role.

Before you delete the service-linked role, clean up the resources that AWS Network Security Manager manages. Disable AWS Network Security Manager and remove the policies and scopes so that no resources that AWS Network Security Manager manages remain in your account. You can then delete the role manually.

**Note**  
If AWS Network Security Manager is using the role when you try to delete the resources, the deletion might fail. If that happens, wait for a few minutes and try the operation again.

**To manually delete the service-linked role using IAM**

1. Open the **Roles** page of the IAM console at [https://console.aws.amazon.com/iam/home\#/roles](https://console.aws.amazon.com/iam/home#/roles).

1. In the search box, enter `AWSServiceRoleForNetworkSecurityManager`, and then select the role.

1. Choose **Delete**.

1. To confirm the deletion, enter the role name, and then choose **Delete**.

For more information, see [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

## Supported Regions for AWS Network Security Manager service-linked roles
<a name="slr-regions"></a>

AWS Network Security Manager supports using service-linked roles in all of the AWS Regions where AWS Network Security Manager is available.