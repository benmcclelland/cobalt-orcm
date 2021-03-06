import time
import pwd
import os
"""
This module is use for generating combo cobalt client commands on a Brooklyn or real system
"""
test_argslist = [
    {"tc_name" : "delete_partions"                     , "command" : "partadm", "args" : "-d '*'"},
    {"tc_name" : "add_partition_ANL_R00_R01_2048"      , "command" : "partadm", "args" : "-a ANL-R00-R01-2048"},
    {"tc_name" : "enable_partition_ANL_R00_R01_2048"   , "command" : "partadm", "args" : "--enable ANL-R00-R01-2048"},
    {"tc_name" : "activate_partition_ANL_R00_R01_2048" , "command" : "partadm", "args" : "--activate ANL-R00-R01-2048"},
    {"tc_name" : "add_partition_ANL_R00_1024"          , "command" : "partadm", "args" : "-a ANL-R00-1024"},
    {"tc_name" : "enable_partition_ANL_R00_1024"       , "command" : "partadm", "args" : "--enable ANL-R00-1024"},
    {"tc_name" : "activate_partition_ANL_R00_1024"     , "command" : "partadm", "args" : "--activate ANL-R00-1024"},
    {"tc_name" : "add_partition_ANL_R01_1024"          , "command" : "partadm", "args" : "-a ANL-R01-1024"},
    {"tc_name" : "enable_partition_ANL_R01_1024"       , "command" : "partadm", "args" : "--enable ANL-R01-1024"},
    {"tc_name" : "activate_partition_ANL_R01_1024"     , "command" : "partadm", "args" : "--activate ANL-R01-1024"},
    {"tc_name" : "add_partition_ANL_R00_M0_512"        , "command" : "partadm", "args" : "-a ANL-R00-M0-512"},
    {"tc_name" : "enable_partition_ANL_R00_M0_512"     , "command" : "partadm", "args" : "--enable ANL-R00-M0-512"},
    {"tc_name" : "activate_partition_ANL_R00_M0_512"   , "command" : "partadm", "args" : "--activate ANL-R00-M0-512"},
    {"tc_name" : "add_partition_ANL_R00_M1_512"        , "command" : "partadm", "args" : "-a ANL-R00-M1-512"},
    {"tc_name" : "enable_partition_ANL_R00_M1_512"     , "command" : "partadm", "args" : "--enable ANL-R00-M1-512"},
    {"tc_name" : "activate_partition_ANL_R00_M1_512"   , "command" : "partadm", "args" : "--activate ANL-R00-M1-512"},
    {"tc_name" : "add_partition_ANL_R01_M0_512"        , "command" : "partadm", "args" : "-a ANL-R01-M0-512"},
    {"tc_name" : "enable_partition_ANL_R01_M0_512"     , "command" : "partadm", "args" : "--enable ANL-R01-M0-512"},
    {"tc_name" : "activate_partition_ANL_R01_M0_512"   , "command" : "partadm", "args" : "--activate ANL-R01-M0-512"},
    {"tc_name" : "list_1"                              , "command" : "partadm", "args" : "-l"},
    {"tc_name" : "delete_default_que"                  , "command" : "cqadm"  , "args" : "--delq default"},
    {"tc_name" : "add_queues"                          , "command" : "cqadm"  , "args" : "--addq default q_1 q_2 q_3 q_4"},
    {"tc_name" : "start_default"                       , "command" : "cqadm"  , "args" : "--start default q_1 q_2 q_3 q_4"},
    {"tc_name" : "get_queues"                          , "command" : "cqadm"  , "args" : "--getq"},
    {"tc_name" : "qstat_1"                             , "command" : "qstat"  , "args" : "-Q"},
    {"tc_name" : "add_que_associations_1"              , "command" : "partadm", "args" : """--queue q_1:q_2:q_3:q_4 ANL-R00-R01-2048 ANL-R00-1024"""},
    {"tc_name" : "list_3"                              , "command" : "partadm", "args" : "-l"},
    {"tc_name" : "add_que_associations_2"              , "command" : "partadm", "args" : """--queue q_1:q_2:q_3:q_4 ANL-R01-1024 ANL-R00-M1-512"""},
    {"tc_name" : "list_4"                              , "command" : "partadm", "args" : "-l"},
    {"tc_name" : "add_que_associations_3"              , "command" : "partadm", "args" : """--queue default:q_1 ANL-R00-M0-512"""},
    {"tc_name" : "list_5"                              , "command" : "partadm", "args" : "-l"},
    {"tc_name" : "rmq_1"                               , "command" : "partadm", "args" : """--queue q_3 --rmq ANL-R00-R01-2048 ANL-R00-1024"""},
    {"tc_name" : "list_6"                              , "command" : "partadm", "args" : "-l"},
    {"tc_name" : "rmq_2"                               , "command" : "partadm", "args" : """--queue q_2 --rmq ANL-R00-R01-2048"""},
    {"tc_name" : "list_7"                              , "command" : "partadm", "args" : "-l"},
    {"tc_name" : "appq_1"                              , "command" : "partadm", "args" : """--queue q_3 --appq ANL-R00-R01-2048 ANL-R00-1024"""},
    {"tc_name" : "list_8"                              , "command" : "partadm", "args" : "-l"},
    {"tc_name" : "appq_2"                              , "command" : "partadm", "args" : """--queue q_2 --appq ANL-R00-R01-2048"""},
    {"tc_name" : "list_9"                              , "command" : "partadm", "args" : "-l"},
    {"tc_name" : "qstat_2"                             , "command" : "qstat"  , "args" : "-Q"},
    {"tc_name" : "setres_1"                            , "command" : "setres" , "args" : "-n george -s 2022_06_30-10:30 -d 50  -q q_1 ANL-R00-R01-2048"},
    {"tc_name" : "showres_1"                           , "command" : "showres", "args" : "-x"},
    {"tc_name" : "setres_2"                            , "command" : "setres" , "args" : "-n george -m -d 300"},
    {"tc_name" : "showres_2"                           , "command" : "showres", "args" : "-x"},
    {"tc_name" : "setres_3"                            , "command" : "setres" , "args" : "-n david -s 2022_12_1-10:30 -d 50  -q q_1 ANL-R00-R01-2048"},
    {"tc_name" : "showres_3"                           , "command" : "showres", "args" : "-x"},
    {"tc_name" : "qsub_1"                              , "command" : "qsub"   , "args" : "-h -t 50  -n 30 /bin/ls"},
    {"tc_name" : "qsub_2"                              , "command" : "qsub"   , "args" : "-h -t 100 -n 30 /bin/ls"},
    {"tc_name" : "qsub_3"                              , "command" : "qsub"   , "args" : "-h -t 150 -n 30 /bin/ls"},
    {"tc_name" : "qsub_4"                              , "command" : "qsub"   , "args" : "--dep 1:2:3 -t 150 -n 30 /bin/ls"},
    {"tc_name" : "qsub_5"                              , "command" : "qsub"   , "args" : "--dep 1:2:3:4:60 -t 150 -n 30 /bin/ls"},
    {"tc_name" : "qstat_3"                             , "command" : "qstat"  , "args" : ""},
    {"tc_name" : "qalter_1"                            , "command" : "qalter" , "args" : "--debug  -t +10 1 2 3 4 5"},
    {"tc_name" : "qstat_4"                             , "command" : "qstat"  , "args" : ""},
    {"tc_name" : "qalter_2"                            , "command" : "qalter" , "args" : "--debug  -t -5 1 2 3 4 5"},
    {"tc_name" : "qstat_5"                             , "command" : "qstat"  , "args" : ""},
    {"tc_name" : "qalter_3"                            , "command" : "qalter" , "args" : "--debug  -t +10 1 2 3 4 5"},
    {"tc_name" : "qstat_6"                             , "command" : "qstat"  , "args" : ""},
    {"tc_name" : "qrls_1"                              , "command" : "qrls"   , "args" : "-d 1 2 3 4 5"},
    {"tc_name" : "qstat_7"                             , "command" : "qstat"  , "args" : ""},
    {"tc_name" : "qrls_2"                              , "command" : "qrls"   , "args" : "-d --dep 4 5"},
    {"tc_name" : "qstat_8"                             , "command" : "qstat"  , "args" : ""},
    {"tc_name" : "qsub_6"                              , "command" : "qsub"   , "args" : "--debug -t 150 -n 30 /bin/ls"},
    {"tc_name" : "qsub_7"                              , "command" : "qsub"   , "args" : "--debug -t 150 -n 30 /bin/ls"},
    {"tc_name" : "qstat_9"                             , "command" : "qstat"  , "args" : ""},
    {"tc_name" : "qalter_4"                            , "command" : "qalter" , "args" : "--debug  --defer 6 7"},
    {"tc_name" : "qstat_10"                            , "command" : "qstat"  , "args" : ""},
    {"tc_name" : "setres_4"                            , "command" : "setres" , "args" : "-n res1 -s 2032_12_1-10:30 -d 50  -q q_1 ANL-R00-R01-2048 ANL-R00-1024"},
    {"tc_name" : "setres_5"                            , "command" : "setres" , "args" : "-n res2 -s 2033_12_1-10:30 -d 50  -q q_1 ANL-R01-1024 ANL-R00-M0-512"},
    {"tc_name" : "showres_4"                           , "command" : "showres", "args" : "-x"},
    {"tc_name" : "releaseres_1"                        , "command" : "releaseres" , "args" : "-d res1 res2 george", },
    {"tc_name" : "setres_6"                            , "command" : "setres" , "args" : "-n r1 -u <USER> -s 2033_12_1-10:30 -d 50 -q q_1 ANL-R01-1024 ANL-R00-M0-512"},
    {"tc_name" : "setres_7"                            , "command" : "setres" , "args" : "-n r2 -u <USER> -s 2033_12_2-10:30 -d 50 -q q_1 ANL-R01-1024 ANL-R00-M0-512"},
    {"tc_name" : "setres_8"                            , "command" : "setres" , "args" : "-n rc1 -u <USER> -s 2033_12_3-10:30 -d 50 -c 72 -q q_1 ANL-R01-1024 ANL-R00-M0-512"},
    {"tc_name" : "setres_9"                            , "command" : "setres" , "args" : "-n rc2 -u <USER> -s 2033_12_4-10:30 -d 50 -c 72 -q q_1 ANL-R01-1024 ANL-R00-M0-512"},
    {"tc_name" : "showres_5"                           , "command" : "showres", "args" : "-x"},
    {"tc_name" : "userres_1"                           , "command" : "userres", "args" : "r1 r2"},
    {"tc_name" : "userres_2"                           , "command" : "userres", "args" : "rc1 rc2"},
    {"tc_name" : "releaseres_2"                        , "command" : "releaseres" , "args" : "-d rc1 rc2", },
    {"tc_name" : "setres_10"                           , "command" : "setres" , "args" : "-n r1 -s 2033_12_1-10:30 -d 50 -q q_1 ANL-R01-1024 ANL-R00-M0-512"},
    {"tc_name" : "userres_3"                           , "command" : "userres", "args" : "r1 r2"},
    {"tc_name" : "showres_6"                           , "command" : "showres", "args" : "-x"},
    {"tc_name" : "releaseres_3"                        , "command" : "releaseres" , "args" : "-d r1", },
    {"tc_name" : "showres_7"                           , "command" : "showres", "args" : "-x"},
    {"tc_name" : "setres_11"                           , "command" : "setres" , "args" : "-n r1 -s now -d 50 -q q_1 ANL-R01-1024 ANL-R00-M0-512"},
    {"tc_name" : "releaseres_4"                        , "command" : "releaseres" , "args" : "-d r1", },
    {"tc_name" : "qsub_8"                              , "command" : "qsub"   , "args" : """--env "A=one:B=two:C=x\=1\:y\=2\:z\=3:D=four" -t 150 -n 30 -d /bin/ls"""},
    {"tc_name" : "qsub_9"                              , "command" : "qsub"   , "args" : """-t 50 -n 30 -h /bin/ls""", },
    {"tc_name" : "qstat_10"                            , "command" : "qstat"  , "args" : "-f", },
    {"tc_name" : "cqadm_1"                             , "command" : "cqadm"  , "args" : "--admin-hold 9", },
    {"tc_name" : "qstat_11"                            , "command" : "qstat"  , "args" : "-f", },
    {"tc_name" : "cqadm_2"                             , "command" : "cqadm"  , "args" : "--user-release 9", },
    {"tc_name" : "qstat_12"                            , "command" : "qstat"  , "args" : "-f", },
    {"tc_name" : "cqadm_3"                             , "command" : "cqadm"  , "args" : "--user-hold 9", },
    {"tc_name" : "qstat_13"                            , "command" : "qstat"  , "args" : "-f", },
    {"tc_name" : "cqadm_4"                             , "command" : "cqadm"  , "args" : "--admin-release 9", },
    {"tc_name" : "qstat_14"                            , "command" : "qstat"  , "args" : "-f", },
    {"tc_name" : "cqadm_5"                             , "command" : "cqadm"  , "args" : "--hold 9", },
    {"tc_name" : "qstat_15"                            , "command" : "qstat"  , "args" : "-f", },
    {"tc_name" : "cqadm_6"                             , "command" : "cqadm"  , "args" : "--user-release 9", },
    {"tc_name" : "qstat_16"                            , "command" : "qstat"  , "args" : "-f", },
    {"tc_name" : "cqadm_7"                             , "command" : "cqadm"  , "args" : "--release 9", },
    {"tc_name" : "qstat_17"                            , "command" : "qstat"  , "args" : "-f", },
    {"tc_name" : "setres_12"                           , "command" : "setres" , "args" : "-n r1 -s 2014-01-01-10:30 -u '*' -d 50 -q q_1 ANL-R01-1024 ANL-R00-M0-512", },
    {"tc_name" : "showres_8"                           , "command" : "showres", "args" : ""},
    {"tc_name" : "setres_13"                           , "command" : "setres" , "args" : "-m -n r1 -u <USER>", },
    {"tc_name" : "showres_9"                           , "command" : "showres", "args" : ""},
    {"tc_name" : "setres_14"                           , "command" : "setres" , "args" : "-m -n r1 -u '*'", },
    {"tc_name" : "showres_10"                          , "command" : "showres", "args" : ""},
    {"tc_name" : "releaseres_5"                        , "command" : "releaseres" , "args" : "-d r1", },
    {"tc_name" : "showres_11"                          , "command" : "showres", "args" : ""},
    {"tc_name" : "setres_15"                           , "command" : "setres" , "args" : "-n r1 -s 2014-01-01-10:30 -u '*' -d 50 -q q_1 -p ANL-R01-1024:ANL-R00-M0-512 ANL-R00-R01-2048", },
    {"tc_name" : "showres_12"                          , "command" : "showres", "args" : ""},
    {"tc_name" : "releaseres_6"                        , "command" : "releaseres" , "args" : "-d r1", },
    {"tc_name" : "showres_13"                          , "command" : "showres", "args" : ""},
    {"tc_name" : "qsub_10"                             , "command" : "qsub"   , "args" : """--jobname "myjob_\$jobid" --env "myenv=myvar_\$jobid" -t 50 -n 30 /bin/ls""", },
    {"tc_name" : "qstat_11"                            , "command" : "qstat"  , "args" : "-f -l 10", },
    {"tc_name" : "qsub_11"                             , "command" : "qsub"   , "args" : """--jobname "myjob_\$jobid" -o "myout_\$jobid" -t 50 -n 30 /bin/ls""", },
    {"tc_name" : "qstat_12"                            , "command" : "qstat"  , "args" : "-f -l 11", },
    {"tc_name" : "qsub_12"                             , "command" : "qsub"   , "args" : """-o "myout_\$jobid" -e "myerr_\$jobid" --debuglog mydebug_\$jobid -t 50 -n 30 /bin/ls""", },
    {"tc_name" : "qstat_13"                            , "command" : "qstat"  , "args" : "-f -l 12", },
    {"tc_name" : "qsub_13"                             , "command" : "qsub"   , "args" : """-O "outpref_\$jobid" -t 50 -n 30 /bin/ls""", },
    {"tc_name" : "qstat_14"                            , "command" : "qstat"  , "args" : "-f -l 13", },
    {"tc_name" : "qsub_14"                             , "command" : "qsub"   , "args" : """--jobname "myjob_\$jobid" -O "outpref_\$jobid" -t 50 -n 30 /bin/ls""", },
    {"tc_name" : "qstat_15"                            , "command" : "qstat"  , "args" : "-f -l 14", },
    {"tc_name" : "qsub_15"                             , "command" : "qsub"   , "args" : """cobalt_script3.sh""", },
    {"tc_name" : "qstat_16"                            , "command" : "qstat"  , "args" : "-f -l 15", },
    {"tc_name" : "qsub_16"                             , "command" : "qsub"   , "args" : """-t 50 -n 30 cobalt_script3.sh""", },
    {"tc_name" : "qstat_17"                            , "command" : "qstat"  , "args" : "-f -l 16", },
    {"tc_name" : "qdel_1"                              , "command" : "qdel"  , "args" : "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16", },
    {"tc_name" : "releaseres_7"                        , "command" : "releaseres" , "args" : "-d david", },
    {"tc_name" : "partadm_add_7"                       , "command" : "partadm", "args" : "-a ANL-R32-R33-2048"},
    {"tc_name" : "partadm_enable_7"                    , "command" : "partadm", "args" : "--enable ANL-R32-R33-2048"},
    {"tc_name" : "partadm_activate_7"                  , "command" : "partadm", "args" : "--activate ANL-R32-R33-2048"},
    {"tc_name" : "partadm_add_8"                       , "command" : "partadm", "args" : "-a ANL-R32-1024"},
    {"tc_name" : "partadm_enable_8"                    , "command" : "partadm", "args" : "--enable ANL-R32-1024"},
    {"tc_name" : "partadm_activate_8"                  , "command" : "partadm", "args" : "--activate ANL-R32-1024"},
    {"tc_name" : "partadm_add_9"                       , "command" : "partadm", "args" : "-a ANL-R32-M0-512"},
    {"tc_name" : "partadm_enable_9"                    , "command" : "partadm", "args" : "--enable ANL-R32-M0-512"},
    {"tc_name" : "partadm_activate_9"                  , "command" : "partadm", "args" : "--activate ANL-R32-M0-512"},
    {"tc_name" : "partadm_add_10"                      , "command" : "partadm", "args" : "-a ANL-R32-M1-512"},
    {"tc_name" : "partadm_enable_10"                   , "command" : "partadm", "args" : "--enable ANL-R32-M1-512"},
    {"tc_name" : "partadm_activate_10"                 , "command" : "partadm", "args" : "--activate ANL-R32-M1-512"},
    {"tc_name" : "partadm_add_11"                      , "command" : "partadm", "args" : "-a ANL-R41-1024"},
    {"tc_name" : "partadm_enable_11"                   , "command" : "partadm", "args" : "--enable ANL-R41-1024"},
    {"tc_name" : "partadm_activate_11"                 , "command" : "partadm", "args" : "--activate ANL-R41-1024"},
    {"tc_name" : "add_queues_q1"                       , "command" : "cqadm"  , "args" : "--addq q1 q2"},
    {"tc_name" : "start_queues_q1"                     , "command" : "cqadm"  , "args" : "--start q1 q2"},
    {"tc_name" : "appq_q1"                             , "command" : "partadm", "args" : """--queue q1 --appq ANL-R32-M0-512"""},
    {"tc_name" : "appq_q2"                             , "command" : "partadm", "args" : """--queue q2 --appq ANL-R32-M1-512"""},
    {"tc_name" : "setres_16"                           , "command" : "setres" , "args" : "-n res1 -s now -u '*' -d 50 -q q2 -p ANL-R32-M1-512", },
    {"tc_name" : "setres_17"                           , "command" : "setres" , "args" : "-n res2 -s now -u '*' -d 50 -p ANL-R41-1024", },
    {"tc_name" : "qsub_17"                             , "command" : "qsub"   , "args" : "-t0 -n 256 -q q1 /bin/ls", },
    {"tc_name" : "qsub_18"                             , "command" : "qsub"   , "args" : "-t0 -n 256 -q q2 /bin/ls", },
    {"tc_name" : "qsub_19"                             , "command" : "qsub"   , "args" : "-t0 -n 1024 -q R.res2 /bin/ls", },
    {"tc_name" : "qstat_18"                            , "command" : "qstat"  , "args" : "", },
    ]
