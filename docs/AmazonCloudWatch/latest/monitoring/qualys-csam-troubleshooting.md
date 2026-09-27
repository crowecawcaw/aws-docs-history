

# Troubleshooting the Qualys CSAM integration
<a name="qualys-csam-troubleshooting"></a>

## Common errors
<a name="qualys-csam-common-errors"></a>

The following table lists common errors and their resolutions.


| Error | Likely cause | Resolution or connector behavior | 
| --- | --- | --- | 
| 401 Unauthorized | Invalid or expired credentials | The connector automatically renews credentials and retries up to six times. Verify the username and password in AWS Secrets Manager. | 
| 403 Forbidden | Insufficient permissions or the CSAM module is not licensed | Make sure that API access is enabled for the Qualys account and that the subscription includes the CSAM module. This error is not retryable and stops processing immediately. | 
| 409 Conflict (CODE 1965) | API rate limit exceeded | The connector reads the X-RateLimit-ToWait-Sec header and retries after the specified wait time. | 
| 409 Conflict (CODE 1960) | Concurrent call limit exceeded | The connector retries with progressive backoff of 5, 10, 30, 60, 120, and 300 seconds. | 
| 5xx Server Error | Qualys platform server-side issue | The connector automatically retries with backoff intervals of 1, 2, 5, 10, 20, and 40 seconds. | 
| No data appears in the log group | The pipeline resource policy was not added within five minutes | Delete and recreate the pipeline, and then immediately add the CloudWatch Logs resource policy. | 
| Empty results | No scans or discovery ran on the hosts in the configured time range | Verify that scans are active and that hosts were evaluated within the range window. | 

## Identify your Qualys API Gateway hostname
<a name="qualys-csam-identify-hostname"></a>
+ The CSAM connector uses the Qualys API Gateway hostname, such as `gateway.qg3.apps.qualys.com`. This differs from the VMDR API hostname, such as `qualysapi.qg3.apps.qualys.com`.
+ Log in to the Qualys Cloud Platform and navigate to **Help** > **About** to identify your platform assignment.
+ If you are not sure which platform you use, see [Qualys Platform Identification](https://www.qualys.com/platform-identification).
+ Enter only the domain. Don't include `https://` in the hostname.

## Difference between CSAM and VMDR hostnames
<a name="qualys-csam-vmdr-hostname-difference"></a>
+ Qualys VMDR uses `qualysapi.<platform>.apps.qualys.com`, such as `qualysapi.qg3.apps.qualys.com`.
+ Qualys CSAM uses `gateway.<platform>.apps.qualys.com`, such as `gateway.qg3.apps.qualys.com`.
+ Both hostnames correspond to the same Qualys platform but use different API surfaces. Use the `gateway` hostname for the Qualys CSAM connector.