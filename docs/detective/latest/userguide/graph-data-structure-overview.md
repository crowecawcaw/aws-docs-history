# Overview of the behavior graph data

structure

The behavior graph data structure defines the structure of the extracted and analyzed data.
It also defines how the source data is mapped to the behavior graph.

## Types of elements in the behavior graph data

structure

The behavior graph data structure is made up of the following information elements.

\***\*Entity\*\***

An entity represents an item extracted from the Detective source data.

Each entity has a type, which identifies the type of object it represents. Examples of
entity types include IP addresses, Amazon EC2 instances, and AWS users.

For each entity, the source data is also used to populate entity properties. Property
values might be extracted directly from source records or aggregated across multiple
records.

Some properties consist of a single scalar or aggregated value. For example, for an EC2
instance, Detective tracks the type of instance and the total number of bytes processed.

Time series properties track activity over time. For example, for an EC2 instance, Detective
tracks over time the unique ports that it used.

\***\*Relationships\*\***

A relationship represents activity occurring between individual entities. Relationships
are also extracted from the Detective source data.

Similar to an entity, a relationship has a type, which identifies the types of entities
involved and the direction of the connection. An example of a relationship type is IP
addresses connecting to EC2 instances.

For each individual relationship, such as a specific IP address connecting to a specific
instance, Detective tracks the occurrences over time.

## Types of entities in the behavior graph data structure

The behavior graph data structure consists of entity and relationship types that do the
following:

- Track the servers, IP addresses, and user agents being used
- Track the AWS users, roles, and accounts being used
- Track the network connections and authorizations that occur in your AWS
  environment

The behavior graph data structure contains the following entity types.

**AWS account**

AWS accounts that are present in the Detective source data.

For each account, Detective answers several questions:

- What API calls has the account used?
- What user agents has the account used?
- What autonomous system organizations (ASOs) has the account used?
- In what geographic locations has the account been active?

**AWS role**

AWS roles that are present in the Detective source data.

For each role, Detective answers several questions:

- What API calls has the role used?
- What user agents has the role used?
- What ASOs has the role used?
- In what geographic locations has the role been active?
- What resources have assumed this role?
- What roles has this role assumed?
- What role sessions have involved this role?

**AWS user**

AWS users that are present in the Detective source data.

For each user, Detective answers several questions:

- What API calls has the user used?
- What user agents has the user used?
- In what geographic locations has the user been active?
- What roles has this user assumed?
- What role sessions have involved this user?

**Federated user**

Instances of a federated user. Examples of federated users include the following:

- An identity that logs in using Security Assertion Markup Language (SAML)
- An identity that logs in using web identity federation

For each federated user, Detective answers these questions:

- What identity provider did the federated user authenticate with?
- What was the audience of the federated user? The audience identifies the application
  that requested the web identity token of the federated user.
- In what geographic locations has the federated user been active?
- What user agents has the federated user used?
- What ASOs has the federated user used?
- What roles has this federated user assumed?
- What role sessions have involved this federated user?

**EC2 instance**

EC2 instances that are present in the Detective source data.

For EC2 instances, Detective answers several questions:

- What IP addresses have communicated with the instance?
- What ports have been used to communicate with the instance?
- What volume of data has been sent to and from the instance?
- What VPC contains the instance?
- What API calls has the EC2 instance used?
- What user agents has the EC2 instance used?
- What ASOs has the EC2 instance used?
- In what geographic locations has the EC2 instance been active?
- What roles has the EC2 instance assumed?

**Role session**

Instances of a resource that is assuming a role. Each role session is identified by the
role identifier and a session name.

For each role, Detective answers several questions:

- What resources were involved in this role session? In other words, what role was
  assumed, and what resource assumed the role?

Note that for cross-account role assumption, Detective cannot identify the resource that
assumed the role.

- What API calls has the role session used?
- What user agents has the role session used?
- What ASOs has the role session used?
- In what geographic locations has the role session been active?
- What user or role started this role session?
- What role sessions started from this role session?

**Finding**

Findings uncovered by Amazon GuardDuty that are fed into the Detective source data.

For each finding, Detective tracks the finding type, origin, and the time window for the
finding activity.

It also stores information specific to the finding, such as roles or IP addresses that
are involved in the detected activity.

**IP address**

IP addresses that are present in the Detective source data.

For each IP address, Detective answers several questions:

- What API calls has the address used?
- What ports has the address used?
- What users and user agents have used the IP address?
- In what geographic locations has the IP address been active?
- What EC2 instances has this IP address been assigned to and communicated with?

**S3 bucket**

S3 buckets that are in the Detective source data.

For each S3 bucket, Detective answers these questions:

- What principals interacted with the S3 bucket?
- What API calls were made to the S3 bucket?
- From what geographic locations did principals make API calls to the S3 bucket?
- What user agents were used to interact with the S3 bucket?
- What ASOs were used to interact with the S3 bucket?

You can delete an S3 bucket and then create a new bucket with the same name. Because
Detective uses the S3 bucket name to identify the S3 bucket, it treats these as a single S3
bucket entity. On the entity profile, **Creation time** is the first
creation time. **Deletion time** is the most recent deletion time.

To view all of the creation and deletion events, set the scope time to start with the
creation time and end with the deletion time. On
the **Overall API call volume** profile panel, display the activity details
for the scope time. Filter the API methods to show `Create` and
`Delete` methods. See [Activity details for Overall API
call volume](profile-panel-drilldown-overall-api-volume.md "profile-panel-drilldown-overall-api-volume.md").

**User agent**

User agents that are present in the Detective source data.

For each user agent, Detective answers questions such as the following:

- What API calls has the user agent used?
- What users and roles have used the user agent?
- What IP addresses have used the user agent?

**EKS Cluster**

EKS clusters that are present in the Detective source data.

###### Note

To see complete details for this entity type the optional EKS audit logs data source must be enabled. For more info see [Optional data sources](detective-source-data-about.md#source-data-types-optional "detective-source-data-about.md#source-data-types-optional")

For each EKS cluster, Detective answers questions such as the following:

- What Kubernetes API calls have been run in this cluster?
- What Kubernetes users and service accounts (subjects) are active in this cluster?
- What containers have been launched in this cluster?
- What images are used to launch containers in this cluster?

**Kubernetes Pod**

Kubernetes pods that are present in the Detective source data.

###### Note

To see complete details for this entity type the optional EKS audit logs data source must be enabled. For more info see [Optional data sources](detective-source-data-about.md#source-data-types-optional "detective-source-data-about.md#source-data-types-optional")

For each pod, Detective answers questions such as the following:

- What container images in this pod are common in my accounts?
- What activity has been directed at this pod?
- What containers run in this pod?
- Are registries from containers in this pod common in my accounts?
- What other containers are running in the other pods of the workload?
- Are there any anomalous containers in this pod that are not in the other pods of the workload?

**Container Image**

Container images that are present in the Detective source data.

###### Note

To see complete details for this entity type the optional EKS audit logs data source must be enabled. For more info see [Optional data sources](detective-source-data-about.md#source-data-types-optional "detective-source-data-about.md#source-data-types-optional")

For each container image, Detective answers questions such as the following:

- What other images in my environment share the same repository or registry with this image?
- How many copies of this image are running in my environment?

**Kubernetes Subject**

Kubernetes subjects that are present in the Detective source data. A Kubernetes subject is a user or service account.

###### Note

To see complete details for this entity type the optional EKS audit logs data source must be enabled. For more info see [Optional data sources](detective-source-data-about.md#source-data-types-optional "detective-source-data-about.md#source-data-types-optional")

For each subject, Detective answers questions such as the following:

- What IAM principals have authenticated as this subject?
- What findings are associated with this subject?
- What IP addresses is the subject using?
