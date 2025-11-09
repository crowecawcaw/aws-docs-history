# Selection

| CMPERF_1: Have you identified the critical components of the architecture,<br>performance data collection to determine the best performing architecture? |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                          |

The connected mobility ecosystem falls under multiple areas based on the type of use
cases. Architecture needs to account for vehicle, cloud, and communication between the
vehicle and cloud. Break down your application into smaller, independent microservices that
can be managed and scaled independently as needed.  By treating data as a product, package
it at the device (vehicle) by categorizing the data, before sending it to the cloud.
Classify the data based on frequency (for example, every 60 seconds), events, on-demand (for
example, during a failure event, send diagnostic logs). Architect your data processing
platform by decoupling the data collection from processing and offloading to cloud. In cloud
similar architecture approach needs to be in place to process data, before sending them to
downstream application consumption. 

Additional aspects to take into account on data:

- Timeliness of the data by minimizing latency (for example, 200 milliseconds or
  less).
- Data as current as possible (close to real time).
  - Primary goal – To support internal applications (for example, last location
    of vehicle, and fuel information.)
  - Vehicle state service – Last known values per vehicle

- Business intelligence data

      + Primary goal – To support the business for understanding the features use
       (for example, infotainment, driver usage patterns, and environmental data)

  When developing a connected mobility platform on AWS focusing on performance efficiency,
  there are essential architectural components and methods for performance data collection
  that should be identified and optimized. Let's break this down:

**[CMPERF\_BP1.1] Confirm critical components of the connected vehicle
platform**

The critical components of a connected vehicle platform into the simplified structure
of data plane, control plane, and consuming applications:

- **Data plane:** This is concerned with the movement of data
  throughout the system.
  - **In-vehicle data plane:**
    - **Data ingestion:** The vehicle collects real-time
      data from its sensors and systems.
    - **Edge processing:** The vehicle's onboard systems
      process this data locally, especially vital in areas with spotty connectivity.
      This can involve analyzing sensor data, determining the current vehicle status,
      or even making immediate decisions like automatic braking in emergencies.

  - **Cloud data plane:**
    - **Data ingestion:** This is where real-time data
      from vehicles is received, ingested, and stored in the cloud for further
      processing or analysis.

- **Control plane:** This component manages and coordinates
  the operations of the system, including ensuring the system's proper function and
  orchestrating event-driven processes.
  - **In-vehicle control plane:**
    - Directly interacts with the vehicle's hardware and
      systems. It takes action based on the processed
      data, such as adjusting vehicle settings or
      activating certain features.

  - **Cloud control plane:**
    - **Compute:** This involves running code in response
      to specific triggers, like changes in data or custom events. With a serverless
      architecture, this can be event-driven, scaling automatically based on demand.

- **Consuming applications:** These are interfaces and
  applications that end users (drivers, passengers, or vehicle owners) interact with.
  - **Mobile applications:** Drivers and users can access
    mobile apps to control and monitor their vehicles remotely. This includes functions
    like starting the vehicle remotely, locking/unlocking doors, checking oil levels,
    and scheduling starts to pre-warm or cool the vehicle.

**[CMPERF\_BP1.2] Enforce performance data collection**

To determine the best performing architecture, it's vital to
continuously collect, monitor, and analyze performance data.

- Collects and tracks metrics, collects and monitors log
  files, and sets alarms. It can be used to collect and
  track custom metrics.
- Get insights into the behavior of your applications,
  helping to understand how they are performing and where
  bottlenecks are occurring.
- Use cloud-native tools to review the resources health, performance, and
  optimizations recommendations.

###### Note

To derive cost per vehicle = Total cloud cost / Number of vehicles connecting to the
platform.

| CMPERF_2: Have you conducted performance tests for vehicle-to-connected<br>mobility platform communication across various connectivity methods, including LTE,<br>Wi-Fi, satellite, and scenarios with no connection? |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                                                                                       |

The performance of vehicle-to-connected mobility platform communication across different
connectivity methods is crucial for the seamless functioning of connected vehicles.

**Steps to test performance across various connectivity methods:**

**[CMPERF\_BP2.1] Define key metrics**

Decide what you'll measure, including latency, bandwidth, data consistency, and uptime,
across different connectivity methods.

Simulate environments:

- **LTE:** Mimic a mobile LTE connection with varying signal
  strengths.
- **Wi-Fi:** Test under various conditions, for example,
  stable home networks, and public Wi-Fi with many connected devices.
- **Satellite:** If possible, conduct tests in environments
  where only satellite connectivity is available, such as remote or maritime areas.
- **No connection:** Simulate scenarios where a vehicle loses
  connection. Monitor how much data is stored locally and then synced when connectivity is
  restored.

###### Caution

There will be storage limitations on the vehicle side and it is critical to
implement logic to persist critical data versus non-critical data.

**[CMPERF\_BP2.2] Check data consistency**

Ensure that data is consistent across various connection states, especially when
transitioning between them.

**[CMPERF\_BP2.3] Evaluate fail-over and redundancy. If one connection
method fails, does the system seamlessly switch to another available method?**

A successful connected vehicle platform not only requires
solid performance under various connectivity conditions but
also robust security, redundancy, and fail-over mechanisms.

| CMPERF_3: Have you evaluated the performance of the connected mobility platform<br>to ensure it can accommodate future vehicle demand projections? |
| -------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                    |

When designing a connected mobility platform, especially for performance efficiency,
it's crucial to evaluate its performance to ensure it can accommodate future vehicle demand
projections. When you are testing the performance and scalability of the platform, keep the
current capacity as 70% utilized, and 30% of capacity available for future needs (for new
vehicles load including data). Based on your vehicle demand projections, forecast 30% of the
infrastructure capacity is available with your vendors (cloud, marketplace, licensing) for
your workloads

**[CMPERF\_BP3.1] Evaluate performance and
scalability**

- **Assess current performance:** Determine the platform's
  current performance metrics, including throughput, latency, error rates, and capacity.
- **Load, stress, and scalability testing:** Simulate
  the expected number of vehicles and users to test how the system behaves under
  anticipated loads. This will help identify any bottlenecks or performance issues. Push
  the system beyond its expected limits. This helps to understand the system's breaking
  point and ensures that it fails gracefully. Determine if the system can scale out (add
  more instances) or scale up (add more resources to an instance) to meet increased
  demand. This is crucial for accommodating future growth.
- **Performance monitoring:** Continuously monitor system
  performance in real-time to identify and address issues before they impact users.
- **Future demand projections:** Use data analytics to
  project future vehicle demands based on current trends, market research, and other
  relevant factors.
- **Infrastructure evaluation:** Ensure that the underlying
  infrastructure (servers, databases, networks) can support the projected increase in
  demand.
- **Database optimization:** As the number of vehicles and
  data points increase, database performance becomes critical. Regularly optimize queries,
  indexes, and storage solutions.
- **Geographical distribution:** If the platform serves a
  global audience, consider distributing data centers geographically to reduce latency and
  improve performance for users worldwide.
- **Redundancy and failover:** Ensure that there are backup
  systems in place to take over if the primary system fails. This is crucial for
  maintaining uptime during unexpected events.
- **Feedback loop:** Regularly gather feedback from users and
  stakeholders to understand any performance-related issues they face and address them
  proactively.
- **Threshold limits:** In addition to load test,
  scalability, performance it is critical to understand the limits on the cloud side
  especially on compute resources, load balancer limits, data transfer across regions /
  3rd party providers. It's good practice to keep an eye on service limits to make sure
  monitoring is in place to alert and take proactive action.

| CMPERF_4: Have you assessed the performance of the connected mobility platform<br>when integrated with third-party vendor solutions? |
| ------------------------------------------------------------------------------------------------------------------------------------ |
|                                                                                                                                      |

Connected mobility platforms when integrated with third-party vendor solutions
evaluate and select a high-performing architecture that aligns with your organization's
goals for efficiency.

**[CMPERF\_BP4.1] Implement steps for performance
assessment**

- Map integration: Identify data flows, dependencies, and potential bottlenecks.
- Baseline metrics: Establish key performance metrics like latency, throughput,
  response time and error rates.
- Testing: Perform load and stress tests to simulate
  real-world traffic.
- Dependency checks: Assess software and hardware dependencies.
- Data integrity: Ensure data consistency and integrity between integrated systems.
- Security and compliance: Evaluate security protocols and ensure legal compliance.
  **[CMPERF\_BP4.2] Collect key performance
  metrics**

- Scalability: Can the system handle growth efficiently?
- Latency and throughput: Assess speed and capacity under different loads.
- Resilience: Evaluate fault tolerance and fail-over
  capabilities.
- Resource utilization: Monitor CPU, memory, and bandwidth usage.
- Interoperability: Assess ease of integration with other
  systems.
- Monitoring: Use analytics to identify bottlenecks or
  inefficiencies.
- Cost: Evaluate total cost of ownership (TCO).
  When assessing the performance of third-party integrations on a platform like the
  connected mobility platform, it's essential to employ a mix of monitoring, testing, and
  optimization tools. AWS offers a robust suite of services that can be leveraged for these
  purposes.

| CMPERF_5: Have you considered irregular data traffic patterns during the day or<br>within Regions and can the system handle sporadic traffic without impacting the<br>overall Service Level Agreement (SLA) and user or vehicle experience? |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                                                                                                             |

**[CMPERF\_BP5.1] Address irregular data traffic patterns and ensure
that the system handles sporadic traffic efficiently.**

These steps are crucial for a connected mobility platform or any large-scale system. AWS
offers various solutions and services that can help in managing these unpredictable
workloads without impacting the SLA, user, or vehicle experience.

**[CMPERF\_BP5.2] Take into account that mobility patterns can vary
significantly.**

When selecting an architecture, some factors to consider are peak commuting hours,
weekends, holidays, climatic conditions (summer versus winter), or even unexpected events
such as accidents and natural disasters.

- Dynamic scaling: Your system architecture should be able to scale up or down
  based on demand to handle irregular data traffic patterns. Cloud-based solutions often
  provide auto-scaling features to meet this need.
- Quality of Service (QoS): Implement QoS mechanisms to
  prioritize essential or time-sensitive data over less
  critical data, ensuring that crucial functions are always
  available.
- Caching and data aggregation: Use caching mechanisms to store frequently used
  data temporarily. Data aggregation techniques can help in reducing the amount of data
  that needs to be transmitted, thus relieving pressure on the system during peak loads.
- Rate limiting: Consider implementing rate limiting for non-essential or batch
  operations. This ensures that the system remains available for real-time and
  high-priority tasks.
- Redundancy and fail-over: Design the architecture with redundancy in mind to
  handle failures without affecting the SLA. Implement failover systems that can take over
  in case one part of the system becomes overloaded or fails.
- Traffic analysis: Use real-time monitoring and analytics to identify traffic
  patterns. This analysis can help in pre-scaling resources before a predicted
  high-traffic event.
- SLA monitoring: Implement tools that continuously monitor the system to ensure
  that it meets the agreed-upon SLAs, even during times of sporadic or high traffic.
- Geographical distribution: Consider deploying resources in multiple geographic
  locations if you expect irregular traffic patterns across different regions.
- User experience monitoring: Keep track of metrics that directly reflect user or
  vehicle experience such as app load times, navigation responsiveness, and real-time
  updates.
- Testing: Perform extensive stress and load testing
  simulating irregular traffic patterns to validate that the
  system can meet SLAs and provide a good user/vehicle
  experience under these conditions.
  By accounting for these factors in your architecture selection, you can better
  prepare the connected mobility platform to handle irregular and sporadic traffic patterns
  without adversely affecting performance or user experience.

| CMPERF_6: Have you taken into account any data regulatory requirements for<br>vehicles and tested that might affect performance? |
| -------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                  |

**[CMPERF\_BP6.1] Consider data regulatory
requirements**

- Data privacy and protection: Regulations like the General Data Protection
  Regulation (GDPR) in the European Union or the California Consumer Privacy Act (CCPA) in
  the United States mandate strict controls over personal data. Ensuring compliance can
  introduce additional processing steps, like encryption or anonymization, which might
  impact performance.
- Data localization: Some regulations require data to be stored in the same country
  or region where it's generated. This can affect the architecture of your platform,
  potentially introducing latency if data needs to be accessed from distant locations.
- Data retention and access: Regulations might dictate how long you can store data
  and who can access it. Implementing these controls can introduce additional database
  queries or checks, impacting performance.
- Data transmission: Secure transmission of data, SSL termination and off-loading
  especially in real-time applications, is crucial. Implementing robust encryption
  protocols (for example, mTLS) can introduce latency, affecting SLAs.
- Audit and logging: To ensure compliance, you might need to maintain detailed logs
  of all data accesses and changes. Writing and storing these logs can have performance
  implications.
- Data recovery and backups: Regulations might require you to have robust data
  recovery solutions in place. While this might not directly impact performance, it can
  affect SLAs, especially in terms of data recovery times.
- Third-party integrations: If your platform integrates with third-party services,
  you need to ensure they are also compliant with relevant regulations. Their performance
  and SLAs can directly impact your platform.
- Continuous monitoring and reporting: To ensure ongoing compliance, continuous
  monitoring and reporting mechanisms might be needed. These systems can introduce
  additional loads on the platform.
  **[CMPERF\_BP6.2] Take regulatory requirements into account as you
  define SLAs for a connected mobility platform**

These requirements can have a direct impact on performance and the Service Level
Agreements (SLAs) you set. For example, if data encryption introduces a delay, factor that
into your SLA. Similarly, if data localization introduces latency, that should be considered
when setting performance benchmarks.

| CMPERF_7: Have you considered a vehicle simulation tool to create artificial<br>load scenarios for better understanding and analyzing the performance metrics of the<br>system? |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                                                 |

**[CMPERF\_7.1] Simulate real-world scenarios to understand how the
system will behave under various conditions**

Using a vehicle simulation tool can be invaluable in this context. Using vehicle
simulation tools is an excellent approach to stress-test a connected mobility platform. By
simulating various load scenarios, you can evaluate how the system performs under different
conditions, anticipate potential bottlenecks, and optimize accordingly.

- Predicting system behavior: By simulating different vehicle behaviors and traffic
  scenarios, you can predict how the system will respond under different conditions. This
  can help in identifying potential bottlenecks or performance issues before they occur in
  a real-world scenario.
- Scalability testing: Connected mobility platforms need to handle a large number
  of vehicles, especially in urban environments. Using a simulation tool, you can
  artificially increase the number of vehicles to test the system's scalability.
- Real-time data processing: Many connected vehicle applications require real-time
  data processing, such as collision avoidance or traffic rerouting. By simulating these
  scenarios, you can ensure that the system can handle real-time data processing
  efficiently.
- Network load testing: Connected vehicles will continuously send and receive data.
  Simulating this can help in understanding the network load and ensuring that the
  infrastructure can handle it.
- Understanding edge cases: While typical scenarios are essential, it's also
  crucial to understand how the system behaves under edge cases. For instance, what
  happens if a large number of vehicles suddenly go offline? Or if there's a sudden surge
  in data transmission?
- Improving SLAs: By understanding the system's behavior
  under various scenarios, you can set more accurate Service
  Level Agreements (SLAs) and ensure that they are met.
- Cost optimization: Running simulations can also help in understanding the cost
  implications. For instance, if you're using cloud services, understanding the data
  transmission rates can help in predicting costs and optimizing them.

**[CMPERF\_BP7.2] Build your vehicle simulation tool to be compatible
with AWS**

When selecting a vehicle simulation tool, ensure its compatible with AWS, or consider
building a custom simulation environment that uses the full power of AWS services.

Whatever your choice, AWS provides a robust suite of tools and services that can be
harnessed to understand and optimize the performance metrics of the connected mobility
platform under various simulated load scenarios.

| CMPERF_8: Have you considered an edge inference simulation solution to<br>continuously test infer or predict based on the past data? |
| ------------------------------------------------------------------------------------------------------------------------------------ |
|                                                                                                                                      |

Edge inference is a crucial concept, especially for applications where real-time data processing is essential, such as autonomous vehicles, industrial IoT, and smart cities. By running inference at the edge (closer to where data is generated), you can reduce latency, save bandwidth, and respond quickly to local changes. Continuously testing the ability of edge devices to infer or predict based on past data is essential to maintain system reliability and performance. 

**[CMPERF\_BP8.1] Edge inference and simulation play a pivotal role in
the realm of connected mobility platforms**

This is especially important when focusing on performance efficiency. Edge computing allows
data processing to occur closer to the data source, such as a vehicle, rather than sending
it to a centralized cloud server. This approach can significantly enhance the performance
and responsiveness of the system.

- Latency reduction: One of the primary benefits of edge inference is the drastic
  reduction in latency. By processing data on the edge (for example, onboard a vehicle or
  a nearby edge server), the need to transmit data to a central server and wait for a
  response is eliminated. This is crucial for real-time applications like autonomous
  driving or collision avoidance.
- Bandwidth efficiency: Transmitting large volumes of raw data from vehicles to
  central servers can be bandwidth-intensive. Edge inference allows for initial processing
  and filtering of data, sending only essential information to the central server, thus
  saving bandwidth.
- Continuous testing and learning: An edge inference simulation solution can
  continuously test and adapt based on past data. This iterative process can help in
  refining algorithms and improving prediction accuracy over time.
- Real-world scenarios: Edge simulation tools can recreate real-world driving
  scenarios, allowing the system to test and infer based on historical data. This can be
  invaluable in understanding how the system would react in specific situations.
- Data privacy and regulatory compliance: Processing data on the edge can also
  address data privacy concerns. By analyzing and making decisions locally, sensitive data
  might not need to be transmitted or stored centrally, aiding in compliance with data
  protection regulations.
- Scalability: As the number of connected vehicles grows,
  central servers might become overwhelmed with data. Edge
  computing distributes the processing load, ensuring that
  the system remains scalable.
- Resilience and reliability: Edge inference provides a decentralized approach,
  ensuring that even if there's a failure in one part of the system, other parts can
  continue to operate independently.
- Integration with other systems: Edge devices can integrate with other local
  systems, such as traffic light controllers or local weather stations, to make more
  informed decisions.
  **[CMPERF\_BP8.2] Your edge inference simulation solution should
  provide a versatile approach to address many variables.**

When considering an edge inference simulation solution for a connected mobility
platform, it's essential to select a solution that can:

- Simulate various real-world scenarios.
- Continuously learn and adapt based on past data.
- Integrate seamlessly with the vehicle's onboard systems
  and other edge devices.
- Ensure data security and privacy.
- Simulate the expected volume and variety of data at the
  edge.
- Test the machine learning models' accuracy and speed under
  various conditions.
- Measure the latency and reliability of communication
  between edge devices and the central cloud or data
  centers.
  In conclusion, edge inference simulation is a forward-thinking approach that can
  significantly enhance the performance efficiency of a connected mobility platform. It allows
  for real-time processing, continuous learning, and adaptation, ensuring that the platform
  remains responsive, accurate, and efficient.

| CMPERF_9: Have you identified an appropriate communication protocol based on<br>use case? |
| ----------------------------------------------------------------------------------------- |
|                                                                                           |

**[CMPERF\_BP9.1] For vehicle-cloud communications, different
protocols must address your specific use case.**

- Pub-Sub protocols such as MQTT and AMQP can be used to exchange telemetry
  messages, command-control functions.
- HTTP or gRPC based protocol can be used to deliver over the air (OTA) updates.
- WebRTC protocol (RTMP) can be used to deliver video stream with real-time
  latency.
- SMS can be used for device wake-up, and run simple commands. 

The appropriate communication protocol often depends on the specific requirements of the use case. Here's a brief overview of common communication protocols and the typical use cases they serve:

- HTTP/HTTPS:
  - Use cases: Web applications, mobile applications, and many modern
    internet-based applications.
  - Advantages: Well-known, widely used, and supported.
    Secure version (HTTPS) available.

- MQTT (Message Queuing Telemetry Transport):
  - Use cases: Internet of Things (IoT) devices, real-time analytics, mobile
    applications, and communication in unreliable networks.
  - Advantages: Lightweight protocol with low bandwidth
    requirements. Supports QoS (Quality of Service)
    levels.

- WebSocket:
  - Use cases: Real-time web applications, gaming, chat applications, live sports
    updates.
  - Advantages: Provides full-duplex communication
    channels over a single TCP connection. More efficient
    than repeatedly opening new HTTP connections.

- AMQP (Advanced Message Queuing Protocol):
  - Use cases: Message-oriented middleware, cloud services, and brokered
    messaging.
  - Advantages: Supports message orientation, queuing, and
    routing.

- Payload efficiency
  - For optimal payload efficiency in a Connected Vehicle
    Platform, adopt compact data formats like Google
    Protocol Buffers (GPB) or MessagePack, which provide
    efficient serialization.
  - Send only changed or relevant data, employing
    compression algorithms like gzip for textual data, and
    utilizing delta encoding can minimize the data's size.

- Consider the trade-offs between data freshness and
  bandwidth utilization, tailoring strategies to the
  specific application's needs.

###### Note

Refer to [Resources](resources-perf.md "resources-perf.md") for links to
the mentioned protocols

**[CMPERF\_BP9.2] Choose a protocol based on the factors that apply
to your use case**

When choosing a communication protocol, it's important to assess the specific needs of
the use case and test the chosen protocol in realistic scenarios to ensure it meets the
requirements.

The choice of protocol will typically depend on:

- Data volume and frequency.
- Power and bandwidth constraints.
- Required communication range.
- Latency and real-time requirements.
- Security and privacy needs.
