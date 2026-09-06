

# Lifecycle configurations within Amazon SageMaker Studio
<a name="studio-lifecycle-configurations"></a>

Lifecycle configurations (LCCs) are scripts that administrators and users can use to automate the customization of the following applications within your Amazon SageMaker Studio environment:
+ Amazon SageMaker AI JupyterLab
+ Code Editor, based on Code-OSS, Visual Studio Code - Open Source
+ Studio Classic
+ Notebook instance

Customizing your application includes:
+ Installing custom packages
+ Configuring extensions
+ Preloading datasets
+ Setting up source code repositories

Users create and attach built-in lifecycle configurations to their own user profiles. Administrators create and attach default or built-in lifecycle configurations at the domain, space, or user profile level.

## Understanding built-in and default lifecycle configurations
<a name="studio-lifecycle-configurations-builtin-vs-default"></a>

There are two types of lifecycle configurations in Studio:
+ **Built-in LCC:** Built-in LCC is controlled by the administrator, always runs when a space starts, and resolves dynamically from the domain settings at launch time. When an administrator updates the built-in LCC at the domain level, all spaces automatically pick up the new LCC on their next launch without requiring any user action.
+ **Default LCC:** The default LCC is pre-selected for the user at the space level and persists until the user explicitly changes it. Updating the domain-level default LCC does not affect running spaces until they are restarted.

**Important**  
Amazon SageMaker Studio first runs the built-in lifecycle configuration and then runs the default LCC. Amazon SageMaker AI won't resolve package conflicts between the user and administrator LCCs. For example, if the built-in LCC installs `python3.11` and the default LCC installs `python3.12`, Studio installs `python3.12`. 