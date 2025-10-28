# 1 Overview

An AWS IoT ExpressLink qualified module is a hardware connectivity module that communicates
with a host processor by means of a serial interface (UART) and allows it to quickly and
securely access AWS IoT Core and its services. In so doing, an ExpressLink module offloads
complex and undifferentiated workloads, such as authentication, device management,
connectivity, and messaging, from the application (host) processor. ExpressLink modules were
conceived after discussions with microcontroller vendors, OEMs, and module makers regarding
the complexity and repetitiveness of migrating existing hardware and software designs to new
or different MCUs and RTOSs. They enable a scalable migration for millions of embedded
applications to cloud-connected applications.

## 1.1 Goals

The top-level goals are to:

- Accelerate time to market for IoT devices.
- Ease the transition to cloud connected solutions:
  - Reduce the skill gap required for cloud-connected embedded
    applications.
  - Allow OEMs to migrate existing designs by adding ExpressLink to existing
    applications with minimal modification to the existing application code.

- Dramatically reduce the resources embedded devices require to connect to AWS IoT
  Core and publish and subscribe to topics, regardless of the connectivity solution
  chosen (Wi-Fi, ethernet, or cellular):
  - An abstract API does not reveal (leak) implementation details to the
    customer application.
  - Configuration parameters (implementation dependent) are easily isolated.
  - Requires minimal hardware connections with defined pinouts (two wire
    minimum).
  - Provides stateless module communication (command mode only, single
    configuration).

- Support a hardware root of trust-based unique identity that allows for an optimal
  out-of-the-box experience and high-volume quick manufacturing, even when using
  untrusted Contract Manufacturers, by taking advantage of the AWS Multi Account
  Registration feature.
- Provide a quick evaluation experience out-of-the-box without requiring an AWS
  account.
- Simplify onboarding with an additional late binding option.
- Offer easy updates over the air (and over the wire) so the module and host processor
  can ensure security throughout the life of the product.
- Connect to standard AWS IoT Core services without additional cost and allow for
  heterogeneous fleets.
