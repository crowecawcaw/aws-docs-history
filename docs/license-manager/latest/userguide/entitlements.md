# Seller issued license entitlements in License Manager

License Manager captures seller issued license capabilities as _entitlements_ in the license.
Entitlements can be characterized with a limited or unlimited quantity. An example of a
limited entitlement is ‘40 GB of data transfer’. An example of an unlimited quantity
entitlement is ‘Platinum Tier’.

A license captures all the granted entitlements, the activation and expiration dates,
and the issuer details. A license is a versioned entity and each version is immutable.
License versions are updated whenever the license is changed.

To check out or check in limited entitlements, ISV applications must specify the amount
of each limited capacity. For unlimited entitlements, ISV applications can simply specify
the relevant entitlement to check out or check in again. Finally, limited capabilities also
support an “overage” flag, which indicates if end-users can exceed their usage of the
initial entitlements. License Manager tracks and reports usage, along with any overages, to the ISV.
