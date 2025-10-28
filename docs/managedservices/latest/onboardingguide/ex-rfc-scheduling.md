# Schedule RFCs

The **Scheduling** feature allows you to choose a start time for RFCs. The following options are available in the **Scheduling** feature:

- **Execute this change ASAP**: AMS runs the RFC as soon as it's approved.
  Most CTs are automatically approved. Use this option if don't want the RFC to start at a specific time.
- **Schedule this change**: Set a day, time, and time zone for the RFC to run. For automated change types, it's a best practice to request a start time that's at least 10 minutes after you plan to submit the RFC. For managed automation change types, it's required that you request a start time that's at least 24 hours after you plan to submit the RFC. If the RFC isn't approved by the configured start time, then the RFC is rejected.

## Set an RFC schedule

To schedule an RFC, use one of the following methods:

**Execute this change ASAP**:

- Console: Do nothing. This uses the default RFC schedule.
- API or CLI: Remove the `RequestedStartTime` and `RequestedEndTime` options in the Create RFC operation.

**ASAP** "managed automation" RFCs are auto-rejected if they are not approved within thirty days of submission.

**Schedule this change**:

- Console: Select the **Schedule this change** radio button. A **Start time** area opens. Manually type in a day
  or use the calendar widget to pick a day. Enter a time, in UTC, expressed in ISO 8601 format, and use the drop-down list to pick a
  location. By default, AMS uses the ISO 8601 format YYYYMMDDThhmmssZ or YYYY-MM-DDThh:mm:ssZ, either format is accepted.

###### Note

The **Default End Time** is 4 hours from the **Start time** that you enter. To set the **End Time** of your scheduled change beyond 4 hours, use the API or CLI to run the change.

- API or CLI: Submit values for the `RequestedStartTime` and `RequestedEndTime` parameters in the
  Create RFC operation. Passing a configured `RequestedEndTime` doesn't stop the run for an automated change type that
  has already started. For a "managed automation" change type, if the
  `RequestedEndTime` is reached while AMS Operations research is still ongoing, and you're in communication with AMS, then you can request an
  extension, or you might be asked to re-submit the RFC.

###### Tip

For an example of a UTC time readout, see [UTC](https://time.is/UTC "https://time.is/UTC") on the Time-is website. Example ISO 8601 format for a date/time value
of 2016-12-05 at 2:20pm: **2016-12-05T14:20:00Z** or **20161205T142000Z**.

If you provide...

- only a `RequestedStartTime`, the RFC is considered
  scheduled and the `RequestedEndTime` is populated using the `ExecutionDurationInMinutes` value.
- only a `RequestedEndTime`, we throw an
  InvalidArgumentException.
- both `RequestedStartTime` and
  `RequestedEndTime`, we overwrite the
  `RequestedEndTime` with the specified start time
  plus the `ExecutionDurationInMinutes` value.
- neither `RequestedStartTime` nor
  `RequestedEndTime`, we keep those values as null and the RFC is treated as an ASAP RFC.

###### Note

For all scheduled RFCs, an unspecified end time is written to be the time of the specified `RequestedStartTime` plus the
`ExpectedExecutionDurationInMinutes` attribute of the submitted change type. For example, if the `ExpectedExecutionDurationInMinutes` is "60" (minutes), and
the specified `RequestedStartTime` is `2016-12-05T14:20:00Z` (December 5, 2016 at 4:20 AM), the actual end time would be set to December 5, 2016 at 5:20 AM.
To find the `ExpectedExecutionDurationInMinutes` for a specific change type, run this command:

```
aws amscm --profile saml get-change-type-version --change-type-id `CHANGE_TYPE_ID` --query "ChangeTypeVersion.{ExpectedDuration:ExpectedExecutionDurationInMinutes}"
```

## Use the RFC Priority option

Use the **Priority** option in `execution mode = manual` change types to alert AMS
Operations to the urgency of the request.

**Priority** option in `execution mode = manual`:

Specify the priority of a manual RFC as **High**,
**Medium**, or **Low**. RFCs classified as
**High** are reviewed and approved prior to RFCs classified as
**Medium**, subject to RFC service level objectives (SLOs) and their submission times.
RFCs with **Low** priority or no priority specified are processed
in the order they are submitted.
