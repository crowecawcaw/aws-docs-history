# Hosting resource customizations

This section provides advanced options for configuring and managing your Amazon GameLift Servers infrastructure to meet specific performance, cost, and operational requirements.
In particular, the topics in this section describe how you can customize your Amazon GameLift Servers managed hosting resources to best fit your game and your players.

Some of the decisions you want to consider:

- Where to deploy hosting resources for your players? Gameplay latency is a major factor in
  selecting your fleet's geographic locations, but there are other factors that vary
  by location, including resource type availability and cost.
- What EC2 instance types will best support your game? Choose from available instance types that
  use the best combination of compute architecture, memory, storage, and networking
  capacity.
- What size of instance type do you need? Choose an instance type size based on the resource requirements
  (memory and CPU) of your game server software and other factors.
- Should your fleet use On-Demand or Spot Instances? Consider whether you can take advantage of
  lower Spot pricing, and whether Amazon GameLift Servers sufficiently mitigates the chance of Spot
  interruptions to your game sessions.
- How do you want your game server software to run on each fleet instance? The runtime configuration tells Amazon GameLift Servers
  what server software to run and how.
- For container fleets, does the default configuration work for your game? Amazon GameLift Servers
  does a lot of the work for you to optimize your container fleet configurations, but
  you can customize most configuration settings.
