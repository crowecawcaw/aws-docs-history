# Table naming for S3 Storage Lens export to S3 Tables

When you export S3 Storage Lens metrics to S3 Tables, the tables are organized using Apache Iceberg catalog conventions with specific naming patterns to ensure compatibility and organization.

## Table location structure

The complete table location follows this pattern:

```
s3tablescatalog/aws-s3/<namespace>/<table-name>
```

### Table bucket name

**Table Bucket:**
`aws-s3`

The S3 Storage Lens export uses the `aws-s3` table bucket, which is the designated bucket for AWS S3-related system tables.

### Catalog name

**Catalog:**
`s3tablescatalog/aws-s3`

S3 Storage Lens tables are stored in the S3 catalog because Storage Lens provides insights about three types of S3 resources:

- Storage metrics
- Bucket properties
- API usage metrics

## Namespace naming convention

Namespaces organize tables within the catalog. For S3 Storage Lens, the namespace is derived from your Storage Lens configuration ID.

### Standard namespace format

For Storage Lens configuration IDs without dots (`.`):

```
lens_<configuration-id>_exp
```

**Example:** If your configuration ID is `my-lens-config`, the namespace will be:

```
lens_my-lens-config_exp
```

### Namespace format with dot character or uppercase letters handling

Storage Lens configuration IDs can contain dots (`.`) or uppercase letters (`A-Z`), but S3 Tables namespaces only support lowercase letters, numbers, hyphens (`-`), and underscores (`_`). When your configuration ID contains dots, they are converted to hyphens, uppercase letters are converted to lower case letters, and a hash suffix is added for uniqueness:

```
lens_<configuration-id-with-dots-or-uppercase-replaced>_exp_<7-char-hash>
```

**Example:** If your configuration ID is `my.LENS.config`, the namespace will be:

```
lens_my-lens-config_exp_a1b2c3d
```

Where `a1b2c3d` is the first 7 characters of the SHA-1 hash of the original configuration ID.

## Complete examples

For a Storage Lens configuration with ID `production-metrics`:

- **Table Bucket:**
  `aws-s3`
- **Catalog:**
  `s3tablescatalog/aws-s3`
- **Namespace:**
  `lens_production-metrics_exp`
- **Full Path:**
  `s3tablescatalog/aws-s3/lens_production-metrics_exp/<table-name>`

For a Storage Lens configuration with ID `prod.us.east.metrics`:

- **Table Bucket:**
  `aws-s3`
- **Catalog:**
  `s3tablescatalog/aws-s3`
- **Namespace:**
  `lens_prod-us-east-metrics_exp_f8e9a1b` (with hash)
- **Full Path:**
  `s3tablescatalog/aws-s3/lens_prod-us-east-metrics_exp_f8e9a1b/<table-name>`

## Table types

The following table shows the different types of tables created for S3 Storage Lens exports:

| Catalog                | Namespace                        | S3 table name                      | Description                                                                                             |
| ---------------------- | -------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------- |
| s3tablescatalog/aws-s3 | lens\_<conf_name>\_exp[\_<hash>] | default_storage_metrics            | This table contains the storage metrics for your Storage Lens configuration.                            |
| s3tablescatalog/aws-s3 | lens\_<conf_name>\_exp[\_<hash>] | default_activity_metrics           | This table contains the activity metrics for your Storage Lens configuration.                           |
| s3tablescatalog/aws-s3 | lens\_<conf_name>\_exp[\_<hash>] | expanded_prefixes_storage_metrics  | This table contains the storage metrics for all the prefixes in your Storage Lens configuration.        |
| s3tablescatalog/aws-s3 | lens\_<conf_name>\_exp[\_<hash>] | expanded_prefixes_activity_metrics | This table contains the activity metrics for all the prefixes in your Storage Lens configuration.       |
| s3tablescatalog/aws-s3 | lens\_<conf_name>\_exp[\_<hash>] | bucket_property_metrics            | This table contains the bucket property metrics for all the buckets in your Storage Lens configuration. |

## Next steps

- Learn about [Understanding S3 Storage Lens table schemas](storage-lens-s3-tables-schemas.md "storage-lens-s3-tables-schemas.md")
- Learn about [Permissions for S3 Storage Lens tables](storage-lens-s3-tables-permissions.md "storage-lens-s3-tables-permissions.md")
