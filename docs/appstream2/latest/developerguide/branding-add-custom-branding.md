# Adding Your Custom Branding to Amazon WorkSpaces Applications

To customize WorkSpaces Applications with your organizational branding, use the WorkSpaces Applications console to
select the stack to customize, and then add your branding.

If you want to choose your organization logo or favicon from your Amazon S3 buckets, make
sure that your Amazon S3 bucket content is not encrypted using keys that you manage
(Customer Managed Keys). Amazon S3 buckets configured to use server-side encryption with
customer-provided encryption keys (SSE-C) are not supported for organization logo and
favicon. If you require encryption at rest for your Amazon S3 objects, server-side encryption
with Amazon S3-managed encryption keys (SSE-S3) is an option for organization logo and
favicon.

###### To add your custom branding to WorkSpaces Applications

1. Open the WorkSpaces Applications console at
   [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
2. In the left pane, choose **Stacks**.
3. In the stack list, select the stack to customize with your branding.
4. Choose **Branding**, **Custom**.
5. For **Application catalog page**, customize how the streaming
   application catalog page appears to users after they sign in to WorkSpaces Applications.
   1. For **Organization logo**, do either of the
      following:
      - Either enter the Amazon S3 URI that represents the organization
        logo, or choose **Browse S3** to navigate to
        your Amazon S3 buckets and find the organization logo.
      - If you already uploaded a organization logo and want to view
        it, choose **View**. You can change it by
        entering another Amazon S3 URI that represents the organization logo,
        or choose **Browse S3** to find another
        organization logo.

   2. For **Organization website links**, specify up to
      three website links to display in the page footer. For each link, choose
      the **Add Link** button, and then enter a display name
      and URL. To add more links, repeat these steps for each link to add. To
      remove a link, choose the **Remove** button under the
      link URL.
   3. For **Color theme**, choose the colors to use for
      your website links, body text, and buttons, and as an accent for the
      page background. For information about each color theme, see [Color Theme Palettes in Amazon WorkSpaces Applications](branding-color-themes.md "branding-color-themes.md") later in this topic.

6. For **Browser tab**, customize the page title and icon to
   display to users at the top of their browser tab during streaming
   sessions.
   1. For **Page title**, enter the title to display at the top
      of the browser tab.
   2. For **Favicon**, do either of the following:
      - Enter the Amazon S3 URI that represents the favicon, or choose
        **Browse S3** to navigate to your Amazon S3
        buckets and find the favicon.
      - If you already uploaded a favicon and want to view it,
        **choose View**. Or, you can change it by
        entering another Amazon S3 URI that represents the favicon, or choose
        **Browse S3** to find another
        favicon.

7. Do either of the following:
   - To apply your branding changes, choose **Save**. When users connect to new streaming sessions that are launched for the stack, your branding changes are displayed.

   ###### Note

   WorkSpaces Applications retains the custom branding changes that you save. If you save your custom branding
   changes, but then choose to restore the WorkSpaces Applications default branding,
   your custom branding changes are saved for later use. If you restore
   the WorkSpaces Applications default branding and decide later to reapply your custom
   branding, choose **Custom**,
   **Save**. In this case, the most recently saved
   custom branding is displayed to your users.
   - To discard your branding changes, choose
     **Cancel**. When prompted to confirm your choice,
     choose **Confirm**. If you cancel your changes, the
     most recently saved branding is displayed to your users.
