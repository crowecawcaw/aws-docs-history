

# Sync plugins to Deadline Cloud workers
<a name="plugin-sync"></a>

Artists rely on plugins to extend the functionality of their digital content creation (DCC) applications. Plugins add capabilities such as custom renderers, file format support, and pipeline tools that are essential to production workflows. Delivering these plugins to cloud workers can be complex, especially when managing multiple versions across different applications.

Plugin sync provides a simplified way to deliver plugins to AWS Deadline Cloud (Deadline Cloud) workers. It works like copying plugins to a shared filesystem folder that all workstations can access—except the shared folder is an Amazon Simple Storage Service (Amazon S3) bucket. You upload your plugin files to a prescribed path in Amazon S3, and Deadline Cloud handles the rest.

## How plugin sync works
<a name="plugin-sync-how-it-works"></a>

When a job session starts, Deadline Cloud syncs plugin files from your queue's job attachments Amazon S3 bucket to the worker's session directory. The conda package for the DCC application then configures the application to load plugins from that directory. This process is automatic—you only need to place your plugin files in the correct Amazon S3 location.

## Upload plugins to Amazon S3
<a name="plugin-sync-upload"></a>

To deliver plugins to your workers, upload the plugin files to the job attachments Amazon S3 bucket associated with your queue. Use the following folder structure in the bucket:

```
s3://{{<job-attachments-bucket>}}/{{<root-prefix>}}/plugins/{{<os>}}/{{<dcc-name>}}/{{<dcc-version>}}/
```

**Important**  
The Amazon S3 path is case-sensitive. Use lowercase for all folder names in the path.

Where:
+ `{{<job-attachments-bucket>}}` – The job attachments Amazon S3 bucket associated with your queue (visible in the queue details page).
+ `{{<root-prefix>}}` – The job attachment root prefix for your queue (visible in the queue details page).
+ `{{<os>}}` – The operating system: `linux` or `windows`.
+ `{{<dcc-name>}}` – The DCC application name in lowercase. See the [supported DCC applications](#plugin-sync-supported-dccs) table for the exact folder name to use.
+ `{{<dcc-version>}}` – The DCC application version (for example, `2025` for Maya, `5.0` for Blender).

**Note**  
Use the major version number in the path. Patch versions such as Maya 2025.3 use `2025`.

For example, to deliver a Maya 2025 plugin on Linux:

```
s3://{{<job-attachments-bucket>}}/{{<root-prefix>}}/plugins/linux/maya/2025/
```

**To upload plugins using the Amazon S3 console**

1. Open the Deadline Cloud console and navigate to your queue details page.

1. Choose the job attachments bucket link to open the bucket in the Amazon S3 console.

1. Navigate to the root prefix folder for your queue.

1. Create the folder path `plugins/{{<os>}}/{{<dcc-name>}}/{{<dcc-version>}}` (for example, `plugins/linux/maya/2025`).

1. Upload your plugin files into the version folder.

## Supported DCC applications
<a name="plugin-sync-supported-dccs"></a>

The following table lists DCC applications that support plugin sync, the exact Amazon S3 folder name to use, whether a conda recipe sample is available on the GitHub website, and whether the service-managed fleet conda channel supports plugin sync for that application.


| DCC application | S3 folder name | Supported versions | [Conda recipe sample](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes) | Service-managed fleet | Forum | 
| --- | --- | --- | --- | --- | --- | 
| Blender | blender | 5.0, 5.1 | ✓ Yes | ✓ Yes | [Plugins](https://github.com/aws-deadline/deadline-cloud-for-blender/discussions/categories/plugins) | 
| Autodesk Maya | maya | 2024, 2025, 2026 | ✓ Yes | ✓ Yes | [Plugins](https://github.com/aws-deadline/deadline-cloud-for-maya/discussions/categories/plugins) | 
| Foundry Nuke | nuke | 15.0, 16.0, 17.0 | ✓ Yes | ✓ Yes | [Plugins](https://github.com/aws-deadline/deadline-cloud-for-nuke/discussions/categories/plugins) | 
| SideFX Houdini | houdini | 19.5, 20.0, 20.5, 21.0 | ✓ Yes | ✓ Yes | [Plugins](https://github.com/aws-deadline/deadline-cloud-for-houdini/discussions/categories/plugins) | 
| Maxon Cinema 4D | cinema4d | 2024, 2025, 2026 | ✓ Yes | ✓ Yes | Not applicable | 
| Adobe After Effects | aftereffects | 24, 25, 26 | ✓ Yes | ✓ Yes | Not applicable | 

To find or discuss supported plugins, visit our GitHub forum for each DCC integration.

**Note**  
You can also use our [conda recipe samples](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes) on the GitHub website for plugin sync with self-hosted channels. To build and host your own channel, see [Create a conda channel using S3](configure-jobs-s3-channel.md).