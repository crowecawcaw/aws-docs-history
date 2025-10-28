# Address Lists

Address Lists is a Mail Manager feature that allows you to create and manage lists of email addresses
and domains that you can use in traffic policies and rule sets to process incoming mail
based on whether or not the recipient or sender of a message belongs to a specific list.
Address Lists lends themselves to more granular control over email flows and help to simplify
management of complex email routing scenarios.

## What are Address Lists?

Address Lists are containers for email addresses and domains that you can use to filter
and process email messages. They provide a convenient way to group related addresses and
apply routing rules and traffic policies collectively.

Key use cases for Address Lists include:

- Deny lists for blocking known spam senders or domains
- Allow lists for ensuring delivery from trusted senders
- Recipient validation to reject emails to non-existent recipients early
- Role-based routing for applying different rules based on recipient
  roles
- Group-based policies for enforcing policies for specific user groups

## How Address Lists work

Address Lists in SES streamline email management by allowing you to create and
maintain collections of email addresses and domains.
Once created, these lists are integrated into
your email workflows through traffic policies and rules.

When SES processes an email, it checks the relevant Address List to determine if
the sender or recipient is a member. Based on this membership and your configured
policies and rules, SES then takes appropriate actions, such as routing,
filtering, or rejecting the email. This process enables efficient and granular control
over your email traffic.

## Setting up Address Lists

###### Topics

- [Creating and populating an
  Address List](#creating-address-lists "#creating-address-lists")
- [Managing Address Lists](#managing-address-lists "#managing-address-lists")

### Creating and populating an

Address List

Part of creating an Address List in the console is to populate it with one or more
addresses. Using the Mail Manager APIs, you can create empty Address Lists and populate them
later. This section will show you how to do either with both console procedures and
AWS CLI examples.

###### To create and populate an Address List:

1. Open the SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. In the navigation pane under Mail Manager, choose
   **Address Lists**.
3. Choose **Create address list** and enter a name in the
   **Address list name** field.
4. Select either **Manual entry** or **Bulk
   upload** and follow the respective steps:
5. **For manual entry** – Enter one or
   more email addresses or domains in the console.

If you use the asterisk (`*`) wildcard, the following formats
apply:

    1. Only one `*` is allowed in the address:




    	* The `*` should be either before or after @ when
    	 the entry is an email address.
    	* When `*` is in the local part, the local part
    	 can be zero or 3 to 19 characters excluding the
    	 `*`.
    	* When `*` is in the domain, the subdomain level
    	 can be 2 to 9 excluding the `*`.
    2. Examples of valid wildcard formats:




    	* *\*.domain1.com to
    	 \*.domain8.domain7...domain1.com*
    	* *\*@domain.com*
    	* *123\*@domain.com to
    	 1234567890123456789\*@domain.com*
    	* *local@\*.domain1.com to
    	 local@\*.domain8.domain7...domain1.com*

6. **For bulk upload** – Select
   **Choose file** and choose a CSV or JSON file from your
   computer containing the addresses to be uploaded.

Use the format shown in the example for each file type:

    1. CSV file example (Note that the header, `address`, is
     required.):



    ```
    address
    `user1@domain.com`
    `user2@*.domain.com`
    `*@domain.com`
    ```
    2. JSON file example:



    ```
    {
      "items": [
        {
          "address": "`user1@domain.com`"
        },
        {
          "address": "`user2@*.domain.com`"
        },
        {
          "address": "`*@domain.com`"
        }
      ]
    }
    ```

7. Once you've finished adding addresses or have selected a bulk file, choose
   **Create address list**.

Using the AWS CLI:

**Create the Address List**

```
aws mailmanager create-address-list --address-list-name "`MyDenyList`"
```

**Populate the Address List:**

- **Single upload**

```
aws mailmanager register-member-to-address-list \
                --address-list-id `al-123456789abc` \
                --address "`user@example.com`"
```

- **Bulk upload**

For bulk uploads, you first have to create an import job specifying either
a CSV or JSON format:

```
aws mailmanager create-address-list-import-job \
                --address-list-id "`al-123456789abc`" \
                --name "`MyImportJob`" \
                --import-data-format ImportDataType=CSV
```

This returns a job ID and a pre-signed URL. Use this pre-signed URL to
upload your CSV or JSON file to an S3 bucket as shown in the
following example using the curl command:

```
curl -X PUT -T "`/path/to/file`" "`pre-signed URL`"
```

After uploading, start the import job using the job ID returned in the
previous command:

```
aws mailmanager start-address-list-import-job --job-id "`job-123456789`"
```

### Managing Address Lists

You can update, view, and delete address lists as needed.

###### Topics

- [Updating an Address List](#updating-address-lists "#updating-address-lists")
- [Viewing Address List details](#viewing-address-lists "#viewing-address-lists")
- [Deleting an Address List](#deleting-address-lists "#deleting-address-lists")

#### Updating an Address List

You can update an address list by adding or removing addresses, and
optionally, adding or removing tags.

###### To update an Address List:

1. On the **Address Lists** page, select the name of the
   Address List you want to edit.
2. To add addresses, choose **Add email address** and
   proceed with either the manual entry or bulk upload method as explained
   in [Creating & populating an
   Address List](#creating-address-lists "#creating-address-lists").
3. To remove addresses, select the checkbox next to each address you want
   to remove followed by **Remove email address** and
   confirm deletion.
4. (Optional) Add or remove **Tags** to your Address List
   by choosing **Manage tags**.

Using the AWS CLI:

**Add**

```
aws mailmanager register-member-to-address-list \
                --address-list-id `al-123456789abc` \
                --address "`user@example.com`"
```

**Remove**

```
aws mailmanager deregister-member-from-address-list \
                --address-list-id `al-123456789abc` \
                --address "`user@example.com`"
```

#### Viewing Address List details

To view Address List details:

- On the **Address Lists** page, select the name of an
  Address List to view its details.

Using the AWS CLI:

```
aws mailmanager list-members-of-address-list --address-list-id `al-123456789abc`
```

#### Deleting an Address List

To delete an Address List:

1. On the **Address Lists** page, select the radio button
   next to the Address List you want to delete followed by
   **Delete**.
2. Confirm deletion of the list by typing _confirm_
   followed by **Delete**.

Using the AWS CLI:

```
aws mailmanager delete-address-list --address-list-id `al-123456789abc`
```

## Using Address Lists

in Traffic Policies and Rule Sets

Address Lists can be used in traffic policy statements and rule conditions to process
emails based on list membership giving control over email flow. The following sections
provide an example of Address Lists being used in each a traffic policy and a rule
set.

###### Topics

- [Traffic policy example](#traffic-policy-example "#traffic-policy-example")
- [Rule set example](#rule-set-example "#rule-set-example")

### Using an Address List in a traffic policy

statement

Address Lists can be selected when you build the condition of a traffic policy
statement to either allow or deny email coming into your ingress endpoint.

The following console procedure and its AWS CLI equivalent are showing an example of
creating a policy statement that allows messages into your ingress endpoint if the
recipient is in the specified Address List.

###### To use an Address List in a traffic policy statement:

1. Create a new traffic policy or edit an existing one as explained in [Creating traffic policies &
   policy statements (console)](eb-filters.md#eb-filters-create-console "eb-filters.md#eb-filters-create-console")
2. In the **Policy statement** container, choose
   **Allow** for the action to be taken when the
   statement's conditions are met.
3. Build the statement's condition as follows:
   - Select **Recipient address** for the
     **Protocol** field.
   - Select **Is in address list** for the
     **Operator** field.
   - Select the name of your Address List for the
     **Value** field.

4. While this is just one example, you can add more policy conditions that
   can be based on a variety of operators with any of your Address Lists.

Using the AWS CLI:

```
aws mailmanager create-traffic-policy \
  --default-action ALLOW \
  --traffic-policy-name "`testpolicy`" \
  --policy-statements '[{
    "Action": "ALLOW",
    "Conditions": [{
      "BooleanExpression": {
        "Evaluate": {
          "IsInAddressList": {
            "Attribute": "RECIPIENT",
            "AddressLists": [
              "arn:aws:ses:`eu-west-3`:`123456789012`:mailmanager-address-list/`al-123456789abc`"
            ]
          }
        },
        "Operator": "IS_TRUE"
      }
  }]
}]'
```

### Using an Address List in a rule

Address Lists can be selected when you build the condition of a rule used in one of
your rule sets to trigger the rule's action.

The following console procedure and its AWS CLI equivalent are showing an example of
creating a rule that invokes the drop action if the recipient is in the specified
Address List.

###### To use an Address List in a rule condition:

1. Create a new rule or edit an existing one as explained in [Creating rule sets & rules
   (console)](eb-rules.md#eb-rules-create-console "eb-rules.md#eb-rules-create-console")
2. In the **Rule conditions** container, build the rule's
   condition as follows.
   - Select **Recipient address** for the
     **Select property** field.
   - Select **Is in address list** for the
     **Select operator** field.
   - Select the name of your Address List for the
     **Value** field.

3. In the **Actions** container choose **Add new
   action** and select **Drop action**.
4. While this is just one example, you can add more rule conditions that can
   be based on a variety of operators with any of your Address Lists for a variety
   of actions to be taken.

Using the AWS CLI:

```
aws mailmanager create-rule-set \
  --rule-set-name "`testruleset2`" \
  --rules '[{
    "Name": "addresslist",
    "Conditions": [{
      "BooleanExpression": {
        "Evaluate": {
          "IsInAddressList": {
            "Attribute": "RECIPIENT",
            "AddressLists": [
              "arn:aws:ses:`us-east-1`:`123456789012`:mailmanager-address-list/`al-123456789abc`"
            ]
          }
        },
        "Operator": "IS_TRUE"
      }
    }],
    "Actions": [{
      "Drop": {}
    }]
  }]'

```

## Best Practices and

Considerations

- Be mindful of list sizes—very large lists may impact
  performance.
- Address Lists are account-specific and can only be used within the same AWS
  account.
- Nested Address Lists are not currently supported.
- A maximum of 100 Address Lists per region is supported.
- A maximum of 100,000 addresses per Address List is supported.
