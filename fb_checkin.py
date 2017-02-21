from __future__ import with_statement
import contextlib
import sys
import time
import os


from pyke import knowledge_engine, krb_traceback, goal

# Compile and load .krb files in same directory that I'm in (recursively).
#engine = knowledge_engine.engine(__file__)
engine = knowledge_engine.engine(os.getcwd())

fc_goal = goal.compile('fb_checkin.updated_sample_size($node,$value)')

def fc_test(node = 7030):
    '''
        This function runs the forward-chaining example (animalia.krb).
    '''
    engine.reset()      # Allows us to run tests multiple times.

    start_time = time.time()
    engine.activate('fb_checkin_fc')  # Runs all applicable forward-chaining rules.
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time

    print "doing proof"
    with fc_goal.prove(engine, node=node) as gen:
        #print "gen1:",gen
        print "train-test-split:",node
        for vars, plan in gen:
            #print "gen:",gen
            print "%s" % \
                    (vars['value'])
    prove_time = time.time() - fc_end_time
    print
    print "done"
    engine.print_stats()
    print "fc time %.2f, %.0f asserts/sec" % \
          (fc_time, engine.get_kb('fb_checkin').get_stats()[2] / fc_time)
    return vars['value']
    
fc_goal1 = goal.compile('fb_checkin.update_feature($node,$value)')

def fc_test1(node = 'time'):
    '''
        This function runs the forward-chaining example (animalia.krb).
    '''
    engine.reset()      # Allows us to run tests multiple times.

    start_time = time.time()
    engine.activate('fb_checkin_fc')  # Runs all applicable forward-chaining rules.
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time

    print "doing proof"
    with fc_goal1.prove(engine, node=node) as gen:
        #print "gen1:",gen
        print "new feature:",node
        for vars, plan in gen:
            #print "gen:",gen
            print (vars['value'])
    prove_time = time.time() - fc_end_time
    print
    print "done"
    engine.print_stats()
    print "fc time %.2f, %.0f asserts/sec" % \
          (fc_time, engine.get_kb('fb_checkin').get_stats()[2] / fc_time)
    return vars['value']

fc_goal2 = goal.compile('fb_checkin.find_threshold($value)')

def fc_test2():
    '''
        This function runs the forward-chaining example (animalia.krb).
    '''
    engine.reset()      # Allows us to run tests multiple times.

    start_time = time.time()
    engine.activate('fb_checkin_fc')  # Runs all applicable forward-chaining rules.
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time

    print "doing proof"
    with fc_goal2.prove(engine) as gen:
        #print "gen1:",gen
        print "threshold accuracy:"
        for vars, plan in gen:
            #print "gen:",gen
            print (vars['value'])
    prove_time = time.time() - fc_end_time
    print
    print "done"
    engine.print_stats()
    print "fc time %.2f, %.0f asserts/sec" % \
          (fc_time, engine.get_kb('fb_checkin').get_stats()[2] / fc_time)
    return vars['value']