# Use historical patterns to scale Amazon ECS services with predictive

scaling

Predictive scaling looks at past load data from traffic flows to analyze daily or weekly patterns. It
then uses this analysis to anticipate future needs and proactively increase tasks in your service as
needed.

Predictive auto scaling is most useful in the following situations.

- Cyclical traffic ‐ Increased use of resources during regular business hours, and decreased
  use of resources during evenings and weekends.
- Recurring on-and-off workload patterns ‐ Examples include batch processing, testing, or
  periodic data analysis.
- Applications with long initialization times ‐ This can impact application performance during
  scale-out events causing of noticeable latency.
  If your applications take a long time to initialize and traffic increases in a regular pattern, you
  should consider using predicitive scaling. It helps you scale faster by proactively increasing the number
  of tasks for forecasted loads, instead of using dynamic scaling policies, such as Target Tracking or Step
  Scaling alone. By helping you avoid the possibility of over-provisioning the number of tasks, predictive
  scaling can also potentially save you money.

For example, consider an application that has high usage during business hours and low usage overnight.
At the start of each business day, predictive scaling can scale-out tasks before the first influx of
traffic. This helps your application maintain high availability and performance when going from a period of
lower utilization to a period of higher utilization. You don't have to wait for dynamic scaling to react to
changing traffic. You also don't have to spend time reviewing your application's load patterns and trying
to schedule the right amount of tasks using scheduled scaling.

Predictive scaling is a service-level capability that scales the task of your service
independently from the scaling of the underlying compute capacity (for example, EC2 or
Fargate). For Fargate, AWS manages and automatically scales the underlying capacity
based on task requirements. For EC2 capacity, you can use Auto Scaling group capacity providers to
automatically scale underlying EC2 instances based on the scaling requirements of your
tasks.

###### Contents

- [Predictive scaling overview](#predictive-auto-scaling-overview "#predictive-auto-scaling-overview")
- [Create a predictive scaling policy](predictive-scaling-create-policy.md "predictive-scaling-create-policy.md")
- [Evaluate your predictive scaling policies](predictive-scaling-graphs.md "predictive-scaling-graphs.md")
- [Override
  the forecast](predictive-scaling-overriding-forecast-capacity.md "predictive-scaling-overriding-forecast-capacity.md")
- [Use custom metrics](predictive-scaling-custom-metrics.md "predictive-scaling-custom-metrics.md")

## How predictive scaling works in Amazon ECS

Here you can learn about considerations for using predictive scaling, how it works, and what the limits
are.

### Considerations for using predictive

scaling

- You want to make sure predictive scaling is suitable for your workload. You can check this by
  configuring scaling policies in **forecast only** mode and see
  what the console recommends. You should evaluate the forecast and recommendations before
  starting to use predictive scaling.
- Before predictive scaling can start forecasting, it needs at least 24 hours of historical
  data. The more historical data that is available, the more effective the forecast, with two
  weeks being ideal. You'll also need to wait 24 hours for before predictive scaling can generate
  new forecasts when you delete an Amazon ECS service and create a new one. One way to speed this up
  is to use custom metrics to aggregate metrics across old and new Amazon ECS service.
- Choose a load metric that accurately represents the full load on your application and is the
  aspect of your application that's most important to scale on.
- Dynamic scaling with predictive scaling helps you follow the demand for your application
  closely, so you can scale in during lulls and scale out during unexpected increases in traffic.
  When multiple scaling policies are active, each policy determines the desired number of tasks
  independently, and the desired number of tasks is set to the maximum of those.
- You can use predictive scaling alongside your dynamic scaling policies, such as target
  tracking or step scaling, so that your applications scale based on both real-time and historic
  patterns. By itself, predictive scaling doesn't scale-in your tasks.
- If you use a custom role when calling the `register-scalable-target` API, you may
  get an error saying predictive scaling policy can only work with SLR enabled. In this case you
  should call `register-scalable-target` again but without role-arn. Use SLR when
  registering the scalable target and call the `put-scaling-policy` API.

### How predictive scaling works

You use predictive scaling by creating a predictive scaling policy that specifies the CloudWatch metric to
monitor and analyze. Predictive scaling must have at least 24 hours of data to start forecasting future
values.

After you create the policy, predictive scaling starts analyzing metric data from up to the past 14
days to identify patterns. This analysis is used to generate the next 48 hours of requirements hourly
forecasts. The latest CloudWatch data is used to update the forecast every six hours. As new data comes in,
predictive scaling continuously improves the accuracy of future forecasts.

When you first enable predictive scaling, it runs in _forecast only_
mode. It generates forecasts in this mode, but it doesn't scale your Amazon ECS service based on those
forecasts. This means you can evaluate the accuracy and suitability of the forecast. You view forecast
data by using the `GetPredictiveScalingForecast` API operation or the AWS Management Console.

When you decide to start using predictive scaling, switch the scaling policy to _forecast and scale_ mode. The following occurs while in this mode.

Your Amazon ECS service is scaled at the start of each hour based on the forecast for that hour, by
default. You can choose to start earlier by using the `SchedulingBufferTime` property in the
`PutScalingPolicy` API operation. This makes new tasks launch ahead of forecasted demand
and gives them time to boot and become ready to handle traffic.

### Maximum tasks limit

When you register Amazon ECS services for scaling, you define a maximum number of tasks that can be
launched per service. By default, when scaling policies are set, they cannot increase the number of
tasks higher than its maximum limit.

Alternatively, you can allow the service's maximum number of tasks to be automatically increased if the
forecast approaches or exceeds the maximum number of tasks of the Amazon ECS service.

###### Warning

Use caution when allowing the maximum number of tasks to be automatically increased. This can
lead to more tasks being launched than intended, if the increased maximum number of tasks isn't
monitored and managed. The increased maximum number of tasks then becomes the new normal maximum
number of tasks for the Amazon ECS service until you manually update it. The maximum number of tasks
doesn't automatically decrease back to the original maximum.

### Supported regions

- US East (N. Virginia)
- US East (Ohio)
- US West (N. California)
- US West (Oregon)
- Africa (Cape Town)
- Asia Pacific (Hong Kong)
- Asia Pacific (Jakarta)
- Asia Pacific (Mumbai)
- Asia Pacific (Osaka)
- Asia Pacific (Seoul)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Asia Pacific (Tokyo)
- Canada (Central)
- China (Beijing)
- China (Ningxia)
- Europe (Frankfurt)
- Europe (Ireland)
- Europe (London)
- Europe (Milan)
- Europe (Paris)
- Europe (Stockholm)
- Middle East (Bahrain)
- South America (São Paulo)
- AWS GovCloud (US-East)
- AWS GovCloud (US-West)
