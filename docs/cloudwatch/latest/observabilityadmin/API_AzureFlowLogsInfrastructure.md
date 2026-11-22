

# AzureFlowLogsInfrastructure

The location of your Flow Logs: your existing Storage Accounts, or Storage Accounts that the setup creates. Specify one.

## Contents
<a name="API_AzureFlowLogsInfrastructure_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** AwsManaged **   <a name="cwoa-Type-AzureFlowLogsInfrastructure-AwsManaged"></a>
Create one Storage Account in each Azure Region that ingests Flow Logs, in the subscription specified by `SubscriptionId`.  
Type: [AzureAwsManagedFlowLogs](API_AzureAwsManagedFlowLogs.md) object  
Required: No

 ** CustomerManaged **   <a name="cwoa-Type-AzureFlowLogsInfrastructure-CustomerManaged"></a>
Use your existing Storage Accounts that already store Flow Logs.  
Type: [AzureCustomerManagedFlowLogs](API_AzureCustomerManagedFlowLogs.md) object  
Required: No

## See Also
<a name="API_AzureFlowLogsInfrastructure_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/AzureFlowLogsInfrastructure) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/AzureFlowLogsInfrastructure) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/AzureFlowLogsInfrastructure) 