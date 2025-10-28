# Environment architecture considerations

Consider the following criteria in deciding how to configure your environment and architecture.

- Will your virtual data center connect back to your corporate network?
  - Do you have an existing AWS DirectConnect service or do you require a new DirectConnect service?
  - Do you have an existing VPN connection or do you require a new VPN service?

- What is the available CIDR block range of internal addresses that you could allocate? (/16 recommended, must not overlap corporate network ranges)
- Will your virtual data center require internet access?
- Which Region(s) do you intend to use? (Sydney/N. Virginia/Dublin)
- Will you require a Shared Services subnet to host applications that have connectivity to all other subnets?
- What are your organizational divisions that you would like to be hosted as separate subnets. For each:
  - What connectivity to other subnets do you need?
  - Does the subnet require Internet access?
  - Are there any application deployment restrictions to that subnet?
  - Are there any particular network requirements for that subnet?

- Would you like separate development and/or test environments? (Will include shared services duplicate for anytime access)
- What are your snapshot backup requirements?
- Do you have an existing maintenance process or patch window(s) that you would like to keep?
- What are your domain registration requirements?
- Do you have any single sign-on requirements? (e.g., AD, LDAP)
- What are your overall expected operating system and anticipated capacity requirements?
