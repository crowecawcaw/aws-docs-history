Amazon Monitron is no longer open to new customers. Existing customers can
continue to use the service as normal. For capabilities similar to Amazon
Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron "https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron").

# Controlling access to projects and sites

To give a user access to all of the resources in a project, including those in all of
the project's sites, you add the user to the project. To give a user access to only the
resources in a site, add the user to the site. Similarly, to make an asset or sensor
available to all of the users who have access to an entire project, add it to the
project. To make an asset or sensor available only to a specific site, add it to only
that site. Gateways are always accessible to anyone or any sensor in the project.

For example: Olga is an admin user associated with the entire project. As a
project-level admin user, she can manage users and resources anywhere within the
project, including those within sites A, B, and C. Sam is an admin user associated with
Site B. As a site-level admin user, he can manage users and resources within Site B but
can't see or manage those within sites A and C. Sensors at Site B can use any gateway
within the project.

Similarly, if Ed is a project-level technician, he can monitor any sensor in the
project. However, Tom, who is a site-level technician for Site C, can see and monitor
only sensors at that site.
