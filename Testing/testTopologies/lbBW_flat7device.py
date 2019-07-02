#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    c0=net.addController(name='c0',
                      controller=RemoteController,
                      ip='127.0.0.1',
                      protocol='tcp',
                      port=6653)

    info( '*** Add switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch)
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch)
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch)



    info( '*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', mac='00:00:00:00:00:01', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', mac='00:00:00:00:00:02', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', mac='00:00:00:00:00:03', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', mac='00:00:00:00:00:04', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.0.0.5', mac='00:00:00:00:00:05', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.0.0.6', mac='00:00:00:00:00:06', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='10.0.0.7', mac='00:00:00:00:00:07', defaultRoute=None)

    info( '*** Add links\n')
    h1s5 = {'bw':1000}
    net.addLink(h1, s5, cls=TCLink , **h1s5)
    s5h2 = {'bw':1000}
    net.addLink(s5, h2, cls=TCLink , **s5h2)
    s5h3 = {'bw':1000}
    net.addLink(s5, h3, cls=TCLink , **s5h3)
    s5h4 = {'bw':1000}
    net.addLink(s5, h4, cls=TCLink , **s5h4)
    s5s2 = {'bw':1000}
    net.addLink(s5, s2, cls=TCLink , **s5s2)
    s5s3 = {'bw':1000}
    net.addLink(s5, s3, cls=TCLink , **s5s3)
    s2s1 = {'bw':1000}
    net.addLink(s2, s1, cls=TCLink , **s2s1)
    s3s4 = {'bw':1000}
    net.addLink(s3, s4, cls=TCLink , **s3s4)
    s4s1 = {'bw':1000}
    net.addLink(s4, s1, cls=TCLink , **s4s1)
    s1s6 = {'bw':1000}
    net.addLink(s1, s6, cls=TCLink , **s1s6)
    s1s7 = {'bw':1000}
    net.addLink(s1, s7, cls=TCLink , **s1s7)
    s6h5 = {'bw':1000}
    net.addLink(s6, h5, cls=TCLink , **s6h5)
    s7h6 = {'bw':1000}
    net.addLink(s7, h6, cls=TCLink , **s7h6)
    s7h7 = {'bw':1000}
    net.addLink(s7, h7, cls=TCLink , **s7h7)
   
    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s1').start([c0])
    net.get('s2').start([c0])
    net.get('s3').start([c0])
    net.get('s4').start([c0])
    net.get('s5').start([c0])
    net.get('s6').start([c0])
    net.get('s7').start([c0])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

