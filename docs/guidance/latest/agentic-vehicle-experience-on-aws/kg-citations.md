

# Citations as a trust pattern
<a name="kg-citations"></a>

Grounded responses are only as useful as the caller’s ability to trust them. AVX implements a structured citation pattern as a first-class feature of every KB-grounded response:
+ Every passage retrieved by the `knowledge()` tool carries a `source` attribute — the document name and (where available) section heading from the Knowledge Base metadata.
+ The supervisor includes these source references in the synthesized response. For voice sessions, the supervisor narrates the source name verbally ("according to the TSB for this issue…​"). For text, web, and Connect Chat sessions, the response JSON includes a `citations` array with the document names of all passages used.
+ The web UI reasoning panel displays the citation list and tool-call trace, making the grounding data path auditable to service managers and quality reviewers without requiring access to CloudWatch logs.

This citation pattern is important for three reasons. First, it prevents the supervisor from presenting retrieved content as its own generated knowledge — callers and service managers can verify the source of a diagnostic or policy statement. Second, it enables quality monitoring: if a citation is wrong or stale, the feedback path leads directly to the source document in the KB, which the operator can update without code changes. Third, for regulated content such as NHTSA recalls and warranty policy, having a named source for every compliance-relevant statement reduces operational and legal exposure.

The `citations` field in the `/assistant/chat` response follows the structure in the API contract:

```
{
  "result": "P0420 is a catalyst system efficiency below threshold ...",
  "sessionId": "session_1234567890_abc123456",
  "classification": "P2",
  "vin": "1AAAA00A0AA000123",
  "citations": ["dtc-P0420.md", "tsb-2024-EN-0298.md"]
}
```

When no KB Retrieve call is made (LTM-only response), the `citations` array is empty or absent; this is the expected behavior for the LTM-only personas and should not be treated as a failure.