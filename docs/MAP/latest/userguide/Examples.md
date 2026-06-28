# Other examples

Use the following examples to further help you tag your migrated workloads.

## Example 1: Re-hosting using AWS Transform MGN (MGN)

Use this example if you are moving from on-premises to AWS using a lift-and-shift
(re-hosting) migration pattern, and decided to use MGN for the migration.

Re-hosting using MGN with short ID example| Tag key (automated) | Tag value (automated) |
| --- | --- |
| `map-migrated` | `mig`5-digit MPE ID`` |

Re-hosting using MGN with long ID example| Tag key (automated) | Tag value (automated) |
| --- | --- |
| `map-migrated` | `mig`10 alphanumeric MPE ID characters`` |

###### Note

Use lowercase letters for the `mig` prefix and uppercase letters for the
alphanumeric MPE IDs (long MPE IDs). For more information about your MPE ID, see [MPE ID length](mpe-length.md "mpe-length.md").

## Example 2: DataCenter Migration (mix of migration patterns)

Use this example if you are moving different workloads from on-premises to AWS using
various migration patterns (re-hosting, re-architecting, etc.) as part of general MAP.

DataCenter migration (mix of migration patterns) with short ID example| Tag key | Tag value |
| --- | --- |
| `map-migrated` | `mig`5-digit MPE ID`` |

DataCenter migration (mix of migration patterns) with long ID example| Tag key | Tag value |
| --- | --- |
| `map-migrated` | `mig`10 alphanumeric MPE ID characters`` |

###### Note

Use lowercase letters for the `mig` prefix and uppercase letters for the
alphanumeric MPE IDs (long MPE IDs). For more information about your MPE ID, see [MPE ID length](mpe-length.md "mpe-length.md").

## Example 3: Migrate commercial database from EC2 to RDS

Use this example if you are moving a commercial databases from Amazon EC2 instances on AWS
to Amazon RDS as part of MAP for Database and Analytics.

Migrate commercial database from EC2 to RDS with short ID example| Tag key | Tag value |
| --- | --- |
| `map-migrated` | `comm_ec2_`5-digit MPE ID`` |

Migrate commercial database from EC2 to RDS with long ID example| Tag key | Tag value |
| --- | --- |
| `map-migrated` | `comm_ec2_`10 alphanumeric MPE ID<br>characters`` |

###### Note

Use lowercase letters for the `comm_ec2_` prefix and uppercase letters for the
alphanumeric MPE IDs (long MPE IDs). For more information about your MPE ID, see [MPE ID length](mpe-length.md "mpe-length.md").

## Example 4: Database modernization

Use this example if you are moving from on-premises commercial database server to Amazon DynamoDB. This example is for a Migration Plan that is eligible for Database & Analytics MAP
Credits.

Database modernization with short ID example| Tag key | Tag value |
| --- | --- |
| `map-migrated` | `comm`5-digit MPE ID`` |

Database modernization with long ID example| Tag key | Tag value |
| --- | --- |
| `map-migrated` | `comm`10 alphanumeric MPE ID<br>characters`` |

###### Note

Use lowercase letters for the `comm` prefix and uppercase letters for the
alphanumeric MPE IDs (long MPE IDs). For more information about your MPE ID, see [MPE ID length](mpe-length.md "mpe-length.md").
