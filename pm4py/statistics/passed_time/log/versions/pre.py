from pm4py.algo.discovery.dfg import factory as dfg_factory


def apply(log, activity, parameters=None):
    """
    Gets the time passed from each preceding activity

    Parameters
    -------------
    log
        Log
    activity
        Activity that we are considering
    parameters
        Possible parameters of the algorithm

    Returns
    -------------
    dictio
        Dictionary containing a 'pre' key with the
        list of aggregates times from each preceding activity to the given activity
    """
    if parameters is None:
        parameters = {}

    dfg = dfg_factory.apply(log, variant="performance", parameters=parameters)

    pre = []

    for entry in dfg.keys():
        if entry[1] == activity:
            pre.append([entry[0], float(dfg[entry])])

    return {"pre": pre}