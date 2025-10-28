# Connected Mobility Lens

Publication date: **January 3, 2024** ([Document revisions](document-revisions.md "document-revisions.md"))

This paper describes the Connected Mobility Lens for the AWS Well-Architected Framework,
which enables you to review and improve your cloud-based architectures and better understand the
impact of design decisions. We present general design principles and specific best practices
aligned to the six pillars of the Well-Architected Framework.

## Introduction

_Connected mobility_ refers to the integration of technology into
transportation systems to improve the flow of traffic and enhance the overall mobility
experience. This includes the use of connected vehicles, smart infrastructure, and advanced
data analytics to help improve traffic flow, improve safety, and reduce emissions. Connected
mobility also includes the integration of various modes of transportation, such as cars,
public transit, bicycles, and pedestrian walkways, to create a seamless, efficient, and safe
transportation system.

This initial version of the Connected Mobility Lens primarily addresses scenarios related
to connected vehicles, with a focus on how each scenario impacts the architecture from the edge to
the cloud. A connected vehicle is defined as a vehicle that can communicate with other systems
outside of the vehicle. These scenarios and use cases are not exhaustive, but they encompass
common patterns in connected vehicles. We present a background on each scenario, general
considerations for the design of the system, and a reference architecture for customers to
consider for how the scenarios can be implemented.

## Lens availability

The Connected Mobility Lens is available as an AWS-official lens in the [Lens Catalog](../userguide/lens-catalog.md "../userguide/lens-catalog.md") of the [AWS Well-Architected Tool](../userguide/intro.md "../userguide/intro.md").

To get started, follow the steps in [Adding a lens to a workload](../userguide/lenses-add.md "../userguide/lenses-add.md") and select the **Connected Mobility Lens**.
