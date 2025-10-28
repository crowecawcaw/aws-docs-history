# Customize your Amazon GameLift Servers EC2 managed fleets

The topics in this section outline some of the customizations you can make when building a hosting
solution with Amazon GameLift Servers managed EC2 fleets.
They provide guidance and best practices for creating and configuring a fleet to host your game.

Required decisions include:

- Where should you deploy hosting resources? Latency is a major factor in selecting your fleet's locations,
  but cost also varies by location.
- What EC2 instance type will best support your game? Choose from instance types that are
  available in all your fleet locations to use the best combination of compute
  architecture, memory, storage, and networking capacity.
- What size of instance type do you need? Choose an instance type size based on the resource requirements
  (memory and CPU) of your game server software and other factors.
- Should your fleet use On-Demand or Spot Instances? Consider whether you can take advantage of lower Spot pricing given
  how Amazon GameLift Servers guards against the chance of game sessions interruptions.
- How do you want your game server software to run on each fleet instance? The runtime configuration tells Amazon GameLift Servers
  what server software to run and how.

###### Topics

- [Choose compute resources for a managed fleet](gamelift-compute.md "gamelift-compute.md")
- [Manage how Amazon GameLift Servers launches game servers](fleets-multiprocess.md "fleets-multiprocess.md")
