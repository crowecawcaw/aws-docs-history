AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Extract parts of

an application as independent services

Review the arrangement of the group or groups you selected and their individual
nodes and dependencies on the main view of the **Visualization (nodes and
dependencies)** page. When you are satisfied with your groups, choose
**Extract group** and perform the following steps:

1. On the **Review details and initiate extraction** page,
   review and verify the **Service details** and the
   **Extraction details**. Address all of the issues
   listed for the **Nodes** and
   **Dependencies**. To view the description of an issue,
   select the **Shared state access detected** or
   **Requires attention** alert under
   **Comments**. Select the corresponding **Class
   ID** to view and address the issue in the source code.

If a class accesses a state that is shared by classes that belong to
multiple groups in the application, modification of the shared state may
result in errors when you extract the nodes as a smaller service. If the
**Shared state access detected** message appears next
to a class, check whether the class accesses a state that is shared by
classes that belong to other groups. If so, update your application source
code to remove access to the shared state. Analyze the application again
before proceeding with the extraction.

The following shared state accesses are detected:

    * `TempData` property in [`ControllerBase`](https://docs.microsoft.com/en-us/dotnet/api/system.web.mvc.controllerbase.tempdata?view=aspnet-mvc-5.2#System_Web_Mvc_ControllerBase_TempData "https://docs.microsoft.com/en-us/dotnet/api/system.web.mvc.controllerbase.tempdata?view=aspnet-mvc-5.2#System_Web_Mvc_ControllerBase_TempData") class.
    * `Session` property in [`Controller`](https://docs.microsoft.com/en-us/dotnet/api/system.web.mvc.controller "https://docs.microsoft.com/en-us/dotnet/api/system.web.mvc.controller") class.
    * `Session` property in ASP.NET Core [`HttpContext`](https://docs.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.httpcontext.session "https://docs.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.httpcontext.session") class.
    * `Items` property in ASP.NET Core [`HttpContext`](https://docs.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.httpcontext.items "https://docs.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.httpcontext.items") class.
    * `TempData` property in ASP.NET Core [`Controller`](https://docs.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.controller.tempdata "https://docs.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.controller.tempdata") class.
    * `TempData` property in ASP.NET Core `WebApi`
     controller.

2. Select the options under **Method invocations from the original
   application to the extracted service**. Consider the following
   limitations for each method.

###### How Microservice Extractor extracts the service code repository:

    * **Extract as a microservice with remote
     endpoints** — network calls can add additional
     overhead to user requests. Manual verification and refactoring may
     be required to ensure accuracy.
    * **Extract as a library** —
     code duplication from manual refactoring may introduce conflicting
     states in the application.

###### How Microservice Extractor processes the original monolithic application repository:

    * **Refactor the methods in the original
     monolithic application repository to the methods that call the
     extracted microservice** — this option is not
     supported for WCF applications.
    * **Do not refactor the methods**
     — code duplication from manual refactoring may introduce
     conflicting states in the application.

3. When you are satisfied with the extraction details, choose
   **Extract**. The progress of the extraction is
   displayed at the top of the page . To cancel the extraction, in the
   extraction progress banner, select **Cancel extraction**.
   If you cancel the extraction, the extraction configuration is deleted, and
   you must restart the extraction.

A successful extraction will display the output location of the extraction
in the green status banner. To view the extraction details, choose
**View details** on the status banner.

If the extraction fails, the red status banner displays an error message.
Navigate to the **Visualization** page to verify and
address issues with the unsupported classes and try again.

###### View and edit extraction details

You can view the details of the extraction from the **Application
details** page by selecting the radio button next to the
**Service name** under **Extractions**,
and choosing **View details** from the
**Actions** dropdown. On the service details page, you can
view the **Extraction details** and **Nodes and
dependencies**. To edit the extraction details, choose
**Re-extract service** from the
**Actions** dropdown. You must re-extract a service in
order to edit its configuration.
