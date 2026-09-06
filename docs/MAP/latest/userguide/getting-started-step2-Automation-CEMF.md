

# Cloud Migration Factory Solution (CMF)
<a name="getting-started-step2-Automation-CEMF"></a>

Cloud Migration Factory Solution coordinates and automates large scale migrations to the AWS Cloud, involving numerous servers. Enterprises can improve performance and prevent long cutover windows by automating manual processes and integrating multiple tools efficiently. This is possible through this solution’s orchestration platform options, which includes MGN(MGN). We recommend using AWS MGN to rehost servers to AWS at scale. Today, this solution is used by AWS Professional Services, AWS Partners, and other enterprises. For more information about CMF, see the [Coordinate and automate large scale migrations to the AWS Cloud using the Cloud Migration Factory on AWS solution](https://aws.amazon.com/solutions/implementations/aws-cloudendure-migration-factory-solution/) in the *Cloud Migration Factory on AWS implementation guide*.

Use the steps outlined below to add tags to all imported servers in CMF.



**To get started**

1. Use the following script to add tags to all imported servers in CMF:

   

   ```
   # Version: 09APR2021.01
   
   from __future__ import print_function
   import sys
   import argparse
   import requests
   import json
   import csv
   import boto3
   import botocore.exceptions
   import mfcommon
   
   serverendpoint = mfcommon.serverendpoint
   
   with open('FactoryEndpoints.json') as json_file:
       endpoints = json.load(json_file)
   
   def get_reader(file):
       ordered_dict_list = []
       input_file = csv.DictReader(open(file))
       for row in input_file:
           ordered_dict_list.append(row)
       # return input_file
       return ordered_dict_list
   
   def data_validation(data, servers):
       # Validate if Name column exist
       keys = data[0].keys()
       if "Name" not in keys:
           print ("ERROR: 'Name' column is mandatory")
           sys.exit(3)
       # check if none value exist
       for row in data:
           for key in keys:
               if key not in row:
                  print("ERROR: "+ key + " tag value is missing for server " + row['Name'])
                  sys.exit(4)
               if row[key] == None:
                  print("ERROR: "+ key + " tag value is missing for server " + row['Name'])
                  sys.exit(6)
               if row[key] == row[key].strip() == "":
                  print("ERROR: "+ key + " tag for server " + row['Name'] + " is empty")
                  sys.exit(7)
       # Validate duplicate server names in csv file
       server_list = []
       for row in data:
           if row['Name'].strip().lower() not in server_list:
               server_list.append(str(row['Name']).strip().lower())
           else:
               print("ERROR: Duplicated Server Name: " + row['Name'])
               sys.exit(2)
       # Check if server exist in the migration factory
       for server in server_list:
           match = False
           for s in servers:
               if (server.lower() == s['server_name'].lower()):
                   match = True
           if (match == False):
               print("ERROR: Server " + server + " doesn't exist in the migration factory")
               sys.exit(1)
   
   
   def uploading_data(data, token, UserHOST):
       keys = data[0].keys()
       auth = {"Authorization": token}
       servers = json.loads(requests.get(UserHOST + serverendpoint, headers=auth).text)
       data_validation(data, servers)
       for row in data:
           update_server_tags = {}
           tags = []
           server_id = ""
           for server in servers:
               if row['Name'].strip().lower() == server['server_name'].strip().lower():
                   server_id = server["server_id"]
                   for key in keys:
                       tag = {}
                       tag['key'] = key
                       tag['value'] = row[key].strip()
                       tags.append(tag)
           update_server_tags['tags'] = tags
           r = requests.put(UserHOST + serverendpoint + '/' + server_id, headers=auth, data=json.dumps(update_server_tags))
           if r.status_code == 200:
              print("Tags for server " + row['Name'] + " updated in the migration factory")
           else:
              print("ERROR: updating tags for server " + row['Name'] + " failed : " + r.text + ".......")
   
   def main(arguments):
       parser = argparse.ArgumentParser(
           description=__doc__,
           formatter_class=argparse.RawDescriptionHelpFormatter)
       parser.add_argument('--Intakeform', required=True)
       args = parser.parse_args(arguments)
   
       UserHOST = ""
   
       # Get MF endpoints from FactoryEndpoints.json file
       if 'UserApiUrl' in endpoints:
           UserHOST = endpoints['UserApiUrl']
       else:
           print("ERROR: Invalid FactoryEndpoints.json file, please update UserApiUrl")
           sys.exit()
   
       print("****************************")
       print("*Login to Migration factory*")
       print("****************************")
       token = mfcommon.Factorylogin()
   
       print("****************************")
       print("*  Reading Tags form List  *")
       print("****************************")
       data = get_reader(args.Intakeform)
       print("Tags loaded for processing....")
       print("")
   
       print("*********************************************")
       print("*   Updating tags in the migration factory  *")
       print("*********************************************")
   
       r = uploading_data(data,token,UserHOST)
   
   if __name__ == '__main__':
       sys.exit(main(sys.argv[1:]))
   ```

1. Go to the migrated resources such as Amazon RDS.

1. Choose **Add tags**.

1. Enter `map-migrated` as the Tag key.

1. Enter and replace your **MPE ID** with the tag value you want to apply to the migrated workloads.

   **Example**: 
   + If your MPE ID is {{12345}}, use the value {{mig12345}}.
   + If your MPE ID is {{ABCDE12345}}, use the value {{migABCDE12345}}.

1. Choose **Add tags**.

Depending on your migrated resource and MPE ID, the tag value can be any of the following:

## Short MPE IDs
<a name="cemf-short-ids"></a>
+ `mig{{5-digit MPE ID}}`
+ `sap{{5-digit MPE ID}}`
+ `oracle{{5-digit MPE ID}}`

## Long MPE IDs
<a name="cemf-long-ids"></a>
+ `mig{{10 alphanumeric MPE ID characters}}`
+ `sap{{10 alphanumeric MPE ID characters}}`
+ `oracle{{10 alphanumeric MPE ID characters}}`

**Note**  
Use lowercase letters for the `mig`, `sap`, and `oracle` prefixes and uppercase letters for the alphanumeric MPE IDs (long MPE IDs). For more information about what tag values you should use, see [Tagging key combinations](setting-up.md). For more information about your MPE ID, see [MPE ID length](mpe-length.md).

Repeat the steps above for any other associated resources such as Snapshots. For more information about what tags you should use, see [Tagging key combinations](setting-up.md).



**Note**  
The Migration Acceleration Program requires that you tag resources with the `map-migrated` tag. This tag is automatically activated for you as a cost allocation tag. Tags that are automatically activated don't count towards your cost allocation tag quota. For more information, see [Quotas and restrictions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-limits.html). 