

# Client-side triage timing
<a name="ca-triage-client"></a>

The app watches incoming telemetry and asks the platform to classify a condition when a threshold is crossed. The classifier is authoritative; the client’s only decision is **when to ask**.

Two details make this safe. The client’s thresholds are deliberately slightly looser than the classifier’s — asking at a lower value than the one that would classify — so a borderline condition is submitted for classification rather than filtered out before anyone evaluates it. And the asking is debounced, so a fast telemetry stream produces one classification request rather than a flood.

The result is that the app cannot suppress a classification by being conservative, and cannot manufacture one by being eager. See [The triage classifier](triage-classifier.md) for the rules themselves, including the P0 outcome whose instruction to the driver is narrated verbatim on every surface that carries it.