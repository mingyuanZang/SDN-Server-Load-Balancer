------------------
ONOS projects
------------------
student-lbdynam: Main implementation project
student-lbRR: testing project for selection method RR and without LB
student-lbWRR:  testing project for selection method WRR
----------------------
Testing topologies
----------------------
lbBW_flat: LB directly connected to servers
lbBW_flat7device: used for dynamic change testing
lbBW_singleSwitch: One switch with 4 clients & 3 servers
lbBW_tree_topo: LB directly connected to neither servers nor clients

serial_req.py: python script run in client terminal to send requests

changePort.sh: commands run in Mininet CLI to change the conneccting port of server 2

----------------------
Testing steps
----------------------
1. Run the Mininet topology script
2. pingall in Mininet CLI
3. Deactivate fwd in controller
4. Compile the project and install it to ONOS controller
5. Activate the application in controller
6. Open client & server terminals in Mininet CLI
7. For server, run "sudo python -m SimpleHTTPServer 8000"
8. For client, run "time sudo python serial_req.py"


