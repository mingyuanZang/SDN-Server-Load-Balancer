link s7 h6 down
py net.addHost('h6')
py net.addLink(s6, net.get('h6'))
#links
py s6.attach('s6-eth3')
py net.get('h6').cmd('ifconfig h6-eth0 10.6')
py net.get('h6').setMAC('00:00:00:00:00:06')
#xterm h6
h2 ping h6



