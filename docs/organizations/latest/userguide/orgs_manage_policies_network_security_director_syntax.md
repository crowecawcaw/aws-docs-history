# AWS Shield Network Security Director policy

syntax and examples

Network Security Director policies follow a standardized JSON syntax that defines how Network Security
Director
is enabled and
configured across your organization. An AWS Shield Network Security Director policy is a JSON document structured
according to the AWS Organizations management-policy syntax. It defines which organizational entities will
have AWS Shield Network Security Director automatically enabled.

## Basic policy structure

An AWS Shield Network Security Director policy uses this basic structure:

```
{
    "network_security_director": {
        "enablement": {
            "network_security_scan": {
                "enable_in_regions": {
                    "@@assign": ["us-east-1", "eu-west-1"]
                },
                "disable_in_regions": {
                    "@@assign": []
                    }
                }
            },
        }
    }
}
```

## Policy components

AWS Shield Network Security Director policies contain these key components:

`network_security_director`

The top-level key for Network Security Director policy documents, which is required for all
Network Security Director policies.

`enablement`

Defines how Network Security Director is enabled across the organization, and contains scan configurations.

`network_security_scan`

Defines enforcement configuration for network security scanning.

`enable_in_regions`

Configuration identifier for region settings. Defines where the network security scan should be enabled.

`disable_in_regions`

Configuration identifier for region settings. Defines where the network security scan
should be disabled.
