import logging
import traceback
import sys
import time
import inspect
import types


__author__ = 'Bauyrzhan Ospan'
__email__ = 'main@cleverest.tech'
__copyright__ = 'Copyright (c) 2022-2027 Bauyrzhan Ospan'
__license__ = 'MIT'
__version__ = '0.0.1'
__url__ = 'https://github.com/bauyrzhanospan/cleverest_debugger'


def debug(func):
    def wrapper(*args, **kwargs):
        if not isinstance(func, types.FunctionType):
            raise TypeError('Only functions or methods INSIDE a class can be debugged')
        logging.getLogger().setLevel(logging.DEBUG)
        inner_logger = logging.getLogger("debugger" + " of " + func.__name__)
        inner_logger.setLevel(logging.DEBUG)
        console = logging.StreamHandler()
        console.setFormatter(logging.Formatter('%(asctime)15s %(name)10s %(funcName)30s on line %(lineno)10s: %(message)s'))
        inner_logger.addHandler(console)
        try:
            inner_logger.debug('='*40)
            inner_logger.debug(f"Calling [{type(func)}]{func.__name__}:")
            args_names = list(inspect.getfullargspec(func)[0])
            args_list = []
            if len(args_names) > 0:
                if len(args) > 0:
                    args = list(args)

                    if len(args) > (len(args_names) - len(kwargs)):
                        args.pop(0)
                    
                    for i in range(len(args)):
                        args_list.append({args_names[i]: args[i]})
                if len(kwargs) > 0:
                    for key, value in kwargs.items():
                        args_list.append({key: value})
            if len(args_list) > 0:
                inner_logger.debug(f"There are {len(args_list)} arguments:")
                for dicts in args_list:
                    for key, value in dicts.items():
                        inner_logger.debug(f"\t{key}: [{type(value)}] {value}")
            start = time.time()
            result = func(*args, **kwargs)
            inner_logger.debug(f"Running {func.__name__} takes: {time.time() - start:.5f}")
            if result:
                inner_logger.debug(f"Result is: [{type(result)}]{result}")
            else:
                inner_logger.debug(f"There is no return.")
        except BaseException as ex:
            ex_type, ex_value, ex_traceback = sys.exc_info()
            trace_back = traceback.extract_tb(ex_traceback)
            stack_trace = list()
            for trace in trace_back:
                stack_trace.append("File : %s , Line : %d, Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))
            inner_logger.error("Exception type : %s " % ex_type.__name__)
            inner_logger.error("Exception message : %s" %ex_value)
            inner_logger.error("Stack trace : %s" %stack_trace)
        
        inner_logger.debug('='*40)
        del inner_logger
    
    return wrapper

