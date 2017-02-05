#!/usr/bin/env bash
echo "Probing sites timestamp:"
cat ./probe/*_ping.csv |tail -1|awk -F',' '{print $1}'
echo "Probing servers timestamp:"
cat ./probe/*_cacheping.csv |tail -1|awk -F',' '{print $1}'
echo "Traceroute servers timestamp:"
ls -tr ./trace/ |tail -1