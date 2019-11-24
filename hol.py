from rhododendron.modules.exploit import *
from rhododendron.modules.printer import *

import click

# Click is a simple Python module that wraps the stdlib's
# optparse to make writing command line scripts fun.
# Unlike other modules,
# it's based around a simple API that does not come with too much magic and is composable.
@click.command()
@click.option('-i', '--ip',   type=str ,default='127.0.0.1',  help='The ip target')
def main(ip):
    '''Testing For Your NetWork'''
    echo    = Printer() # Objects
    fs      = Rhododendron() # Objects
    au      = Tool()
    echo.Mypass()
    echo.print_index('Rhododendron') # Show Interfice script

    ############
    #   Nmap   #
    ############
    echo.print_title('Start Nmap') 
    
    nmap = fs.nmap(ip)
    if nmap == {}: echo.print_error('nmap', 'Not Find Ports Opens'); sys.exit(0)
        
    #######################
    #    Search Exploit   #
    #######################
    echo.print_title('Start Search Exploit')
    time.sleep(1) # Delay execution for a given number of seconds. The argument may be a floating point number for subsecond precision.
    ports   =  list() # list exploits
    exploit =  list() # list ports open 
    for i in nmap:
        try:
            _, product, *_, version = nmap[i].split(';')
            product = product.split()[0]; version = version.split()[0]
            if len(version) >= 5: version = version[:len(version) - 1]
            ex = fs.find_exploit(product, version, i.split(';')[1])

            # add data 
            exploit.append(ex) if ex is not None else None
            ports.append(i.split(';')[1])

        except IndexError: pass
        except KeyError  : pass  
        except Exception as e: echo.print_error('Search Exploit', e)

    # Save Data in File history
    au.history(
        ip,
         '-'.join(ports),
         '-'.join(exploit)
        )
    
if __name__ == "__main__":
    main()