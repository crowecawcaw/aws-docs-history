

# Deliver custom plugins with plugin sync
<a name="plugin-sync"></a>

Plugin sync delivers custom plugins and add-ons without requiring you to build a conda package. Upload the plugin files to a prescribed prefix in the queue's job attachments bucket. When a job uses a supported application package, the package copies the files to the worker and configures the application to load them.

Use plugin sync when the plugin can run after its files are copied to an application search path. If the plugin requires dependency resolution, installation commands, or a system change, return to [Use custom plugins with Deadline Cloud](custom-plugins.md) to choose another delivery method.

## How plugin sync works
<a name="plugin-sync-how-it-works"></a>

The supported digital content creation (DCC) conda packages use activation and deactivation scripts for plugin sync. The following events occur for each worker session:

1. The queue environment creates a conda environment containing the DCC and adaptor packages selected by the job.

1. When conda activates the environment, the DCC package's plugin sync script reads the job attachments bucket and root prefix from the session environment.

1. The script downloads files from the operating system, DCC, and DCC version prefix in Amazon S3. It then sets application-specific environment variables or copies the files to an application plugin directory.

1. When the session ends, the deactivation script removes the downloaded plugin files and configuration. The next session starts from the packaged DCC environment.

The script writes messages that begin with `Plugin Sync:` to the session log. You can use these messages to confirm the source prefix, destination, and files processed.

## Prerequisites
<a name="plugin-sync-prerequisites"></a>

Before you upload a plugin, confirm the following requirements:
+ The application, version, and worker operating system appear in the [supported applications table](#plugin-sync-supported-dccs).
+ The plugin files are compatible with the worker operating system, application version, and processor architecture.
+ You know the plugin vendor's required directory structure. Plugin sync preserves the directory structure that you upload.
+ If the plugin requires a license, the worker can reach the license server.

## Upload plugin files to Amazon S3
<a name="plugin-sync-upload"></a>

Upload the plugin files to the job attachments Amazon S3 bucket associated with your queue. Use the following prefix:

```
s3://{{<job-attachments-bucket>}}/{{<root-prefix>}}/plugins/{{<os>}}/{{<dcc-name>}}/{{<dcc-version>}}/
```

**Important**  
The Amazon S3 prefix is case-sensitive. Use lowercase for the operating system and DCC folder names.

Replace the variables as follows:

`{{<job-attachments-bucket>}}`  
The job attachments bucket associated with your queue. The queue details page displays the bucket.

`{{<root-prefix>}}`  
The job attachments root prefix for your queue. The queue details page displays the prefix.

`{{<os>}}`  
The worker operating system, either `linux` or `windows`.

`{{<dcc-name>}}`  
The exact folder name from the [supported applications table](#plugin-sync-supported-dccs).

`{{<dcc-version>}}`  
The version folder from the supported applications table. For example, Maya 2025.3 uses `2025`, and Blender 5.1 uses `5.1`.

For example, the prefix for a Maya 2025 plugin on Linux is:

```
s3://{{<job-attachments-bucket>}}/{{<root-prefix>}}/plugins/linux/maya/2025/
```

**To upload plugin files using the Amazon S3 console**

1. Open the Deadline Cloud console, and then open the queue details page.

1. Choose the job attachments bucket link to open the bucket in the Amazon S3 console.

1. Open the root prefix for the queue.

1. Create the prefix `plugins/{{<os>}}/{{<dcc-name>}}/{{<dcc-version>}}/`. For example, use `plugins/linux/maya/2025/` for Maya 2025.

1. Upload the plugin files and directories to the version prefix. Preserve the directory structure that the plugin vendor requires.

## Verify plugin delivery
<a name="plugin-sync-verify"></a>

**To verify that plugin sync delivered the files**

1. Submit a job that selects the supported DCC package and version.

1. In the AWS Deadline Cloud monitor (Deadline Cloud monitor), open the session log for a task.

1. Search the session log for `Plugin Sync:`. Confirm that the log shows the expected Amazon S3 prefix and destination.

1. Confirm in the task log that the application loaded the plugin. The message depends on the application and plugin.

## Applications that support plugin sync
<a name="plugin-sync-supported-dccs"></a>

The following table lists applications and versions that contain plugin sync scripts. It also identifies whether a conda recipe sample is available on the GitHub website and whether the `deadline-cloud` channel for service-managed fleets includes the scripts.


| DCC application | S3 folder name | Version folders | Worker operating system | [Conda recipe sample](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes) | Service-managed fleet package | 
| --- | --- | --- | --- | --- | --- | 
| Blender | blender | 5.0, 5.1 | Linux | Yes | Yes | 
| Autodesk Maya | maya | 2024, 2025, 2026, 2027 | Linux | Yes | Yes | 
| Foundry Nuke | nuke | 15.0, 16.0, 17.0 | Linux | Yes | Yes | 
| SideFX Houdini | houdini | 19.5, 20.0, 20.5, 21.0, 22.0 | Linux | Yes | Yes | 
| Maxon Cinema 4D | cinema4d | Linux: 2024.5.1, 2025.3.1, and 2026.3.4; Windows: 2025.3.3 and 2026.3.4 | 2024: Linux; 2025 and 2026: Linux and Windows | Yes | Yes | 
| Adobe After Effects | aftereffects | 25.6 or 25.6.4; 26.0 or 26.0.0 | Windows | Yes | Yes | 

If your application or version does not appear in the table, see [Package a plugin](conda-package.md#conda-package-plugins) or [Configure jobs using queue environments](configure-jobs.md), or use a customer-managed fleet. The [conda recipe samples](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes) on the GitHub website include plugin sync scripts that you can use with a self-hosted channel.