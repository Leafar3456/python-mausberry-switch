retropie-mausberry-switch
=========================

Script for my "Retropie in a NES case" project

This script is intended to use with a mausberry shutdown circuit
```sh
http://mausberry-circuits.myshopify.com/products/shutdown-circuit-use-your-own-switch
```

Unlike the mausberry's script this doesn't keep looping and insteads halts the script to wait for gpio pin changes.

If you would like the script to also gracefully shutdown ES, Download:
```sh
https://retropie.org.uk/forum/topic/12895/ensuring-es-gracefully-finish-and-save-metadata-in-every-system-shutdown
```
and put it in "/etc/killes.sh" and uncomment line 24 and 25.
