# General design principles

The [Well-Architected Framework](../framework/welcome.md "../framework/welcome.md") identifies a set of general design principles to help
customers design in the cloud for building and managing connected mobility workloads.

**Improving the customer experience with data integrity and data
privacy**

Customer experience and confidence in technology and processes used by the automotive
manufacturer are key considerations in buyer decisions. According to a [recent report](https://www.jdpower.com/business/press-releases/2023-us-mobility-confidence-index-mci-study "https://www.jdpower.com/business/press-releases/2023-us-mobility-confidence-index-mci-study"):

######

“Consumers are not comfortable sharing personal information which results from
uncertainty as to what information is being shared; how the information is being used; whether
it is being stored; and, if so, stored securely.”

**Selecting synchronous versus asynchronous communication
pattern**

The selection of a [synchronous
versus asynchronous pattern](https://www.youtube.com/watch?v=RfvL_423a-I "https://www.youtube.com/watch?v=RfvL_423a-I") depends upon your use cases. Request/Reply use cases, such
as vehicle state management, require responses to be given synchronously. Other use cases, such
as remote commands, require asynchronous communication. The asynchronous design pattern should
always be considered first before switching to other patterns of communication. Asynchronicity
leads to loosely coupled systems that are scalable, failure tolerant, and have evolvable
architecture. Systems that must absorb vehicle traffic spikes and can accommodate asynchronous
processing can improve reliability by allowing clients to quickly release resources by using
message queues. A robust tracking mechanism should be implemented for the requests received,
responses delivered and failures.

**Event-driven architecture enables the global scale**

[Event-driven architecture (EDA)](https://aws.amazon.com/blogs/architecture/best-practices-for-implementing-event-driven-architectures-in-your-organization/ "https://aws.amazon.com/blogs/architecture/best-practices-for-implementing-event-driven-architectures-in-your-organization/") is better suited for building global scale
distributed microservice-based applications. EDA can bring agility, cost optimization, and
reliability to the connected mobility implementations. EDA requires an enterprise-wide strategy
in designing data contracts for the event producers and consumers. As all the event-driven
applications are distributed, it's important to use tracing to understand and observe service
dependencies and diagnose any bottlenecks and issues in the application.

**Optimizing the frequency of data transferred from vehicle to
cloud**

According to a study by McKinsey & Company, by 2030, [95% of the cars shipped globally](https://www.mckinsey.com/industries/automotive-and-assembly/our-insights/unlocking-the-full-life-cycle-value-from-connected-car-data "https://www.mckinsey.com/industries/automotive-and-assembly/our-insights/unlocking-the-full-life-cycle-value-from-connected-car-data") will connect to the internet, generating 10 exabytes
of data per month. Vehicle manufacturers have been addressing the data synchronization challenge
between vehicle and cloud in different ways. Some companies are opting for low frequency rather
than high frequency, while others are using off-peak hour scheduling of low priority data.
[Intelligent data filtering](https://aws.amazon.com/blogs/iot/generating-insights-from-vehicle-data-with-aws-iot-fleetwise-part1/ "https://aws.amazon.com/blogs/iot/generating-insights-from-vehicle-data-with-aws-iot-fleetwise-part1/"), sensor and event prioritization, and
compression can also lead to lower data transfer charges and better resiliency in managing the
data.

The biggest challenge with delaying the offloading of data is the buffer size in the
vehicle. A recommended approach is to [use rule- or condition-based data collection](../../../iot-fleetwise/latest/developerguide/create-campaign-console.md "../../../iot-fleetwise/latest/developerguide/create-campaign-console.md") schemes. A promising approach to address
these issues is the application of machine learning (ML) powered, [context-aware
communication](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8778710 "https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8778710") that exploits the dynamics of the communication channel. This approach
allows the scheduling of delay-tolerant transmissions in an opportunistic way, which increases
the transmission efficiency with regard to data rate, packet loss probability, and energy
consumption.

**Alignment with local regulations in handling data transfer, storage,
and usage**

Connected vehicles operate in diverse geographies so it is essential to abide by the
regulations to build customer trust and for privacy compliance. For more information, see [Security design principles](design-principles-sec.md "design-principles-sec.md").

**Don't guess about your performance requirements**

The connected mobility scenarios generally have a time bound pattern of traffic generation.
The [observability tools](https://aws.amazon.com/blogs/mt/observability-using-native-amazon-cloudwatch-and-aws-x-ray-for-serverless-modern-applications/ "https://aws.amazon.com/blogs/mt/observability-using-native-amazon-cloudwatch-and-aws-x-ray-for-serverless-modern-applications/") can give a trend of historic traffic based on
location, time and use cases. Certain features, such as remote commands to start the vehicle and
set climate control, can have high traffic during peak hours of the day and peak seasons. It is
recommended to have [automated scaling](https://aws.amazon.com/autoscaling/ "https://aws.amazon.com/autoscaling/") of
services to accommodate periodic and seasonal shifts in customer usage and demands.
