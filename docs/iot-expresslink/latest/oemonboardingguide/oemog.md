# AWS IoT ExpressLink Onboarding-by-Claim Customer/OEM Guide

AWS IoT ExpressLink modules are hardware modules that enable easy cloud connectivity and security for AWS IoT devices. OEMs can integrate
ExpressLink modules into their products to accelerate IoT development. ExpressLink modules come pre-provisioned with unique credentials
to authenticate with AWS IoT Core. There are several options for onboarding ExpressLink devices, including individual/batch uploads,
just-in-time provisioning, and fleet provisioning. The description focuses on a novel "onboarding-by-claim" process specific to
ExpressLink. This leverages the module's unique capabilities to provide a more secure and streamlined onboarding experience.

## Overview

AWS IoT [ExpressLink](https://aws.amazon.com/iot-expresslink/ "https://aws.amazon.com/iot-expresslink/") modules
are hardware connectivity modules that enable easy AWS cloud connectivity and implement
strict and AWS-mandated security requirements for device-to-cloud connections. OEMs can
accelerate the development of IoT products by integrating ExpressLink modules into their
designs.

ExpressLink modules come pre-provisioned with a unique identifier and a certificate
signed by the module manufacturer's Certificate Authority (CA), ready to authenticate
with AWS IoT Core. _Onboarding_ refers to the act of binding the module's
credentials to a `thing` inside the
[AWS IoT
registry](../../../iot/latest/developerguide/iot-thing-management.md "../../../iot/latest/developerguide/iot-thing-management.md") of an OEM's account. There are multiple ways to onboard devices:

- individual certificate upload
- batch certificate upload
- just-in-time provisioning (JITP)
- just-in-time registration (JITR)
- fleet provisioning

### The onboarding process

This guide describes a novel _onboarding-by-claim_ mechanism specifically
created to leverage an ExpressLink module's unique capabilities.

By default, ExpressLink modules connect to ExpressLink _staging account
endpoints_. The staging account is managed by AWS to facilitate the
onboarding-by-claim mechanism. It acts as a spring board to dispatch devices to their ultimate
destination– the customer/OEM account. (See the
[AWS IoT ExpressLink Getting Started Guide](../gettingstartedguide/elgsg.md "../gettingstartedguide/elgsg.md")).

The onboarding-by-claim process uses the
[Just-in-time
provisioning (JITP)](../../../iot/latest/developerguide/jit-provisioning.md "../../../iot/latest/developerguide/jit-provisioning.md") mechanism to automatically upload the device certificate,
associate a policy, and create a "thing", but provides additional features, including:

- Late binding– the onboarding happens only when the end-user activates a
  finished product. This makes the onboarding process less time consuming during
  product manufacturing and, therefore, less expensive.
- No disclosure of confidential information is required with any element of the
  supply chain. This makes the process more secure and flexible, as the supply
  chain of trust is reduced to a direct link from the ExpressLink module manufacturer
  to the end-user in possession of the finished product.

###### The Onboarding Process in Detail: the user experience

1. The onboarding-by-claim process is driven by the end-user who purchased
   a finished IoT capable product. It is triggered when the user interacts with a
   "product registration portal". This is OEM-specific software that can be a web or
   mobile application that offers end-users the opportunity to bind their identity
   to the unique product in their possession. After that, the OEM's application(s)
   can offer unique, personalized services augmented by the product's IoT
   connectivity.
2. During product registration, the user is instructed to turn on the product and
   connect it for the first time. If the product uses an ExpressLink module, it
   connects to the default staging account, unless otherwise configured. Then, it
   automatically subscribes to a configuration (MQTT) topic.
3. The end-user is instructed to enter a unique identifier that they can find on a
   label on the finished product or its packaging. This identifier is a long
   alphanumerical string or possibly a QR code (the preferred option if the registration
   portal is implemented as a mobile app).
4. The identifier can now be used to find the unique "thing" present in the staging
   account and communicate with it (using the configuration topic) to provide the
   desired customer/OEM endpoint. It is this latter action that constitutes the
   actual "claim". After that, the device disconnects from the staging account, and
   then connects to the newly assigned endpoint.
5. The just-in-time provisioning (JITP) mechanism completes the process–
   the new device is authenticated, and a new "thing" is created in the selected
   customer/OEM account according to the instructions provided by a JITP template.
