# Relative Mouse Offset

By default, during users' streaming sessions, WorkSpaces Applications transmits information about
mouse movements to the streaming instance by using absolute coordinates and
rendering the mouse movements locally. For graphics-intensive applications, such as
computer-aided design (CAD)/computer-aided manufacturing (CAM) software or video
games, mouse performance improves when relative mouse mode is enabled. Relative
mouse mode uses relative coordinates, which represent how far the mouse moved since
the last frame, rather than the absolute x-y coordinate values within a window or
screen. When relative mouse mode is enabled, WorkSpaces Applications renders the mouse movements
remotely.

Users can enable this feature during their WorkSpaces Applications streaming sessions
by doing either of the following:

- Pressing Ctrl+Shift+F8 on the Windows client application or Ctrl+Shift+Fn+F8 on the macOS
  client application
- Choosing **Relative Mouse Position [Ctrl+Shift+F8]** from the
  **Settings** menu on the WorkSpaces Applications toolbar in the top left area of their streaming session window. This method works when they use classic mode or **Desktop View**.
