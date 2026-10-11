

# The Acquire journey
<a name="ca-acquire"></a>

Acquire is the app’s second major surface and the largest single body of view code in it. It is gated on tenant segment: a tenant whose configuration does not enable the Buy tab does not get one. The journey design, its personas and its commercial framing are documented in [The Customer Journey](the-customer-journey.md); this section covers what the client implements.

## Flows
<a name="ca-acquire-flows"></a>
+  **Buy landing** — the tab’s entry point, presenting discovery and any active offer.
+  **Discover** — browsing and narrowing the lineup, with a discovery-watch card for a shopper tracking something not yet available. See [Stage 1 — Discover / Find](discover-find.md).
+  **Configurator** — the build flow, described below.
+  **Upgrade** — an offer presented to an existing owner, with a trade-in score and an energy-savings projection where the comparison is between powertrains. Dismissals are remembered, so a declined offer does not reappear as though it were new.
+  **Lead capture** — hands an interested shopper to a dealer, which is the point at which the journey crosses into dealer systems.
+  **Order tracker** — post-order status, with supply-chain views covering order routing, delivery proposal and planning.

## Configurator step sequence
<a name="ca-acquire-configurator"></a>

The build flow is a step sequence rather than one long form, each step a separate view: category, model, variant, edition summary, interior style, color, accessories, finance, review, confirm, handover, and a success state. A lighter confirmation path exists for flows that do not require the full review.

Keeping the steps as discrete views is what makes the flow testable and reorderable per tenant. Finance is a step in the same sequence, but the terms it presents come from the platform — see [Stage 2 — Acquire / Finance](acquire-finance.md). The app does not compute offer terms, and mandatory disclosure text is presented as issued rather than paraphrased. This is the same boundary the voice path observes: the client renders decisions made by components whose output is authoritative.

## Catalog, reservations and leads
<a name="ca-acquire-catalog"></a>

The Acquire client reads a per-tenant catalog and writes reservations and leads, then reads order state back by order id. A catalog fallback exists so the flow remains navigable when the live catalog is unreachable — the alternative being a Buy tab that opens to nothing. An availability contract governs what the flow may assert about whether a configuration can actually be built, so the app does not promise a build it cannot support.

## Kiosk mode
<a name="ca-acquire-kiosk"></a>

The app can run as a showroom kiosk on a shared device, which introduces a privacy requirement the personal-device case does not have: everything a visitor entered must be gone before the next visitor. Kiosk state is therefore a single explicitly-scrubbed session, and the scrub is enforced by a test that enumerates every stored property on that state — so adding a field without clearing it fails the test rather than silently leaking the previous visitor’s input. The app also monitors whether the device is actually in a locked-down single-app mode, since a kiosk that can be navigated out of is not a kiosk.