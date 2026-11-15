

# Authoring firewall rules
<a name="firewall-rule-groups-authoring"></a>

You author the rules in a firewall rule group in one of two ways. Each create or update request uses exactly one of these authoring modes, and you can switch between them in later requests.
+ **Rule strings** – Raw firewall-mode rules in Suricata compatible syntax. Use this mode if you're comfortable writing Suricata firewall-mode rules directly. In the console, you author rule strings with the **Text rule builder**.
+ **Modeled rules** – A list of structured rule entries. Network Firewall compiles each modeled rule into one Suricata compatible rule string. Use this mode if you prefer a structured form that's easier to generate and manage programmatically. In the console, you author modeled rules with the **Visual rule builder**. For the fields of a modeled rule, see [Fields of a modeled firewall rule](firewall-rule-groups-modeled.md).

The two forms are interchangeable. Network Firewall compiles each modeled rule into exactly one rule string, and when you describe a firewall rule group you can request either the modeled form or the compiled rule-string form. The conversion preserves each rule's behavior, but it isn't byte-for-byte lossless: the protocol normalizes to the hook's protocol family, accept-prior-hooks on a packet-layer hook isn't represented, and a domain-list rule group can be described as modeled rules but can't be written back in that form. If a rule string can't be represented as a modeled rule, the describe request returns an error that identifies the rule by its line number rather than silently changing it.