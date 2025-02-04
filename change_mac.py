import subprocess
import re

mac_addresse = str(input('Please enter the mac addresse :'))
network_interface = int(input('Please enter the name of your interface :'))
if network_interface == '' :
        print('[-]please enter the name of your interface, and try again')
        exit()
elif mac_addresse == '' :
        print('[-]please enter the new mac addresse, and try again')
        exit()
else:
        print('[+]Please wait ...')

        

def change_mac(network_interface, mac_addresse):
    subprocess.call(f'ifconfig {network_interface} down', shell=True)
    subprocess.call(f'ifconfig {network_interface} hw ether {mac_addresse}', shell=True)
    subprocess.call(f'ifconfig {network_interface} up', shell=True)
    print(f'[+]Changing mac addresse to {mac_addresse} ....')


def get_mac(network_interface, mac_addresse) :
    ifconfig_result = subprocess.check_output(f'ifconfig {network_interface}', shell=True).decode("UTF-8")
    result = re.search('\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_result)
    return result[0]



change_mac(network_interface, mac_addresse)
new_mac = get_mac(network_interface, mac_addresse)
if new_mac == mac_addresse :
    print(f'[+]Mac addresse changed to {mac_addresse}')
else:
    print(f'[-]Failed to chonging mac addresse to {mac_addresse}\n Please check the mac addresse and name of your network interface try again')

    
