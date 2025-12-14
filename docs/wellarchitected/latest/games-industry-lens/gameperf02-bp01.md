# GAMEPERF02-BP01 Select a home Region that is near your

players

For an initial game launch, you should determine where to deploy
infrastructure based on discussions with your business
stakeholders, such as publishing teams who determine where the
game is expected to be made available to players, and where they
are focusing their pre-launch marketing and advertising efforts.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Your business stakeholders should also have mechanisms to
stimulate demand to gain a better understanding of player
reception and viability. For example, these teams will have
mechanisms such as game pre-orders, marketing events and
campaigns, public email lists for players to register interest
before launch, and other approaches to establish relevant signals
to determine where the game will likely have the most players at
launch. The game may also use a regional roll out strategy that
includes play test and soft-launch phases to determine regional
player demand.

[Select
a home Region](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/") that is near your player base and your
developers and has the AWS services and features you need to host
your game. The home RSegion will be where the game backend
services will run, and it may also run game servers. Evaluate a
home Region based on services supported, connectivity to edge
locations, proximity to failover Regions, and number of
Availability Zones. If you are using a Local Zone, consider the
parent Region is sometimes located in a different geographic area.
As an example: Santiago, Chile Local Zone us-east-1-scl-1a has N.
Virginia us-east-1 as its parent Region even though it is
geographically closer to Sao Paulo sa-east-1.

### Implementation steps

- Identify deployment Regions based on player demand signals
  from pre-launch activities like pre-orders, marketing
  campaigns, and interest registrations.
- Choose a home Region close to the primary player base and
  developers, making sure it supports required AWS services,
  edge locations, and failover Regions.
- Evaluate Local Zones carefully, considering that the parent
  Region may differ geographically from the location of the
  Local Zone.
