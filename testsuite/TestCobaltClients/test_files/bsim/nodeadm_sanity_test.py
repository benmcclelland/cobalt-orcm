import testutils

# ---------------------------------------------------------------------------------
def test_nodeadm_args_1():
    """
    nodeadm test run: args_1

        Command Output:
          No arguments provided
          Usage: nodeadm.py [-l] [--down part1 part2] [--up part1 part2]"
          
          Options:
            --version      show program's version number and exit
            -h, --help     show this help message and exit
            -d, --debug    turn on communication debugging
            --down         mark nodes as down
            --up           mark nodes as up (even if allocated)
            --queue=QUEUE  set queue associations
            -l, --list     list node states
          

    """

    args      = ''
    exp_rs    = 256

    results = testutils.run_cmd('nodeadm.py',args,None) 
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
def test_nodeadm_args_2():
    """
    nodeadm test run: args_2

        Command Output:
          Need at least one option
          Usage: nodeadm.py [-l] [--down part1 part2] [--up part1 part2]"
          
          Options:
            --version      show program's version number and exit
            -h, --help     show this help message and exit
            -d, --debug    turn on communication debugging
            --down         mark nodes as down
            --up           mark nodes as up (even if allocated)
            --queue=QUEUE  set queue associations
            -l, --list     list node states
          

    """

    args      = """p1"""
    exp_rs    = 256

    results = testutils.run_cmd('nodeadm.py',args,None) 
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
def test_nodeadm_up_1():
    """
    nodeadm test run: up_1

        Command Output:
          nodeadm is only supported on cluster systems.  Try partlist instead.
          

    """

    args      = """--up p1 p2 p3"""
    exp_rs    = 0

    results = testutils.run_cmd('nodeadm.py',args,None) 
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
def test_nodeadm_up_2():
    """
    nodeadm test run: up_2

        Command Output:
          nodeadm is only supported on cluster systems.  Try partlist instead.
          

    """

    args      = """--up U1 U2 U5 p1"""
    exp_rs    = 0

    results = testutils.run_cmd('nodeadm.py',args,None) 
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
def test_nodeadm_down_1():
    """
    nodeadm test run: down_1

        Command Output:
          nodeadm is only supported on cluster systems.  Try partlist instead.
          

    """

    args      = """--down p1 p2 p3"""
    exp_rs    = 0

    results = testutils.run_cmd('nodeadm.py',args,None) 
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
def test_nodeadm_down_2():
    """
    nodeadm test run: down_2

        Command Output:
          
          nodeadm.py -d --down p1 p2 p3
          
          component: "system.get_implementation", defer: False
            get_implementation(
               )
          
          
          nodeadm is only supported on cluster systems.  Try partlist instead.
          

    """

    args      = """-d --down p1 p2 p3"""
    exp_rs    = 0

    results = testutils.run_cmd('nodeadm.py',args,None) 
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
def test_nodeadm_down_3():
    """
    nodeadm test run: down_3

        Command Output:
          nodeadm is only supported on cluster systems.  Try partlist instead.
          

    """

    args      = """--down D1 D2 D5 p1"""
    exp_rs    = 0

    results = testutils.run_cmd('nodeadm.py',args,None) 
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
def test_nodeadm_list_1():
    """
    nodeadm test run: list_1

        Command Output:
          nodeadm is only supported on cluster systems.  Try partlist instead.
          

    """

    args      = """-l"""
    exp_rs    = 0

    results = testutils.run_cmd('nodeadm.py',args,None) 
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
def test_nodeadm_list_2():
    """
    nodeadm test run: list_2

        Command Output:
          nodeadm is only supported on cluster systems.  Try partlist instead.
          

    """

    args      = """-l p1"""
    exp_rs    = 0

    results = testutils.run_cmd('nodeadm.py',args,None) 
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
def test_nodeadm_queue_1():
    """
    nodeadm test run: queue_1

        Command Output:
          No arguments provided
          Usage: nodeadm.py [-l] [--down part1 part2] [--up part1 part2]"
          
          Options:
            --version      show program's version number and exit
            -h, --help     show this help message and exit
            -d, --debug    turn on communication debugging
            --down         mark nodes as down
            --up           mark nodes as up (even if allocated)
            --queue=QUEUE  set queue associations
            -l, --list     list node states
          

    """

    args      = """--queue QU1"""
    exp_rs    = 256

    results = testutils.run_cmd('nodeadm.py',args,None) 
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
def test_nodeadm_queue_2():
    """
    nodeadm test run: queue_2

        Command Output:
          nodeadm is only supported on cluster systems.  Try partlist instead.
          

    """

    args      = """--queue "QU1 QD1" U1 D1 P1"""
    exp_rs    = 0

    results = testutils.run_cmd('nodeadm.py',args,None) 
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
