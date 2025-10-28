# Define teams

The process of defining team size and structure is the same as with small matches,
but the way FlexMatch fills the teams is different. This affects how matches are likely
to look like when only partially filled. You may want to adjust your minimum team
sizes in response.

FlexMatch uses the following rules when assigning a player to a team. First: look for
teams that haven't yet reached their minimum player requirement. Second: of those
teams, find the one with the most open slots.

For matches that define multiple equally sized teams, players are added
sequentially to each team until full. As a result, teams in a match always have a
nearly equal number of players, even when the match is not full. There is currently
no way to force equally sized teams in large matches. For matches with
asymmetrically sized teams, the process is a bit more complex. In this scenario,
players are initially assigned to the largest teams that have the most open slots.
As the number of open slots become more evenly distributed across all teams, players
are slotted into the smaller teams.

For example, let's say you have a rule set with three teams. The Red and Blue
teams are both set to `maxPlayers`=10, `minPlayers`=5. The
Green team is set to `maxPlayers`=3, `minPlayers`=2. Here's
the fill sequence:

1. No team has reached `minPlayers`. Red and Blue teams have 10
   open slots, while Green has 3. The first 10 players are assigned (5 each) to
   the Red and Blue teams. Both teams have now reached
   `minPlayers`.
2. Green team has not yet reached `minPlayers`. The next 2 players
   are assigned to the Green team. The Green team has now reached
   `minPlayers`.
3. With all teams at `minPlayers`, additional players are now
   assigned based on the number of open slots. The Red and Blue teams each have
   5 open slots, while the Green team has 1. The next 8 players are assigned (4
   each) to the Red and Blue teams. All teams now have 1 open slot.
4. The remaining 3 player slots are assigned (1 each) to teams in no
   particular order.
