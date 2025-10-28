# Alerts for multiplexes

The following table lists the alerts that MediaLive might generate for a multiplex. You
can view these alerts in these ways:

- You can view the alerts for each multiplex on the MediaLive console. For more
  information, see [Alerts tab – Viewing
  alerts](monitoring-console-general.md#view-alerts "monitoring-console-general.md#view-alerts").
- You use your preferred AWS SDK or API to monitor alerts about multiplex
  activity. For more information, see [Monitoring alerts using the AWS SDKs or API](monitoring-api.md "monitoring-api.md").
- MediaLive turns alerts into CloudWatch events with the detailType set to `MediaLive
Multiplex Alert`. For an example of the JSON for these events, see [JSON
  for a state change event](monitoring-cloudwatch-json-state-change.md "monitoring-cloudwatch-json-state-change.md").

| Alert ID | Alert wording                            | Description                                                                                                                                                             |
| -------- | ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 7001     | Communication Lost from Encoder          | The multiplex is not receiving communication from one or more encoders.                                                                                                 |
| 7002     | Communication Lost from Multiplex        | The encoder is not receiving communication from the multiplex.                                                                                                          |
| 7003     | Active Encoder Switched for Program      | The multiplex has switched to using a different encoder pipeline for the output of a multiplex program.                                                                 |
| 7004     | Active Encoder Sent Fill or Slate Frames | Program ${multiplex_program_name} is receiving fill or slate frames from the active encoder.                                                                            |
| 7005     | MPTS Bitrate Overflow                    | The bitrate for the MPTS is over the limit. The MPTS bitrate is the sum of the bitrate for all of the programs. The problem should resolve itself within a few seconds. |
