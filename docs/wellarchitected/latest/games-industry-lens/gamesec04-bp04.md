# GAMESEC04-BP04 Restrict access to content with digital rights

management (DRM) solutions

Consider restricting access to your game content by using strong
encryption tools such as a
[digital
rights management (DRM)](https://aws.amazon.com/marketplace/solutions/media-entertainment/drm/ "https://aws.amazon.com/marketplace/solutions/media-entertainment/drm/") solution. This type of solution can
be used to encrypt your private content and distribute the
decryption keys to authorized players.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

DRM solutions are recommended in situations where you want to
allow players to download game content early, but you do not want
them to be able to access or play the content until a
predetermined time. For example, this is common in situations
where players are allowed to pre-order a game and configure their
game client to automatically begin downloading the encrypted files
early. This strategy verifies that the game is downloaded and
ready to be played once the game has been officially
released. After the game is released, the player's game client can
request decryption keys from the DRM backend solution so that it
can decrypt the previously downloaded files and begin playing the
game. 

DRM systems are also used to block unauthorized re-distribution
and manipulation of games after they have been downloaded and
installed by an authorized player. DRM systems require integration
with the origin for exchanging encryption keys and authorizing
players to retrieve the decryption key. Commercial DRM providers
offer a range of solutions with features and support for different
devices.

### Implementation steps

- Use DRM solutions to encrypt private game content and
  distribute decryption keys to authorized players.
- Enable pre-download of encrypted files for pre-ordered
  games, unlocking access with decryption keys at release
  time.
- Integrate DRM systems with the origin to manage encryption
  keys and block unauthorized redistribution or manipulation
  of content.
