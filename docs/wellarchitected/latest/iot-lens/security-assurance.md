

# Security assurance
<a name="security-assurance"></a>

 Assuring security of IoT applications involves identifying the regulations which are applicable to the IoT devices or gateways and application code, establishing the set of controls which must be adhered to from those regulations, and assessing the devices or gateways and application against those controls. While proving that something is secure is, in general, difficult, it is possible to show or exhibit how a solution is architected, built, deployed, and operated. This information can show that relevant security configuration is set up as expected. Additional information can also show how the solution would detect risks and incidents so that appropriate response and recovery activities would take effect. Taken together, a solution can be evaluated for meeting required controls and being prepared to address situations where the controls did not prevent an incident from occurring. 

 Preparing for security assurance involves configuring for and collecting evidence that is used for logging, monitoring, auditing, and reporting. Performing security assurance activities includes evaluating the evidence provided and verifying those devices or gateways and solution components are configured according to required policies and controls. 

 Relevant regulations or standards for IoT applications include [ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards), [Purdue Model](https://www.energy.gov/sites/default/files/2022-10/Infra_Topic_Paper_4-14_FINAL.pdf), and the [Industrial Internet of Things Security Framework (IISF)](https://www.iiconsortium.org/iisf/). In addition, standards and frameworks such as [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework), [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final), and [NIST 800-82](https://csrc.nist.gov/pubs/sp/800/82/r3/final) and standards related to connected mobile security may also apply. If personal information is involved, privacy regulations such as [General Data Protection Regulation (GDPR)](https://gdpr-info.eu/) and [California Consumer Privacy Act (CCPA)](https://oag.ca.gov/privacy/ccpa) may also apply and be considered. Industry specific regulations or standards may also apply, such as [North American Electric Reliability Corporation – Critical Infrastructure Protection (NERC-CIP)](https://www.nerc.com/pa/Stand/Pages/ReliabilityStandards.aspx). 

 In order to streamline and automate assurance activities as much as possible, employ compliance as code mechanisms which build automation into performing compliance checks and result in testing or verification logs which can be evaluated for both adherence to required controls and which violated controls must be remediated. 


| IOTSEC15: What regulations apply to your IoT applications and how do you show compliance with these regulations? | 
| --- | 
|   | 

 To carry out security assurance, understand which regulations apply to your IoT applications. Establish the set of regulations and plan to re-evaluate the set of regulations whenever the features or information processed by the application changes and at regular time intervals, for example, on a yearly review schedule. 

## IOTSEC15-BP01 Identify the set of relevant regulations for your IoT applications
<a name="iotsec15-bp01"></a>

 Establish both the security and privacy related regulations which apply to IoT applications. If the application processes any information related to humans, then pay particular attention to privacy regulations and the sets of people that will use the application. 

 **Level of risk exposed if this best practice is not established:** Medium 

 **Prescriptive guidance IOTSEC15-BP01-01** *Understand which standards and regulations apply to the IoT application.* 

 The following standards and regulations are a starting point to use to understand which regulations apply to the application. There may be industry-specific regulations which also apply: 
+  [ISA/IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards) 
+  [ISO/IEC 33601](https://www.iso.org/standard/80362.html) 
+  [ISO/SAE 21434](https://www.iso.org/standard/70918.html) 
+  [Purdue Model](https://www.energy.gov/sites/default/files/2022-10/Infra_Topic_Paper_4-14_FINAL.pdf) 
+  [Industrial Internet of Things Security Framework (IISF)](https://www.iiconsortium.org/iisf/) 
+  [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework) 
+  [NIST 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) 
+  [General Data Protection Regulation (GDPR)](https://gdpr-info.eu/) 
+  [California Consumer Privacy Act (CCPA)](https://oag.ca.gov/privacy/ccpa) 
+  [NERC-CIP](https://www.nerc.com/pa/Stand/Pages/ReliabilityStandards.aspx) 
+  [Automotive Information Sharing and Analysis Center (Auto-ISAC)](https://automotiveisac.com/) 
+  [National Highway Traffic Safety Administration (NHTSA)](https://www.nhtsa.gov/) 

 **Prescriptive guidance IOTSEC15-BP01-02** *Determine which controls within the regulations apply to the IoT devices or gateways and application components.* 

 Within each regulation, determine which controls apply to the IoT application, the devices and gateways used in the application, and other services that are made use of by the application. Compliance with these controls can then be evaluated. 

## IOTSEC15-BP02 Set up logging and monitoring to support audit checks for compliance
<a name="iotsec15-bp02"></a>

 Logging and monitoring provide a means of building a base of evidence which can be used to show both explicit compliance with regulations and, in the case of attempting to show that something did not happen, showing that there are checks and processing in place which would have identified an issue if that issue have been present. 

 **Level of risk exposed if this best practice is not established:** Low 

 **Prescriptive guidance IOTSEC15-BP02-01** *Centralize storage of log records used for audit reporting.* 

 Use a centralized storage mechanism for log records to reduce the potential for log records being lost or tampering with log records by authorized or unauthorized users. By off-loading log records to a separate storage location which has different access controls, the potential for log record tampering can be greatly reduced. Refer to recommendations for audit and logging in the [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/welcome.html)(AWS SRA) for examples of centralizing log management and auditing activities. 

 **Prescriptive guidance IOTSEC15-BP02-02** *Identify which log information can be used to show compliance with which controls.* 

 For each control which can be checked based on log information collected, identify the log records in the logged information which provide positive evidence of compliance with the control. For controls which require evidence that something did not occur, use log records which show that if a situation did occur, a log record would have signaled that situation. Use log testing events and mock situations to test and verify that this is the case. 

## IOTSEC15-BP03 Implement automated compliance checking using compliance as code
<a name="iotsec15-bp03"></a>

 With an understanding of which logged information provides evidence of compliance with controls, automated compliance checks can be implemented which use the log data and evaluate the compliance check. 

 **Level of risk exposed if this best practice is not established:** Medium 

 **Prescriptive guidance IOTSEC15-BP03-01** *Use automated compliance checking tools to evaluate compliance and produce summary reports and dashboards.* 

 Use tools such as [AWS Config](https://aws.amazon.com/config/) and rules development kit (RDK), [Amazon CloudWatch](https://aws.amazon.com/pm/cloudwatch/), [Amazon EventBridge](https://aws.amazon.com/pm/eventbridge/) Rules, and [Serverless Computing - AWS Lambda](https://aws.amazon.com/pm/lambda/). to automate compliance checks. 

 **Prescriptive guidance IOTSEC15-BP03-02** *Integrate compliance checking with other problem management tools that are used by the development and operations teams.* 

 Any work items or tasks which are generated from automated compliance of IoT application logs should be reflected back into the problem management tools used by the application and infrastructure development teams. Depending on the tools used to perform compliance checks, this integration can be built into the environment by using services such as [Amazon EventBridge](https://aws.amazon.com/eventbridge/) coupled with [Amazon Simple Queue Service](https://aws.amazon.com/pm/sqs/) and [Serverless Computing - AWS Lambda](https://aws.amazon.com/pm/lambda/). 