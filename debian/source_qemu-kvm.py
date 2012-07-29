'''apport package hook for qemu-kvm

(c) 2009 Canonical Ltd.
Author: Dustin Kirkland <kirkland@canonical.com>
'''

from apport.hookutils import *

def add_info(report):
    attach_hardware(report)
    attach_related_packages(report, ['kvm*', '*libvirt*', 'virt-manager', 'qemu*'])
    report['KvmCmdLine'] = command_output(['ps', '-C', 'kvm', '-F'])
