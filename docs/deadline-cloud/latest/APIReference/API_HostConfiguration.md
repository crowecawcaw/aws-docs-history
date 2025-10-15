# HostConfiguration

Provides a script that runs as a worker is starting up that you can use to provide
 additional configuration for workers in your fleet. 

To remove a script from a fleet, use the [UpdateFleet](API_UpdateFleet.md "API_UpdateFleet.md")
 operation with the `hostConfiguration`
`scriptBody` parameter set to an empty string ("").


## Contents





**scriptBody** 


The text of the script that runs as a worker is starting up that you can use to provide
 additional configuration for workers in your fleet. The script runs after a worker enters
 the `STARTING` state and before the worker processes tasks.


For more information about using the script, see [Run scripts as an
 administrator to configure workers](../developerguide/smf-admin.md "../developerguide/smf-admin.md") in the *Deadline Cloud Developer
 Guide*. 


###### Important

The script runs as an administrative user (`sudo root` on Linux, as an
 Administrator on Windows). 


Type: String


Length Constraints: Minimum length of 0. Maximum length of 15000.


Required: Yes




**scriptTimeoutSeconds** 


The maximum time that the host configuration can run. If the timeout expires, the worker
 enters the `NOT RESPONDING` state and shuts down. You are charged for the time
 that the worker is running the host configuration script.


###### Note

You should configure your fleet for a maximum of one worker while testing your host
 configuration script to avoid starting additional workers.


The default is 300 seconds (5 minutes).


Type: Integer


Valid Range: Minimum value of 300. Maximum value of 3600.


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/HostConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/HostConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/HostConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/HostConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/HostConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/HostConfiguration")
