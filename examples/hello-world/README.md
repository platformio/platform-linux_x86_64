How to build PlatformIO based project
=====================================

1. [Install PlatformIO Core](https://docs.platformio.org/page/core.html)
2. Download [development platform with examples](https://github.com/platformio/platform-linux_x86_64/archive/develop.zip)
3. Extract ZIP archive
4. Run these commands:

```shell
# Change directory to example
$ cd platform-linux_x86_64/examples/hello-world

# Build project
$ pio run

# Run program
> .pio/native/program

# Clean build files
$ pio run --target clean
```
