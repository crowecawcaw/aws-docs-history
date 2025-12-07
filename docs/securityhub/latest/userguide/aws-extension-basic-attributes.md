# Basic attributes

These are fundamental attributes used for resource identification, location, and basic metadata.
They consist of simple data types such as strings, timestamps, and arrays.

## Cloud Partition

The cloud partition where the resource exists.

**Requirement**

Recommended

**Type**

String

**OCSF status**

Existing

**Example**

```
{
  "resources": [
    {
      "cloud_partition": "aws"
    }
  ]
}
```

## Owner account ID

A 12-digit account identifier that the resource belongs to.

**Requirement**

Recommended

**Type**

String

**OCSF status**

Existing

**Example**

```
{
  "resources": [
    {
      "owner": {
        "account": {
          "uid": "123456789012"
        }
      }
    }
  ]
}
```

## Resource Type

The AWS CloudFormation resource type that identifies the specific service and resource.

**Requirement**

Required

**Type**

String

**Format**

Must follow AWS CloudFormation resource type naming convention: `AWS::<Service>::<ResourceType>`

**OCSF status**

Existing

**Example**

```
{
  "resources": [
    {
      "type": "AWS::EC2::Instance"
    }
  ]
}
```

## Resource identifier

The unique identifier for the cloud resource (e.g. i-1234567890abcdef0).

**Requirement**

Recommended

**Type**

String

**Format**

Must be a valid resource identifier. Minimum length of 1. Maximum length of 768.

**OCSF status**

Existing

**Example**

```
{
  "resources": [
    {
      "uid": "i-1234567890abcdef0"
    }
  ]
}
```

## Alternate Resource Identifier

The unique identifier for the cloud resource, typically the Amazon Resource Name (ARN).

**Requirement**

Recommended

**Type**

String

**Format**

Should be a valid AWS ARN. Common patterns include:

- `"arn:partition:service:region:account-id:resource-id"`
- `"arn:partition:service:region:account-id:resource-type/resource-id"`
- `"arn:partition:service:region:account-id:resource-type:resource-id"`

Note: Some services like S3 use variations such as arn:aws:s3:::bucket-name (without region or account-id).

**OCSF status**

Existing

**Examples**

```
{
  "resources": [
    {
      "uid_alt": "arn:aws:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0"
    }
  ]
}
```

```
"{
  "resources": [
    {
      "uid_alt": "arn:aws:s3:::my-bucket-name"
    }
  ]
}"
```

## Resource Name

The unique name for the cloud resource.

**Requirement**

Recommended

**Type**

String

**Format**

User-created names whose values will depend on the environment.

**OCSF status**

Existing

**Example**

```
{
  "resources": [
    {
      "name": "My-Server-1"
    }
  ]
}
```

## Cloud Region

The AWS region where the resource is located.

**Requirement**

Recommended

**Type**

String

**Format**

Valid cloud region identifier (e.g., us-east-1, eu-west-1, ap-southeast-2)

**OCSF status**

Existing

**Example**

```
{
  "resources": [
    {
      "region": "us-west-2"
    }
  ]
}
```

## Resource Creation Time

The time when the resource was created.

**Requirement**

Recommended

**Type**

Timestamp

**Format**

Unix timestamp in milliseconds since epoch (January 1, 1970, 00:00:00 UTC)

**OCSF status**

Existing

**Example**

```
{
  "resources": [
    {
      "created_time": 1762019193000
    }
  ]
}
```

## Tags

Key-value pairs for resource metadata and organization.

**Requirement**

Recommended

**Type**

Array of key:value objects

**Format**

A generic object allowing to define a key:value pair.

**OCSF status**

Existing

**Example**

```
{
  "resources": [
    {
      "tags": [
        {
          "name": "Environment",
          "value": "Production"
        },
        {
          "name": "Owner",
          "value": "SecurityTeam"
        }
      ]
    }
  ]
}
```

## IP Address

The IP address associated with the instance in either IPv4 or IPv6 format.

**Requirement**

Optional

**Type**

String

**Format**

Valid IPv4 or IPv6 address

**OCSF status**

Existing

**Example**

```
{
  "resources": [
    {
      "ip": "10.0.1.25"
    }
  ]
}
```

## IP Addresses

An array of IP addresses (IPv4 or IPv6) associated with the device. These may include both public and private IP addresses.

**Requirement**

Optional

**Type**

Array of IP addresses

**OCSF status**

New

**Example**

```
{
  "resources": [
    {
      "ip_addresses": ["10.0.1.25", "52.12.34.56"]
    }
  ]
}
```

## VPC UID

The VPC ID where the resource is located.

**Requirement**

Optional

**Type**

String

**Format**

VPC identifier (e.g. vpc-12345678900)

**OCSF status**

Added to `resource_details`

**Example**

```
{
  "resources": [
    {
      "vpc_uid": "vpc-0a1b2c3d4e5f6g7h8"
    }
  ]
}
```

## Example resource object with basic attributes

```
{
  "resources": [
    {
      "cloud_partition": "aws",
      "owner": {
        "account": {
          "uid": "123456789012"
        }
      },
      "region": "us-east-1",
      "type": "AWS::EC2::NetworkInterface",
      "uid": "eni-03e6c892dd45e836c",
      "uid_alt": "arn:aws:ec2:us-east-1:123456789012:network-interface/eni-03e6c892dd45e836c",
      "zone": "us-east-1f",
      "vpc_uid": "vpc-0ef6045717b0362f6"
    }
  ]
}
```
