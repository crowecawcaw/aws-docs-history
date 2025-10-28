# Operational analytics

Operational analytics refers to inter-disciplinary techniques and
methodologies that aim to measure and improve day-to-day business
performance in terms of increasing the efficiency of internal
business processes and improving customer experience and value.

Traditional analytics like Business Intelligence (BI) provide each
Line of Business (LOB) with insights to identify trends and take
decisions based on what happened in the past. 

But this is no longer sufficient. To deliver a good customer
experience, organizations must continually measure their workload
performance and quickly respond to operational inefficiencies for
a better customer experience.

By using operational analytics systems, they can initiate such
business actions based on the recommendations that the systems
provide. They can also automate the execution processes to reduce
the human errors. This makes the system go beyond being
descriptive to being more prescriptive and even being predictive
in nature.

On the other hand, IT infrastructures are becoming increasingly
distributed adding more complexity to the workloads in terms of
identifying the operational data that captures the system’s state,
characterize its behavior, and finally rectify potential issues in
the pipelines.

Several tools and methodologies have emerged that help companies
keep their systems reliable. Every system or application must be
instrumented to expose telemetry data that provides operational
insights in real or near real time.

The telemetry data can be of different form of signals: logs,
traces, and metrics. Traditionally this data came in the form of
logs that represent a record of an event happened within an
application, server or a system operation. It can be of different
types such as: application logs, security logs, system logs, audit
trails, and infrastructure logs. Logs are usually used in
troubleshooting and generating root-cause analysis for a system or
application failure at a specific point in time.

Trace signal captures the user request for resources as it passes
through different systems all the way to the destination and the
response back to the user. It indicates a causal relationship
between all the services being part of a distributed transaction.
Organizations used to develop their own trace mechanisms but it is
recommended to use existing tools that support a standard
trace-context propagation format. The trace-context holds the
information that links the producer of a message to its downstream
consumers.

Metric data provides a point-in-time measure of the health of the
system, such as resource consumptions in terms of CPU utilization.
Metric signals offer an overview of the overall system health
while reducing the manual effort to build these metrics and store
them. With metrics, system operators can be notified in real time
about anomalies in production environments and establish automated
recovery process in case of a recurrent incident.

The signals mentioned above have different ways to be instrumented
and provide different approaches to implement operational
analytics use cases. Therefore, organizations must have an
operational objective in mind from which they can work backwards
to identify what data output they need from their system, which
tool is better fit for their business and IT environment and
finally what insights are needed to better understand their
customers and improve their production resiliency.
