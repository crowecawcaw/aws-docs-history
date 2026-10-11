

# Integrating medical coding into your workflows
<a name="mc-integration"></a>

Medical coding returns structured, evidence-linked codes, so you can place it wherever coding happens in your revenue cycle. Three integration patterns are common.


| Pattern | When codes are generated | Who reviews | Best for | 
| --- | --- | --- | --- | 
| Point of care coding | As the clinician finalizes the note | The clinician confirms the codes; a coder handles exceptions | Coding at the source and fixing documentation gaps before the note is signed | 
| Computer-assisted coding (CAC) | After the note is signed, in the coding queue | A coder validates each suggestion against its evidence | Reducing time per chart and coding backlog in back-office operations | 
| Autonomous coding | After the note is signed, in an automated pipeline | Coders review exceptions and low-confidence encounters; the rest go through audit sampling | Organizations that measure accuracy on their own encounters and want to reduce manual coding | 

**Important**  
During the gated preview, a qualified coder should review every suggested code before claim submission. Use the preview to measure accuracy on your own encounters and to design the review policy you will use in production.

**Topics**
+ [Point of care coding](#mc-int-point-of-care)
+ [Computer-assisted coding](#mc-int-cac)
+ [Autonomous coding](#mc-int-autonomous)
+ [Design considerations](#mc-int-design)

## Point of care coding
<a name="mc-int-point-of-care"></a>

Chain medical coding after [ambient documentation](ambient-documentation.md). The visit conversation produces a clinical note, and your application submits that note to medical coding to produce codes. Before signing, the clinician sees the suggested codes and E/M level next to the evidence for each. If the documented MDM doesn’t support the level of care delivered, the clinician can correct the documentation while the encounter is still fresh, instead of answering a coder query days later.

![Point of care coding: your application submits the ambient documentation note to medical coding.](https://docs.aws.amazon.com/connecthealth/latest/userguide/images/medical-coding-point-of-care-chain.png)


## Computer-assisted coding
<a name="mc-int-cac"></a>

Submit finalized notes to medical coding and pre-populate each encounter in the coder’s worklist with the suggested code set. Coders review the evidence for each code and accept, edit, or reject it. They no longer have to read the full note to build the code set.

![Computer-assisted coding: suggested codes go to a coder worklist for review before claim submission.](https://docs.aws.amazon.com/connecthealth/latest/userguide/images/medical-coding-cac-workflow.png)


## Autonomous coding
<a name="mc-int-autonomous"></a>

Route each encounter by the confidence score on each suggested code and by your organization’s rules:
+  **Reduced review.** Encounters inside a policy you define, such as specific visit types, E/M levels, and code families with high confidence, can move forward with reduced review. Use this path only after you measure accuracy on your own encounters.
+  **Coder review.** New patients, higher E/M levels, modifiers, low-confidence codes, and any suggestion your policy flags go to a coder, who accepts, edits, or rejects each code.
+  **Audit sampling.** Keep a standing audit sample of encounters that moved forward with reduced review, send it to coder review, and track accuracy over time.

Both paths end in claim submission.

![Autonomous coding: routing rules send codes to reduced review or coder review, with audit sampling.](https://docs.aws.amazon.com/connecthealth/latest/userguide/images/medical-coding-autonomous-workflow.png)


Set your routing policy from accuracy you measure on your own encounters, not from general benchmarks. Your organization stays responsible for the accuracy and compliance of submitted claims.

## Design considerations
<a name="mc-int-design"></a>
+  **Code final documentation.** Submit signed or finalized notes. Coding a draft that later changes causes rework.
+  **Use one `clientToken` per encounter.** Derive it from your encounter identifier so that a retry can’t create a duplicate job. See [Idempotent submissions](mc-how-it-works.md#mc-idempotency).
+  **Always send context.** Patient status, encounter type, and demographics change which codes are correct. See [How context affects code selection](mc-inputs.md#mc-input-context-impact).
+  **Keep the evidence.** Store the evidence references with the final codes to keep an audit trail for compliance reviews and payer audits.
+  **Capture coder decisions.** Record each accept, edit, and reject. These decisions are your accuracy signal, and your AWS account team can use them to adapt the model to your code distribution.