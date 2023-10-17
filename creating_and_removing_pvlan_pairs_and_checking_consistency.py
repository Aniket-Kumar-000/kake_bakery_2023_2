testbed:
    custom:
      
        primary : "2260"
        isolated : "2261"
        community : "2262"
        
        num_one : "1"
        num_two : "2"

        port : "15"
        vls : "30,40,50,60,70"    

class common_setup(aetest.CommonSetup):
    @aetest.subsection
    def connect_to_devices(self,testscript,testbed,R1):
        global uut1 #, uut1_intf1 , uut1_intf2
        global file
        uut1=testbed.devices[R1]
        testscript.parameters['uut1'] = uut1
        n1=testbed.custom['num_one']
        n2=testbed.custom['num_two']
    
        log.info("Connecting to Device...")
        log.info("%s"%uut1.name)
        try:
            uut1.connect()
            log.info("Connection to %s Successful..."%uut1.name)
        except Exception as e:
            log.info("Connection to %s Unsuccessful "\
                      "Exiting error:%s"%(uut1.name,e))
            self.failed(goto=['exit'])

class CSCwh52964(aetest.Testcase):
    @aetest.test
    def creating_private_vlan_pair(self,testbed,testscript):
        global v
        global c
        global i
        
        global ran_v2
        global ran_c2
        global ran_i2
        
        global ran_v3
        global ran_c3
        global ran_i3
        
        x = 0
        y = 0
        z = 0
        
        uut1.configure("feature private-vlan")
        v = testbed.custom['primary']
        c = testbed.custom['community']
        i = testbed.custom['isolated']
        
        testscript.parameters['v'] = v
        testscript.parameters['c'] = c
        testscript.parameters['i'] = i
        
        cmd = f""" vlan {v}\n private-vlan primary\n vlan {c}\n private-vlan community\n no shut\n vlan {i}\n private-vlan isolated\n no shut\n exit\n vlan {v}\n private-vlan association add {i},{c}\n no shut"""
        status = True         
        try:
            uut1.configure(cmd)
            output = uut1.execute("show vlan private-vlan")
            pattern1 = fr"{v}\s*{i}\s*[Ii]solated"
            if re.findall(pattern1, output):
                pattern2 = fr"{v}\s*{c}\s*[Cc]ommunity"
                if re.findall(pattern2, output):
                    match = True
                else:
                    log.error("Something went wrong")
            elif "non-operational" in output:
                log.error("Some pvlan pairs showing non-operational")
        except:
            log.error('Invalid CLI given: %s' % (cmd))
            status = False
        if status == False:
            x = x + 1
            
        ran_v2 = str(random.randint(300,400))
        ran_c2 = str(random.randint(300,400))
        ran_i2 = str(random.randint(300,400))
        print("second pair :-", ran_v2,ran_c2,ran_i2)
        while ran_v2 == ran_c2 and ran_v2 == ran_i2:
            log.info("Same numbers observed trying again to get some random unique numbers...")
            ran_v2 = str(random.randint(300,400))
            ran_c2 = str(random.randint(300,400))
            ran_i2 = str(random.randint(300,400))
            print("second pair :-", ran_v2,ran_c2,ran_i2)
            
        testscript.parameters['ran_v2'] = ran_v2
        testscript.parameters['ran_c2'] = ran_c2
        testscript.parameters['ran_i2'] = ran_i2    
            
        cmd = f""" vlan {ran_v2}\n private-vlan primary\n vlan {ran_c2}\n private-vlan community\n no shut\n vlan {ran_i2}\n private-vlan isolated\n no shut\n exit\n vlan {ran_v2}\n private-vlan association add {ran_i2},{ran_c2}\n no shut"""
        status = True         
        try:
            uut1.configure(cmd)
            output = uut1.execute("show vlan private-vlan")
            pattern1 = fr"{ran_v2}\s*{ran_i2}\s*[Ii]solated"
            if re.findall(pattern1, output):
                pattern2 = fr"{ran_v2}\s*{ran_c2}\s*[Cc]ommunity"
                if re.findall(pattern2, output):
                    match = True
                else:
                    log.error("Something went wrong")
            elif "non-operational" in output:
                log.error("Some pvlan pairs showing non-operational")
        except:
            log.error('Invalid CLI given: %s' % (cmd))
            status = False
        if status == False:
            y = y + 1
            
        ran_v3 = str(random.randint(700,800))
        ran_c3 = str(random.randint(700,800))
        ran_i3 = str(random.randint(700,800))
        print("third pair :-",ran_v3,ran_c3,ran_i3)
        while ran_v2 == ran_c2 and ran_v2 == ran_i2:
            log.info("Same numbers observed trying again to get some random unique numbers...")
            ran_v3 = str(random.randint(700,800))
            ran_c3 = str(random.randint(700,800))
            ran_i3 = str(random.randint(700,800))
            print("third pair :-",ran_v3,ran_c3,ran_i3)
            
        testscript.parameters['ran_v3'] = ran_v3
        testscript.parameters['ran_c3'] = ran_c3
        testscript.parameters['ran_i3'] = ran_i3
            
        cmd = f""" vlan {ran_v3}\n private-vlan primary\n vlan {ran_c3}\n private-vlan community\n no shut\n vlan {ran_i3}\n private-vlan isolated\n no shut\n exit\n vlan {ran_v3}\n private-vlan association add {ran_i3},{ran_c3}\n no shut"""
        status = True         
        try:
            uut1.configure(cmd)
            output = uut1.execute("show vlan private-vlan")
            pattern1 = fr"{ran_v3}\s*{ran_i3}\s*[Ii]solated"
            if re.findall(pattern1, output):
                pattern2 = fr"{ran_v3}\s*{ran_c3}\s*[Cc]ommunity"
                if re.findall(pattern2, output):
                    match = True
                else:
                    log.error("Something went wrong")
            elif "non-operational" in output:
                log.error("Some pvlan pairs showing non-operational")
        except:
            log.error('Invalid CLI given: %s' % (cmd))
            status = False
        if status == False:
            z = z + 1 
        if x != 0:
            self.failed("Issue with 1st pair")
        elif y != 0:
            self.failed("Issue with 2nd pair")
        elif z != 0:
            self.failed("Issue with 3rd pair")
    @aetest.test        
    def adding_ports_to_port_channel(self,testbed,testscript):
        global chan,n1,n2,vlans
        n1=testbed.custom['num_one']
        n2=testbed.custom['num_two']
        vlans=testbed.custom['vls']
        chan=testbed.custom['port']
        log.info("create vlans")
        uut1.configure(f"vlan {vlans}\nno shut")
        log.info("create port-channel and adding members to PO")
        uut1.configure(f"int eth 1/{n1}-{n2}\nswitchport\nchannel-group {chan} mode active\n no shut")
        
    @aetest.test
    def configure_trunk_prom(self,testbed,testscript):
        log.info("configure po as Trunk-promiscous and map the primary vlans")
        uut1.configure(f"interface po {chan}\n switchport\nswitchport mode private-vlan trunk promiscuous\nswitchport private-vlan trunk allowed vlan add {vlans}\nswitchport private-vlan mapping trunk {v} {i}-{c}\nswitchport private-vlan mapping trunk {ran_v2} {ran_i2},{ran_c2}\nswitchport private-vlan mapping trunk {ran_v3} {ran_i3},{ran_c3}")
        output=uut1.execute("show vlan private-vlan")
        pattern1 = fr"{v}.*{i}.*[Ii]solated.*Po{chan}.*Eth1/{n1}.*Eth1/{n2}.*"
        if re.findall(pattern1, output):
            pattern2 = fr"{v}.*{c}.*[Cc]ommunity.*Po{chan}.*.*Eth1/{n1}.*Eth1/{n2}.*"
            if re.findall(pattern2, output):
                pattern3 = fr"{ran_v2}.*{ran_i2}.*[Ii]solated.*Po{chan}.*.*Eth1/{n1}.*Eth1/{n2}.*"
                if re.findall(pattern3, output):
                    pattern4 = fr"{ran_v2}.*{ran_c2}.*[Cc]ommunity.*Po{chan}.*.*Eth1/{n1}.*Eth1/{n2}.*"
                    if re.findall(pattern4, output):
                        pattern5 = fr"{ran_v3}.*{ran_i3}.*[Ii]solated.*Po{chan}.*.*Eth1/{n1}.*Eth1/{n2}.*"
                        if re.findall(pattern5, output):
                            pattern6 = fr"{ran_v3}.*{ran_c3}.*[Cc]ommunity.*Po{chan}.*.*Eth1/{n1}.*Eth1/{n2}.*"
                            if re.findall(pattern6, output):
                                match = True
                            else:
                                self.failed("Something went wrong")
                        else:
                             self.failed("Something went wrong")
                    else:
                        self.failed("Something went wrong")
                else:
                    self.failed("Something went wrong")
            else:
                self.failed("Something went wrong")                       
        elif "non-operational" in output:
            log.error("Some pvlan pairs showing non-operational")
            self.failed()
        if match:
            self.passed("All mappings of trunk promiscous are present.")
    @aetest.test
    def verify_mapping_in_PO(self,testbed,testscript):        
        output=uut1.execute(f"sh run int po{chan}")
        conditions = [
            vlans in output,
            v in output,
            c in output,
            i in output,
            ran_v2 in output,
            ran_c2 in output,
            ran_i2 in output,
            ran_v3 in output,
            ran_c2 in output,  
            ran_i3 in output,
            ]
        
        if all(conditions):
            self.passed("mapping is successful")
        else:
            self.failed("mapping is unsuccessful")
            
    @aetest.test
    def removing_private_vlan_mapping_trunk_under_po_and_verify(self,testbed,testscript):
        A = 0
        B = 0
        C = 0
        count1 = 0
        count2 = 0
        count3 = 0
        mount1 = 0
        mount2 = 0
        mount3 = 0       
        uut1.configure(f"int po {chan}\nno switchport private-vlan mapping trunk {v} {i}-{c}\nno switchport private-vlan mapping trunk {ran_v2} {ran_i2},{ran_c2}\nno switchport private-vlan mapping trunk {ran_v3} {ran_i3},{ran_c3}\n")
        output3=uut1.execute(f"sh run int po{chan}")
        lines3 = output3.split('\n')
        lines3 = [line.strip() for line in lines3]
        pattern1=f"switchport private-vlan mapping trunk {v} {i}-{c}"
        pattern2=f"switchport private-vlan mapping trunk {ran_v2} {ran_i2},{ran_c2}"
        pattern3=f"switchport private-vlan mapping trunk {ran_v3} {ran_i3},{ran_c3}"
        for j in lines3:
            if pattern1 == j:
                count1 = count1 +1
            else:
                mount1 = mount1 +1
        if count1 != 0:
            log.error("not able to remove switchport_private_vlan_mapping_trunk_under_port_channel")
            A = A + 1
        for j in lines3:
            if pattern2 == j:
                count2 = count2 +1
            else:
                mount2 = mount2 +1
        if count2 != 0:
            log.error("not able to remove switchport_private_vlan_mapping_trunk_under_port_channel")
            B = B + 1
        for j in lines3:
            if pattern3 == j:
                count3 = count3 +1
            else:
                mount3 = mount3 +1
        if count3 != 0:
            log.error("not able to remove switchport_private_vlan_mapping_trunk_under_port_channel")
            C = C + 1
        log.info("Reload process will take few minutes...")
        uut1.configure("copy running-config startup-config")
        uut1.transmit("reload\r")
        uut1.receive("This command will reboot the system")
        uut1.transmit("y\r")
        uut1.receive(r'nopattern^')
        log.info("Waiting for device bringup")
        time.sleep(280)
        uut1.disconnect()
        time.sleep(10)
        uut1.connect()
        time.sleep(10)
        output=uut1.execute(f"sh run int po{chan}")
        lines = output.split('\n')
        lines = [line.strip() for line in lines]
        pattern1=f"switchport private-vlan mapping trunk {v} {i}-{c}"
        pattern2=f"switchport private-vlan mapping trunk {ran_v2} {ran_i2},{ran_c2}"
        pattern3=f"switchport private-vlan mapping trunk {ran_v3} {ran_i3},{ran_c3}"
        for j in lines:
            if pattern1 == j:
                count1 = count1 +1
            else:
                mount1 = mount1 +1
        if count1 != 0:
            log.error("not able to remove switchport_private_vlan_mapping_trunk_under_port_channel")
            A = A + 1
        for j in lines:
            if pattern2 == j:
                count2 = count2 +1
            else:
                mount2 = mount2 +1
        if count2 != 0:
            log.error("not able to remove switchport_private_vlan_mapping_trunk_under_port_channel")
            B = B + 1
        for j in lines:
            if pattern3 == j:
                count3 = count3 +1
            else:
                mount3 = mount3 +1
        if count3 != 0:
            log.error("not able to remove switchport_private_vlan_mapping_trunk_under_port_channel")
            C = C + 1    
        if A != 0:
            self.failed("Issue with 1st pair")
        elif B != 0:
            self.failed("Issue with 2nd pair")
        elif C != 0:
            self.failed("Issue with 3rd pair")
