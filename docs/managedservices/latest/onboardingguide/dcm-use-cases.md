# Direct Change Mode use cases

The following are uses cases for Direct Change Mode:

###### Resource provision and management through AWS CloudFormation

- Integrate existing CloudFormation-based tooling and processes.

###### Ongoing resource management and updates

- Small atomic changes with low risk.
- Changes that would otherwise run through a manual or automated RFC.
- Tooling that requires native AWS API access.
- The DCM role can be utilized if you're in the migration stage. Migration teams leverage the permissions on the DCM to create or modify stacks.
- DCM roles can be used in the CI/CD pipeline to build new AMIs, create Amazon ECS tasks, and so on.
