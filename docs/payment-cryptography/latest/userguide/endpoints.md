# Endpoints for AWS Payment Cryptography

To connect programmatically to AWS Payment Cryptography, you use an endpoint, the URL of the entry point
for the service. The AWS SDKs and the command line tools automatically use
the default endpoint for the service in an AWS Region based on the region
context of a request, so there's typically no need to explicitly set these values. When
needed, you can specify a different endpoint for your API requests.

## Control plane endpoints

| Region Name              | Region         | Endpoint                                                                                                                | Protocol    |
| ------------------------ | -------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------- | ----------------------- |
| US East (Ohio)           | us-east-2      | controlplane.payment-cryptography.us-east-2.amazonaws.com controlplane.payment-cryptography.us-east-2.api.aws           | HTTPS HTTPS |
| US East (N. Virginia)    | us-east-1      | controlplane.payment-cryptography.us-east-1.amazonaws.com controlplane.payment-cryptography.us-east-1.api.aws           | HTTPS HTTPS |
| US West (Oregon)         | us-west-2      | controlplane.payment-cryptography.us-west-2.amazonaws.com controlplane.payment-cryptography.us-west-2.api.aws           | HTTPS HTTPS |
| Asia Pacific (Mumbai)    | ap-south-1     | controlplane.payment-cryptography.ap-south-1.amazonaws.com controlplane.payment-cryptography.ap-south-1.api.aws         | HTTPS HTTPS |
| Asia Pacific (Osaka)     | ap-northeast-3 | controlplane.payment-cryptography.ap-northeast-3.amazonaws.com controlplane.payment-cryptography.ap-northeast-3.api.aws | HTTPS HTTPS |
| Asia Pacific (Singapore) | ap-southeast-1 | controlplane.payment-cryptography.ap-southeast-1.amazonaws.com controlplane.payment-cryptography.ap-southeast-1.api.aws | HTTPS HTTPS |
| Asia Pacific (Tokyo)     | ap-northeast-1 | controlplane.payment-cryptography.ap-northeast-1.amazonaws.com controlplane.payment-cryptography.ap-northeast-1.api.aws | HTTPS HTTPS |
| Europe (Frankfurt)       | eu-central-1   | controlplane.payment-cryptography.eu-central-1.amazonaws.com controlplane.payment-cryptography.eu-central-1.api.aws     | HTTPS HTTPS |
| Europe (Ireland)         | eu-west-1      | controlplane.payment-cryptography.eu-west-1.amazonaws.com controlplane.payment-cryptography.eu-west-1.api.aws           | HTTPS HTTPS | ## Data plane endpoints |
| Region Name              | Region         | Endpoint                                                                                                                | Protocol    |
| ---                      | ---            | ---                                                                                                                     | ---         |
| US East (Ohio)           | us-east-2      | dataplane.payment-cryptography.us-east-2.amazonaws.com dataplane.payment-cryptography.us-east-2.api.aws                 | HTTPS HTTPS |
| US East (N. Virginia)    | us-east-1      | dataplane.payment-cryptography.us-east-1.amazonaws.com dataplane.payment-cryptography.us-east-1.api.aws                 | HTTPS HTTPS |
| US West (Oregon)         | us-west-2      | dataplane.payment-cryptography.us-west-2.amazonaws.com dataplane.payment-cryptography.us-west-2.api.aws                 | HTTPS HTTPS |
| Asia Pacific (Mumbai)    | ap-south-1     | dataplane.payment-cryptography.ap-south-1.amazonaws.com dataplane.payment-cryptography.ap-south-1.api.aws               | HTTPS HTTPS |
| Asia Pacific (Osaka)     | ap-northeast-3 | dataplane.payment-cryptography.ap-northeast-3.amazonaws.com dataplane.payment-cryptography.ap-northeast-3.api.aws       | HTTPS HTTPS |
| Asia Pacific (Singapore) | ap-southeast-1 | dataplane.payment-cryptography.ap-southeast-1.amazonaws.com dataplane.payment-cryptography.ap-southeast-1.api.aws       | HTTPS HTTPS |
| Asia Pacific (Tokyo)     | ap-northeast-1 | dataplane.payment-cryptography.ap-northeast-1.amazonaws.com dataplane.payment-cryptography.ap-northeast-1.api.aws       | HTTPS HTTPS |
| Europe (Frankfurt)       | eu-central-1   | dataplane.payment-cryptography.eu-central-1.amazonaws.com dataplane.payment-cryptography.eu-central-1.api.aws           | HTTPS HTTPS |
| Europe (Ireland)         | eu-west-1      | dataplane.payment-cryptography.eu-west-1.amazonaws.com dataplane.payment-cryptography.eu-west-1.api.aws                 | HTTPS HTTPS |
