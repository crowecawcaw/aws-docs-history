# Change management

| HPCREL02: How do you reliably manage software packages and dependencies across<br>users? |
| ---------------------------------------------------------------------------------------- |
|                                                                                          |

HPC workloads often consist of software packages with complex
dependencies. Managing software and dependencies, with specific
versioning requirements, across many users, can be complex.
Consider the following best practices when building out your
architecture.

## HPCREL02-BP01 Install software packages in a shared location to simplify multi-user,

multi-resource software requirements management

Installing software packages on shared storage, such as Amazon Elastic File System (EFS), allows users
across compute environments and clusters access the same versioned set of packages.
Dependencies can also be installed using a custom AMI, or using a post-install script, such
as configured with [AWS ParallelCluster](../../../parallelcluster/latest/ug/custom-bootstrap-actions-v3.md "../../../parallelcluster/latest/ug/custom-bootstrap-actions-v3.md").

### Implementation guidance

Install software in shared location for multi-user or multi-resource environments.
Single resource environments can use a custom AMI or separate Amazon Elastic Block Store (Amazon EBS) volume,
and multi-resource environments can use shared storage, such as Amazon Elastic File System (Amazon EFS).

## HPCREL02-BP02 Use package managers to simplify software dependency management when possible

Managing HPC applications can potentially be simplified with
package managers, such as Spack, SBGrid, and EasyBuild. AWS
hosts a Spack binary cache for fast installation of commonly
used HPC packages and applications. Leveraging a package manager
simplifies dependency management for system admins while
providing exact versioning per user requirements.

### Implementation guidance

Consider a package manager to simplify software dependencies.
