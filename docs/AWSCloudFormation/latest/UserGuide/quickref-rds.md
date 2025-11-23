# Amazon RDS template snippets

###### Topics

- [Amazon RDS DB instance resource](#scenario-rds-instance "#scenario-rds-instance")
- [Amazon RDS oracle database DB instance resource](#scenario-rds-oracleinstance "#scenario-rds-oracleinstance")
- [Amazon RDS DBSecurityGroup resource for CIDR range](#scenario-rds-security-group-cidr "#scenario-rds-security-group-cidr")
- [Amazon RDS DBSecurityGroup with an Amazon EC2 security group](#scenario-rds-security-group-ec2 "#scenario-rds-security-group-ec2")
- [Multiple VPC security groups](#scenario-multiple-vpc-security-groups "#scenario-multiple-vpc-security-groups")
- [Amazon RDS database instance in a VPC security group](#w2aac11c41c76c15 "#w2aac11c41c76c15")

## Amazon RDS DB instance resource

This example shows an Amazon RDS DB Instance resource with managed master user password. For more information,
see [Password management with AWS Secrets Manager](../../../AmazonRDS/latest/UserGuide/rds-secrets-manager.md "../../../AmazonRDS/latest/UserGuide/rds-secrets-manager.md")
in the _Amazon RDS User Guide_
and [Password management with AWS Secrets Manager](../../../AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.md "../../../AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.md")
in the _Aurora User Guide_. Because the optional `EngineVersion`
property isn't specified, the default engine version is used for this DB Instance. For details
about the default engine version and other default settings, see [CreateDBInstance](../../../AmazonRDS/latest/APIReference/API_CreateDBInstance.md "../../../AmazonRDS/latest/APIReference/API_CreateDBInstance.md"). The `DBSecurityGroups` property authorizes network ingress to the
`AWS::RDS::DBSecurityGroup` resources named `MyDbSecurityByEC2SecurityGroup` and
MyDbSecurityByCIDRIPGroup. For details, see [AWS::RDS::DBInstance](../TemplateReference/aws-resource-rds-dbinstance.md "../TemplateReference/aws-resource-rds-dbinstance.md"). The DB Instance resource also has a `DeletionPolicy` attribute
set to `Snapshot`. With the `Snapshot` `DeletionPolicy` set, CloudFormation will take a snapshot of this DB
Instance before deleting it during stack deletion.

### JSON

```
"MyDB" : {
 "Type" : "AWS::RDS::DBInstance",
 "Properties" : {
     "DBSecurityGroups" : [
        {"Ref" : "MyDbSecurityByEC2SecurityGroup"}, {"Ref" : "MyDbSecurityByCIDRIPGroup"} ],
     "AllocatedStorage" : "5",
     "DBInstanceClass" : "db.t2.small",
     "Engine" : "MySQL",
     "MasterUsername" : "MyName",
     "ManageMasterUserPassword" : true,
     "MasterUserSecret" : {
        "KmsKeyId" : {"Ref" : "KMSKey"}
     }
 },
 "DeletionPolicy" : "Snapshot"
}
```

### YAML

```
MyDB:
  Type: AWS::RDS::DBInstance
  Properties:
    DBSecurityGroups:
    - Ref: MyDbSecurityByEC2SecurityGroup
    - Ref: MyDbSecurityByCIDRIPGroup
    AllocatedStorage: '5'
    DBInstanceClass: db.t2.small
    Engine: MySQL
    MasterUsername: MyName
    ManageMasterUserPassword: true
    MasterUserSecret:
      KmsKeyId: !Ref KMSKey
  DeletionPolicy: Snapshot
```

## Amazon RDS oracle database DB instance resource

This example creates an Oracle Database DB Instance resource with managed master user password. For more information,
see [Password management with AWS Secrets Manager](../../../AmazonRDS/latest/UserGuide/rds-secrets-manager.md "../../../AmazonRDS/latest/UserGuide/rds-secrets-manager.md")
in the _Amazon RDS User Guide_.
The example specifies the `Engine` as `oracle-ee` with a
license model of bring-your-own-license. For details about the settings for Oracle Database DB instances, see
[CreateDBInstance](../../../AmazonRDS/latest/APIReference/API_CreateDBInstance.md "../../../AmazonRDS/latest/APIReference/API_CreateDBInstance.md"). The DBSecurityGroups property authorizes network ingress to the
`AWS::RDS::DBSecurityGroup` resources named MyDbSecurityByEC2SecurityGroup and MyDbSecurityByCIDRIPGroup. For
details, see [AWS::RDS::DBInstance](../TemplateReference/aws-resource-rds-dbinstance.md "../TemplateReference/aws-resource-rds-dbinstance.md"). The DB Instance resource also has a
`DeletionPolicy` attribute set to `Snapshot`. With the `Snapshot` `DeletionPolicy` set, CloudFormation will take a snapshot
of this DB Instance before deleting it during stack deletion.

### JSON

```
"MyDB" : {
 "Type" : "AWS::RDS::DBInstance",
 "Properties" : {
     "DBSecurityGroups" : [
        {"Ref" : "MyDbSecurityByEC2SecurityGroup"}, {"Ref" : "MyDbSecurityByCIDRIPGroup"} ],
     "AllocatedStorage" : "5",
     "DBInstanceClass" : "db.t2.small",
     "Engine" : "oracle-ee",
     "LicenseModel" : "bring-your-own-license",
     "MasterUsername" : "master",
     "ManageMasterUserPassword" : true,
     "MasterUserSecret" : {
        "KmsKeyId" : {"Ref" : "KMSKey"}
     }
 },
 "DeletionPolicy" : "Snapshot"
}
```

### YAML

```
MyDB:
  Type: AWS::RDS::DBInstance
  Properties:
    DBSecurityGroups:
    - Ref: MyDbSecurityByEC2SecurityGroup
    - Ref: MyDbSecurityByCIDRIPGroup
    AllocatedStorage: '5'
    DBInstanceClass: db.t2.small
    Engine: oracle-ee
    LicenseModel: bring-your-own-license
    MasterUsername: master
    ManageMasterUserPassword: true
    MasterUserSecret:
      KmsKeyId: !Ref KMSKey
  DeletionPolicy: Snapshot
```

## Amazon RDS DBSecurityGroup resource for CIDR range

This example shows an Amazon RDS `DBSecurityGroup` resource with ingress authorization for the specified CIDR
range in the format `ddd.ddd.ddd.ddd/dd`. For details, see
[AWS::RDS::DBSecurityGroup](../TemplateReference/aws-resource-rds-dbsecuritygroup.md "../TemplateReference/aws-resource-rds-dbsecuritygroup.md") and
[Ingress](../TemplateReference/aws-properties-rds-dbsecuritygroup-ingress.md "../TemplateReference/aws-properties-rds-dbsecuritygroup-ingress.md").

### JSON

```
"MyDbSecurityByCIDRIPGroup" : {
 "Type" : "AWS::RDS::DBSecurityGroup",
 "Properties" : {
     "GroupDescription" : "Ingress for CIDRIP",
     "DBSecurityGroupIngress" : {
         "CIDRIP" : "`192.168.0.0/32`"
     }
 }
}
```

### YAML

```
MyDbSecurityByCIDRIPGroup:
  Type: AWS::RDS::DBSecurityGroup
  Properties:
    GroupDescription: Ingress for CIDRIP
    DBSecurityGroupIngress:
      CIDRIP: "`192.168.0.0/32`"
```

## Amazon RDS DBSecurityGroup with an Amazon EC2 security group

This example shows an [AWS::RDS::DBSecurityGroup](../TemplateReference/aws-resource-rds-dbsecuritygroup.md "../TemplateReference/aws-resource-rds-dbsecuritygroup.md")
resource with ingress authorization from an Amazon EC2 security group referenced by `MyEc2SecurityGroup`.

To do this, you define an EC2 security group and then use the intrinsic `Ref` function to refer to the EC2
security group within your `DBSecurityGroup`.

### JSON

```

"DBInstance" : {
   "Type": "AWS::RDS::DBInstance",
   "Properties": {
      "DBName"            : { "Ref" : "DBName" },
      "Engine"            : "MySQL",
      "MasterUsername"    : { "Ref" : "DBUsername" },
      "DBInstanceClass"   : { "Ref" : "DBClass" },
      "DBSecurityGroups"  : [ { "Ref" : "DBSecurityGroup" } ],
      "AllocatedStorage"  : { "Ref" : "DBAllocatedStorage" },
      "MasterUserPassword": { "Ref" : "DBPassword" }
   }
},

"DBSecurityGroup": {
   "Type": "AWS::RDS::DBSecurityGroup",
   "Properties": {
      "DBSecurityGroupIngress": {
         "EC2SecurityGroupName": {
            "Fn::GetAtt": ["WebServerSecurityGroup", "GroupName"]
         }
      },
      "GroupDescription" : "Frontend Access"
   }
},

"WebServerSecurityGroup" : {
   "Type" : "AWS::EC2::SecurityGroup",
   "Properties" : {
      "GroupDescription" : "Enable HTTP access via port 80 and SSH access",
      "SecurityGroupIngress" : [
         {"IpProtocol" : "tcp", "FromPort" : 80, "ToPort" : 80, "CidrIp" : "0.0.0.0/0"},
         {"IpProtocol" : "tcp", "FromPort" : 22, "ToPort" : 22, "CidrIp" : "0.0.0.0/0"}
      ]
   }
}
```

### YAML

This example is extracted from the following full example: [Drupal_Single_Instance_With_RDS.template](https://s3.amazonaws.com/cloudformation-templates-us-east-1/Drupal_Single_Instance_With_RDS.template "https://s3.amazonaws.com/cloudformation-templates-us-east-1/Drupal_Single_Instance_With_RDS.template")

```
DBInstance:
  Type: AWS::RDS::DBInstance
  Properties:
    DBName:
      Ref: DBName
    Engine: MySQL
    MasterUsername:
      Ref: DBUsername
    DBInstanceClass:
      Ref: DBClass
    DBSecurityGroups:
    - Ref: DBSecurityGroup
    AllocatedStorage:
      Ref: DBAllocatedStorage
    MasterUserPassword:
      Ref: DBPassword
DBSecurityGroup:
  Type: AWS::RDS::DBSecurityGroup
  Properties:
    DBSecurityGroupIngress:
      EC2SecurityGroupName:
        Ref: WebServerSecurityGroup
    GroupDescription: Frontend Access
WebServerSecurityGroup:
  Type: AWS::EC2::SecurityGroup
  Properties:
    GroupDescription: Enable HTTP access via port 80 and SSH access
    SecurityGroupIngress:
    - IpProtocol: tcp
      FromPort: 80
      ToPort: 80
      CidrIp: 0.0.0.0/0
    - IpProtocol: tcp
      FromPort: 22
      ToPort: 22
      CidrIp: 0.0.0.0/0
```

## Multiple VPC security groups

This example shows an [AWS::RDS::DBSecurityGroup](../TemplateReference/aws-resource-rds-dbsecuritygroup.md "../TemplateReference/aws-resource-rds-dbsecuritygroup.md")
resource with ingress authorization for multiple Amazon EC2 VPC security groups in [AWS::RDS::DBSecurityGroupIngress](../TemplateReference/aws-resource-rds-dbsecuritygroupingress.md "../TemplateReference/aws-resource-rds-dbsecuritygroupingress.md").

### JSON

```
{
   "Resources" : {
      "DBinstance" : {
         "Type" : "AWS::RDS::DBInstance",
         "Properties" : {
            "AllocatedStorage" : "5",
            "DBInstanceClass" : "db.t2.small",
           "DBName" : {"Ref": "MyDBName" },
            "DBSecurityGroups" : [ { "Ref" : "DbSecurityByEC2SecurityGroup" } ],
            "DBSubnetGroupName" : { "Ref" : "MyDBSubnetGroup" },
            "Engine" : "MySQL",
           "MasterUserPassword": { "Ref" : "MyDBPassword" },
           "MasterUsername"    : { "Ref" : "MyDBUsername" }
        },
         "DeletionPolicy" : "Snapshot"
      },
      "DbSecurityByEC2SecurityGroup" : {
         "Type" : "AWS::RDS::DBSecurityGroup",
         "Properties" : {
            "GroupDescription" : "Ingress for Amazon EC2 security group",
           "EC2VpcId" : { "Ref" : "MyVPC" },
            "DBSecurityGroupIngress" : [ {
               "EC2SecurityGroupId" : "sg-b0ff1111",
               "EC2SecurityGroupOwnerId" : "111122223333"
            }, {
               "EC2SecurityGroupId" : "sg-ffd722222",
               "EC2SecurityGroupOwnerId" : "111122223333"
            } ]
         }
      }
   }
}
```

### YAML

```
Resources:
  DBinstance:
    Type: AWS::RDS::DBInstance
    Properties:
      AllocatedStorage: '5'
      DBInstanceClass: db.t2.small
      DBName:
        Ref: MyDBName
      DBSecurityGroups:
      - Ref: DbSecurityByEC2SecurityGroup
      DBSubnetGroupName:
        Ref: MyDBSubnetGroup
      Engine: MySQL
      MasterUserPassword:
        Ref: MyDBPassword
      MasterUsername:
        Ref: MyDBUsername
    DeletionPolicy: Snapshot
  DbSecurityByEC2SecurityGroup:
    Type: AWS::RDS::DBSecurityGroup
    Properties:
      GroupDescription: Ingress for Amazon EC2 security group
      EC2VpcId:
        Ref: MyVPC
      DBSecurityGroupIngress:
      - EC2SecurityGroupId: sg-b0ff1111
        EC2SecurityGroupOwnerId: '111122223333'
      - EC2SecurityGroupId: sg-ffd722222
        EC2SecurityGroupOwnerId: '111122223333'
```

## Amazon RDS database instance in a VPC security group

This example shows an Amazon RDS database instance associated with an Amazon EC2 VPC security
group.

### JSON

```
{
  "DBEC2SecurityGroup": {
    "Type": "AWS::EC2::SecurityGroup",
    "Properties" : {
      "GroupDescription": "Open database for access",
      "SecurityGroupIngress" : [{
        "IpProtocol" : "tcp",
        "FromPort" : 3306,
        "ToPort" : 3306,
        "SourceSecurityGroupName" : { "Ref" : "WebServerSecurityGroup" }
      }]
    }
  },
  "DBInstance" : {
    "Type": "AWS::RDS::DBInstance",
    "Properties": {
      "DBName"            : { "Ref" : "DBName" },
      "Engine"            : "MySQL",
      "MultiAZ"           : { "Ref": "MultiAZDatabase" },
      "MasterUsername"    : { "Ref" : "DBUser" },
      "DBInstanceClass"   : { "Ref" : "DBClass" },
      "AllocatedStorage"  : { "Ref" : "DBAllocatedStorage" },
      "MasterUserPassword": { "Ref" : "DBPassword" },
      "VPCSecurityGroups" : [ { "Fn::GetAtt": [ "DBEC2SecurityGroup", "GroupId" ] } ]
    }
  }
}
```

### YAML

```
DBEC2SecurityGroup:
  Type: AWS::EC2::SecurityGroup
  Properties:
    GroupDescription: Open database for access
    SecurityGroupIngress:
    - IpProtocol: tcp
      FromPort: 3306
      ToPort: 3306
      SourceSecurityGroupName:
        Ref: WebServerSecurityGroup
DBInstance:
  Type: AWS::RDS::DBInstance
  Properties:
    DBName:
      Ref: DBName
    Engine: MySQL
    MultiAZ:
      Ref: MultiAZDatabase
    MasterUsername:
      Ref: DBUser
    DBInstanceClass:
      Ref: DBClass
    AllocatedStorage:
      Ref: DBAllocatedStorage
    MasterUserPassword:
      Ref: DBPassword
    VPCSecurityGroups:
    - !GetAtt DBEC2SecurityGroup.GroupId
```
