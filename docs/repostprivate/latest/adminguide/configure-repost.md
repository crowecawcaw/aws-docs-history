

End of support notice: On June 30, 2027, AWS will end support for AWS re:Post Private. After June 30, 2027, you will no longer be able to access the re:Post Private console or re:Post Private resources. For more information, see [AWS re:Post Private end of support](https://docs.aws.amazon.com/repostprivate/latest/userguide/repost-private-end-of-support.html). 

# Configure your private re:Post
<a name="configure-repost"></a>

When you use your IAM Identity Center credentials to sign in to your private re:Post application for the first time, choose **Start setting up** on the **Welcome to your private re:Post** page. This section explains how you can configure your new private re:Post.

**Topics**
+ [Customize appearance for your private re:Post](#customize-appearance)
+ [Add custom tags, custom topics, and blocked terminology for your private re:Post](#add-tags-topics-blocked-terminology)
+ [Choose your topics of interest for selections](#add-selections-topics)

## Customize appearance for your private re:Post
<a name="customize-appearance"></a>

Follow these steps to customize appearance for your private re:Post:

1. On the **Customize appearance** page, for **Title**, enter a title for your private re:Post. This is the title that shows at the top of your private re:Post home page.

1. For **Description**, enter a welcome message to greet your re:Post Private users. When a user signs in to your private re:Post, this message is displayed on the re:Post Private home page.

1. Under **Logo**, choose **Change logo**, and then upload an image. The maximum size for this image is 2 MiB. The supported file types are .jpg, .peg, and .png. This logo appears on the top-left of your private re:Post and has a resolution of 150 X 50.

1. Under **Color scheme**, for **Primary color** and **Button color**, choose the colors. The primary color that you choose is used as the header color for your private re:Post. The button color that you choose is used as the color for the buttons within your private re:Post.

1. Choose **Save and continue**.

## Add custom tags, custom topics, and blocked terminology for your private re:Post
<a name="add-tags-topics-blocked-terminology"></a>

As an administrator for your private re:Post, you can add custom tags, custom topics, and blocked terminology for your private re:Post.

To add custom tags that apply to your private re:Post, follow these steps:

1. On the **Add custom tags, topics and blocked terminology** page, choose **Tags**, and then choose **Create tag**.

1. In the **Create tag?** dialog box, enter the tag. Then, choose **Create**.
**Note**  
You can't start the tags with `AWS` or `Amazon`.
You can't enter duplicate tags.

   The tags that you added are displayed in the list under the **Tags** section. The users of your private re:Post can add these custom tags in questions, articles, and selections that they post in the private re:Post.

To add custom topics to your private re:Post, follow these steps:

1. On the **Add custom tags, topics and blocked terminology** page, choose **Topics**, and then choose **Create topic**.

1. In the **Create new topic** dialog box, do the following:

   For **Name**, enter a name for the custom topic.
**Note**  
You can't start the topics with `AWS` or `Amazon`.
You can't enter duplicate topics.

   For **Brief description**, enter a description for your topic.

   For **Full description**, enter a detailed description for your topic.

   For **Included tags**, select all tags that you want to include in this topic. You can only choose custom tags to include in a custom topic.

   Choose **Create**.

The topics that you added are displayed in the list under the **Topics** section. If a user posts a question, article, or selection with the tag that you included in the custom topic, then your private re:Post adds the topic to this content.

To add blocked terminology to your private re:Post, follow these steps:

1. Choose **Blocked terminology**. Then, choose **Add blocked terminology**.

1. In the **Add blocked terminology?** dialog box, enter the text that you want to block your private re:Post users from using. Then, choose **Add**.

   The terms that you added are displayed in the list under the **Blocked terminology** section. When users try to use the blocked term in their private re:Post content, they get a warning message that asks them to edit the content and remove the term.

1. Choose **Continue**.

## Choose your topics of interest for selections
<a name="add-selections-topics"></a>

A selection is a learning path or a curated set of content assets that are relevant to a use case, technology domain, industry, or specific problem area. It's a collection of knowledge assets specific to your organization's cloud use case within AWS services and contains high-quality content from AWS sources, such as AWS re:Post, Knowledge Center, AWS Blogs, and AWS Documentation.

To choose your topics of interest for selections, follow these steps:

1. On the **Select topics of interest** page, select your topics of interest for selections that you want to display on the home page of your private re:Post.

   You can also use the dropdown list to select topics of your interest.

1. Choose **Launch your private re:Post**.

All selections with the selected topics are added to the home page for your private re:Post.

**Important**  
Your private re:Post is launched and ready for use after the console administrator onboards users to it. For more information, see [Invite users and groups to your private re:Post](https://docs.aws.amazon.com/repostprivate/latest/caguide/invite-users.html). The users of your private re:Post use the information in the onboarding email to sign in to your private re:Post after it's launched.