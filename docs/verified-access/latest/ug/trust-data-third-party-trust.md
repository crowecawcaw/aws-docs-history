# Third-party trust provider context for Verified Access trust data

This section describes the trust data provided to AWS Verified Access by third-party trust
providers.

###### Note

The context key for your trust provider comes from the policy reference name that you
configure when you create the trust provider. For example, if you configure the policy
reference name as "idp123", the context key will be "context.idp123". Ensure you are using
the correct context key when you create the policy.

###### Contents

- [Browser extension](#trust-data-browser "#trust-data-browser")
- [Jamf](#trust-data-iam-jamf "#trust-data-iam-jamf")
- [CrowdStrike](#trust-data-iam-cs "#trust-data-iam-cs")
- [JumpCloud](#trust-data-jc "#trust-data-jc")

## Browser extension

If you plan to incorporate device trust context into your access policies, then you will
need either the AWS Verified Access browser extension, or another partner's browser extension. Verified Access currently supports Google Chrome
and Mozilla Firefox browsers.

We currently support three device trust providers: Jamf (which supports macOS devices), CrowdStrike (which supports Windows 11 and Windows 10 devices), and JumpCloud (which supports both Windows and MacOS).

- If you're using **Jamf** trust data in your policies,
  your users must download and install the AWS Verified Access browser extension from the [Chrome web store](https://chromewebstore.google.com/category/extensions "https://chromewebstore.google.com/category/extensions")
  or [Firefox Add-on site](https://addons.mozilla.org/en-US/firefox/ "https://addons.mozilla.org/en-US/firefox/") on
  their devices.
- If you are using **CrowdStrike** trust data in your
  policies, first your users need to install the [AWS Verified Access Native Messaging Host](https://d3p8dc6667u8pq.cloudfront.net/WPF/latest/AWS_Verified_Access_Native_Messaging_Host.msi "https://d3p8dc6667u8pq.cloudfront.net/WPF/latest/AWS_Verified_Access_Native_Messaging_Host.msi") (direct download link). This component is
  required to get the trust data from the CrowdStrike agent running on users’ devices.
  Then, after installing this component, users must install the AWS Verified Access browser
  extension from the [Chrome web store](https://chromewebstore.google.com/category/extensions "https://chromewebstore.google.com/category/extensions") or [Firefox Add-on site](https://addons.mozilla.org/en-US/firefox/ "https://addons.mozilla.org/en-US/firefox/") on their devices.
- If you're using **JumpCloud**,
  your users must have the JumpCloud browser extension from the
  [Chrome web
  store](https://chromewebstore.google.com/category/extensions "https://chromewebstore.google.com/category/extensions") or [Firefox
  Add-on site](https://addons.mozilla.org/en-US/firefox/ "https://addons.mozilla.org/en-US/firefox/") installed on their devices.

## Jamf

Jamf is a third-party trust provider. When a policy is evaluated, if you define Jamf
as a trust provider, Verified Access includes the trust data in the Cedar context under the key you
specify as “Policy Reference Name” on the trust provider configuration. You can write a
policy that evaluates against the trust data if you choose. The following [JSON schema](https://json-schema.org/ "https://json-schema.org/") shows which data is included in the
evaluation.

For more information about using Jamf with Verified Access, see [Integrating AWS Verified Access with Jamf Device Identity](https://docs.jamf.com/technical-papers/jamf-security/aws-verified-access/index.html "https://docs.jamf.com/technical-papers/jamf-security/aws-verified-access/index.html") on the Jamf
website.

```
{
    "title": "Jamf device data specification",
    "type": "object",
    "properties": {
        "iss": {
            "type": "string",
            "description": "\"Issuer\" - the Jamf customer ID"
        },
        "iat": {
            "type": "integer",
            "description": "\"Issued at Time\" - a unixtime (seconds since epoch) value of when the device information data was generated"
        },
        "exp": {
            "type": "integer",
            "description": "\"Expiration\" - a unixtime (seconds since epoch) value for when this device information is no longer valid"
        },
        "sub": {
            "type": "string",
            "description": "\"Subject\" - either the hardware UID or a value generated based on device location"
        },
        "groups": {
            "type": "array",
            "description": "Group IDs from UEM connector sync",
            "items": {
                "type": "string"
            }
        },
        "risk": {
            "type": "string",
            "enum": [
                "HIGH",
                "MEDIUM",
                "LOW",
                "SECURE",
                "NOT_APPLICABLE"
            ],
            "description": "a Jamf-reported level of risk associated with the device."
        },
        "osv": {
            "type": "string",
            "description": "The version of the OS that is currently running, in Apple version number format (https://support.apple.com/en-us/HT201260)"
        }
    }
}
```

The following is an example of a policy that evaluates against the trust data provided
by Jamf.

```
permit(principal, action, resource) when {
   context.jamf.risk == "LOW"
};
```

Cedar provides a useful `.contains()` function to help with enums like
Jamf’s risk score.

```
permit(principal, action, resource) when {
   ["LOW", "SECURE"].contains(context.jamf.risk)
};
```

## CrowdStrike

CrowdStrike is a third-party trust provider. When a policy is evaluated, if you define
CrowdStrike as a trust provider, Verified Access includes the trust data in the Cedar context under
the key you specify as “Policy Reference Name” on the trust provider configuration. You can
write a policy that evaluates against the trust data if you choose. The following [JSON schema](https://json-schema.org/ "https://json-schema.org/") shows which data is included in the
evaluation.

For more information about using CrowdStrike with Verified Access, see [Securing private applications
with CrowdStrike and AWS Verified Access](https://github.com/CrowdStrike/aws-verified-access/ "https://github.com/CrowdStrike/aws-verified-access/") on the GitHub website.

```
{
  "title": "CrowdStrike device data specification",
  "type": "object",
  "properties": {
    "assessment": {
      "type": "object",
      "description": "Data about CrowdStrike's assessment of the device",
      "properties": {
        "overall": {
          "type": "integer",
          "description": "A single metric, between 1-100, that accounts as a weighted average of the OS and and Sensor Config scores"
        },
        "os": {
          "type": "integer",
          "description": "A single metric, between 1-100, that accounts for the OS-specific settings monitored on the host"
        },
        "sensor_config": {
          "type": "integer",
          "description": "A single metric, between 1-100, that accounts for the different sensor policies monitored on the host"
        },
        "version": {
          "type": "string",
          "description": "The version of the scoring algorithm being used"
        }
      }
    },
    "cid": {
      "type": "string",
      "description": "Customer ID (CID) unique to the customer's environment"
    },
    "exp": {
      "type": "integer",
      "description": "unixtime, The expiration time of the token"
    },
    "iat": {
      "type": "integer",
      "description": "unixtime, The issued time of the token"
    },
    "jwk_url": {
      "type": "string",
      "description": "URL that details the JWT signing"
    },
    "platform": {
      "type": "string",
      "enum": ["Windows 10", "Windows 11", "macOS"],
      "description": "Operating system of the endpoint"
    },
    "serial_number": {
      "type": "string",
      "description": "The serial number of the device derived by unique system information"
    },
    "sub": {
      "type": "string",
      "description": "Unique CrowdStrike Agent ID (AID) of machine"
    },
    "typ": {
      "type": "string",
      "enum": ["crowdstrike-zta+jwt"],
      "description": "Generic name for this JWT media. Client MUST reject any other type"
    }
  }
}
```

The following is an example of a policy that evaluates against the trust data provided
by CrowdStrike.

```
permit(principal, action, resource) when {
   context.crowdstrike.assessment.overall > 50
};
```

## JumpCloud

JumpCloud is a third-party trust provider. When a policy is evaluated, if you define
JumpCloud as a trust provider, Verified Access includes the trust data in the Cedar context
under the key you specify as “Policy Reference Name” on the trust provider configuration.
You can write a policy that evaluates against the trust data if you choose. The following
[JSON schema](https://json-schema.org/ "https://json-schema.org/") shows which data is included
in the evaluation.

For more information about using JumpCloud with AWS Verified Access, see [Integrating JumpCloud and AWS Verified Access](https://jumpcloud.com/support/integrate-with-aws-verified-access "https://jumpcloud.com/support/integrate-with-aws-verified-access") on the JumpCloud website.

```
{
  "title": "JumpCloud device data specification",
  "type": "object",
  "properties": {
    "device": {
      "type": "object",
      "description": "Properties of the device",
      "properties": {
        "is_managed": {
          "type": "boolean",
          "description": "Boolean to indicate if the device is under management"
        }
      }
    },
    "exp": {
      "type": "integer",
      "description": "Expiration. Unixtime of the token's expiration."
    },
    "durt_id": {
      "type": "string",
      "description": "Device User Refresh Token ID. Unique ID that represents the device + user."
    },
    "iat": {
      "type": "integer",
      "description": "Issued At. Unixtime of the token's issuance."
    },
    "iss": {
      "type": "string",
      "description": "Issuer. This will be 'go.jumpcloud.com'"
    },
    "org_id": {
      "type": "string",
      "description": "The JumpCloud Organization ID"
    },
    "sub": {
      "type": "string",
      "description": "Subject. The managed JumpCloud user ID on the device."
    },
    "system": {
      "type": "string",
      "description": "The JumpCloud system ID"
    }
  }
}
```

The following is an example of a policy that evaluates against the trust context provided
by JumpCloud.

```
permit(principal, action, resource) when {
   context.jumpcloud.org_id == 'Unique_organization_identifier'
};
```
