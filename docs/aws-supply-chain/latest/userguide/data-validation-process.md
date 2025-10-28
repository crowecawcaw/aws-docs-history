# Data Validation Process

After the preprocessing process described above completes, the data validation process
begins. Data validation consists of three steps:

1.  Data Structure Validation[Demand Planning](required_entities.md "required_entities.md") - This step includes checks to ensure all required tables and
    columns exist and have data before any transformation begins. This stage confirms your
    data tables are properly set up.
2.  Data Quality Validation - This step ensures that data content is complete and error-free. It
    checks for:

        * Missing values in essential fields
        * Validation checks on data formats and validity of dates
        * Data completeness required for building forecast input

    This ensures all necessary data is present and valid before proceeding with transformations.

3.  Forecasting Eligibility Validation: This step ensures that sufficient data is provided to
    create a forecast, including:

        * Minimum historical data requirements
        * Time series length limitations
        * Other algorithm-specific constraints

    This stage ensures that your data is suitable for generating forecasts.
    Even a single validation failure will stop the forecast creation process. You must work
    with your data administrator to correct the underlying data issues, then choose
    **Retry** to try forecast creation again.
