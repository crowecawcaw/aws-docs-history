

# Operator surface: unified Diagnostic Triage panel
<a name="rd-operator-surface"></a>

The vehicle-detail **Diagnostic Triage** panel is the primary operator entry point for the remote-diagnostics stack. It unifies four surfaces the earlier UI split across separate buttons:
+  **DTC catalog verdicts** — every DTC code rendered against a live event-catalog lookup. An uncatalogued code renders with no fabricated severity — never a placeholder default — so operators can distinguish a benign uncatalogued code from a red-flagged one.
+  **Powertrain-correct UDS/SOVD scans** — the underlying sim (and, on real vehicles, the ECU roster resolver) uses a per-vehicle powertrain profile (gasoline, diesel, hybrid, electric) so a battery-electric vehicle is never asked for engine or EVAP-system DTCs. `read_dtcs` with `components: ["*"]` returns only the ECUs the profile actually addresses.
+  **ECU identity and version drift** — `read_identity` responses feed a compare view that flags where a vehicle’s on-vehicle part numbers or software versions differ from the fleet’s expected baseline.
+  **Safety-classified routines disclosure** — routines are grouped by their server-derived safety class (see [Safety envelope for remote actuation](rd-safety.md)) so the operator sees what can be run here (`INERT`), what needs the vehicle stationary (`STATIONARY`), and what is handled downstream at a dealership (`SERVICE_ONLY`).

 `SERVICE_ONLY` routines render **no invocation control at all** — not a disabled button. A disabled button is still a hover-tooltip UI; an absent control makes the affordance boundary structural. Refusal reasons, when a routine is refused server-side, render verbatim from the deterministic catalog — no client-side summarisation, no fabricated placeholder text.

The fleet-operator persona reads the vehicle’s diagnostic state on this panel and decides whether to keep the vehicle running (issue a `clear_dtcs` if the underlying repair is complete and attested) or dispatch it to a technician (see [Cross-platform diagnostic sessions](rd-cross-platform-sessions.md)). Repair work itself is not performed from this surface.