# Create a practice run configuration

Before you can enable zonal autoshift for a resource, you must create a practice run configuration
for the resource, to choose options for the required practice runs. You create a practice run configuration for a resource
with the CLI by using the `create-practice-run-configuration` command.

Note the following when you create a practice run configuration for a resource:

- The only supported alarm type at this time is `CLOUDWATCH`.
- You must use alarms that are in the same AWS Region that your resource is deployed in.
- Specifying an outcome alarm is required. Specifying a blocking alarm is optional.
- Specifying blocked or allowed dates or windows is optional.
  You create a practice run configuration with the CLI by using the `create-practice-run-configuration` command.

For example, to create a practice run configuration for a resource, use a command like the following:

```
aws arc-zonal-shift create-practice-run-configuration \
      --resource-identifier="arn:aws:elasticloadbalancing:`Region`:`111122223333`:`ExampleALB123456890`" \
      --outcome-alarms type=CLOUDWATCH,alarmIdentifier=arn:aws:cloudwatch:`Region`:`111122223333`:alarm:`Region`-`MyAppHealthAlarm` \
      --blocking-alarms type=CLOUDWATCH,alarmIdentifier=arn:aws:cloudwatch:`Region`:`111122223333`:alarm:`Region`-`BlockWhenALARM` \
      --blocked-dates 2023-12-01 --blocked-windows Mon:10:00-Mon:10:30
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
           "2023-12-01"
       ]
}
```
