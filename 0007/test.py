from lib.framework import *
from lib.groups_and_tags import Group, Tag
from lib import console_log
import config
from platforms import platform

@test
class evnt_int_01(TestCase):
    group = Group.Automatic
    test_requirements = [((config.bmc_console_active), 'This test needs BMC console'),
                         ((config.bmc_ip != None), 'Can only be run over LAN')]
    tags = [Tag.ExternalEvent, Tag.InterfaceEvent]

    def test(self):
        console_log.BMC_EXPECT.DeterminePromptGeneration()
        console_log.BMC_EXPECT.LinuxPrompt()
        console_log.BMC_EXPECT.ClearPrompts()

        bmc_log.info("Sending Get Device ID Command")
        out = console_log.BMC_EXPECT.IpmiCmd([6, 1])
        if out[1][0] != 0x00:
            error(ResponseError('Completion Code', out[1][0], 0x00))


@test
class evnt_int_02(TestCase):
    group = Group.Automatic
    test_requirements = [((config.bmc_ip != None), 'Can only be run over LAN')]
    tags = [Tag.ExternalEvent, Tag.InterfaceEvent]

    def test(self):
        bmc_log.info("SOL Activating")
        ipmi_send([0x0C,0x20,0x00,0x01,0x01,0x00], compcode=0, raw=True)

@test
class evnt_int_04(TestCase):
    group = Group.Manual
    test_requirements = [((config.bmc_ip != None), 'Can only be run over LAN')]
    tags = [Tag.ExternalEvent, Tag.InterfaceEvent]

    def test(self):
        user_input("Connect to Host serial console. Press <Enter> to continue: ")

        bmc_log.info("Sending Issue Reset command to perform a host cold reset")
        ipmi_send(['OEM', 'ISSUE_RESET', 'BMC_NONE', 'HOST_COLD'], compcode=0)

        inp = user_input("Are there readable boot progress messages on the host console? [y/n]: ")
        if inp.strip().lower() != 'y':
            error(TestError("No boot progress messages on host console"))

@test
class evnt_int_06(TestCase):
    group = Group.Automatic
    test_requirements = [((config.bmc_ip != None), 'This test needs LAN'),
                         ((config.bmc_console_active), 'This test needs BMC console')]
    platform_requirements = [platform.has_ssp]
    tags = [Tag.ExternalEvent, Tag.InterfaceEvent]

    def test(self):
        console_log.BMC_EXPECT.DeterminePromptGeneration()
        console_log.BMC_EXPECT.LinuxPrompt()
        console_log.BMC_EXPECT.ClearPrompts()

        bmc_log.info("Going to enter SSP console menu")
        console_log.BMC_EXPECT.sendline(b'ssp_console')
        case = console_log.BMC_EXPECT.expect([b'Starting SSP Console', pexpect.TIMEOUT], timeout=5)
        if case == 0:
            bmc_log.info("Successfully enter SSP console menu")
        elif case == 1:
            error(TestError("Timeout waiting to enter SSP console menu"))

        bmc_log.info("Exit SSP console menu")
        console_log.BMC_EXPECT.SendCtrlC()

@test
class evnt_int_07(TestCase):
    group = Group.Manual
    tags = [Tag.ExternalEvent, Tag.InterfaceEvent]

    def test(self):
        user_input("Connect to Host serial console. Press <Enter> to continue: ")

        inp = user_input("Send the Get Device IP command using GEM SMA application: "
                        "'./gem_sma -i 6 1'. "
                         "Did the command return completion code 0x00? [y/n]: ")
        if inp.strip().lower() != 'y':
            error(TestError("Get Device ID did not return completion code 0x00"))
