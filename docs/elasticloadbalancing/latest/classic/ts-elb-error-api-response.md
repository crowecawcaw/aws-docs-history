# Troubleshoot a Classic Load Balancer: API errors

The following are error messages returned by ELB API, the
potential causes, and the steps you can take to resolve the issues.

###### Error Messages

- [CertificateNotFound: Undefined](#ts-elb-error-message-certificate "#ts-elb-error-message-certificate")
- [OutofService: A transient error occurred](#ts-elb-error-message-service "#ts-elb-error-message-service")

## CertificateNotFound: Undefined

**Cause 1**: There is a delay in propagating the certificate to all Regions
when it is created using the AWS Management Console. When this delay occurs, the error message is shown
in the last step in the process of creating the load balancer.

**Solution 1**: Wait approximately 15 minutes and then try
again. If the problem persists, go to the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") for assistance.

**Cause 2**: If you are using the AWS CLI or API directly,
you can receive this error if you provide an Amazon Resource Name (ARN)
for a certificate that does not exist.

**Solution 2**: Use the AWS Identity and Access Management (IAM) action
[GetServerCertificate](../../../IAM/latest/APIReference/API_GetServerCertificate.md "../../../IAM/latest/APIReference/API_GetServerCertificate.md")
to get the certificate ARN and verify that you provided the correct value for the ARN.

## OutofService: A transient error occurred

**Cause**: There is a transient internal problem within the
ELB service or the underlying network. This temporary issue might also occur
when ELB queries the health of the load balancer and its registered instances.

**Solution**: Retry the API call. If the problem persists,
go to the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") for assistance.
