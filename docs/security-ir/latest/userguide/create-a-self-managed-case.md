# Create a self-managed case

You can create a self-managed for AWS Security Incident Response through the Console, API, or AWS Command Line Interface.
This type of case _DOES NOT_ engage the AWS Security Incident Response engineers.
The following example covers use of the console.

1. Sign into AWS Security Incident Response via the AWS Management Console at [https://console.aws.amazon.com/security-ir/](https://console.aws.amazon.com "https://console.aws.amazon.com").
2. Choose **Create Case.**
3. Choose **Resolve case with my own
   incident response team.**
4. Set the start date estimate to the date of your earliest
   indicator of the incident. For example, when you experienced
   abnormal behavior for the first time or when you received
   the first related security alert.
5. Define a title for the case.
   It is recommended to include the data into the case title as suggested when
   selecting the **Generate Title** option.
6. Enter AWS account IDs that are part of the case. To add an
   account ID, do the following:
   1. Enter the 12-digit account ID and choose
      **Add account**.
   2. To remove an account, choose
      **Remove** next to the
      account you want to remove from the case.

7. Provide a detailed description of the case. 
   1. Consider the following aspects which can help incident
      responders with the case resolution:
      1. What happened?
      2. Who discovered and reported the incident?
      3. Who is affected by the case?
      4. What is the known impact?
      5. What is the urgency for this case?

8. Add optional case details:
   1. Select the main services that are impacted from the
      drop-down list.
   2. Select the main regions that are impacted from the
      drop-down list.
   3. Add one or many threat actor IP addresses that you
      identified as part of this case.

9. Add optional additional incident responders to the case that
   will receive notifications. To add an individual, do the
   following:
   1. Add an email address.
   2. Add an optional first and last name.
   3. Choose **Add new** to add
      another individual.
   4. To remove an individual, choose
      the **Remove** option for
      an individual.
   5. Choose **Add** to add all listed individuals to the case.
      You can select multiple individuals and choose **Remove**
      to delete them from the list.

10. Add optional tags to the case. To add a tag, do the
    following:
    1. Choose **Add new tag**.
    2. For **Key**, enter the
       name of the tag.
    3. For **Value**, enter the
       value of the tag.
    4. To remove a tag, choose the
       **Remove** option for
       that tag.

The incident response team will be notified by e-mail after the
case is created.
