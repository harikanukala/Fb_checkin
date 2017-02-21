# animalia_fc_fc.py

from __future__ import with_statement
from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def gives_milk(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('animalia', 'gives_milk', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('animalia', 'animal_kind',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),
                        rule.pattern(3).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def have_feathers(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('animalia', 'have_feathers', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('animalia', 'animal_kind',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),
                        rule.pattern(3).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def eats_meat(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('animalia', 'eats_meat', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('animalia', 'animal_kind',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),
                        rule.pattern(3).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def can_swim(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('animalia', 'can_swim', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('animalia', 'animal_kind',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),
                        rule.pattern(3).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def lays_eggs(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('animalia', 'lays_eggs', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('animalia', 'animal_kind',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),
                        rule.pattern(3).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def has_hair(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('animalia', 'has_hair', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('animalia', 'animal_kind',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),
                        rule.pattern(3).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def have_scales(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('animalia', 'have_scales', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('animalia', 'animal_kind',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),
                        rule.pattern(3).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def has_antenna(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('animalia', 'has_antenna', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('animalia', 'animal_kind',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),
                        rule.pattern(3).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def have_webbed_feet(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('animalia', 'have_webbed_feet', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('animalia', 'animal_kind',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),
                        rule.pattern(3).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def find_animal_feature(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('animalia', 'animal_kind', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('animalia', 'find_animal_kind',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('animalia_fc')
  
  fc_rule.fc_rule('gives_milk', This_rule_base, gives_milk,
    (('animalia', 'gives_milk',
      (contexts.variable('animal'),
       contexts.variable('type'),),
      False),),
    (contexts.variable('animal'),
     contexts.variable('type'),
     pattern.pattern_literal('mammal'),
     pattern.pattern_literal('gives_milk'),))
  
  fc_rule.fc_rule('have_feathers', This_rule_base, have_feathers,
    (('animalia', 'have_feathers',
      (contexts.variable('animal'),
       contexts.variable('type'),),
      False),),
    (contexts.variable('animal'),
     contexts.variable('type'),
     pattern.pattern_literal('bird'),
     pattern.pattern_literal('have_feathers'),))
  
  fc_rule.fc_rule('eats_meat', This_rule_base, eats_meat,
    (('animalia', 'eats_meat',
      (contexts.variable('animal'),
       contexts.variable('type'),),
      False),),
    (contexts.variable('animal'),
     contexts.variable('type'),
     pattern.pattern_literal('carnivore'),
     pattern.pattern_literal('eats_meat'),))
  
  fc_rule.fc_rule('can_swim', This_rule_base, can_swim,
    (('animalia', 'can_swim',
      (contexts.variable('animal'),
       contexts.variable('type'),),
      False),),
    (contexts.variable('animal'),
     contexts.variable('type'),
     pattern.pattern_literal('aquatic'),
     pattern.pattern_literal('can_swim'),))
  
  fc_rule.fc_rule('lays_eggs', This_rule_base, lays_eggs,
    (('animalia', 'lays_eggs',
      (contexts.variable('animal'),
       contexts.variable('type'),),
      False),),
    (contexts.variable('animal'),
     contexts.variable('type'),
     pattern.pattern_literal('bird'),
     pattern.pattern_literal('lays_eggs'),))
  
  fc_rule.fc_rule('has_hair', This_rule_base, has_hair,
    (('animalia', 'has_hair',
      (contexts.variable('animal'),
       contexts.variable('type'),),
      False),),
    (contexts.variable('animal'),
     contexts.variable('type'),
     pattern.pattern_literal('mammal'),
     pattern.pattern_literal('has_hair'),))
  
  fc_rule.fc_rule('have_scales', This_rule_base, have_scales,
    (('animalia', 'have_scales',
      (contexts.variable('animal'),
       contexts.variable('type'),),
      False),),
    (contexts.variable('animal'),
     contexts.variable('type'),
     pattern.pattern_literal('aquatic'),
     pattern.pattern_literal('have_scales'),))
  
  fc_rule.fc_rule('has_antenna', This_rule_base, has_antenna,
    (('animalia', 'has_antenna',
      (contexts.variable('animal'),
       contexts.variable('type'),),
      False),),
    (contexts.variable('animal'),
     contexts.variable('type'),
     pattern.pattern_literal('insect'),
     pattern.pattern_literal('has_antenna'),))
  
  fc_rule.fc_rule('have_webbed_feet', This_rule_base, have_webbed_feet,
    (('animalia', 'have_webbed_feet',
      (contexts.variable('animal'),
       contexts.variable('type'),),
      False),),
    (contexts.variable('animal'),
     contexts.variable('type'),
     pattern.pattern_literal('amphibian'),
     pattern.pattern_literal('have_webbed_feet'),))
  
  fc_rule.fc_rule('find_animal_feature', This_rule_base, find_animal_feature,
    (('animalia', 'animal_kind',
      (contexts.variable('animal'),
       contexts.variable('type'),
       contexts.variable('kind'),
       contexts.variable('feature'),),
      False),),
    (contexts.variable('animal'),
     contexts.variable('feature'),
     contexts.variable('kind'),))


Krb_filename = '../../Week_4/animalia/animalia_fc.krb'
Krb_lineno_map = (
    ((13, 17), (3, 3)),
    ((18, 22), (5, 5)),
    ((31, 35), (9, 9)),
    ((36, 40), (11, 11)),
    ((49, 53), (15, 15)),
    ((54, 58), (17, 17)),
    ((67, 71), (21, 21)),
    ((72, 76), (23, 23)),
    ((85, 89), (27, 27)),
    ((90, 94), (29, 29)),
    ((103, 107), (33, 33)),
    ((108, 112), (35, 35)),
    ((121, 125), (39, 39)),
    ((126, 130), (41, 41)),
    ((139, 143), (45, 45)),
    ((144, 148), (47, 47)),
    ((157, 161), (51, 51)),
    ((162, 166), (53, 53)),
    ((175, 179), (57, 57)),
    ((180, 183), (59, 59)),
)
