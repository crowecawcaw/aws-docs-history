# Definitions

**Foundations:**

- Foundational requirements are those whose scope extends beyond
  a single workload or project. Before architecting any system,
  foundational requirements that influence reliability should be
  in place.
- In an on-premises environment, these requirements can cause
  long lead times due to dependencies and therefore must be
  incorporated during initial planning. With AWS, however, most
  of these foundational requirements are already incorporated or
  can be addressed as needed. The cloud is designed to be nearly
  limitless, so it's the responsibility of AWS to satisfy the
  requirement for sufficient networking and compute capacity,
  leaving you free to change the end user computing environment
  on demand.

**Amazon WorkSpaces architecture:**

- A reliable Amazon WorkSpaces deployment starts with upfront
  design decisions for both software and infrastructure. Your
  architecture choices will impact your WorkSpaces behavior
  across the six Well-Architected pillars. For reliability,
  there are specific patterns you must follow to provide high
  availability and improve fault tolerance.
- Use Amazon Virtual Private Cloud (VPC) for network isolation
  and security.

**Change management:**

- Changes to your Amazon WorkSpaces environment must be
  anticipated and accommodated to achieve reliable operation.
  Changes include those imposed on your WorkSpaces, such as
  spikes in demand, as well as those from within, such as
  feature deployments and security patches.
- Use AWS CloudFormation, Service Catalog, or AWS Systems Manager to manage and automate changes to your WorkSpaces
  environment, creating consistency and reducing the risk of
  errors.

**Failure management:**

- Amazon WorkSpaces are deployed in a specific AWS Region with
  built-in redundancies to protect against component failures.
  This provides high availability and minimizes downtime.
- There is the potential for failures to impact your WorkSpaces
  environment. Therefore, you must take steps to implement
  resiliency if you need your WorkSpaces to be reliable.
- Spread awareness amongst the people designing, implementing,
  and operating your Amazon WorkSpaces about business objectives
  and the required reliability goals to achieve them. Leaders or
  system owners must provide training and guidance to verify
  that individuals understand and can design for the reliability
  requirements pertinent to their roles.
