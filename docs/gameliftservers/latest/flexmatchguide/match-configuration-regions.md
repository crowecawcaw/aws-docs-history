# Choose a location for the

matchmaker

Decide where you want matchmaking activity to take place and create your
matchmaking configuration and rule set in that location. Amazon GameLift Servers maintains ticket pools for
your game's match requests where they are sorted and evaluated for viable matches.
After making a match, Amazon GameLift Servers sends the match details for game session placement.
You can run the matched game sessions in any location that's supported by your hosting solution.

See [FlexMatch supported AWS Regions](match-regions.md "match-regions.md") for the locations where you can
create FlexMatch resources.

When choosing an AWS Region for your matchmaker, consider how location might impact
performance and how it can optimize the match experience for players. We
recommend the following best practices:

- Place a matchmaker in an location that is close to your players and
  your client service that sends FlexMatch matchmaking requests. This approach
  decreases the latency effect on your matchmaking request workflow and makes it
  more efficient.
- If your game reaches a global audience, consider creating matchmakers in
  multiple locations and routing match requests to the matchmaker that is closest to
  the player. In addition to boosting efficiency, this causes ticket pools to form
  with players who are geographically near each other, which improves the
  matchmaker's ability to match players based on latency requirements.
- When using FlexMatch with Amazon GameLift Servers managed hosting, place your matchmaker and the
  game session queue that it uses in the same location. This helps to minimize
  communication latency between the matchmaker and queue.
