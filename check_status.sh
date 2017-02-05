echo "Probing sites timestamp:"
cat ~/superbowl/probe/*_ping.csv |tail -1|awk -F',' '{print $1}'
echo "Probing servers timestamp:"
cat ~/superbowl/probe/*_cacheping.csv |tail -1|awk -F',' '{print $1}'
echo "Traceroute servers timestamp:"
ls -tr ~/superbowl/trace/ |tail -1|awk -F'_' '{print $2}'
echo "END"
