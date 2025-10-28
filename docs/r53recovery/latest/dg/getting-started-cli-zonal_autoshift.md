# Edit a practice run configuration

You can edit a practice run configuration for a resource with the CLI to update different configuration
options, such as changing the alarms for practice runs or updating the blocked dates or blocked windows,
when ARC won't start practice runs. To edit a practice run configuration, use the
`update-practice-run-configuration` command.

Note the following when you edit a practice run configuration for a resource:

- The only supported alarm type at this time is `CLOUDWATCH`.
- You must use alarms that are in the same AWS Region that your resource is deployed in.
- Specifying an outcome alarm is required. Specifying a blocking alarm is optional.
- Specifying blocked dates or blocked windows is optional.
- The blocked dates or blocked windows that you specify replace any existing values.
  For example, to edit a practice run configuration for a resource to specify a new blocked date, use a
  command like the following:

```
aws arc-zonal-shift update-practice-run-configuration \
      --resource-identifier="arn:aws:elasticloadbalancing:`Region`:`111122223333`:`ExampleALB123456890`" \
      --blocked-dates 2024-03-01
```

```
{
   "arn": "arn:aws:elasticloadbalancing:us-west-2:111122223333:ExampleALB123456890",
   "name": "zonal-shift-elb"
   "zonalAutoshiftStatus": "DISABLED",
   "practiceRunConfiguration": {
       "blockingAlarms": [
                  {
               "type": "CLOUDWATCH",
               "alarmIdentifier": "arn:aws:cloudwatch:us-west-2:111122223333:alarm:us-west-2-BlockWhenALARM"
           }
       ]
       "outcomeAlarms": [
           {
               "type": "CLOUDWATCH",
               "alarmIdentifier": "arn:aws:cloudwatch:us-west-2:111122223333:alarm:us-west-2-MyAppHealthAlarm"
           }
       ],
       "blockedWindows": [
           "Mon:10:00-Mon:10:30"
       ],
       "blockedDates": [
           "2024-03-01"
       ]
}
```
