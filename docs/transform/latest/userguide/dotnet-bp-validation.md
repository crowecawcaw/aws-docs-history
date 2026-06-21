# Validation and finalization

After transformation completes, validate your transformed application and finalize it for production use.

## Review the transformation report and Next Steps to understand what is done and what remains

Review the HTML transformation report to understand what has been done. Review the Next Steps markdown file to understand what tasks still remain. Ask the agent to clarify anything that is not clear.

## Use an AI code companion to validate, debug, and finalize your application

Review your transformed application for correctness. Use an AI code companion such as [Kiro](https://kiro.dev/ "https://kiro.dev/") to resolve issues.

## Validate unit tests

If your solution contains unit test projects (NUnit, xUnit, or MSTest), AWS Transform will port them to modern .NET and run the tests for you. Check the HTML transformation report for unit test results. Correct failing tests with an AI code companion.

## Validate application functionality

Run your application and confirm its functionality matches the original. Note functional issues and runtime errors. Correct with an AI code companion.

## Validate application UI

Run your application and confirm it looks and behaves like the original including navigation and routing. If your application has no styling, it might be that .css files are not in the correct location. Correct with an AI code companion.
