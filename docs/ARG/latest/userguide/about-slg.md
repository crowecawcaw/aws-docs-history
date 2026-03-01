# Service configurations for resource groups

Resource groups enable you to manage collections of your AWS resources as a unit. Some
AWS services support this by performing requested operations on all members of the group.
Such services can store the settings to be applied to group members as a
_configuration_ in the form of a [JSON](https://www.json.org/ "https://www.json.org/") data structure that is attached to the group.

This topic describes the available configuration settings for supported AWS
services.

###### Topics

- [How to access the service configuration attached to a resource group](#about-slg-how-to-access "#about-slg-how-to-access")
- [JSON syntax of a service configuration](#about-slg-config-syntax "#about-slg-config-syntax")
- [Supported configuration types and parameters](about-slg-types.md "about-slg-types.md")

## How to access the service configuration attached to a resource group

Services that support service-linked groups typically set the configuration for you
when you use the tools provided by that service, such as that service's management
console or its AWS CLI and AWS SDK operations. Some services fully manage their
service-linked groups and you can't modify them in any way except as allowed by the
console or commands provided by the owning AWS service. However, in some cases, you
can interact with the service configuration by using the following API operations in the
AWS SDKs or their AWS CLI equivalents:

- You can attach your own configuration to a group when you create the group by
  using the [CreateGroup](../APIReference/API_CreateGroup.md "../APIReference/API_CreateGroup.md") operation.
- You can modify the current configuration attached to a group by using the
  [PutGroupConfiguration](../APIReference/API_PutGroupConfiguration.md "../APIReference/API_PutGroupConfiguration.md") operation.
- You can view the current configuration of a resource group by calling the
  [GetGroupConfiguration](../APIReference/API_GetGroupConfiguration.md "../APIReference/API_GetGroupConfiguration.md") operation.

## JSON syntax of a service configuration

A resource group can contain a _configuration_ that defines
service-specific settings that apply to the resources that are members of that
group.

A configuration is expressed as a [JSON](https://www.json.org/ "https://www.json.org/")
object. At the top-most level, a configuration is an array of [group
configuration items](../APIReference/API_GroupConfigurationItem.md "../APIReference/API_GroupConfigurationItem.md"). Each group configuration item contains two elements: a
`Type` for the configuration and a set of `Parameters` defined
by that type. Each parameter contains a `Name` and an array of one or more
`Values`. The following example with
`placeholders` shows the basic syntax for a configuration
for a single sample resource type. This example shows a type with two parameters, and
each parameter with two values. The actual valid types, parameters, and values are
discussed in the next section.

```
[
  {
    "Type": "`configuration-type`",
    "Parameters": [
      {
        "Name": "`parameter1-name`",
        "Values": [
          "value1",
          "value2"
        ]
      },
      {
        "Name": "`parameter2-name`",
        "Values": [
          "value3",
          "value4"
        ]
      }
    ]
  }
]
```
