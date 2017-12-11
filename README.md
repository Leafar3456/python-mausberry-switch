retropie-mausberry-switch
=========================

Script for my "Retropie in a NES case" project

This script is intended to use with a mausberry shutdown circuit
http://mausberry-circuits.myshopify.com/products/shutdown-circuit-use-your-own-switch

Like most such scripts, it sends a continuous "on" signal to the mausberry circuit for it to cut power once shutdown is complete, and it listens on a GPIO pin for an action on a switch in order to send a shutdown command to the OS.
