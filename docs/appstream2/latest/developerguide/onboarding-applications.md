

# Application onboarding guidelines
<a name="onboarding-applications"></a>

Before you make an application available to end users through WorkSpaces Applications, validate that the application works correctly in the WorkSpaces Applications cloud environment, verify that the application can be streamed without rendering artifacts, and size your fleet appropriately for the application's resource profile. This page provides a structured onboarding checklist that you can follow for each application you plan to stream. If you plan to use multi-session, you need to pay specific attention to the ability to run multiple versions of the application on the same host. If you plan to use [native application mode](https://docs.aws.amazon.com/appstream2/latest/developerguide/feature-support-native-application-mode.html), you need to verify that the application does not present any compatibility problems with this mode.

These guidelines apply whether you are onboarding a new application or migrating an existing application from another delivery model.

## Overview of the onboarding process
<a name="onboarding-overview"></a>

Onboarding an application to WorkSpaces Applications has two parallel tracks:
+ **Application compatibility validation:** Confirm the application behaves correctly in the streaming environment across the features your users rely on.
+ **Instance sizing and capacity planning:** Choose an instance type and fleet scaling policy that match the application's CPU, memory, and GPU profile and your expected concurrent user count.

We recommend completing compatibility validation first (on an Image Builder and a pilot fleet), then using the measurements from that validation to drive instance sizing decisions.

## Part 1: Application compatibility validation
<a name="onboarding-compatibility"></a>

### General compatibility
<a name="onboarding-general-compat"></a>

WorkSpaces Applications establishes a streaming session in this order:

1. The user's client connects to a streaming instance.

1. The user is logged into the server operating system session on the instance.

1. The application is started.

1. The streaming session begins, at which point environment settings that depend on the client (for example, client display resolution, DPI, client time zone, and client-redirected devices like printers) are applied.

Because client-dependent environment settings are applied *after* the application starts, an application that reads these values only once during startup will not react to the user's actual client configuration. Validate the following:
+ The application reads or subscribes to display resolution, DPI, and time zone changes after startup, **or** you configure the streaming instance with defaults that match your user population before the client connects.
+ The application tolerates the user's local time zone being different from the streaming instance's time zone.
+ The application does not fail or hang when the client disconnects and reconnects mid-session.

### Multi-session compatibility
<a name="onboarding-multi-session-compat"></a>

If you plan to run the application on a multi-session fleet, validate the following on an Image Builder and a pilot fleet with two or more concurrent users:
+ The application's license permits concurrent multi-user sessions on a single server instance. Some applications' per-device or per-user licenses explicitly forbid this configuration.
+ User profiles, application settings, and user data are isolated between sessions. Test that a change one user makes is not visible to another concurrent user.
+ User-specific data is written to per-user locations such as `%APPDATA%` and `%LOCALAPPDATA%`, not to shared directories such as `C:\Program Files` or `C:\ProgramData`.
+ The application does not rely on system services shared across all sessions, or such services can correctly handle multiple concurrent sessions.
+ The application does not contain hardcoded paths that assume a single-user environment.
+ System device dialogs enumerate only the current user's redirected devices like scanners and printers, not all devices visible to the server.
+ File open and save dialogs correctly resolve mapped client drives and redirected folders for the current user.
+ The application's installer, updater, and any background processes do not require interactive administrator access while users are signed in.

**Note**  
Multi-session fleets currently do not support webcam, [Dynamic Application Framework](https://docs.aws.amazon.com/appstream2/latest/developerguide/dynamic-app-framework.html), and [Smart Card Authentication](https://docs.aws.amazon.com/appstream2/latest/developerguide/active-directory-prerequisites-smart-card-authentication.html). If you need any of these features, we recommend that you use single-session fleets.

### Native application mode compatibility
<a name="onboarding-native-app-mode"></a>

Native application mode streams each remote application as a separate window on the user's local device, with its own taskbar icon. Applications that work correctly in classic mode can behave differently in native application mode because window management, focus, and rendering are handled differently. For an overview of the feature, see [Native Application Mode](https://docs.aws.amazon.com/appstream2/latest/developerguide/feature-support-native-application-mode.html).

Validate the following in native application mode on an Image Builder and a pilot fleet:
+ **Window display:** All application windows, including dialogs, splash screens, and modal prompts, display correctly and can be interacted with. Pay particular attention to windows that are drawn manually rather than with the standard Windows UI toolkits (for example, custom-rendered splash screens or startup dialogs that appear before the main window). These are more likely to have compatibility issues.
+ **Transparent or non-rectangular windows:** Check for any windows that have transparent areas or that have rounded or non-rectangular shapes (for example, balloon tips, custom tooltips, or skinned windows). These may not render correctly in native application mode.
+ **System tray:** Applications that require the Windows notification area (system tray) are not currently supported in native application mode. If your application uses a tray icon only for secondary features, confirm that the core workflow still functions when the tray is unavailable.
+ **DPI awareness:** Streaming sessions may run at resolutions and DPI settings that differ from the local client. If the application is not DPI-aware, Windows itself scales the output, which results in blurred rendering. Test on at least one client with a DPI scaling other than 100% (for example, a high-DPI laptop at 125% or 150%).
+ **Multi-window workflows:** Test workflows that span multiple application windows (for example, switching between a main window and a modal dialog, or between two documents opened in separate windows). Confirm that focus transitions and taskbar click-to-activate behave as expected.
+ **Alt\+Tab and taskbar behavior:** Switch between the application and other local applications by using Alt\+Tab and by clicking the taskbar icon. The remote application should come to the foreground without bringing unrelated remote windows with it.
+ **Modal dialogs:** When a modal dialog is open in the remote application, the underlying remote window should correctly indicate it is disabled, and clicking it should flash or activate the modal.
+ **Print workflows:** Print from within the application and verify that the print dialog is visible (not hidden behind the main window) and that redirected printers are enumerated. Print dialogs displayed by some printer drivers may attach to the wrong window. If you observe this, consider using the **DCV PDF Printer** instead of **Microsoft Print to PDF**.
+ **Browser tab docking:** When users try to dock or undock tabs in one browser window into separate windows during a streaming session in native application mode, the remote streaming browser does not work the same way as a local browser. Users must press the Alt key until the tabs dock into separate browser windows. If your users rely on frequent tab undocking, plan user training for this behavior.
+ **Mode switching:** Test that the application continues to function if the user switches between native application mode and classic mode during a session.

We recommend starting native application mode validation with a pilot user group and documenting any application-specific limitations before full deployment. Application behavior and performance can vary between streaming modes, so testing in classic mode is not a substitute for testing in native application mode.

### File handling and redirection
<a name="onboarding-file-handling"></a>
+ Open and save files from and to mapped client drives and redirected folders.
+ If the application uses temporary files, confirm they are written to per-user temp directories.
+ Test large-file operations over the session's file transfer mechanism if your users work with files larger than the typical size handled by the streaming session.

### Printing
<a name="onboarding-printing"></a>
+ Test printing to each redirected printer type your users will use (network printers, Microsoft Print to PDF, PDF printer drivers such as the DCV PDF Printer, and third-party redirected printers).
+ Test printing from each application that has a print workflow, including applications that embed web content (such as Chromium-based views).
+ Validate print dialog behavior in native application mode (see the previous section).

### Local device interactions
<a name="onboarding-local-devices"></a>
+ Audio input and output (microphone, speakers, and headsets).
+ Webcam, if used by the application.
+ USB device redirection, if used by the application. See [USB device redirection](https://docs.aws.amazon.com/appstream2/latest/developerguide/feature-support-USB-devices-qualified.html) for the list of supported devices.
+ Smart card authentication, if required by the application.

### Network performance
<a name="onboarding-network-perf"></a>
+ Measure application responsiveness over a network connection representative of your worst-case user (for example, a remote user on a consumer broadband connection with 100 ms round-trip time). Streaming sessions are sensitive to round-trip time and packet loss.
+ Validate that the application tolerates brief network interruptions and session reconnects.

### Multi-monitor support
<a name="onboarding-multi-monitor"></a>
+ Test workflows that span multiple monitors on the client side.
+ If the application reads monitor geometry, confirm it reads the client's monitor layout, not the streaming instance's layout.

### Audio and video features
<a name="onboarding-audio-video"></a>

Real-time audio-video scenarios (voice, video conferencing, and collaboration tools embedded in the application) require higher frame rates and may need a larger instance type. See [Part 2: Instance sizing and capacity planning](#onboarding-sizing).

### Validation environment
<a name="onboarding-validation-env"></a>

Perform the checks in this section on an Image Builder first, then on a pilot fleet with a small group of representative users, before rolling the image out to your full user base. Do not rely on classic-mode testing as a substitute for native-application-mode testing.

## Part 2: Instance sizing and capacity planning
<a name="onboarding-sizing"></a>

### Choose an instance family
<a name="onboarding-instance-family"></a>

Select an instance family based on the resource profile of the application. For hardware specifications and pricing, see [WorkSpaces Applications Instance Families](https://docs.aws.amazon.com/appstream2/latest/developerguide/instance-types.html) and [WorkSpaces Applications Pricing](https://aws.amazon.com/appstream2/pricing/).


| Application profile | Recommended instance family | 
| --- | --- | 
| Office, web browsers, most line-of-business applications | General Purpose | 
| Compute-bound applications (heavy client-side computation, local analytics) | Compute Optimized | 
| Memory-intensive applications (large datasets in memory, in-memory databases) | Memory Optimized | 
| Graphics applications using DirectX, OpenGL, or OpenCL | Graphics G4dn, G5, or G6 family | 
| Real-time audio-video for high-frame-rate scenarios | Scale up the instance size within your chosen family; consider a Graphics family instance if the application also uses GPU acceleration | 

Each WorkSpaces Applications instance has a 200 GB fixed-size C drive that is deleted after every user session. Do not rely on instance-local storage for user data; use home folders, file shares, or profile management for persistence.

### Size an instance for a single user
<a name="onboarding-single-user-sizing"></a>

Before sizing for concurrent users, measure the application's resource use for a single session:
+ Provision an Image Builder of the smallest instance size in your chosen family that meets the application's stated minimum requirements.
+ Sign in as a single user and run the representative workload end to end. Include all dependencies that will run in the streaming session (for example, background sync clients, security agents, and profile management clients).
+ Measure, using Windows Performance Monitor or an equivalent tool: peak and sustained CPU use, peak and sustained working-set (private bytes) memory use, disk I/O rate, and if applicable, GPU use and video memory.
+ If peak CPU exceeds approximately 80% or peak memory exceeds approximately 75% of instance capacity during normal workflows, move up to the next instance size.
+ Leave headroom for the Windows Server operating system, the WorkSpaces Applications agent, Amazon DCV, anti-malware, and any other management agents. A rule of thumb is to reserve approximately 1 vCPU and 1 GB of memory for base system overhead on a single-session instance.

### Size for multi-session fleets
<a name="onboarding-multi-session-sizing"></a>

Multi-session fleets run multiple users concurrently on a single Windows Server instance. The supported maximum users per instance depends on the instance size and the resource profile of the application.
+ Start from your single-user measurement (from the previous section).
+ Apply a concurrency multiplier based on the application's behavior. For applications that have a predominantly idle resource profile (for example, office applications used interactively), plan for aggregate CPU and memory use to scale roughly linearly with user count, but with a 20–30% reduction due to shared OS overhead. For applications that have a consistently active resource profile (for example, data processing tools or browsers running heavy web applications), plan for nearly linear scaling with no reduction.
+ Calculate a candidate maximum users per instance as:

```
max_users_per_instance = min(
    (instance_vcpus - 1) / peak_single_user_vcpus_under_concurrency,
    (instance_memory_gb - 1) / peak_single_user_memory_gb_under_concurrency
)
```
+ Validate the candidate value in an actual multi-session pilot. Run a test with the candidate number of concurrent users (for example, with a load-generation tool or with actual pilot users). Monitor CPU use (target less than 80% peak, less than 70% sustained), available memory (target greater than 15% of total at peak), disk queue length (target less than 2 sustained), and DCV session responsiveness (subjective — does the session feel interactive?).
+ If the pilot fails any of these targets, reduce the maximum users per instance by one and retest. If the pilot passes comfortably, you may increase the maximum users per instance by one and retest, or leave headroom for workload spikes.

### Configure fleet scaling
<a name="onboarding-fleet-scaling"></a>

After you know the maximum users per instance, configure fleet scaling based on your expected concurrent user count over time. See [Fleet Auto Scaling for WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/autoscaling.html) for the full mechanics. This section summarizes the decisions you should make as part of onboarding.
+ **Minimum capacity.** Set based on the lowest expected concurrent user count during business hours, divided by the users per instance. Provisioning takes several minutes per instance, so a minimum capacity of zero or a value that is too low can result in users waiting for an instance to launch at the start of the workday. For predictable morning ramp-ups, use a **scheduled scaling policy** to increase the minimum capacity before the workday starts and decrease it before the workday ends.
+ **Maximum capacity.** Set to an upper bound that accounts for peak concurrent users plus a safety margin. The peak is typically 1.2–1.5× the average during business hours, but measure your own traffic to set this accurately.
+ **Target utilization.** For fleets with unpredictable demand, use a **target tracking scaling policy**. Choose a target utilization such that `100% - target utilization` exceeds your expected user turnover rate (churn) within a 15-minute window. For example, if 10% of users start and end sessions within any 15-minute window, set the target to 90% or lower. See [Best Practices for Scaling Policy Design](https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/best-practices-for-scaling-policy-design.html) in the whitepaper for more detail.
+ **InsufficientCapacityError alarm.** Create an Amazon CloudWatch alarm on the `InsufficientCapacityError` metric for each fleet, so that administrators are alerted when automatic scaling cannot keep up with demand.

### Validate end-to-end with a pilot
<a name="onboarding-pilot"></a>

Before rolling an application out to all users, run a pilot with 10–50 users for at least one full business week. During the pilot:
+ Confirm that application compatibility validation results from Part 1 hold under real user workloads.
+ Confirm that the chosen instance size supports the observed peak concurrent users per instance.
+ Confirm that the fleet scaling policy handles the start-of-day ramp and end-of-day ramp-down without `InsufficientCapacityError` events.
+ Collect feedback on session responsiveness and application behavior from pilot users.

## Onboarding checklist
<a name="onboarding-checklist"></a>

Use this checklist to track the status of each application you are onboarding.

**Application compatibility**
+ The application license permits the intended deployment (single-session or multi-session, concurrent users).
+ General compatibility checks pass (client-dependent settings applied after application start).
+ Multi-session compatibility checks pass (if targeting multi-session fleets).
+ Native application mode checks pass (windows, dialogs, tray, DPI, focus, print, and mode switching).
+ File handling and redirection checks pass.
+ Printing workflows validated for all redirected printer types users will use.
+ Local device interactions (audio, webcam, USB, and smart card) validated for all devices users will use.
+ Multi-monitor workflows validated.

**Instance sizing and capacity**
+ Instance family chosen based on application resource profile.
+ Single-user resource use measured on an Image Builder.
+ Maximum users per instance calculated and validated in a multi-session pilot (if applicable).
+ Fleet scaling policy configured (minimum capacity, maximum capacity, target utilization or scheduled scaling).
+ `InsufficientCapacityError` alarm configured.

**Pilot and rollout**
+ Pilot run with 10–50 users for at least one business week.
+ Pilot feedback reviewed and any blocking issues resolved.
+ Application documented for end-user training (including any native application mode known behaviors such as browser tab docking via the Alt key).
+ Rollout plan agreed with stakeholders.