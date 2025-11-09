# Quotas for AWS Verified Access

Your AWS account has default quotas, formerly referred to as limits, for each
AWS service. Unless otherwise noted, each quota is Region-specific.

###### AWS account-level quotas

Your AWS account has the following quotas related to Verified Access.

| Name                            | Default | Adjustable                                                                                                                                                                 | Description                                                                                            |
| ------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Verified Access Instances       | 5       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-17A8BD20 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-17A8BD20") | The maximum number of Verified Access Instances that customers can create in the current Region.       |
| Verified Access Groups          | 10      | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-3829BC77 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-3829BC77") | The maximum number of Verified Access Groups that customers can create in the current Region.          |
| Verified Access Trust Providers | 15      | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-AF309E5E "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-AF309E5E") | The maximum number of Verified Access Trust Providers that customers can create in the current Region. |
| Verified Access Endpoints       | 50      | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-5D439CF7 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-5D439CF7") | The maximum number of Verified Access Endpoints that customers can create in the current Region.       |

###### HTTP headers

The following are the size limits for HTTP headers.

| Name                   | Default | Adjustable |
| ---------------------- | ------- | ---------- |
| Request line           | 16 K    | No         |
| Single header          | 16 K    | No         |
| Entire response header | 32 K    | No         |
| Entire request header  | 64 K    | No         |

###### HTTP traffic

The connection idle timeout is 60 seconds. If an application takes longer than 60 seconds
to respond to an HTTP request, the client receives an HTTP 504 gateway timeout error. If
Verified Access logs is enabled, we log any HTTP 504 errors.

###### OIDC claim size

The following is the OIDC claim size limit.

| Name            | Default | Adjustable |
| --------------- | ------- | ---------- |
| OIDC claim size | 11 K    | No         |

###### IAM Identity Center

Verified Access can provide access to users in IAM Identity Center who are assigned to up to 1,000 groups.
