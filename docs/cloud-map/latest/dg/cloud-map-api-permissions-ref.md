# AWS Cloud Map API permissions reference

When you set up access control and write
 a permissions policy that you can attach to an IAM identity (identity-based policies), you
 can use the following list as a reference. The list includes each AWS Cloud Map API action and
 the actions that you must grant permissions access to. You specify the actions in the
 `Action` field for the policy. For details about the resource value you must
 specify in the `Resource` field or the IAM policy, see [Actions, resources, and condition keys for AWS Cloud Map](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscloudmap.html "https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscloudmap.html") in the *Service
 Authorization Reference*. 

You can use AWS Cloud Map–specific condition keys in your IAM policies for some
 operations. For more information, see [Condition keys for AWS Cloud Map](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscloudmap.html#awscloudmap-policy-keys "https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscloudmap.html#awscloudmap-policy-keys") in the *Service Authorization
 Reference*.

To specify an action, use the `servicediscovery` prefix followed by the API
 action name, for example, `servicediscovery:CreatePublicDnsNamespace` and
 `route53:CreateHostedZone`.


## Required permissions for AWS Cloud Map
 actions




[CreateHttpNamespace](https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateHttpNamespace.html "https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateHttpNamespace.html")

Required permissions (API action):



* `servicediscovery:CreateHttpNamespace`


[CreatePrivateDnsNamespace](https://docs.aws.amazon.com/cloud-map/latest/api/API_CreatePrivateDnsNamespace.html "https://docs.aws.amazon.com/cloud-map/latest/api/API_CreatePrivateDnsNamespace.html")

Required permissions (API action):



* `servicediscovery:CreatePrivateDnsNamespace`
* `route53:CreateHostedZone`
* `route53:GetHostedZone`
* `route53:ListHostedZonesByName`
* `ec2:DescribeVpcs`
* `ec2:DescribeRegions`


[CreatePublicDnsNamespace](https://docs.aws.amazon.com/cloud-map/latest/api/API_CreatePublicDnsNamespace.html "https://docs.aws.amazon.com/cloud-map/latest/api/API_CreatePublicDnsNamespace.html")

Required permissions (API action):



* `servicediscovery:CreatePublicDnsNamespace`
* `route53:CreateHostedZone`
* `route53:GetHostedZone`
* `route53:ListHostedZonesByName`


[CreateService](https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateService.html "https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateService.html")

Required Permissions (API Action):
 `servicediscovery:CreateService`



[DeleteNamespace](https://docs.aws.amazon.com/cloud-map/latest/api/API_DeleteNamespace.html "https://docs.aws.amazon.com/cloud-map/latest/api/API_DeleteNamespace.html")

Required permissions (API action):



* `servicediscovery:DeleteNamespace`


[DeleteService](https://docs.aws.amazon.com/cloud-map/latest/api/API_DeleteService.html "https://docs.aws.amazon.com/cloud-map/latest/api/API_DeleteService.html")

Required Permissions (API Action):
 `servicediscovery:DeleteService`



[DeleteServiceAttributes](https://docs.aws.amazon.com/cloud-map/latest/api/API_DeleteServiceAttributes.html "https://docs.aws.amazon.com/cloud-map/latest/api/API_DeleteServiceAttributes.html")

Required Permissions (API Action):
 `servicediscovery:DeleteServiceAttributes`



[DeregisterInstance](https://docs.aws.amazon.com/cloud-map/latest/api/API_DeregisterInstance.html "https://docs.aws.amazon.com/cloud-map/latest/api/API_DeregisterInstance.html")

Required permissions (API action):



* `servicediscovery:DeregisterInstance`
* `route53:GetHealthCheck`
* `route53:DeleteHealthCheck`
* `route53:UpdateHealthCheck`


[DiscoverInstances](https://docs.aws.amazon.com/cloud-map/latest/api/API_DiscoverInstances.html "https://docs.aws.amazon.com/cloud-map/latest/api/API_DiscoverInstances.html")

Required Permissions (API Action):
 `servicediscovery:DiscoverInstances`



[GetInstance](https://docs.aws.amazon.com/cloud-map/latest/api/API_GetInstance.html "https://docs.aws.amazon.com/cloud-map/latest/api/API_GetInstance.html")

Required Permissions (API Action):
 `servicediscovery:GetInstance`



[GetInstancesHealthStatus](https://docs.aws.amazon.com/cloud-map/latest/api/API_GetInstancesHealthStatus.html "https://docs.aws.amazon.com/cloud-map/latest/api/API_GetInstancesHealthStatus.html")

Required Permissions (API Action):
 `servicediscovery:GetInstancesHealthStatus`



[GetNamespace](https://docs.aws.amazon.com/cloud-map/latest/api/API_GetNamespace.html "https://docs.aws.amazon.com/cloud-map/latest/api/API_GetNamespace.html")

Required Permissions (API Action):
 `servicediscovery:GetNamespace`



[GetOperation](https://docs.aws.amazon.com/cloud-map/latest/api/API_GetOperation.html "https://docs.aws.amazon.com/cloud-map/latest/api/API_GetOperation.html")

Required Permissions (API Action):
 `servicediscovery:GetOperation`



[GetService](https://docs.aws.amazon.com/cloud-map/latest/api/API_GetService.html "https://docs.aws.amazon.com/cloud-map/latest/api/API_GetService.html")

Required Permissions (API Action): `servicediscovery:GetService`



[GetServiceAttributes](https://docs.aws.amazon.com/cloud-map/latest/api/API_GetServiceAttributes.html "https://docs.aws.amazon.com/cloud-map/latest/api/API_GetServiceAttributes.html")

Required Permissions (API Action): `servicediscovery:GetServiceAttributes`



[ListInstances](https://docs.aws.amazon.com/cloud-map/latest/api/API_ListInstances.html "https://docs.aws.amazon.com/cloud-map/latest/api/API_ListInstances.html")

Required Permissions (API Action):
 `servicediscovery:ListInstances`



[ListNamespaces](https://docs.aws.amazon.com/cloud-map/latest/api/API_ListNamespaces.html "https://docs.aws.amazon.com/cloud-map/latest/api/API_ListNamespaces.html")

Required Permissions (API Action):
 `servicediscovery:ListNamespaces`



[ListOperations](https://docs.aws.amazon.com/cloud-map/latest/api/API_ListOperations.html "https://docs.aws.amazon.com/cloud-map/latest/api/API_ListOperations.html")

Required Permissions (API Action):
 `servicediscovery:ListOperations`



[ListServices](https://docs.aws.amazon.com/cloud-map/latest/api/API_ListServices.html "https://docs.aws.amazon.com/cloud-map/latest/api/API_ListServices.html")

Required Permissions (API Action):
 `servicediscovery:ListServices`



[ListTagsForResource](https://docs.aws.amazon.com/cloud-map/latest/api/API_ListTagsForResource.html "https://docs.aws.amazon.com/cloud-map/latest/api/API_ListTagsForResource.html")

Required Permissions (API Action):
 `servicediscovery:ListTagsForResource`



[RegisterInstance](https://docs.aws.amazon.com/cloud-map/latest/api/API_RegisterInstance.html "https://docs.aws.amazon.com/cloud-map/latest/api/API_RegisterInstance.html")

Required permissions (API action):



* `servicediscovery:RegisterInstance`
* `route53:GetHealthCheck`
* `route53:CreateHealthCheck`
* `route53:UpdateHealthCheck`
* `ec2:DescribeInstances`


[TagResource](https://docs.aws.amazon.com/cloud-map/latest/api/API_TagResource.html "https://docs.aws.amazon.com/cloud-map/latest/api/API_TagResource.html")

Required Permissions (API Action):
 `servicediscovery:TagResource`



[UntagResource](https://docs.aws.amazon.com/cloud-map/latest/api/API_UntagResource.html "https://docs.aws.amazon.com/cloud-map/latest/api/API_UntagResource.html")

Required Permissions (API Action):
 `servicediscovery:UntagResource`



[UpdateHttpNamespace](https://docs.aws.amazon.com/cloud-map/latest/api/API_UpdateHttpNamespace.html "https://docs.aws.amazon.com/cloud-map/latest/api/API_UpdateHttpNamespace.html")

Required Permissions (API Action):
 `servicediscovery:UpdateHttpNamespace`



[UpdateInstanceCustomHealthStatus](https://docs.aws.amazon.com/cloud-map/latest/api/API_UpdateInstanceCustomHealthStatus.html "https://docs.aws.amazon.com/cloud-map/latest/api/API_UpdateInstanceCustomHealthStatus.html")

Required Permissions (API Action):
 `servicediscovery:UpdateInstanceCustomHealthStatus`



[UpdatePrivateDnsNamespace](https://docs.aws.amazon.com/cloud-map/latest/api/API_UpdatePrivateDnsNamespace.html "https://docs.aws.amazon.com/cloud-map/latest/api/API_UpdatePrivateDnsNamespace.html")

Required permissions (API action):



* `servicediscovery:UpdatePrivateDnsNamespace`
* `route53:ChangeResourceRecordSets`


[UpdatePublicDnsNamespace](https://docs.aws.amazon.com/cloud-map/latest/api/API_UpdatePublicDnsNamespace.html "https://docs.aws.amazon.com/cloud-map/latest/api/API_UpdatePublicDnsNamespace.html")

Required permissions (API action):



* `servicediscovery:UpdatePublicDnsNamespace`
* `route53:ChangeResourceRecordSets`


[UpdateService](https://docs.aws.amazon.com/cloud-map/latest/api/API_UpdateService.html "https://docs.aws.amazon.com/cloud-map/latest/api/API_UpdateService.html")

Required permissions (API action):



* `servicediscovery:UpdateService`
* `route53:GetHealthCheck`
* `route53:CreateHealthCheck`
* `route53:DeleteHealthCheck`
* `route53:UpdateHealthCheck`


[UpdateServiceAttributes](https://docs.aws.amazon.com/cloud-map/latest/api/API_UpdateServiceAttributes.html "https://docs.aws.amazon.com/cloud-map/latest/api/API_UpdateServiceAttributes.html")

Required Permissions (API Action):
 `servicediscovery:UpdateServiceAttributes`
