

# Configuring Active Directory Sites and Services for WorkSpaces Applications
<a name="active-directory-sites-services"></a>

As with all multi-site Active Directory deployments, Windows authentication within WorkSpaces Applications is most reliable when Active Directory Sites and Services includes the WorkSpaces Applications fleet subnets. Assign those subnets to a site that includes a domain controller in the same AWS Region as WorkSpaces Applications to prevent logon and replication delays.

Because WorkSpaces Applications streaming instances are ephemeral, they are frequently terminated, re-provisioned, and joined to the domain with new computer object credentials. If you configure Sites and Services incorrectly, the Windows domain join mechanism might target one site for the domain join and another site for authentication. In larger Active Directory environments where the sites are not directly linked, syncing the latest domain join information to the randomly selected authentication site can take multiple hours. This delay occurs because site-to-site replication is three hours by default. The delay can create database inconsistencies for the computer account and cause the user's logon to fail.

At a high level, a basic configuration uses two existing domain controllers. Domain controller A is in the site `"us-east-1-site"`, and domain controller B is in the site `"us-east-2-site"`. To configure Sites and Services for this setup, complete the following steps:

1. Create WorkSpaces Applications fleet A in `us-east-1` in the summary subnet `10.0.0.0/24`.

1. Create WorkSpaces Applications fleet B in `us-east-2` in the summary subnet `172.16.0.0/24`.

1. Create a new subnet (`10.0.0.0/24`) in Active Directory Sites and Services and assign it to `"us-east-1-site"`.

1. Create a new subnet (`172.16.0.0/24`) in Active Directory Sites and Services and assign it to `"us-east-2-site"`.

With this configuration, WorkSpaces Applications fleet A targets domain controller A as the primary, with failover to domain controller B. WorkSpaces Applications fleet B targets domain controller B as the primary, with failover to domain controller A.

For more information about Microsoft Active Directory Sites and Services and the domain controller locator process, see the following Microsoft documentation: [Designing the site topology](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/designing-the-site-topology) and [How Domain Controllers Are Located in Windows](https://learn.microsoft.com/en-us/archive/technet-wiki/24457.how-domain-controllers-are-located-in-windows).