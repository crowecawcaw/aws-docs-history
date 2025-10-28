# AWS Device Farm endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name                                         | Region                             | Endpoint                                                                                                                                                                                 | Protocol                                                                         |
| --------------------------------------------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ----------------- |
| US West (Oregon)                                    | us-west-2                          | devicefarm.us-west-2.amazonaws.com                                                                                                                                                       | HTTPS                                                                            | ## Service quotas |
| Name                                                | Default                            | Adjustable                                                                                                                                                                               | Description                                                                      |
| ---                                                 | ---                                | ---                                                                                                                                                                                      | ---                                                                              |
| Concurrency for automation tests on metered devices | Each supported Region: 5           | [Yes](https://console.aws.amazon.com/servicequotas/home/services/devicefarm/quotas/L-681D859E "https://console.aws.amazon.com/servicequotas/home/services/devicefarm/quotas/L-681D859E") | The maximum number of concurrent metered devices running automation tests.       |
| Concurrency for remote access on metered devices    | Each supported Region: 2           | [Yes](https://console.aws.amazon.com/servicequotas/home/services/devicefarm/quotas/L-F73D98D4 "https://console.aws.amazon.com/servicequotas/home/services/devicefarm/quotas/L-F73D98D4") | The maximum number of concurrent metered devices running remote access sessions. |
| Remote access session length in minutes             | Each supported Region: 150         | No                                                                                                                                                                                       | The maximum length of a remote access session per device in minutes.             |
| Test run timeout per device in minutes              | Each supported Region: 150         | No                                                                                                                                                                                       | The maximum length of an automation test run per device in minutes.              |
| Uploaded file size                                  | Each supported Region: 4 Gigabytes | No                                                                                                                                                                                       | The maximum size of a file to be uploaded.                                       |
