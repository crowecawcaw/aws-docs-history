

# Custom
<a name="custom"></a>

## What is AWS Transform custom?
<a name="custom-what-is"></a>

AWS Transform custom uses agentic AI to perform large-scale modernization of software, code, libraries, and frameworks to reduce technical debt. It handles diverse scenarios including language version upgrades, API and service migrations, framework upgrades and migrations, code refactoring, and organization-specific transformations.

Through continual learning, the agent improves from every execution and developer feedback, delivering high-quality, repeatable transformations without requiring specialized automation expertise.

### Key Capabilities
<a name="custom-key-capabilities"></a>

AWS Transform custom provides the following capabilities:
+ **Natural language-driven transformation definition** - Create custom transformations using natural language, documentation, and code samples
+ **Transformation execution** - Apply transformations consistently and reliably across multiple codebases
+ **Continual learning** - Automatically improve transformation quality from every execution
+ **AWS-managed transformations** - Use ready-to-use, AWS-vetted transformations for common scenarios

### Transformation Patterns
<a name="custom-transformation-patterns"></a>

AWS Transform custom supports diverse transformation patterns to address your modernization needs. Each pattern has different complexity characteristics based on the scope and nature of the changes required.


| Pattern | Description | Complexity | Examples | 
| --- | --- | --- | --- | 
| API and Service Migrations | Migrating between API versions or equivalent services while maintaining functionality | Medium | AWS SDK v1→v2 (Java, Python, JavaScript), Boto2→Boto3, JUnit 4→5, javax→jakarta | 
| Language Version Upgrades | Upgrading to newer versions of the same programming language, adopting new features and replacing deprecated functionality | Low-Medium | Java 8→17, Python 3.9→3.13, Node.js 12→22, TypeScript version upgrades | 
| Framework Upgrades | Upgrading to newer versions of the same framework, addressing breaking changes | Medium | Spring Boot 2.x→3.x, React 17→18, Angular upgrades, Django upgrades | 
| Framework Migrations | Migrating to entirely different frameworks that serve similar purposes | High | Angular→React, Redux→Zustand, Vue.js→React | 
| Library and Dependency Upgrades | Upgrading third-party libraries to newer versions while maintaining the same language and framework | Low-Medium | Pandas 1.x→2.x, NumPy upgrades, Hadoop/HBase/Hive library upgrades, Lodash upgrades | 
| Code Refactoring and Pattern Modernization | Modernizing code patterns and adopting best practices without changing external functionality | Low-Medium | Print→Logging frameworks, string concatenation→f-strings, type hints adoption, observability instrumentation | 
| Script and File-by-File Translations | Translating independent scripts or configuration files where files are mostly self-contained | Low-Medium | AWS CDK→Terraform, Terraform→CloudFormation, Excel→Python notebooks, Bash→PowerShell | 
| Architecture Migrations | Migrating between hardware architectures or runtime environments with minimal code changes | Medium-High | x86→AWS Graviton (ARM), on-premises→Lambda, traditional server→containers | 
| Language-to-Language Migrations | Translating codebases from one programming language to another | Very High | Java→Python, JavaScript→TypeScript, C→Rust, Python→Go | 
| Custom and Organization-Specific Transformations | Unique organizational requirements and specialized modernization needs | Varies | Custom internal library migrations, organization-specific coding standards, proprietary framework migrations | 

**Note**  
For COBOL/mainframe languages, use AWS Transform for Mainframe. For .NET Framework upgrades to .NET Core, consider AWS Transform for Windows. For VMware migrations to AWS, consider AWS Transform for VMware.

### How AWS Transform custom Works
<a name="custom-how-it-works"></a>

AWS Transform custom is usually used in large-scale projects where multiple codebases or modules are transformed. Teams typically follow a four-phase workflow:

**Define Transformation** - Provide natural language prompts, documentation, and code samples to the agent, which generates an initial transformation definition. This definition can be iteratively refined through chat or direct edits. This phase can be skipped when using AWS-managed transformations.

**Pilot or Proof-of-Concept** - Test the transformation on sample codebases and refine based on results. This validation phase helps estimate the cost and effort of the full transformation. Continual learning improves quality during this phase.

**Scaled Execution** - Set up automated bulk execution using the CLI, with developers reviewing and validating results. Monitor progress using the web application and track transformations across multiple repositories.

**Monitor and Review** - Continual learning automatically improves the transformation quality. Review the lessons that have been extracted from previous runs to ensure they meet quality standards, and archive any that are not useful.

## Understanding Key Concepts
<a name="custom-understanding-key-concepts"></a>

This section explains key concepts for working with AWS Transform custom.

### Transformation Definitions
<a name="custom-transformation-definitions"></a>

A **transformation definition** contains the instructions and knowledge needed to perform a specific code transformation. It is represented as a skill and consists of:
+ `SKILL.md` (required) - Instructions in Markdown with YAML frontmatter (`name` and `description` fields) that contains the core transformation logic and execution instructions
+ `references/` folder (optional) - Documentation loaded as needed during transformation execution
+ `scripts/` folder (optional) - Scripts that the transformation downloads and runs during execution

AWS Transform CLI automatically downloads transformation definitions to the current directory when needed for execution, inspection, or modification.

**Important**  
When publishing a transformation, the directory must contain only `SKILL.md` and optionally the `references/` folder, the `scripts/` folder, or both. No other files or subdirectories are allowed.

**Note**  
CLI version 2.0 and later uses the skills format. Existing transformation definitions are automatically handled by the CLI.

### Transformation Registry
<a name="custom-transformation-registry"></a>

The **transformation registry** is your AWS account's centralized repository for storing and managing transformation definitions. Transformations in the registry can be:
+ Listed using `atx custom def list`
+ Executed across multiple codebases
+ Shared with other users in your AWS account
+ Version-controlled

**Important**  
Transformation definitions are account-specific. If you want to use a transformation in a different AWS account, you must publish it separately in that account.

### Draft vs Published Transformations
<a name="custom-draft-vs-published"></a>

AWS Transform custom supports two states for transformations in the registry:

**Draft transformations** are in-progress or untested transformation definitions. They are saved as specific versions and can be retrieved, updated, and executed by users referring to that specific version. Drafts are useful for iterative development, testing, and refinement before the transformation is ready to be shared with your team. Drafts are also associated to specific conversation. If you restart the CLI, you can use `atx --conversation-id {id}` to restore a previous one.

**Published transformations** are available in your account's transformation registry for execution by other users with the required IAM permissions. Published transformations can be discovered using `atx custom def list`.

The typical workflow is:

1. Create transformation locally

1. Save as draft for testing (`atx custom def save-draft`)

1. Refine and validate

1. Publish to share with your team (`atx custom def publish`)

You can also publish a transformation directly without saving it as a draft.

### References vs. Lessons
<a name="custom-references-vs-knowledge-items"></a>

AWS Transform custom uses two types of knowledge to improve transformation quality:

**References** are user-provided documentation stored in the `references/` folder of a transformation definition. References support text files only (maximum 10MB total for all files) and usually contain documentation, API specifications, migration guides, and code samples. References are loaded as needed during transformation execution. You add references when creating or updating a transformation definition in interactive mode.

**Lessons** are automatically extracted from previous runs of a transformation. The continual learning system generates them from execution trajectories, developer feedback, and code fixes it encounters during transformations. It groups related lessons into categories so you can review them together. Unlike references, which you provide upfront, lessons accumulate over time as you run the transformation across different codebases, and the system applies them automatically to improve future runs. You review and manage lessons interactively with `atx custom def learnings`.

### Build and Validation Commands
<a name="custom-build-validation-commands-concept"></a>

The **build or validation command** is an optional parameter that specifies how to validate your code during the transformation process. This command is executed at various points during the transformation to ensure code integrity.

Providing a command that validates the results and returns issues if validation fails is very important to improve transformation quality through continual learning. If no build or validation is needed, omit from your input.

For examples and detailed guidance, see Build and Validation Commands in the Workflows section.

### Continual Learning
<a name="custom-continual-learning-concept"></a>

**Continual learning** is the system that automatically captures feedback from every transformation execution and improves transformation quality over time. The system gathers information through:
+ Explicit feedback - Comments and code fixes provided in interactive mode
+ Implicit observations - Issues the agent encounters while transforming and debugging code

The continual learning system processes this information to create **lessons** that it adds to the transformation definition to improve future transformations. The system runs the learning process automatically after transformations complete, requiring no additional input from you.

**Important**  
Lessons are transformation-specific and are not shared across different transformations or different customer accounts.

#### Managing Lessons
<a name="custom-managing-lessons-concept"></a>

The system generates lessons automatically, but you stay in control of which ones it applies to future runs. The `atx custom def learnings` command opens an interactive terminal session for reviewing and curating the lessons a transformation has accumulated.

In this session, you can:
+ Browse lessons grouped into categories, and see how many active lessons each category contains.
+ Open a lesson to read its full detail, including the lesson body, its impact, and how many previous runs consulted it.
+ Archive a lesson to prevent the system from applying it to future runs, and restore it later if needed.
+ Permanently delete an archived lesson that is no longer useful.

For step-by-step instructions, see [Continual Learning](custom-workflows.md#custom-continual-learning).

### Client-Side Skills
<a name="custom-client-side-skills-concept"></a>

**Client-side skills** are additional capabilities that extend the agent during transformation executions. Unlike transformation definitions which define what transformation to perform, client-side skills provide supplementary tools, scripts, and instructions that the agent can use alongside its built-in capabilities during any transformation.

Client-side skills are discovered from project-level and user-level directories. Place skills at the project level when they enforce standards specific to a repository, and at the user level when they apply across all your projects. Project-level skills are only available when a code repository path is provided. For detailed configuration and usage, see [Client-Side Skills](custom-workflows.md#custom-client-side-skills).

## Introduction to custom transformation commands
<a name="custom-cmd-intro"></a>

Here are a few of the commands you can use with custom transformations. The complete list of commands is in the [AWS Transform custom transformations command reference](https://docs.aws.amazon.com/transform/latest/userguide/custom-command-reference.html).
+ `atx custom`
  + **Executes custom transformation interactive experience, allowing creation, discovery, execution, and refinement of transformations.**
  + This is the default command for `atx`.
  + `--trust-all-tools` (`-t`) is optional and implicitly allows all requested tool requests by the agent. Use with caution especially in production environments. You can configure tool trust for specific tools and commands using the [trust settings file](https://docs.aws.amazon.com/transform/latest/userguide/custom-workflows.html#custom-advanced-configuration).
+ `atx custom --help` \| `atx custom -h`
  + **Shows help menu.**
  + Each command also includes a help menu, for example, `atx custom def exec --help`.
+ `atx --version` \| `atx -v`
  + **Shows version.**
  + The version number changes with each release.
+ `atx custom def list`
  + **Prints list of transformations available in the transformation registry.**
+ `atx custom def exec`
  + **Executes a transformation**
+ `atx custom def learnings`
  + **Opens an interactive session to view and manage the lessons a transformation has learned from previous runs**
+ `atx mcp`
  + **Used to manage MCP server configurations**