

# Tag a dataset

A tag is a label that you assign to an AWS resource. Each tag has a key and an optional value. Tags on a dataset are ordinary AWS tags with your own keys, and an IAM condition matches on them, so tagging is how you scope access to a particular dataset without naming its ARN.

1. On the **Data Hub** page, choose the dataset name.

1. On the **Tags** card, choose **Manage tags**. Manage tags opens the same page that **Edit** opens, with the tags in view.

1. Choose **Add new tag**, then enter a key and an optional value.

1. Choose **Save changes**.

**Note**  
You can add tags when you create the dataset and change them afterwards. The `aws:` prefix is reserved, so a request with a key that starts with aws: fails, and a create request with such a key creates no dataset. A tag key holds 1 to 128 characters, a value up to 256, and a dataset carries up to 50 tags.