# Creating a lifecycle policy for a repository in

Amazon ECR

Use a lifecycle policy to create a set of rules that expire or archive unused repository images.
After creating a lifecycle policy, the affected images are expired or archived within 24
hours.

###### Note

If you are using Amazon ECR replication to make copies of a repository across different
Regions or accounts, note that a lifecycle policy can only take an action on
repositories in the Region it was created in. Therefore, if you have replication
turned on you may want to create a lifecycle policy in each Region and account you
are replicating your repositories to.

## Prerequisite

**Best practice:** Create a lifecycle policy preview to
verify that the images expired or archived by your lifecycle policy rules are what you intend. For
instructions, see [Creating a lifecycle policy preview in Amazon ECR](lpp_creation.md "lpp_creation.md").

1. Open the Amazon ECR console at
   [https://console.aws.amazon.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories "https://console.aws.amazon.com/ecr/repositories").
2. From the navigation bar, choose the Region that contains the
   repository for which to create a lifecycle policy.
3. In the navigation pane, under **Private registry**,
   choose **Repositories**.
4. On the **Private repositories** page, select a
   repository and that use the **Actions** drop down to
   choose **Lifecycle policies**.
5. On the lifecycle policy rules page for the repository, choose
   **Create rule**.
6. Enter the following details for your lifecycle policy rule.
   1. For **Rule priority**, type a number for the
      rule priority. The rule priority determines in what order the
      lifecycle policy rules are applied. A lower rule priority number
      means higher priority. For example, a rule with priority 1 takes
      precedence over a rule with priority 2.
   2. For **Rule description**, type a description
      for the lifecycle policy rule.
   3. For **Image status**, choose **Tagged
      (wildcard matching)**, **Tagged (prefix
      matching)**, **Untagged**, or
      **Any**.

   ###### Important

   If you specify multiple tags, only the images with all specified
   tags are selected. 4. If you chose **Tagged (wildcard matching)**
   for **Image status**, then for
   **Specify tags for wildcard matching**, you
   can specify a list of image tags with a wildcard
   (**\***) on which to take action with your
   lifecycle policy. For example, if your images are tagged as
   `prod`, `prod1`, `prod2`,
   and so on, you would specify `prod*` to take action
   on all of them. If you specify multiple tags, only the images
   with all specified tags are selected.

   ###### Important

   There is a maximum limit of four wildcards
   (`*`) per string. For example,
   `["*test*1*2*3", "test*1*2*3*"]` is valid but
   `["test*1*2*3*4*5*6"]` is invalid. 5. If you chose **Tagged (prefix matching)**for
   **Image status**, then for
   **Specify tags for prefix matching**, you
   can specify a list of image tags on which to take action with
   your lifecycle policy. 6. For **Match criteria**, choose **Days since image created**, **Days since last recorded pull time**, **Days since image archived**, or **Image count** and then specify a value. 7. For **Rule action**, choose either **Expire** or **Archive**. 8. Choose **Save**.

7. Create additional lifecycle policy rules by repeating steps
   5–7.
8. Obtain the name of the repository for which to create the lifecycle
   policy.

```
`aws ecr describe-repositories`
```

2. Create a local file named `policy.json` with the contents
   of the lifecycle policy. For lifecycle policy examples, see [Examples of lifecycle policies in
   Amazon ECR](lifecycle_policy_examples.md "lifecycle_policy_examples.md").
3. Create a lifecycle policy by specifying the repository name and
   reference the lifecycle policy JSON file you created.

```
`aws ecr put-lifecycle-policy \
 --repository-name `repository-name` \
 --lifecycle-policy-text file://`policy.json``
```
