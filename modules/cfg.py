# -*- coding: utf-8 -*-
# Copyright 2015, 2016, 2017 Ravshello Authors
# License: Apache License 2.0 (see LICENSE or http://apache.org/licenses/LICENSE-2.0.html)

# All references to program name should use this
prog = 'ravshello'

# Version info
__version__ = '1.21.0'
__date__    = '2017/03/07'
version = "{} v{} last mod {}".format(prog, __version__, __date__)

# Defaults
defaultUserCfgDir = '~/.ravshello'
defaultUserCfgFile = 'config.yaml'
defaultAppExpireTime = 120
defaultAppExtendTime = 60

# Some learner mode rules
maxLearnerPublishedApps = 3
maxLearnerActiveVms = 8
maxLearnerExtendTime = 120

# Learner mode can only create apps from blueprints which have
# one of these strings in their description
learnerBlueprintTag = [
    "#is_learner_blueprint",
    "#learner_bp",
    ]

# This will hold the options namespace generated by argparse
opts = None

# This will hold the local username
user = None

# This will hold the RavelloClient object
rClient = None

# This will hold the RavelloCache object
rCache = None

# This will hold the options read from config files
cfgFile = {}
