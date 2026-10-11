

# Partner Integration Points
<a name="reference-partner-integrations"></a>

The Agentic Vehicle Experience is designed to compose with third-party services across the vehicle-ownership lifecycle. The table below lists the integration domains, example partner categories, and the integration pattern used in each case. Specific partner selection is customer-owned; the patterns are reusable across providers.


**Partner integration points**  

| Domain | Example Partner Categories | Integration Pattern | 
| --- | --- | --- | 
|  **Digital Commerce**  | CRM platforms (for example, Salesforce), digital experience platforms (for example, Adobe) | REST webhook triggered by the `book` tool when a service request or appointment is created. The agent emits a STAR-JSON `ServiceRequestAdd` envelope to the configured tenant sink; a thin Lambda adapter converts to the partner’s API shape. | 
|  **Payments**  | Payment processors (for example, Stripe), open-banking connectivity platforms (for example, Plaid) | Agent tool call for payment initiation (deductible collection, subscription renewal, parts deposit). The tool invokes the partner’s payment API and returns a transaction reference that is embedded in the STAR-JSON `ServiceRequestAdd` `costEstimate` block. | 
|  **Document Processing**  | Dealer management systems with document APIs (for example, CDK, Reynolds and Reynolds) | Lambda invocation for repair-order and invoice generation. The AVX `ServiceRequestAdd` payload is translated to the DMS import format; the resulting repair-order number is written back into the STAR envelope and emitted to the tenant sink. | 
|  **Contract Management**  | Contract lifecycle management platforms (for example, Conga, Agiloft) | Agent tool lookup for warranty-contract terms, extended-service-contract eligibility, and lease-end conditions. The tool returns structured coverage data that feeds the `WarrantyClaimPreCheck` payload. | 
|  **Credit Decisioning**  | Credit-scoring and decisioning bureaus (for example, FICO, Experian) | API call from the finance/ownership persona when a driver explores financing for a repair or a vehicle upgrade. Results inform the agent’s recommendation but are not persisted in STAR messages. | 
|  **Subscription Management**  | Subscription billing platforms (for example, Zuora) | Webhook for connected-service subscription events (activation, renewal, cancellation). The agent queries current subscription status to gate feature availability (for example, over-the-air update eligibility, roadside-assistance entitlement). | 