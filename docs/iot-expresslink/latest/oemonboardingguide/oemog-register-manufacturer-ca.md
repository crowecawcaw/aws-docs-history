

# Appendix B - Register the ExpressLink manufacturer certificate authority (CA)
<a name="oemog-register-manufacturer-ca"></a>

 After a claim-thing certificate is obtained, the next steps is to register the ExpressLink certificate with the manufacturer certificate authority (CA). This four step process walks the user through registering with the certificate authority (CA). 

1. Follow the steps in [ Getting started with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) to install the AWS CLI on your development machine. 

1. Follow the steps in [ Configuration and credential file settings](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) to configure the AWS CLI to use your AWS account credentials.

1. Register the root CA on your AWS account with the following AWS CLI command (replace {{path-to-manufacturer-CA}} with the local path of the the root CA):

   ```
   aws iot register-ca-certificate --ca-certificate file://{{path-to-manufacturer-CA}} --certificate-mode SNI_ONLY --set-as-active --allow-auto-registration 
   ```

   (For more information on non-Amazon-signed certificates and certificate authorities on AWS IoT Core, see [ Create your own client certificates](https://docs.aws.amazon.com/iot/latest/developerguide/device-certs-your-own.html).

1. Record the *CA certificate id* that is shown in the output of the command above. The CA certificate id is a long hexadecimal string. You will need this later.