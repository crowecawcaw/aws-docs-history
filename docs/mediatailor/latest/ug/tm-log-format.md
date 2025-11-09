# AWS Elemental MediaTailor transcode logs description and event

types

The following sections describe the logs that MediaTailor emits to describe events with the
transcode service when preparing creatives for ad stitching. These are
`TranscodeService` logs.

###### Topics

- [TranscodeService events](#log-types-tminteraction "#log-types-tminteraction")
- [Transcode logs properties](#transcode-logs-main "#transcode-logs-main")

## TranscodeService events

The following events are emitted during MediaTailor interactions while transcoding ads.

| Log                     | Description                                                                                                            |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `IMPORT_ERROR`          | MediaTailor encountered an internal error during an import job (for<br>preconditioned ads). Using an empty set of ads. |
| `INITIALIZED`           | MediaTailor initialized either a transcode job or an import job (for<br>preconditioned ads).                           |
| `INTERNAL_ERROR`        | MediaTailor encountered an internal error. Using an empty set of<br>ads.                                               |
| `MISSING_VARIANTS`      | MediaTailor could not transcode the ad because of missing variants.<br>Using an empty set of ads.                      |
| `PROFILE_NOT_FOUND`     | MediaTailor could not transcode the ad because of a missing profile to<br>transcode. Using an empty set of ads.        |
| `TRANSCODE_COMPLETED`   | Video transcoding is complete. The ad can be used for ad<br>insertion.                                                 |
| `TRANSCODE_ERROR`       | MediaTailor encountered an internal error during a transcode job. Using<br>an empty set of ads.                        |
| `TRANSCODE_IN_PROGRESS` | Video transcoding is in progress. The transcoded video is not<br>ready. Using an empty set of ads.                     |

## Transcode logs properties

This section describes the properties of the transcode logs.

| Property             | Type   | Required | Description                                                                                                                                                                                                       |
| -------------------- | ------ | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `awsAccountId`       | string | true     | The AWS account ID for the MediaTailor configuration that was used<br>for the session.                                                                                                                            |
| `eventTimestamp`     | string | true     | The date and time of the event.                                                                                                                                                                                   |
| `originId`           | string | true     | The configuration name from the MediaTailor configuration. This is<br>different from the video content source, which is also part of the<br>configuration.                                                        |
| `eventType`          | string | false    | The code for the event that triggered this log message. Example:<br>`TRANSCODE_ERROR`.                                                                                                                            |
| `eventDescription`   | string | false    | A short description of the event that triggered this log message,<br>provided by the MediaTailor service. By default, this is empty.                                                                              |
| `sessionId`          | string | false    | The unique numeric identifier that MediaTailor assigned to the player<br>session. All requests that a player makes for a session have the<br>same session ID. Example:<br>`e039fd39-09f0-46b2-aca9-9871cc116cde`. |
| `creativeUniqueId`   | string | false    | The unique identifier for the ad creative that's being<br>transcoded.                                                                                                                                             |
| `profileName`        | string | false    |                                                                                                                                                                                                                   |
| `adUri`              | string | false    | The URI for the ad creative.                                                                                                                                                                                      |
| `transcodeRequestId` | string | false    | The unique identifier for this transcode request.                                                                                                                                                                 |
| `cacheStatus`        | string | false    | Indicates if MediaTailor cached the transcoded ad.                                                                                                                                                                |
