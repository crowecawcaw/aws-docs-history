# Cache (ElastiCache Memcached) Stack | Create

Use to create an Amazon ElastiCache cluster (one or more cache nodes) that uses the Memcached engine, and specify CloudWatch metrics and alarms for the cluster.

**Full classification:** Deployment | Advanced stack components | Cache (ElastiCache Memcached) stack | Create

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-0xi6q7uwuwrqe |
| Current version             | 1.0              |
| Expected execution duration | 60 minutes       |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

### Create ElastiCache Memcached stack

The following shows this change type in the AMS console.

![Details of a Create Cache change type for an ElastiCache Memcached stack, including description and execution mode.](images/guiCacheMemCreateCT.png)
How it works:

1. Navigate to the **Create RFC** page: In the left navigation pane of the AMS console click **RFCs** to open the RFCs list page, and then click **Create RFC**.
2. Choose a popular change type (CT) in the default **Browse change types** view, or select a CT in the
   **Choose by category** view.
   - **Browse by change type**: You can click on a popular CT in the **Quick create** area to immediately open the
     **Run RFC** page. Note that you cannot choose an older CT version with quick create.

   To sort CTs, use the **All change types** area in either the **Card** or **Table** view.
   In either view, select a CT and then click **Create RFC** to open the **Run RFC** page. If applicable,
   a **Create with older version** option appears next to the **Create RFC** button.
   - **Choose by category**: Select a category, subcategory, item, and operation and the CT details box opens with an option to
     **Create with older version** if applicable. Click **Create RFC** to open the **Run RFC** page.

3. On the **Run RFC** page, open the CT name area to see the CT details box.
   A **Subject** is required (this is filled in for you if you choose your CT in the **Browse change types** view). Open the
   **Additional configuration** area to add information about the RFC.

In the **Execution configuration** area, use available drop-down lists or enter values for the required parameters. To configure
optional execution parameters, open the **Additional configuration** area. 4. When finished, click **Run**. If there are no errors, the **RFC successfully created**
page displays with the submitted RFC details, and the initial **Run output**. 5. Open the **Run parameters** area to see the configurations you submitted. Refresh the page to update the RFC execution status.
Optionally, cancel the RFC or create a copy of it with the options at the top of the page.
How it works:

1. Use either the Inline Create (you issue a `create-rfc` command with all RFC and execution parameters included), or
   Template Create (you create two JSON files, one for the RFC parameters and one for the execution parameters) and issue the `create-rfc`
   command with the two files as input. Both methods are described here.
2. Submit the RFC: `aws amscm submit-rfc --rfc-id `ID`` command with the returned RFC ID.

Monitor the RFC: `aws amscm get-rfc --rfc-id `ID`` command.
To check the change type version, use this command:

```
aws amscm list-change-type-version-summaries --filter Attribute=ChangeTypeId,Value=`CT_ID`
```

###### Note

You can use any `CreateRfc` parameters with any RFC whether or not they are part of the schema for the
change type. For example, to get notifications when the RFC status changes, add this line, `--notification "{\"Email\": {\"EmailRecipients\" : [\"email@example.com\"]}}"` to the
RFC parameters part of the request (not the execution parameters). For a list of all CreateRfc parameters, see the
[AMS Change Management API Reference](../ApiReference-cm/API_CreateRfc.md "../ApiReference-cm/API_CreateRfc.md").

_INLINE CREATE_:

Issue the create RFC command with execution parameters provided inline (escape quotes
when providing execution parameters inline), and then submit the returned RFC ID. For example, you can replace the contents with something like this:

```
aws amscm create-rfc --change-type-id "ct-0xi6q7uwuwrqe" --change-type-version "1.0" --execution-parameters "{\"Description\":\"`Test description`\",\"VpcId\":\"`VPC_ID`\",\"Name\":\"`TEST_MEMCACHE`\",\"StackTemplateId\":\"stm-sfpo2o00000000000\",\"TimeoutInMinutes\":60,\"Parameters\":{\"ElastiCacheAvailabilityZones": [ \"`eu-west-1b`\", \"`eu-west-1c`\" ],\"ElastiCacheClusterName\":\"`TEST_NAME`\",\"ElastiCacheEngine\":\"`redis`\",\"ElastiCacheSubnetIds\":[\"`SUBNET_ID`\"]}}"
```

_TEMPLATE CREATE_:

1. Output the execution parameters JSON schema for this change type to a JSON file;
   this example names it CreateMemcacheParams.json:

```
aws amscm get-change-type-version --change-type-id "ct-0xi6q7uwuwrqe" --query "ChangeTypeVersion.ExecutionInputSchema" --output text > CreateMemcacheParams.json
```

2. Modify and save the CreateMemcacheParams file as follows. For example, you can replace the contents with something like this:

```
{
  "Description": "`This is a test description`",
  "VpcId": "`VPC_ID`",
  "StackTemplateId": "stm-sfpo2o00000000000",
  "Name": "`Test Stack`",
  "Tags": [
    {
      "Key": "`foo`",
      "Value": "`bar`"
    },
    {
      "Key": "`testkey`",
      "Value": "`testvalue`"
    }
  ],
  "TimeoutInMinutes": 60,
  "Parameters": {
    "ElastiCacheAvailabilityZones": [ "`eu-west-1b`", "`eu-west-1c`" ],
    "ElastiCacheClusterName": "`test-cluster`",
    "ElastiCacheEngine": "memcached",
    "ElastiCacheSubnetIds": [ "`SUBNET_ID`" , "`SUBNET_ID`" ]
  }
}
```

3. Output the RFC template to a file in your current folder; this example names it CreateMemcacheRfc.json:

```
aws amscm create-rfc --generate-cli-skeleton > CreateMemcacheRfc.json
```

4. Modify and save the CreateMemcacheRfc.json file. For example, you can replace the contents with something like this:

```
{
"ChangeTypeVersion":    "`1.0`",
"ChangeTypeId":         "ct-0xi6q7uwuwrqe",
"Title":                "`Memcache-Create-RFC`"
}
```

5. Create the RFC, specifying the CreateMemcacheRfc file and the CreateMemcacheParams file:

```
aws amscm create-rfc --cli-input-json file://CreateMemcacheRfc.json --execution-parameters file://CreateMemcacheParams.json
```

You receive the ID of the new RFC in the response and can use it to submit and monitor the RFC. Until you submit it, the RFC remains in the editing state and does not start.
For more information, see [Amazon ElastiCache for Memcached](https://aws.amazon.com/elasticache/memcached/ "https://aws.amazon.com/elasticache/memcached/").

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-0xi6q7uwuwrqe](schemas.md#ct-0xi6q7uwuwrqe-schema-section "schemas.md#ct-0xi6q7uwuwrqe-schema-section").

## Example: Required Parameters

```
{
  "Description": "This is a test description",
  "VpcId": "vpc-1234567890abcdef0",
  "StackTemplateId": "stm-sfpo2o00000000000",
  "Name": "Test Stack",
  "Tags": [
    {
      "Key": "foo",
      "Value": "bar"
    },
    {
      "Key": "testkey",
      "Value": "testvalue"
    }
  ],
  "TimeoutInMinutes": 60,
  "Parameters": {
    "ElastiCacheAvailabilityZones": [ "eu-west-1b", "eu-west-1c" ],
    "ElastiCacheClusterName": "some-cluster",
    "ElastiCacheEngine": "memcached",
    "ElastiCacheSubnetIds": [ "subnet-1234567890abcdef0", "subnet-1234567890abcdef1" ]
  }
}

```

## Example: All Parameters

```
{
  "Description": "This is a test description",
  "VpcId": "vpc-1234abcd",
  "StackTemplateId": "stm-sfpo2o00000000000",
  "Name": "Test Stack",
  "Tags": [
    {
      "Key": "foo",
      "Value": "bar"
    },
    {
      "Key": "testkey",
      "Value": "testvalue"
    }
  ],
  "TimeoutInMinutes": 60,
  "Parameters": {
    "ElastiCacheAutoMinorVersionUpgrade": true,
    "ElastiCacheAvailabilityZones": ["eu-west-1a","eu-west-1b"],
    "ElastiCacheClusterName": "mmulti-az",
    "ElastiCacheCPUThresholdAlarmOverride": 95,
    "ElastiCacheEngine": "memcached",
    "ElastiCacheEngineVersion": "1.4.25",
    "ElastiCacheInstanceType": "cache.t1.micro",
    "ElastiCacheMultiAZ": true,
    "ElastiCacheNumberOfNodes": 2,
    "ElastiCachePort": 1121,
    "ElastiCachePreferredMaintenanceWindow": "sun:05:00-sun:09:00",
    "ElastiCacheSubnetGroup": "cachegroup",
    "ElastiCacheSubnetIds": ["subnet-1234abcd","subnet-1a2b3c4d"],
    "SecurityGroups": ["sg-1234abcd"]
  }
}

```
