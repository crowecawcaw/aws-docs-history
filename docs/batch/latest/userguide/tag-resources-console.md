

# Tutorial: Manage tags using the console
<a name="tag-resources-console"></a>

Using the AWS Batch console, you can manage the tags associated with new or existing compute environments, jobs, job definitions, and job queues.

## Add tags on an individual resource on creation
<a name="adding-tags-creation"></a>

You can add tags to AWS Batch compute environments, jobs, job definitions, job queues, and scheduling policies when you create them.

## Add and delete tags on an individual resource
<a name="adding-or-deleting-tags"></a>

AWS Batch allows you to add or delete tags associated with your clusters directly from the resource's page. 

**To add or delete a tag on an individual resource**

1.  Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/).

1. From the navigation bar, choose the Region to use.

1. In the navigation pane, choose a resource type (for example, **Job Queues**).

1. Choose a specific resource, then choose **Edit tags**.

1. Add or delete your tags as necessary.
   + To add a tag — specify the key and value in the empty text boxes at the end of the list.
   + To delete a tag — choose the ![Delete icon](http://docs.aws.amazon.com/batch/latest/userguide/images/DeleteIcon.png) button next to the tag.

1. Repeat this process for each tag you want to add or delete, and then choose **Edit tags** to finish.