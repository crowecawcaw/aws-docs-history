End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October
7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure
will remain intact. For more information, see [AWS Proton Service Deprecation and Migration
Guide](proton-end-of-support.md "proton-end-of-support.md").

# AWS Proton terminology

**Environment template**

Defines shared infrastructure, such as a VPC or cluster, that is used by multiple applications or resources.

**Environment template bundle**

A collection of files that you upload to create and register an environment template in AWS Proton. An environment template bundle contains the
following:

1. A schema file that defines infrastructure as code input parameters.
2. An infrastructure as code (IaC) file that defines shared infrastructure, such as a VPC or cluster, that is used by multiple applications or
   resources.
3. A manifest file that lists the IaC file.

**Environment**

Provisioned shared infrastructure, such as a VPC or cluster, that is used by multiple applications or resources.

**Service template**

Defines the type of infrastructure that's needed to deploy and maintain an application or microservice in an environment.

**Service template bundle**

A collection of files that you upload to create and register a service template in AWS Proton. A service template bundle contains the
following:

1. A schema file that defines infrastructure as code (IaC) input parameters.
2. An IaC file that defines the infrastructure that's needed to deploy and maintain an application or microservice in an environment.
3. A manifest file that lists the IaC file.
4. Optional
   1. An IaC file that defines the service pipeline infrastructure.
   2. A manifest file that lists the IaC file.

**Service**

Provisioned infrastructure that's needed to deploy and maintain an application or microservice in an environment.

**Service instance**

Provisioned infrastructure that supports an application or microservice in an environment.

**Service pipeline**

Provisioned infrastructure that supports a pipeline.

**Template version**

A major or minor version of a template. For more information, see [Versioned templates](ag-template-versions.md "ag-template-versions.md").

**Input parameters**

Defined in a schema file and used in an infrastructure as code (IaC) file so that the IaC file can be used repeatably and for a variety of use
cases.

**Schema file**

Defines infrastructure as code file input parameters.

**Spec file**

Specifies values for infrastructure as code file input parameters, as defined in a schema file.

**Manifest file**

Lists an infrastructure as code file.
