

# Unit tests
<a name="dotnet-unit-tests"></a>

AWS Transform can port and run existing unit tests, and can generate missing unit tests after transformation.

## Port and run existing unit tests
<a name="dotnet-unit-tests-port"></a>

If your original solution contains unit test projects (MSTest, NUnit, xUnit), AWS Transform ports them to the target .NET version. The agent then executes the ported unit tests and summarizes the results in the transformation report. You can also run the ported tests yourself using Visual Studio Test Explorer or the `dotnet test` command.

Unit test porting and execution are automatic.

## Generate unit tests for transformed code
<a name="dotnet-unit-tests-generate"></a>

AWS Transform can optionally generate unit tests for your transformed code. The agent assesses existing unit test coverage (MSTest, NUnit, xUnit) and automatically generates missing unit tests. The generated unit tests target the testable classes in your transformed .NET application, such as business logic and controllers.

**Note**  
Unit tests are generated **after** modernization. They do not validate original code functionality in the modernized code.

This is an opt-in feature. You can enable unit test generation either at the start of a job or after transformation:
+ **To generate unit tests during transformation:** Start a job. In the **Port solution with AWS Transform** dialog box, choose the **Generate unit tests** option. The generated unit tests are included in the local build verification step.
+ **To generate unit tests after transformation:** Use interactive mode. After transformation, the agent prompts you whether to generate unit tests. These unit tests are not included in the local build verification step, which has already completed. Generating unit tests at this point allows you to make post-transformation code changes prior to generating unit tests.

The transformation report describes the resulting unit test coverage.