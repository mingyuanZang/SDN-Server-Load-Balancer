#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf

def treeTopo():
    net = Mininet( controller=Controller )
    
    info( '*** Adding controller\n' )
    c0=net.addController(name='c0',
                      controller=RemoteController,
                      ip='127.0.0.1',
                      protocol='tcp',
                      port=6653)

    info( '*** Adding hosts\n' )
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', mac='00:00:00:00:00:01', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', mac='00:00:00:00:00:02', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', mac='00:00:00:00:00:03', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', mac='00:00:00:00:00:04', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.0.0.5', mac='00:00:00:00:00:05', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.0.0.6', mac='00:00:00:00:00:06', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='10.0.0.7', mac='00:00:00:00:00:07', defaultRoute=None)

    info( '*** Adding switches\n' )
    s1 = net.addSwitch( 's1', cls=OVSKernelSwitch )
    s2 = net.addSwitch( 's2', cls=OVSKernelSwitch )
    s3 = net.addSwitch( 's3', cls=OVSKernelSwitch )

    info( '*** Creating links\n' )
    s2h1 = {'bw':1000}
    net.addLink( h1, s2, cls=TCLink , **s2h1 )
    s2h2 = {'bw':1000} 
    net.addLink( h2, s2, cls=TCLink , **s2h2 )
    s2h3 = {'bw':1000}
    net.addLink( h3, s2, cls=TCLink , **s2h3 )
    s2h4 = {'bw':1000}
    net.addLink( h4, s2, cls=TCLink , **s2h4 )
    s3h5 = {'bw':1000} 
    net.addLink( h5, s3, cls=TCLink , **s3h5 )
    s3h6 = {'bw':1000}
    net.addLink( h6, s3, cls=TCLink , **s3h6 )
    s3h7 = {'bw':1000}
    net.addLink( h7, s3, cls=TCLink , **s3h7 )

    
    root = s1
    layer1 = [s2,s3]

    for idx,l1 in enumerate(layer1):
	rootl1 = {'bw':10000}
        net.addLink( root,l1 )
       
        
    info( '*** Starting network\n')
    net.build()

    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s1').start([c0])
    net.get('s2').start([c0])
    net.get('s3').start([c0])

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    treeTopo()
