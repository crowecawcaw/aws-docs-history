# Design principles

In the cloud, there are a number of principles that can help you
create and run streaming media workloads. Keep these in mind as we
discuss best practices:

**Keep a Glass-to-Glass Perspective**
— From camera to viewer device, always consider how change impacts
the critical path of video delivery. For example, adding a
transcoding component can increase live latency, reduce video
quality, and introduce another point of failure in your workload. 

**Understand Your Audience** — Build
a deep understanding of your audience to inform business and
technical decision making. Use analytics to uncover the network
conditions, devices, and displays that your audience uses to
optimize for their unique consumption habits and prioritize playback
testing. Make sense of interaction data and proactively engage with
your audience through recommendations, personalization, and
notifications. Analyze viewership data and forecast usage to
validate the performance of all the components in the workflow at
peak scale. 

**Know your Content’s Value** — Start
your design with a shared understanding of the content value between
stakeholders. This will help you make decisions and tradeoffs around
overall costs, reliability objectives, performance, and content
protection schemes.

**Design for Disruption** — While
care should be taken to minimize failures, you should expect
disruption. In designing for disruption, start with a shared
reliability objective across the organization taking into account
the content value. Aligned to your reliability objective, build
redundancy into each component and the network links between them.
Also, seek to understand the areas of concern between components and
architect to gracefully handle failure or impairment of components.
