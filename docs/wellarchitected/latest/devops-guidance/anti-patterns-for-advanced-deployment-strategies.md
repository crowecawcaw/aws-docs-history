# Anti-patterns for advanced

deployment strategies

- **Deploying directly to
  production**: Deploying changes directly to
  production without first testing in pre-production
  environments risks unforeseen errors, bugs, or performance
  issues that can lead to service disruptions or downtime.
  Pre-production testing in environments that mimic
  production as closely as possible is crucial to verify the
  functionality and compatibility of changes under realistic
  conditions.
- **Ignoring rollbacks and data
  compatibility**: The absence of an automatic
  rollback strategy and a lack of consideration for data
  compatibility can lead to prolonged service disruptions
  and compatibility issues. An automatic rollback mechanism
  can reduce downtime and maintain system reliability as it
  ensures a quick return to a stable state in the event of a
  fault. Maintaining backward compatibility in data stores
  and schemas can prevent disruptions to existing
  functionalities and integration pipelines. Changes should
  be designed to coexist with previous data structures and
  contracts, allowing both old and new versions to operate
  concurrently.
- **Monolithic deployment
  model**: Deploying all changes simultaneously and
  treating the entire system as a single unit increases the
  risk of errors that could impact the entire system and
  limits scalability. To mitigate these risks, adopt
  staggered deployments and consider cell-based
  architectures. Staggering deployments through wave,
  one-box, or rolling deployments allows for easier issue
  detection and rollback which reduces negative impact of
  failed deployments. A cell-based architecture enhances
  fault isolation, granular control, and operational
  resilience, making it a preferred strategy for complex,
  distributed systems.
- **Abrupt feature release**:
  Releasing new features to all users at once without
  incremental deployment or testing can result in widespread
  disruptions if the feature fails or impacts the system
  negatively. Techniques like
  [dark
  launching](https://martinfowler.com/bliki/DarkLaunching.html "https://martinfowler.com/bliki/DarkLaunching.html"), two-phase deployments,
  [feature
  flags](https://aws.amazon.com/systems-manager/features/appconfig#Feature_flags "https://aws.amazon.com/systems-manager/features/appconfig#Feature_flags"), and canary releases reduce this risk by
  providing control and facilitating monitoring of the
  feature's impact in real-world conditions.
