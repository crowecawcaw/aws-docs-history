# Troubleshoot your Classic Load Balancer

The following tables list the troubleshooting resources that you'll find useful as you
work with a Classic Load Balancer.

| API errors                                                                                                                                                                             | Error                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- | -------------------- |
| [CertificateNotFound: Undefined](ts-elb-error-api-response.md#ts-elb-error-message-certificate "ts-elb-error-api-response.md#ts-elb-error-message-certificate")                        |
| [OutofService: A transient error occurred](ts-elb-error-api-response.md#ts-elb-error-message-service "ts-elb-error-api-response.md#ts-elb-error-message-service")                      | HTTP errors                  | Error                |
| ---                                                                                                                                                                                    |
| [HTTP 400: BAD_REQUEST](ts-elb-error-message.md#ts-elb-errorcodes-http400 "ts-elb-error-message.md#ts-elb-errorcodes-http400")                                                         |
| [HTTP 405: METHOD_NOT_ALLOWED](ts-elb-error-message.md#ts-elb-errorcodes-http405 "ts-elb-error-message.md#ts-elb-errorcodes-http405")                                                  |
| [HTTP 408: Request timeout](ts-elb-error-message.md#ts-elb-errorcodes-http408 "ts-elb-error-message.md#ts-elb-errorcodes-http408")                                                     |
| [HTTP 502: Bad gateway](ts-elb-error-message.md#ts-elb-errorcodes-http502 "ts-elb-error-message.md#ts-elb-errorcodes-http502")                                                         |
| [HTTP 503: Service unavailable](ts-elb-error-message.md#ts-elb-errorcodes-http503 "ts-elb-error-message.md#ts-elb-errorcodes-http503")                                                 |
| [HTTP 504: Gateway timeout](ts-elb-error-message.md#ts-elb-errorcodes-http504 "ts-elb-error-message.md#ts-elb-errorcodes-http504")                                                     | Response code metrics        | Response code metric |
| ---                                                                                                                                                                                    |
| [HTTPCode_ELB_4XX](ts-elb-http-errors.md#ts-elb-error-metrics-ELB_4XX "ts-elb-http-errors.md#ts-elb-error-metrics-ELB_4XX")                                                            |
| [HTTPCode_ELB_5XX](ts-elb-http-errors.md#ts-elb-error-metrics-ELB_5XX "ts-elb-http-errors.md#ts-elb-error-metrics-ELB_5XX")                                                            |
| [HTTPCode_Backend_2XX](ts-elb-http-errors.md#ts-elb-error-metrics-Backend_2XX "ts-elb-http-errors.md#ts-elb-error-metrics-Backend_2XX")                                                |
| [HTTPCode_Backend_3XX](ts-elb-http-errors.md#ts-elb-error-metrics-Backend_3XX "ts-elb-http-errors.md#ts-elb-error-metrics-Backend_3XX")                                                |
| [HTTPCode_Backend_4XX](ts-elb-http-errors.md#ts-elb-error-metrics-Backend_4XX "ts-elb-http-errors.md#ts-elb-error-metrics-Backend_4XX")                                                |
| [HTTPCode_Backend_5XX](ts-elb-http-errors.md#ts-elb-error-metrics-Backend_5XX "ts-elb-http-errors.md#ts-elb-error-metrics-Backend_5XX")                                                | Health check issues          | Issue                |
| ---                                                                                                                                                                                    |
| [Health check target page error](ts-elb-healthcheck.md#ts-elb-healthcheck-targetpage "ts-elb-healthcheck.md#ts-elb-healthcheck-targetpage")                                            |
| [Connection to the instances has timed out](ts-elb-healthcheck.md#ts-elb-healthcheck-failed "ts-elb-healthcheck.md#ts-elb-healthcheck-failed")                                         |
| [Public key authentication is failing](ts-elb-healthcheck.md#ts-elb-healthcheck-publickey "ts-elb-healthcheck.md#ts-elb-healthcheck-publickey")                                        |
| [Instance is not receiving traffic from the load balancer](ts-elb-healthcheck.md#ts-elb-healthcheck-securitygroup "ts-elb-healthcheck.md#ts-elb-healthcheck-securitygroup")            |
| [Ports on instance are not open](ts-elb-healthcheck.md#ts-elb-healthcheck-ports "ts-elb-healthcheck.md#ts-elb-healthcheck-ports")                                                      |
| [Instances in an Auto Scaling group are failing the ELB health check](ts-elb-healthcheck.md#ts-elb-healthcheck-autoscaling "ts-elb-healthcheck.md#ts-elb-healthcheck-autoscaling")     | Connectivity issues          | Issue                |
| ---                                                                                                                                                                                    |
| [Clients cannot connect to an internet-facing load balancer](ts-elb-connection-failed.md#client-cannot-connect "ts-elb-connection-failed.md#client-cannot-connect")                    |
| [Requests sent to a custom domain aren't received by the load balancer](ts-elb-connection-failed.md#custom-domain-request "ts-elb-connection-failed.md#custom-domain-request")         |
| [HTTPS requests sent to the load balancer return "NET::ERR_CERT_COMMON_NAME_INVALID"](ts-elb-connection-failed.md#https-cert-invalid "ts-elb-connection-failed.md#https-cert-invalid") | Instance registration issues | Issue                |
| ---                                                                                                                                                                                    |
| [Taking too long to register an EC2 instance](ts-elb-register-instance.md#ts-elb-register-too-long "ts-elb-register-instance.md#ts-elb-register-too-long")                             |
| [Unable to register an instance launched from a paid AMI](ts-elb-register-instance.md#ts-elb-paid-ami-instance "ts-elb-register-instance.md#ts-elb-paid-ami-instance")                 |
