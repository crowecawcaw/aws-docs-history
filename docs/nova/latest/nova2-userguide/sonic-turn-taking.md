# Turn-taking controllability

Turn-taking is a fundamental aspect of natural conversation. Amazon Nova 2 Sonic
provides fine-grained control over when the AI takes its turn to speak through the
turnDetectionConfiguration parameter. This allows you to optimize the conversation
flow for different use cases, balancing responsiveness with accuracy. The
endpointingSensitivity parameter controls how quickly Amazon Nova 2 Sonic detects the end
of a user's turn and begins responding. This setting affects both the latency of
responses and the likelihood of interrupting users who are still speaking.

## API configuration

Configure turn detection sensitivity in the sessionStart event:

```

                {
    "event": {
        "sessionStart": {
            "inferenceConfiguration": {
                "maxTokens": 1000,
                "topP": 0.9,
                "temperature": 0.7
            },
            "turnDetectionConfiguration": {
                "endpointingSensitivity": "HIGH" | "MEDIUM" | "LOW"
            }
        }
    }
}

```

## Sensitivity levels

The endpointingSensitivity parameter accepts three values: HIGH, MEDIUM, and
LOW. Each level balances response speed against the risk of interrupting users
who are still speaking.

HIGH

Fastest response time, optimized for latency. Nova Sonic responds
as quickly as possible after detecting the end of speech. Pause
duration: 1.5 seconds. Best for quick Q and A, command-and-control
applications, and time-sensitive interactions.

MEDIUM

Balanced approach with moderate response time. Reduces false
positives while maintaining responsiveness. Pause duration: 1.75
seconds. Best for general conversations, customer service with
complex queries, and multi-turn discussions.

LOW

Slowest response time with maximum patience. Nova Sonic waits the
longest before responding, minimizing interruptions of users who
pause while thinking. Pause duration: 2 seconds. Best for thoughtful
conversations, elderly or speech-impaired users, and complex
problem-solving.

## Pause duration reference

| Sensitivity level | Pause duration (seconds) |
| ----------------- | ------------------------ |
| High (fast)       | 1.5                      |
| Medium            | 1.75                     |
| Low (slow)        | ~2.0                     |
