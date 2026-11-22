

# AWS Glue support for Workday Live Data Query

AWS Glue supports Workday Live Data Query as follows:

**Supported as a source?**  
Yes. You can use AWS Glue ETL jobs to query data from Workday Live Data Query.

**Supported as a target?**  
No. The Workday Live Data Query connector is read-only.

**Supported AWS Glue versions**  
The following AWS Glue versions are supported:
+ AWS Glue 5.0
+ AWS Glue 6.0

**Supported authentication types**  
The Workday Live Data Query connector supports the `CUSTOM` authentication type. AWS Glue uses the OAuth 2.0 JWT bearer grant. It signs a JSON Web Token (JWT) with a private key that you store in AWS Secrets Manager, and then exchanges the JWT for an access token at your Workday OAuth 2.0 token endpoint. For more information, see [Configuring Workday Live Data Query connections](workday-ldq-configuring-connections.md).