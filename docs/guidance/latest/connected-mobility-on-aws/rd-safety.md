

# Safety envelope for remote actuation
<a name="rd-safety"></a>

UDS `0x14` (Clear Diagnostic Information) and `0x31` (RoutineControl) change the state of the vehicle. Some routines — an ABS pump cycle, an injector cut-out test, an evaporative-emissions purge — are physically unsafe if executed at road speed or with the engine unexpectedly running. This is where the transport-layer design ends and the application-layer safety envelope begins.

The guidance’s pattern is a **routine safety class** on every actuation-capable operation:


| Class | Preconditions | Remotely invocable | Enforcement point | 
| --- | --- | --- | --- | 
|  `INERT`  | Vehicle connected | Yes — reads, self-tests, identity queries | UI affordance, cloud allow-list, sidecar allow-list | 
|  `STATIONARY`  | Speed = 0, engine on, transmission in park or neutral | Yes, from an authorised bay-side operator | Cloud-side check at execution time against vehicle-state cache; sidecar re-checks against live vehicle state immediately before dispatch | 
|  `SERVICE_ONLY`  | Facts the platform cannot observe (vehicle on a lift, key removed, battery disconnected) | No | Refused at cloud-side catalog lookup; sidecar refuses defence-in-depth | 

Two invariants hold this envelope together.

 **Preconditions are enforced in executable code, not in prose.** A source comment stating "do not run this off a moving vehicle" is not a control. An assertion in the cloud handler that rejects a `STATIONARY` invocation when the vehicle-state cache reports speed greater than zero is a control. An assertion in the sidecar that re-checks CAN-observed vehicle state before dispatching `0x31` is a defence-in-depth control. Both are required, because the cloud check can be bypassed by a compromised credential and the sidecar cannot be bypassed by anything short of firmware compromise.

 **Verdict narration is verbatim.** If a diagnostic result carries a safety verdict — for example, "stop driving, engine at critical temperature" — that phrase is narrated verbatim to the operator, sourced from a deterministic catalog, never summarised. This matters especially when a language model is added to the read path: an LLM may summarise conversational output, but summarisation of a safety verdict is a behaviour change disguised as UX. The guidance separates the deterministic result — the catalog-derived phrase — from any conversational surface that describes it.

## Rate limiting: protect the resource, not the label
<a name="rd-rate-limiting"></a>

The vehicle’s CAN bus has physical bandwidth limits, and ECU diagnostic response windows are bounded. A rate limiter that caps "full-scan requests" but not "single-ECU requests" creates a bypass: nine sequential single-ECU reads impose the same CAN load as one nine-ECU scan.

The pattern is to rate-limit the underlying resource, not the label. Tokens are accounted per ECU-read, so N single-ECU reads cost N tokens whether they arrive as one request or nine. This lives in the sidecar, which observes the actual bus traffic.