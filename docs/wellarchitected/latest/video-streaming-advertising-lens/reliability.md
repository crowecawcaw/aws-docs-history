# Reliability

The reliability pillar encompasses the ability of a workload to
perform its intended function correctly and consistently when it's
expected to. This includes the ability to operate and test the
workload through its entire lifecycle. This section provides
in-depth, best practice guidance for implementing reliable workloads
on AWS.

The reliability pillar provides an overview of design principles,
best practices, and questions. You can find implementation guidance in the
[Reliability
Pillar whitepaper](../reliability-pillar/welcome.md "../reliability-pillar/welcome.md").

## Design principles

There are three key dimensions that define Reliability in the
advertising industry: latency, uptime, data security. While this
is similar to the range of criticality in transactional systems
found in the financial industry, there are unique expectations of
resiliency for SSPs, exchanges, and DSPs. We will use RPO and RTO,
which are established in the reliability pillar of the
Well-Architected Framework

## Definitions

- **Recovery Point
  Objective (RPO):** The maximum amount of data loss
  allowed as the result of a system failure expressed in units
  of time.
- **Recovery Time
  Objective (RTO):** The maximum amount of time allowed
  for a system to resume its normal operations after a failure.
- **Uptime:** A measure of system
  reliability, expressed as the period of time a machine,
  typically a computer, has been continuously working and
  available.
- **Microservices:** An
  architectural pattern that arranges an application as a
  collection of loosely-coupled, fine-grained services
  communicating through lightweight protocols. One of its goals
  is to enable teams to develop and deploy their services
  independently.
