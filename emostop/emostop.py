'''
Created on 15/5/2015

@author: lm
'''

import numpy as np

class InternalState:

    def __init__(self):
        self.previous_genenation = None

class StoppingCriterion(object):
    '''
    classdocs
    '''

    def __init__(self, progress_indicators, evidence_gatherers, stop_decisors, voting=np.all):
        '''
        Constructor
        '''

        self.progress_indicators = progress_indicators
        self.evidence_gatherers = evidence_gatherers
        self.stop_decisors = stop_decisors
        self.voting = voting

        self.internal_state = InternalState


    def is_end_condition_met(self, population):
        '''Decides if the evolution can/must/should be stopped.'''
        prog_ind_values = [indicator.compute_indicator(population) for indicator in self.progress_indicators]
        evidences = [gatherer.gather_evidence(prog_ind_values) for gatherer in self.evidence_gatherers]
        decisions = [decisor.must_stop(evidences) for decisor in self.stop_decisors]

        return self.voting(decisions), (prog_ind_values, evidences, decisions)

class EvidenceGatherer():

    def gather_evidence(self, prog_inds_values):
        raise NotImplementedError('Method belongs to abstract class')

class ProgressIndicator():

    def compute_indicator(self, population):
        raise NotImplementedError('Method belongs to abstract class')

class StopDecisor():

    def must_stop(self, evidences):
        raise NotImplementedError('Method belongs to abstract class')


class MutualDominationRateIndicator(ProgressIndicator):

    def compute_indicator(self, population):
        if not self.previous_pop:
          self.previous_pop = population
          return np.nan

    def _norm_delta(a,b):


