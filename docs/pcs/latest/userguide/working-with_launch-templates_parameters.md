# Useful launch template

parameters

This section describes some launch template parameters that may be broadly useful with
AWS PCS.

## Turn on detailed CloudWatch

monitoring

You can enable collection of CloudWatch metrics at a shorter interval using a launch
template parameter.

AWS Management Console
On the console pages for creating or editing launch templates, this option is found
under the **Advanced details** section. Set **Detailed
CloudWatch monitoring** to _Enable._

YAML

```
Monitoring:
    Enabled: True
```

JSON

```
{"Monitoring": {"Enabled": "True"}}
```

For more information, see [Enable or turn off detailed
monitoring for your instances](../../../AWSEC2/latest/UserGuide/using-cloudwatch-new.md "../../../AWSEC2/latest/UserGuide/using-cloudwatch-new.md") in the _Amazon Elastic Compute Cloud User Guide for Linux
Instances_.

## Instance Metadata Service

Version 2 (IMDS v2)

Using IMDS v2 with EC2 instances offers significant security enhancements and helps
mitigate potential risks associated with accessing instance metadata in AWS environments.

AWS Management Console
On the console pages for creating or editing launch templates, this option is found
under the **Advanced details** section. Set **Metadata
accessible** to _Enabled_,
**Metadata version** to _V2 only (token
required)_, and **Metadata response hop limit** to
_4_.

YAML

```
MetadataOptions:
  HttpEndpoint: enabled
  HttpTokens: required
  HttpPutResponseHopLimit: 4
```

JSON

```
{
    "MetadataOptions": {
        "HttpEndpoint": "enabled",
        "HttpPutResponseHopLimit": 4,
        "HttpTokens": "required"
    }
}
```

.
