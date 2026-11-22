

# Proactive troubleshooting for your WorkSpaces fleet (Preview)

**Important**  
Proactive troubleshooting for your WorkSpaces fleet is in preview release and is subject to change.

WorkSpaces Advisor monitors your WorkSpaces fleet and tells you about issues that affect groups of WorkSpaces, so you can act before more of your users are affected. Advisor learns what's normal for your fleet, groups affected WorkSpaces by the configuration they share, and diagnoses the likely cause where it can. Each detected issue shows the affected WorkSpaces, the evidence Advisor used, and a recommended action.

You don't need to start an investigation, turn anything on, or set any threshold. Advisor monitors your fleet automatically.

During preview, this capability is available in the AWS Regions that support WorkSpaces Personal, except the AWS GovCloud (US) Regions, the China Regions, and the Saudi Arabia Region. There's no additional charge for it during preview.

## How Advisor detects fleet issues
<a name="workspaces-advisor-fleet-detect"></a>
+ Learns your baseline. Advisor compares current behavior with recent history for your own fleet, so an issue reflects a change from what's normal for you rather than a fixed limit.
+ Groups related WorkSpaces. Advisor groups affected WorkSpaces that share a configuration, such as a directory, subnet, bundle, or compute type, and reports them as one issue.
+ Forecasts resource use. Advisor projects when WorkSpaces will run short of CPU, memory, or disk space, so you can act before users are affected.
+ Diagnoses the likely cause. Where the evidence supports it, Advisor names the likely cause and the component involved. When it can't determine a cause, it says so.
+ Excludes expected activity. Advisor excludes known AWS maintenance and similar expected events, so they aren't reported as issues.
+ Handles new directories. For a directory with little history, Advisor starts from a reference baseline and switches to the directory's own baseline when enough history is available.

## Issues Advisor detects
<a name="workspaces-advisor-fleet-issues"></a>


| Issue category | What Advisor tells you | Example | 
| --- | --- | --- | 
| Unhealthy WorkSpaces that share a configuration | A group of WorkSpaces became unhealthy at a higher rate than normal, the configuration they share, and the likely cause where known. | WorkSpaces in one directory and subnet stopped responding at the same time. | 
| Resources running out | WorkSpaces that have reached, or are projected to reach, a critical level of CPU, memory, root volume, or user volume; the expected time frame; top processes using the resource. | Several WorkSpaces in one bundle are projected to run out of user volume space within days. | 
| Trusted device certificates nearing expiry | Certificates that restrict access to trusted devices and are about to expire, and where they're used. | A certificate imported for trusted device access expires soon. | 
| Certificate authority issues for certificate-based authentication | AWS Private CA certificates used for certificate-based authentication that are nearing expiry or not available, and the affected directories. | The private CA that issues sign-in certificates for a directory is about to expire. | 

Advisor might add issue categories during preview.

## Review and act on detected issues
<a name="workspaces-advisor-fleet-review"></a>

1. Open the [Amazon WorkSpaces console](https://console.aws.amazon.com/workspaces/v2/home).

1. In the navigation pane, choose **WorkSpaces Advisor**.

1. Review the list of detected issues. Each issue shows the affected WorkSpaces, when the issue started, and its status.

1. Choose an issue to view its details, including the evidence and the recommended action.

1. Review the risk and impact of the recommended action, then take the action from the console or through your own change process.

## Preview limitations
<a name="workspaces-advisor-fleet-limits"></a>
+ Detected issues appear in the WorkSpaces console only. Advisor doesn't send notifications to other services during preview.
+ Detection thresholds aren't configurable.
+ This capability covers WorkSpaces Personal only.

For what data this capability uses and how it's protected, see [Security for proactive troubleshooting for your WorkSpaces fleet](workspaces-advisor-security.md#workspaces-advisor-security-fleet).