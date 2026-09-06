# Troubleshooting

Use the following guidance to diagnose common issues with A/B forensic video
watermarking. If watermarking is configured incorrectly, MediaLive disables watermarking
for that output group and the channel continues to run and produce video. You can
view alerts on the MediaLive console, and MediaLive also emits them as CloudWatch events with
the detail type `MediaLive Channel Alert`. For the full list of channel
alerts and for information about how to view alerts, see [List of alerts for channels](monitor-activity-types-alerts-channels.md "monitor-activity-types-alerts-channels.md").

**Alert 5051 — Watermark License Failure**

MediaLive couldn't retrieve or read the license secret from AWS Secrets Manager. To
resolve this:

- Verify that the configured AWS Secrets Manager secret name is valid and that
  the secret exists. A typo or a deleted secret causes this failure.
- Verify that the secret is in the same AWS Region as the MediaLive
  channel. MediaLive doesn't retrieve secrets across Regions.
- Confirm that MediaLive can read the secret by checking both the IAM
  policy on the trusted-entity role (it must include
  `secretsmanager:GetSecretValue`) and the resource policy on
  the secret itself. For more information about the trusted-entity role,
  see [IAM permissions for MediaLive as a trusted entity](setting-up-trusted-entity.md "setting-up-trusted-entity.md").
  **Alert 5052 — Watermark Library Initialization
  Failure**

MediaLive retrieved the secret but the Irdeto watermarker failed to initialize.
To resolve this:

- Verify that the license stored in the secret is not expired,
  truncated, or malformed.
- Verify that the **Operator Id** value configured in
  the output group matches the operator ID in the license
  entitlement.
- Verify that the **Watermark ID Length** value
  configured in the output group matches the license entitlement.

###### Note

MediaLive has no visibility into Irdeto licensing details. For
any question about whether a license is valid, or about the operator ID,
watermark ID length, or entitlements, contact Irdeto directly.

**Individual rendition delivered without watermarks**

If one or more renditions are delivered to both the regular A destination and
B alternate destination without watermarks, but the channel continues running
without error, the encode dimensions might be outside the supported range. The
supported A/B watermarking range is 240 through 3840 pixels wide by 240 through 2160
pixels high. Verify that the output width is from 240 through 3840 pixels and the
height is from 240 through 2160 pixels.

**Watermark detection fails at the downstream
system**

If the channel is running and producing output but the downstream watermark
detection system can't extract valid watermarks, check the following:

- Verify that the input provides an embedded UTC timecode. Epoch locking uses this timecode
  to sequence the watermark. For
  the full set of epoch locking requirements and to verify that your pipeline
  can epoch lock successfully, see [Configuring output locking and setting the mode](pipeline-locking-set-up.md#pipeline-locking-mode "pipeline-locking-set-up.md#pipeline-locking-mode").
