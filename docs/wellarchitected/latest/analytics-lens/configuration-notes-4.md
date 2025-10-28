# Configuration notes

**Security:** Implement the principle of least privilege
throughout the visualization application stack. Ensure data sources are connected using VPCs
and restrict security groups to only the required protocols, sources, and destinations.
Enforce that the users as well as applications in every layer of the stack are given just the
right level of access permissions to data and the underlying resources. Ensure seamless
integration with identity providers—either industry supported or customized. To ease flow and
remove confusion, set up QuickSight and single sign-on (SSO) such that email addresses for end
users are automatically synced at their first login. In the case of multi-tenancy, use
namespaces for better isolation of principals and other assets across tenants. For example,
QuickSight follows the least privilege principle and access to AWS resources such as
Amazon Redshift, Amazon S3 or Amazon Athena (common services used in data warehouse, data lake or modern data
architectures) can be managed through the QuickSight user interface. Additional security at
the user or group level is supported using fine-grained access control through a combination
of IAM permissions. Additionally, QuickSight features, such as row level security, column
level security, and a range of asset governance capabilities that can be configured directly
through QuickSight user interface.

**Cost optimization:** Accurately identify the volume of
dashboard consumers and embedding requirements to determine the optimal pricing model for the
given visualization use case. QuickSight offers two different pricing options (capacity and
user based) that allows clients to implement cost-effective BI solutions. Capacity pricing
allows large-scale implementations and user-based pricing allows clients to get started with
minimal investment (Note: SPICE has a 500M records or 500 GB volume per dataset limitation).

**Low latency considerations:** Use in-memory caching option,
such as Memcached, Redis, or the in-memory caching engine in QuickSight called SPICE
(Super-fast, Parallel, In-memory Calculation Engine) to prevent latency in dashboard rendering
while accommodating any built-in restrictions that the caching technology might have.

**Pre-process data views:** Ensure that the data is cleansed,
standardized, enhanced, and pre-processed to allow analysis within the BI layer. If possible,
create pre-processed, pre-combined, pre-aggregated data views for analysis purposes. ETL
tools, such as AWS Glue DataBrew, or techniques, such as materialized views, can be employed to
achieve this. After uploading the dataset, users can add calculated fields to a dataset during
the data preparation or from the analysis page for additional insights provided data.
