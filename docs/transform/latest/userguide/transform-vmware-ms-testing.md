

# Step 5: Test
<a name="transform-vmware-ms-testing"></a>

After data replication is complete, you can launch test instances to validate your migrated servers before performing the final cutover. For more information, see [Launch test instances](https://docs.aws.amazon.com/mgn/latest/ug/launch-test-instances.html) in the *MGN User Guide*. AWS Transform supports two testing options:
+ **Full wave testing** – Launch test instances for all servers in the wave.
+ **Selective testing** – Launch test instances for specific servers that you select by providing their user-provided IDs from the inventory file.

AWS Transform launches Amazon EC2 instances from the replicated data and provides the instance IDs so you can connect to and validate the test instances. After testing, you can:
+ Proceed to cutover if testing is successful.
+ Launch new test instances to retest.
+ Terminate test instances and address any issues before retesting.

## Mark applications as ready for cutover
<a name="transform-vmware-ms-mark-ready"></a>

After testing is complete and you are satisfied with the results, mark your applications as ready for cutover. AWS Transform reviews the replication status of each application and resolves any replication alerts before allowing you to proceed. Only applications with a clean replication status can be marked for cutover.