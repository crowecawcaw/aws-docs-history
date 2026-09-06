

# Network Exclusions
<a name="network-exclusions"></a>

 The WorkSpaces Applications management network range (`198.19.0.0/16`) and following ports and addresses should not be blocked by any security / firewall or antivirus solutions within WorkSpaces Applications instances. 

 *Table 7 — Ports in WorkSpaces Applications streaming instances security software must not interfere with* 


|  **Port**  |   **Usage**   | 
| --- | --- | 
|  8300  |  This is used for establishing the streaming connection  | 
|  3128  |  This is used for managing the streaming instance by WorkSpaces Applications  | 
|  8000  |  This is used for managing the streaming instance by WorkSpaces Applications  | 
|  8443  |  This is used for managing the streaming instance by WorkSpaces Applications  | 
|  53  |  DNS  | 

 *Table 8 — WorkSpaces Applications managed service addresses security software must not interfere with* 


|  **Port**  |  **Usage**  | 
| --- | --- | 
|  169.254.169.123  |  NTP  | 
|  169.254.169.249  |  NVIDIA GRID License Service  | 
|  169.254.169.250  |  KMS  | 
|  169.254.169.251  |  KMS  | 
|  169.254.169.253  |  DNS  | 
|  169.254.169.254  |  Metadata  | 