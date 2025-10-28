# How Amazon Q Developer transforms code for Java language upgrades

To transform your code, Amazon Q Developer generates a transformation plan that it uses to upgrade
the code language version of your project. After transforming your code, it provides a
transformation summary and a file diff for you to review changes before accepting them. Since
Amazon Q Developer makes the minimal changes necessary to make your upgraded code compatible with the
target JDK, an additional transformation is required to upgrade your project's libraries and dependencies.
The following sections provide more details on how Amazon Q performs the transformation.

## Building your code and creating a transformation plan

To begin transforming your code, Amazon Q builds your project locally and generates a
build artifact that contains your source code, project dependencies, and build logs.

After generating the build artifact, Amazon Q builds your code in a secure build
environment and creates a transformation plan, which is customized to the project or module
you’re upgrading. The transformation plan outlines the specific changes Amazon Q will
attempt to make, including new dependency versions, major code changes, and
suggested replacements for deprecated code. These changes are based on the preliminary
build of your code, and might change during the transformation.

## Transforming your code

To transform your code, Amazon Q attempts to upgrade your code to the target Java version based on the proposed
changes in the transformation plan. As it makes changes, it re-builds and runs existing
unit tests in your source code to iteratively fix any encountered errors. The JDK upgrade
can be made from the following source code version to the target version:

- Java 8 to 17
- Java 8 to 21
- Java 11 to 17
- Java 11 to 21
- Java 17 to 21

Amazon Q makes the minimal changes necessary to make your code compatible with the
target Java version. Once Amazon Q performs
a minimum JDK upgrade, you can initiate a separate transformation to upgrade all third
party dependencies. Alternatively, you can specify third party dependencies and their
versions in a YAML file to only upgrade those dependencies during the library upgrade
transformation.

Amazon Q attempts to make the following changes when upgrading your code:

- Update deprecated code components according to the target Java version recommendations
- Upgrade popular libraries and frameworks to a version compatible with the target Java version.
  This includes updating the following libraries and frameworks to their latest
  available major versions:
  - Apache Commons IO
  - Apache HttpClient
  - bc-fips
  - Cucumber-JVM
  - Hibernate
  - jackson-annotations
  - JakartaEE
  - Javax
  - javax.servlet
  - jaxb-api
  - jaxb-impl
  - jaxen
  - jcl-over-slf4j
  - json-simple
  - jsr305
  - junit
  - junit-jupiter-api
  - Log4j
  - Micronaut
  - Mockito
  - mockito-core
  - Okio
  - PowerMockito
  - Quarkus
  - slf4j
  - slf4j-api
  - Spring Boot
  - Spring Framework
  - Spring Security
  - Swagger
  - testng

[Show moreShow less](# "#")

###### Note

Do not turn off or close your local machine during the code transformation because
client-side build requires a stable network connection.

## Building code in your local environment

During a transformation, Amazon Q performs verification builds in your local
environment. Amazon Q transforms your code on the server side in multiple steps. After
each step, Amazon Q sends the code to your local environment to build and test the
changes it made. The code is then sent back to the server side to continue the
transformation.

The build in your local environment helps verify the transformed code by allowing
Amazon Q to run tests that require access to private resources. To minimize security
risks associated with building AI-generated code in your local environment, Amazon Q
reviews and updates the code it generates to address security concerns.

## Reviewing the transformation summary and accepting changes

After the transformation is complete, Amazon Q provides a transformation summary with
details about the changes it made, including the status of the final build which indicates
whether your entire project was upgraded. You can also view a build log summary to
understand any issues that prevented Amazon Q from building your code in the upgraded
version.

The transformation summary additionally includes the differences between the changes
proposed in the transformation plan and the changes Amazon Q ultimately made to upgrade
your code, and any additional changes that weren’t in the original plan.

After you review the transformation summary, you can view the changes Amazon Q is
proposing in a file diff view. Any code changes Amazon Q suggests will not affect your
current project files until you accept the changes. The transformed code is available up to
30 days after the transformation completes.

## Completing partially successful transformations

Depending on the complexity and specifics of your codebase, there might be instances
where the transformation is partially successful. This means that Amazon Q was able to
transform only certain files or areas of code in your project. In this case, you have to
manually update the remaining code for your project to be buildable in the updated language
version.

To help transform the rest of your code, you can use Amazon Q chat in the IDE. You can
ask Amazon Q to review the partially updated files and provide new code to address issues,
such as compilation errors. You can also use features like [Feature development](q-in-IDE-chat.md#develop-code "q-in-IDE-chat.md#develop-code") and
[Workspace context](workspace-context.md "workspace-context.md") to include
more of your project as context and get suggestions for multiple files at a time.
