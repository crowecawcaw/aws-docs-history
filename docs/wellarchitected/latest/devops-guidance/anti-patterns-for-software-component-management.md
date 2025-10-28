# Anti-patterns for software component management

- **Avoiding version control:** Not using version control
  means that there's no historical record of code changes. This makes it hard to track
  down when a bug was introduced, who made specific changes, or how to roll back to a
  previous state leading to increased debugging time, potential loss of code, inability to
  collaborate effectively, and no traceability of changes. Use version control systems
  like Git for both code and infrastructure (IaC). Make sure to commit frequently with
  meaningful commit messages and maintain a clear change log.
- **Mutable artifacts:** Permitting alterations to existing
  artifacts in artifact repositories and registries undermines the integrity of the
  software supply chain. Instead, artifacts should be made immutable. Immutable artifacts
  help ensure consistent deployments and rollbacks. Mutable artifacts, on the other hand,
  introduce unpredictability and can be a vector for malicious alterations. Artifacts
  stored should be immutable with access control preventing overwriting or modifying
  existing artifacts.
- **Ignoring dependencies management:** A significant portion
  of modern applications consists of third-party libraries or dependencies. Ignoring these
  can introduce hidden vulnerabilities, versioning conflicts, or deprecated
  functionalities. This can lead to security breaches, unexpected behavior in
  applications, and makes debugging more challenging. Adopt a comprehensive dependency
  management strategy that not only tracks direct dependencies but also transitive
  (dependencies of dependencies). Use tools to regularly scan for vulnerabilities in your
  dependencies and update them as needed. Keep a centralized inventory of third-party
  dependencies that can be audited. Only grant build systems usage to trusted sources or
  specific repositories that have been approved.
- **Using git submodules for sharing common code:** Git
  submodules can introduce a layer of complexity in development. It is easy to end up with
  a parent repository pointing to an outdated or even deleted commit in the submodule.
  Submodules can also introduce recursive nesting. This complexity can hinder development
  speed, increase the risk of errors, and introduce potential security concerns if a
  submodule is compromised. Consider alternative strategies such as monorepos for
  large-scale projects or microservices for better separation of concerns. Package
  managers can be used to share common libraries across multiple projects without the
  complexity of submodules.
- **Traditional branching strategies:** Traditional branching
  strategies, like GitFlow, involve multiple long-lived branches like feature, release,
  and hotfix, which can add overhead to the development process. For most modern web-based
  applications, especially those using continuous integration and continuous delivery
  (CI/CD) pipelines, this can slow down the release pace, extend integration times, and
  lead to complex merge conflicts. Adopt a simpler branching strategy like trunk-based
  development or GitHub flow, which emphasizes shorter-lived branches and more frequent
  merges to the main branch.
