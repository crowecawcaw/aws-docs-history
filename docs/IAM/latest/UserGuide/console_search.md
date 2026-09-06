

# Using search to find IAM resources
<a name="console_search"></a>

As you work through your access findings, you can use the IAM console search page as a faster option for finding IAM resources. You can search for resources using partial resource names or ARNs.

------
#### [ Console ]

The IAM console search feature can locate any of the following:
+ IAM entity names that match your search keywords (for users, groups, roles, identity providers, and policies)
+ Tasks that match your search keywords

The IAM console search feature does not return information about IAM Access Analyzer.

Every line in the search result is an active link. For example, you can choose the user name in the search result, which takes you to that user's detail page. Or you can choose an action link, for example **Create user**, to go to the **Create User** page.

**Note**  
Access key search requires you to type the full access key ID in the search box. The search result shows the user associated with that key. From there you can navigate directly to that user's page, where you can manage the access key.

Use the **Search** page in the IAM console to find items related to that account. 

**To search for items in the IAM console**

1. Follow the sign-in procedure appropriate to your user type as described in the topic [How to sign in to AWS](https://docs.aws.amazon.com/signin/latest/userguide/how-to-sign-in.html) in the *AWS Sign-In User Guide*.

1. On the **IAM Console Home** page, in the left navigation pane, enter your query in the **Search IAM** text box.

1. In the navigation pane, choose **Search**. 

1. In the **Search** box, type your search keywords.

1. Choose a link in the search results list to navigate to the corresponding part of the console. 

The following icons identify the types of items that are found by a search:



| Icon | Description | 
| --- | --- | 
| ![a portrait outline on gray background.](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/search_user.png) | IAM users | 
| ![multiple portrait outlines on a blue background.](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/search_group.png) | IAM groups | 
| ![a magic wand icon on a navy background.](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/search_role.png) | IAM roles | 
| ![a document icon on an orange background.](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/search_policy.png) | IAM policies | 
| ![a white star on an orange background.](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/search_action.png) | Tasks such as "create user" or "attach policy" | 
| ![a white X on a red background.](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/search_delete.png) | Results from the keyword delete | 

**Sample search phrases**

You can use the following phrases in the IAM search. Replace terms in italics with the names of the actual IAM users, groups, roles, access keys, policies, or identity providers that you want to locate.
+ **{{user\_name}}** or **{{group\_name}} ** or **{{role\_name}}** or **{{policy\_name}}** or **{{identity\_provider\_name}}**
+ **{{access\_key}}**
+ **add user {{user\_name}} to groups** or **add users to group {{group\_name}}**
+ **remove user {{user\_name}} from groups**
+ **delete {{user\_name}}** or **delete {{group\_name}}** or **delete {{role\_name}}**, or **delete {{policy\_name}}**, or **delete {{identity\_provider\_name}}**
+ **manage access keys {{user\_name}}**
+ **manage signing certificates {{user\_name}}**
+ **users**
+ **manage MFA for {{user\_name}}**
+ **manage password for {{user\_name}}**
+ **create role**
+ **password policy**
+ **edit trust policy for role {{role\_name}}**
+ **show policy document for role {{role\_name}}**
+ **attach policy to {{role\_name}}**
+ **create managed policy**
+ **create user**
+ **create group**
+ **attach policy to {{group\_name}}**
+ **attach entities to {{policy\_name}}**
+ **detach entities from {{policy\_name}}**

------