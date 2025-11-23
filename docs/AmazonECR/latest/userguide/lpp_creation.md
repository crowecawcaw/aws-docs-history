# Creating a lifecycle policy preview in Amazon ECR

You can use a lifecycle policy preview to see the impact of a lifecycle policy on an
image repository before you apply it. It is considered best practice to do a preview
before applying a lifecycle policy to a repository.

###### Note

If you are using Amazon ECR replication to make copies of a repository across different
Regions or accounts, note that a lifecycle policy can only take an action on
repositories in the Region it was created in. Therefore, if you have replication
turned on you may want to create a lifecycle policy in each Region and account you
are replicating your repositories to.

###### To create a lifecycle policy preview (AWS Management Console)

1. Open the Amazon ECR console at
   [https://console.aws.amazon.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories "https://console.aws.amazon.com/ecr/repositories").
2. From the navigation bar, choose the Region that contains the repository on
   which to perform a lifecycle policy preview.
3. In the navigation pane, under **Private registry**, choose
   **Repositories**.
4. On the **Private repositories** page, select a repository and
   that use the **Actions** drop down to choose
   **Lifecycle policies**.
5. On the lifecycle policy rules page for the repository, choose **Edit
   test rules**, **Create rule**.
6. Specify the following details for each test lifecycle policy rule.
   1. For **Rule priority**, type a number for the rule
      priority. The rule priority determines in what order the lifecycle
      policy rules are applied. A lower number means higher priority. For
      example, a rule with priority 1 takes precedence over a rule with
      priority 2.
   2. For **Rule description**, type a description for the
      lifecycle policy rule.
   3. For **Image status**, choose **Tagged
      (wildcard matching)**, **Tagged (prefix
      matching)**, **Untagged**, or
      **Any**.

   ###### Important

   If you specify multiple tags, only the images with all specified
   tags are selected. 4. If you chose **Tagged (wildcard matching)** for
   **Image status**, then for **Specify tags
   for wildcard matching**, you can specify a list of image
   tags with a wildcard (**\***) on which to take action
   with your lifecycle policy. For example, if your images are tagged as
   `prod`, `prod1`, `prod2`, and so
   on, you would specify `prod*` to take action on all of them.
   If you specify multiple tags, only the images with all specified tags
   are selected.

   ###### Important

   There is a maximum limit of four wildcards (`*`) per
   string. For example, `["*test*1*2*3", "test*1*2*3*"]` is
   valid but `["test*1*2*3*4*5*6"]` is invalid. 5. If you chose **Tagged (prefix matching)** for
   **Image status**, then for **Specify tags
   for prefix matching**, you can specify a list of image tags
   on which to take action with your lifecycle policy. 6. For **Match criteria**, choose **Days since image created**, **Days since last recorded pull time**, **Days since image archived**, or **Image count** and then specify a value. 7. For **Rule action**, choose either **Expire** or **Archive**. 8. Choose **Save**.

7. Create additional test lifecycle policy rules by repeating steps 5–7.
8. To run the lifecycle policy preview, choose **Save and run
   test**.
9. Under **Image matches for test lifecycle rules**, review the
   impact of your lifecycle policy preview.
10. If you are satisfied with the preview results, choose **Apply as
    lifecycle policy** to create a lifecycle policy with the specified
    rules. You should expect that after applying a lifecycle policy, the affected
    images are expired or archived within 24 hours.
11. If you aren't satisfied with the preview results, you may delete one or more
    test lifecycle rules and create one or more rules to replace them and then
    repeat the test.
