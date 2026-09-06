

# Preventive controls
<a name="preventive-controls"></a>

A preventive control ensures that your accounts maintain compliance, because it disallows actions that lead to policy violations. The status of a preventive control is either **enforced** or **not enabled**. Preventive controls are supported in all AWS Regions.
+ Preventive controls are implemented using service control policies (SCPs), or resource control policies (RCPs), each of which are part of AWS Organizations.
+ Regarding nested OUs, preventive controls enabled on any OUs higher in the tree will apply to unregistered OUs in that tree.
+ When you enable controls on an organizational unit (OU) that is registered with AWS Control Tower, preventive controls apply to all member accounts under the OU, enrolled and unenrolled. 

**Note**  [Mandatory controls](mandatory-controls.md)
Detect Public Read Access Setting for Log Archive
Detect Public Write Access Setting for Log Archive
Detect whether shared accounts under the Security organizational unit have AWS CloudTrail or CloudTrail Lake enabled

**Topics**
+ [Controls implemented with resource control policies (RCPs)](rcp-controls.md)
+ [Controls implemented with declarative policies](declarative-controls.md)
+ [Controls for AWS Backup](backup-controls.md)
+ [Digital sovereignty controls](digital-sovereignty-controls.md)