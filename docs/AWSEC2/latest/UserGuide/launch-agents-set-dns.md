# Configure DNS Suffix for EC2 Windows launch agents

With Amazon EC2 launch agents, you can configure a list of DNS suffixes that Windows
instances use for domain name resolution. The launch agents override the standard
Windows settings in the
`System\CurrentControlSet\Services\Tcpip\Parameters\SearchList`
registry key by adding the following values to the DNS suffix search list:

- The domain of the instance
- The suffixes that result from devolution of the instance domain
- NV domain
- The domains specified by each network interface cards
  All launch agents support DNS suffix configuration. For more information, see your
  specific launch agent version:

- For information about the `setDnsSuffix` task and how to configure
  DNS suffixes in EC2Launch v2, see [setDnsSuffix](ec2launch-v2-task-definitions.md#ec2launch-v2-setdnssuffix "ec2launch-v2-task-definitions.md#ec2launch-v2-setdnssuffix") .
- For information about DNS suffix list setup and how to enable or disable
  devolution for EC2Launch v1, see [Configure the EC2Launch v1 agent on your Windows
  instance](ec2launch-config.md "ec2launch-config.md").
- For information about DNS suffix list setup and how to enable or disable
  devolution for EC2Config, see [EC2Config settings files](ec2config-service.md#UsingConfigXML_WinAMI "ec2config-service.md#UsingConfigXML_WinAMI").

###### Domain name devolution

Domain name devolution is an Active Directory behavior that allows computers in a
child domain to access resources in the parent domain without using a fully qualified
domain name. By default, domain name devolution continues until there are only two
nodes left in the domain name progression.

Launch agents perform devolution on the domain name if the instance is connected to a
domain, and add the results to the DNS suffix search list that's maintained in the
**`System\CurrentControlSet\Services\Tcpip\Parameters\SearchList`**
registry key. The agents use the settings from the following registry keys, to determine
the devolution behavior.

- **`System\CurrentControlSet\Services\Tcpip\Parameters\UseDomainNameDevolution`**
  - When not set, disables devolution
  - When set to `1`, enables devolution (default)
  - When set to `0`, disables devolution

- **`System\CurrentControlSet\Services\Dnscache\Parameters\DomainNameDevolutionLevel`**

      + When not set, use level of `2` (default)
      + When set to `3` or greater, use value to set level

  When you disable devolution or change your devolution settings to a higher level, the
  `System\CurrentControlSet\Services\Tcpip\Parameters\SearchList`
  registry key stil contains the suffixes that were added previously. They are not
  automatically removed. You can manually update the list, or you can clear the list
  and let your agent run through the process to set up the new list.

###### Note

To clear the DNS suffix list from the registry, you can run the following command.

```
`PS C:\>` `Invoke-CimMethod -ClassName Win32_NetworkAdapterConfiguration -MethodName "SetDNSSuffixSearchOrder" -Arguments @{ DNSDomainSuffixSearchOrder = $null } | Out-Null`
```

###### Devolution examples

The following examples show domain name progression through the devolution process.

`corp.example.com`

- Progresses to `example.com`

`locale.region.corp.example.com`

1. Progresses to `region.corp.example.com`
2. Progresses to `corp.example.com`
3. Progresses to `example.com`

`locale.region.corp.example.com` with a setting of
`DomainNameDevolutionLevel=3`

1. Progresses to `region.corp.example.com`
2. Progresses to `corp.example.com`. The progression
   stops here, due to the level setting.
