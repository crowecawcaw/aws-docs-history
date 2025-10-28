# Add project members

In Amazon SageMaker Unified Studio, projects enable a group of users to collaborate on various business use
cases. Within projects, you can manage data assets in the Amazon SageMaker Unified Studio catalog, perform data
analysis, organize workflows, develop machine learning models, build generative AI apps, and
more.

A project member can be a user or a group of users, and a project can have a maximum of 20
members.

There are two different roles that members can have:

- **Contributor**: These members can contribute to the project.
- **Owner**: These members can contribute to the project, add members
  to the project, and remove members of the project. They can also edit the project
  description or delete the project. The person who creates the project has the role of
  Owner by default.
  There are three different kinds of members you can add:

- Single sign-on (SSO) users. An SSO user can sign into Amazon SageMaker Unified Studio using credentials from
  IAM Identity Center or another SSO source.
- SSO groups. You can add groups of users created in IAM Identity Center. An SSO group
  is considered one project member.
- IAM principals (roles or users). An IAM user can sign into Amazon SageMaker Unified Studio with their
  IAM credentials. Note that IAM roles can't access Amazon SageMaker Unified Studio directly and must
  contribute to the project programmatically.
  To add members to an existing project, complete the following steps.

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Choose **Select a project**.
3. If you don't see the name of your project under **Recently updated
   projects**, choose **Browse all projects**.
4. Choose the project that you want to edit. If you don't readily see it in the list of
   projects, you can search for it by specifying the project name in the **Search
   projects** field.
5. On the **Project overview** page, expand **Actions**
   and choose **Manage members**.
6. Choose **Add members**.
7. Enter the name of the user or group you want to add in the search bar, and select the
   name from the list.
8. Select **Contributor** if you want to add the project member as a
   contributor, or choose **Owner** if you want to add the project member as
   a project owner.
9. (Optional) Repeat these steps to add more project members. You can add up to 8 project
   members at a time.
10. Choose **Add members**.
