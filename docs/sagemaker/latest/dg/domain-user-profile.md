# Domain user profiles

A user profile represents a single user within an Amazon SageMaker AI domain. The user profile is the
main way to reference a user for the purposes of sharing, reporting, and other user-oriented
features. This entity is created when a user onboards to the Amazon SageMaker AI domain. A user profile can
have (at most) a single JupyterServer application outside the context of a shared space. The user
profile's Studio Classic application is directly associated with the user profile and has an
isolated Amazon EFS directory, an execution role associated with the user profile, and Kernel Gateway
applications. A user profile can also create other applications from the console or from
Amazon SageMaker Studio.

###### Topics

- [Add user profiles](domain-user-profile-add.md "domain-user-profile-add.md")
- [Remove user profiles](domain-user-profile-remove.md "domain-user-profile-remove.md")
- [View user profiles in a domain](domain-user-profile-view.md "domain-user-profile-view.md")
- [View user profile details](domain-user-profile-describe.md "domain-user-profile-describe.md")
