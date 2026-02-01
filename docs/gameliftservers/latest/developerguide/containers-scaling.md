# Scale Amazon GameLift Servers container fleets

One of the most challenging tasks with game hosting is scaling capacity to meet player
demand without wasting money on resources that you don't need. In a managed container fleet, you scale
your fleet capacity by adding or removing fleet instances.

When you create a new fleet, Amazon GameLift Servers sets the fleet's desired capacity to one instance and
deploys one instance in the fleet's home region. For a multi-location fleet, Amazon GameLift Servers deploys one
instance to the home region and to each remote location. After the fleet status reaches
`ACTIVE`, you can raise the desired capacity to raise or lower the desired
capacity to scale down.

You can use Amazon GameLift Servers scaling features to change capacity manually or set up automatic scaling
based on player demand:

- Set up automatic scaling with target tracking. See [Target-based auto scaling](fleets-autoscaling-target.md "fleets-autoscaling-target.md").
- Manually change the capacity of your fleet. See [Manually set capacity for an Amazon GameLift Servers fleet](fleets-updating-capacity.md "fleets-updating-capacity.md").
  When scaling a container fleet, consider how adding or removing instances impacts the
  fleet's capacity to host game sessions and players.

- Game sessions per instance
  - Each game server process running on an instance represents the capacity to host one
    game session.
  - Use this formula to calculate the number of game sessions that run concurrently on a
    container fleet instance:

  ```
  [Game sessions per instance] = [# of game server processes per game server container] * [# of game server container groups per instance]
  ```

  If your container architecture runs one game server process concurrently in the game
  server container, then game sessions per instance equal the number of game server
  container groups per instance.

      - For game server container groups per instance, call [DescribeContainerFleet](../apireference/API_DescribeContainerFleet.md "../apireference/API_DescribeContainerFleet.md") to get the
       `GameServerContainerGroupsPerInstance` or `MaximumGameServerContainerGroupsPerInstance` value.

- Players per instance

      + You decide the number of player slots to allow in each game session. Depending on
       how your hosting solution handles game session placement, you might define players per
       game session in your matchmaking configuration or in your calls to start a game session
       placement.
      + Use this formula to calculate the number of players that can play your game
       concurrently on a container fleet instance:



      ```
      [Players per instance] = [# of game sessions per instance] * [# of player slots per game session]
      ```

  To get the current total capacity of a container fleet, call [DescribeFleetCapacity](../apireference/API_DescribeFleetCapacity.md "../apireference/API_DescribeFleetCapacity.md") or [DescribeFleetLocation Capacity](../apireference/API_DescribeFleetLocationCapacity.md "../apireference/API_DescribeFleetLocationCapacity.md") to get the number of game server container groups in
  the fleet. Active groups are those that are currently hosting game sessions. Idle groups are
  ready to host a new game session. Multiply these values by the number of server processes per
  game server container group.
