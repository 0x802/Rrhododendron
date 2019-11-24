import sqlite3 

from .printer import Printer

class Tool(Printer):
    """
    Tools for sqlite3 and details infomation
    """
    def __init__(self):
        self.path_db = './rhododendron/resources/sqlite/explit.sqlite'  #  Path dtabase 
        
    def details(self, data: dict, port: str = None):
        for i in data:
            if i.split(';')[0] == 'nmap':
                self.print_out1("Port %s" % i.split(';')[1], str())
                self.print_out2('type',     data[i].split(';')[0])
                self.print_out2('Product',  data[i].split(';')[1])
                self.print_out2('cpe' ,     data[i].split(';')[2])
                self.print_out2('Version',  data[i].split(';')[3])

            elif i == 'exploit':
                self.print_out1("Exploiting Port: %s" % (port), str())
                self.print_out2('Title',    data[i].split(';')[0])
                self.print_out2('Type',     data[i].split(';')[1])
                self.print_out2('Platform', data[i].split(';')[2])
                self.print_out2('File',     data[i].split(';')[3])

    def sqlite(self, product: str, version: str) -> list():
        """
        1. The origin of this software must not be misrepresented; you must not
           claim that you wrote the original software. If you use this software
           in a product, an acknowledgment in the product documentation would be
           appreciated but is not required.
        2. Altered source versions must be plainly marked as such, and must not be
           misrepresented as being the original software.
        3. This notice may not be removed or altered from any source distribution.
        """
        
        # Opens a connection to the SQLite database file *database*.
        # You can use ":memory:" to open a database connection 
        # to a database that resides in RAM instead of on disk.
        exploit_db_connect = sqlite3.connect(self.path_db)  # connect to database exploit
        
        # Executes a SQL statement. Non-standard.
        exploit_db_search  = exploit_db_connect.execute("select description, type, platform, file from \
                `Data_Exploit` where description LIKE '%{}% %{}%'; ".format(product, version)) # serach in database for information

        return exploit_db_search.fetchall()

    def history(self, ip, ports, exploit):
        open('./rhododendron/loge/history', 'a').write('\n{} ... {} ... {}'.format(ip, ports, exploit))
