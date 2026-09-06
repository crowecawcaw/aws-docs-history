

# List and describe systems
<a name="next-gen-list-describe-systems"></a>

**To view your systems (console)**

1. Open the Next generation Resilience Hub console.

1. In the navigation pane, choose **Systems**.

1. The systems list shows all systems in your account with their name, number of services, and creation date.

1. To view details for a specific system, choose the system name.

**To list systems (AWS CLI)**
+ Run the following commands:

  ```
  aws resiliencehubv2 list-systems
  
  aws resiliencehubv2 get-system \
    --system-arn "arn:aws:resiliencehub:{{region}}:{{account-id}}:system/{{system-name}}:{{id}}"
  ```