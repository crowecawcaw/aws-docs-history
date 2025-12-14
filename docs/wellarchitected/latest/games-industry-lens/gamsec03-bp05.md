# GAMESEC03-BP05 Provide an option for players to set up

multi-factor authentication (MFA) on their accounts

Player accounts can be an asset to bad actors, particularly in
games that support in-game currency and purchases. Due to the
pervasiveness of player account hacking and social engineering
attacks, provide players with the option to enhance the security
of their accounts by configuring multi-factor authentication
(MFA).

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

When a player attempts to access their account by using MFA, a
temporary code is sent to their email address, phone number, or a
purpose-built multi-factor authentication mobile app. To
successfully authenticate, the player must then enter the code
into the login system within a limited time frame. 

MFA can also be used to help protect accounts that are attempting
to authenticate from a new geo-location, accounts that have been
flagged by player support for potential malicious activity, and
even for accounts that have not logged into the game for an
extended period. 

For example, Amazon Cognito user pools can
[configure multi-factor
authentication](../../../cognito/latest/developerguide/user-pool-settings-mfa.md "../../../cognito/latest/developerguide/user-pool-settings-mfa.md") on user directories.

### Implementation steps

- Enable multi-factor authentication (MFA) to enhance player
  account security.
- Use temporary codes sent via email, phone, or MFA apps to
  verify account access.
- Apply MFA for new geo-locations, flagged accounts, or
  accounts with extended inactivity.
