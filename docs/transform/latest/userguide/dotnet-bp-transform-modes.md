

# Transform interactively or autonomously
<a name="dotnet-bp-transform-modes"></a>

The Visual Studio IDE experience offers autonomous and interactive modes to control the degree of interactivity during transformation.

## Use interactive and autonomous modes to control the degree of interactivity
<a name="dotnet-bp-modes"></a>

You select the mode when starting a transformation, and you can change it anytime through a dropdown at the top of the chat window.
+ Use **autonomous mode** for unattended transformation, suitable for overnight or long-running jobs. You still have the opportunity to review results and ask for changes at the end of the job.
+ Use **interactive mode** to work alongside the agent in chat throughout the transformation process with a customizable transformation plan, high visibility into transformation details, and step-by-step review of each project. You can iterate to refine results or change direction until satisfied.

You can combine modes. For example, start in interactive mode to review and adjust the transformation plan, then switch to autonomous mode to transform the projects automatically.

## Ask the agent to explain code changes
<a name="dotnet-bp-explain-changes"></a>

If you see code changes you do not understand, ask the agent to explain them.

## Use checkpoints to stop at projects for review or changes
<a name="dotnet-bp-checkpoints"></a>

In interactive mode, after approving your plan, you can set or clear checkpoints for every project. When a project with a checkpoint has been transformed, the transformed code is applied to the project in IDE and the agent pauses for your review. You can review the results, and if you do not like them you can ask for more changes.

While stopped at a checkpoint, you can:
+ Review results as presented in chat and ask questions in chat. For example: "Why did you change the cryptography API in file X?"
+ View code changes, by choosing the **View Results** button for the project in the AWS Transform Job Plan window.
+ Refine the transformation, by asking for additional changes. For example: "Change this to use logger X" or "Change this to use package X instead of package Y".
+ Retry the transformation, doing it over with different instructions. For example: "Change this class library to target .NET Standard instead of .NET 10" or "Retry this transformation and change the target from Blazor to MVC Razor Pages".
+ Make your own code changes in the IDE.
+ Tell the agent to continue on to the next project checkpoint.

## Iterate until satisfied
<a name="dotnet-bp-iterate"></a>

Modernization is inherently iterative, and you can expect to iterate with the agent. You can make changes at project checkpoints, and also at end of transformation. Iterate as needed until you are satisfied. Transformation is not complete until you say it is.

## Code alongside the agent when stopped at a checkpoint
<a name="dotnet-bp-code-alongside"></a>

You can make your own code changes as you work with the agent. When stopped at a checkpoint, you can edit code files in Visual Studio. Your changes will be synced when you direct the agent to continue on.