# Understanding EC2 instance hostnames and domains

A EC2 instance address is made up of different components. The following is an example of an EC2 instance address that uses the private IPv4 address of the instance:

```
   IP address         Domain name
   ↓--------↓ ↓------------------------↓
ip-10-24-34-0.us-west-2.compute.internal
↑-----------↑
  Hostname
↑--------------------------------------↑
    Fully qualified domain name (FQDN)
```

Where:

- **IP address**: The primary IPv4 address of the primary network interface associated with an instance.
- **Hostname**: The local name of a specific EC2 instance (used by the operating system and for local network identification)
- **Domain name**: The part of the FQDN that AWS provides
- **Fully qualified domain name (FQDN)**: The complete address that includes both the hostname and the domain name. This is the full, globally unique identifier used to reach your instance across networks.
  Depending on the hostname type you choose for the instance or primary network interface attached to the instance, the hostname and domain name formats will be different from the example above. This section explains the hostname type options.
