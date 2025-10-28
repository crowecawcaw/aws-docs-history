# Automated and manual CTs

A constraint on change types is whether they are automated or manual, this is the change type
`AutomationStatusId` attribute, called the
**Execution mode** in the AMS console.

Automated change types have expected results and execution times and run
through the AMS automated system, generally within an hour or less (this largely depends on what resources
the CT is provisioning).
Manual change types are uncommon,
but they are treated differently because they require that an AMS operator act on the RFC before it can be
run. That
sometimes means communicating with the RFC submitter, so, manual change types require varying lengths of
time to complete.

For all scheduled RFCs, an unspecified end time is written to be the time of the specified `RequestedStartTime` plus the
`ExpectedExecutionDurationInMinutes` attribute of the submitted change type. For example, if the `ExpectedExecutionDurationInMinutes` is "60" (minutes), and
the specified `RequestedStartTime` is `2016-12-05T14:20:00Z` (December 5, 2016 at 4:20 AM), the actual end time would be set to December 5, 2016 at 5:20 AM.
To find the `ExpectedExecutionDurationInMinutes` for a specific change type, run this command:

```
aws amscm --profile saml get-change-type-version --change-type-id `CHANGE_TYPE_ID` --query "ChangeTypeVersion.{ExpectedDuration:ExpectedExecutionDurationInMinutes}"
```

###### Note

Scheduled RFCs with **Execution mode**= Manual, in the Console, must be set to run
at least 24 hours in the future.

###### Note

When using manual CTs, AMS recommends that you use the ASAP **Scheduling** option
(choose **ASAP** in the console, leave start and end time blank in the API/CLI) as these CTs require an AMS operator to examine the RFC, and
possibly communicate with you before it can be approved and run. If you schedule these RFCs, be sure to allow at least 24 hours. If approval does not
happen before the scheduled start time, the RFC is rejected automatically.

AMS aims to respond to a manual CT within four hours, and will correspond as soon as possible, but it could take much longer for the RFC to actually
be run.

For a list of the CTs that are Manual and require AMS review, see the Change Type CSV file, available
on the **Developer's Resources** page of the Console.

**YouTube Video**:
[How can I find automated change types for AMS RFCs?](https://www.youtube.com/watch?v=sOzDuCCOduI&list=PLhr1KZpdzukc_VXASRqOUSM5AJgtHat6-&index=2&t=1s "https://www.youtube.com/watch?v=sOzDuCCOduI&list=PLhr1KZpdzukc_VXASRqOUSM5AJgtHat6-&index=2&t=1s")

To find the **Execution mode** for a CT in the AMS console, you must use the
**Browse change types** search option. The results show the execution mode of the matching
change type or change types.

To find the `AutomationStatus` for a specific change type by using the AMS CLI,
run this command:

```
aws amscm --profile saml get-change-type-version --change-type-id `CHANGE_TYPE_ID` --query "ChangeTypeVersion.{AutomationStatus:AutomationStatus.Name}"
```

You can also look up change types in the
[AMS Change Type Reference](../ctref/index.md "../ctref/index.md"), which provides information
about all AMS change types.

###### Note

The AMS API/CLI are not currently part of the AWS API/CLI. To access the AMS
API/CLI, you download the AMS SDK through the AMS console.
