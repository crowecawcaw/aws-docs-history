# Amazon Neptune Serverless

Amazon Neptune Serverless is an on-demand autoscaling configuration
that is architected to scale your DB cluster as needed to meet even very large
increases in processing demand, and then scale down again when the demand decreases.
It helps to automate the processes of monitoring workload and adjusting capacity
for your Neptune database. Because capacity is adjusted automatically based on
application demand, you're charged only for the resources that your application
actually needs.

## Use cases for Neptune Serverless

Neptune Serverless supports many types of workloads. It is suitable for demanding,
highly variable workloads and can be very helpful if your database usage is typically
heavy for short periods of time, followed by long periods of light activity or no
activity at all. Neptune Serverless is especially useful for the following use cases:

- **Variable workloads**   –  
  Workloads that have sudden and unpredictable increases in CPU activity. With Neptune
  Serverless, your graph database automatically scales capacity to meet the needs
  of the workload and scales back down when the surge of activity is over. You no
  longer have to provision for peak or average capacity. You can specify an upper
  capacity limit to handle peak workloads, and that capacity isn't used unless
  it's needed.

The granularity of scaling provided by Neptune Serverless helps you match
capacity closely to your workload's needs. Neptune Serverless can add or
remove capacity in fine grained increments based on what is needed. It can
add as little as half a [Neptune
Capacity Unit (NCU)](neptune-serverless-capacity-scaling.md "neptune-serverless-capacity-scaling.md") when only a little more capacity is required.

- **Multi-tenant applications**   –  
  By taking advantage of Neptune Serverless, you can create a separate DB cluster
  for each of the applications you need to run without having to manage those tenant
  clusters individually. Each of the tenant clusters may have different busy and idle
  periods depending on multiple factors, but Neptune Serverless can scale them
  efficiently without your intervention.
- **New applications**   –  
  When you deploy a new application, you're often unsure how much database
  capacity it will need. Using Neptune Serverless, you can set up a DB cluster
  that can scale automatically to meet the new application's capacity
  requirements as they develop.
- **Capacity planning**   –  
  Suppose you usually adjust your database capacity, or verify the optimal
  database capacity for your workload, by modifying the DB instance classes
  of all the DB instances in a cluster. With Neptune Serverless, you can
  avoid this administrative overhead. Instead, you can modify existing DB
  instances from provisioned to serverless or from serverless to provisioned
  without having to create a new DB cluster or instance.
- **Development and testing**   –  
  Neptune Serverless is also perfect for development and testing environments.
  With Neptune Serverless you can create DB instances with a high enough
  maximum capacity to test your most demanding application, and a low minimum
  capacity for all the other times when the system may be idle between tests.

Neptune Serverless only scales compute capacity. Your storage volume remains
the same, and is not affected by serverless scaling.

###### Note

You can also [use Neptune
auto-scaling with Neptune Serverless](manage-console-autoscaling.md#autoscaling-with-serverless "manage-console-autoscaling.md#autoscaling-with-serverless") to handle different kinds of workload
variations.

## Amazon Neptune Serverless constraints

- Neptune Serverless is only available in the following regions:
  - US East (N. Virginia):   `us-east-1`
  - US East (Ohio):   `us-east-2`
  - US West (N. California):   `us-west-1`
  - US West (Oregon):   `us-west-2`
  - Canada (Central):   `ca-central-1`
  - Europe (Stockholm):   `eu-north-1`
  - Europe (Spain):   `eu-south-2`
  - Europe (Ireland):   `eu-west-1`
  - Europe (London):   `eu-west-2`
  - Europe (Paris):   `eu-west-3`
  - Europe (Frankfurt):   `eu-central-1`
  - Europe (Zurich):   `eu-central-2`
  - Asia Pacific (Tokyo):   `ap-northeast-1`
  - Asia Pacific (Seoul):   `ap-northeast-2`
  - Asia Pacific (Singapore):   `ap-southeast-1`
  - Asia Pacific (Sydney):   `ap-southeast-2`
  - Asia Pacific (Jakarta):   `ap-southeast-3`
  - Asia Pacific (Hong Kong):   `ap-east-1`
  - Asia Pacific (Mumbai):   `ap-south-1`
  - South America (São Paulo):   `sa-east-1`

- **Not available in early engine versions**   –  
  Neptune Serverless is only available in engine releases 1.2.0.1 or later.
- **Not compatible with the Neptune lookup cache**   –  
  The [lookup cache](feature-overview-lookup-cache.md "feature-overview-lookup-cache.md") does not work with
  serverless DB instances.
- **Maximum memory in a serverless instance is 256 GB**   –  
  Setting `MaxCapacity` to 128 NCUs (the highest supported setting) allows a
  Neptune Serverless instance to scale to 256 GB of memory, which is equivalent to that
  of an `R6g.8XL` provisioned instance type.
