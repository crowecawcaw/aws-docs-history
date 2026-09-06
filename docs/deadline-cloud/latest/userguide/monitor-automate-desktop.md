

# Automate Deadline Cloud monitor desktop deployment and workflows
<a name="monitor-automate-desktop"></a>

The AWS Deadline Cloud monitor desktop application includes a command-line interface (CLI) that administrators can use to set up profiles for users and that artists and developers can use to integrate the monitor into automated workflows on their workstations.

## Finding the Deadline Cloud monitor executable
<a name="monitor-automate-desktop-binary-location"></a>

To use the CLI commands, run the Deadline Cloud monitor executable from a terminal. The default installation location depends on your operating system and installation method.

Windows  

```
%LOCALAPPDATA%\DeadlineCloudMonitor\DeadlineCloudMonitor.exe
```

macOS  

```
/Applications/DeadlineCloudMonitor.app/Contents/MacOS/DeadlineCloudMonitor
```

Linux (deb or RPM package)  

```
/usr/bin/deadline-cloud-monitor
```

Linux (AppImage)  
Run the AppImage file directly from the location where you downloaded it.

In the following examples, replace `DeadlineCloudMonitor` with the full path to the executable for your operating system.

## Setting up a profile for streamlined user access
<a name="monitor-automate-desktop-create-profile"></a>

Administrators use the `create-profile` command to create Deadline Cloud monitor profiles for users. This command configures a profile so that users can open the monitor, log in, and start working without additional configuration or profile selection.

The `create-profile` command accepts the following flags:
+ `--enable-auto-login` – Configures the monitor to automatically log in with the most recently used profile when the application starts.
+ `--set-as-deadline-default` – Sets the profile as the default for Deadline Cloud tools, including the Deadline Cloud submitter, the Deadline CLI, and the Deadline Cloud GUI applications. This flag does not affect the AWS Command Line Interface (AWS CLI).

When both flags are enabled, users open the monitor and are logged in automatically with no other configuration or profile selection required.

**To create a profile**  


Run the following command, replacing the placeholder values with your monitor details.

```
DeadlineCloudMonitor create-profile \
    --profile {{profile-name}} \
    --monitor-id {{monitor-id}} \
    --monitor-url https://{{monitorName}}.{{region}}.deadlinecloud.amazonaws.com \
    --enable-auto-login \
    --set-as-deadline-default
```

The command creates the profile and writes the configuration to the Deadline Cloud configuration files on the user's workstation. The monitor URL must be in the format `https://{{monitorName}}.{{region}}.deadlinecloud.amazonaws.com`.

**Note**  
The `create-profile` command exits after creating the profile. To open the monitor with the new profile, run the `login` command or open the Deadline Cloud monitor desktop application.

## Integrating the Deadline Cloud monitor into your workflows
<a name="monitor-automate-desktop-workflow-integration"></a>

Use the `login`, `logout`, and `handle-url` commands to integrate the Deadline Cloud monitor into scripts and automated workflows on your workstation.

### Logging in and logging out
<a name="monitor-automate-desktop-login-logout"></a>

Use the `login` and `logout` commands to control authentication as part of a workflow. For example, a script that submits jobs can use the `login` command to ensure the user is authenticated before submission begins.

When you use the `login` command, the monitor opens directly to the specified profile, skipping the profile selection screen. After authentication completes, the monitor minimizes to the system tray so that your workflow can continue. If the monitor is already running for the specified profile, the existing window comes to the foreground instead of starting a new instance.

**To log in to a profile**  


Run the following command, replacing {{profile-name}} with the name of your Deadline Cloud monitor profile.

```
DeadlineCloudMonitor login --profile {{profile-name}}
```

**To log out of a profile**  


Run the following command to clear the credentials for a profile and signal any running monitor instance for that profile to exit.

```
DeadlineCloudMonitor logout --profile {{profile-name}}
```

### Opening the monitor to a specific page
<a name="monitor-automate-desktop-handle-url"></a>

Use the `handle-url` command to open the Deadline Cloud monitor to a specific page. This command is useful when a script performs an action, such as creating a job, and you want to automatically open the monitor to show the result. For example, after a script submits a job, the script can call `handle-url` to open the monitor directly to the job details page.

You can also use the `deadline-cloud-monitor://` URL as a link on company websites, wikis, or task trackers to let users open the monitor directly to a specific page.

The URL uses the `deadline-cloud-monitor://` protocol scheme with a `launch` command. The URL includes the profile name and the monitor page URL to open.

**To open the monitor to a specific page**  


Run the following command, replacing {{monitor-page-url}} with the URL-encoded monitor page URL and {{profile-name}} with your profile name.

```
DeadlineCloudMonitor handle-url --url "deadline-cloud-monitor://launch?url={{monitor-page-url}}&profile={{profile-name}}"
```