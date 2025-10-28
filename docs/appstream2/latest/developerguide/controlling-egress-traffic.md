# Controlling egress traffic

Where data loss is a concern, it’s important to cover off what a User can access once they
are inside of their AppStream 2.0 instance. What does the network exit (or egress) path look
like? It is a common requirement to have public internet access available to the end user
inside their AppStream 2.0 instance, so placing a WebProxy or Content Filtering Solution in
the network path needs to be considered. Other considerations include a local Antivirus
application and other endpoint security measures inside the AppStream instance (see the
section “Endpoint Security and Antivirus” for more information).
