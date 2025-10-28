# Limit access to the Instance

Metadata Service

You can consider using local firewall rules to disable access from some or all
processes to the Instance Metadata Service (IMDS).

For [Nitro-based instances](instance-types.md#instance-hypervisor-type "instance-types.md#instance-hypervisor-type"), the IMDS can be reached from your own
network when a network appliance within your VPC, such as a virtual router,
forwards packets to the IMDS address, and the default [source/destination check](../../../vpc/latest/userguide/VPC_NAT_Instance.md#EIP_Disable_SrcDestCheck "../../../vpc/latest/userguide/VPC_NAT_Instance.md#EIP_Disable_SrcDestCheck") on the instance is disabled. To prevent a
source from outside your VPC reaching the IMDS, we recommend that you modify the
configuration of the network appliance to drop packets with the destination IPv4
address of the IMDS `169.254.169.254` and, if you enabled the IPv6
endpoint, the IPv6 address of the IMDS `[fd00:ec2::254]`.

## Limit IMDS access for Linux instances

**Using iptables to limit access**

The following example uses Linux iptables and its `owner`
module to prevent the Apache webserver (based on its default installation
user ID of `apache`) from accessing 169.254.169.254. It uses a
_deny rule_ to reject all instance
metadata requests (whether IMDSv1 or IMDSv2) from any
process running as that user.

```
`$` `sudo iptables --append OUTPUT --proto tcp --destination 169.254.169.254 --match owner --uid-owner apache --jump REJECT`
```

Or, you can consider only allowing access to particular users or groups,
by using _allow rules_. Allow rules might
be easier to manage from a security perspective, because they require you to
make a decision about what software needs access to instance metadata. If
you use _allow rules_, it's less likely you
will accidentally allow software to access the metadata service (that you
did not intend to have access) if you later change the software or
configuration on an instance. You can also combine group usage with allow
rules, so that you can add and remove users from a permitted group without
needing to change the firewall rule.

The following example prevents access to the IMDS by all
processes, except for processes running in the user account
`trustworthy-user`.

```
`$` `sudo iptables --append OUTPUT --proto tcp --destination 169.254.169.254 --match owner ! --uid-owner `trustworthy-user` --jump REJECT`
```

###### Note

- To use local firewall rules, you need to adapt the preceding
  example commands to suit your needs.
- By default, iptables rules are not persistent across system
  reboots. They can be made to be persistent by using OS features,
  not described here.
- The iptables `owner` module only matches group
  membership if the group is the primary group of a given local
  user. Other groups are not matched.

**Using PF or IPFW to limit access**

If you are using FreeBSD or OpenBSD, you can also consider using PF or
IPFW. The following examples limit access to the IMDS to just the
root user.

**PF**

```
`$` `block out inet proto tcp from any to 169.254.169.254`
```

```
`$` `pass out inet proto tcp from any to 169.254.169.254 user root`
```

**IPFW**

```
`$` `allow tcp from any to 169.254.169.254 uid root`
```

```
`$` `deny tcp from any to 169.254.169.254`
```

###### Note

The order of the PF and IPFW commands matter. PF defaults to last
matching rule and IPFW defaults to first matching rule.

## Limit IMDS access for Windows instances

**Using Windows firewall to limit access**

The following PowerShell example uses the built-in Windows firewall to
prevent the Internet Information Server webserver (based on its default
installation user ID of `NT AUTHORITY\IUSR`) from accessing
169.254.169.254. It uses a _deny rule_ to
reject all instance metadata requests (whether IMDSv1 or
IMDSv2) from any process running as that user.

```
`PS C:\>` `$blockPrincipal = New-Object -TypeName System.Security.Principal.NTAccount ("NT AUTHORITY\IUSR")`
`PS C:\>` `$BlockPrincipalSID = $blockPrincipal.Translate([System.Security.Principal.SecurityIdentifier]).Value`
`PS C:\>` `$BlockPrincipalSDDL = "D:(A;;CC;;;$BlockPrincipalSID)"`
`PS C:\>` `New-NetFirewallRule -DisplayName "Block metadata service from IIS" -Action block -Direction out `
-Protocol TCP -RemoteAddress 169.254.169.254 -LocalUser $BlockPrincipalSDDL`
```

Or, you can consider only allowing access to particular users or groups,
by using _allow rules_. Allow rules might
be easier to manage from a security perspective, because they require you to
make a decision about what software needs access to instance metadata. If
you use _allow rules_, it's less likely you
will accidentally allow software to access the metadata service (that you
did not intend to have access) if you later change the software or
configuration on an instance. You can also combine group usage with allow
rules, so that you can add and remove users from a permitted group without
needing to change the firewall rule.

The following example prevents access to instance metadata by all
processes running as an OS group specified in the variable
`blockPrincipal` (in this example, the Windows group
`Everyone`), except for processes specified in
`exceptionPrincipal` (in this example, a group called
`trustworthy-users`). You must specify both deny and allow
principals because Windows Firewall, unlike the `! --uid-owner
 trustworthy-user` rule in Linux iptables, does not provide a
shortcut mechanism to allow only a particular principal (user or group) by
denying all the others.

```
`PS C:\>` `$blockPrincipal = New-Object -TypeName System.Security.Principal.NTAccount ("Everyone")`
`PS C:\>` `$BlockPrincipalSID = $blockPrincipal.Translate([System.Security.Principal.SecurityIdentifier]).Value`
`PS C:\>` `$exceptionPrincipal = New-Object -TypeName System.Security.Principal.NTAccount ("trustworthy-users")`
`PS C:\>` `$ExceptionPrincipalSID = $exceptionPrincipal.Translate([System.Security.Principal.SecurityIdentifier]).Value`
`PS C:\>` `$PrincipalSDDL = "O:LSD:(D;;CC;;;$ExceptionPrincipalSID)(A;;CC;;;$BlockPrincipalSID)"`
`PS C:\>` `New-NetFirewallRule -DisplayName "Block metadata service for $($blockPrincipal.Value), exception: $($exceptionPrincipal.Value)" -Action block -Direction out `
-Protocol TCP -RemoteAddress 169.254.169.254 -LocalUser $PrincipalSDDL`
```

###### Note

To use local firewall rules, you need to adapt the preceding example
commands to suit your needs.

**Using netsh rules to limit access**

You can consider blocking all software using `netsh` rules, but
those are much less flexible.

```
`C:\>` `netsh advfirewall firewall add rule name="Block metadata service altogether" dir=out protocol=TCP remoteip=169.254.169.254 action=block`
```

###### Note

- To use local firewall rules, you need to adapt the preceding
  example commands to suit your needs.
- `netsh` rules must be set from an elevated command
  prompt, and can’t be set to deny or allow particular
  principals.
