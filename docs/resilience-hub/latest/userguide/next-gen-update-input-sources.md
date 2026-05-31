# Update input sources

To change where the next generation of Resilience Hub looks for resources, add or remove input sources on the
service. See [Add input sources to a service](next-gen-add-input-source.md "next-gen-add-input-source.md") for instructions on adding input
sources.

###### To remove an input source (console)

1. Open the Next generation Resilience Hub console and navigate to your service.
2. Choose the **Configuration** tab.
3. Choose **Edit**.
4. Remove existing input source selections.
5. Choose **Save changes**.

###### To remove an input source (AWS CLI)

- Run the following command:

```

aws resiliencehubv2 delete-input-source \
  --service-arn "`service-arn`" \
  --input-source-id "`input-source-id`"

```
