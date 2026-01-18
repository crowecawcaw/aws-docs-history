# How Session Protection

Works

When you request a playback URL with a valid playback token, IVS creates an authorized
session and returns playlist and segment URLs that are unique to that session. These
subsequent URLs do not contain a visible token parameter, but they are still tied to the
authorized session.

Mechanisms are in place to mitigate sharing of session-bound URLs while still allowing
legitimate usage patterns (e.g., mobile users switching between WiFi and cellular). If
IVS detects unnatural usage, the authorized session is revoked and playback stops for
all clients using that session.
