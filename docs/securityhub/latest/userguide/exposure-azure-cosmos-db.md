

# Remediating exposures for Azure Cosmos DB accounts
<a name="exposure-azure-cosmos-db"></a>

AWS Security Hub can generate exposure findings for Azure Cosmos DB accounts.

On the Security Hub console, the Azure Cosmos DB account involved in an exposure finding and its identifying information are listed in the **Resources** section of the finding details. Programmatically, you can retrieve resource details with the [GetFindingsV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetFindingsV2.html) operation of the Security Hub CSPM API.

After identifying the resource involved in an exposure finding, you can delete the resource if you don't need it. Deleting a nonessential resource can reduce your exposure profile and AWS costs. If the resource is essential, follow these recommended remediation steps to help mitigate the risk. The remediation topics are divided based on the type of trait. 

A single exposure finding contains issues identified in multiple remediation topics. Conversely, you can address an exposure finding and bring down its severity level by addressing just one remediation topic. Your approach to risk remediation depends on your organizational requirements and workloads.

**Note**  
 The remediation guidance provided in this topic might require additional consultation in other Microsoft Azure resources. 

**Contents**
+ [Misconfiguration traits for Azure Cosmos DB accounts](#azure-cosmos-misconfiguration)
  + [The Azure Cosmos DB account has public network access enabled](#cosmos-public-network-access)
  + [The Azure Cosmos DB account does not use continuous backup](#cosmos-continuous-backup-disabled)

## Misconfiguration traits for Azure Cosmos DB accounts
<a name="azure-cosmos-misconfiguration"></a>

Here are misconfiguration traits for Azure Cosmos DB accounts and suggested remediation steps.

### The Azure Cosmos DB account has public network access enabled
<a name="cosmos-public-network-access"></a>

 When public network access is enabled, the Azure Cosmos DB account is reachable through a public endpoint. It can accept connections from the public internet, subject to firewall and virtual network rules. A public endpoint increases the attack surface of your account and exposes it to unauthorized connection attempts and potential data exfiltration. Following standard security principles, disable public network access and connect to the account privately, or tightly restrict the account firewall rules. 

**Remediation**  
Take one or more of the following actions to address this exposure:

**Disable public network access and use Private Link**  
 Set the account's `publicNetworkAccess` property to `Disabled` and connect through a private endpoint (Azure Private Link) within your virtual network. When combined with restrictive network security group policies, private endpoints help reduce the risk of data exfiltration. For more information, see [Configure Azure Private Link](https://learn.microsoft.com/en-us/azure/cosmos-db/how-to-configure-private-endpoints) in the Microsoft Azure documentation. 

**Restrict firewall rules if public access is required**  
 If you must keep public access enabled, configure IP firewall rules and virtual network rules to allow only the specific trusted sources your workload requires, instead of allowing all networks. For more information, see [Configure IP firewall](https://learn.microsoft.com/en-us/azure/cosmos-db/how-to-configure-firewall) in the Microsoft Azure documentation. 

### The Azure Cosmos DB account does not use continuous backup
<a name="cosmos-continuous-backup-disabled"></a>

 With continuous backup mode, you can use point-in-time restore to recover from an accidental write or delete. You can also restore a deleted database or container to any timestamp within the retention period. When the account uses periodic backup mode instead of continuous backup, you cannot perform self-service point-in-time restore. This limitation increases recovery time and the risk of data loss after an accidental or malicious change. Following data protection best practices, enable continuous backup mode where your workload supports it. 

**Remediation: Enable continuous backup mode**  
 Configure the account to use continuous backup mode (7-day or 30-day tier) so that point-in-time restore is available. Review the current limitations and supported APIs before migrating from periodic to continuous backup. For more information, see [Continuous backup with point-in-time restore](https://learn.microsoft.com/en-us/azure/cosmos-db/continuous-backup-restore-introduction) in the Microsoft Azure documentation. 