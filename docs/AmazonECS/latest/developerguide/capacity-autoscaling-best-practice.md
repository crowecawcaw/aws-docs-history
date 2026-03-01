# Optimizing Amazon ECS service auto scaling

An Amazon ECS service is a managed collection of tasks. Each service has an associated task
definition, a desired task count, and an optional placement strategy.

Amazon ECS service auto scaling works through the Application Auto Scaling service. Application Auto Scaling uses CloudWatch metrics as the source for scaling metrics. It also uses CloudWatch alarms to set thresholds on when to scale your service in or out.

You provide the thresholds for scaling. You can set a metric target, which is called _target tracking scaling_. You can also specify thresholds, which is called _step scaling_.

After you configure Application Auto Scaling, it continually calculates the appropriate desired task count for the service. It also notifies Amazon ECS when the desired task count should change, either by scaling it out or scaling it in.

To use service auto scaling effectively, you must choose an appropriate scaling metric. We discuss how to choose a metric in the following sections.

## Characterizing your application

Properly scaling an application requires you to know the conditions where you
should scale your application in and when you should scale it out.

In essence, you should scale out your application if demand is forecasted to outstrip capacity. Conversely, you can scale in your application to conserve costs when resources exceed demand.

### Identifying a utilization metric

To scale effectively, you must identify a metric that indicates
utilization or saturation. This metric must exhibit the following properties to
be useful for scaling.

- The metric must be correlated with demand. When you hold resources
  steady but demand changes, the metric value must also change. The
  metric should increase or decrease when demand increases or
  decreases.
- The metric value must scale in proportion to capacity. When demand
  holds constant, adding more resources must result in a proportional
  change in the metric value. So, doubling the number of tasks should
  cause the metric to decrease by 50%.

The best way to identify a utilization metric is through load testing in a
pre-production environment such as a staging environment. Commercial and
open-source load testing solutions are widely available. These solutions
typically can either generate synthetic load or simulate real user
traffic.

To start the process of load testing, you should first build dashboards
for your application’s utilization metrics. These metrics include CPU
utilization, memory utilization, I/O operations, I/O queue depth, and network
throughput. You can collect these metrics with a service such as CloudWatch Container
Insights. You can also collect them by using Amazon Managed Service for Prometheus together with Amazon Managed Grafana. During this
process, make sure that you collect and plot metrics for your application’s
response times or work completion rates.

When you load test, begin with a small request or job insertion rate. Keep this
rate steady for several minutes to allow your application to warm up. Then,
slowly increase the rate and hold it steady for a few minutes. Repeat this
cycle, increasing the rate each time until your application’s response or
completion times are too slow to meet your service-level objectives
(SLOs).

While you load test, examine each of the utilization metrics. The metrics that
increase along with the load are the top candidates to serve as your best
utilization metrics.

Next, identify the resource that reaches saturation. At the same time, also
examine the utilization metrics to see which one flattens out at a high level
first. Or, examine which one reaches peak and then crashes your application
first. For example, if CPU utilization increases from 0% to 70-80% as you add
load, then stays at that level after you add even more load, then it's safe to
say that the CPU is saturated. Depending on the CPU architecture, it might never
reach 100%. For example, assume that memory utilization increases as you add
load, and then your application suddenly crashes when it reaches the task or
Amazon EC2 instance memory limit. In this situation, it's likely the case that memory
has been fully consumed. Multiple resources might be consumed by your
application. Therefore, choose the metric that represents the resource that
depletes first.

Last, try load testing again after you double the number of tasks or Amazon EC2
instances. Assume that the key metric increases, or decreases, at half the rate
as before. If this is the case, then the metric is proportional to capacity.
This is a good utilization metric for auto scaling.

Now consider this hypothetical scenario. Suppose that you load test an
application and find that the CPU utilization eventually reaches 80% at 100
requests per second. When you add more load, it doesn't make CPU utilization
increase anymore. However, it does make your application respond more slowly. Then,
you run the load test again, doubling the number of tasks but holding the rate
at its previous peak value. If you find the average CPU utilization falls to
about 40%, then average CPU utilization is a good candidate for a scaling
metric. On the other hand, if CPU utilization remains at 80% after increasing
the number of tasks, then average CPU utilization isn't a good scaling metric.
In that case, you need more research to find a suitable metric.

### Common application models and scaling properties

You can run software of all kinds on AWS. Many workloads are homegrown, whereas
others are based on popular open-source software. Regardless of where they
originate, we have observed some common design patterns for services. How you
scale effectively depends in large part on the pattern.

#### The efficient CPU-bound server

The efficient CPU-bound server utilizes almost no resources other than CPU
and network throughput. Each request can be handled by the application
alone. Requests don't depend on other services such as databases. The
application can handle hundreds of thousands of concurrent requests, and can
efficiently utilize multiple CPUs to do so. Each request is either serviced
by a dedicated thread with low memory overhead, or there's an asynchronous
event loop that runs on each CPU that services requests. Each replica of the
application is equally capable of handling a request. The only resource that
might be depleted before CPU is network bandwidth. In CPU bound-services,
memory utilization, even at peak throughput, is a fraction of the resources
available.

You can use CPU-based auto scaling for this type of application. The
application enjoys maximum flexibility in terms of scaling. You can scale it
vertically by providing larger Amazon EC2 instances or Fargate vCPUs to it.
And, you can also scale it horizontally by adding more replicas. Adding more
replicas, or doubling the instance size, cuts the average CPU utilization
relative to capacity by half.

If you're using Amazon EC2 capacity for this application, consider placing it
on compute-optimized instances such as the `c5` or
`c6g` family.

#### The efficient memory-bound server

The efficient memory-bound server allocates a significant amount of memory
per request. At maximum concurrency, but not necessarily throughput, memory
is depleted before the CPU resources are depleted. Memory associated with a
request is freed when the request ends. Additional requests can be accepted
as long as there is available memory.

You can use memory-based auto scaling for this type of application. The
application enjoys maximum flexibility in terms of scaling. You can scale it
both vertically by providing larger Amazon EC2 or Fargate memory resources to
it. And, you can also scale it horizontally by adding more replicas. Adding
more replicas, or doubling the instance size, can cut the average memory
utilization relative to capacity by half.

If you're using Amazon EC2 capacity for this application, consider placing it
on memory-optimized instances such as the `r5` or
`r6g` family.

Some memory-bound applications don't free the memory that's associated
with a request when it ends, so that a reduction in concurrency doesn't
result in a reduction in the memory used. For this, we don't recommend that
you use memory-based scaling.

#### The worker-based server

The worker-based server processes one request for each individual worker
thread one after another. The worker threads can be lightweight threads,
such as POSIX threads. They can also be heavier-weight threads, such as UNIX
processes. No matter which thread they are, there's always a maximum
concurrency that the application can support. Usually the concurrency limit
is set proportionally to the memory resources that are available. If the
concurrency limit is reached, the application places additional requests into a backlog
queue. If the backlog queue overflows, the application immediately rejects additional incoming requests. Common applications that fit this pattern include
Apache web server and Gunicorn.

Request concurrency is usually the best metric for scaling this
application. Because there's a concurrency limit for each replica, it's
important to scale out before the average limit is reached.

The best way to obtain request concurrency metrics is to have your
application report them to CloudWatch. Each replica of your application can
publish the number of concurrent requests as a custom metric at a high
frequency. We recommend that the frequency is set to be at least once every
minute. After several reports are collected, you can use the average
concurrency as a scaling metric. You calculate this metric by taking the
total concurrency and dividing it by the number of replicas. For example, if
total concurrency is 1000 and the number of replicas is 10, then the average
concurrency is 100.

If your application is behind an Application Load Balancer, you can also use the
`ActiveConnectionCount` metric for the load balancer as a
factor in the scaling metric. You must divide the `ActiveConnectionCount` metric
by the number of replicas to obtain an average value. You must use the
average value for scaling, as opposed to the raw count
value.

For this design to work best, the standard deviation of response latency
should be small at low request rates. We recommend that, during periods of
low demand, most requests are answered within a short time, and there isn't
a lot of requests that take significantly longer than average time to
respond. The average response time should be close to the 95th percentile
response time. Otherwise, queue overflows might occur as result. This leads
to errors. We recommend that you provide additional replicas where necessary
to mitigate the risk of overflow.

#### The waiting server

The waiting server does some processing for each request, but it is highly
dependent on one or more downstream services to function. Container
applications often make heavy use of downstream services like databases and
other API services. It can take some time for these services to respond,
particularly in high capacity or high concurrency scenarios. This is because
these applications tend to use few CPU resources and utilize their maximum
concurrency in terms of available memory.

The waiting service is suitable either in the memory-bound server pattern
or the worker-based server pattern, depending on how the application is
designed. If the application’s concurrency is limited only by memory, then
average memory utilization should be used as a scaling metric. If the
application’s concurrency is based on a worker limit, then average
concurrency should be used as a scaling metric.

#### The Java-based server

If your Java-based server is CPU-bound and scales proportionally to CPU
resources, then it might be suitable for the efficient CPU-bound server
pattern. If that is the case, average CPU utilization might be appropriate
as a scaling metric. However, many Java applications aren't CPU-bound,
making them challenging to scale.

For the best performance, we recommend that you allocate as much memory as
possible to the Java Virtual Machine (JVM) heap. Recent versions of the JVM,
including Java 8 update 191 or later, automatically set the heap size as
large as possible to fit within the container. This means that, in Java,
memory utilization is rarely proportional to application utilization. As the
request rate and concurrency increases, memory utilization remains constant.
Because of this, we don't recommend scaling Java-based servers based on
memory utilization. Instead, we typically recommend scaling on CPU
utilization.

In some cases, Java-based servers encounter heap exhaustion before
exhausting CPU. If your application is prone to heap exhaustion at high
concurrency, then average connections are the best scaling metric. If your
application is prone to heap exhaustion at high throughput, then average
request rate is the best scaling metric.

#### Servers that use other garbage-collected runtimes

Many server applications are based on runtimes that perform garbage
collection such as .NET and Ruby. These server applications might fit into
one of the patterns described earlier. However, as with Java, we don't
recommend scaling these applications based on memory, because their observed
average memory utilization is often uncorrelated with throughput or
concurrency.

For these applications, we recommend that you scale on CPU utilization if
the application is CPU bound. Otherwise, we recommend that you scale on
average throughput or average concurrency, based on your load testing
results.

#### Job processors

Many workloads involve asynchronous job processing. They include
applications that don't receive requests in real time, but instead subscribe
to a work queue to receive jobs. For these types of applications, the proper
scaling metric is almost always queue depth. Queue growth is an indication
that pending work outstrips processing capacity, whereas an empty queue
indicates that there's more capacity than work to do.

AWS messaging services, such as Amazon SQS and Amazon Kinesis Data Streams, provide CloudWatch
metrics that can be used for scaling. For Amazon SQS,
`ApproximateNumberOfMessagesVisible` is the best metric. For
Kinesis Data Streams, consider using the `MillisBehindLatest` metric, published
by the Kinesis Client Library (KCL). This metric should be averaged across
all consumers before using it for scaling.
