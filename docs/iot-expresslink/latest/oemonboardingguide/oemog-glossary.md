# Appendix D - Glossary

This is a glossary, containing all the terms used in this guide.

**ExpressLink modules**

Hardware connectivity modules that enable easy AWS cloud connectivity and
implement strict and AWS-mandated security requirements for device-to-cloud
connections.

**ExpressLink devices**

OEM products that embed an ExpressLink module and use the module for AWS
cloud connectivity.

**OEM AWS account**

An AWS account that OEMs use to manage their IoT devices.

**ExpressLink AWS staging account/endpoint**

An AWS-managed account that provides:

- out-of-the-box Quick Connect functionality.
- a staging area for non-onboarded ExpressLink devices waiting to be
  claimed and onboarded.

**onboarding**

The registering of an OEM's ExpressLink device inside the OEM AWS Account;
ExpressLink provides 5 ways to do this.

**onboarding-by-claim**

One of the 5 onboarding methods provided by ExpressLink; it streamlines onboarding
and eliminates manual setup.

**claim-thing**

A virtual device in the staging account (registry) whose sole purpose is to
publish configuration messages.

**registration portal**

A web or mobile application that allows the end-user to register an (IoT)
product.

**Onboarding functionality**

Any piece of code that is able to:

- connect to the ExpressLink AWS staging account as the claim-thing.
- publish the MQTT endpoint change message to the MQTT control topic in
  the staging account.
