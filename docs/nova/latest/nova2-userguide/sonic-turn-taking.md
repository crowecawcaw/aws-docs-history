# Turn-taking controllability

Use turn-taking controllability to adjust how Amazon Nova 2 Sonic detects when a
user has finished speaking. This feature helps optimize the conversational
experience for different use cases and user speaking patterns.

## API configuration

The `endpointingSensitivity` parameter controls how quickly Nova
Sonic detects when a user has finished speaking. This parameter is set in the
`RequestStartEvent` during session initialization.

## Sensitivity levels

HIGH

Detects pauses quickly, enabling faster responses but may cut off
slower speakers

MEDIUM

Balanced sensitivity for most conversational scenarios
(recommended default)

LOW

Waits longer before detecting end of speech, better for thoughtful
or hesitant speakers
