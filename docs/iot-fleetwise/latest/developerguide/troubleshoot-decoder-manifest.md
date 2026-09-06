

AWS IoT FleetWise is no longer open to new customers. Existing AWS IoT FleetWise customers can continue using the service. The [Guidance for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/) provides guidance on how to develop and deploy modular services for connected mobility solutions that can be used to achieve equivalent capabilities as AWS IoT FleetWise.

# AWS IoT FleetWise decoder manifest issues
<a name="troubleshoot-decoder-manifest"></a>

Troubleshoot decoder manifest issues.


**Diagnosing decoder manifest API calls**  

| Error | Troubleshooting guidelines | 
| --- | --- | 
| UpdateOperationFailure.ConflictingDecoderUpdate | The same decoder manifest has multiple update requests. Wait and try again. | 
| UpdateOperationFailure.InternalFailure | InternalFailure is launched as an encapsulated exception. The problem itself depends on the exception encapsulated. | 
| UpdateOperationFailure.ActiveDecoderUpdate | The decoder manifest is in an Active state and can't be updated. Change the decoder manifest state to DRAFT, and then try again. | 
| UpdateOperationFailure.ConflictingModelUpdate | AWS IoT FleetWise is trying to validate against a vehicle model (model manifest) that's being modified by someone else. Wait and try again. | 
| UpdateOperationFailure.ModelManifestValidationResponse : FailureReason.MODEL\_DATA\_ENTRIES\_NOT\_FOUND | The vehicle model doesn't have any signals associated with it. Add signals to the vehicle model and verify that the signals can be found in the associated signal catalog. | 
| UpdateOperationFailure.ModelManifestValidationResponse : FailureReason.MODEL\_NOT\_ACTIVE | Update the vehicle model so that it's in ACTIVE state, and then try again. | 
| UpdateOperationFailure.ModelManifestValidationResponse : FailureReason.MODEL\_NOT\_FOUND | AWS IoT FleetWise can't find the vehicle model associated with the decoder manifest. Verify the Amazon Resource Name (ARN) of the vehicle model and try again. | 
| UpdateOperationFailure.ModelManifestValidationResponse(FailureReason.MODEL\_DATA\_ENTRIES\_READ\_FAILURE | The validation of the vehicle model failed because signal names from the vehicle model weren't found in the signal catalog. Verify that the signals in the vehicle model are all included in the associated signal catalog. | 
| UpdateOperationFailure.ValidationFailure | Signals or network interfaces that aren't valid were found in the request to update the decoder manifest. Verify that all signals and network interfaces returned by the exception exist, that all signals used are associated with an available interface, and that you won't remove an interface that has signals associated with it. | 
| UpdateOperationFailure.KmsKeyAccessDenied | There's a permission issue on the AWS Key Management Service (AWS KMS) key used for the operation. Verify that you're using a role that has access to the key and try again. | 
|  UpdateOperationFailure.DecoderDoesNotExist | The decoder manifest doesn't exist. Verify the decoder manifest name and try again.  | 

Vision system data error messages with the `SIGNAL_DECODER_INCOMPATIBLE_WITH_SIGNAL_CATALOG` reason will include a hint in the response that provides information about why the request failed. You can use the hint to determine which troubleshooting guidelines to follow. 

**Note**  
Vision system data is in preview release and is subject to change.


**Diagnosing decoder manifest vision system data validation**  

| Error | Troubleshooting guidelines | 
| --- | --- | 
| InvalidSignalDecoder.withReason(SignalDecoderFailureReason.NO\_SIGNAL\_IN\_CATALOG\_FOR\_DECODER\_SIGNAL) | AWS IoT FleetWise didn't find the root signal structure used in the signal decoder using the signal catalog. Verify that the root signal of the structure is properly defined in the signal catalog. | 
| InvalidSignalDecoder.withReason(SignalDecoderFailureReason.SIGNAL\_DECODER\_TYPE\_INCOMPATIBLE\_WITH\_MESSAGE\_SIGNAL\_TYPE) | A primitive message in the signal catalog wasn't defined with the same data type in the decoder manifest update request. Verify that the primitive messages defined in the request match their corresponding signal catalog definition. | 
| InvalidSignalDecoder.withReason(SignalDecoderFailureReason.STRUCT\_SIZE\_MISMATCH) | The number of properties defined in a struct in the signal catalog don't match the number of properties you're trying to decode in the decoder manifest. Verify that you have the correct number of signals to decode by comparing it with the signals defined in the signal catalog. | 
| InvalidSignalDecoder.withReason(SignalDecoderFailureReason.SIGNAL\_DECODER\_INCOMPATIBLE\_WITH\_SIGNAL\_CATALOG) | AWS IoT FleetWise found a signal defined as a STRUCT in the signal catalog without a structuredMessageDefinition defined in the decoder manifest request. Make sure that each struct is defined as a structuredMessageDefinition in the decoder manifest update request. | 
| InvalidSignalDecoder.withReason(SignalDecoderFailureReason.SIGNAL\_DECODER\_INCOMPATIBLE\_WITH\_SIGNAL\_CATALOG) | The root signal of the structure used in the decoder manifest is not properly defined as a structure in the signal catalog. The root signal structure used in the decoder manifest must have its field structFullyQualifiedName defined. It also needs a STRUCT node with that fullyQualifiedName. | 
| InvalidSignalDecoder.withReason(SignalDecoderFailureReason.SIGNAL\_DECODER\_INCOMPATIBLE\_WITH\_SIGNAL\_CATALOG) | One of the leaf messages used in the decoder manifest request is not defined as a primitive message. Verify that all leaf objects in the request are defined as primitive messages.  | 
| InvalidSignalDecoder.withReason(SignalDecoderFailureReason.SIGNAL\_DECODER\_INCOMPATIBLE\_WITH\_SIGNAL\_CATALOG) | An array object in the signal catalog wasn't defined as a structuredMessageListDefinition in the decoder manifest update request. Verify that all array properties are defined as structuredMessageListDefinition in the decoder manifest update request. | 