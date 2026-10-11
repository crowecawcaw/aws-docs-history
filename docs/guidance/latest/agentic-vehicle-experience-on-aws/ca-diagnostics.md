

# Diagnostics and instrumentation
<a name="ca-diagnostics"></a>

The voice path is instrumented so that one log capture yields a complete causal timeline — state transitions with their reasons, connection and teardown, tool results, watchdog fires, credential exchange, and the UI events that triggered each. Each subsystem uses a distinct prefix so a capture can be filtered to one concern.

Two practical notes. The logging uses the older `NSLog` call rather than a modern structured logger specifically so the lines reach the unified system log, which is what makes them visible in a capture from an app launched outside a debugger. And predicate-based log filters do not capture these lines from an app started that way — filter the stream on the prefix instead. Reaching for a predicate and finding nothing is a common false negative, not evidence that instrumentation is missing.

The instrumentation observes fixed rules, verified by security review:
+ Token bodies, secret keys and session tokens are never logged. Token **lengths** are, which is enough to distinguish an empty token from a present one.
+ Access key identifiers are logged as a short prefix only — always the same prefix for temporary credentials, so no entropy is disclosed.
+ Error response bodies are logged on failure only. A successful credential exchange logs the body length, never the body.

This discipline is why the voice path can be debugged from a customer-supplied log without that log becoming a credential disclosure.