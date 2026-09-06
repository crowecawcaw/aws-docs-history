

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Revenue analytics
<a name="waf-ai-traffic-monetization-analytics"></a>

## Revenue dashboard
<a name="waf-ai-traffic-monetization-revenue-dashboard"></a>

The revenue dashboard shows:
+ Revenue summary – Total revenue, verified vs unverified revenue breakdown, total settlements, and total 402 responses served (GetRevenueStatisticsSummary)
+ Top sources by revenue – Ranked AI bots by revenue amount, grouped by name, category, intent, or organization (GetRevenueStatistics with TOP\_SOURCES\_BY\_REVENUE)
+ Top paths by revenue – Ranked content paths by revenue amount (GetRevenueStatistics with TOP\_PATHS\_BY\_REVENUE)
+ Revenue over time – Time series charts at minutely, 5-minute, hourly, or daily intervals (GetRevenueStatisticsTimeSeries with DATE\_HISTOGRAM)
+ Payment traffic over time – Payment attempt volume over time (GetRevenueStatisticsTimeSeries with PAYMENT\_TRAFFIC)
+ Settlement records – Individual transaction details including status (SETTLED, PENDING, FAILED, SERVICE\_ERROR, SKIPPED\_ORIGIN\_ERROR), payer address, amount, and blockchain transaction ID (ListSettlementRecords)

All revenue data can be filtered by source name, category, organization, and intent. By default, only real currency (REAL) transactions are shown – use the CurrencyMode filter to view test transactions.

## Log fields
<a name="waf-ai-traffic-monetization-log-fields"></a>

When you enable AWS WAF logging, monetization events include the following additional fields:


| Field | Description | 
| --- | --- | 
| `action` | WAF action taken on request | 
| `monetizeVerifyResponse.verificationStatus` | Verification result: VERIFIED, INSUFFICIENT\_FUNDS, INVALID\_PAYLOAD, INVALID\_PAYMENT\_REQUIREMENTS, SERVICE\_ERROR | 
| `monetizeVerifyResponse.failureReason` | Reason for verification failure (empty on success) | 
| `monetizeVerifyResponse.chainName` | Blockchain chain used | 
| `monetizeVerifyResponse.network` | Blockchain network identifier in CAIP-2 format | 
| `monetizeVerifyResponse.amount` | Payment amount in atomic token units | 
| `monetizeVerifyResponse.currency` | Payment currency (for example, USDC) | 
| `monetizeVerifyResponse.asset` | Token contract address | 
| `monetizeVerifyResponse.payerAddress` | Paying client's wallet address | 
| `monetizeVerifyResponse.idempotencyKey` | x402 payment idempotency key for retry correlation | 
| `monetizeVerifyResponse.currencyMode` | Currency mode: REAL or TEST | 

For more information, see [Logging AWS WAF protection pack (web ACL) traffic](logging.md).

## Metrics
<a name="waf-ai-traffic-monetization-metrics"></a>

Metrics are published in Amazon CloudWatch under namespace `AWS/WAFV2`.


| Metric Name | Description | 
| --- | --- | 
| `MonetizeRequests` | Emitted when the terminating rule has action Monetize | 
| `MonetizeRequestsFailedVerification` | Emitted when terminating rule has action Monetize AND verification status is not VERIFIED | 

These metrics have the following dimensions: Region, Rule, WebACL, Resource, ResourceType, Device, Country.

For more information, see [AWS WAF metrics and dimensions](waf-metrics.md).