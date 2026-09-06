

# Useful launch template parameters
<a name="working-with_launch-templates_parameters"></a>

This section describes some launch template parameters that may be broadly useful with AWS PCS.

## Turn on detailed CloudWatch monitoring
<a name="working-with_launch-templates_parameters_cw"></a>

You can enable collection of CloudWatch metrics at a shorter interval using a launch template parameter.

------
#### [ AWS Management Console ]

On the console pages for creating or editing launch templates, this option is found under the **Advanced details** section. Set **Detailed CloudWatch monitoring** to *Enable.*

------
#### [ YAML ]

```
Monitoring:
    Enabled: True
```

------
#### [ JSON ]

```
{"Monitoring": {"Enabled": "True"}}
```

------

For more information, see [Enable or turn off detailed monitoring for your instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch-new.html) in the *Amazon Elastic Compute Cloud User Guide for Linux Instances*.

## Instance Metadata Service Version 2 (IMDS v2)
<a name="working-with_launch-templates_parameters_imds2"></a>

Using IMDS v2 with EC2 instances offers significant security enhancements and helps mitigate potential risks associated with accessing instance metadata in AWS environments. 

------
#### [ AWS Management Console ]

On the console pages for creating or editing launch templates, this option is found under the **Advanced details** section. Set **Metadata accessible** to *Enabled*, **Metadata version** to *V2 only (token required)*, and **Metadata response hop limit** to *4*.

------
#### [ YAML ]

```
MetadataOptions:
  HttpEndpoint: enabled
  HttpTokens: required
  HttpPutResponseHopLimit: 4
```

------
#### [ JSON ]

```
{
    "MetadataOptions": {
        "HttpEndpoint": "enabled",
        "HttpPutResponseHopLimit": 4,
        "HttpTokens": "required"
    }
}
```

------

.