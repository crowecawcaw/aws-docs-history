# Discovery tool

The AWS Transform discovery tool enables you to automatically discover server inventory in your organization in preparation for migration. To use the discovery tool, you configure it, let it run, and then review the results in the Discovered Inventory pane.

After you configure vCenter access the discovery tool begins collecting information. The
length of time that the discovery tool needs to run to completely analyze your network
depends on the size of your VMware environment. For a directional migration business case you can use the VMware MPA file that the tool generates after the server collection has completed.

## Discovery tool workflow

The workflow for the discovery tool consists of two types of activities:

- Configuration activities
- Data review and use

These steps describe the workflow to installing and using the discovery tool and making use of the collected data:

1. Installation of the discovery tool on vCenter
2. Set up vCenter access

Data discovery begins after this step 3. Set up OS access and then review the collection status of VMware servers, databases, network connection.

    1. Adjust OS credentials as needed.

4. To generate a migration business case, upload the ZIP file to [Migration assessment](transform-app-assessments.md "transform-app-assessments.md") or unzip it and upload _vmware_data_mpa.csv_ from the _mpa_exports_ directory.
