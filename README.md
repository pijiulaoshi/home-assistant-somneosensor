# home-assistant-somneosensor
Custom Home Assistant component for Philips Somneo Connect

This component allows you to get the data from your Philips Somneo sensors into Home Assistant.

This is my first attempt at making a custom integration, so maybe it is not as good as it should be. It works though :) at least for me it does.

The next step, I hope, is to control certain settings/functions of the Somneo.

Feel free to provide constructive feedback.

Set-up:
1. copy the somneosensor folder to your custom_components folder.
2. add the following to your configuration.yaml:

sensor:
  - platform: somneosensor
    host: <somneo_ip>
    port: <somneo_port>  (default: 443, probably redundant setting)
    display_options:
      - temperature
      - humidity
      - light
      - noise
