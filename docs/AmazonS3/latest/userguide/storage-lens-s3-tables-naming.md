

# Table naming for S3 Storage Lens export to S3 Tables
<a name="storage-lens-s3-tables-naming"></a>

When you export S3 Storage Lens metrics to S3 Tables, the tables are organized using Apache Iceberg catalog conventions with specific naming patterns to ensure compatibility and organization.

## Table location structure
<a name="storage-lens-s3-tables-naming-location"></a>

The complete table location follows this pattern:

```
s3tablescatalog/aws-s3/<namespace>/<table-name>
```

### Table bucket name
<a name="storage-lens-s3-tables-naming-bucket"></a>

 **Table Bucket:** `aws-s3` 

The S3 Storage Lens export uses the `aws-s3` table bucket, which is the designated bucket for AWS S3-related system tables.

### Catalog name
<a name="storage-lens-s3-tables-naming-catalog"></a>

 **Catalog:** `s3tablescatalog/aws-s3` 

S3 Storage Lens tables are stored in the S3 catalog because Storage Lens provides insights about three types of S3 resources:
+ Storage metrics
+ Bucket properties
+ API usage metrics

## Namespace naming convention
<a name="storage-lens-s3-tables-naming-namespace"></a>

Namespaces organize tables within the catalog. For S3 Storage Lens, the namespace is derived from your Storage Lens configuration ID.

### Standard namespace format
<a name="storage-lens-s3-tables-naming-namespace-standard"></a>

For Storage Lens configuration IDs without dots (`.`): 

```
lens_<configuration-id>_exp
```

 **Example:** If your configuration ID is `my-lens-config`, the namespace will be:

```
lens_my-lens-config_exp
```

### Namespace format with dot character or uppercase letters handling
<a name="storage-lens-s3-tables-naming-namespace-dots"></a>

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
<a name="storage-lens-s3-tables-naming-examples"></a>

For a Storage Lens configuration with ID `production-metrics`: 
+  **Table Bucket:** `aws-s3` 
+  **Catalog:** `s3tablescatalog/aws-s3` 
+  **Namespace:** `lens_production-metrics_exp` 
+  **Full Path:** `s3tablescatalog/aws-s3/lens_production-metrics_exp/<table-name>` 

For a Storage Lens configuration with ID `prod.us.east.metrics`: 
+  **Table Bucket:** `aws-s3` 
+  **Catalog:** `s3tablescatalog/aws-s3` 
+  **Namespace:** `lens_prod-us-east-metrics_exp_f8e9a1b` (with hash)
+  **Full Path:** `s3tablescatalog/aws-s3/lens_prod-us-east-metrics_exp_f8e9a1b/<table-name>` 

## Table types
<a name="storage-lens-s3-tables-naming-types"></a>

The following table shows the different types of tables created for S3 Storage Lens exports:


| Catalog | Namespace | S3 table name | Description | 
| --- | --- | --- | --- | 
| s3tablescatalog/aws-s3 | lens\_<conf\_name>\_exp[\_<hash>] | default\_storage\_metrics | This table contains the storage metrics for your Storage Lens configuration. | 
| s3tablescatalog/aws-s3 | lens\_<conf\_name>\_exp[\_<hash>] | default\_activity\_metrics | This table contains the activity metrics for your Storage Lens configuration. | 
| s3tablescatalog/aws-s3 | lens\_<conf\_name>\_exp[\_<hash>] | expanded\_prefixes\_storage\_metrics | This table contains the storage metrics for all the prefixes in your Storage Lens configuration. | 
| s3tablescatalog/aws-s3 | lens\_<conf\_name>\_exp[\_<hash>] | expanded\_prefixes\_activity\_metrics | This table contains the activity metrics for all the prefixes in your Storage Lens configuration. | 
| s3tablescatalog/aws-s3 | lens\_<conf\_name>\_exp[\_<hash>] | bucket\_property\_metrics | This table contains the bucket property metrics for all the buckets in your Storage Lens configuration. | 

## Next steps
<a name="storage-lens-s3-tables-naming-next-steps"></a>
+ Learn about [Understanding S3 Storage Lens table schemas](storage-lens-s3-tables-schemas.md) 
+ Learn about [Permissions for S3 Storage Lens tables](storage-lens-s3-tables-permissions.md) 