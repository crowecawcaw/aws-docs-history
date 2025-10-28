# Anti-patterns for dynamic environment provisioning

- **Manual environment
  management**: Relying on manual provisioning and
  management of environments, or using uncoordinated
  scripts, can introduce inconsistencies and inefficiencies.
  Manual approaches are prone to errors and can slow down
  development. It's vital to transition towards an
  automated, code-based approach for environment management.
  This ensures enhanced repeatability and reliability, and
  also allows teams to maintain a consistent pace of
  development, ultimately reducing operational overheads.
- **Inflexible environment provisioning**: Provisioning
  _one-size-fits-all_ environments without considering the unique
  needs of different workloads or teams can restrict the ability of workloads to operate
  optimally. Not taking into account the diverse requirements of different teams or
  workloads can result in inefficiencies, operational burdens, and slowed
  innovation. Instead, a dynamic provisioning approach tailored to the specific needs of
  each workload, combined with equipping developers with self-service capabilities, can
  greatly improve resource utilization and cost efficiency.
- **Bypassing non-production testing
  for environment changes**: Implementing changes
  directly in the production landing zone or to environment
  baselines without prior testing in a mirrored
  non-production environment exposes the organization to
  unnecessary risks. Always test these large-scale changes
  in a safe, non-production environment to identify
  potential issues and mitigate them before they impact the
  production environment.
- **Allowing configuration
  drift**: Deviations in environment configurations
  can creep in due to manual changes or lack of consistent
  monitoring. This drift can compromise security, increase
  maintenance complexity, and lead to unpredictable
  outcomes. To counteract this, adopt tools and practices
  that continuously baseline environments to maintain the
  desired state and enforce uniform configurations.
- **Fragmented self-service tools**: Providing multiple,
  disjointed self-service tools for developers to manage environments can create
  confusion, result in inefficiencies, and make it harder to enforce standards and best
  practices. Integrating these functionalities into a unified developer portal helps
  ensure consistent practices, better governance, and smoother operations. This unified
  portal could include self-service capabilities from development lifecycle, quality
  assurance, and observability best practices, streamlining the developer experience.
