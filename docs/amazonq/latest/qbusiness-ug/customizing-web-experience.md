# Customizing an Amazon Q Business web experience

Creating an Amazon Q Business application environment automatically creates a web experience
with a shareable URL. Amazon Q offers customization options for your web
experience, allowing you to align the interface with your organization's branding and user
needs. This guide will walk you through the process of customizing text elements, visual
themes, and some accessibility features, helping you create a more suited experience for
your users.

###### Note

As of Oct 31, 2024, once you have created a new Amazon Q Business
application environment, the default web experience will allow users to interact directly with the
LLM to get answers from its general knowledge or uploaded file content, even if the Admin has not yet connected any enterprise data sources.

For existing application environments, the _Allow direct access to LLM_
setting will remain as previously configured. For new application environments, the
_Allow direct access to LLM_ setting will be enabled by default,
though Admins can still disable this if desired.

You can customize a web experience by using either the AWS Management Console or the Amazon Q API. These customizations persist even in _Amazon Q
embedded_. You can perform these customizations using either the AWS Management Console or
the Amazon Q API (available via the AWS SDK, REST API, and AWS CLI).

If you use the API, customizing your Amazon Q Business can involve a combination of
the following API operations.

- [CreateApplication](../api-reference/API_CreateApplication.md "../api-reference/API_CreateApplication.md") – Creates
  an Amazon Q application environment.
- [CreateWebExperience](../api-reference/API_CreateWebExperience.md "../api-reference/API_CreateWebExperience.md") – Creates
  an Amazon Q web experience.
- [GetWebExperience](../api-reference/API_GetWebExperience.md "../api-reference/API_GetWebExperience.md") – Gets the
  properties of the web experience that you set up.
- [UpdateWebExperience](../api-reference/API_UpdateWebExperience.md "../api-reference/API_UpdateWebExperience.md") – Updates
  the properties of an existing Amazon Q web experience.
- [ListWebExperiences](../api-reference/API_ListWebExperiences.md "../api-reference/API_ListWebExperiences.md") – Lists
  Amazon Q web experiences.

###### Topics

- [Customization overview](#customization-web-experience-iam-overview "#customization-web-experience-iam-overview")
- [Customizing text elements](customizing-web-experience-text-elements.md "customizing-web-experience-text-elements.md")
- [Customizing visual themes](customizing-web-experience-themes.md "customizing-web-experience-themes.md")
- [Reference materials for customizing the visual theme](customizing-web-experience-themes-reference-materials.md "customizing-web-experience-themes-reference-materials.md")

## Customization overview

Creating an Amazon Q Business application environment automatically generates a
web experience with a shareable URL. Before sharing this URL, you can customize various
elements:

- Title and subtitle
- Welcome message
- Sample prompts
- Logo and favicon
- Colors and fonts
