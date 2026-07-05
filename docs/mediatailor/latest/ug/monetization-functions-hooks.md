# Functions lifecycle hooks

A lifecycle hook defines when MediaTailor runs your function during playback. This page is a
complete reference for input fields, output namespaces, and the rules that govern data flow
at each hook.

## Overview

MediaTailor supports two lifecycle hooks:

- **`PRE_SESSION_INITIALIZATION`** fires
  once when a viewer starts a new session. Use it for one-time setup work such as
  fetching audience segments. At this point, no ad break has occurred, so ad break
  context is not available.
- **`PRE_ADS_REQUEST`** fires before
  every ad decision server (ADS) request — once per ad break in the stream.
  Use it to customize the ADS request with targeting data, modify the ADS URL, or
  add headers.

The key difference is timing: `PRE_SESSION_INITIALIZATION` runs once and
sets up data that persists for the entire session, while `PRE_ADS_REQUEST`
runs repeatedly and can tailor each ADS request to the specific ad break.

## Input field reference

| Field                                  | Type    | PRE\_SESSION\_INITIALIZATION | PRE\_ADS\_REQUEST |
| -------------------------------------- | ------- | ---------------------------- | ----------------- |
| `session.id`                           | Long    | ✓                            | ✓                 |
| `session.uuid`                         | String  | ✓                            | ✓                 |
| `session.client_ip`                    | String  | ✓                            | ✓                 |
| `session.user_agent`                   | String  | ✓                            | ✓                 |
| `session.referer`\*                    | String  | ✓                            | ✓                 |
| `session.avail_duration_secs`          | Long    | ✗                            | ✓                 |
| `session.avail_duration_ms`            | Long    | ✗                            | ✓                 |
| `player_params.*`                      | String  | ✓                            | ✓                 |
| `event.id`                             | String  | ✓                            | ✓                 |
| `event.hook`                           | String  | ✓                            | ✓                 |
| `event.timestamp`                      | String  | ✓                            | ✓                 |
| `avail.index`                          | Int     | ✗                            | ✓                 |
| `avail.random`                         | Long    | ✗                            | ✓                 |
| `avail.source_content_time_epoch_ms`   | Long    | ✗                            | ✓                 |
| `scte.event_id`                        | Int     | ✗                            | ✓                 |
| `scte.avail_num`                       | Int     | ✗                            | ✓                 |
| `scte.segmentation_event_id`           | Int     | ✗                            | ✓                 |
| `scte.segmentation_type_id`            | Int     | ✗                            | ✓                 |
| `scte.segmentation_upid`               | String  | ✗                            | ✓                 |
| `scte.segmentation_upid.assetId`       | String  | ✗                            | ✓                 |
| `scte.segmentation_upid.cueData.key`   | String  | ✗                            | ✓                 |
| `scte.segmentation_upid.cueData.value` | String  | ✗                            | ✓                 |
| `scte.unique_program_id`               | Int     | ✗                            | ✓                 |
| `scte.archive_allowed_flag`            | Boolean | ✗                            | ✓                 |
| `scte.delivery_not_restricted_flag`    | Boolean | ✗                            | ✓                 |
| `scte.device_restrictions`             | Int     | ✗                            | ✓                 |
| `scte.no_regional_blackout_flag`       | Boolean | ✗                            | ✓                 |
| `scte.segment_num`                     | Int     | ✗                            | ✓                 |
| `scte.segments_expected`               | Int     | ✗                            | ✓                 |
| `scte.sub_segment_num`                 | Int     | ✗                            | ✓                 |
| `scte.sub_segments_expected`           | Int     | ✗                            | ✓                 |
| `scte.avails_expected`                 | Long    | ✗                            | ✓                 |
| `asset.*`                              | String  | ✗                            | ✓                 |
| `adsRequest.url`                       | String  | ✗                            | ✓                 |
| `adsRequest.method`                    | String  | ✗                            | ✓                 |
| `adsRequest.headers.<key>`             | String  | ✗                            | ✓                 |
| `adsRequest.body`                      | String  | ✗                            | ✓                 |

\* `session.referer` is only present when a
Referer header is included in the session initialization request. Use
`$exists(session.referer)` to check before accessing.
