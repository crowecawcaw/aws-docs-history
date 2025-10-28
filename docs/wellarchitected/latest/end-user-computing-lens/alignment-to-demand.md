# Alignment to demand

| EUCSUS01: How do you select the type of fleet and running mode for your end users?
|
| --- |
| | With Amazon AppStream 2.0, you can select between Always-On or On-Demand fleet types. Similarly, Amazon WorkSpaces offers two running modes with AlwaysOn and AutoStop.
| EUCSUS02: How do you select the bundle or instance family for your end users? |
| --- |
| | Selecting an appropriate bundle or instance family involves evaluating your application's compute, memory, storage, and network requirements.
| EUCSUS03: How do you align session settings with efficient resource management? |
| --- |
| | Timeouts are crucial for an AWS EUC deployment, as timeouts enable efficient resource management by disconnecting idle sessions. For example, consider two scenarios where disconnect timeouts have been configured for an AppStream 2.0 fleet at six hours and 15 minutes respectively. In the case of the 15 minute timeout, a session will be timed out and the instance terminated within 15 minutes. In comparison, the six hour timeout will result in an instance running for six hours after the user disconnects before it is terminated, which incurs a larger carbon footprint. Timeouts optimize costs and the carbon footprint for AppStream 2.0and WorkSpaces instances by helping to prevent unnecessary resource consumption and associated charges.
| EUCSUS04: How do you align your scaling strategy with efficient use of resources? |
| --- |
| | Scaling in Amazon AppStream 2.0 helps create a seamless user experience by providing the necessary resources to handle fluctuating user demands, while also optimizing costs and sustainability by avoiding over-provisioning when demand is low. ###### Best practices <br>• [EUCSUS01-BP01 Choose the appropriate fleet type](eucsus01-bp01.md "eucsus01-bp01.md") <br>• [EUCSUS01-BP02 Choose the appropriate running mode for your Amazon WorkSpaces](eucsus01-bp02.md "eucsus01-bp02.md") <br>• [EUCSUS02-BP01 Select the instance type or bundle to match software requirement and user personas](eucsus02-bp01.md "eucsus02-bp01.md") <br>• [EUCSUS03-BP01 Adapt your AppStream 2.0 fleet timeout](eucsus03-bp01.md "eucsus03-bp01.md") <br>• [EUCSUS03-BP02 Adapt the AutoStop timeout and idle disconnect timeout for Amazon DCV](eucsus03-bp02.md "eucsus03-bp02.md") <br>• [EUCSUS04-BP01 Implement a scaling methodology in AppStream 2.0](eucsus04-bp01.md "eucsus04-bp01.md")
