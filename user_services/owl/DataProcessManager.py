from data_ops import read_pcap as pcap_reader
import glob
import sys
import os

class DataProcessManager:
    def __init__(self, dir_path, outfile, delete_pcap=False, verbose=True):

        self.data_dir = dir_path
        files = glob.glob(f'{self.data_dir}/*.pcap')
        # Remove zero-bye pcap files
        self.pcapfiles = [f for f in files if os.stat(f).st_size > 0] 
        
        print("pcapfiles: ", self.pcapfiles)

        self.outfile = f'{self.data_dir}/{outfile}'
        self.delete_pcap = delete_pcap
        self.verbose = verbose


    def process(self):
        processor = pcap_reader.PcapProcessor(
                            self.pcapfiles, 
                            self.outfile, 
                            self.delete_pcap, 
                            self.verbose)
        processor.process()


    def delete_csv(self):
        csv_files = glob.glob(f'{self.data_dir}/*.csv')
        
        for csv_f in csv_files:
            try:
                os.remove(csv_f)
            except:
                print("Error while deleting file: ", csv_f)


    def delete_pcap(self):
        for pcap_f in self.pcapfiles:
            try:
                os.remove(pcap_f)
            except:
                print("Error while deleting file: ", pcap_f)

if __name__ == "__main__":
    '''
    Args:
        [1] action (required): 'process' | 'delete_csv' | 'delete_pcap'
        [2] directory path (required)
        [3] output ccsv file name (optional)
    '''

    if len(sys.argv) < 3:
        print("Error: needs action +  directory path")
        exit(1)
    
    elif len(sys.argv) == 4:
        outfile = sys.argv[3]

    else:
        outfile = 'out.csv'

    # Create an instance
    data_processor = DataProcessManager(sys.argv[2], outfile)

    # Action!
    if sys.argv[1] == 'process':
        data_processor.process()

    elif sys.argv[1] == 'delete_csv':
        data_processor.delete_csv()

    elif sys.argv[1] == 'delete_pcap':
        data_processor.delete_pcap()

    else:
        print("Error: no such action")
        exit(1)

    
