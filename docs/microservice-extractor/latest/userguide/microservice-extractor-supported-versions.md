AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Supported use cases

AWS Microservice Extractor for .NET supports the following use cases.

###### .NET Versions

AWS Microservice Extractor for .NET supports .NET Framework and .NET Core ASP.NET web service applications.
Specifically, Microservice Extractor supports the following versions:

- **Application visualization**:
  - .NET Framework version 4.0 and later
  - .NET Core version 3.1
  - .NET version 5.0
  - .NET version 6.0
  - .NET version 7.0

- **Application extraction**:

      + .NET Framework version 4.5 and later
      + .NET Core version 3.1
      + .NET version 5.0
      + .NET version 6.0
      + .NET version 7.0

  Microservice Extractor supports analysis of `C#` source code. Extraction is supported for
  only ASP.NET MVC applications.

###### Extraction

Microservice Extractor supports extraction for the following use cases:

- Classes are extracted in their entirety. Partial class extraction is not supported.
- Classes do not change during compilation. Classes that change class structure during
  compilation are not supported.

###### Controllers

Microservice Extractor supports the following actions in relation to controllers:

- For applications with controllers, Microservice Extractor converts local method calls at the controller
  level to network calls to the extracted service.
- For other applications, Microservice Extractor adds code comments by default. If you choose the advanced
  option for **Method invocations from the application to the extracted
  service** during extraction, Microservice Extractor replaces local method calls with network calls,
  where possible.
- For MVC applications, Microservice Extractor copies the views (.cshtml file) to the extracted service to
  be able to render the relevant HTML when returning the response.
