# Review and customize transformation plan

In the _Prepare for transformation_ phase, after selecting repositories and resolving missing dependencies, AWS Transform will generate a modernization plan for review.

The web application uses a single global plan to modernize your selected repositories, which you can customize. The modernization plan provides details about the transformation. It includes these sections:

1. **Repository topology:** waves of repos in dependency order with project and dependency information.
2. **Feature & Package Migration Map:** package actions with before and after package names and versions.
3. **Transformation Strategy:** project type strategies, transformation execution order, risks and mitigations.
   Discuss the plan with the agent for clarifications or to explore options.

## Customize the plan

There are several ways to customize the transformation plan:

- **Chat**: Discuss the plan with the agent in chat and give it revised instructions (_Prepare for transformation_ phase).
- **Edit plan**: Edit the transformation plan markdown in the web application (_Prepare for transformation_ phase).
- **Upload customized plan**: Download the transformation plan markdown, review it, and upload a revised plan (_Prepare for transformation_ phase).
- **Steering document**: Upload one or more [steering documents](#steering-documents "#steering-documents") to tell the agent about your organization's requirements and preferences (_Assessment_ or _Prepare for transformation_ phase).

After you are satisfied with the modernization plan and have resolved any missing dependencies, confirm the repositories to transform and transformation will begin.

## Steering Documents

You can give the agent one or more steering documents to tailor the transformation plan. Steering documents can describe your organization's requirements and preferences such as those listed below. You can also upload application information such as a README file or specification to tell the agent more about the solution. To upload a steering document, drag and drop a file into the chat area and explain the document to give the agent context.

- Technology stack decisions
- Preferred .NET version(s)
- Preferred packages
- Front-end UI framework
- Back-end web service framework
- Organization conventions
- Examples of preferred coding patterns

A sample steering document follows.

```
# Organizational preferences

## Tech Stack for modernized .NET applications

We target the latest LTS .NET release (currently .NET 10)

For class libraries, we target .NET Standard 2.0 so they can be used by both .NET Framework and .NET applications.

We use the C# programming language. We convert legacy VB.NET code to C#.

We run our front-end web UIs on ASP.NET Core MVC projects with Razor Views.

We run our back-end web services on ASP.NET Web API projects.

## Package preferences

We use System.Text.Json for serialization.

We use the log4net .NET logger.
```
