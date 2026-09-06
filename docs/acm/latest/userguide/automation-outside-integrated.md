

# Automation outside integrated services
<a name="automation-outside-integrated"></a>

You can export an ACM issued certificate for use on any workload. Once exported, you get access to the certificate's private key that you can employ to securely terminate TLS traffic.

**Tip**  
If you want to automate certificate issuance and renewal directly on your customer-managed infrastructure, we recommend ACME certificate automation for use with industry-standard, open source ACME clients (such as Certbot or cert-manager). See [ACME certificate automation](acm-acme.md). Alternatively, if you cannot use ACME, you can automate exportable certificates issued from ACM through [AWS Workload Credentials Provider](acm-certificate-automation.md).