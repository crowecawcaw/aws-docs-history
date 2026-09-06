

# Action
<a name="API_UBS_Action"></a>

Represents action metadata added to an Action dataset using the `PutActions` API. For more information see [Importing actions individually](https://docs.aws.amazon.com/personalize/latest/dg/importing-actions.html). 

## Contents
<a name="API_UBS_Action_Contents"></a>

 ** actionId **   <a name="personalize-Type-UBS_Action-actionId"></a>
The ID associated with the action.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: Yes

 ** properties **   <a name="personalize-Type-UBS_Action-properties"></a>
A string map of action-specific metadata. Each element in the map consists of a key-value pair. For example, `{"value": "100"}`.  
The keys use camel case names that match the fields in the schema for the Actions dataset. In the previous example, the `value` matches the 'VALUE' field defined in the Actions schema. For categorical string data, to include multiple categories for a single action, separate each category with a pipe separator (`|`). For example, `\"Deluxe|Premium\"`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 32000.  
Required: No

## See Also
<a name="API_UBS_Action_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/personalize-events-2018-03-22/Action) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-events-2018-03-22/Action) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/personalize-events-2018-03-22/Action) 