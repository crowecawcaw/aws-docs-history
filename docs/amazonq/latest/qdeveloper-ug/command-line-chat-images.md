# Working with images

Amazon Q can analyze and discuss images directly in your chat session. You can share images with Amazon Q by dragging and dropping them into your terminal window or by using the `fs_read` tool with the Image mode.

## Drag and drop images

The simplest way to share images with Amazon Q is to drag and drop them directly into your terminal window. When you drag an image into the terminal:

1. The image path is automatically inserted into your prompt
2. You can then add text to provide context about what you want Amazon Q to do with the image
3. Amazon Q will process the image and respond based on its content

Example:

```
Amazon Q> /path/to/architecture-diagram.png Can you explain this architecture and generate sample code for implementing it?
```

## Using fs_read with images

You can also explicitly use the `fs_read` tool to share images:

```
Amazon Q> Can you analyze this screenshot at /path/to/screenshot.png?
```

Amazon Q will automatically suggest using fs_read with Image mode when you mention image files.

## Image use cases

Common use cases for sharing images with Amazon Q include:

- Analyzing screenshots of error messages for troubleshooting
- Converting architecture diagrams into code implementations
- Discussing UI/UX designs and generating corresponding HTML/CSS
- Understanding flowcharts and translating them into algorithms
- Reviewing code snippets shared as images
- Interpreting technical diagrams for documentation

## Supported formats and limitations

Supported image formats include JPEG/JPG, PNG, GIF, and WebP. Images must be under 10MB in size, and you can share up to 10 images in a single request.

For best results:

- Use high-resolution images with clear text
- Provide specific instructions about what you want Amazon Q to do with the image
- For complex diagrams, consider providing additional context
