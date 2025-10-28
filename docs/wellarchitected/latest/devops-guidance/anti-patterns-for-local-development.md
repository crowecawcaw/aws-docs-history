# Anti-patterns for local development

- **Irregular commits:** Sporadic or large commits can lead
  to lost progress, complicates the tracking of changes, and reduces the ability to roll
  back to a specific state. Frequently committing locally enables you to experiment
  fearlessly, knowing that there is a secure point to return to. Bundling large changes,
  or combining multiple changes, into a single, large batched commit should be avoided.
  This practice also usually leads to having larger commits to the main releasable branch
  of the repository, making it difficult to integrate with other changes, perform code
  reviews, and deploy with confidence. It is best practice to commit small, logical
  changes more frequently.
- **Avoiding local development environments:** Avoiding the
  use of local environments can result in teams making changes directly in production or
  having multiple developers share a single development account. This restricts developers
  from safely experimenting and testing their code changes and can result in increased
  risk of errors, service disruption, and integration issues that make troubleshooting
  complex. Set up individual local development environments for each developer.
- **Inconsistent local environment setup:** Allowing each
  developer to set up their local environment without following a standardized process can
  lead to variations across developer setups. Divergent environments can introduce
  hard-to-diagnose bugs and the notorious _it works on my machine_
  scenarios, which can impact overall team productivity. Use automated tools, scripts, and
  playbooks to help ensure that the team has consistent local development environment
  setups.
- **Long-lived development branches:** Maintaining long-lived
  development branches for the purpose of continuously deploying to local environments can
  lead to merge conflicts, increased technical debt, and divergence from the main code
  base. To keep the development environment as close to the production setup as possible,
  deployments to the environment should always be sourced from the main releasable branch
  which reflects the integrated code base used for production deployments.
- **Over-reliance on basic text editors:** Relying solely on
  traditional text editors such as VI or Emacs for development activities. While these
  editors have their merits and uses, they fall short of the capabilities provided by
  modern IDEs and text editors that are capable of improving developer experience. Use
  IDEs and text editors that provide a vast plugin ecosystem and can be tailored to
  specific development tasks and integrate with automated tools.
