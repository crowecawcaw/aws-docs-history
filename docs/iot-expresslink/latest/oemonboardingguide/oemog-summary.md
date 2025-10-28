# Summary

To summarize, ExpressLink modules come pre-provisioned with a unique identifier and a certificate signed
by the module manufacturer Certificate Authority (CA), ready to authenticate with AWS IoT Core.

Onboarding, the act of binding the module credentials to a
[thing](../../../iot/latest/developerguide/iot-thing-management.md "../../../iot/latest/developerguide/iot-thing-management.md")
inside the AWS IoT registry of an customer/OEM's account is accomplished using various
mechanisms provided to all devices that connect to AWS IoT Core. This guide describes a novel
onboarding-by-claim mechanism specifically created to leverage an ExpressLink module's unique
capabilities.

By following the steps in this document, any customer/OEM can take
advantage of this new capability to provide their own customers with the best experience,
while optimizing the supply chain for security and flexibility.
