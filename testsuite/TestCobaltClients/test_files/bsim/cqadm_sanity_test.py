import testutils

# ---------------------------------------------------------------------------------
def test_cqadm_getq_option_1():
    """
    cqadm test run: getq_option_1

        Command Output:
          Queue    Users  MinTime  MaxTime  MaxRunning  MaxQueued  MaxUserNodes  MaxNodeHours  TotalNodes  AdminEmail  State    Cron  Policy   Priority  
          ===============================================================================================================================================
          default  None   None     None     None        None       None          None          None        None        running  None  default  0         
          q_1      None   None     None     None        None       None          None          None        None        running  None  default  0         
          q_2      None   None     None     None        None       None          None          None        None        running  None  default  0         
          q_3      None   None     None     None        None       None          None          None        None        running  None  default  0         
          q_4      None   None     None     None        None       None          None          None        None        running  None  default  0         
          

    """

    args      = """--getq"""
    exp_rs    = 0

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_getq_option_2():
    """
    cqadm test run: getq_option_2

        Command Output:
          
          cqadm.py -d --getq
          
          component: "queue-manager.get_queues", defer: True
            get_queues(
               [{'maxuserjobs': '*', 'priority': '*', 'name': '*', 'mintime': '*', 'totalnodes': '*', 'cron': '*', 'state': '*', 'tag': 'queue', 'maxqueued': '*', 'maxrunning': '*', 'maxusernodes': '*', 'maxnodehours': '*', 'policy': '*', 'maxtime': '*', 'adminemail': '*', 'users': '*'}],
               )
          
          
          [{'maxuserjobs': None, 'priority': 0, 'name': 'default', 'mintime': None, 'totalnodes': None, 'cron': None, 'state': 'running', 'tag': 'queue', 'maxqueued': None, 'maxrunning': None, 'maxusernodes': None, 'maxnodehours': None, 'policy': 'default', 'maxtime': None, 'adminemail': None, 'users': None}, {'maxuserjobs': None, 'priority': 0, 'name': 'q_4', 'mintime': None, 'totalnodes': None, 'cron': None, 'state': 'running', 'tag': 'queue', 'maxqueued': None, 'maxrunning': None, 'maxusernodes': None, 'maxnodehours': None, 'policy': 'default', 'maxtime': None, 'adminemail': None, 'users': None}, {'maxuserjobs': None, 'priority': 0, 'name': 'q_3', 'mintime': None, 'totalnodes': None, 'cron': None, 'state': 'running', 'tag': 'queue', 'maxqueued': None, 'maxrunning': None, 'maxusernodes': None, 'maxnodehours': None, 'policy': 'default', 'maxtime': None, 'adminemail': None, 'users': None}, {'maxuserjobs': None, 'priority': 0, 'name': 'q_2', 'mintime': None, 'totalnodes': None, 'cron': None, 'state': 'running', 'tag': 'queue', 'maxqueued': None, 'maxrunning': None, 'maxusernodes': None, 'maxnodehours': None, 'policy': 'default', 'maxtime': None, 'adminemail': None, 'users': None}, {'maxuserjobs': None, 'priority': 0, 'name': 'q_1', 'mintime': None, 'totalnodes': None, 'cron': None, 'state': 'running', 'tag': 'queue', 'maxqueued': None, 'maxrunning': None, 'maxusernodes': None, 'maxnodehours': None, 'policy': 'default', 'maxtime': None, 'adminemail': None, 'users': None}]
          Queue    Users  MinTime  MaxTime  MaxRunning  MaxQueued  MaxUserNodes  MaxNodeHours  TotalNodes  AdminEmail  State    Cron  Policy   Priority  
          ===============================================================================================================================================
          default  None   None     None     None        None       None          None          None        None        running  None  default  0         
          q_1      None   None     None     None        None       None          None          None        None        running  None  default  0         
          q_2      None   None     None     None        None       None          None          None        None        running  None  default  0         
          q_3      None   None     None     None        None       None          None          None        None        running  None  default  0         
          q_4      None   None     None     None        None       None          None          None        None        running  None  default  0         
          

    """

    args      = """-d --getq"""
    exp_rs    = 0

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_getq_option_3():
    """
    cqadm test run: getq_option_3

        Command Output:
          Queue    Users  MinTime  MaxTime  MaxRunning  MaxQueued  MaxUserNodes  MaxNodeHours  TotalNodes  AdminEmail  State    Cron  Policy   Priority  
          ===============================================================================================================================================
          default  None   None     None     None        None       None          None          None        None        running  None  default  0         
          q_1      None   None     None     None        None       None          None          None        None        running  None  default  0         
          q_2      None   None     None     None        None       None          None          None        None        running  None  default  0         
          q_3      None   None     None     None        None       None          None          None        None        running  None  default  0         
          q_4      None   None     None     None        None       None          None          None        None        running  None  default  0         
          

    """

    args      = """-f --getq"""
    exp_rs    = 0

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_preempt_job_1():
    """
    cqadm test run: preempt_job_1

        Command Output:
          
          cqadm.py -d --preempt 1 2 3
          
          component: "queue-manager.preempt_jobs", defer: True
            preempt_jobs(
               [{'tag': 'job', 'location': '*', 'walltime': '*', 'jobid': 1}, {'tag': 'job', 'location': '*', 'walltime': '*', 'jobid': 2}, {'tag': 'job', 'location': '*', 'walltime': '*', 'jobid': 3}],
               georgerojas,
               False,
               )
          
          
          Failed to match any jobs or queues
          

    """

    args      = """-d --preempt 1 2 3"""
    exp_rs    = 0

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_preempt_job_2():
    """
    cqadm test run: preempt_job_2

        Command Output:
          Failed to match any jobs or queues
          

    """

    args      = """-f --preempt 1 2 3"""
    exp_rs    = 0

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_kill_job_1():
    """
    cqadm test run: kill_job_1

        Command Output:
          
          cqadm.py -d -f --kill 1 2 3
          
          component: "queue-manager.del_jobs", defer: False
            del_jobs(
               [{'tag': 'job', 'location': '*', 'walltime': '*', 'jobid': 1}, {'tag': 'job', 'location': '*', 'walltime': '*', 'jobid': 2}, {'tag': 'job', 'location': '*', 'walltime': '*', 'jobid': 3}],
               True,
               georgerojas,
               )
          
          
          Failed to match any jobs or queues
          

    """

    args      = """-d -f --kill 1 2 3"""
    exp_rs    = 0

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_kill_job_2():
    """
    cqadm test run: kill_job_2

        Command Output:
          Failed to match any jobs or queues
          

    """

    args      = """--kill 1 2 3"""
    exp_rs    = 0

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_kill_job_3():
    """
    cqadm test run: kill_job_3

        Command Output:
          Failed to match any jobs or queues
          

    """

    args      = """-f --kill 1 2 3"""
    exp_rs    = 0

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_kill_job_4():
    """
    cqadm test run: kill_job_4

        Command Output:
          
          cqadm.py -d --kill 1 2 3
          
          component: "queue-manager.del_jobs", defer: False
            del_jobs(
               [{'tag': 'job', 'location': '*', 'walltime': '*', 'jobid': 1}, {'tag': 'job', 'location': '*', 'walltime': '*', 'jobid': 2}, {'tag': 'job', 'location': '*', 'walltime': '*', 'jobid': 3}],
               False,
               georgerojas,
               )
          
          
          Failed to match any jobs or queues
          

    """

    args      = """-d --kill 1 2 3"""
    exp_rs    = 0

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_addq_option_1():
    """
    cqadm test run: addq_option_1

        Command Output:
          At least on jobid or queue name must be supplied
          

    """

    args      = """--addq"""
    exp_rs    = 256

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_addq_option_2():
    """
    cqadm test run: addq_option_2

        Command Output:
          Added Queues  
          ==============
          myq1          
          myq3          
          myq2          
          

    """

    args      = """--addq myq1 myq2 myq3"""
    exp_rs    = 0

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_delq_option_1():
    """
    cqadm test run: delq_option_1

        Command Output:
          At least on jobid or queue name must be supplied
          

    """

    args      = """--delq"""
    exp_rs    = 256

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_delq_option_2():
    """
    cqadm test run: delq_option_2

        Command Output:
          Deleted Queues  
          ================
          myq3            
          myq2            
          myq1            
          

    """

    args      = """--delq myq1 myq2 myq3"""
    exp_rs    = 0

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_stopq_option_1():
    """
    cqadm test run: stopq_option_1

        Command Output:
          At least on jobid or queue name must be supplied
          

    """

    args      = """--stopq"""
    exp_rs    = 256

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_stopq_option_2():
    """
    cqadm test run: stopq_option_2

        Command Output:
          Failed to match any jobs or queues
          

    """

    args      = """--stopq myq1 myq2 myq3"""
    exp_rs    = 0

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_startq_option_1():
    """
    cqadm test run: startq_option_1

        Command Output:
          At least on jobid or queue name must be supplied
          

    """

    args      = """--startq"""
    exp_rs    = 256

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_startq_option_2():
    """
    cqadm test run: startq_option_2

        Command Output:
          Failed to match any jobs or queues
          

    """

    args      = """--startq myq1 myq2 myq3"""
    exp_rs    = 0

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_drainq_option_1():
    """
    cqadm test run: drainq_option_1

        Command Output:
          At least on jobid or queue name must be supplied
          

    """

    args      = """--drainq"""
    exp_rs    = 256

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_drainq_option_2():
    """
    cqadm test run: drainq_option_2

        Command Output:
          Failed to match any jobs or queues
          

    """

    args      = """--drainq myq1 myq2 myq3"""
    exp_rs    = 0

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_killq_option_1():
    """
    cqadm test run: killq_option_1

        Command Output:
          At least on jobid or queue name must be supplied
          

    """

    args      = """--killq"""
    exp_rs    = 256

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_killq_option_2():
    """
    cqadm test run: killq_option_2

        Command Output:
          Failed to match any jobs or queues
          

    """

    args      = """--killq myq1 myq2 myq3"""
    exp_rs    = 0

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_policy_option_1():
    """
    cqadm test run: policy_option_1

        Command Output:
          Usage: cqadm.py [options] <jobid> <jobid> OR <queue> <queue>
          
          cqadm.py: error: --policy option requires an argument
          

    """

    args      = """--policy"""
    exp_rs    = 512

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_policy_option_2():
    """
    cqadm test run: policy_option_2

        Command Output:
          At least on jobid or queue name must be supplied
          

    """

    args      = """--policy 'mypolicy'"""
    exp_rs    = 256

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_policy_option_3():
    """
    cqadm test run: policy_option_3

        Command Output:
          Failed to match any jobs or queues
          

    """

    args      = """--policy 'mypolicy' myq1 myq2"""
    exp_rs    = 0

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_setq_option_1():
    """
    cqadm test run: setq_option_1

        Command Output:
          Usage: cqadm.py [options] <jobid> <jobid> OR <queue> <queue>
          
          cqadm.py: error: --setq option requires an argument
          

    """

    args      = """--setq"""
    exp_rs    = 512

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_setq_option_2():
    """
    cqadm test run: setq_option_2

        Command Output:
          At least on jobid or queue name must be supplied
          

    """

    args      = """--setq 'a=b b=c a=c'"""
    exp_rs    = 256

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_setq_option_3():
    """
    cqadm test run: setq_option_3

        Command Output:
          Failed to match any jobs or queues
          

    """

    args      = """--setq 'a=b b=c a=c' myq1 myq2"""
    exp_rs    = 0

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_unsetq_option_1():
    """
    cqadm test run: unsetq_option_1

        Command Output:
          Usage: cqadm.py [options] <jobid> <jobid> OR <queue> <queue>
          
          cqadm.py: error: --unsetq option requires an argument
          

    """

    args      = """--unsetq"""
    exp_rs    = 512

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_unsetq_option_2():
    """
    cqadm test run: unsetq_option_2

        Command Output:
          At least on jobid or queue name must be supplied
          

    """

    args      = """--unsetq 'a b a'"""
    exp_rs    = 256

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_unsetq_option_3():
    """
    cqadm test run: unsetq_option_3

        Command Output:
          Failed to match any jobs or queues
          

    """

    args      = """--unsetq 'a b a' myq1 myq2"""
    exp_rs    = 0

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_setjobid_option_1():
    """
    cqadm test run: setjobid_option_1

        Command Output:
          Usage: cqadm.py [options] <jobid> <jobid> OR <queue> <queue>
          
          cqadm.py: error: -j option requires an argument
          

    """

    args      = """-j"""
    exp_rs    = 512

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_setjobid_option_2():
    """
    cqadm test run: setjobid_option_2

        Command Output:
          Usage: cqadm.py [options] <jobid> <jobid> OR <queue> <queue>
          
          cqadm.py: error: --setjobid option requires an argument
          

    """

    args      = """--setjobid"""
    exp_rs    = 512

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_setjobid_option_3():
    """
    cqadm test run: setjobid_option_3

        Command Output:
          

    """

    args      = """-j 1"""
    exp_rs    = 0

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_setjobid_option_4():
    """
    cqadm test run: setjobid_option_4

        Command Output:
          

    """

    args      = """--setjobid 1"""
    exp_rs    = 0

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_setjobid_option_5():
    """
    cqadm test run: setjobid_option_5

        Command Output:
          

    """

    args      = """-j 1 --setjobid 2"""
    exp_rs    = 0

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_run_option_1():
    """
    cqadm test run: run_option_1

        Command Output:
          Usage: cqadm.py [options] <jobid> <jobid> OR <queue> <queue>
          
          cqadm.py: error: --run option requires an argument
          

    """

    args      = """--run"""
    exp_rs    = 512

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_run_option_2():
    """
    cqadm test run: run_option_2

        Command Output:
          At least on jobid or queue name must be supplied
          

    """

    args      = """--run mayaguez"""
    exp_rs    = 256

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_hold_option_1():
    """
    cqadm test run: hold_option_1

        Command Output:
          At least on jobid or queue name must be supplied
          

    """

    args      = """--hold"""
    exp_rs    = 256

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_hold_option_2():
    """
    cqadm test run: hold_option_2

        Command Output:
          Failed to match any jobs or queues
          

    """

    args      = """--hold 1 2 3"""
    exp_rs    = 0

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_hold_option_3():
    """
    cqadm test run: hold_option_3

        Command Output:
          
          cqadm.py -d --hold 1 2 3
          
          component: "queue-manager.set_jobs", defer: False
            set_jobs(
               [{'admin_hold': False, 'tag': 'job', 'location': '*', 'walltime': '*', 'jobid': 1}, {'admin_hold': False, 'tag': 'job', 'location': '*', 'walltime': '*', 'jobid': 2}, {'admin_hold': False, 'tag': 'job', 'location': '*', 'walltime': '*', 'jobid': 3}],
               {'admin_hold': True},
               georgerojas,
               )
          
          
          Failed to match any jobs or queues
          

    """

    args      = """-d --hold  1 2 3"""
    exp_rs    = 0

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_hold_option_4():
    """
    cqadm test run: hold_option_4

        Command Output:
          Failed to match any jobs or queues
          

    """

    args      = """-f --hold  1 2 3"""
    exp_rs    = 0

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_release_option_1():
    """
    cqadm test run: release_option_1

        Command Output:
          At least on jobid or queue name must be supplied
          

    """

    args      = """--release"""
    exp_rs    = 256

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_release_option_2():
    """
    cqadm test run: release_option_2

        Command Output:
          Failed to match any jobs or queues
          

    """

    args      = """--release 1 2 3"""
    exp_rs    = 0

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_release_option_3():
    """
    cqadm test run: release_option_3

        Command Output:
          
          cqadm.py -d --release 1 2 3
          
          component: "queue-manager.set_jobs", defer: False
            set_jobs(
               [{'admin_hold': True, 'tag': 'job', 'location': '*', 'walltime': '*', 'jobid': 1}, {'admin_hold': True, 'tag': 'job', 'location': '*', 'walltime': '*', 'jobid': 2}, {'admin_hold': True, 'tag': 'job', 'location': '*', 'walltime': '*', 'jobid': 3}],
               {'admin_hold': False},
               georgerojas,
               )
          
          
          Failed to match any jobs or queues
          

    """

    args      = """-d --release 1 2 3"""
    exp_rs    = 0

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_release_option_4():
    """
    cqadm test run: release_option_4

        Command Output:
          Failed to match any jobs or queues
          

    """

    args      = """-f --release 1 2 3"""
    exp_rs    = 0

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_release_and_hold():
    """
    cqadm test run: release_and_hold

        Command Output:
          Attribute admin_hold already set
          

    """

    args      = """--hold --release 1 2 3"""
    exp_rs    = 256

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_queue_option_1():
    """
    cqadm test run: queue_option_1

        Command Output:
          Usage: cqadm.py [options] <jobid> <jobid> OR <queue> <queue>
          
          cqadm.py: error: --queue option requires an argument
          

    """

    args      = """--queue"""
    exp_rs    = 512

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_queue_option_2():
    """
    cqadm test run: queue_option_2

        Command Output:
          At least on jobid or queue name must be supplied
          

    """

    args      = """--queue myq"""
    exp_rs    = 256

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_time_option_1():
    """
    cqadm test run: time_option_1

        Command Output:
          Usage: cqadm.py [options] <jobid> <jobid> OR <queue> <queue>
          
          cqadm.py: error: --time option requires an argument
          

    """

    args      = """--time"""
    exp_rs    = 512

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_time_option_2():
    """
    cqadm test run: time_option_2

        Command Output:
          At least on jobid or queue name must be supplied
          

    """

    args      = """--time 50"""
    exp_rs    = 256

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_time_option_4():
    """
    cqadm test run: time_option_4

        Command Output:
          Failed to match any jobs or queues
          

    """

    args      = """--time 50 1 2 3"""
    exp_rs    = 0

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_combine_getq_and_addq():
    """
    cqadm test run: combine_getq_and_addq

        Command Output:
          Option combinations not allowed with: addq, getq option(s)
          

    """

    args      = """--getq --addq myq1 myq2 myq3"""
    exp_rs    = 256

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_combine_getq_and_setjobid():
    """
    cqadm test run: combine_getq_and_setjobid

        Command Output:
          Option combinations not allowed with: setjobid, getq option(s)
          

    """

    args      = """--getq -j 1 123"""
    exp_rs    = 256

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_combine_time_and_getq():
    """
    cqadm test run: combine_time_and_getq

        Command Output:
          Option combinations not allowed with: getq option(s)
          

    """

    args      = """--time 50 --getq"""
    exp_rs    = 256

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_combine_release_and_getq():
    """
    cqadm test run: combine_release_and_getq

        Command Output:
          Option combinations not allowed with: getq option(s)
          

    """

    args      = """--release --getq 123"""
    exp_rs    = 256

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_combine_setq_with_queue():
    """
    cqadm test run: combine_setq_with_queue

        Command Output:
          Option combinations not allowed with: setq option(s)
          

    """

    args      = """--setq 'a=1 b=2' --queue q 1"""
    exp_rs    = 256

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_combine_addq_and_delq():
    """
    cqadm test run: combine_addq_and_delq

        Command Output:
          Option combinations not allowed with: addq, delq option(s)
          

    """

    args      = """--addq --delq q1 q2"""
    exp_rs    = 256

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_combine_addq_and_stopq():
    """
    cqadm test run: combine_addq_and_stopq

        Command Output:
          Option combinations not allowed with: addq, stopq option(s)
          

    """

    args      = """--stopq --addq q1 q2"""
    exp_rs    = 256

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg

# ---------------------------------------------------------------------------------
def test_cqadm_combine_addq_and_startq():
    """
    cqadm test run: combine_addq_and_startq

        Command Output:
          Option combinations not allowed with: addq, startq option(s)
          

    """

    args      = """--startq --addq q1 q2"""
    exp_rs    = 256

    results = testutils.run_cmd('cqadm.py',args,None) 
    rs      = results[0]
    cmd_out = results[1]

    # Test Pass Criterias
    no_rs_err     = (rs == exp_rs)
    no_fatal_exc  = (cmd_out.find("FATAL EXCEPTION") == -1)

    result = no_rs_err and no_fatal_exc

    errmsg  = "\n\nFailed Data:\n\n" \
        "Return Status %s, Expected Return Status %s\n\n" \
        "Command Output:\n%s\n\n" \
        "Arguments: %s" % (str(rs), str(exp_rs), str(cmd_out), args)

    assert result, errmsg
