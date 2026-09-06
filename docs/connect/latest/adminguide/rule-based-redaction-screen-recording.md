

# Rule-based redaction for agent screen recordings in Connect Customer
<a name="rule-based-redaction-screen-recording"></a>

Rule-based redaction for agent screen recordings automatically hides sensitive content from recorded agent desktops based on the browser pages and application windows that agents view during a contact. When an agent navigates to a URL or opens an application window that matches one of your redaction rules, the matching window is masked in the final recording. Redaction is applied when the recording is assembled. The original unredacted video is not exposed to users who only have access to redacted recordings.

Use rule-based redaction to enforce internal privacy policies that prohibit capturing specific applications or pages that contain customer data.

![An example of rule-based redaction applied to an agent screen recording.](http://docs.aws.amazon.com/connect/latest/adminguide/images/rule-based-redaction-overview.png)


**Topics**
+ [How rule-based redaction works](#how-rule-based-redaction-works)
+ [Permissions for redacted recordings](#permissions-for-redacted-recordings)
+ [Limitations](#rule-based-redaction-limitations)
+ [Where redacted recordings are stored](#where-redacted-recordings-stored)
+ [AWS Region availability](#rule-based-redaction-region-availability)
+ [Next steps](#rule-based-redaction-next-steps)
+ [Configure rule-based redaction in a contact flow](configure-rule-based-redaction.md)
+ [Deploy the Connect Customer browser extension](deploy-browser-extension.md)

## How rule-based redaction works
<a name="how-rule-based-redaction-works"></a>

Rule-based redaction evaluates each browser page and application window the agent views during a recorded contact against the redaction rules you configure, and produces a redacted version of the recording in which matching windows are masked. The rest of the agent's screen is unchanged.

The redacted recording is produced in addition to the unredacted original. Both versions are stored in your Amazon S3 bucket under separate prefixes, so you can grant access to each version independently through security profile permissions.

Rule-based redaction runs in three stages.
+ **Configure** – In a contact flow, add a **Set recording, analytics, and processing behavior** block, enable screen recording, and enable redaction. In the same block, specify URL rules that match browser pages, window title rules that match native application windows, or both, and choose a mode that either hides or shows the matched content. Redaction applies to every contact that runs through the flow. For instructions, see [Configure rule-based redaction](configure-rule-based-redaction.md).
+ **Record** – When an agent handles a contact that runs through the flow, their screen is recorded as usual. For rules to match, the Connect Customer browser extension must be installed on every browser the agent uses. For deployment instructions, see [Deploy the browser extension](deploy-browser-extension.md).
+ **Review** – After the contact ends, a redacted version of the recording is available on the contact detail page, subject to the user's security profile. For details, see [Review agent screen recordings](review-screen-recordings.md) and [Permissions for redacted recordings](#permissions-for-redacted-recordings).

### What a redacted recording looks like
<a name="redacted-recording-appearance"></a>

The redacted recording is identical to the unredacted recording except that browser windows and application windows that match a rule are masked. The following image shows the same agent screen recorded with rule-based redaction off (left) and on (right) with a rule that redacts `aws.amazon.com`.

![A side-by-side comparison of an agent screen recording with redaction off and on.](http://docs.aws.amazon.com/connect/latest/adminguide/images/rule-based-redaction-comparison.png)


### Redaction modes
<a name="redaction-modes"></a>

Rule-based redaction uses one of two modes.
+ **Denylist - hide matching content** – Only content that matches a rule is masked in the final recording; all other content remains visible. Use this mode when agents work across a wide range of applications and you only need to hide specific pages or applications that contain sensitive data.
+ **Allowlist - show matching content** – Only content that matches a rule remains visible in the final recording; all other browser windows and native application windows are masked. Use this mode when agents are expected to work in a small set of approved applications and you want to exclude everything else.

### What rule-based redaction does not do
<a name="redaction-behavior-limits"></a>
+ It does not redact voice or chat content. For call recording redaction, see [Use sensitive data redaction with conversational analytics](https://docs.aws.amazon.com/connect/latest/adminguide/sensitive-data-redaction.html). When rule-based redaction is enabled for a contact, Connect Customer stitches the redacted video with the redacted call recording if conversational analytics call recording redaction is also enabled, and with no audio otherwise.
+ It does not hide content at the field level. Entire matching windows are masked; individual fields, DOM elements, or regions within a window cannot be selectively hidden.
+ It does not apply redaction in real time. Redaction is applied only when the recording is assembled after the contact ends.
+ It does not push configuration changes to contacts that are already in progress. Updates to a configuration take effect for the next new contact.

## Permissions for redacted recordings
<a name="permissions-for-redacted-recordings"></a>

Rule-based redaction introduces two new security profile permissions that control who can view and download redacted screen recordings. Together with the existing screen recording permissions, they let you grant broad access to redacted recordings while restricting the unredacted originals to a smaller group.

Both new permissions are in the **Recordings and Transcripts** category of the security profile. For general information about security profiles, see [Security profiles](https://docs.aws.amazon.com/connect/latest/adminguide/connect-security-profiles.html).


| Permission | Grants the ability to | 
| --- | --- | 
| Screen recording (redacted) - Access | Open the contact detail page media player and view redacted screen recordings. | 
| Screen recording (redacted) - Enable download button | Download redacted screen recordings. Requires Screen recording (redacted) - Access. | 

You assign permissions in the Connect Customer admin website. On the navigation menu, choose **Users**, then **Security profiles**.

If a user has both the unredacted and redacted access permissions, and redaction was enabled for the contact, the contact detail page displays the redacted recording.

## Limitations
<a name="rule-based-redaction-limitations"></a>
+ URL-based rules match browser pages on Google Chrome, Microsoft Edge, and Mozilla Firefox. Browsers other than Chrome, Edge, and Firefox do not report URLs to the Connect Customer Client Application, so URL rules cannot match pages in those browsers. You can still match windows in other browsers by using window title rules based on the browser's window title.
+ The redacted recording is produced in addition to the unredacted original. Both files are stored in your Amazon S3 bucket. Use Amazon S3 lifecycle policies if you need to expire the unredacted originals on a different shorter schedule than the redacted versions.
+ Each flow block supports up to 100 URL and window title rules. Each pattern string is 1 to 128 characters.
+ Windows is the only supported agent workstation operating system.

## Where redacted recordings are stored
<a name="where-redacted-recordings-stored"></a>

Redacted recordings are stored in the same Amazon S3 bucket as the unredacted recordings, as a sibling of the unredacted file. The redacted key is rooted at the parent of your configured prefix, under a fixed `Analysis/ScreenRecordings/Redacted/` path.

```
s3://{{your-bucket}}/{{your-prefix-parent}}/Analysis/ScreenRecordings/Redacted/{{year}}/{{month}}/{{day}}/{{contact-id}}_screen_recording_redacted_{{UTC-timestamp}}.mp4
```

In this path, {{your-prefix-parent}} is your configured screen recordings prefix with its last segment removed. For example, with the console default prefix `connect/{{your-instance-alias}}/ScreenRecordings`, redacted recordings are stored under `connect/{{your-instance-alias}}/Analysis/ScreenRecordings/Redacted/`.

Users with the appropriate permission can view and download redacted recordings from the contact detail page in the Connect Customer admin website. For instructions, see [Review agent screen recordings](review-screen-recordings.md).

## AWS Region availability
<a name="rule-based-redaction-region-availability"></a>

Rule-based redaction is available in the same AWS Regions that support Connect Customer agent screen recording. For the current list of supported Regions, see [Connect Customer endpoints and quotas](https://docs.aws.amazon.com/connect/latest/adminguide/regions.html).

## Next steps
<a name="rule-based-redaction-next-steps"></a>

To start using rule-based redaction, complete the following steps.
+ Confirm that your Connect Customer instance, agent workstations, and browsers meet the requirements. See [System and network requirements](sr-system-req.md).
+ Update the Connect Customer Client Application to version 3.0.2 or later on every agent workstation. See [Connect Customer Client Application](amazon-connect-client-app.md).
+ Deploy the Connect Customer browser extension to every browser that agents use during recorded contacts. See [Deploy the browser extension](deploy-browser-extension.md).
+ In a contact flow, add or update a **Set recording, analytics, and processing behavior** block to enable screen recording, enable redaction, and configure your rules and mode. See [Configure rule-based redaction](configure-rule-based-redaction.md).
+ Grant the appropriate security profile permissions to the users who need to view redacted or unredacted recordings.

For information about reviewing recordings after they are redacted, see [Review agent screen recordings](review-screen-recordings.md). For troubleshooting, see [Download log files for the screen recording app](troubleshoot-sr.md). For frequently asked questions, see [Frequently asked questions about Connect Customer screen recording capabilities](faq-screenrecording.md).