# Review

| CMPERF_10: Have you considered the implementation of scalable, cost-effective,<br>and low-maintenance managed services for high-performance computing workloads to<br>process diverse data types (such as high and low fidelity data, logs, and commands)<br>collected from vehicles? |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                                                                                                                                                       |

**[CMPERF\_BP10.1] Build a cost-effective solution that is scalable
and yet easy to manage as more vehicles connect to the cloud.**

We need to think about use cases that are critical in order to bring a good user
experience to end consumers. For example, vehicle state services play a key role for
consumers to know the state of vehicle, for example, door locked, or window down. In this
case, data caching solutions (Redis Cache or MemoryDB) are important to quickly access last
available data with low latency (200 milliseconds or less) interval. Any new data will move
classify earlier as historical data, this can be stored in either No SQL database such as
DynamoDB or data lake for further processing. Training can be done to improve machine learning
models and later it can be deployed for prediction based on the type of use case (for
example, recommend cabin temperature based on historical data in vehicle)

Recommendation - Telemetry data strategy 

- Top 50 Properties – In memory cache (open standard numbers)
- Next 500 Properties – Microsecond interval
- 5000+ Properties – Seconds or higher interval

| CMPERF_11: Have you tested the ability of your platform to seamlessly adopt,<br>replace, or upgrade various compute solutions, including standalone systems,<br>container-based architectures, and serverless technologies? |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                                                                                             |

Ensuring that your platform can seamlessly adopt, replace, or
upgrade various compute solutions is crucial for scalability,
adaptability, and resilience.

When considering AWS services, here's how you can ensure flexibility across
different compute solutions:

**[CMPERF\_BP11.1] Self-managed systems (Amazon EC2)**

- Compute: Virtual servers in the cloud where you can run
  applications.
- Load balancing: Distributes incoming application traffic across multiple targets,
  such as EC2 instances.
- Auto scaling: Ensures that you have the right number of EC2 instances available
  to handle the load for your application.
- Seamless adoption and upgrades: Use Amazon Machine Images (AMIs) to create and
  save configurations, making it easier to scale, replace, or upgrade.
  **[CMREF\_BP11.2] Container-based architectures**

- Containerization: A highly scalable, high-performance
  container orchestration service that supports Docker
  containers. 
  - Serverless compute for containers. You don't need to
    provision, configure, or scale clusters of virtual
    machines to run containers.

- Seamless adoption and upgrades: Use container orchestration to manage the
  lifecycle of containers, ensuring that services can be updated or rolled back without
  downtime.
  **[CMPERF\_BP11.3] Serverless technologies**

- Run code without provisioning or managing servers. You pay
  only for the compute time that you consume.
- API Gateway: For creating, deploying, and managing APIs
  along with serverless function to create serverless
  applications.
- Seamless adoption and upgrades: With serverless, deployments can be versioned,
  allowing for easy rollbacks.
