# AWS CloudHSM quotas

Quotas, formerly known as limits, are the assigned values for AWS resources. The
following quotas apply to your AWS CloudHSM resources per AWS Region and AWS account. The
default quota is the initial value applied by AWS, and these values are listed in the
table below. An adjustable quota can be increased above the default quota.

| Service quotas   | Resource | Default Quota | Adjustable? |
| ---------------- | -------- | ------------- | ----------- |
| Clusters         | 4        | Yes           |
| HSMs             | 6        | Yes           |
| HSMs per cluster | 28       | No            |

The recommended way of requesting a quota increase is to open the [Service Quotas
console](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/dashboard "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/dashboard"). In the console, choose your service and quota, and submit your request.
For more information, see the [Service Quotas documentation](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md").

The quotas in the following System Quotas table are not adjustable.

| System quotas                                                                             | Resource           | Quota for hsm1.medium                                             | Quota for hsm2m.medium |
| ----------------------------------------------------------------------------------------- | ------------------ | ----------------------------------------------------------------- | ---------------------- |
| Maximum keys per cluster                                                                  | 3,300              | 16,666 total keys, with asymmetric keys having a maximum of 3,333 |
| Maximum users per cluster                                                                 | 250                | 1,024                                                             |
| Maximum length of a user name                                                             | 31 characters      | 31 characters                                                     |
| Required password length                                                                  | 8 to 32 characters | 8 to 32 characters                                                |
| Maximum number of concurrent client connections per cluster[1](#QuotaNote1 "#QuotaNote1") | 900                | 900                                                               |
| Maximum number of PKCS#11 sessions per application                                        | 1,024              | 1,024                                                             |

[1] A client connection for Client SDK 3 is a client daemon. For Client SDK 5, a client connection is an application.
