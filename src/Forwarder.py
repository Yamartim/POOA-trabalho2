import csv

class Forwarder():
    '''
    Class to retrieve a list of results and 
    forward it in any way (depending on the child implementation).
    '''
    def __init__(self, results: list):
        '''
        @param: results the list of results
        '''
        self._results = results
    def forward(self):
        "method to be overloaded"
        pass

class ForwarderCSV(Forwarder):
    '''
    Class to foward a list as a csv file
    '''
    def __init__(self, results, fl=None):
        '''
        @param: results the list of results
        @param: fl opened stream to write as csv
        '''
        super().__init__(results)
        self._file = fl
    def forward(self):
        "Creates csv writter and write every list item as a row"
        wr = csv.writer(self._file, quoting=csv.QUOTE_ALL)
        wr.writerows(self._results)

class ForwarderStdout(Forwarder):
    '''
    Class to foward a list on stdout
    '''
    def __init__(self, results):
        '''
        @param: results the list of results
        '''
        super().__init__(results)
    def forward(self):
        "to print results"
        print (self._results)

'''
Returns the correct forwarder class depending on the name param
'''
class ForwarderFactory():
    def create_forwarder(self, name, results, **kwargs):
        if name == 'csv':
            return ForwarderCSV(results, **kwargs)
        elif name == 'stdout':
            return ForwarderStdout(results, **kwargs)