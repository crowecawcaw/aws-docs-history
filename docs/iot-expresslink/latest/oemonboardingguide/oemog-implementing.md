# Claim implementation

The actual claim is implemented in the claim-script (a function of the registration application).
To do this, it publishes a specific, JSON formatted message on the unique device configuration
topic. This operation requires the script to obtain access to the ExpressLink module staging
account which is managed by AWS. While AWS does not share such credentials with customers/OEMs,
upon request the AWS IoT Device service team allows the customer/OEM to create a "claim-thing"
within the staging account registry. The claim-thing can then be controlled by the OEM
registration application (using an MQTT client API) to publish the endpoint update message.
To request and obtain control of a claim-thing follow the configuration steps indicated in
[Appendix A - Steps to obtain a claim-thing](oemog-claim-thing.md "oemog-claim-thing.md").

## Configure the OEM account

In the last step, the customer/OEM's AWS account must be configured to enable the use
of the just-in-time provisioning mechanism. To do this:

1. Register the ExpressLink module vendor's Certificate Authority with the customer/OEM
   account. Follow the steps in [Appendix B - Register the ExpressLink
   manufacturer certificate authority (CA)](oemog-register-manufacturer-ca.md "oemog-register-manufacturer-ca.md").
2. Create a JITP template so that new devices that are directed to the account will
   be automatically associated with a desired policy and given a proper thing-name.
   Follow the steps in [Appendix C - Create a JITP template](oemog-creating-jitp-template.md "oemog-creating-jitp-template.md").
