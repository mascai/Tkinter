#!/bin/bash
sudo mn --topo single,3 --mac --controller remote --switch ovsk
#~/pox/pox.py openflow.of_01 --port=6653 forwarding.l2_learning 
