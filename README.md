# Linux x86_64: development platform for [PlatformIO](http://platformio.org)

Linux x86_64 (64-bit) is a Unix-like and mostly POSIX-compliant computer operating system (OS) assembled under the model of free and open-source software development and distribution. Using host OS (Mac OS X or Linux 64-bit) you can build native application for Linux x86_64 platform.

* [Home](https://registry.platformio.org/platforms/platformio/linux_x86_64) (home page in the PlatformIO Registry)
* [Documentation](https://docs.platformio.org/page/platforms/linux_x86_64.html) (advanced usage, packages, boards, frameworks, etc.)

# Usage

1. [Install PlatformIO](http://platformio.org)
2. Create PlatformIO project and configure a platform option in [platformio.ini](https://docs.platformio.org/page/projectconf.html) file:

## Stable version

```ini
[env:stable]
platform = linux_x86_64
board = ...
...
```

## Development version

```ini
[env:development]
platform = https://github.com/platformio/platform-linux_x86_64.git
board = ...
...
```

# Configuration

Please navigate to [documentation](https://docs.platformio.org/page/platforms/linux_x86_64.html).
