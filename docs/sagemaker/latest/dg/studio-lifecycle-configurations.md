# Lifecycle configurations within

Amazon SageMaker Studio

Lifecycle configurations (LCCs) are scripts that administrators and users can use to
automate the customization of the following applications within your Amazon SageMaker Studio
environment:

- Amazon SageMaker AI JupyterLab
- Code Editor, based on Code-OSS, Visual Studio Code - Open Source
- Studio Classic
- Notebook instance
  Customizing your application includes:

- Installing custom packages
- Configuring extensions
- Preloading datasets
- Setting up source code repositories
  Users create and attach built-in lifecycle configurations to their own user profiles.
  Administrators create and attach default or built-in lifecycle configurations at the domain,
  space, or user profile level.

###### Important

Amazon SageMaker Studio first runs the built-in lifecycle configuration and then runs the
default LCC. Amazon SageMaker AI won't resolve package conflicts between the user and administrator
LCCs. For example, if the built-in LCC installs `python3.11` and the default
LCC installs `python3.12`, Studio installs `python3.12`.
