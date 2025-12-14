# GAMEPERF01-BP03 Evaluate integration with other AWS services, development environments, target CPU architectures, and features

Evaluate how well each hosting option integrates with other AWS
services your game relies on, such as databases, analytics, or
content delivery services.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

**Integration with other AWS
services**

Seamless integration between services
provides operational benefits like improved performance monitoring
and efficient secure data delivery between game components, game
servers, game backend services and observability solutions.

For example, Coordinating traffic shifts for live games can be
complex. Amazon Route 53 will help keep your DNS records up to
date which simplifies coordinated traffic shifts. AWS Global Accelerator traffic dials enable you to send a percentage of
traffic to another Region and keep your game running during
maintenance.

**Development environment and
tools**

Consider the development tools, frameworks, and environments
supported by each architecture option. Verify that your chosen
option aligns with your game development solution and programming
languages, as this can impact your team's ability to optimize and
maintain game server performance. Delivering a game across mobile,
console, and PC will increase tooling and testing complexity.
Cross-system support is particularly important for multi-game
studios where centralized services can standardize development
best practices across titles.

**Target CPU architecture and
features**

Consider the performance profile of your game engine and game
server processes and the level of ARM support available. Evaluate
if you can benefit from improved price performance of ARM based
Graviton or x86 based AMD64 processors. Do you need to use Intel
features like AES-NI encryption, AVX or Turbo Boost? Review
[Dedicated
Host types](https://aws.amazon.com/ec2/dedicated-hosts/pricing/ "https://aws.amazon.com/ec2/dedicated-hosts/pricing/") to identify single versus multi-socket instance
families. When using a multi-socket instance family, consider NUMA
pinning and L3 cache sharing in your game server processes. Use
[C-state
and P-state](../../../AWSEC2/latest/UserGuide/processor_state_control.md "../../../AWSEC2/latest/UserGuide/processor_state_control.md") configuration to get the best performance for
your game by tuning frequency clock and reducing sleep levels.

### Implementation steps

- Select hosting options with seamless integration with AWS
  services like AWS Secrets Manager, ACM, and others to help
  streamline performance monitoring, secure data delivery, and
  reduce manual operational tasks.
- Verify compatibility between your hosting option and your
  development environment, frameworks, and programming
  languages to optimize and maintain server performance
  effectively.
- Evaluate CPU architecture requirements, leveraging Graviton
  for price-performance or x86 for specific features like
  AES-NI, AVX, and Turbo Boost, and optimize server
  performance with NUMA pinning and C-state/P-state tuning.
