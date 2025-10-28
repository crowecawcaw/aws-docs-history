# Best practices

There are four best practice areas for reliability in the cloud:

- Foundations
- Workload architecture
- Change management
- Failure management

The probability of workload failure increases as the number of
components in your system increases. Media industry people
generally agree with AWS CTO Werner Vogels’ often-quoted
statement that “Failures are a given and everything will
eventually fail over time.... This is a given, whether you are
using the highest-quality hardware or lowest cost components”,
thus we build our workloads to operate despite single points of
failure. Your objective is to maintain the viewing experience
when failure or degradation does occur. As we’ve seen from the
scenarios, the delivery of high-quality streaming media requires
a considerable amount of complexity that often crosses business
stakeholders. Keep a glass-to-glass perspective, from content
production to delivery, and consider how any single component
failure could impact the quality of playback experience.

In this section, we provide best practices that you can use to
evaluate and improve the reliability of your streaming media
services.
