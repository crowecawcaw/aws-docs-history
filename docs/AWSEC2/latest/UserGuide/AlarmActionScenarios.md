# Amazon CloudWatch alarm action scenarios

You can use the Amazon EC2 console to create alarm actions that stop or terminate an Amazon EC2
instance when certain conditions are met. In the following screen capture of the console page
where you set the alarm actions, we've numbered the settings. We've also numbered the settings
in the scenarios that follow, to help you create the appropriate actions.

![Manage Cloudwatch alarms page.](images/manage-cloudwatch-alarms.png)

## Scenario 1: Stop idle development and test

instances

Create an alarm that stops an instance used for software development or testing when it
has been idle for at least an hour.

| Setting | Value                       |
| ------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1       | Stop                        |
| 2       | Maximum                     |
| 3       | CPU Utilization             |
| 4       | <=                          |
| 5       | 10%                         |
| 6       | 1                           |
| 7       | 1 Hour                      | ## Scenario 2: Stop idle instances Create an alarm that stops an instance and sends an email when the instance has been idle for 24 hours.                                             |
| Setting | Value                       |
| ---     | ---                         |
| 1       | Stop and email              |
| 2       | Average                     |
| 3       | CPU Utilization             |
| 4       | <=                          |
| 5       | 5%                          |
| 6       | 24                          |
| 7       | 1 Hour                      | ## Scenario 3: Send email about web servers with unusually high traffic Create an alarm that sends email when an instance exceeds 10 GB of outbound network traffic per day.           |
| Setting | Value                       |
| ---     | ---                         |
| 1       | Email                       |
| 2       | Sum                         |
| 3       | Network Out                 |
| 4       | >                           |
| 5       | 10 GB                       |
| 6       | 24                          |
| 7       | 1 Hour                      | ## Scenario 4: Stop web servers with unusually high traffic Create an alarm that stops an instance and send a text message (SMS) if outbound traffic exceeds 1 GB per hour.            |
| Setting | Value                       |
| ---     | ---                         |
| 1       | Stop and send SMS           |
| 2       | Sum                         |
| 3       | Network Out                 |
| 4       | >                           |
| 5       | 1 GB                        |
| 6       | 1                           |
| 7       | 1 Hour                      | ## Scenario 5: Stop an impaired instance Create an alarm that stops an instance that fails three consecutive status checks (performed at 5-minute intervals).                          |
| Setting | Value                       |
| ---     | ---                         |
| 1       | Stop                        |
| 2       | Average                     |
| 3       | Status Check Failed: System |
| 4       | -                           |
| 5       | -                           |
| 6       | 1                           |
| 7       | 15 Minutes                  | ## Scenario 6: Terminate instances when batch processing jobs are complete Create an alarm that terminates an instance that runs batch jobs when it is no longer sending results data. |
| Setting | Value                       |
| ---     | ---                         |
| 1       | Terminate                   |
| 2       | Maximum                     |
| 3       | Network Out                 |
| 4       | <=                          |
| 5       | 100,000 bytes               |
| 6       | 1                           |
| 7       | 5 Minutes                   |
