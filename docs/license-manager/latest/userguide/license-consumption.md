# Check out seller issued licenses in License Manager

License Manager allows multiple users to concurrently consume entitlements, with limited
capabilities, from a single license. Call the [CheckoutLicense](../APIReference/API_CheckoutLicense.md "../APIReference/API_CheckoutLicense.md") API action. The
following is a description of the parameters.

- **Key fingerprint** – Trusted license
  issuer.

Example: aws:123456789012:issuer:issuer-fingerprint

- **Product SKU** – Product identifier for this
  license, as defined by the license issuer when creating the license. The same product
  SKU might exist across multiple ISVs. Therefore, trusted key fingerprints play an
  important role.

Example: 1a2b3c4d2f5e69f440bae30eaec9570bb1fb7358824f9ddfa1aa5a0daEXAMPLE

- **Entitlements** – Capabilities to check out.
  If you specify an unlimited capability, the quantity is zero. Example:

```
"Entitlements": [
    {
        "Name": "DataTransfer",
        "Unit": "Gigabytes",
        "Value": 10
    },
    {
        "Name": "DataStorage",
        "Unit": "Gigabytes",
        "Value": 5
    }
]
```

- **Beneficiary** – Software as a Service (SaaS)
  ISVs can check out licenses on behalf of a customer by including the customer
  identifier. License Manager limits the call to the repository of licenses created in the SaaS
  ISV account.

Example: user@domain.com

- **Node ID** – An identifier used to node-lock
  the license to a single instance of the application.

Example: 10.0.21.57
