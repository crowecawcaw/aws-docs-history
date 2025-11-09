# EUCPERF04-BP02 Identify all user types, and deploy required fleet types and instance

types as needed

Not all end users necessarily require the same level of performance. Users who perform
routine tasks such as data entry, document review, or customer service may need a low level
of performance, while content or video editors, investment and securities traders, or
graphics users may require performant desktops. Other users may require moderate levels of
performance as their workloads may be unpredictable.

It's important to have a high degree of familiarity with the applications that need to
be delivered using Amazon WorkSpaces Applications in terms of their compute resource requirements. By
understanding core compute requirements such as the amount of memory, CPU, network
bandwidth, latency, and disk space that applications require, you can determine the optimum
fleet type and instance sizes required for the workload.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Determine the compute requirements for your applications.

- Assess your users' applications and tasks, and deploy a sufficient level of fleet
  types and instance types as are needed.
- Monitor the resulting user feedback to verify that performance meets their needs
  without overprovisioning their instance types.
- If performance or productivity suffers for various users, increase the
  performance of their instances. This can be achieved by using larger instances with
  more CPU or in the case of WorkSpaces Applications using a different instance family that
  provides higher clock speed for CPU cores.
