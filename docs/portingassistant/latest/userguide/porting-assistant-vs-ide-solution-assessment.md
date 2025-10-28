AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Assess and analyze

solution using Porting Assistant for .NET Visual Studio IDE extension

To assess your solution and analyze the results from the Porting Assistant for .NET Visual Studio IDE
extension, perform the following steps:

1. Open a solution file, then open a .cs file within the solution.
2. From the Porting Assistant for .NET Visual Studio IDE Extension, select the
   **Analyze** tab. In the drop-down menu, you can choose to
   **Enable Incremental Assessments** or **Run Full
   Assessment**.
   1. **Enable Incremental Assessments**. When you select
      this option, Porting Assistant for .NET automatically runs a continuous assessment as you make
      changes to the source code. Compatibility errors are displayed when
      encountered.
   2. **Run Full Assessment**. When you select this option,
      Porting Assistant for .NET runs a one-time, full assessment for the compatibility solution
      loaded in the IDE.

3. The **Error List** pane at the bottom of the screen displays
   all of the incompatibilities discovered in the source files associated with the
   solution. You can select each entry in the list of incompatibilities to view the
   incompatibility in the source code, which is highlighted.
