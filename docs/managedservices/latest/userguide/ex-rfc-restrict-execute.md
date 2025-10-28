# Request RFC restricted run periods

Formerly known as blackout days, you can request to restrict certain time periods. No changes can be run during those times.

To set a restricted run period, use the [UpdateRestrictedExecutionTimes](../ApiReference-cm/API_UpdateRestrictedExecutionTimes.md "../ApiReference-cm/API_UpdateRestrictedExecutionTimes.md")
API operation and set a specific time period, in UTC. The period that you specify
overrides any previous periods that were specified. If you submit an RFC during
the specified restricted run time, submission fails with the error Invalid RFC Schedule.
You can specify up to 200 restricted time periods. By default, no restricted period is
set. The following is an example request command (with SAML authentication configured):

```
aws amscm  --profile saml update-restricted-execution-times --restricted-execution-times="[{\"TimeRange\":{\"StartTime\":\"2018-01-01T12:00:00Z\",\"EndTime\":\"2018-01-01T12:00:01Z\"}}]"
```

You can also view your current RestrictedExecutionTimes setting by running the
[ListRestrictedExecutionTimes](../ApiReference-cm/API_ListRestrictedExecutionTimes.md "../ApiReference-cm/API_ListRestrictedExecutionTimes.md") API operation. Example:

```
aws amscm  --profile saml list-restricted-execution-times
```

If you want to submit an RFC during a specified restricted execution time, then
add the **RestrictedExecutionTimesOverrideId** with the value of **OverrideRestrictedTimeRanges**,
and then submit the RFC as you normally would. It's a best practice to only use this method for a critical or
emergency RFC. For more information, see the API reference for [SubmitRfc](../ApiReference-cm/API_SubmitRfc.md "../ApiReference-cm/API_SubmitRfc.md").
