# Data Validation Report Access

When creating a forecast for the first time, navigate to the **Demand
Planning** module in AWS Supply Chain and choose **Create a
Plan**. The system guides you through three steps: Data Ingestion, Plan
Configuration, and finally, Forecast Generation. After completing data ingestion and plan
configuration, choose **Generate Forecast** to initiate data validation.
Each new forecast generation creates a fresh validation report based on the current state
of your data.

Data Structure validation failures (such as missing tables or columns) appear as
banner messages at the top of your screen. These fundamental issues must be resolved
before proceeding. After data structure validation passes, the system proceeds with Data
Quality and Forecasting Eligibility validations. Any failures in these stages are detailed
in the validation report, accessible by choosing **Data
Validations**.

## Subsequent Forecast Creation

For subsequent forecasts, choose **Generate Forecast**. You will
see a banner displaying three steps, with data validation as the first step. The same
validation behavior applies. Structural issues appear as banners, while other validation
failures are available in the detailed report.

## Report Content

The Data Validation Issues report provides a comprehensive view of Data Quality and
Forecasting Eligibility validation failures that need to be addressed. The report
displays the following:

- Dataset: Identifies the specific dataset where the issue occurs
- Rule: Describes the type of validation that failed
- Error Date/Time: Shows when the error was detected
- Status Message: Provides detailed information about the records affected and
  recommended actions

To help navigate and resolve these issues, you can do the following:

- Use the search box to find specific types of errors
- Filter by dataset using the drop-down menu
- Download a detailed report containing all validation failures
- View **Records affected** for each validation to understand the
  scope of the issue
