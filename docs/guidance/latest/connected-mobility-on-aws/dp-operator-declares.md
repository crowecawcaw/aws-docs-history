

# The operator declares the catalog
<a name="dp-operator-declares"></a>

This platform is a third-party fleet platform. It has no knowledge of any particular producer’s portal, and does not assume one exists. So a fleet operator declares, inside the platform, every data product they intend to consume — producer identity, connection endpoint, authentication method, credentials pointer, tier, and transform manifest.

That is the load-bearing decision of the whole definition layer. The alternative — discovering products by calling a producer’s catalog API — would be less configuration to type and would make the platform a captive client of one producer’s portal. Operator-declared configuration keeps it generic across producers who have no portal at all.

The consequence is worth stating rather than papering over: **the catalog can drift from what the producer actually offers, and nothing reconciles the two.** Treat the catalog as the operator’s declaration of intent, not as a mirror of the producer’s inventory.