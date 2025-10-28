# Two security agents on same

underlying host

Amazon EC2 instances can support multiple types of workloads. When you configure automated
security agent on an Amazon EC2 instance, the same EC2 instance might have another security agent
through EKS.

## Overview

Consider a scenario where you have enabled Runtime Monitoring. Now, you enable the automated
agent for Amazon EKS through GuardDuty. You have also enabled the automated agent for Amazon EC2. It
may happen that the same underlying host gets installed with two security agents - one
for Amazon EKS and the other for Amazon EC2. This could result in two security agents running
inside the same host, collecting runtime events and sending them to GuardDuty, and
potentially generating duplicate findings.

## Impact

- When there is more than one security agent running on the same host, your
  account may experience double the amount of CPU and memory processing needs. For
  information about the CPU and memory limits for each resource type, see [Prerequisites](runtime-monitoring-prerequisites.md "runtime-monitoring-prerequisites.md") for that
  resource.
- GuardDuty has designed the Runtime Monitoring feature in a way that even if there is an
  overlap of two security agents collecting runtime events from the same
  underlying host, your account will only be charged for one stream of runtime
  events.

## How GuardDuty handles multiple

agents

GuardDuty detects when two security agents are running on the same host and designates
only one of them to be the security agent that actively collects runtime events. The
second agent will consume minimum system resources so as to prevent any impact to the
performance of your applications.

GuardDuty considers the following scenarios:

- When an EC2 instance falls under the scope of both Amazon EKS and Amazon EC2 security
  agents, the EKS security agent takes priority. This will apply only when you use
  the security agent v1.1.0 or above for Amazon EC2. Older agent versions will continue
  to run and collect runtime events because older agent versions are not affected
  by prioritization.
- When both Amazon EKS and Amazon EC2 have GuardDuty managed security agents and your Amazon EC2
  instance is also SSM managed, both the security agents will be installed at the
  host level. Once the agents are installed, GuardDuty decides which security agent
  will keep running. When both the security agents are running, eventually only
  one of them will collect runtime events.
- When the security agents associated with both EC2 and EKS run at the same
  time, GuardDuty might generate duplicate findings during the overlap period
  only.

This can happen when:

    + Security agents for both EC2 and EKS are configured through GuardDuty
     (automatically), or
    + Your Amazon EKS resource has automated security agent.

- When the EKS security agent is already running, if you deploy the EC2 security
  agent manually on the same underlying host and meet all the prerequisites, GuardDuty
  might not install a second security agent.
