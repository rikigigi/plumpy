# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod, abstractproperty


class ProcessRecord(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def pid(self):
        """
        The id assigned to this process.
        :return: The process id.
        """
        pass

    @abstractproperty
    def process_class(self):
        """
        The fully qualified string for the name of the process class.
        :return:
        """
        pass

    @abstractproperty
    def inputs(self):
        pass

    @abstractproperty
    def last_saved(self):
        """
        The point this record was last saved to backing storage.
        :return:
        """
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def create_checkpoint(self, exec_engine, process, wait_on=None):
        pass

    @abstractmethod
    def has_checkpoint(self):
        pass

    @abstractmethod
    def create_process_from_checkpoint(self):
        """
        Create the process from the last checkpoint.

        :precondition: has_checkpoint() is True
        :return: An instance of a Process class with its state set to that
        when the checkpoint was created.
        """
        pass

    @abstractmethod
    def create_wait_on_from_checkpoint(self, exec_engine):
        """
        Create the wait_on from the last checkpoint.

        :precondition: has_checkpoint() is True
        :param exec_engine:
        :return: An instance of a WaitOn class with its state set to that
        when the checkpoint was created.
        """
        pass

