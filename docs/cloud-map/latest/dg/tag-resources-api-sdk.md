# Updating tags for AWS Cloud Map resources

Use the following AWS CLI commands or AWS Cloud Map API operations to add, update, list, and delete the tags for your
resources.

| Tagging support for AWS Cloud Map resources | Task                                                                                         | API action                                                                                                                                                                    | AWS CLI                                                                                                                                                 | AWS Tools for Windows PowerShell |
| ------------------------------------------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| Add or overwrite one or more tags.          | [TagResource](../api/API_TagResource.md "../api/API_TagResource.md")                         | [tag-resource](../../../cli/latest/reference/servicediscovery/tag-resource.md "../../../cli/latest/reference/servicediscovery/tag-resource.md")                               | [Add-SDResourceTag](../../../powershell/v4/reference/items/Add-SDResourceTag.md "../../../powershell/v4/reference/items/Add-SDResourceTag.md")          |
| Delete one or more tags.                    | [UntagResource](../api/API_UntagResource.md "../api/API_UntagResource.md")                   | [untag-resource](../../../cli/latest/reference/servicediscovery/untag-resource.md "../../../cli/latest/reference/servicediscovery/untag-resource.md")                         | [Remove-SDResourceTag](../../../powershell/v4/reference/items/Remove-SDResourceTag.md "../../../powershell/v4/reference/items/Remove-SDResourceTag.md") |
| List tags for a resource                    | [ListTagsForResource](../api/API_ListTagsForResource.md "../api/API_ListTagsForResource.md") | [list-tags-for-resource](../../../cli/latest/reference/servicediscovery/list-tags-for-resource.md "../../../cli/latest/reference/servicediscovery/list-tags-for-resource.md") | [Get-SDResourceTag](../../../powershell/v4/reference/items/Get-SDResourceTag.md "../../../powershell/v4/reference/items/Get-SDResourceTag.md")          |

The following examples show how to tag or untag resources using the AWS CLI.

###### Example 1: Tag an existing resource

The following command tags an existing resource.

```
`aws servicediscovery tag-resource --resource-arn `resource_ARN` --tags `team`=`devs``
```

###### Example 2: Untag an existing resource

The following command deletes a tag from an existing resource.

```
`aws servicediscovery untag-resource --resource-arn `resource_ARN` --tag-keys `tag_key``
```

###### Example 3: List tags for a resource

The following command lists the tags associated with an existing resource.

```
`aws servicediscovery list-tags-for-resource --resource-arn `resource_ARN``
```

Some resource-creating actions enable you to specify tags when you create the resource. The following actions
support tagging on creation.

| Task                                    | API action                                                                                                     | AWS CLI                                                                                                                                                                                         | AWS Tools for Windows PowerShell                                                                                                                                       |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Create an HTTP namespace                | [CreateHttpNamespace](../api/API_CreateHttpNamespace.md "../api/API_CreateHttpNamespace.md")                   | [create-http-namespace](../../../cli/latest/reference/servicediscovery/create-http-namespace.md "../../../cli/latest/reference/servicediscovery/create-http-namespace.md")                      | [New-SDHttpNamespace](../../../powershell/v4/reference/items/New-SDHttpNamespace.md "../../../powershell/v4/reference/items/New-SDHttpNamespace.md")                   |
| Create a private namespace based on DNS | [CreatePrivateDnsNamespace](../api/API_CreatePrivateDnsNamespace.md "../api/API_CreatePrivateDnsNamespace.md") | [create-private-dns-namespace](../../../cli/latest/reference/servicediscovery/create-private-dns-namespace.md "../../../cli/latest/reference/servicediscovery/create-private-dns-namespace.md") | [New-SDPrivateDnsNamespace](../../../powershell/v4/reference/items/New-SDPrivateDnsNamespace.md "../../../powershell/v4/reference/items/New-SDPrivateDnsNamespace.md") |
| Create a public namespace based on DNS  | [CreatePublicDnsNamespace](../api/API_CreatePublicDnsNamespace.md "../api/API_CreatePublicDnsNamespace.md")    | [create-public-dns-namespace](../../../cli/latest/reference/servicediscovery/create-public-dns-namespace.md "../../../cli/latest/reference/servicediscovery/create-public-dns-namespace.md")    | [New-SDPublicDnsNamespace](../../../powershell/v4/reference/items/New-SDPublicDnsNamespace.md "../../../powershell/v4/reference/items/New-SDPublicDnsNamespace.md")    |
| Create a service                        | [CreateService](../api/API_CreateService.md "../api/API_CreateService.md")                                     | [create-service](../../../cli/latest/reference/servicediscovery/create-service.md "../../../cli/latest/reference/servicediscovery/create-service.md")                                           | [New-SDService](../../../powershell/v4/reference/items/New-SDService.md "../../../powershell/v4/reference/items/New-SDService.md")                                     |
