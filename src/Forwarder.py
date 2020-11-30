import csv

class Forwarder():
    def __init__(self, results):
        self._results = results
    def foward(self):
        pass

class ForwarderCSV(Forwarder):
    def __init__(self, results, fl=None):
        super().__init__(results)
        self._file = fl
    def forward(self):
        wr = csv.writer(self._file, quoting=csv.QUOTE_ALL)
        wr.writerows(self._results)

class ForwarderStdout(Forwarder):
    def __init__(self, results):
        super().__init__(results)
    def forward(self):
        print (self._results)

class ForwarderFactory():
    def create_forwarder(self, name, results, **kwargs):
        if name == 'csv':
            return ForwarderCSV(results, **kwargs)
        elif name == 'stdout':
            return ForwarderStdout(results, **kwargs)