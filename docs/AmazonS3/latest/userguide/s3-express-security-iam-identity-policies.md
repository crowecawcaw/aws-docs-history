# IAM identity-based policies
 for directory buckets

Before you can create directory buckets, you must grant the necessary permissions to your
 AWS Identity and Access Management (IAM) role or users. This example policy allows access to the
 `CreateSession` API operation (for use with Zonal endpoint [object level] API
 operations) and all of the Regional endpoint (bucket-level) API operations. This policy
 allows the `CreateSession` API operation for use with all directory buckets, but
 the Regional endpoint API operations are allowed only for use with the specified directory
 bucket. To use this example policy, replace the ``user input
 placeholders`` with your own information.
