

# Deterministic Seams and Guards
<a name="ap-deterministic-seams"></a>

Some components in AVX are deterministic by design. Agents narrate the output of these components verbatim. They do not modify the values.


| Seam | Why deterministic | 
| --- | --- | 
| Triage classification (P0 stop-driving) | P0 is a safety determination, not an LLM judgment. The supervisor does not allow override. When an Agent 2 Finding involves a P0, the headline carries the classifier’s exact phrase. Mutation-tested: replacing "pull over immediately" with softer wording fails the test. | 
| DMS warranty verdict | The DMS is the authority on coverage decisions. Agent 3 carries the exact verdict text — "Your repair is approved" or "Your repair is denied." The agent may add cost or next-steps context but does not rephrase the verdict. | 
| Order and payment state machine | Money and legal state transitions run in Step Functions. The LLM narrates current state; it does not advance the state machine. | 
|  `finance_qualify` / `payment_initiate`  | Partner APIs compute the result. The LLM surfaces the qualification tier and rate range; it does not derive them. | 
|  `offers_lookup` \+ `disclosure_txt`  |  `disclosure_txt` is narrated verbatim. No LLM generates offer terms or disclosure text. | 
| ADP prediction models | Statistical inference runs in ADP. ADP emits "left front tire, 8,000 km to threshold, slow leak indicated." Agent 2 reasons about what to do — coverage check, bundling, slot availability, timing. The prediction is not re-derived. | 
| Trade-in valuation (Agent 4) | Any monetary figure in a `concierge.*` Finding is an indicative range, not an offer. `disclosure_txt` is mandatory and verbatim. When the partner comps seam is mocked, the surface omits the monetary figure (M14 mock-provenance guard). | 
| Fleet recall matching and safety text | Which vehicles a recall affects (`CONFIRMED` or `POPULATION`) is ADP SQL, and severity and grounding come from a fixed band table, so the model cannot add or remove a grounding. The catalog’s safety text goes into `disclosure_txt` byte for byte, and the assistant reads it word for word. | 
| Stop-driving faults on fleet vehicles | A fault code’s fleet band comes from ADP’s fault-code catalog. A `p0` fault always raises a grounding item and carries the catalog’s directive verbatim on both the booking and the grounding item. | 
| Money in fleet recommendations |  `estimated_value_usd` is a formula over evidence values: a monthly cost saving, DMS’s recoverable warranty amount, or a move’s net benefit. No tool the model calls has a numeric field. | 
| Engineering campaign drafts | A draft recall’s population rule, remedy and notice text come from the fault pattern, the failure mode and fixed templates. No model text goes into a recall notice, and a second engineer approval issues it. | 

Each seam has a corresponding test that mutates the deterministic output — widens an IAM resource, swaps the verdict phrase, omits the disclosure — and confirms the test fails. A seam enforced only by a prompt is not reliably enforced.

Several AVX outputs are produced by deterministic components and must be narrated exactly as the component produced them. The agent receives the output and says it. These boundaries are enforced by mutation-tested assertions. A test that stays green when the boundary is removed asserts presence, not the property.

## Triage P0 stop-driving phrase
<a name="triage-p0-stop-driving-phrase"></a>

The `triage()` tool classifies a fault using a decision table. When the result is `p0`, the tool returns the verbatim stop-driving phrase. Every Finding with `severity == "p0"` carries that phrase in `headline` and `detail` without shortening or substitution. Tier 1 narrates it aloud and the card displays it.

 **Mutation test**: replace the phrase with "exercise caution" in the narration path; the P0 narration test fails.

## Warranty coverage verdict
<a name="warranty-coverage-verdict"></a>

Agent 2 reads the DMS warranty verdict for a repair (`approved`, `declined`, `under_review`) and narrates it verbatim. The agent does not substitute "pending review" for "declined" or offer an interpretation of the verdict’s likelihood of changing.

 **Mutation test**: soften "declined" to "under review" in the narration; the coverage-verdict test fails.

## Mock-provenance guard (M14)
<a name="mock-provenance-guard-m14"></a>

Every evidence entry carries `provenance: live | mocked | absent`. When any entry is `mocked` — for example, a trade-in comparable from an unavailable partner feed — the system refuses to render a monetary figure derived from that evidence, or displays it with an explicit "illustrative" watermark. The agent does not present a mocked-data estimate as live.

 **Mutation test**: inject `provenance="mocked"` into a monetary-output path and remove the guard; the mock-provenance test fails.

## Verbatim disclosure text (M8)
<a name="verbatim-disclosure-text-m8"></a>

Any Finding that surfaces a monetary figure carries `disclosure_txt`. This field contains the exact disclosure copy that accompanies the figure — authored by the business, not generated by the LLM. Tier 1 narrates `disclosure_txt` verbatim and the app displays it unchanged.

## Agent 3 as sole discount authority
<a name="agent-3-as-sole-discount-authority"></a>

Only Agent 3 (the Ownership Cost and Coverage Advocate) may produce a Finding with `discount_applied` set. Agent 2 may identify that a discount may apply and route to Agent 3; it does not emit `discount_applied` on its own. This keeps Agent 3 as the single accountable point for loyalty and coverage decisions.

 **Guard**: any Agent 2 Finding with `discount_applied` set fails a schema assertion.

## Order and payment state machine
<a name="order-and-payment-state-machine"></a>

The order state machine — `finance_qualify`, `payment_initiate`, and the Acquire step sequence — is deterministic. The agent narrates what each step returned. Credit qualification is the partner API’s decision; `payment_initiate` calls the partner API directly. The agent does not skip steps, reverse them, or soften a payment-declined result.

## Channel API separation
<a name="channel-api-separation"></a>

No Tier 2 agent module calls a channel API. No Tier 2 agent module imports an executor. These rules are stated here because they are encoded in the test suite — failing either constraint causes a test to fail, not just a code review comment.