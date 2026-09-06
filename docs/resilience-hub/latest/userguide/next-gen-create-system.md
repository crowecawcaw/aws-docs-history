

# Create a system
<a name="next-gen-create-system"></a>

**To create a system (console)**

1. Open the Next generation Resilience Hub console at [https://console.aws.amazon.com/resiliencehub/v2/home](https://console.aws.amazon.com/resiliencehub/v2/home).

1. In the navigation pane, choose **Systems**.

1. Choose **Create system**.

1. Provide the following details:
   + **System name** – Enter a descriptive name for your system. The name must be 1–60 characters and can contain letters, numbers, hyphens, and underscores.
   + **Description** – (Optional) Enter a description that helps your team identify the purpose of this system.
   + **Cross-account sharing** – (Optional) Enable this setting if you want services in other AWS accounts to associate with this system.
   + **Encryption** – (Optional) Choose a customer managed AWS KMS key to encrypt system data.
   + **Tags** – (Optional) Add one or more tags to your system.

1. Choose **Create system**.

**To create a system (AWS CLI)**
+ Run the following command:

  ```
  aws resiliencehubv2 create-system \
    --name "{{system-name}}" \
    --description "{{system-description}}"
  ```