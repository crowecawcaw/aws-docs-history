

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Managing users as an admin user
<a name="viewing-users-as-admin"></a>

As an admin, you can use the list of users to manage users in the Amazon Monitron web app. As project level admin, you can view all users at the project level and all users at a particular site level.

The **Users & Permissions** page displays the following information to make user management easier:
+ **Name** – The name of the user. 
+ **Role** – The role assigned to the user, whether Admin, Technician, Viewer, or any combination of these. 
+ **Assigned locations** – The number of locations the user is assigned to.
+ **Project level access** – Whether the user has project level access or only specific site level access.

1. Navigate to the project or site that you want to add a user to or update user permissions from, and then to the **Users & Permissions** list.   
![Users and Permissions page showing a table with 8 users, their roles, assigned locations, and project level access.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/user-10.png)

1. Select **Edit**. Then, from the **Modify user permissions** page, in **Username**, select the user whose details you want to view or edit. Amazon Monitron displays the list of locations the user is assigned to.  
![Username dropdown menu showing User 9 search with list of users and their email addresses.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/user-7.png)

1. To change the role assigned to the user, select between **Admin**, **Technician**, and **Viewer**. Or, you can choose to **Remove** the user. Then, select **Done**.  
![Permission dropdown menu showing Admin selected, with Technician, Viewer, and Remove options.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/user-8.png)

   Amazon Monitron diplays how the user was assigned permissions to all locations. If a user is assigned an **Admin** role at the project level, they inherit access to all locations within that project. In this case, Amazon Monitron indicates their access level as **Admin – inherited**.  
![Modify user permissions page showing Project name with Admin role and inherited permissions for sites.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/user-9.png)