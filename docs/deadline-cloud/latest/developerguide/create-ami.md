# Create an Amazon Machine Image

To create an Amazon Machine Image (AMI) to use in an Amazon Elastic Compute Cloud (Amazon EC2) customer-managed fleet
(CMF), complete the tasks in this section. You must create an Amazon EC2 instance before
proceeding. For more information, see [Launch your
instance](../../../AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.md "../../../AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.md") in the _Amazon EC2 User Guide for Linux
Instances_.

###### Important

Creating an AMI creates a snapshot of the Amazon EC2 instance’s attached volumes. Any
software installed on the instance persists so instances, which are reused when you
launch instances from the AMI. We recommend adopting a patching strategy and regularly
updating any new AMI with updated software before applying to your fleet.

## Prepare the Amazon EC2 instance

Before you build an AMI, you must delete the worker state. The worker state persists
between worker agent launches. If this state persists onto the AMI, then all instances
launched from it will share the same state.

We also recommend you delete any existing log files. Log files can remain on an Amazon EC2
instance when your prepare the AMI. Deleting these files minimizes confusion when
diagnosing possible issue in worker fleets that use the AMI.

You should also enable the worker agent system service so the Deadline Cloud worker agent
launch when the Amazon EC2 is started.

Finally, we recommend you enable the worker agent auto shutdown. This allows the
worker fleet to scale up when needed and to shutdown when the rendering job finishes.
This auto scaling helps ensure you're only using resources as needed.

**To prepare the Amazon EC2 instance**

1. Open the Amazon EC2 console.
2. Launch an Amazon EC2 instance. For more information, see [Launch your instance](../../../AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.md "../../../AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.md").
3. Set up the host to connect to your identity provider (IdP), then mount any
   shared filesystem it needs.
4. Follow the tutorials to [Install Deadline Cloud worker agent](worker-host.md#install-worker-agent "worker-host.md#install-worker-agent"), then [Configure worker agent](worker-host.md#worker-agent-config "worker-host.md#worker-agent-config"),
   and [Create job users and groups](worker-host.md#create-job-user-and-group "worker-host.md#create-job-user-and-group").
5. If you are preparing an AMI based on Amazon Linux 2023 to run software compatible
   with the VFX Reference Platform, you need to update several requirements. For
   information, see [VFX Reference Platform
   compatibility](../userguide/smf-vfx.md "../userguide/smf-vfx.md") in the _AWS Deadline Cloud User
   Guide_.
6. Open a terminal.
   1. On Linux, open a terminal as the `root` user (or use
      `sudo` / `su`)
   2. On Windows, open an administrator command prompt or
      PowerShell terminal.

7. Ensure the worker service is not running and configured to start on
   boot:
   1. On Linux, run

   ```
   `systemctl stop deadline-worker
   systemctl enable deadline-worker`
   ```

   2. On Windows, run

   ```
   `sc.exe stop DeadlineWorker
   sc.exe config DeadlineWorker start= auto`
   ```

8. Delete the worker state.
   1. On Linux, run

   ```
   `rm -rf /var/lib/deadline/*`
   ```

   2. On Windows, run

   ```
   `del /Q /S %PROGRAMDATA%\Amazon\Deadline\Cache\*`
   ```

9. Delete the log files.
   1. On Linux, run

   ```
   `rm -rf /var/log/amazon/deadline/*`
   ```

   2. On Windows, run

   ```
   `del /Q /S %PROGRAMDATA%\Amazon\Deadline\Logs\*`
   ```

10. On Windows, it is recommended to run the Amazon EC2Launch
    Settings application found in the Start menu to complete the final host
    preparation and shutdown of the instance.

###### Note

You MUST choose **Shutdown without Sysprep** and never
choose Shutdown with Sysprep. Shutting down with Sysprep will cause all
local users to become unusable. For more information, see [Before you Begin section of the Create a custom AMI topic of the User
Guide for Windows Instances](../../../AWSEC2/latest/WindowsGuide/Creating_EBSbacked_WinAMI.md#sysprep-begin "../../../AWSEC2/latest/WindowsGuide/Creating_EBSbacked_WinAMI.md#sysprep-begin").

## Build the AMI

**To build the AMI**

1. Open the Amazon EC2 console.
2. Select **Instances** in the navigation pane, then select your
   instance.
3. Choose **Instance state**, then **Stop
   instance**.
4. After the instance is **Stopped**, choose
   **Actions**.
5. Choose **Image and templates**, then **Create
   image**.
6. Enter an **Image name**.
7. (Optional) Enter a description for your image.
8. Choose **Create image**.
