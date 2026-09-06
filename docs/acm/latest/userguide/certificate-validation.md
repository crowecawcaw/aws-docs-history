

# Troubleshoot certificate validation
<a name="certificate-validation"></a>

If the ACM certificate request status is **Pending validation**, the request is waiting for action from you. If you chose email validation when you made the request, you or an authorized representative must respond to the validation email messages. These messages were sent to the common email addresses for the requested domain. For more information, see [AWS Certificate Manager email validation](email-validation.md). If you chose DNS validation, you must write the CNAME record that ACM created for you to your DNS database. For more information, see [AWS Certificate Manager DNS validation](dns-validation.md). 

**Important**  
You must validate that you own or control every domain name that you included in your certificate request. If you chose email validation, you will receive validation email messages for each domain. If you do not, then see [Not receiving validation email](troubleshooting-email-validation.md#troubleshooting-no-mail). If you chose DNS validation, you must create one CNAME record for each domain. 

**Note**  
To automate public certificate issuance and renewal outside integrated services such as on Amazon EC2 instances, use the ACME protocol. For more information, see [ACME certificate automation](acm-acme.md). Alternatively, if you cannot use ACME, you can automate exportable certificates issued from ACM through [AWS Workload Credentials Provider](acm-certificate-automation.md).

We recommend that you use DNS validation rather than email validation.

Consult the following topics if you experience validation problems.

**Topics**
+ [Troubleshoot DNS validation problems](troubleshooting-DNS-validation.md)
+ [Troubleshoot email validation problems](troubleshooting-email-validation.md)
+ [Troubleshooting HTTP validation problems](troubleshooting-HTTP-validation.md)