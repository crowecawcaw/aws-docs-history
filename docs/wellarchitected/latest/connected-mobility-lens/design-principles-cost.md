# Design principles

In addition to the general Well-Architected cost optimization design principles, there are some design principles specific for cost optimization for connected mobility:

**Manage cost and business value tradeoffs:** Managing tradeoffs
between cost and other factors in connected mobility requires a careful balance between
short-term costs, such as installation, setup and subscription fees, and long-term costs, such
as data storage, management and infrastructure upgrades cost, cost-benefit analysis, and risk
management. For example, if you want to optimize for speed to market with low cost?

Choosing a solution solely based on cost without considering its business value can result
in increased operational cost overtime. Factors such as functionality, scalability, security,
speed of innovation, and going to market should be carefully evaluated along with cost to
select the right services/solutions. For example, a logistics company wants to implement a
connected mobility solution to track packages and optimize delivery routes. Implementing a
flexible architecture that can scale to accommodate growth and demand may come with an
increased short-term cost, however, it also comes with an increased business value creation
which will result in cost savings in long-term.

**Design the system to filter relevant data:** Connected mobility
applications could generate 10 exabytes of data per month. That's why it is important to
identify the data to be collected throughout your vehicle's fleets based on the corresponding
business use-case or security/compliance requirements. Identify opportunities to stop
collecting unnecessary data and consider collecting data targeted on business case and moving
to event-based collection instead of interval whenever possible.

**Evaluate where to process data:** Data transfer between vehicle
and cloud backend incur cost. Evaluation based on the use case through several
dimensions:

- The network cost private or public may have different cost implications. In the
  context of connected vehicles, a private network refers to a dedicated and secure
  communication network established specifically for the vehicles and related systems within
  a closed environment. This network is isolated from public networks and is designed to
  provide a controlled and reliable communication infrastructure for connected vehicle
  operations.

For example, imagine a fleet of autonomous delivery vehicles operated by a logistics
company. To ensure seamless and secure communication between these vehicles, as well as
with the central control system, the company sets up a private network. This network could
consist of dedicated cellular connections, Wi-Fi hotspots, or even a custom-built
communication infrastructure.

- The latency requirements to process the data. Latency refers to the delay between
  when data is generated or transmitted and when it is received and processed by the
  relevant systems. Here are two examples of latency requirements for processing data in
  connected vehicles:

**Emergency collision avoidance:**

Data source: Sensors on a vehicle detect an imminent collision with another vehicle.

Processing needs: The data from these sensors must be processed immediately to assess
the risk and decide on an appropriate action (for example, applying brakes, or changing
lanes).

Latency tolerance: In this scenario, extremely low latency is critical. A delay of
even a few milliseconds could be the difference between a successful collision avoidance and
an accident.

**Traffic signal optimization:**

Data source: The connected vehicle is equipped with technology to communicate with
traffic signals in real-time.

Processing needs: The vehicle's system sends data to the traffic signal control
system to request a green light or to adjust the signal timing for optimal traffic flow.

Latency tolerance: While not as critical as collision avoidance, low latency is still
important. Delays should be minimized to ensure smooth traffic flow and reduce unnecessary
stops.

In both cases, low latency is essential for the effective
operation of connected vehicle systems. It allows for timely
decision-making and actions, enhancing safety and efficiency
on the road.

- The compute capacity requirements where processing the data makes more sense, at edge
  in the vehicle or in the AWS Cloud. In this scenario, edge processing (in-vehicle) is
  critical for immediate decision-making and ensuring passenger safety. It allows each
  vehicle to operate autonomously, reacting swiftly to its environment.

On the other hand, cloud processing is beneficial for
higher-level, aggregate analysis. It can be used to optimize
routes across the entire fleet, predict traffic patterns, and
perform long-term planning. Overall, a combination of edge and
cloud processing can offer the best of both worlds, allowing
for real-time decision-making at the vehicle level while also
leveraging the cloud's computational power for broader fleet
optimization and analytics.
