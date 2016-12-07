from igraph import *
import time
from pprint import pprint
import numpy as np
import pickle
from datetime import datetime

def main( graphfname):
    '''

    :param graphfname: path of csv file with graph edgelists
    :return:
    '''

    def CreateConnectedComponents(graphloc,logfile):
        '''
        :param graphloc: location of the graph file
        :param logfile: filename for logfile
        :return: lscc and lwcc dictionaries
        '''

        printfile = open(logfile, 'w+')

        g = Graph.Read_Ncol(graphloc, names=True, directed=True)

        # Main graph
        graphsumm = {'number of edges':g.ecount(),
                     'number of vertices':g.vcount()}
        print("Main Graph:", file=printfile)
        pprint(graphsumm, printfile)
        print("---------------------------------------------"+"\n", file=printfile)

        # strongly connected component
        t0 = time.time()
        lscc = g.clusters().giant()
        t1 = time.time()

        lsccsumm = {'number of edges':lscc.ecount(),
                     'number of vertices':lscc.vcount()}

        t2 = time.time()
        lsccdm = np.array(lscc.shortest_paths())
        t3 = time.time()

        print("Largest Strongly Connected Component:", file=printfile)
        print("Generated in "+str(round((t1-t0)/60,3))+"mins", file=printfile)
        print("Distance matrix generated in "+str(round((t3-t2)/60,3))+"mins", file=printfile)
        print("Summary:", file=printfile)
        pprint(lsccsumm, printfile)
        print("---------------------------------------------" + "\n", file=printfile)


        lsccdict ={'glscc':lscc,
                   'summlscc':lsccsumm,
                   # 'dmlscc':lsccdm
                   }

        # weakly connected component
        t0 = time.time()
        lwcc = g.as_undirected(mode="collapse", combine_edges=None).clusters().giant()
        t1 = time.time()

        lwccsumm = {'number of edges':lwcc.ecount(),
                     'number of vertices':lwcc.vcount()}

        t2 = time.time()
        lwccdm = np.array(lwcc.shortest_paths())
        t3 = time.time()

        print("Largest Weakly Connected Component:", file=printfile)
        print("Generated in "+str(round((t1-t0)/60,3))+"mins", file=printfile)
        print("Distance matrix generated in "+str(round((t3-t2)/60,3)), file=printfile)
        print("Summary:", file=printfile)
        pprint(lwccsumm, printfile)
        print("---------------------------------------------" + "\n",file=printfile)

        printfile.close()

        lwccdict ={'glwcc':lwcc,
                   'summlwcc':lwccsumm,
                   # 'dmlwcc':lwccdm
                   }

        return lsccdict, lwccdict


    # create output file requirements
    graphname =  graphfname.split("/")[-1].split(".")[0]
    dirname = "/".join(graphfname.split("/")[0:-1])+"/"+graphname+datetime.now().strftime('%Y%m%d-%H-%M')
    logfname = dirname+"/"+graphname+'-log-'+datetime.now().strftime('%Y%m%d-%H-%M')+'.txt'
    lsccpfile = dirname+"/"+graphname+'-lscc-'+datetime.now().strftime('%Y%m%d-%H-%M')+'.pickle'
    lwccpfile = dirname+"/"+graphname+'-lwcc-'+datetime.now().strftime('%Y%m%d-%H-%M')+'.pickle'

    if not os.path.exists(dirname):
        os.makedirs(dirname)

    # extract connected components
    lsccout, lwccout = CreateConnectedComponents( graphfname,logfname)

    with open(lsccpfile, 'wb') as handle:
        pickle.dump(lsccout, handle, protocol=pickle.HIGHEST_PROTOCOL)

    with open(lwccpfile, 'wb') as handle:
        pickle.dump(lsccout, handle, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    main(sys.argv[1])

