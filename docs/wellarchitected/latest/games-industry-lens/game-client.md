# Game client

The _game client_ represents the software, hardware device, or both, that the player uses for
playing a game. The game client provides the software for translating the player’s inputs
into messages that are sent to a server for processing. It's also responsible for handling
the incoming responses from the server and rendering any outputs, such as graphics, to the
player. In real-time networked multiplayer games, the game client usually maintains a
persistent network connection to a game server for the duration of a gameplay session
to reduce network latency and minimize processing time. However, the game client might
also interact via representational state transfer (REST) with a game server or backend
services.
