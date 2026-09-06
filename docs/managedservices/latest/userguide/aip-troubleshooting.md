

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Troubleshooting AMS Automated IAM Provisioning fndings and errors
<a name="aip-troubleshooting"></a>

There are three ways you might run into problems when using AMS Automated IAM Provisioning:
+ RFC errors: These can happen for a variety of reasons; for example, incorrect input. For more information, see [Troubleshooting RFC errors in AMS](rfc-troubleshoot.md).
+ SSM errors: These can happen for a variety of reasons; for example, poor formatting. For more information, see [Troubleshooting Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-troubleshooting.html).
+ Validation check findings: These occur when one of the many validation checks that Automated IAM Provisioning runs finds a problem. For a list of validation checks, and recommended actions to fix, see [Runtime checks for AMS Automated IAM Provisioning in AMS](aip-runtime-checks.md).