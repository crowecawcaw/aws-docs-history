

# Exclude organizational units from IPAM
<a name="exclude-ous"></a>

If your IPAM is integrated with AWS Organizations, you can exclude an [organizational unit (OU)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#organizationalunit) from being managed by IPAM. When you exclude an OU, IPAM will not manage the IP addresses in accounts in that OU. This feature gives you more flexibility in how you use IPAM.

You can use OU exclusions in the following ways:
+ **Enable IPAM for specific parts of your business**: If you have multiple business units or subsidiaries in AWS Organizations, you can now use IPAM just for the ones that need it.
+ **Keep your sandbox accounts separate**: You can exclude your sandbox accounts from IPAM, focusing only on the accounts that really matter for your IP management.

## How OU exclusions work
<a name="exclude-ous-how-it-works"></a>

The diagrams in this section demonstrate two use cases for adding OU exclusions in IPAM.

The first diagram shows the impact of adding an organization unit (OU) exclusion on a parent OU only. As a result, IPAM will not manage the IP addresses in accounts in the parent OU. IPAM will manage the IP addresses in accounts in the other OUs outside the exclusion.

![Diagram of OU exclusion on parent OU.](http://docs.aws.amazon.com/vpc/latest/ipam/images/ipam-ou-1.png)


The second diagram shows the impact of adding an organization unit (OU) exclusion on a parent OU *and* all child OUs. As a result, IPAM will not manage the IP addresses in accounts in the parent OU or in accounts in any child OUs. IPAM will manage the IP addresses in accounts in the OUs outside of the exclusion.

![Diagram of OU exclusion on parent OU and all child OUs.](http://docs.aws.amazon.com/vpc/latest/ipam/images/ipam-ou-2.png)


## Add or remove OU exclusions
<a name="exclude-ous-create-delete"></a>

Complete the steps in this section to add or remove OU exclusions.

**Note**  
The delegated IPAM admin account is not excluded even if it's within an OU that's excluded.
Your IPAM must be integrated with AWS Organizations to add an OU exclusion. The Organization must have OUs in it.
You must be the delegated IPAM admin to view, add, or remove OU exclusions.
It takes time for IPAM to discover recently created organizational units.
There is a default quota for the number of exclusions you can add per resource discovery. For more information, see *Organizational unit exclusions per resource discovery* in [Quotas for your IPAM](quotas-ipam.md).
If you [share a resource discovery with another account](res-disc-work-with-share.md), that account can see the OU exclusions on it, which contains information such as the Org ID, Root ID, and organizational unit IDs of the resource discovery owner's Organization.

------
#### [ AWS Management Console ]

**To add or remove OU exclusions**

1. Open the IPAM console at [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/). 

1. In the navigation pane, choose **Resource discoveries**.

1. Choose your default resource discovery.

1. Choose **Edit**.

1. Under **Organizational unit exclusions**, do the following:
   + **To add an OU exclusion**:
     + If you want to exclude the OU and all its child OUs: 
       + Find the OU in the table and select the checkbox. All child OUs are automatically selected.
     + If you want to exclude only parent OU accounts: 
       + Find the OU in the table and select the checkbox. All child OUs are automatically selected. Deselect all child OUs.
     + Alternatively, you can use the **Actions **column to select only a parent OU or parent and child OUs:
       + **Select all child OUs**: Include any child OUs in the exclusion. As a result of choosing an OU, the OU is added on screen. Each OU contains the ID and the [entity path](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed-view-data-orgs.html#access_policies_last-accessed-viewing-orgs-entity-path) of the OU exclusion.
       + **Select only this OU**: Include only this OU in the exclusion. As a result of choosing an OU, the OU is added on screen. Each OU contains the ID and the [entity path](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed-view-data-orgs.html#access_policies_last-accessed-viewing-orgs-entity-path) of the OU exclusion.
       + **Copy OU entity path**: Copy the organization entity path to use as needed.
     + If you know the AWS Organizations entity path already or you want to build it:
       + Choose **Input organizational unit exclusion** and enter the [entity path](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed-view-data-orgs.html#access_policies_last-accessed-viewing-orgs-entity-path) of the OU exclusion. Build the path for the OU(s) using AWS Organizations IDs separated by a `/`. Include all child OUs by ending the path with `/*`.
         + Example 1
           + Path to a child OU: `o-a1b2c3d4e5/r-f6g7h8i9j0example/ou-ghi0-awsccccc/ou-jkl0-awsddddd/`
           + In this example, `o-a1b2c3d4e5` is the organization ID, `r-f6g7h8i9j0example` is the root ID, `ou-ghi0-awsccccc` is an OU ID, and `ou-jkl0-awsddddd` is a child OU ID.
           + IPAM will not manage the IP addresses in accounts in the child OU.
         + Example 2
           + Path where all child OUs will be part of the exclusion: `o-a1b2c3d4e5/r-f6g7h8i9j0example/ou-ghi0-awsccccc/*`
           + In this example, IPAM will not manage the IP addresses in accounts in the OU (`ou-ghi0-awsccccc`) or in accounts in any OUs that are children of the OU.
   + **To remove an OU exclusion**: 
     + Choose the **X** next to an OU that's already been added. The `/*` after the OU ID indicates that it's a parent OU and that child OUs are part of the OU exclusion.

1. Choose **Save changes**.

------
#### [ Command line ]

The commands in this section link to the *AWS CLI Command Reference*. The documentation provides detailed descriptions of the options that you can use when you run the commands.

1. View resource discovery details to get the ID of the default resource discovery for the next step with [describe-ipam-resource-discoveries](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-ipam-resource-discoveries.html).

   Input:

   ```
   aws ec2 describe-ipam-resource-discoveries
   ```

   Output:

   ```
   {                                                                                                                              
       "IpamResourceDiscoveries": [                                                                                               
           {                                                                                                                      
               "OwnerId": "111122223333",                                                                                         
               "IpamResourceDiscoveryId": "ipam-res-disco-1234567890abcdef0",                                                     
               "IpamResourceDiscoveryArn": "arn:aws:ec2::111122223333:ipam-resource-discovery/ipam-res-disco-1234567890abcdef0",  
               "IpamResourceDiscoveryRegion": "us-east-1",                                                                        
               "OperatingRegions": [                                                                                              
                   {                                                                                                              
                       "RegionName": "us-east-1"                                                                                  
                   },                                                                                                             
                   {                                                                                                              
                       "RegionName": "us-west-1"                                                                                  
                   },                                                                                                             
                   {                                                                                                              
                       "RegionName": "us-west-2"                                                                                  
                   }                                                                                                              
               ],                                                                                                                 
               "IsDefault": true,                                                                                                 
               "State": "modify-complete",                                                                                        
               "Tags": []                                                                                                         
           }                                                                                                                      
       ]                                                                                                                          
   }
   ```

1. Add or remove an organizational unit exclusion from a resource discovery with [modify-ipam-resource-discovery](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-ipam-resource-discovery.html) and the `--add-organizational-unit-exclusions` or `--remove-organizational-unit-exclusions` options. You'll need enter an AWS Organizations entity path. Build the path for the OU(s) using AWS Organizations IDs separated by a `/`. Include all child OUs by ending the path with `/*`. You can't include the same entity path more than once in the add or remove parameters.
   + Example 1
     + Path to a child OU: `o-a1b2c3d4e5/r-f6g7h8i9j0example/ou-ghi0-awsccccc/ou-jkl0-awsddddd/`
     + In this example, `o-a1b2c3d4e5` is the organization ID, `r-f6g7h8i9j0example` is the root ID, `ou-ghi0-awsccccc` is an OU ID, and `ou-jkl0-awsddddd` is a child OU ID.
     + IPAM will not manage the IP addresses in accounts in the child OU.
   + Example 2
     + Path where all child OUs will be part of the exclusion: `o-a1b2c3d4e5/r-f6g7h8i9j0example/ou-ghi0-awsccccc/*`
     + In this example, IPAM will not manage the IP addresses in accounts in the OU (`ou-ghi0-awsccccc`) or in accounts in any OUs that are children of the OU.
**Note**  
The resulting set of exclusions must not "overlap", meaning two or more OU exclusions must not exclude the same OU.  
**Example of non-overlapping entity paths:**  
Path 1 ="o-1/r-1/ou-1/"
Path 2 ="o-1/r-1/ou-1/ou-2/"
These paths are do not overlap because Path 1 only excludes the accounts under ou-1 and Path 2 only excludes accounts under ou-2.  
**Example of overlapping entity paths:**  
Path 1 ="o-1/r-1/ou-1/\*"
Path 2 ="o-1/r-1/ou-1/ou-2/"
These paths overlap because Path 1 represents both "o-1/r-1/ou-1/" and "o-1/r-1/ou-1/ou-2/", and "o-1/r-1/ou-1/ou-2/" overlaps with Path 2.

   Input:

   ```
   aws ec2 modify-ipam-resource-discovery \
       --ipam-resource-discovery-id ipam-res-disco-1234567890abcdef0 \
       --add-organizational-unit-exclusions OrganizationsEntityPath='o-a1b2c3d4e5/r-f6g7h8i9j0example/ou-ghi0-awsccccc/*' \
       --remove-organizational-unit-exclusions OrganizationsEntityPath='o-a1b2c3d4e5/r-f6g7h8i9j0example/ou-ghi0-awsccccc/ou-jkl0-awsddddd/' \
       --region us-east-1
   ```

   Output:

   ```
   {
       "IpamResourceDiscovery": {
           "OwnerId": "111122223333",
           "IpamResourceDiscoveryId": "ipam-res-disco-1234567890abcdef0",
           "IpamResourceDiscoveryArn": "arn:aws:ec2::111122223333:ipam-resource-discovery/ipam-res-disco-1234567890abcdef0",
           "IpamResourceDiscoveryRegion": "us-east-1",
           "OperatingRegions": [
               {
                   "RegionName": "us-east-1"
               }
           ],
           "IsDefault": false,
           "State": "modify-in-progress",
           "OrganizationalUnitExclusions": [
               {
                   "OrganizationsEntityPath": "o-a1b2c3d4e5/r-f6g7h8i9j0example/ou-ghi0-awsccccc/*"
               }
           ]
       }
   }
   ```

------