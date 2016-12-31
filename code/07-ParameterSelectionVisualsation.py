import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def plotParams(df,exactdict,lab,lab2):
    fig = plt.figure(figsize=(16, 8), dpi=80)
    plt1 = fig.add_subplot(221)
    plt1.plot(df['param'],df['median'])
    plt1.plot(df['param'],np.repeat(exactdict['median'],df.shape[0]))
    plt1.set_ylim(plt1.get_ylim()[0]-(0.02*plt1.get_ylim()[0]),plt1.get_ylim()[1]+(0.02*plt1.get_ylim()[1]))
    plt1.set_xlabel("parmeter")
    plt1.set_ylabel("median")
    plt1.legend([lab,'actual'])

    plt2 = fig.add_subplot(222)
    plt2.plot(df['param'],df['mean'])
    plt2.plot(df['param'],np.repeat(exactdict['mean'],df.shape[0]))
    plt2.set_ylim(plt2.get_ylim()[0]-(0.02*plt2.get_ylim()[0]),plt2.get_ylim()[1]+(0.02*plt2.get_ylim()[1]))
    plt2.set_xlabel("parmeter")
    plt2.set_ylabel("mean")
    plt2.legend([lab,'actual'])

    plt3 = fig.add_subplot(223)
    plt3.plot(df['param'],df['dia'])
    plt3.plot(df['param'],np.repeat(exactdict['dia'],df.shape[0]))
    plt3.set_ylim(plt3.get_ylim()[0]-(0.02*plt3.get_ylim()[0]),plt3.get_ylim()[1]+(0.02*plt3.get_ylim()[1]))
    plt3.set_xlabel("parmeter")
    plt3.set_ylabel("diameter")
    plt3.legend([lab,'actual'])

    plt4 = fig.add_subplot(224)
    plt4.plot(df['param'],df['eff_dia'])
    plt4.plot(df['param'],np.repeat(exactdict['eff_dia'],df.shape[0]))
    plt4.set_ylim(plt4.get_ylim()[0]-(0.02*plt4.get_ylim()[0]),plt4.get_ylim()[1]+(0.02*plt4.get_ylim()[1]))
    plt4.set_xlabel("parmeter")
    plt4.set_ylabel("effective dia")
    plt4.legend([lab,'actual'])

    fig.suptitle('Approximation statistics for varying parameter values of '+lab)
    fig.savefig(lab+lab2+'_param'+".png")
    plt.clf()


    plt.plot(df['param'],df['time'])
    plt.ylim(plt.ylim()[0]-(0.02*plt.ylim()[0]),plt.ylim()[1]+(0.02*plt.ylim()[1]))
    plt.xlabel("parmeter")
    plt.ylabel("time")
    plt.locator_params(nbins=4, axis='x')
    plt.title("Computation time for "+lab)
    plt.savefig(lab+lab2+'_time'+".png")
    plt.close()

# load files
pickleloc = '/media/Documents/01 Aalto/03 Study/Semester 01/05 Algorithmic Methods of Data Mining - Aristides Gionis/Project/rawdata/02-soc-epinions1/soc-Epinions1-Analysis'
lsccpsrpastatsfname = pickleloc + '/analysis-param-lscc-srspa-summ.csv'
lsccpsrsastatsfname = pickleloc + '/analysis-param-lscc-srsa-summ.csv'
lsccpanfstatsfname = pickleloc + '/analysis-param-lscc-anf-summ.csv'

lsccpsrpastats = pd.read_csv(lsccpsrpastatsfname)
lsccpsrsastats = pd.read_csv(lsccpsrsastatsfname)
lsccpanfstats = pd.read_csv(lsccpanfstatsfname)

lwccpsrpastatsfname = pickleloc + '/analysis-param-lwcc-srspa-summ.csv'
lwccpsrsastatsfname = pickleloc + '/analysis-param-lwcc-srsa-summ.csv'
lwccpanfstatsfname = pickleloc + '/analysis-param-lwcc-anf-summ.csv'

lwccpsrpastats = pd.read_csv(lwccpsrpastatsfname)
lwccpsrsastats = pd.read_csv(lwccpsrsastatsfname)
lwccpanfstats = pd.read_csv(lwccpanfstatsfname)


lsccexact = {'dia': 16,
 'eff_dia': 5.2980012587061234,
 'mean': 4.4049156603919295,
 'median': 4}


lwccexact = {'dia': 15,
 'eff_dia': 4.9918300215392755,
 'mean': 4.3078597183442406,
 'median': 4}

plotParams(lsccpsrpastats,lsccexact,"SRPA","LSCC")
plotParams(lsccpsrsastats,lsccexact,"SRSA","LSCC")
plotParams(lsccpanfstats,lsccexact,"ANF","LSCC")

plotParams(lwccpsrpastats,lwccexact,"SRPA","LWCC")
plotParams(lwccpsrsastats,lwccexact,"SRSA","LWCC")
plotParams(lwccpanfstats,lwccexact,"ANF","LWCC")


