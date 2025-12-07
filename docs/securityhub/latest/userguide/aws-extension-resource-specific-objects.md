# Resource specific objects

These are complex nested objects that provide detailed information for specific resource types and services.
Each object contains multiple fields and sub-objects with service-specific configuration and metadata.

## Device

Enhanced cloud instance attributes for compute resources including encryption details, image information, instance profile, and launch time.

**Requirement**

Optional

**Type**

Object

**OCSF status**

Added to `resource_details`

- See the OCSF [Device](https://schema.ocsf.io/1.6.0/objects/device "https://schema.ocsf.io/1.6.0/objects/device") object definition.

AWS Extension adds the following attributes to this object:

- `encryption_details` - The encryption details of resource
- `image` - Image information
- `instance_profile` - The IAM instance profile to associate with the instance
- `launch_time` - The time the instance was launched
- `uid_alt` - Amazon Resource Name (ARN) of the resource

**Example**

```
{
  "device": {
    "image": {
      "uid": "ami-99999999",
      "name": "LoadTestAMI-Current"
    },
    "instance_profile": {
      "uid": "LoadTestingInstanceProfileId",
      "uid_alt": "arn:aws:iam::012345678999:instance-profile/generated"
    },
    "launch_time": 1762019193000,
    "launch_time_dt": "2025-08-02T02:05:06Z",
    "model": "m3.xlarge",
    "network_interfaces": [
      {
        "ip": "198.51.100.0",
        "security_groups": [
          {
            "name": "LoadTestingSecurityGroupName",
            "uid": "LoadTestingSecurityId"
          }
        ],
        "uid": "eni-abcdef12"
      }
    ],
    "type": "Virtual",
    "type_id": 6,
    "uid": "i-99999999"
  }
}

```

## Network Interface

Network interface details and configuration including attachments and security groups.

**Requirement**

Optional

**Type**

Object

**OCSF status**

Added to `resource_details`

- See the OCSF [Network Interface](https://schema.ocsf.io/1.6.0/objects/network_interface "https://schema.ocsf.io/1.6.0/objects/network_interface") object definition.

AWS Extension adds the following attributes to this object:

- `attachments` - Information about the network interface attachments
- `security_groups` - Array of security group unique identifiers
- `uid_alt` - Amazon Resource Name (ARN) of the resource

**Example**

```
{
  "network_interface": {
    "uid": "eni-0a1b2c3d4e5f6g7h8",
    "uid_alt": "arn:aws:ec2:us-east-1:123456789012:network-interface/eni-0a1b2c3d4e5f6g7h8",
    "name": "prod-web-server-eni",
    "attachments": [
      {
        "uid": "eni-attach-0abcd1234efgh5678",
        "instance_uid": "i-0123456789abcdef0",
        "name": "/dev/eth0",
        "state": "attached",
        "attach_time": 1762019193000
      }
    ],
    "security_groups": [
      {
        "uid": "sg-0a1b2c3d4e5f6g7h8",
        "name": "web-server-sg"
      },
      {
        "uid": "sg-9i8h7g6f5e4d3c2b1",
        "name": "ssh-access-sg"
      }
    ]
  }
}

```

## Storage Device

Storage device details including attachments, encryption, and snapshot information.

**Requirement**

Optional

**Type**

Object

**OCSF status**

New

The storage device object includes the following attributes:

- `name` - The name of the storage device
- `uid` - The unique identifier of the storage devices
- `attachments` - The storage device attachments
- `encryption_details` - The storage device encryption key
- `is_encrypted` - Whether the storage device is encrypted (required)
- `snapshot_id` - The storage device snapshot identifier
- `uid_alt` - Amazon Resource Name (ARN) of the resource

**Example**

```
{
  "storage_device": {
    "is_encrypted": false,
    "name": "LocalVolumeDeviceName1",
    "snapshot_id": "snap-12345678901234567",
    "uid": "vol-09d5050dea915943d",
    "uid_alt": "arn:aws:ec2:us-west-2:123456789000:volume/vol-09d5050dea915943d"
  }
}

```

## Database

Database instance attributes including engine type, endpoint, and user information.

**Requirement**

Optional

**Type**

Object

**OCSF status**

Added to `resource_details`

- See the OCSF [Database](https://schema.ocsf.io/1.6.0/objects/database "https://schema.ocsf.io/1.6.0/objects/database") object definition.

AWS Extension adds the following attributes to this object:

- `cluster_uid` - The database cluster identifier
- `db_endpoint` - The database endpoint
- `encryption_details` - The database encryption details
- `engine` - The database engine name (e.g. mysql)
- `is_encrypted` - Whether the database is encrypted
- `is_iam_authentication` - Whether IAM authentication is enabled
- `is_public` - Whether the database is publicly accessible
- `port` - The database port number
- `security_groups` - Array of VPC security groups associated with the database instance
- `snapshot_details` - The database snapshot details
- `status` - The database status (e.g. available)
- `subnet_group` - A database subnet group is a collection of subnets in a VPC
- `uid_alt` - Amazon Resource Name (ARN) of the resource
- `user` - The database user
- `version` - The database version

**Example**

```
{
  "database": {
    "cluster_uid": "SampleDBClusterId",
    "engine": "mysql",
    "is_iam_authentication": true,
    "is_public": false,
    "type": "Relational",
    "type_id": 1,
    "uid": "SampleDBId",
    "version": "13.6"
  }
}

```

## Database Cluster

Database instance attributes including engine type, endpoint, and user information.

**Requirement**

Optional

**Type**

Object

**OCSF status**

New

The database object includes the following attributes:

- `uid` - The unique identifier of the database cluster
- `uid_alt` - Amazon Resource Name (ARN) of the resource
- `name` - The name of the database cluster
- `status` - The database cluster status
- `engine` - The engine associated with the cluster
- `version` - The database cluster version
- `cluster_members` - List of database instances that are part of the cluster
- `security_groups` - Array of security groups associated with the cluster
- `is_encrypted` - Whether the database cluster is encrypted
- `is_iam_authentication` - Whether IAM authentication is enabled
- `encryption_details` - The database cluster encryption details
- `subnet_group` - The subnet group associated with the cluster
- `port` - The database cluster port number
- `zones` - List of availability zones
- `db_endpoint` - The database cluster endpoint
- `snapshot_details` - Details of the database snapshot

**Example**

```
{
  "db_cluster": {
    "uid": "production-aurora-cluster",
    "uid_alt": "arn:aws:rds:us-east-1:123456789012:cluster:production-aurora-cluster",
    "name": "production-aurora-cluster",
    "status": "available",
    "engine": "aurora-mysql",
    "version": "8.0.mysql_aurora.3.04.0",
    "cluster_members": [
      "instance-1",
      "instance-2"
    ],
    "security_groups": [
      {
        "uid": "sg-0a1b2c3d4e5f6g7h8",
        "name": "db-security-group"
      }
    ],
    "is_encrypted": true,
    "is_iam_authentication": true,
    "encryption_details": {
      "key_uid": "arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012"
    },
    "subnet_group": {
      "uid": "production-db-subnet-group"
    },
    "port": 3306,
    "zones": [
      "us-east-1a",
      "us-east-1b",
      "us-east-1c"
    ],
    "db_endpoint": {
      "name": "production-aurora-cluster.cluster-abc123xyz.us-east-1.rds.amazonaws.com",
      "port": 3306
    }
  }
}

```

## Cloud Function

Cloud function attributes for serverless functions including handler, layers, and runtime configuration.

**Requirement**

Optional

**Type**

Object

**OCSF status**

New

The cloud function object includes the following attributes:

- `name` - The name of the cloud function
- `uid` - The unique identifier of the cloud function
- `uid_alt` - Amazon Resource Name (ARN) of the resource
- `encryption_details` - The cloud function encryption details
- `handler` - The method in the function code that processes events
- `layers` - The list of cloud function layers that contain supplementary code or data
- `runtime` - The cloud function language-specific environment
- `security_groups` - Array of security groups associated with the cloud function
- `subnet_info_list` - Details about subnets associated with the cloud function
- `user` - Details about the IAM entity that grants the cloud_function permission to access services
- `version` - The cloud function version
- `vpc_uid` - The unique identifier of the VPC if the cloud function is in a VPC

**Example**

```
{
  "cloud_function": {
    "name": "my-lambda-function",
    "uid": "my-lambda-function",
    "uid_alt": "arn:aws:lambda:us-east-1:123456789012:function:my-lambda-function",
    "handler": "index.handler",
    "runtime": "python3.11",
    "version": "$LATEST",
    "layers": [
      {
        "name": "my-layer",
        "uid_alt": "arn:aws:lambda:us-east-1:123456789012:layer:my-layer:1",
        "version": "1"
      }
    ],
    "security_groups": [
      {
        "name": "lambda-security-group",
        "uid": "sg-0123456789abcdef0"
      }
    ],
    "subnet_info_list": [
      {
        "uid": "subnet-0a1b2c3d4e5f6g7h8"
      }
    ],
    "vpc_uid": "vpc-0ef6045717b0362f6"
  }
}

```

## Databucket

S3 bucket or data storage attributes.

**Requirement**

Optional

**Type**

Object

**OCSF status**

Added to `resource_details`

- See the OCSF [Databucket](https://schema.ocsf.io/1.6.0/objects/databucket "https://schema.ocsf.io/1.6.0/objects/databucket") object definition.

Note: This object is added to resource_details by the AWS Extension.
The core OCSF Databucket object is used without additional attributes.

**Example**

```
{
  "databucket": {
    "type": "S3",
    "type_id": 1,
    "uid": "my-bucket-name"
  }
}

```

## Image

Image information for compute resources including platform and usage details.

**Requirement**

Optional

**Type**

Object

**OCSF status**

Added to `resource_details`

- See the OCSF [Image](https://schema.ocsf.io/1.6.0/objects/image "https://schema.ocsf.io/1.6.0/objects/image") object definition.

AWS Extension adds the following attributes to this object:

- `platform` - The operating system platform of the image
- `in_use_count` - Count of resources using this image

**Example**

```
{
  "image": {
    "uid": "ami-0abcdef1234567890",
    "uid_alt": "arn:aws:ec2:us-east-1:123456789012:image/ami-0abcdef1234567890",
    "name": "my-custom-ami",
    "platform": "AMAZON_LINUX_2",
    "in_use_count": 2
  }
}

```

## Subnet Info

Details about the subnet where the resource is located.

**Requirement**

Optional

**Type**

Object

**OCSF status**

New

The subnet info object includes the following attributes:

- `uid` - The unique identifier of the subnet
- `uid_alt` - Amazon Resource Name (ARN) of the resource
- `name` - The name of the subnet
- `zone` - The availability zone
- `ip_count` - The number of IP addresses in the subnet
- `cidr_block` - The CIDR block of the subnet
- `is_default` - Whether this is the default subnet
- `is_public` - Whether the subnet is publicly accessible
- `state` - The state of the subnet
- `vpc_uid` - The VPC ID where the subnet is located

**Example**

```
{
  "subnet_info": {
    "uid": "subnet-0a1b2c3d4e5f6g7h8",
    "uid_alt": "arn:aws:ec2:us-east-1:123456789012:subnet/subnet-0a1b2c3d4e5f6g7h8",
    "name": "production-web-subnet-1a",
    "zone": "us-east-1a",
    "ip_count": 251,
    "cidr_block": "10.0.1.0/24",
    "is_default": false,
    "is_public": true,
    "state": "available",
    "vpc_uid": "vpc-0123456789abcdef0"
  }
}

```

## User

IAM user attributes including instance profiles and policies.

**Requirement**

Optional

**Type**

Object

**OCSF status**

Added to `resource_details`

- See the OCSF [User](https://schema.ocsf.io/1.6.0/objects/user "https://schema.ocsf.io/1.6.0/objects/user") object definition.

The user object includes the following attributes:

- `instance_profiles` - List of instance profiles attached to an cloud instance
- `policies` - Policies that assign permissions for users, groups, roles, and resources

**Example**

```
{
  "user": {
    "type_id": 1,
    "uid": "AIDACKCEVSQ6C2EXAMPLE",
    "uid_alt": "arn:aws:iam::123456789012:user/developers/john.doe",
    "name": "john.doe",
    "type": "User",
    "groups": [
      {
        "name": "Developers"
      },
      {
        "name": "ReadOnlyAccess"
      }
    ],
    "policies": [
      {
        "name": "AmazonS3ReadOnlyAccess"
      },
      {
        "name": "AmazonEC2ReadOnlyAccess"
      }
    ]
  }
}

```
