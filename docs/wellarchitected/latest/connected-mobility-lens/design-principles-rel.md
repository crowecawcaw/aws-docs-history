# Design principles

In addition to the overall Well-Architected Framework design principles, the following
are the design principles for reliability for connected mobility:

- **Design for failure and resiliency:** It's essential to plan
  for resiliency on the vehicle-based telematics unit. Depending on your use case,
  resiliency might entail robust retry logic for intermittent connectivity, ability to roll
  back firmware updates, ability to fail over to a different networking protocol for
  critical message delivery, ability to perform a factory reset.
- **Implement synthetic monitoring:** Simulate the vehicles
  behavior by implementing digital clone of the in-vehicle software communicating with the
  connected mobility application. The monitoring must share no cloud resources with the
  connected mobility backed that is monitoring to being able to assess impairments of the
  cloud part.
- **Plan for poor network connectivity:** Vehicles must
  tolerate connectivity or backend errors. Connectivity is subject to continuous
  interruption given the position of the vehicle, like tunnels, underground parks or remote
  locations with low to none signal. Cloud backend applications must tolerate vehicles that
  often transition between being connected and disconnected. Availability of connected
  services and user experience on disconnection is the core aspect and basic reason of this
  platform's existence.
- **Invalidate commands that have passed their usability
  threshold:** Connected mobility platforms enable the communication of commands
  to the vehicle. The commands are intended to be run on the vehicle at the requested or
  configured time, generally in near real time. At times, the state of the vehicle or the
  backend system may be such that this communication fails to execute in expected timeframe.
  Due to this delay the command may either have been overridden by next command, are no
  longer relevant or may be not safe enough to execute. For example, a door unlock command
  might not be safe enough or relevant to run after few minutes of delay. Based upon the use
  case and the nature of the commands, the backend system should invalidate the commands if
  they are stale or passed their usability threshold.
- **Design for idempotent systems:** There can be situations
  where the connected mobility system might receive multiple messages that are identical
  thus causing an overload. Although the complexity of implementation would be higher,
  idempotency reduces the risks of system overload, failure, and reduced availability.
- **Aggregate for simplicity but be prepared to dive deep into logs for
  causal analysis:** Connected mobility platforms collect data at high velocity
  and volume. Vehicle manufacturers use various mechanisms to aggregate this data for
  specific vehicle or fleet over a time. Based upon the use case, a deep dive into the
  system and application logs may be needed to troubleshoot issues, determine performance
  bottlenecks, execution steps, or to meet compliance regulations.
