

# AgentCore generated payments observability data
<a name="observability-payments-metrics"></a>

AgentCore payments automatically generates spans and metrics for every data plane API call. This data is available in Amazon CloudWatch and AWS X-Ray.

For full details on payments observability setup, prerequisites, IAM permissions, and vended logs, see [Observability with Amazon CloudWatch](payments-observability.md) in the payments documentation.

## Provided spans
<a name="observability-payments-spans"></a>

AgentCore payments emits one span per data plane API call. Span names follow the pattern `Bedrock.AgentCore.Payments.<Operation>`.


| Operation | Span attributes | Description | 
| --- | --- | --- | 
| ProcessPayment | aws.payments.payment\_manager\_id, payment\_connector\_id, payment\_instrument\_id, payment\_session\_id, spend\_amount, spend\_currency, session\_remaining\_budget, merchant, token\_fetch\_latency\_ms, payment\_agent\_name | Process a payment transaction | 
| CreatePaymentInstrument | aws.payments.payment\_manager\_id, payment\_connector\_id, payment\_instrument\_id, payment\_agent\_name | Create a payment instrument | 
| GetPaymentInstrument | aws.payments.payment\_manager\_id, payment\_connector\_id, payment\_instrument\_id, payment\_agent\_name | Retrieve a payment instrument | 
| ListPaymentInstruments | aws.payments.payment\_manager\_id, payment\_agent\_name | List payment instruments | 
| DeletePaymentInstrument | aws.payments.payment\_manager\_id, payment\_connector\_id, payment\_instrument\_id, payment\_agent\_name | Delete a payment instrument | 
| GetPaymentInstrumentBalance | aws.payments.payment\_manager\_id, payment\_connector\_id, payment\_instrument\_id, payment\_agent\_name | Get instrument balance | 
| CreatePaymentSession | aws.payments.payment\_manager\_id, payment\_session\_id, session\_start\_time, payment\_agent\_name | Create a payment session | 
| GetPaymentSession | aws.payments.payment\_manager\_id, payment\_session\_id, session\_start\_time, payment\_agent\_name | Retrieve a payment session | 
| ListPaymentSessions | aws.payments.payment\_manager\_id, payment\_agent\_name | List payment sessions | 
| DeletePaymentSession | aws.payments.payment\_manager\_id, payment\_session\_id, payment\_agent\_name | Delete a payment session | 

All spans also include standard AWS attributes: `aws.region`, `aws.account.id`, `aws.resource.arn`, `aws.request_id`, `http.response.status_code`.

## Provided metrics
<a name="observability-payments-metrics-provided"></a>


| Metric | Unit | Description | 
| --- | --- | --- | 
| OperationSuccess | Count | Number of successful API calls | 
| OperationFailure | Count | Number of failed API calls | 
| OperationLatency | Milliseconds | End-to-end latency per API call | 
| SpendAmount | None | Payment amount processed (ProcessPayment only) | 
| Throttles | Count | Number of throttled requests | 
| UserErrors | Count | Number of client-side validation errors | 
| ActiveSessions | Count | Number of active payment sessions | 
| PaymentRequestCount | Count | Total payment requests | 
| PaymentSuccessCount | Count | Successful payment transactions | 
| PaymentFailureCount | Count | Failed payment transactions | 
| PaymentLatency | Milliseconds | Payment processing latency | 

Metrics are published with the following dimensions: **Operation**, **PaymentManagerId**, **PaymentConnectorId**, **AgentName**, **Currency** (for SpendAmount).