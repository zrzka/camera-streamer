# Camera streamer

* Discovers `_cameraplayer._udp` service on local network
* Streams camera to the player via `raspivid`
  * Check the [camera player](https://github.com/zrzka/camera-player) project

## Deployment

This project is ready to be deployed to the [balenaCloud](https://www.balena.io/cloud).

```sh
balena push $YOUR_APP_NAME
```

## Hardware

* Raspberry Pi 3 B+
* Raspberry Pi Camera V2

## Fleet configuration variables

* `BALENA_HOST_CONFIG_gpu_mem_1024=448`
* `BALENA_HOST_CONFIG_gpu_mem_256=192`
* `BALENA_HOST_CONFIG_gpu_mem_512=256`
* `BALENA_HOST_CONFIG_start_x=1`
