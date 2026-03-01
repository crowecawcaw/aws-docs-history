# Associate Connection Functions with distributions

After publishing a Connection Function to the LIVE stage, you must associate it with an mTLS-enabled distribution to handle live connections. Connection functions are associated at the distribution level, unlike viewer request and viewer response functions which are associated with cache behaviors.

###### Topics

- [Association requirements](#connection-function-association-requirements "#connection-function-association-requirements")
- [Organizing functions with filters](#connection-function-organizing-filters "#connection-function-organizing-filters")
- [Deployment considerations](#connection-function-deployment-considerations "#connection-function-deployment-considerations")

## Association requirements

To associate a Connection Function with a distribution:

- The function must be in the LIVE stage
- The distribution must have mTLS enabled
- The distribution must have a valid trust store configured
- You can only associate one Connection Function per distribution

## Organizing functions with filters

CloudFront provides filtering capabilities to help you organize and manage connection
functions:

- **Distribution ID filter** – Find functions
  associated with specific distributions
- **Key-value store filter** – Find functions
  that use specific key-value stores for data lookup
- **Stage filter** – List functions in
  DEVELOPMENT or LIVE stage

Use these filters when managing multiple Connection Functions across different
distributions or development environments.

## Deployment considerations

Consider these factors when deploying Connection Functions:

- **Global deployment** – Connection functions
  deploy to all CloudFront edge locations worldwide, which may take several
  minutes
- **Version management** – Each published
  version creates a new LIVE function that replaces the previous
  version
- **Rollback strategy** – Plan for rollback by
  keeping previous working versions of your function code
- **Testing in production** – Consider using
  separate distributions for staging and production environments
