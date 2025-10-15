# Manage users and groups for farms, queues, and
 fleets

As part of managing users and groups, you can grant access permissions at different levels.
 Each subsequent level includes the permissions for the previous levels. The following list
 describes the four access levels from the lowest level to the highest level:


* **Viewer** â Permission
 to see resources in the farms, queues, fleets, and jobs they have access to. A viewer can't
 submit or make changes to jobs.
* **Contributor** â Same
 as a viewer, but with permission to submit jobs to a queue or farm.
* **Manager** â Same
 as contributor, but with permission to edit jobs in queues they have access to, and grant
 permissions on resources that they have access to.
* **Owner** â Same
 as manager, but can view and create budgets and see usage.
###### Note

Changes to access permissions can take up to 10 minutes to reflect in the system.

1. If you haven't already, sign in to the AWS Management Console and open the Deadline Cloud [console](https://console.aws.amazon.com/deadlinecloud/home "https://console.aws.amazon.com/deadlinecloud/home").
2. In the left navigation pane, choose **Farms and other
 resources**.
3. Select the farm to manage. Choose the farm name to open the details page. You
 can search for the farm using the search bar.
4. To manage a queue or fleet, choose the **Queues** or
 **Fleets** tab, and then choose the queue or fleet to
 manage.
5. Choose the **Access management** tab. By default, the
 **Groups** tab is selected. To manage users, choose
 **Users**.
Depending on the action to take, choose either the **Groups** tab or **Users** tab.


Groups
###### To add groups

1. Select the **Groups** toggle.
2. Choose **Add group**.
3. From the dropdown, select the groups to add.
4. For the group access level, choose one of the following
 options:




	* **Viewer**
	* **Contributor**
	* **Manager**
	* **Owner**
5. Choose **Add**.

###### To remove groups

1. Select the groups to remove.
2. Choose **Remove**.
3. In the confirmation dialog, choose **Remove group**.


Users
###### To add users

1. To add a user, choose **Add user**.
2. From the dropdown, select the users to add.
3. For the user access level, choose one of the following
 options:




	* **Viewer**
	* **Contributor**
	* **Manager**
	* **Owner**
4. Choose **Add**.

###### To remove users

1. Select the user to remove.
2. Choose **Remove**.
3. In the confirmation dialog, choose **Remove user**.
