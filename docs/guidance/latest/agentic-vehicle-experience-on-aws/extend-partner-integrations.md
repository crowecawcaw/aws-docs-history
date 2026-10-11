

# Partner Integrations
<a name="extend-partner-integrations"></a>

AVX exposes integration points across six partner domains. In each case the pattern is the same: an agent tool wraps a partner API call and returns a structured result; the supervisor synthesizes the spoken or written response from that result. The tool signature is thin and deterministic — the LLM never constructs API calls directly.


| Domain | Example partner types | Integration pattern | 
| --- | --- | --- | 
| Digital commerce | CRM and e-commerce platforms | REST webhook from `book()` tool on confirmed appointment or quote acceptance; event payload includes STAR `ServiceRequestAdd` envelope | 
| Payments | Payment processors, open-banking APIs | Agent tool for payment initiation; tool validates amount and reference before making the API call; never passes raw card data through the LLM | 
| Document processing | Repair order and invoice platforms | Lambda invoked from `book()` or `escalate()` to generate structured repair-order documents from the STAR `ServiceRequestAdd` payload | 
| Contract management | Warranty and contract platforms | Agent tool for warranty and contract lookup; returns coverage summary that the supervisor narrates; used by `service_advisor` and `technician` personas | 
| Credit decisioning | Credit bureaus and scoring platforms | API call from a finance persona tool; result is a pre-qualification summary, never raw bureau data; gated on explicit customer consent | 
| Subscription management | Connected-service subscription platforms | Webhook from `book()` on subscription change events (activation, upgrade, cancellation) | 

## Implementing a partner tool
<a name="extend-partner-tool-pattern"></a>

The following example shows a payment-initiation tool. The same structure applies to any partner domain — replace the API call and return shape:

```
# agents/supervisor/tools/payment_initiation.py
import logging
import httpx
from strands import tool
from agents.supervisor.session import SessionContext
from agents.supervisor.config import Config

log = logging.getLogger(__name__)

def make_payment_initiation_tool(ctx: SessionContext, config: Config):
    @tool
    def payment_initiation(
        amount_usd: float,
        description: str,
        service_request_number: str,
    ) -> dict:
        """Initiate a payment for an approved service estimate.

        Only call this after the customer has explicitly confirmed the
        amount and given consent. Never call speculatively.
        """
        if amount_usd <= 0:
            return {"error": "amount_usd must be positive"}

        # Partner API call — replace with actual endpoint and auth
        try:
            resp = httpx.post(
                config.payment_api_endpoint,
                json={
                    "amount": int(amount_usd * 100),   # cents
                    "currency": "USD",
                    "description": description,
                    "reference": service_request_number,
                    "tenant_id": ctx.tenant_id,
                },
                headers={"Authorization": f"Bearer {config.payment_api_key}"},
                timeout=5.0,
            )
            resp.raise_for_status()
            data = resp.json()
            return {
                "status": "initiated",
                "payment_id": data.get("id"),
                "amount_usd": amount_usd,
                "redirect_url": data.get("redirect_url"),
            }
        except httpx.HTTPError as exc:
            log.warning("payment_initiation failed: %s", exc)
            return {"error": "Payment initiation failed — please try again"}

    return payment_initiation
```

Key constraints that apply to all partner tools:
+  **Latency budget:** if the partner API may take more than one second, return a pending reference immediately and poll asynchronously. Nova 2 Sonic will go silent on tool calls that exceed the bidi window. See [Nova 2 Sonic latency constraint](extend-specialist-tool.md#extend-tool-latency).
+  **Never pass raw sensitive data through the LLM:** card numbers, SSNs, and credentials are handled exclusively in the tool function, not in the prompt or the model turn.
+  **Tenant gating:** check `config` or the tenant config record before making the API call. Tools in the `PERSONA_TOOL_FACTORIES` list are registered for every session of a given persona; a partner integration that is not universally available should guard at call time using the tenant’s `features` flags.