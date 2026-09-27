

# Known Qualys CSAM platform limitations
<a name="qualys-csam-limitations"></a>

The following table describes known Qualys CSAM platform limitations.


| Limitation | Details | Impact | 
| --- | --- | --- | 
| Customer-specific API Gateway hostname | The API Gateway URL varies by Qualys platform region. There is no universal endpoint. | You must identify your platform and configure the correct gateway hostname. | 
| API rate limits | With the default Standard API Service, Qualys permits 300 API calls per subscription for each API in a rolling 3,600-second window. When the limit is exceeded, Qualys returns HTTP 409 Conflict with error code 1965 and an X-RateLimit-ToWait-Sec header. | The connector waits for the interval in the X-RateLimit-ToWait-Sec header and then retries. Large environments might experience a slower initial backfill. | 
| Pagination on list endpoints | CSAM uses cursor-based pagination for assets, software, vulnerabilities, and domains. Each page requires a separate API call. | Large inventories have higher retrieval latency. The connector handles pagination internally. | 
| JWT token expiration | The bearer token expires after approximately four hours. | The connector automatically renews the token before expiration. No action is required. | 
| No sort-order support | The CSAM API does not document an ascending or descending sort parameter. | Records are not guaranteed to arrive in a specific order within a window. | 
| Shared credentials with VMDR | Qualys CSAM and VMDR share platform credentials but use different API endpoints and hostnames. | If you use both connectors, you can store credentials separately for each connector or use a shared secret. | 
| CSAM module licensing | Qualys CSAM is separately licensed. Individual EASM vulnerability and domain APIs require their corresponding submodules. | API calls fail if your subscription does not include the corresponding module. | 