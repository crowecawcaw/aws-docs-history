

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Windows Instances
<a name="fw-app-access-windows"></a>

These are the rules to configure for your Windows parent and child domain controllers.

## Parent Domain Controller, Windows
<a name="parent-domain-controller-win"></a>


**FROM: Parent domain controllers TO: Windows stack and shared services subnets**  

| Source Port | Destination Port | Protocol | 
| --- | --- | --- | 
| 88 | 49152 - 65535 | TCP | 
| 389 | 49152 - 65535 | UDP | 




**FROM: Stack subnets, including shared services TO: Windows forest root domain controllers**  

| Source Port | Destination Port | Protocol | 
| --- | --- | --- | 
| 49152 - 65535 | 88 | TCP | 
| 49152 - 65535 | 389 | UDP | 

## Child Domain Controller, Windows
<a name="child-domain-controller-win"></a>


**FROM: Child domain controllers TO: Windows AWS domain controllers**  

| Source Port | Destination Port | Protocol | 
| --- | --- | --- | 
| 49152 - 65535 | 53 | TCP | 
| 49152 - 65535 | 88 | TCP | 
| 49152 - 65535 | 389 | UDP | 


**FROM: Child domain controllers TO: Windows stack and shared services subnets**  

| Source Port | Destination Port | Protocol | 
| --- | --- | --- | 
| 88 | 49152 - 65535 | TCP | 
| 135 | 49152 - 65535 | TCP | 
| 389 | 49152 - 65535 | TCP | 
| 389 | 49152 - 65535 | UDP | 
| 445 | 49152 - 65535 | TCP | 
| 49152 - 65535 | 49152 - 65535 | TCP | 


**FROM: Stack subnets, including shared services TO: Windows child domain controllers**  

| Source Port | Destination Port | Protocol | 
| --- | --- | --- | 
| 49152 - 65535 | 88 | TCP | 
| 49152 - 65535 | 135 | TCP | 
| 49152 - 65535 | 389 | TCP | 
| 49152 - 65535 | 389 | UDP | 
| 49152 - 65535 | 445 | TCP | 
| 49152 - 65535 | 49152 - 65535 | TCP | 