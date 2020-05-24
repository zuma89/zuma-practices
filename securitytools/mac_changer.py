#!/usr/bin/env python3

import subprocess
from argparse import ArgumentParser


def get_arguments():
    parser = ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="interface to change MAC address")
    parser.add_argument("-m", "--mac", dest="new_mac", help="New MAC address")
    options = parser.parse_args()
    if not options.interface:
        # code to handle error
        parser.error("[-]  Please specify an interface, use --help for more info")
    elif not options.new_mac:
        # code to handle error
        parser.error("[-]  Please specify a MAC address, use --help for more info")
    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.run(["ifconfig", interface, "up"])


args = get_arguments()
change_mac(args.interface, args.new_mac)
