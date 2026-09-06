

# Before you transform
<a name="dotnet-bp-before-transform"></a>

Review the following recommendations before you start a .NET transformation job.

## Use the .NET conversational AI assistant
<a name="dotnet-bp-use-assistant"></a>

Use the new .NET agent for best transformation results. The conversational AI assistant is available for Visual Studio through the [AWS Toolkit for Visual Studio](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.AWSToolkitforVisualStudio2022). It is also available for [Kiro](https://kiro.dev/) or other IDEs through the Kiro power for AWS Transform and AWS Transform MCP agents. The new .NET agent is not yet available in web console.

## Use other tools if the objective is not .NET to .NET transformation
<a name="dotnet-bp-use-other-tools"></a>

AWS Transform for .NET is appropriate for .NET Framework to .NET code modernization and .NET upgrades to later versions. It is not suitable for transformations that include non-.NET languages, such as Java, or non-.NET frameworks, such as React. It also does not provide application architectural refactoring. Use [AWS Transform custom](custom.md) or Kiro for those kinds of modernization.

## Use a stable edition of Visual Studio, preferably VS2026
<a name="dotnet-bp-stable-vs"></a>

Use a GA edition of Visual Studio rather than a preview or Insiders edition to avoid complications from preview software. The AWS Toolkit can be used with Visual Studio 2026 or 2022. VS2026 is recommended because it performs better with reduced memory consumption.

## Use the latest AWS Toolkit for Visual Studio
<a name="dotnet-bp-latest-toolkit"></a>

Stay on the latest version of AWS Toolkit for Visual Studio for bug fixes and feature updates. You can check your toolkit version and upgrade at **Extensions** > **Manage Extensions** > **Installed**.

## Work in Visual Studio IDE for medium or higher complexity projects
<a name="dotnet-bp-ide-complexity"></a>

The IDE experience gives you the deepest view of transformation, where you can work alongside the .NET agent as it transforms projects. For medium, high, or critical complexity projects, use the IDE rather than web console.

## Have a validation plan
<a name="dotnet-bp-validate-before"></a>

Decide how you will validate your application for correctness after it is transformed. Post-transformation, you'll need to confirm that it behaves and looks correctly when run, and that security controls, business logic, and data storage are intact. Will validation be conducted manually and/or using test automation? If your solution contains unit tests, AWS Transform will port them for you and execute them, and results will appear in the transformation report.

## Provide NuGet private package dependencies
<a name="dotnet-bp-nuget-deps"></a>

If your solution depends on private packages, ensure they are available on your local machine so the IDE and AWS Transform can find them.

## Specify package replacements or ask for agent recommendations
<a name="dotnet-bp-package-replacements"></a>

For packages that do not have modern .NET versions, you can either customize the transformation plan to specify your intended package substitutions, or ask the agent for recommendations.

## Do not end your job until you are sure you do not want any more changes
<a name="dotnet-bp-dont-end-job"></a>

After transformation completes, do not end your job right away in case you want additional changes. Transformation is not complete until you say it is. You can ask for changes up until you mark the job complete.

## After transforming, hand off to an AI code companion to finalize your app
<a name="dotnet-bp-handoff"></a>

Expect to combine AWS Transform with an AI code companion such as Kiro. A common pattern is to first transform with AWS Transform for .NET, then hand off to an AI code companion to finalize the application. That finalization work might include identifying and correcting runtime errors, behavioral issues, and UX styling.

In the modernization journey, think of AWS Transform as the express travel that takes you a long way towards your objective, and an AI code companion as the local travel that takes you to your final destination.

To aid hand-off from AWS Transform to AI code companions, AWS Transform provides an HTML transformation report and a Next Steps markdown document at the end of transformation.