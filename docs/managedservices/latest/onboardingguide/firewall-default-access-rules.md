# Default Access Firewall Rules

These are the default firewall rules required to access your instances.

###### Note

For information on firewall rules and ports required for establishing an AD one-way trust, see the AMS Security Guide by
going to the AWS Artifact console -> Reports tab and search for AWS Managed Services.

## Linux Stack Instance Ports

These rules are required for your authentication into AMS Linux stacks.

Linux Instance Ports Rules FROM: Linux Stack Instance TO: CORP Domain
Controller| Port | Protocol | Service | Direction |
| --- | --- | --- | --- |
| 389 | TCP | LDAP | Ingress |
| 389 | UDP | LDAP | Ingress |
| 88 | TCP | Kerberos | Ingress |
| 88 | UDP | Kerberos | Ingress |

## Windows Stack Instance Ports

These rules are required for your authentication into AMS Windows stacks.

| FROM: Windows Stack Instance TO: CORP Domain Controller | Port | Protocol                                                                                                                                                                                    | Service                                                                                            | Direction          |
| ------------------------------------------------------- | ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ------------------ |
| 88                                                      | TCP  | UDP                                                                                                                                                                                         | Kerberos                                                                                           | Ingress and Egress |
| 135                                                     | TCP  | UDP                                                                                                                                                                                         | DCE/RPC Locator service                                                                            | Ingress and Egress |
| 389                                                     | TCP  | UDP                                                                                                                                                                                         | LDAP                                                                                               | Ingress and Egress |
| 3268                                                    | TCP  | UDP                                                                                                                                                                                         | msft-gc, Microsoft Global Catalog (LDAP service which contains data from Active Directory forests) | Ingress and Egress |
| 445                                                     | TCP  | Microsoft-DS Active Directory, Windows shares                                                                                                                                               | Ingress and Egress                                                                                 |
| 49152<br>• 65535                                        | TCP  | Dynamic or private ports that cannot be registered with IANA. This range is used for private, or customized services or temporary purposes and for automatic allocation of ephemeral ports. | Ingress and Egress                                                                                 |
