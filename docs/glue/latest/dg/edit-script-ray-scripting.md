

# Using Ray Core and Ray Data in AWS Glue for Ray
<a name="edit-script-ray-scripting"></a>

**Important**  
AWS Glue for Ray is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Glue for Ray end of support](https://docs.aws.amazon.com/glue/latest/dg/awsglue-ray-jobs-availability-change.html).

Ray is a framework for scaling up Python scripts by distributing work across a cluster. You can use Ray as a solution to many sorts of problems, so Ray provides libraries to optimize certain tasks. In AWS Glue, we focus on using Ray to transform large datasets. AWS Glue offers support for Ray Data and parts of Ray Core to facilitate this task. 

## What is Ray Core?
<a name="edit-script-ray-scripting-core-what"></a>

The first step of building a distributed application is identifying and defining work that can be performed concurrently. Ray Core contains the parts of Ray that you use to define tasks that can be performed concurrently. Ray provides reference and quick start information that you can use to learn the tools they provide. For more information, see [What is Ray Core?](https://docs.ray.io/en/latest/ray-core/walkthrough.html) and [Ray Core Quick Start](https://docs.ray.io/en/latest/ray-overview/getting-started.html#ray-core-quick-start). For more information about effectively defining concurrent tasks in Ray, see [Tips for first-time users](https://docs.ray.io/en/latest/ray-core/tips-for-first-time.html). 

**Ray tasks and actors**  
In AWS Glue for Ray documentation, we might refer to *tasks* and *actors*, which are core concepts in Ray.  
Ray uses Python functions and classes as the building blocks of a distributed computing system. Much like when Python functions and variables become "methods" and "attributes" when used in a class, functions become "tasks" and classes become "actors" when they're used in Ray to send code to workers. You can identify functions and classes that might be used by Ray by the `@ray.remote` annotation.  
Tasks and actors are configurable, they have a lifecycle, and they take up compute resources throughout their life. Code that throws errors can be traced back to a task or actor when you're finding the root cause of problems. Thus, these terms might come up when you're learning how to configure, monitor, or debug AWS Glue for Ray jobs.   
To begin learning how to effectively use tasks and actors to build a distributed application, see [Key Concepts](https://docs.ray.io/en/latest/ray-core/key-concepts.html) in the Ray docs.

## Ray Core in AWS Glue for Ray
<a name="edit-script-ray-scripting-core-glue"></a>

AWS Glue for Ray environments manage cluster formation and scaling, as well as collecting and visualizing logs. Because we manage these concerns, we consequently limit access to and support for the APIs in Ray Core that would be used to address these concerns in an open-source cluster.

In the managed `Ray2.4` runtime environment, we do not support:
+ [Ray Core CLI](https://docs.ray.io/en/releases-2.4.0/ray-core/api/cli.html)
+ [Ray State CLI](https://docs.ray.io/en/releases-2.4.0/ray-observability/api/state/cli.html)
+ `ray.util.metrics` Prometheus metric utility methods:
  + [Counter](https://docs.ray.io/en/releases-2.4.0/ray-core/api/doc/ray.util.metrics.Counter.html)
  + [Gauge](https://docs.ray.io/en/releases-2.4.0/ray-core/api/doc/ray.util.metrics.Gauge.html)
  + [Histogram](https://docs.ray.io/en/releases-2.4.0/ray-core/api/doc/ray.util.metrics.Histogram.html)
+ Other debugging tools:
  + [ray.util.pdb.set\_trace](https://docs.ray.io/en/releases-2.4.0/ray-core/api/doc/ray.util.pdb.set_trace.html)
  + [ray.util.inspect\_serializability](https://docs.ray.io/en/releases-2.4.0/ray-core/api/doc/ray.util.inspect_serializability.html)
  + [ray.timeline](https://docs.ray.io/en/releases-2.4.0/ray-core/api/doc/ray.timeline.html)

## What is Ray Data?
<a name="edit-script-ray-scripting-data-what"></a>

When you're connecting to data sources and destinations, handling datasets, and initiating common transforms, Ray Data is a straightforward methodology for using Ray to solve problems transforming Ray datasets. For more information about using Ray Data, see [Ray Datasets: Distributed Data Preprocessing](https://docs.ray.io/en/releases-2.4.0/data/dataset.html). 

You can use Ray Data or other tools to access your data. For more information on accessing your data in Ray, see [Connecting to data in Ray jobs](edit-script-ray-connections-formats.md).

## Ray Data in AWS Glue for Ray
<a name="edit-script-ray-scripting-data-glue"></a>

Ray Data is supported and provided by default in the managed `Ray2.4` runtime environment. For more information about provided modules, see [Modules provided with Ray jobs](edit-script-ray-env-dependencies.md#edit-script-ray-modules-provided).