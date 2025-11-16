# Transferring Chrome policies

In case you already have Chrome policies set up to allow or block specific domains, we recommend that you transfer them to the Web Content Filtering feature.

The Web Content Filtering feature will detect any URLAllow or URLBlock policies that apply to a WorkSpaces Secure Browser session and will signal it in the AWS Console.

To transfer the Chrome policies for URLAllowlist and / or URLBlocklist:

- In your AWS Console, under URL Filtering, click **Review Chrome Policies** (if you do not see the Review Chrome Policies button, this means not Chrome policies currently applies for URL Allow or URLBlock)
- Under the overlay, review the Chrome policies
- Click **Transfer**
  The Chrome policies will be removed from the JSON Editor under Policy Settings and new URLs will be automatically added to the Web Content Filtering feature.
