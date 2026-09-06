

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Request RFC restricted run periods
<a name="ex-rfc-restrict-execute"></a>

Formerly known as blackout days, you can request to restrict certain time periods. No changes can be run during those times.

To set a restricted run period, use the [UpdateRestrictedExecutionTimes](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_UpdateRestrictedExecutionTimes.html) API operation and set a specific time period, in UTC. The period that you specify overrides any previous periods that were specified. If you submit an RFC during the specified restricted run time, submission fails with the error Invalid RFC Schedule. You can specify up to 200 restricted time periods. By default, no restricted period is set. The following is an example request command (with SAML authentication configured):

```
aws amscm  --profile saml update-restricted-execution-times --restricted-execution-times="[{\"TimeRange\":{\"StartTime\":\"2018-01-01T12:00:00Z\",\"EndTime\":\"2018-01-01T12:00:01Z\"}}]"
```

You can also view your current RestrictedExecutionTimes setting by running the [ListRestrictedExecutionTimes](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_ListRestrictedExecutionTimes.html) API operation. Example:

```
aws amscm  --profile saml list-restricted-execution-times
```

If you want to submit an RFC during a specified restricted execution time, then add the **RestrictedExecutionTimesOverrideId** with the value of **OverrideRestrictedTimeRanges**, and then submit the RFC as you normally would. It's a best practice to only use this method for a critical or emergency RFC. For more information, see the API reference for [SubmitRfc](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_SubmitRfc.html).