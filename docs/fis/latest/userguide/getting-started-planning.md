# Planning your AWS FIS experiments

Fault injection is the process of stressing an application in testing or production
environments by creating disruptive events, such as server outages or API throttling. From
observing how the system responds, you can then implement improvements. When you run
experiments on your system, it can help you to identify systemic weaknesses in a controlled
manner, before those weaknesses affect the customers who depend on your system. Then you can
proactively address the issues to help prevent unpredictable outcomes.

Before you get started running fault injection experiments using AWS FIS, we recommend that
you familiarize yourself with the following principles and guidelines.

###### Important

AWS FIS carries out real actions on real AWS resources in your system. Therefore,
before you get started using AWS FIS to run experiments, we strongly recommend that
you first complete a planning phase and a test in a pre-production or test
environment.

###### Contents

- [Basic principles and guidelines](#planning-basic-principles "#planning-basic-principles")
- [Experiment planning guidelines](#planning-experiment-guidelines "#planning-experiment-guidelines")

## Basic principles and guidelines

Before starting experiments with AWS FIS, take the following steps:

1. Identify the target deployment for the
   experiment — Start by identifying the target deployment. If
   this is your first experiment, we recommend starting in a pre-production or test
   environment.
2. Review the application architecture —
   You must ensure that you have identified all of the application components,
   dependencies, and recovery procedures for each component. Begin with reviewing
   the application architecture. Depending on the application, refer to the [AWS
   Well-Architected Framework](../../../wellarchitected/latest/framework.md "../../../wellarchitected/latest/framework.md").
3. Define steady-state behavior — Define
   the steady-state behavior of your system in terms of important technical and
   business metrics, such as latency, CPU load, failed sign-ins per minute, number
   of retries, or page load speed.
4. Form a hypothesis — Form a hypothesis of
   how you expect the system behavior to change during the experiment. A hypothesis
   definition follows this format:

If `fault injection action` is performed, the
`business or technical metric impact` should not exceed
`value`.

For example, a hypothesis for an authentication service might read as follows:
"If network latency increases by 10%, there is less than a 1% increase in sign-in
failures." After the experiment is completed, you evaluate whether the application
resiliency aligns with your business and technical expectations.

We also recommend following these guidelines when working with AWS FIS:

- Always start experimenting with AWS FIS in a test environment. Never start with
  a production environment. As you progress in your fault injection experiments,
  you can experiment in other controlled environments beyond the test
  environment.
- Build your team’s confidence in your application resilience by starting with
  small, simple experiments, such as running the
  **aws:ec2:stop-instances** action on one target.
- Fault injection can cause real issues. Proceed with caution and make sure that
  your first fault injections are on test instances so that no customers are
  affected.
- Test, test, and test some more. Fault injection is meant to be implemented in
  a controlled environment with well-planned experiments. This allows you to build
  confidence in the abilities of your application and your tools to withstand
  turbulent conditions.
- We strongly recommend that you have an excellent monitoring and alerting
  program in place before you begin. Without it, you won’t be able to understand
  or measure the impact of your experiments, which is critical to sustainable
  fault injection practices.

## Experiment planning guidelines

With AWS FIS, you run experiments on your AWS resources to test your theory of how an
application or system will perform under fault conditions.

The following are recommended guidelines for planning your AWS FIS experiments.

- Review outage history — Review the
  previous outages and events for your system. This can help you to build up a
  picture of the overall health and resiliency of your system. Before you start
  running experiments on your system, you should address known issues and
  weaknesses in your system.
- Identify services with the largest impact
  — Review your services and identify the ones that have the biggest impact
  on your end users or customers if they go down or do not function correctly.
- Identify the target system — The target
  system is the system on which you will run experiments. If you are new to AWS FIS
  or you have never run fault injection experiments before, we recommend that you
  start by running experiments on a pre-production or test system.
- Consult with your team — Ask what they
  are worried about. You can form a hypothesis to prove or disprove their
  concerns. You can also ask your team what they are not worried about. This
  question can reveal two common fallacies: the sunk cost fallacy and the
  confirmation bias fallacy. Forming a hypothesis based on your team’s answers can
  help provide more information about the reality of your system’s state.
- Review your application architecture —
  Conduct a review of your system or application and ensure that you have
  identified all of the application components, dependencies, and recovery
  procedures for every component.

We recommend that you review the AWS Well-Architected Framework. The
framework can help you build secure, high-performing, resilient, and efficient
infrastructure for your applications and workloads. For more information, see
[AWS
Well-Architected](https://aws.amazon.com/architecture/well-architected/ "https://aws.amazon.com/architecture/well-architected/").

- Identify the applicable metrics — You
  can monitor the impact of an experiment on your AWS resources using Amazon CloudWatch
  metrics. You can use these metrics to determine the baseline or "steady state"
  when your application is performing optimally. Then, you can monitor these
  metrics during or after the experiment to determine the impact. For more
  information, see [Monitor AWS FIS usage metrics using Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
- Define an acceptable performance threshold for your
  system — Identify the metric that represents an acceptable,
  steady state for your system. You will use this metric to create one or more
  CloudWatch alarms that represent a stop condition for your experiment. If the alarm is
  triggered, the experiment is automatically stopped. For more information, see
  [Stop conditions for AWS FIS](stop-conditions.md "stop-conditions.md").
