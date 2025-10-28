AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see
[AWS Mainframe Modernization availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Understand Code conversion billing for Assembler conversion

You will refer this page to understand the Code conversion billing scope and process before doing the actual conversion.
The billing calculation section mentions the process though which conversion from Assembler to COBOL is charged per each line of code.

## Code conversion billing and scope

Assembler code conversion generates charges (billing reports) on your AWS account
only after completing the _conversion_ step. The charge
is based on the number of lines of code converted. If you perform multiple conversion
steps, for instance after adding new Assembler code, changing the conversion
configuration, or applying a new version of the container, only changed lines and/or
newly added lines are used to calculate the charge. We won't charge you twice for
conversion of the same line of code in the same program.

###### Note

The modules with changed lines of code and all lines of code in new or renamed
programs will be charged.

To avoid multiple charges, Code conversion stores an encoded binary file for each
Assembler or Macro module in the project bucket in `<Project_bucket>/`awsm2ccm-do-not-delete`/<AWS_account_number>/Hash`.
These encoded files do not contain any customer code.

###### Important

Don't manually edit or delete these files. Changes may result in multiple billings for converting the same components.

The AWS Mainframe Modernization Code conversion analysis report (“Analysis Report”) provides customers with
details about the anticipated conversion scope, outcome, and billing to ensure accurate
expectations of the actual conversion. Conversion may result in some lines of code not
getting converted, some lines of code partially getting converted, and some lines of
code converting completely. The Analysis Report shows the number of lines of code for
each category. **You must run and read the Analysis Report prior to
processing any conversion of programs, macros, and copybooks.** Once a
customer reviews the Analysis Report and agrees with the reported scope, expected
outcome, and expected billing, the customer can move forward with executing the
conversion.

###### Note

By executing the AWS Mainframe Modernization Code Conversion `**Convert**` command, you acknowledge that you have
run and read the Analysis Report, and agree with the expected outcome and the
billable number of lines of code.

### Scope of Conversion

AWS Mainframe Modernization Code conversion processes all lines of code of all assembler, macro and
copybook components available in the _scrlib_ and
_macrolib_ directories in the configured S3
source location. Assembler programs, and any macros, and copybooks referenced in an
assembler program are _in scope_. Macro and
copybook components that are not referenced by an assembler program are considered
as _out of scope_ and not converted. During
processing, the converter executes advanced algorithms that consider each in-scope
component holistically. All lines of code of these components participate in the
processing regardless of whether they are totally converted, partially converted, or
not converted. AWS Mainframe Modernization Code conversion ignores blank lines and doesn't count them
as lines of code. Comment lines and lines containing any other text (e.g., JCL
statements for assembler embedded in JCL) are counted as lines of code for
billing.

### Billing calculation

AWS Mainframe Modernization Code conversion charges for the in-scope components in their entirety.
This means that it charges for every line of code within each in-scope component,
including lines that could not be converted, were partially converted, and were
totally converted. AWS Mainframe Modernization Code conversion adds up all lines of code of components
supplied for processing (including assembler programs, referenced copybooks, and
referenced macros), and uses the total number of lines of code for billing.

###### Note

Copybooks and macros not referenced by an Assembler program are not considered
in-scope.

For example, assume a program has 1,000 lines of code:

- 700 lines are fully converted
- 200 lines are partially converted
- 100 lines are not converted

1,000 lines of code would be processed and will be billable.

### Improving the conversion

If you as a customer seek a higher conversion rate for the lines of code or have
other specific requirements, you can reach out to the AWS representatives for additional
engagement options such as a calibration effort, or professional services
assistance.
