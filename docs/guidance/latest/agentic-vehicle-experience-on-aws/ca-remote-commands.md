

# Remote commands
<a name="ca-remote-commands"></a>

Remote commands go to the CMS commands API, a separate API Gateway from the CMS main API, whose Cognito authorizer trusts the same user pool the app signs into.

 **The controls sheet is catalog-driven.** The app fetches the command catalog and renders what the platform advertises for that vehicle, rather than hardcoding a control set. Familiar commands — locking all doors, remote start, preconditioning, flashing hazards, locating the vehicle, opening the charge door, and panic mode — get dedicated iconography; anything else renders with a neutral glyph rather than a misleading one. A platform that gains a command does not need an app release for it to appear.

 **Sending is not confirming.** A successful send means the command was accepted for publication, not that the vehicle performed it. The app presents the command as in-flight and confirms separately: either from command history, where the command reaches a succeeded state, or — for commands that change vehicle state — from live state arriving over the telemetry WebSocket. Treating the send response as confirmation would tell a driver their doors are locked when the vehicle is out of coverage.

 **Scope is the driver’s own vehicle.** Commands act on the vehicle assigned to the signed-in driver, and command history shows the commands that driver issued rather than every command recorded against the vehicle, so an operator’s or technician’s activity is not surfaced as the driver’s own. The authorization decision is the API’s; the app hides what the user cannot do, but does not decide it.

The vehicle-side path — protobuf encoding, dual-path publishing, and actuation limits — is documented in the Connected Mobility guidance rather than here, since the commands API and its transport belong to that platform.