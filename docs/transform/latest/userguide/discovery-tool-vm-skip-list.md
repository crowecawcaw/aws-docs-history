

# Excluding VMs from collection
<a name="discovery-tool-vm-skip-list"></a>

You can exclude specific virtual machines from VMware and Hyper-V inventory by editing a skip list file on the discovery tool appliance. VMs whose names match a pattern in the skip list are excluded from VMware and Hyper-V inventory and do not appear in the discovered inventory. This is useful for excluding infrastructure or management VMs that are not part of your migration scope.

**Note**  
The skip list applies only to VMware and Hyper-V auto-discovery. If you import the same server through a CSV file, it is collected regardless of the skip list.

**Important**  
Configure the skip list before you add your VMware and Hyper-V sources. VMs collected before a pattern is added remain in the database and appear in exports that cover the dates before the pattern was added. You can limit the export date range to exclude earlier rounds, but it is simpler to set up the skip list first.

**Skip list file locations**

The following table lists the skip list file path for each supported virtualization source. The paths below are for the standard OVA and VHD appliance. On a Linux installer deployment, the path depends on which user ran the installer — run `systemctl show discovery-tool -p Environment` and look for `DT_DATA_DIR` to find the correct path.


| Source | File path | 
| --- | --- | 
| VMware | /home/discovery/.local/share/DiscoveryTool/vm-skip-list.txt | 
| Hyper-V | /home/discovery/.local/share/DiscoveryTool/hyperv-vm-skip-list.txt | 

The skip list file is created automatically from built-in defaults the first time the discovery tool starts. It is never overwritten by updates, so your customizations are preserved across upgrades.

**VMware default skip patterns**

The VMware skip list is seeded with the following built-in patterns that exclude common VMware infrastructure VMs:

```
# VMC-A Infrastructure VMs
*Interconnect-IX*
*Interconnect-NE*
*Interconnect-SDR*
*Interconnect-WO*
hcx_cloud_manager
NSX-Edge-*
NSX-Manager-*
srm
vr
vcenter

# vSphere Cluster Service VMs
vCLS-*
```

You can add your own patterns below these defaults. Do not remove them unless you intentionally want to collect these infrastructure VMs.

**File format**
+ One pattern per line. Lines starting with `#` are comments and are ignored. Blank lines are ignored.
+ `*` matches any sequence of characters. `?` matches exactly one character.
+ Patterns are anchored to the full VM name. For example, `vCLS-*` matches `vCLS-001` but does not match `my-vCLS-001`. To match anywhere in the name, use `*vCLS-*`.
+ Matching is case-sensitive by default. The skip list file ships with a `# case-sensitive: true` directive on its first line. Because the first matching directive in the file wins, edit this existing line and change `true` to `false` to enable case-insensitive matching — adding a second directive elsewhere in the file has no effect.

Example skip list file (with case-sensitive matching enabled):

```
# case-sensitive: true
# Exclude VMware infrastructure VMs
vCLS-*
# Exclude management VMs
mgmt-*
vCenter-*
```

**When changes take effect**

The skip list file is read at the start of each collection cycle. Changes take effect on the next collection cycle without requiring a restart. Previously collected data for VMs that you add to the skip list is not removed retroactively.

**Warning**  
A pattern of `*` alone matches every VM name and disables collection for the entire VMware or Hyper-V source.

**Multi-host behavior (Hyper-V)**

For Hyper-V, a single skip list file applies to all configured Hyper-V hosts. VM names are per host and might not be unique across hosts. A pattern such as `mgmt-*` excludes matching VMs on all configured hosts.