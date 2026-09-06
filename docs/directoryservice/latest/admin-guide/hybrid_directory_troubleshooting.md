

# Troubleshooting hybrid directory and directory assessment
<a name="hybrid_directory_troubleshooting"></a>

A directory assessment is required to create a hybrid directory. Assessment tests run on each domain controller. The assessment tests examines different areas and result in a Passed or Failed status. If your directory assessment fails, you can view the assessment tests of your domain controllers to identify what issues caused the failure.

**Important**  
A hybrid directory can be created when the directory assessment's status is Passed with warning. We recommend you address the issue causing the warning prior to creating a hybrid directory

**Topics**
+ [Troubleshooting failed hybrid directory assessment](#hybrid_directory_troubleshooting_steps)
+ [Directory Status Errors](hybrid_directory_status_errors.md)
+ [Directory Assessment Error Messages](da-error-msgs.md)
+ [Assessment Test error messages](assessment_test_error-msgs.md)
+ [Assessment Test warning messages](assessment_test_warning-msgs.md)

## Troubleshooting failed hybrid directory assessment
<a name="hybrid_directory_troubleshooting_steps"></a>

You can troubleshoot a failed directory assessment from the **Directories** page in the AWS Management Console.

1. Sign in to the AWS Management Console and open the Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/).

1. Under the **Directory assessments** section, select the failed hybrid directory assessment.

1. On the **Assessment Details** page, review the directory assessment and identify what test(s) failed.

   1. The domain controller's assessment tests will have more information on what tests were successful or failed. The **Status** column provides more details on what caused the failed test. To view your domain controller's assessment tests, see [Viewing directory assessments](viewing_hybrid_dir_assessment.md).

1. Resolve the issues causing the failures on your self-managed Active Directory or AWS Managed Microsoft AD. See [Directory Assessment Error Messages](da-error-msgs.md) and [Assessment Test error messages](assessment_test_error-msgs.md) for more information.

1. Return to the failed assessment in the Directory Service console. Choose **Create assessment** in the red warning message. See [Creating a hybrid directory with your self-managed AD](hybrid_directory_create.md#creating_hybrid_directory) for more information on creating a directory assessment.