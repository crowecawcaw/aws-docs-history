

# Cross-platform diagnostic sessions
<a name="rd-cross-platform-sessions"></a>

Deep repair work — invoking `SERVICE_ONLY` routines that require the vehicle on a lift, keys removed, or high-voltage systems isolated — is performed by a technician at a dealership. In this guidance, dealer-side operations run on a companion accelerator (referred to below as the **Dealer Management System** or DMS accelerator) that renders the same routine result payloads described in [Typed routine result contracts](rd-routine-results.md) using byte-identical copies of the six renderers. A drift-guard script in this repository verifies renderer parity across both codebases so the operator- and technician-facing surfaces cannot diverge silently.

![Diagnostic session detail: typed results for three routines. cell_balance_check reads outside tolerance with one cell at 3.762 V against a 62 mV maximum delta; pack_isolation_test passes at 738 megohms against a 100 megohm minimum; lamp_self_check is within tolerance with three lamps dim](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/rd-session-detail.png)


![Dispatch to service dialog: choose a service center and a priority](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/rd-dispatch.png)


The handoff is a single click. A fleet operator reading the Diagnostic Triage panel invokes **Dispatch to service** and picks a dealer; the platform generates a `sessionId` and posts it, together with the outbound-safe VIN and any prior `routinesRun[]` evidence, to the DMS-side dispatch endpoint. On the DMS side a repair order opens in `Draft`; when both `initiated_by` names a CMS-origin caller (either the `cms_booking` service identity or a `cms:` prefix on the human caller) and `evidence.sessionId` is present, the service view auto-opens on the Diagnostics tab. The technician’s subsequent `run_routine` invocations append to the same session log; the fleet operator sees the technician’s work in line, from the same triage panel that initiated the handoff.

Two seams stay deterministic across the handoff:

 **Dispatch VIN re-derivation.** The CMS-side `/api/dispatch` handler resolves the VIN from the vehicle record it holds, server-side, before the outbound DMS call. A client-supplied VIN in the request body is ignored — otherwise a caller with write access to fleet A could name a VIN in fleet B and open a repair order under someone else’s dealer relationship. Fleet-scope authorization is applied CMS-side before forwarding as defense in depth; the DMS-side `authorize_fleet_scope` control is the authoritative check.

 ** `SERVICE_ONLY` invoke gating.** A `dms-technician` may invoke a `SERVICE_ONLY` routine only when an active repair order for the VIN exists at one of the technician’s assigned dealers, with an RO status that means the vehicle is physically present on a lift (`InProgress` or `AwaitingParts`; a narrower set than the general "active" bucket, because physical presence is the whole justification for allowing the invocation). `platform-admin` composite-holders are excluded from this bypass — administrative authority cannot substitute for physical presence — and read-only viewer roles are excluded regardless of dealer scope.

The `dms-technician` Cognito group is provisioned on the CMS side and recognized by the DMS handler layer, so a single deployment step brings the group into existence for both surfaces. The full staging playbook, together with the exact provisioning commands, lives in this guidance’s operator deployment documentation.