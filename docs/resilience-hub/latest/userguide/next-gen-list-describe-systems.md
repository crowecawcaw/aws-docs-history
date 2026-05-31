# List and describe systems

###### To view your systems (console)

1. Open the Next generation Resilience Hub console.
2. In the navigation pane, choose **Systems**.
3. The systems list shows all systems in your account with their name, number of services,
   and creation date.
4. To view details for a specific system, choose the system name.

###### To list systems (AWS CLI)

- Run the following commands:

```

aws resiliencehubv2 list-systems

aws resiliencehubv2 get-system \
  --system-arn "arn:aws:resiliencehub:`region`:`account-id`:system/`system-name`:`id`"

```
