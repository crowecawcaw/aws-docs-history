# Appendix B - Register the ExpressLink

manufacturer certificate authority (CA)

After a claim-thing certificate is obtained, the next steps is to register the ExpressLink certificate with the manufacturer certificate
authority (CA). This four step process walks the user through registering with the certificate authority (CA).

1. Follow the steps in
   [Getting started with the AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md") to install the AWS CLI on your
   development machine.
2. Follow the steps in
   [Configuration and credential file settings](../../../cli/latest/userguide/cli-configure-files.md "../../../cli/latest/userguide/cli-configure-files.md") to configure the AWS
   CLI to use your AWS account credentials.
3. Register the root CA on your AWS account with the following AWS CLI
   command (replace `path-to-manufacturer-CA`
   with the local path of the the root CA):

```
aws iot register-ca-certificate --ca-certificate file://`path-to-manufacturer-CA` --certificate-mode SNI_ONLY --set-as-active --allow-auto-registration
```

(For more information on non-Amazon-signed certificates and certificate
authorities on AWS IoT Core, see
[Create your own client certificates](../../../iot/latest/developerguide/device-certs-your-own.md "../../../iot/latest/developerguide/device-certs-your-own.md"). 4. Record the _CA certificate id_ that is shown in the
output of the command above. The CA certificate id is a long hexadecimal
string. You will need this later.
