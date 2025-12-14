# GAMESEC03-BP01 Determine your approach to identify and control

player access to your game's environment and resources

This decision is influenced by your player acquisition and
monetization strategy, player experience, and other factors such
as the existing capabilities that might be provided by your game
publishing partners. For example, a game might require purchases
and require a player to create a user profile to associate
real-money payment methods with their account.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Alternatively, a game may desire to reduce the barrier to entry
for first-time player experiences by removing the need to create a
user account before playing the game, thereby improving the chance
that a player will try the game for the first time. Typically,
games will implement one or more combinations of player identity
and access management approaches for their game.

**Unauthenticated or anonymous
access**

This access level is useful in situations where a game does not
require a player to create a new user account or link with their
identity on social networks and gaming systems. This is the
simplest and quickest way for a player to start playing a game and
is particularly useful in mobile games where a game developer may
want to reduce the barrier to entry for the initial experience. 

In this access scenario, if you want to identify usage from the
game installation, you can program the game client to generate and
store a unique identifier onto the player's device. This unique
identifier is used to identify the player across game sessions on
their device and allow analytics reporting on usage over
time. Later, if a player chooses to create an account, you can
associate their new user account with their previously-generated
unique identifier. This will link their new player identity to
their historical usage, which might include stats and game
achievements. 

If a player does not eventually create and link an account, the
device that the player uses to interact with the game can be
uniquely identified, but recoverable information about the player
is not collected and stored. Thus, if the player breaks or loses
their device, the previous stored data associated with the device
is also lost and might not be recoverable.

**Authentication with username and
password**

A game may allow players to create their own user accounts with a
username and password that are stored within the game's
backend. This might occur when a game developer is collaborating
with a game publisher who already has an existing player account
system that the developer can integrate with. Alternatively, a
developer who publishes their own games might want to simplify the
player experience by allowing players to create a single user
account for access across the games that they publish.

**Authentication and account linking with
third-party social networks and gaming systems**

It is common for online games and games with social features to
provide third-party identity provider federation to simplify the
player experience. Instead of asking players to create a username
and password combination to authenticate, you can use identity
federation to allow players to authenticate using their
third-party accounts with social networks and gaming systems. This
login process simplifies the sign-in and registration experience
for players. It also provides a convenient alternative to
mandatory account creation and a frictionless method for players
to access games. 

For game developers, a federated login process can offer a
streamlined player verification workflow. It may also provide a
more reliable way to manage player data that is used for
personalization. This is because you do not need to ask players to
provide you with certain data that they likely have already
provided to the third-party identity provider. Additionally, these
systems provide integration with additional social features such
as the ability to link players with their friends.

### Implementation steps

- Use unauthenticated or anonymous access to reduce barriers
  for first-time players by generating a unique device
  identifier to track usage and enabling account linking
  later.
- Implement username and password authentication for dedicated
  user accounts, using existing player account systems or
  creating a unified experience across games.
- Integrate third-party identity providers for federated
  authentication, simplifying login processes and enabling
  access to social features and personalization data.
