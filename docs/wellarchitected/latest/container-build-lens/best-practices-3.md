# Best practices

The performance efficiency pillar includes the ability to use computing resources
efficiently to meet system requirements, and to maintain that efficiency as demand changes
and technologies evolve. In the context of containers, there are two different aspects of
performance: the build-time performance for your container image, and the runtime
performance. In this section, we’ll focus on build-time performance in order to reduce the
time that is necessary to create a container image from a Dockerfile. Reducing the
build-time of a container image has a huge impact on developer productivity, and it reduces
the amount of time that is necessary to roll out new versions of your application to
production. Optimizing the performance at runtime has a direct impact on customer
experience, latency, and costs, but is outside the scope of this lens. The following
guidance is in addition to the best practice guidance found in the [Performance Efficiency Pillar whitepaper](../performance-efficiency-pillar/welcome.md "../performance-efficiency-pillar/welcome.md").

###### The following are best practice areas for performance efficiency in

the cloud:

- [Selection](selection.md "selection.md")
- [Review](review.md "review.md")
- [Monitoring](monitoring.md "monitoring.md")
- [Tradeoffs](tradeoffs.md "tradeoffs.md")
