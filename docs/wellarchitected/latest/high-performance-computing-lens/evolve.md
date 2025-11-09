# Evolve

| HPCOPS07: What mechanisms are you using to keep your environment updated with<br>relevant service, product, and software improvements? |
| -------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                        |

Having designed your system to allow for upgrades and modular
additions of new components, consider how you can keep up to date
with and test the latest releases of services, products and
software.

- Consider evolving the way your users interact with the
  environment and carry out their operations.
- Look at offering additional functionality to encourage the
  behavior of end users. For example, offering additional
  compute instances for different stages of users' workflows.
- Educate users on the differences between environments to help
  them make choices, such as by providing demonstrations of new
  workload specific solutions that reduce their operational
  overhead.
- Collect end-user feedback on the systems already in place, and
  implement mechanisms to respond to requests and explore
  options to evolve your environment or highlight areas to
  educate end-users.

## HPCOPS07-BP01 Review and test the latest service, product and software updates for business fit and reduction in operational overhead

Consider creating a test environment where you can review your
representative workload benchmarks on new instances and software
versions. If using AWS Organizations, create your test
environment within a designated Sandbox organizational unit
(OU). For more information, see
[Organizing
Your AWS Environment Using Multiple Accounts](../../../whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.md "../../../whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.md"). Consider
also new storage options and configurations which may offer
additional functionality such as increased resiliency. Software
updates such as communication library upgrades can provide
performance improvements on existing hardware, and so should
also be tested periodically with your representative benchmarks,
as well as new functionality that can improve the user
experience.

In addition to performance improvements, new services and
products may offer reduced operational overhead. This may be by
managing more of the operations of the cluster for you in a
prescriptive approach, or may be by offering domain or workload
specific interfaces that make it easier for end-users to
interact with the system and reduce the customization you have
to maintain from a single generic environment. By being able to
integrate these new modules into your existing environment, for
example by mounting the same file systems, you can enable
experimentation and provide a mechanism to asses business fit.

### Implementation guidance

Test the latest versions of your chosen products, and review the latest HPC on AWS
news.

If using AWS ParallelCluster, periodically deploy test
environments with the latest release, as these often have
software upgrades included. New major releases also often add
new functionality that you can explore to see if it helps your
use case. AWS Parallel Computing Service is a good example of
a service that offers a way for you to reduce your operational
overhead in the management of your cluster, and introduces
prescriptive implementations of patterns and features that are
commonly required in HPC environments.

To keep updated on new releases relevant to the HPC space more
broadly and learn from continuously evolving best practices,
periodically review the
[AWS HPC community
site, Day1HPC](https://day1hpc.com/ "https://day1hpc.com/"). Updates such as new instance launches
can offer price and performance improvements, and new features
can improve the end-user experience or reduce your operations
management overhead.
