# fb_checkin_fc_fc.py

from __future__ import with_statement
from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def prior(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('fb_checkin', 'prior', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('fb_checkin', 'update_prior',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def inc_num_samples(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('fb_checkin', 'inc_num_samples', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('fb_checkin', 'sample_size',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        engine.assert_('fb_checkin', 'update_inc_num_samples',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def inc_num_features(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('fb_checkin', 'inc_num_features', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('fb_checkin', 'feature',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        engine.assert_('fb_checkin', 'update_inc_num_features',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def accuracy(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('fb_checkin', 'accuracy', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('fb_checkin', 'update_accuracy',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def sample_size(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('fb_checkin', 'sample_size', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('fb_checkin', 'updated_sample_size',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def feature(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('fb_checkin', 'feature', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('fb_checkin', 'update_feature',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def threshold(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('fb_checkin', 'threshold', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('fb_checkin', 'find_threshold',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('fb_checkin_fc')
  
  fc_rule.fc_rule('prior', This_rule_base, prior,
    (('fb_checkin', 'prior',
      (contexts.variable('node'),
       contexts.variable('value'),),
      False),),
    (contexts.variable('node'),
     pattern.pattern_literal(0),))
  
  fc_rule.fc_rule('inc_num_samples', This_rule_base, inc_num_samples,
    (('fb_checkin', 'inc_num_samples',
      (contexts.variable('node'),
       contexts.variable('value'),
       contexts.variable('prob'),),
      False),),
    (contexts.variable('node'),
     contexts.variable('value'),
     pattern.pattern_literal(0),))
  
  fc_rule.fc_rule('inc_num_features', This_rule_base, inc_num_features,
    (('fb_checkin', 'inc_num_features',
      (contexts.variable('node'),
       contexts.variable('value'),
       contexts.variable('prob'),),
      False),),
    (contexts.variable('node'),
     contexts.variable('value'),
     pattern.pattern_literal(0),))
  
  fc_rule.fc_rule('accuracy', This_rule_base, accuracy,
    (('fb_checkin', 'accuracy',
      (contexts.variable('new_value'),),
      False),),
    (contexts.variable('new_value'),))
  
  fc_rule.fc_rule('sample_size', This_rule_base, sample_size,
    (('fb_checkin', 'sample_size',
      (contexts.variable('node'),
       contexts.variable('value'),),
      False),),
    (contexts.variable('node'),
     contexts.variable('value'),))
  
  fc_rule.fc_rule('feature', This_rule_base, feature,
    (('fb_checkin', 'feature',
      (contexts.variable('node'),
       contexts.variable('value'),),
      False),),
    (contexts.variable('node'),
     contexts.variable('value'),))
  
  fc_rule.fc_rule('threshold', This_rule_base, threshold,
    (('fb_checkin', 'threshold',
      (contexts.variable('value'),),
      False),),
    (contexts.variable('value'),))


Krb_filename = '../fb_checkin_fc.krb'
Krb_lineno_map = (
    ((13, 17), (3, 3)),
    ((18, 20), (5, 5)),
    ((29, 33), (9, 9)),
    ((34, 36), (11, 11)),
    ((37, 40), (12, 12)),
    ((49, 53), (16, 16)),
    ((54, 56), (18, 18)),
    ((57, 60), (19, 19)),
    ((69, 73), (23, 23)),
    ((74, 75), (25, 25)),
    ((84, 88), (29, 29)),
    ((89, 91), (31, 31)),
    ((100, 104), (35, 35)),
    ((105, 107), (37, 37)),
    ((116, 120), (41, 41)),
    ((121, 122), (43, 43)),
)
