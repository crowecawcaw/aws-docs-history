

# Exception handling
<a name="actions-exception-handling"></a>

Exception handling allows you to manage errors and unexpected conditions in your automations. Amazon Quick Automate provides capabilities for creating, raising, and handling exceptions appropriately to ensure robust error management and process continuity.

## Types of exceptions
<a name="types-of-exceptions"></a>

Amazon Quick Automate supports two types of exceptions:
+ Business exceptions - Used for expected errors from business rule violations such as:
  + Missing required data
  + Invalid input values
  + Policy violations
+ System exceptions - Used for technical or infrastructure errors such as:
  + Connection failures
  + Service timeouts
  + Authentication errors

## Actions
<a name="exception-actions"></a>

Raise exception  
Interrupts the process flow with an exception. Used to trigger or throw an exception to either end the process or to take specific actions to handle the exception scenario. If you do not want to end the process immediately, add an Exception flow to your Process step to handle the exception. Properties:  
+ **Title** (optional) - Action name shown in the process visualization (e.g., "Raise validation error")
+ **Create custom exception** (required) - When selected on, create a new exception with custom details. When off, raise or re-raise an existing exception stored in a variable
+ **Exception type** (required) - Category of the exception (e.g., "Business exception", "System exception")
+ **Exception reason** (required) - Short identifier used to categorize similar exceptions for reporting (e.g., "REQUIRED\_FIELD\_MISSING", "INVALID\_FORMAT")
+ **Exception message** (required) - Detailed description that will help with troubleshooting (e.g., "Customer email is required but not provided")
+ **Exception to raise** (required when Create custom exception is off) - The exception you want to raise or re-raise, typically stored as a variable (e.g., new\_exception)

Create custom exception  
Creates an exception without raising it. Used to prepare an exception variable that can be raised later in subsequent steps. Properties:  
+ **Title** (optional) - Action name shown in the process visualization (e.g., "Create validation exception")
+ **Exception type** (required) - Category of the exception (e.g., "Business exception", "System exception")
+ **Exception reason** (required) - Short identifier used to categorize similar exceptions for reporting (e.g., "REQUIRED\_FIELD\_MISSING")
+ **Exception message** (required) - Detailed description that will help with troubleshooting (e.g., "Customer email is required but not provided")
+ **Error code** (optional) - Numerical code used to distinguish different types of errors (e.g., 404 for not found, 503 for service unavailable)
+ **Caused by** (optional) - Reference to another exception that triggered this one, typically stored as a variable (e.g., original\_exception)
+ **New exception** (output) - Variable that will store the newly created exception (e.g., new\_exception)

Exception flow  
Defines how to handle exceptions that occur within a Process step. Used to create an alternative path to follow when exceptions occur in your process. After an exception is handled, the process continues with the next Step. Raise the exception again if you want to end the process. Add an Exception flow by clicking the **Exception flow** plus button found in the Process step. Properties:  
+ **Title** (optional) - Action name shown in the process visualization (e.g., "Handle validation errors")
+ **Exception reference** (required) - Variable name to refer to the exception within the Exception flow. Access exception details using variable["property"] where property can be: type, reason, message, code, or caused\_by (e.g., error)
Exception flows can only be added to Process steps. They are not found otherwise in the Actions panel.

## Working with exceptions
<a name="working-with-exceptions"></a>

**Exception properties**

When handling exceptions, you can access these properties:
+ type - Category of the exception ("Business exception" or "System exception")
+ reason - Short identifier for the exception
+ message - Detailed description of the error
+ code - Numerical error code if provided
+ caused\_by - Original exception that triggered this one if applicable

**Best practices**
+ Use descriptive exception reasons for easy categorization and reporting
+ Include detailed messages for troubleshooting
+ Implement retry logic for temporary system exceptions
+ Consider human intervention for business exceptions
+ Consider the impact on case status when handling exceptions
+ Ensure critical cleanup operations occur even after exceptions such as restarting a browser
+ Monitor exception frequencies and patterns
+ Review exception logs regularly
+ Re-raise exceptions once handled if you do not want to proceed with the remaining steps