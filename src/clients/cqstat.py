#!/usr/bin/env python

'''Cobalt Queue Status'''
__revision__ = '$Revision$'

import getopt, math, sys, time
import Cobalt.Proxy, Cobalt.Util

if __name__ == '__main__':
    try:
        (opts, args) = getopt.getopt(sys.argv[1:], 'df', ['version'])
    except getopt.GetoptError, msg:
        print "Usage: cqstat [--version] [-d] [-f jobid]"
        print msg
        raise SystemExit, 1

    if '--version' in sys.argv:
        print "cqstat %s" % __revision__
        raise SystemExit, 0

    jobid = None

    if len(args) > 0:
        jobid = args[0]

    if jobid:
        jobid_tosend = jobid
    else:
        jobid_tosend = "*"

    cqm = Cobalt.Proxy.queue_manager()
    query = [{'tag':'job', 'user':'*', 'walltime':'*'}]
    if '-f' in sys.argv:
        query[0].update({'nodes':'*', 'state':'*', 'jobid':'%s', "location":'*'})
    jobs = cqm.GetJobs(query)

    if '-f' in sys.argv:
        header = [('JobID', 'User', 'WallTime', 'Nodes', 'State', 'Location', 'Mode', 'Procs', 'Queue', 'StartTime')]
    else:
        header = [('JobID', 'User', 'WallTime', 'Nodes', 'State', 'Location')]
        
    output = [[job.get(x) for x in [y.lower() for y in header[0]]] for job in jobs]

    if output:
        maxjoblen = max([len(item[0]) for item in output])
        jobidfmt = "%%%ss" % maxjoblen
    # next we cook walltime
    for i in xrange(len(output)):
        t = int(output[i][2].split('.')[0])
        h = int(math.floor(t/60))
        t -= (h * 60)
        output[i][2] = "%02d:%02d:00" % (h, t)
        output[i][0] = jobidfmt % output[i][0]
        if '-f' in sys.argv:
            if output[i][9] == '-1' or output[i][9] == 'BUG':
                output[i][9] = 'N/A'
            else:
                output[i][9] = time.strftime("%m/%d/%y %T", time.localtime(float(output[i][9])))

    output.sort()
    Cobalt.Util.print_tabular([tuple(x) for x in header + output])
