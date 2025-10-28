# AWS Cloud Map API permissions reference

When you set up access control and write
a permissions policy that you can attach to an IAM identity (identity-based policies), you
can use the following list as a reference. The list includes each AWS Cloud Map API action and
the actions that you must grant permissions access to. You specify the actions in the
`Action` field for the policy. For details about the resource value you must
specify in the `Resource` field or the IAM policy, see [Actions, resources, and condition keys for AWS Cloud Map](../../../service-authorization/latest/reference/list_awscloudmap.md "../../../service-authorization/latest/reference/list_awscloudmap.md") in the _Service
Authorization Reference_.

You can use AWS Cloud Map–specific condition keys in your IAM policies for some
operations. For more information, see [Condition keys for AWS Cloud Map](../../../service-authorization/latest/reference/list_awscloudmap.md#awscloudmap-policy-keys "../../../service-authorization/latest/reference/list_awscloudmap.md#awscloudmap-policy-keys") in the _Service Authorization
Reference_.

To specify an action, use the `servicediscovery` prefix followed by the API
action name, for example, `servicediscovery:CreatePublicDnsNamespace` and
`route53:CreateHostedZone`.

## Required permissions for AWS Cloud Map

actions

[CreateHttpNamespace](../api/API_CreateHttpNamespace.md "../api/API_CreateHttpNamespace.md")

Required permissions (API action):

- `servicediscovery:CreateHttpNamespace`

[CreatePrivateDnsNamespace](../api/API_CreatePrivateDnsNamespace.md "../api/API_CreatePrivateDnsNamespace.md")

Required permissions (API action):

- `servicediscovery:CreatePrivateDnsNamespace`
- `route53:CreateHostedZone`
- `route53:GetHostedZone`
- `route53:ListHostedZonesByName`
- `ec2:DescribeVpcs`
- `ec2:DescribeRegions`

[CreatePublicDnsNamespace](../api/API_CreatePublicDnsNamespace.md "../api/API_CreatePublicDnsNamespace.md")

Required permissions (API action):

- `servicediscovery:CreatePublicDnsNamespace`
- `route53:CreateHostedZone`
- `route53:GetHostedZone`
- `route53:ListHostedZonesByName`

[CreateService](../api/API_CreateService.md "../api/API_CreateService.md")

Required Permissions (API Action):
`servicediscovery:CreateService`

[DeleteNamespace](../api/API_DeleteNamespace.md "../api/API_DeleteNamespace.md")

Required permissions (API action):

- `servicediscovery:DeleteNamespace`

[DeleteService](../api/API_DeleteService.md "../api/API_DeleteService.md")

Required Permissions (API Action):
`servicediscovery:DeleteService`

[DeleteServiceAttributes](../api/API_DeleteServiceAttributes.md "../api/API_DeleteServiceAttributes.md")

Required Permissions (API Action):
`servicediscovery:DeleteServiceAttributes`

[DeregisterInstance](../api/API_DeregisterInstance.md "../api/API_DeregisterInstance.md")

Required permissions (API action):

- `servicediscovery:DeregisterInstance`
- `route53:GetHealthCheck`
- `route53:DeleteHealthCheck`
- `route53:UpdateHealthCheck`

[DiscoverInstances](../api/API_DiscoverInstances.md "../api/API_DiscoverInstances.md")

Required Permissions (API Action):
`servicediscovery:DiscoverInstances`

[GetInstance](../api/API_GetInstance.md "../api/API_GetInstance.md")

Required Permissions (API Action):
`servicediscovery:GetInstance`

[GetInstancesHealthStatus](../api/API_GetInstancesHealthStatus.md "../api/API_GetInstancesHealthStatus.md")

Required Permissions (API Action):
`servicediscovery:GetInstancesHealthStatus`

[GetNamespace](../api/API_GetNamespace.md "../api/API_GetNamespace.md")

Required Permissions (API Action):
`servicediscovery:GetNamespace`

[GetOperation](../api/API_GetOperation.md "../api/API_GetOperation.md")

Required Permissions (API Action):
`servicediscovery:GetOperation`

[GetService](../api/API_GetService.md "../api/API_GetService.md")

Required Permissions (API Action): `servicediscovery:GetService`

[GetServiceAttributes](../api/API_GetServiceAttributes.md "../api/API_GetServiceAttributes.md")

Required Permissions (API Action): `servicediscovery:GetServiceAttributes`

[ListInstances](../api/API_ListInstances.md "../api/API_ListInstances.md")

Required Permissions (API Action):
`servicediscovery:ListInstances`

[ListNamespaces](../api/API_ListNamespaces.md "../api/API_ListNamespaces.md")

Required Permissions (API Action):
`servicediscovery:ListNamespaces`

[ListOperations](../api/API_ListOperations.md "../api/API_ListOperations.md")

Required Permissions (API Action):
`servicediscovery:ListOperations`

[ListServices](../api/API_ListServices.md "../api/API_ListServices.md")

Required Permissions (API Action):
`servicediscovery:ListServices`

[ListTagsForResource](../api/API_ListTagsForResource.md "../api/API_ListTagsForResource.md")

Required Permissions (API Action):
`servicediscovery:ListTagsForResource`

[RegisterInstance](../api/API_RegisterInstance.md "../api/API_RegisterInstance.md")

Required permissions (API action):

- `servicediscovery:RegisterInstance`
- `route53:GetHealthCheck`
- `route53:CreateHealthCheck`
- `route53:UpdateHealthCheck`
- `ec2:DescribeInstances`

[TagResource](../api/API_TagResource.md "../api/API_TagResource.md")

Required Permissions (API Action):
`servicediscovery:TagResource`

[UntagResource](../api/API_UntagResource.md "../api/API_UntagResource.md")

Required Permissions (API Action):
`servicediscovery:UntagResource`

[UpdateHttpNamespace](../api/API_UpdateHttpNamespace.md "../api/API_UpdateHttpNamespace.md")

Required Permissions (API Action):
`servicediscovery:UpdateHttpNamespace`

[UpdateInstanceCustomHealthStatus](../api/API_UpdateInstanceCustomHealthStatus.md "../api/API_UpdateInstanceCustomHealthStatus.md")

Required Permissions (API Action):
`servicediscovery:UpdateInstanceCustomHealthStatus`

[UpdatePrivateDnsNamespace](../api/API_UpdatePrivateDnsNamespace.md "../api/API_UpdatePrivateDnsNamespace.md")

Required permissions (API action):

- `servicediscovery:UpdatePrivateDnsNamespace`
- `route53:ChangeResourceRecordSets`

[UpdatePublicDnsNamespace](../api/API_UpdatePublicDnsNamespace.md "../api/API_UpdatePublicDnsNamespace.md")

Required permissions (API action):

- `servicediscovery:UpdatePublicDnsNamespace`
- `route53:ChangeResourceRecordSets`

[UpdateService](../api/API_UpdateService.md "../api/API_UpdateService.md")

Required permissions (API action):

- `servicediscovery:UpdateService`
- `route53:GetHealthCheck`
- `route53:CreateHealthCheck`
- `route53:DeleteHealthCheck`
- `route53:UpdateHealthCheck`

[UpdateServiceAttributes](../api/API_UpdateServiceAttributes.md "../api/API_UpdateServiceAttributes.md")

Required Permissions (API Action):
`servicediscovery:UpdateServiceAttributes`
