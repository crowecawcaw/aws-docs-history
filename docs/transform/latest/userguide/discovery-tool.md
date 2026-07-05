# Discovery tool

The AWS Transform discovery tool helps you automatically discover server inventory in your organization to prepare for migration. The tool supports VMware vCenter, Microsoft Hyper-V, and imported servers. To use the discovery tool, you configure one or more discovery sources, let the tool run, and then review the results in the **Discovered inventory** pane.

After you configure a discovery source, the discovery tool begins collecting information. The
time that the discovery tool needs to completely analyze your network
depends on the size of your environment. For a directional migration business case, you can use the Migration Portfolio Assessment (MPA) files that the tool generates after server collection completes.

## Discovery tool workflow

The discovery tool workflow consists of two types of activities:

- Configuration activities
- Data review and use

The following steps describe how to install and use the discovery tool and work with the collected data:

1. Install the discovery tool.
2. Configure discovery sources. You can configure one or more of the following: VMware vCenter, Microsoft Hyper-V hosts, or servers through a CSV file import. Data discovery begins after you configure any source.
3. Set up OS access and then review the collection status of servers, databases, and network connections.

   1. Adjust OS credentials as needed.

4. (Optional) Configure Oracle credentials to enable direct SQL collection, or use OS-level fallback detection through SSH or WinRM.
5. To generate a migration business case, upload the .zip file to [Migration assessment](transform-app-assessments.md "transform-app-assessments.md"), or unzip it and upload MPA files from the _mpa\_exports_ directory. The export includes data from all configured sources and contains MPA files for VMware, Hyper-V, and imported servers.

The discovery tool supports the following discovery paths:

- **VMware vCenter auto-discovery** – Automatically discover servers managed by VMware vCenter.
- **Hyper-V auto-discovery** – Automatically discover servers managed by Microsoft Hyper-V hosts.
- **Server import** – Manually import server inventory through a CSV file.
