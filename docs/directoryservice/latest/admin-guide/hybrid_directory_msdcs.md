

# DNS `_msdcs` zone modernization
<a name="hybrid_directory_msdcs"></a>

Modernizing a DNS `_msdcs` zone is a mandatory prerequisite before Hybrid AD directory creation. In modern Active Directory environments, `_msdcs.<ForestRoot>` is created as a separate, forest-wide replicated zone stored in the ForestDnsZones application partition. In legacy environments originally built on Windows NT 4.0 or Windows 2000 (and subsequently upgraded), `_msdcs` was never separated; it exists simply as a standard subdomain (subfolder) directly inside the parent domain zone file.

When a new Domain Controller is promoted with DNS installed, its installation process looks for the dedicated `_msdcs.<ForestRoot>` application partition. Because it does not find a standalone zone, it automatically creates a new, blank `_msdcs` zone locally and claims authority over that namespace. This completely cuts off the new DC from reading the legacy subdomain records in the parent zone, and updates the NS delegation to point to itself.

The result is an architectural conflict. All domain-joined clients are now referred to a DC that has an empty `_msdcs` zone, while the actual DC locator records (`_ldap._tcp.dc._msdcs`, `_kerberos._tcp.dc._msdcs`, Global Catalog records, DC GUID CNAMEs) remain stranded in the old parent zone subdomain where no client can reach them. This breaks Kerberos authentication, LDAP discovery, and site-aware DC location across the entire forest.

## Legacy vs modern `_msdcs` zone design
<a name="hybrid_directory_msdcs_legacy_vs_modern"></a>

Legacy (delegated subdomain)  
Default in Windows Server 2000, 2003, 2008, and 2008 R2. In this design, `_msdcs` exists as a delegated subdomain under the parent zone. NS records in the parent zone point to specific DCs as authoritative for the `_msdcs` namespace.

Modern (standalone zone)  
Default in Windows Server 2012 and later. In this design, `_msdcs.<forest>` exists as its own AD-integrated zone, replicated to all DCs in the forest via the ForestDnsZones application partition. All DCs are authoritative and can read/write records directly.

## How to identify `_msdcs` zone design
<a name="hybrid_directory_msdcs_identify"></a>

You can identify your `_msdcs` zone design by running the following on any Domain Controller:

1. **List all DNS zones and look for `_msdcs`:**

   ```
   Get-DnsServerZone | Where-Object { $_.ZoneName -like "*_msdcs*" }
   ```

   **Modern design (no action needed)** — you will see `_msdcs.<forest-name>` listed as a Primary zone:

   ```
   ZoneName                          ZoneType   IsAutoCreated  IsDsIntegrated  IsReverseLookupZone  IsSigned
   --------                          --------   -------------  --------------  -------------------  --------
   _msdcs.premier.local              Primary    False          True            False                False
   ```

   **Legacy design (conversion required)** — `_msdcs.<forest-name>` will NOT appear in the zone list. Instead, `_msdcs` exists only as a delegated subdomain under your forest zone. You can confirm this by checking for the delegation NS records:

   ```
   Get-DnsServerResourceRecord -ZoneName "<forest-name>" -Name "_msdcs" -RRType NS
   ```

   If this returns NS records, your environment uses the legacy delegated subdomain design.

1. **Additional validation — confirm the zone type:**

   ```
   # This will succeed on modern design
   Get-DnsServerZone -Name "_msdcs.<forest-name>"
   
   # If you get an error like "Zone _msdcs.<forest-name> was not found", you have the legacy design
   ```

## How to modernize DNS `_msdcs` zone
<a name="hybrid_directory_msdcs_modernize"></a>

These steps must be performed before initiating the AWS Managed Microsoft AD Hybrid directory creation. All steps are performed on existing self-managed Domain Controllers with DNS Manager access with Domain Admin and DnsAdmins privileges.

1. **Create the standalone `_msdcs` zone**

   On an existing self-managed Domain Controller:

   ```
   dnscmd localhost /ZoneAdd "_msdcs.<forest-name>" /DsPrimary /dp /forest
   ```

   This creates `_msdcs.<forest-name>` as a dedicated AD-integrated zone with Forest-wide replication scope. All DCs in the forest will receive a copy via the ForestDnsZones partition.

   Wait for AD replication to propagate:

   ```
   repadmin /syncall /AeD
   ```

   Verify the zone exists (run on multiple DCs):

   ```
   Get-DnsServerZone -Name "_msdcs.<forest-name>"
   ```

1. **Remove the old delegation from the parent zone**

   The old `_msdcs` subdomain node and its records still exist in the parent zone. These must be removed so that DNS queries are served exclusively from the new standalone zone.

   ```
   # Remove the _msdcs subtree (NS delegation + all child records) from the parent zone
   dnscmd localhost /NodeDelete <forest-name> _msdcs /tree /f
   ```
**Important**  
Only perform this step after confirming the standalone zone was created successfully in Step 1. If you skip Step 1, deleting the old records will cause an immediate outage.

1. **Force all DCs to re-register SRV records**

   With the old subdomain removed and the new standalone zone in place, all DCs must re-register their locator records into the new zone.

   Run the following on every on-premises Domain Controller:

   ```
   # Flush DNS cache
   ipconfig /flushdns
   
   # Restart Netlogon — this triggers re-registration of all SRV, CNAME, and A records
   net stop netlogon
   net start netlogon
   
   # Force host record registration
   ipconfig /registerdns
   ```

1. **Verify**

   Wait 5–10 minutes for replication, then verify:

   Confirm records populated in the new standalone zone:

   ```
   Get-DnsServerResourceRecord -ZoneName "_msdcs.<forest-name>" -RRType SRV
   ```

   You should see `_ldap._tcp.dc`, `_kerberos._tcp.dc`, `_ldap._tcp.gc`, and site-specific records for all on-premises DCs.

   Confirm DNS resolution works end-to-end:

   ```
   Resolve-DnsName "_ldap._tcp.dc._msdcs.<forest-name>" -Type SRV
   Resolve-DnsName "_kerberos._tcp.dc._msdcs.<forest-name>" -Type SRV
   ```

   All on-premises DCs should appear in the results.

   Confirm the old delegation is gone from the parent zone:

   ```
   Get-DnsServerResourceRecord -ZoneName "<forest-name>" -Name "_msdcs" -RRType NS -ErrorAction SilentlyContinue
   ```

   This should return nothing.

   For more information about modernizing DNS `_msdcs` zones, see [How To Split and Migrate Child Domain DNS Records To a Dedicated DNS Zone](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/how-to-split-and-migrate-child-domain-dns-records-to-a-dedicated-dns-zone/255534) on the Microsoft Core Infrastructure and Security Blog website.

## Troubleshooting
<a name="hybrid_directory_msdcs_troubleshooting"></a>

If the new standalone zone remains empty after Step 3:

Netlogon may not re-register if it believes records already exist. Force a clean re-registration:

```
# Delete the Netlogon DNS registration cache
Remove-Item "HKLM:\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters\DnsAvoidRegisterRecords" -ErrorAction SilentlyContinue

# Restart Netlogon again
net stop netlogon
net start netlogon
```

If records still don't appear, manually create the critical records using the values from the old parent zone (available from backup or from other DCs that cached them):

```
# Example: SRV record for LDAP DC locator
Add-DnsServerResourceRecord -ZoneName "_msdcs.<forest-name>" -Name "_ldap._tcp.dc" -Srv -DomainName "dc1.<forest-name>" -Priority 0 -Weight 100 -Port 389

# Example: SRV record for Kerberos DC locator
Add-DnsServerResourceRecord -ZoneName "_msdcs.<forest-name>" -Name "_kerberos._tcp.dc" -Srv -DomainName "dc1.<forest-name>" -Priority 0 -Weight 100 -Port 88
```

If applications are still failing after conversion:

Flush DNS caches on affected application servers and client machines:

```
ipconfig /flushdns
```

Negative DNS cache entries (from the outage period) may persist for up to 900 seconds (15 minutes) before expiring.