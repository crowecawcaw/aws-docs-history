

# Virtual desktop infrastructure autostop
<a name="virtual-desktops-autostop"></a>

Administrators can configure settings to allow idle VDIs to be stopped or terminated. There are 4 configurable settings:

1. Idle Timeout: Sessions idle for this time with CPU utilization below the threshold will time out.

1. CPU Utilization Threshold: Sessions with no interaction and under this threshold (vCPU usage) are considered idle. If this is set to 0, then sessions will never be considered idle.
**Important**  
RES runs an idle detection script at the top of every minute that checks CPU utilization. This script itself causes temporary CPU spikes, which can prevent idle detection if your threshold is set too low.

1. Transition State: After idle timeout, sessions will transition to this state (stopped or terminated).

1. Enforce Schedule: If selected, a session that has been stopped for being idle can be resumed by its daily schedule.

![update session settings](http://docs.aws.amazon.com/res/latest/ug/images/res-update-session-settings.png)


These settings are present on the **Desktop Settings** page under the **Server** tab. After you update the settings according to your requirements, choose **Submit** to save the settings. New sessions will use the updated settings, but note that existing sessions will still use the settings which they had when they were launched.

After they time out, sessions will either terminate or transition into the `STOPPED_IDLE` state based on their configuration. Users will have the ability to start `STOPPED_IDLE` sessions from the UI.