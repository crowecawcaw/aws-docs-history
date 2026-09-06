

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Launching cutover instances
<a name="launch-cutover"></a>

Once you have finalized the testing of all of your source servers, you are ready for cutover. You should perform the cutover at a set date and time. The cutover migrates your source servers to the cutover instances on AWS. 

**Important**  
It is a best practice to perform a test at least two weeks before you plan to migrate your source servers. This time frame allows you to identify potential problems and solve them, before the actual migration takes place. After launching Test instances, use either SSH (Linux) or RDP (Windows) to connect to your instance and ensure that everything is working correctly. 

You can cutover one source server at a time, or simultaneously cutover multiple source servers. For each source server, you are informed of the success or failure of the cutover. For each new cutover, AWS Transform MGN first deletes any previously launched Test instance and dependent resources. Then, it launches a new cutover instance which reflects the most up-to-date state of the source server. After the cutover, data replication continues as before. The new and modified data on the source server is transferred to the staging area subnet, and not to the cutover instances that were launched during the cutover.

**Topics**
+ [Ready for cutover indicators](ready-for-cutover.md)
+ [Starting a cutover](starting-cutover.md)
+ [Reverting a cutover](revert-finalize-cutover.md)
+ [Finalizing a cutover](finalizing-cutover-2.md)