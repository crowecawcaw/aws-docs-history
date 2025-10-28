# Use AMS SSP to provision Alexa for Business in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Alexa for Business capabilities directly in your AMS managed account. Alexa for Business is a service that enables your organization and employees to use Alexa to get more work done. With Alexa for Business, you can use Alexa
as your intelligent assistant to be more productive in meeting rooms, at your desk, and even with the Alexa devices you already use
at home or on the go. IT and facilities managers can use Alexa for Business to measure and increase the utilization of the existing meeting rooms in their workplace.

To learn more, see
[Alexa for Business](https://aws.amazon.com/alexaforbusiness/ "https://aws.amazon.com/alexaforbusiness/").

## Alexa for Business in AWS Managed Services FAQ

**Q: How do I request access to Alexa for Business in my AMS account?**

Request access by submitting a Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny) change type.
This RFC provisions the following IAM role to your account: `customer_alexa_console_role`. A
`customer_alexa_device_setup_user` is also created for the Device Setup Tool provided by Alexa for Business;
this Device Setup Tool can then be used to set up your devices. Once provisioned in your account, you must onboard the
roles in your federation solution.

The Alexa for Business gateway enables you to connect Alexa for Business to your Cisco Webex and Poly Group Series endpoints to control meetings
with your voice. The gateway software runs on your on-premises hardware and securely proxies conferencing directives from Alexa for Business
to your Cisco endpoint. The gateway needs two pairs of AWS credentials to communicate with Alexa for Business. We provide two limited-access
IAM users: `customer_alexa_gateway_installer_user` and `customer_alexa_gateway_execution_user`
for your Alexa for Business gateways, one for installing the gateway and one for operating the gateway; these can be requested by submitting an
RFC with the Deployment | Advanced stack components | Identity and Access Management (IAM) | Create entity or policy (managed automation) change type (ct-3dpd8mdd9jn1r).

###### Note

To generate usage reports and send them to Amazon S3, specify the Amazon S3 bucket name in the self-provisioned service RFC.

**Q: What are the restrictions to using Alexa for Business in my AMS account?**

There are no restrictions. Full functionality of Alexa for Business is available with the Alexa for Business self-provisioned service role.

**Q: What are the prerequisites or dependencies to using Alexa for Business in my AMS account?**

- If you intend to use WPA2 Enterprise Wi-Fi to set up your shared devices, then specify this network
  security type in the Device Setup Tool, for which an AWS Private Certificate Authority is required.
- AMS only creates secret keys that start with the namespace "A4B". This is restrictive only to this namespace.

**Q: What Alexa for Business functionality requires separate RFCs?**

To register an Alexa Voice Service (AVS) device with Alexa for Business, provide access to the Alexa built-in device
maker. To do this, an IAM role needs to be created in the Alexa for Business console that can be deployed using
the Management | Other | Other change type. This allows the AVS device maker to register and manage devices with Alexa for Business on your behalf.
